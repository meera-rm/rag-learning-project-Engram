---
title: MongoDB — study notes
topic: databases
source_type: my-notes
note_kind: study-notes
---

# MongoDB — Study Notes

## What MongoDB is

MongoDB is a **document database**: instead of rows in tables, it stores **documents** (JSON-like objects) inside **collections**. A document can hold nested objects and arrays, so data that belongs together can live together.

| Relational term | MongoDB term |
| --- | --- |
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | `_id` (added automatically if you don't set one) |
| JOIN | `$lookup` (aggregation) or embedding |

Collections are **schema-flexible**: two documents in the same collection can have different fields. That's useful while a product evolves, but you still need discipline (validation rules, consistent field names).

## BSON and document structure

Documents are stored as **BSON** — a binary form of JSON that adds types JSON lacks: dates, 64-bit integers, decimals, binary data and `ObjectId`.

- **`ObjectId`**: a 12-byte id that starts with a timestamp, so ids sort roughly by creation time.
- **Size limit**: a single document can be at most 16 MB — a hint not to grow arrays forever.

```javascript
{
  _id: ObjectId("..."),
  name: "Priya",
  email: "priya@example.com",
  address: { city: "Austin", zip: "78701" },   // embedded document
  skills: ["sql", "python"],                     // array
  joinedAt: ISODate("2025-03-01")
}
```

## CRUD operations

| Operation | Method | Example |
| --- | --- | --- |
| Create | `insertOne`, `insertMany` | `db.users.insertOne({ name: "Sam" })` |
| Read | `find`, `findOne` | `db.users.find({ city: "Austin" })` |
| Update | `updateOne`, `updateMany`, `replaceOne` | `db.users.updateOne({ name: "Sam" }, { $set: { city: "Dallas" } })` |
| Delete | `deleteOne`, `deleteMany` | `db.users.deleteMany({ active: false })` |

`find` returns a **cursor**, which fetches results in batches rather than all at once.

## Query operators and filtering

- **Comparison**: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`
- **Logical**: `$and`, `$or`, `$not`, `$nor`
- **Element**: `$exists` (field present?), `$type` (field type)
- **Array**: `$all` (contains all values), `$elemMatch` (one element matches several conditions), `$size`
- **Text/pattern**: `$regex`, and `$text` with a text index

```javascript
db.orders.find({ total: { $gte: 100 }, status: { $in: ["paid", "shipped"] } })
db.users.find({ $or: [{ city: "Austin" }, { remote: true }] })
```

Dot notation reaches into nested fields: `{ "address.city": "Austin" }`.

## Projection, sorting and pagination

- **Projection** chooses which fields come back: `find({}, { name: 1, email: 1, _id: 0 })`.
- **Sort**: `.sort({ createdAt: -1 })` (1 = ascending, -1 = descending).
- **Pagination**: `.skip(20).limit(10)` works, but `skip` gets slow on large offsets because the server still walks past the skipped documents. **Range-based pagination** ("give me 10 after the last `_id` I saw") scales better.

## Update operators and arrays

| Operator | Does |
| --- | --- |
| `$set` / `$unset` | Set or remove a field |
| `$inc` | Add to a number (atomic counter) |
| `$push` / `$addToSet` | Append to an array (`$addToSet` skips duplicates) |
| `$pull` | Remove matching array elements |
| `$` / `$[]` / `$[id]` | Update the matched element, all elements, or filtered elements of an array |

**Upsert**: `updateOne(filter, update, { upsert: true })` inserts the document if nothing matches.

## Schema design and data modeling

The central question: **embed or reference?**

| Embed (put it inside) | Reference (store an id) |
| --- | --- |
| Data is read together | Data is read separately |
| One-to-few relationships (a user's 3 addresses) | One-to-many with unbounded growth (a user's orders) |
| Child has no life of its own | Child is shared by many parents |
| Single read, atomic update of one document | Avoids huge documents and duplication |

Rule of thumb: **design around how the app queries the data**, not around normalisation. Common patterns include the *subset* pattern (embed only the latest N items), *computed* fields (store a precomputed total) and *bucketing* (group time-series points per hour).

## Aggregation pipeline

An aggregation is a **pipeline of stages**; each stage transforms the documents and passes them on.

| Stage | Like SQL | Does |
| --- | --- | --- |
| `$match` | `WHERE` | Filter (put it early so indexes help) |
| `$project` / `$addFields` | `SELECT` | Reshape or compute fields |
| `$group` | `GROUP BY` | Aggregate with `$sum`, `$avg`, `$min`, `$max`, `$push` |
| `$sort`, `$limit`, `$skip` | `ORDER BY`, `LIMIT` | Order and page |
| `$unwind` | — | Turn one document with an array into one document per element |
| `$lookup` | `LEFT JOIN` | Pull matching documents from another collection |
| `$facet` | — | Run several sub-pipelines on the same input |

```javascript
db.orders.aggregate([
  { $match: { status: "paid" } },
  { $group: { _id: "$customerId", spent: { $sum: "$total" }, orders: { $sum: 1 } } },
  { $sort: { spent: -1 } },
  { $limit: 5 }
])
```

`$lookup` with a sub-pipeline can join on several conditions. Joins are more expensive than in a relational database, which is another reason embedding is often preferred.

## Indexing and query optimisation

- **Single-field**, **compound** (order matters — follow the *equality, sort, range* rule), **multikey** (on arrays), **text**, **geospatial**, **TTL** (auto-delete documents after a time), **unique**, **partial** (only documents matching a filter).
- **`explain("executionStats")`** shows whether a query used an index (`IXSCAN`) or scanned the whole collection (`COLLSCAN`), and how many documents it examined versus returned.
- A **covered query** is answered from the index alone, without reading documents.
- Every index speeds reads but slows writes and uses memory — index for real query patterns.

## Relationships and transactions

- Single-document writes are always **atomic**, which covers many cases when related data is embedded.
- **Multi-document transactions** (on replica sets and sharded clusters) give ACID guarantees across documents and collections. They cost performance, so use them when the business really needs all-or-nothing across documents (e.g. moving money between two account documents).

## Security and authentication

- Turn on **authentication** (don't run open to the network) and use **role-based access control** with least-privilege users.
- **Encrypt in transit** (TLS) and **at rest**; restrict network access (bind to private interfaces, firewall rules, IP allow-lists).
- Validate input on the application side to avoid **query injection** — e.g. never pass a user-supplied object straight into a filter, since `{ "$ne": null }` would match everything.

## Replica sets

A **replica set** is a group of servers holding the same data: one **primary** takes writes; **secondaries** copy its operation log (oplog).

- If the primary fails, the members **elect** a new primary automatically.
- **Write concern** (e.g. `w: "majority"`) decides how many members must confirm a write.
- **Read preference** decides where reads go (primary only, or secondaries for scale, accepting slightly stale data).

## Sharding, performance and backup

- **Sharding** spreads one collection across several replica sets (**shards**) using a **shard key**; a router (`mongos`) sends each query to the right shard(s).
- A good shard key has **high cardinality** and **spreads writes evenly**; a monotonically increasing key (like a timestamp) sends all new writes to one shard — a "hot shard".
- **Hashed** shard keys spread writes; **ranged** keys keep related data together for range queries.
- Backups: snapshots, `mongodump`/`mongorestore` for smaller datasets, or managed backups in a hosted service. Test restores, not just backups.

## MongoDB with Node.js and Mongoose

- The **native driver** gives direct access to collections.
- **Mongoose** adds **schemas**, **validation**, **middleware** (hooks before/after save) and **population** (filling referenced documents, like a join done in the app).

```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
});
const User = mongoose.model("User", userSchema);
await User.create({ name: "Sam", email: "sam@example.com" });
```

## Interview quick checks

- **SQL vs MongoDB?** Fixed schema + joins + strong relational integrity vs flexible documents designed around access patterns, with easy horizontal scaling.
- **When is embedding wrong?** When the embedded array grows without limit, or the child data is shared and updated from many places.
- **Why is my query slow?** Run `explain`; look for `COLLSCAN`, a high examined-to-returned ratio, or a sort that can't use an index.
- **What makes a bad shard key?** Low cardinality or monotonically increasing values.
