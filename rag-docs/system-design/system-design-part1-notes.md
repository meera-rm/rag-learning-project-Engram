---
title: System design handbook part 1 (networking, APIs, security, databases, caching) — study notes
topic: system-design
source_type: my-notes
note_kind: study-notes
---

# System Design Handbook, Part 1 — Study Notes

Networking, APIs, edge infrastructure, security basics, resilience, databases and caching.

## Networking and protocols

- **OSI / TCP-IP layers**: application (HTTP, DNS), transport (TCP, UDP), network (IP), link.
- **TCP**: connection-based, reliable, ordered (three-way handshake). **UDP**: connectionless, fast, no delivery guarantee.
- **HTTP/1.1** (one request at a time per connection), **HTTP/2** (multiplexing many requests over one connection, header compression), **HTTP/3** (runs over QUIC on UDP, faster connection setup, no head-of-line blocking at the transport layer).
- **TLS handshake**: agree on keys and verify the server certificate before encrypted traffic flows.

## API styles

| Style | Strengths | Weaknesses |
| --- | --- | --- |
| REST | Simple, cacheable, widely understood | Over/under-fetching, many round trips |
| GraphQL | Client asks for exactly the fields it needs | Caching and query-cost control are harder |
| gRPC | Fast binary (Protocol Buffers), streaming, strict contracts | Less browser-friendly, harder to inspect |
| WebSockets | Two-way, real-time | Stateful connections to scale |
| Webhooks | Server pushes events to a client URL | Receiver must be reachable and verify signatures |

Good API habits: versioning (`/v1/`), pagination (cursor-based for large lists), idempotency keys for POSTs that create payments/orders, consistent error format.

## DNS, CDN and proxies

- **DNS** resolves names to IPs: browser cache → OS → recursive resolver → root → TLD → authoritative server. Record types: A/AAAA (IP), CNAME (alias), MX (mail), TXT. TTL controls caching.
- **CDN**: edge servers cache content close to users; pull CDN (fetch on first request) vs push CDN (you upload in advance).
- **Forward proxy** acts for clients (corporate filtering); **reverse proxy** sits in front of servers (TLS termination, caching, routing, e.g. Nginx).

## Load balancers and API gateways

- **L4 load balancer**: routes by IP/port — fast, protocol-agnostic. **L7**: understands HTTP — can route by path, header, cookie.
- Algorithms: round robin, weighted, least connections, IP hash, consistent hashing.
- **API gateway**: single entry point for clients — routing, authentication, rate limiting, request aggregation, protocol translation.

## Security basics

- **Cookies** hold session ids (`HttpOnly`, `Secure`, `SameSite`).
- **Sessions** store state on the server; **JWT** is a signed, self-contained token.
- **OAuth 2.0**: lets a user grant an app limited access to their data on another service without sharing their password (authorisation). Flows: authorization code with PKCE (web/mobile), client credentials (service-to-service).
- **OpenID Connect (OIDC)**: an identity layer on top of OAuth 2.0 — adds an ID token that says who the user is (authentication, "Sign in with …").

## Resilience patterns

| Pattern | Problem it solves |
| --- | --- |
| Rate limiting | Protects services from overload and abuse |
| Timeouts | Stops a slow dependency from holding threads forever |
| Retries with exponential backoff + jitter | Recovers from brief failures without stampedes |
| Idempotency | Makes retries safe (same request → same effect once) |
| Circuit breaker | Stops calling a failing dependency; fails fast, tries again later (closed → open → half-open) |
| Bulkhead | Isolates resources (thread pools) so one failure doesn't sink everything |
| Fallback | Return cached or default data when a dependency is down |

## Databases

### SQL vs NoSQL

| Type | Examples | Good for |
| --- | --- | --- |
| Relational | PostgreSQL, MySQL | Transactions, joins, structured data |
| Key-value | Redis, DynamoDB | Fast lookups by key, sessions, caching |
| Document | MongoDB | Flexible JSON-like records |
| Wide-column | Cassandra, HBase | Massive write throughput, time-series |
| Graph | Neo4j | Relationships (social networks, recommendations) |
| Search | Elasticsearch, OpenSearch | Full-text search, log analytics |
| Time-series | InfluxDB, TimescaleDB | Metrics over time |
| Vector | pgvector, Pinecone, Chroma, Weaviate | Similarity search over embeddings (semantic search, RAG) |

### ACID vs BASE
- **ACID**: Atomicity, Consistency, Isolation, Durability — traditional transactions.
- **BASE**: Basically Available, Soft state, Eventually consistent — many distributed NoSQL stores.

### Normalisation
Split data to remove duplication (1NF: atomic values; 2NF: no partial dependency on a composite key; 3NF: no dependency between non-key columns). Denormalise deliberately for read speed.

### Indexes
B-tree (equality + ranges, the default), hash (equality only), composite (column order matters — leftmost prefix rule), covering (all needed columns in the index), full-text, geospatial. Indexes speed reads but slow writes and use storage.

### Transactions and isolation
| Level | Prevents |
| --- | --- |
| Read uncommitted | Nothing much |
| Read committed | Dirty reads |
| Repeatable read | + non-repeatable reads |
| Serializable | + phantom reads (behaves as if transactions ran one at a time) |

- **Pessimistic locking**: lock rows before changing (`SELECT … FOR UPDATE`). **Optimistic locking**: check a version number at write time, retry on conflict.
- **MVCC**: readers see a snapshot while writers create new versions, so reads don't block writes (PostgreSQL, MySQL InnoDB).

### Replication, partitioning, sharding
- Leader–follower (one writer), multi-leader (writes in several regions, conflict resolution needed), leaderless (quorum reads/writes, e.g. Cassandra: `R + W > N`).
- Synchronous replication = no data loss, slower writes; asynchronous = faster, possible lag.
- **Partitioning** splits a table (often within one database); **sharding** spreads partitions across servers. Choose keys to avoid hot spots; resharding is painful, so consistent hashing helps.

## Caching

- Where: browser, CDN, API gateway, application (in-process), distributed cache (Redis), database buffer cache.
- Strategies: cache-aside, read-through, write-through, write-behind, write-around.
- Eviction: LRU, LFU, TTL.
- Failure modes:
  - **Cache stampede / thundering herd**: many requests miss at once — use locks or request coalescing, staggered TTLs.
  - **Cache penetration**: requests for non-existent keys — cache negatives or use a Bloom filter.
  - **Cache avalanche**: many keys expire together or the cache goes down — random TTL jitter, replicas.
  - **Stale data**: invalidate on write, or accept short TTLs.

## Bloom filters and consistent hashing

- **Bloom filter**: a bit array plus several hash functions. "No" is certain; "yes" may be a false positive. Uses: skip disk reads for missing keys, check if a username might be taken.
- **Consistent hashing**: keys and servers on a ring; each key goes to the next server clockwise. Adding a server moves only a small share of keys. Virtual nodes balance load.
