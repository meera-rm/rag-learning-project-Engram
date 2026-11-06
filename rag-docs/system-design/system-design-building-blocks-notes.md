---
title: System design building blocks and trade-offs — study notes
topic: system-design
source_type: my-notes
note_kind: study-notes
---

# System Design Building Blocks and Trade-offs — Study Notes

## Key qualities

- **Scalability**: handle more load by adding resources.
- **Availability**: the share of time the system works (99.9 % ≈ 8.8 hours of downtime a year; 99.99 % ≈ 53 minutes).
- **Latency**: time for one request. **Throughput**: requests handled per second. You can have high throughput with high latency (a slow but wide pipeline).
- **Reliability**: the system keeps doing the right thing despite failures.

## CAP theorem

When a **network partition** happens, a distributed data store must choose:
- **Consistency** — every read sees the latest write (some requests fail), or
- **Availability** — every request gets an answer (possibly stale).

Partitions can't be ruled out, so the real choice is CP vs AP during a partition. A bank balance leans CP; a social media like-count leans AP. **PACELC** adds: *else* (no partition), choose between latency and consistency.

## Building blocks

| Block | What it does | Notes |
| --- | --- | --- |
| Load balancer | Spreads requests across servers | Algorithms: round robin, least connections, consistent hashing; health checks remove dead servers |
| Database | Stores data durably | SQL for relations/transactions; NoSQL for flexible schemas and easy horizontal scale |
| Cache | Keeps hot data in memory | Redis/Memcached; huge latency win; must handle invalidation |
| CDN | Serves static files from edge locations near users | Images, JS, CSS, video |
| Message queue | Decouples producers and consumers | Kafka, RabbitMQ, SQS; absorbs spikes, enables async work |
| Rate limiter | Caps requests per client | Token bucket, leaky bucket, sliding window |
| Index | Speeds lookups at the cost of slower writes | B-tree for ranges, hash for equality |
| Proxy | Forward proxy acts for clients; reverse proxy sits in front of servers | Reverse proxies do TLS, caching, routing |

## Caching

- **Cache-aside** (lazy loading): app checks cache → on miss reads DB and fills cache. Most common.
- **Read-through**: the cache itself loads from the DB on a miss.
- **Write-through**: write to cache and DB together — consistent, slower writes.
- **Write-back (write-behind)**: write to cache, flush to DB later — fast, risk of loss.
- **Eviction policies**: LRU (least recently used), LFU (least frequently used), FIFO, TTL expiry.
- Problems: stale data, **thundering herd** (many misses at once after expiry), cache penetration (requests for keys that never exist — use a Bloom filter or cache negatives).

## Scaling data

- **Replication**: copies of data on several nodes — leader/follower for read scaling and failover.
- **Sharding (partitioning)**: split data across nodes by a key. Range-based (easy range queries, risk of hot spots) vs hash-based (even spread, range queries harder).
- **Consistent hashing**: nodes and keys sit on a hash ring; adding/removing a node only moves the keys next to it. Virtual nodes even out the load.

## Coordination and reliability techniques

| Technique | Purpose |
| --- | --- |
| Consensus (Raft, Paxos) | Nodes agree on one value / leader despite failures |
| Heartbeats | Detect dead nodes |
| Checksums | Detect corrupted data |
| Service discovery | Find healthy instances by name |
| Bloom filter | Fast "definitely not present / maybe present" check using little memory |
| Gossip protocol | Nodes spread state to random peers until everyone knows |

## Classic trade-offs

| Choice | Option A | Option B |
| --- | --- | --- |
| Scaling | Vertical: bigger machine, simple, has a ceiling | Horizontal: more machines, near-unlimited, more complex |
| Consistency | Strong: always latest, slower | Eventual: fast and available, briefly stale |
| Services | Stateful: keeps session data, harder to scale | Stateless: any instance serves any request |
| Database | SQL: schemas, joins, ACID | NoSQL: flexible, scales out, weaker joins |
| APIs | REST: simple, cacheable, human-readable | RPC/gRPC: fast binary, strict contracts, great service-to-service |
| Communication | Synchronous: simple, caller waits | Asynchronous: decoupled, resilient, harder to debug |
| Processing | Batch: high throughput, delayed | Stream: low latency, more complex |
| Real-time updates | Long polling: works everywhere | WebSockets: true two-way, persistent connection (SSE for server→client only) |
| Schema | Normalised: no duplication, more joins | Denormalised: fast reads, duplicated data |
| Transport | TCP: reliable, ordered | UDP: fast, no guarantees (video calls, games) |

## Architectural styles

- **Client–server**: clients request, servers respond.
- **Monolith**: one deployable — simple to start.
- **Microservices**: small independent services — independent scaling and deployment, at the cost of network calls, distributed data and operational complexity.
- **Event-driven**: components react to events on a broker.
- **Serverless**: functions run on demand; no servers to manage, cold starts and limits.
- **Peer-to-peer**: nodes act as both clients and servers.

## How to approach a design question

1. Clarify functional and non-functional requirements.
2. Estimate scale (users, requests/sec, storage).
3. Define the API.
4. Sketch the high-level architecture.
5. Design the data model and storage.
6. Deep-dive into bottlenecks: caching, sharding, queues.
7. Discuss failures, monitoring and trade-offs.
