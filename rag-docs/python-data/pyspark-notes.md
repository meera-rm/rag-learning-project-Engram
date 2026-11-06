---
title: PySpark and Spark internals — study notes
topic: python-data
source_type: my-notes
note_kind: study-notes
---

# PySpark and Spark Internals — Study Notes

## What Spark is

Apache Spark processes large datasets **in parallel across a cluster**. PySpark is its Python API. Data is split into **partitions**, and each partition is processed by a task on some machine.

## Architecture

| Part | Role |
| --- | --- |
| **Driver** | Runs your program, builds the plan, schedules tasks |
| **Executors** | Processes on worker machines that run tasks and hold cached data |
| **Cluster manager** | Allocates resources — YARN, Kubernetes, Spark standalone (or a managed platform such as Databricks or EMR) |
| **SparkSession** | Your entry point (wraps the older `SparkContext`) |

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("orders-etl").getOrCreate()
```

## Reading data and schemas

```python
# Schema inference: convenient, but reads data an extra time and may guess wrong
df = spark.read.csv("s3://bucket/orders/", header=True, inferSchema=True)

# Explicit schema: faster and safer in production
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
schema = StructType([
    StructField("order_id", StringType(), False),
    StructField("qty", IntegerType(), True),
    StructField("price", DoubleType(), True),
])
df = spark.read.schema(schema).csv("s3://bucket/orders/", header=True)
```

Prefer columnar formats such as **Parquet** or Delta: they store the schema and let Spark read only the needed columns.

## DataFrame operations

```python
from pyspark.sql import functions as F

result = (df
    .filter(F.col("qty") > 0)
    .withColumn("total", F.col("qty") * F.col("price"))
    .drop("internal_note")
    .groupBy("region")
    .agg(F.sum("total").alias("revenue"), F.countDistinct("customer_id").alias("customers"))
    .orderBy(F.desc("revenue")))
```

Use built-in functions (`F.*`) instead of Python UDFs where possible — UDFs move data between the JVM and Python and block optimisations.

## Lazy evaluation: transformations vs actions

- **Transformations** (`filter`, `select`, `withColumn`, `join`, `groupBy`) only build a plan.
- **Actions** (`count`, `show`, `collect`, `write`) trigger execution.

Spark waits until an action so it can optimise the whole plan at once.

## Narrow vs wide transformations and shuffles

| Narrow | Wide |
| --- | --- |
| Each output partition depends on one input partition | Output partitions need data from many input partitions |
| `filter`, `select`, `withColumn` | `groupBy`, `join` (non-broadcast), `distinct`, `orderBy` |
| No data movement | Requires a **shuffle** across the network |

Shuffles are the most expensive part of most jobs (disk + network). They also split a job into **stages**.

## Joins

- Types: `inner`, `left`, `right`, `full`, plus `left_semi` (keep left rows that match) and `left_anti` (keep left rows that don't).
- **Broadcast join**: when one table is small, copy it to every executor so the big table doesn't shuffle.

```python
big.join(F.broadcast(small_lookup), on="country_code", how="left")
```

- **Data skew**: one key with huge numbers of rows makes one task very slow. Fixes: AQE skew handling, salting the key, or handling the hot key separately.

## The Catalyst optimizer

Spark turns your code into a **logical plan**, optimises it, then picks a **physical plan**. Optimisations include:
- **Predicate pushdown**: apply filters as early as possible, even inside the file reader.
- **Column pruning**: read only the columns you use.
- **Constant folding**: compute constant expressions once.
- **Join reordering and strategy selection** (e.g. choosing a broadcast join).

`df.explain(True)` prints the plans — look for `Exchange` (a shuffle) and `BroadcastHashJoin`.

## Adaptive Query Execution (AQE)

AQE re-optimises **during** execution using real statistics: it merges tiny shuffle partitions, switches to a broadcast join when a table turns out small, and splits skewed partitions. It's on by default in modern Spark.

## Partition pruning

If data is stored partitioned by a column (e.g. `.../date=2025-03-01/`), a filter on that column makes Spark skip whole folders.

```python
df.write.partitionBy("date").parquet("s3://bucket/orders_clean/")
```

Choose partition columns with moderate cardinality — partitioning by user id creates millions of tiny files.

## Tungsten

Spark's execution engine work on memory and CPU efficiency: compact binary row format, off-heap memory management and whole-stage code generation (compiling several operators into one function).

## Caching and persistence

```python
df.cache()                         # keep in memory after first use
df.persist(StorageLevel.MEMORY_AND_DISK)
df.unpersist()
```

Cache only when a DataFrame is reused several times; caching everything wastes memory.

## Partitions: repartition vs coalesce

- `repartition(n)` reshuffles to exactly n partitions (can increase or decrease; full shuffle).
- `coalesce(n)` merges partitions to reduce the count without a full shuffle — good before writing to avoid many small files.

## Common performance problems

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| One task runs far longer than others | Skew | AQE, salting, broadcast |
| Thousands of tiny output files | Too many partitions | `coalesce` before writing |
| Out-of-memory on the driver | `collect()` on big data | Write results out or use `take`/`limit` |
| Slow joins | Large shuffle | Broadcast small side, filter early |
| Slow reads | CSV/JSON, no pruning | Parquet/Delta, partitioning |

## Data quality in pipelines

- Remove duplicates: `dropDuplicates(["order_id"])`.
- Handle bad records when reading: `mode="PERMISSIVE"` with a corrupt-record column, `DROPMALFORMED`, or `FAILFAST`.
- Validate: null checks on keys, value ranges, row counts versus the source.

## Incremental loads

Process only new data instead of everything:
1. Store the last processed timestamp (the **watermark**).
2. Read rows with `updated_at > last_watermark`.
3. Merge into the target (upsert with Delta `MERGE`, or append).
4. Save the new watermark only after the write succeeds.

## Write modes

`append` (add rows), `overwrite` (replace — can be limited to affected partitions with dynamic partition overwrite), `ignore`, `error`/`errorifexists` (the default).

## RDDs

The original low-level API (Resilient Distributed Datasets): fault-tolerant through **lineage** (Spark can recompute a lost partition from the steps that created it). DataFrames are preferred today because Catalyst can optimise them; RDDs are for unusual low-level needs.

## Running in production

`spark-submit` with settings for executor count, cores and memory, on YARN, Kubernetes or a managed service. Monitor jobs in the **Spark UI** (stages, tasks, shuffle sizes, skew).
