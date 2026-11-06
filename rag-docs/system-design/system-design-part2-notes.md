---
title: System design handbook part 2 (messaging, microservices, cloud, observability, distributed internals) — study notes
topic: system-design
source_type: my-notes
note_kind: study-notes
---

# System Design Handbook, Part 2 — Study Notes

Messaging, data patterns, microservices infrastructure, cloud, observability and advanced distributed-systems internals.

## Messaging

| System | Model | Typical use |
| --- | --- | --- |
| Kafka | Distributed append-only log; consumers track their own offsets; messages kept for a retention period | Event streaming, high throughput, replaying history |
| RabbitMQ | Broker with exchanges routing to queues; messages removed when acknowledged | Task queues, flexible routing |
| Amazon SQS | Managed queue (standard: at-least-once; FIFO: ordered, exactly-once processing within limits) | Decoupling AWS services |
| Google Pub/Sub, Amazon SNS | Managed publish/subscribe | Fan-out notifications |
| Pulsar | Log + queue, separate storage layer | Multi-tenant streaming |

### Delivery semantics
- **At-most-once**: may lose messages, never duplicates.
- **At-least-once**: never loses, may duplicate → make consumers **idempotent**.
- **Exactly-once**: hard; achieved within systems like Kafka with transactions, or effectively via idempotent processing.

### Other messaging ideas
- **Dead-letter queue (DLQ)**: messages that keep failing go aside for inspection instead of blocking the queue.
- **Ordering**: usually guaranteed only within a partition/key — send all events for one order with the same key.
- **Backpressure**: slow consumers signal producers to slow down, or the queue buffers.

## Data patterns for distributed systems

- **Event sourcing**: store every change as an event; current state is rebuilt by replaying events. Full audit trail; more complex queries.
- **CQRS**: separate models for writes (commands) and reads (queries), each optimised independently; often paired with event sourcing.
- **Saga**: a long business transaction across services as a series of local transactions, each with a **compensating action** to undo it (e.g. refund if shipping fails). Coordinated by choreography (events) or orchestration (a coordinator).
- **Transactional outbox**: write the business change and an "event to publish" row in the same database transaction; a relay publishes the outbox rows. Avoids "saved to DB but message lost".
- **Change data capture (CDC)**: stream database changes (from the transaction log) to other systems.

## Microservices infrastructure

| Concern | Solution |
| --- | --- |
| Finding services | Service discovery (registry + health checks; DNS-based in Kubernetes) |
| Following a request across services | Distributed tracing (trace id passed along every call) |
| Logs from many services | Centralised logging (structured JSON logs, correlation ids) |
| Service-to-service security, retries, traffic splitting | Service mesh (sidecar proxies such as Envoy; Istio, Linkerd) |
| Configuration and secrets | Central config service, secrets manager, environment variables |
| Turning features on/off without deploys | Feature flags |

### Deployment strategies
- **Rolling**: replace instances gradually.
- **Blue–green**: run the new version beside the old, switch traffic at once, switch back if needed.
- **Canary**: send a small percentage of traffic to the new version, watch metrics, expand.
- **Shadow**: copy live traffic to the new version without returning its responses.

## Cloud and containers

- Compute: VMs (EC2), containers (ECS, Kubernetes/EKS/GKE/AKS), serverless functions (Lambda, Cloud Functions, Azure Functions).
- Storage: object (S3, GCS, Blob), block (EBS), file (EFS); managed databases (RDS, DynamoDB, Cloud SQL, Cosmos DB).
- **Docker** packages an app and its dependencies into an image; **Kubernetes** schedules containers across machines, restarts failed ones, scales them (Horizontal Pod Autoscaler) and provides service networking.
- **Autoscaling** on CPU, memory, queue length or custom metrics; scale-in carefully to avoid dropping in-flight work.

## Architecture styles

- **MVC**: model (data), view (UI), controller (input handling).
- **MVVM**: view model exposes state the view binds to (common in front-end/mobile).
- **Layered**: presentation → business → data.
- **Clean / hexagonal (ports and adapters)**: business logic in the centre, independent of frameworks and databases; adapters connect it to the outside. Easy to test and to swap infrastructure.

## Security attacks to know

XSS, CSRF, SQL injection, **SSRF** (server tricked into fetching internal URLs such as cloud metadata endpoints), clickjacking (hidden frames trick clicks), DDoS (absorbed with CDNs, rate limiting, autoscaling), credential stuffing (reused passwords — use MFA and rate limits). The OWASP Top 10 is the standard checklist.

## Observability

- **Three pillars**: metrics (numbers over time), logs (events), traces (the path of one request).
- Tools: **Prometheus** (collects metrics), **Grafana** (dashboards), **ELK/OpenSearch** (log search), **OpenTelemetry** (vendor-neutral standard for emitting traces, metrics, logs), Jaeger/Zipkin (trace viewers).
- **SLI** = a measured indicator (e.g. % of requests under 300 ms). **SLO** = the target for it (99.9 %). **SLA** = a contract with consequences if missed. The **error budget** is the allowed failure (0.1 %) — spend it on releasing faster, stop releasing when it's gone.
- Golden signals: latency, traffic, errors, saturation.

## Advanced distributed-systems internals

### Consensus
- **Raft**: a leader is elected by majority vote; the leader replicates a log; an entry is committed once a majority stores it. Used by etcd, Consul.
- **Paxos**: the earlier, harder-to-understand family of consensus algorithms.
- Majorities mean a cluster of 5 tolerates 2 failures.

### Distributed transactions
- **Two-phase commit (2PC)**: coordinator asks everyone to *prepare*, then tells everyone to *commit*. Blocks if the coordinator dies at the wrong time.
- **Three-phase commit (3PC)**: adds a step to reduce blocking, rarely used in practice.
- Microservices usually prefer sagas over 2PC.

### Time and ordering
Physical clocks drift, so systems use **logical clocks**: **Lamport clocks** give an order consistent with cause and effect; **vector clocks** can also detect concurrent (conflicting) updates.

### Storage engines
- **Write-ahead log (WAL)**: write the change to an append-only log before applying it, so a crash can be recovered.
- **B-tree**: updates pages in place; great for reads and range scans (most relational databases).
- **LSM-tree**: buffer writes in memory, flush sorted files, merge them in the background (compaction); great for heavy writes (Cassandra, RocksDB). Reads may check several files — Bloom filters help.

### Kafka internals
Topics split into **partitions**; each partition is an ordered log replicated to several brokers with one leader. Consumers in a **consumer group** share partitions (one partition → one consumer in the group). The in-sync replica set decides when a write is safe.

### Stream processing
Tools: Kafka Streams, Flink, Spark Structured Streaming. Concepts: event time vs processing time, **windows** (tumbling, sliding, session), **watermarks** for late data, stateful operators with checkpoints.

### Redis internals
In-memory, mostly single-threaded command execution (simple and fast), data structures (strings, hashes, lists, sets, sorted sets, streams), persistence via snapshots (RDB) and/or append-only file (AOF), replication and Redis Cluster (hash slots) for scaling.

### Migration and reliability patterns
- **Strangler fig**: replace a legacy system piece by piece behind a routing layer until the old system can be removed.
- **Bulkhead** and **backpressure** keep failures and overload contained.
- **Multi-region disaster recovery**: backup/restore (cheapest, slowest), pilot light, warm standby, active–active (fastest, most expensive). Define **RPO** (how much data loss is acceptable) and **RTO** (how long recovery may take).

### Kubernetes extras
Pod networking (every pod has an IP), Services and Ingress for traffic, **operators** (controllers that automate running complex apps like databases), **GitOps** (Git is the source of truth; a tool like Argo CD syncs the cluster to it).

### Cloud best-practice frameworks
**Well-Architected** frameworks group concerns into pillars: operational excellence, security, reliability, performance efficiency, cost optimisation and sustainability.

### Serverless
Pay per execution, automatic scaling, no servers to manage. Watch out for cold starts, execution time limits, vendor lock-in and harder local testing.
