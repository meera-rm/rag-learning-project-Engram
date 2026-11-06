---
title: SYSTEM-DESIGN-NOTES
topic: system-design
source_type: my-notes
source_file: systemdesign/SYSTEM-DESIGN-NOTES.md
---

# System Design — Master Notes

Consolidated notes from everything in `systemdesign/`: the 30-concepts article, its saved diagrams, two PDF handbooks, the 50-question guide screenshots and the large 1,354-page interview book.

**How to use this file.** Read Parts 1-3 first (concepts, handbook, interview template). Use Part 4 and Part 5 for question practice and low-level design. The full chapter-by-chapter text of the big book lives in `SYSTEM-DESIGN-INTERVIEW-BOOK-DIGEST.md` (Part 6 explains how to find things in it).

---

## Part 1 — The 30 core concepts (your earlier notes, copied in full)

Source: Ashish Pratap Singh, AlgoMaster. "System Design was HARD until I Learned these 30 Concepts" (article: blog.algomaster.io/p/30-system-design-concepts; video: youtube.com/watch?v=s9Qh9fWeOAk). Each concept has *What*, *Why it matters*, a *Real-world example* and the matching *AWS service*. The original file `SYSTEM-DESIGN-30-CONCEPTS.md` is unchanged.

### The big picture: one request's journey

```
User → DNS lookup → CDN (static files) → API Gateway / Reverse Proxy (auth, rate limit)
     → Load Balancer → App servers (horizontally scaled, microservices)
     → Cache (Redis) → Database (primary + read replicas, sharded)
     → Message Queue → background workers   |   Blob storage (S3) for files
```

---

### Group A — Basics: how a client reaches a server

#### 1. Client-Server Architecture
- **What:** A client (browser, mobile app) sends a request. A server that is always running processes it and sends back a response.
- **Why:** Almost every system design starts from this.
- **Example:** A React app calls `GET /books` on an Express server, which returns JSON.

#### 2. IP Address
- **What:** A unique address for a machine on a network, similar to a phone number.
- **Problem:** People can't remember IPs, and they change when you migrate servers. DNS solves this.

#### 3. DNS (Domain Name System)
- **What:** Turns `algomaster.io` into an IP address. The browser asks DNS first and then connects to that IP.
- **Try it:** `ping google.com` shows the IP it resolves to.
- **AWS:** Route 53

#### 4. Proxy vs Reverse Proxy
| | Forward Proxy | Reverse Proxy |
|---|---|---|
| Sits in front of | Clients | Servers |
| Hides | The client's IP | The servers' IPs |
| Used for | Privacy, corporate filtering, VPN-style access | Security, DDoS filtering, load balancing, SSL termination |
- **Example:** NGINX in front of your Node app.

#### 5. Latency
- **What:** The round-trip delay between client and server. Physical distance is the main cause (e.g., NY ↔ India).
- **Fix:** Deploy to several data centers or regions and use CDNs so users connect to the nearest one.
- **AWS:** Multi-region deployments, CloudFront

#### 6. HTTP / HTTPS
- **HTTP:** The request/response protocol. A request has a method, headers and an optional body. A response has a status code, headers and a body.
- **HTTPS:** HTTP encrypted with SSL/TLS, so passwords and card numbers can't be read in transit.
- **AWS:** ACM (certificates) on an ALB or CloudFront

---

### Group B — APIs

#### 7. APIs
- **What:** A contract that lets a client use a server without knowing how it works inside. Usually returns JSON.

#### 8. REST
- **What:** Resource-based URLs (`/users`, `/orders/42`) with standard methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove).
- **Key rule:** Stateless. Every request carries everything the server needs.
- **Pros:** Simple, scalable, cacheable. **Cons:** Over-fetching, or needing several calls for related data.

#### 9. GraphQL
- **What:** One endpoint where the client asks for exactly the fields it needs (introduced by Facebook in 2015).
- **Example:** User + profile + posts takes 3 REST calls but only 1 GraphQL query.
- **Cons:** More work on the server, and caching is harder.
- **AWS:** AppSync

---

### Group C — Databases and scaling

#### 10. Databases
- **Why:** Memory is fine for tiny data. Real data needs durable, queryable storage.

#### 11. SQL vs NoSQL
| SQL | NoSQL |
|---|---|
| Tables with a fixed schema | Flexible schema |
| ACID transactions | Scales horizontally with ease |
| MySQL, PostgreSQL | Key-value (Redis), Document (MongoDB), Graph (Neo4j), Wide-column (Cassandra) |
| Banking, orders | Feeds, recommendations, sessions |
- **Real systems often use both:** SQL for orders, NoSQL for recommendations.
- **AWS:** RDS/Aurora (SQL), DynamoDB (NoSQL)

#### 12. Vertical Scaling (scale UP)
- **What:** Give one machine more CPU, RAM or disk.
- **Cons:** There's a hardware ceiling, cost rises sharply at the top end, and it's a **single point of failure**.
- **AWS:** Move from t3.micro to m5.4xlarge

#### 13. Horizontal Scaling (scale OUT)
- **What:** Add more machines that share the work.
- **Pros:** Fault tolerant (others take over if one fails) and uses cheap commodity machines.
- **New problem:** Which server should the client talk to? A load balancer answers that.
- **AWS:** EC2 Auto Scaling Groups

#### 14. Load Balancers
- **What:** Spread traffic across servers and skip unhealthy ones (via health checks).
- **Algorithms:**
  - **Round Robin:** Servers take turns.
  - **Least Connections:** Send to the server with the fewest active connections.
  - **IP Hash:** The same client always goes to the same server ("sticky" sessions).
- **AWS:** ALB (layer 7, HTTP), NLB (layer 4, TCP)

#### 15. Database Indexing
- **What:** A lookup structure (like a book's index) that points straight to rows, so the database doesn't scan the whole table.
- **Index:** Primary keys, foreign keys, and columns used in WHERE / JOIN / ORDER BY.
- **Trade-off:** Reads get faster, but INSERT, UPDATE and DELETE get slower. Only index the columns you actually query.
- **Example:** `CREATE INDEX idx_users_email ON users(email);`

#### 16. Replication
- **What:** One **primary** handles writes and copies them to **read replicas**, which handle SELECTs.
- **Pros:** More read throughput, and high availability because a replica can be promoted if the primary dies.
- **Watch out:** Replication lag means a replica can briefly return stale data.
- **AWS:** RDS Read Replicas, Multi-AZ

#### 17. Sharding (horizontal partitioning)
- **What:** Split the **rows** across several databases using a **shard key** (e.g., `user_id % 4`).
- **Pros:** Each database handles less load. **Cons:** Cross-shard queries and joins are hard, and a bad key creates "hot" shards.
- **AWS:** DynamoDB partitions data automatically by partition key

#### 18. Vertical Partitioning
- **What:** Split a table by **columns** according to how they're used.
- **Example:** `User` becomes `User_Profile` + `User_Login` + `User_Billing`.
- **Pro:** Queries read fewer columns, so there's less disk I/O.

#### 19. Caching
- **What:** Keep hot data in memory so you don't hit the database every time.
- **Cache-aside pattern:**
  1. Check the cache. On a hit, return it.
  2. On a miss, read from the database, write the result to the cache, then return it.
- **TTL (time-to-live):** Expires entries so stale data gets refreshed.
- **Tools:** Redis, Memcached. **AWS:** ElastiCache, DAX (for DynamoDB)

#### 20. Denormalization
- **What:** Deliberately duplicate data into one table to avoid expensive JOINs.
- **Trade-off:** Reads get faster, but you use more storage and updates get more complex. Best for **read-heavy** systems.
- **Example:** A `UserOrders` table that stores the user name next to each order.

#### 21. CAP Theorem
- **The rule:** A distributed system can guarantee only 2 of these 3: **C**onsistency (everyone sees the same data), **A**vailability (every request gets a response) and **P**artition tolerance (it keeps working when the network splits).
- **Since partitions always happen, the real choice is CP or AP:**
  - **CP:** Banking, inventory (correctness matters most)
  - **AP:** Social feeds, likes (being up matters most), e.g., Cassandra, DynamoDB
- **Eventual consistency:** A write is acknowledged right away, then spreads to replicas, and they all converge over time.

#### 22. Blob Storage
- **What:** Stores big unstructured files (images, video, PDFs) in buckets, and each object gets a URL.
- **Pros:** Scales to petabytes, pay-as-you-go, replicated automatically.
- **Rule:** Don't put large files in your database. Store them in S3 and keep the URL in the database.
- **AWS:** S3

#### 23. CDN (Content Delivery Network)
- **What:** Edge servers around the world cache static content (HTML, JS, CSS, images, video) close to users.
- **Example:** A user in India streams a video hosted in California from a nearby Indian edge node.
- **AWS:** CloudFront (often with S3 as the origin)

---

### Group D — Real-time and communication

#### 24. WebSockets
- **Problem:** With plain HTTP the client has to keep polling ("anything new?"), and most answers are empty, which wastes bandwidth.
- **What:** One persistent, **two-way** connection that lets the server push updates instantly.
- **Use for:** Chat, live stock prices, multiplayer games.
- **AWS:** API Gateway WebSocket APIs

#### 25. Webhooks
- **What:** Server-to-server push. A provider sends an HTTP POST to your URL when an event happens.
- **Examples:** Stripe → "payment succeeded". GitHub push → triggers CI/CD (Jenkins / GitHub Actions).
- **WebSocket vs Webhook:** A WebSocket is a live connection to a client. A webhook is a one-off callback between servers.

#### 26. Microservices
- **Monolith problem:** One codebase. One bug or a risky deploy can take down everything.
- **Microservices:** Small independent services with one job each, their **own database**, and independent scaling and deploys.
- **They talk via:** APIs (synchronous) or message queues (asynchronous).
- **AWS:** ECS/EKS, Lambda

#### 27. Message Queues
- **What:** A producer puts a message on a queue, and a consumer processes it later (**asynchronous**).
- **Example:** The checkout service drops an "order placed" message and the payment and email services pick it up.
- **Pros:** Decoupled services, absorbs traffic spikes, keeps messages safe if a consumer is down.
- **Tools:** Kafka, RabbitMQ. **AWS:** SQS (queue), SNS (pub/sub), Kinesis/MSK (streams)

#### 28. Rate Limiting
- **What:** Caps requests per client in a time window (e.g., 100 requests/min). Going over returns **HTTP 429 Too Many Requests**.
- **Algorithms:**
  - **Fixed Window:** Count per minute. Simple, but allows bursts at window edges.
  - **Sliding Window:** Smooths out those edge bursts.
  - **Token Bucket:** Tokens refill at a fixed rate and each request spends one. Allows controlled bursts.
- **AWS:** API Gateway throttling, WAF rate-based rules

#### 29. API Gateway
- **What:** The single front door for microservices. It handles **auth, rate limiting, logging, monitoring and routing**.
- **Flow:** Client → Gateway (validate) → the right service → response.
- **Tools:** NGINX, Kong. **AWS:** API Gateway

#### 30. Idempotency
- **What:** Sending the same request twice has the same effect as sending it once.
- **Why:** Retries, double-clicks and refreshes could otherwise charge a card twice.
- **How:** The client sends a unique **idempotency key**. The server checks whether it has seen that key: if so, it returns the stored result; if not, it processes the request and saves the key.
- **Note:** GET, PUT and DELETE are idempotent by design. POST is not, so it needs a key.

---

### Quick recall sheet
| Problem | Concept / tool |
|---|---|
| Can't remember IPs | DNS |
| Hide or protect servers | Reverse proxy |
| One server too small | Vertical, then horizontal scaling |
| Spread traffic | Load balancer |
| Slow queries | Index, cache, denormalize |
| Too many reads | Read replicas + cache |
| Too much data or too many writes | Sharding |
| Big files | Blob storage (S3) |
| Far-away users | CDN / multi-region |
| Real-time to client | WebSockets |
| Event notification between servers | Webhooks |
| Slow or fragile service calls | Message queue |
| Abuse or traffic spikes | Rate limiting (429) |
| Many services, one entry point | API gateway |
| Duplicate payments | Idempotency key |
| Consistency vs availability | CAP theorem |


---

## Part 2 — Extra details from the article's diagrams

The article's illustrations carry concrete examples that Part 1 only mentions. These are the ones worth remembering. (The article's cover image is the list of all 30 concepts, in the same order as Part 1.)

- **Client-server / HTTP (concept 6).** A request is a method plus path plus headers: `GET /index.html`, `Host: www.example.com`, `User-Agent: Mozilla`, `Cookie: sessionId=123`. A response is a status line plus headers plus body: `HTTP/1.1 200 OK`, `Content-Type: text/html`, `Content-Length: 142`.
- **APIs (concept 7).** Client sends a request to the API, the API talks to the API server, and the response comes back the same way. The API is the contract in the middle.
- **REST (concept 8).** Example: `GET /api/users/123` to the Users Service returns JSON `{ "id": 123, "firstName": "John", "secondName": "Smith", "email": "john.smith@example.com" }`.
- **SQL vs NoSQL (concept 11).** One relational table versus four NoSQL shapes: **key-value** (K1→V1), **column store**, **graph** (nodes and edges), **document** (a tree of nested records).
- **Sharding (concept 17).** A database with 3 million rows becomes 3 shards with 1 million rows each.
- **Vertical partitioning (concept 18).** One `Users` table (`user_id, name, email, last_login, billing_address, payment_method`) splits into three: `User_Profile (user_id, name, email)`, `User_Login (user_id, last_login)` and `User_Billing (user_id, billing_address, payment_method)`.
- **Caching, cache-aside (concept 19).** The application first reads from the cache (a *cache hit* ends here). On a *cache miss* it reads from the database, then writes the result to the cache. The cache in the diagram is Redis.
- **Denormalization (concept 20).** Two normalized tables, `Users (user_id, name, email, address)` and `Orders (order_id, user_id, product, amount)`, are merged into one `User_Orders` table (`order_id, user_id, user_name, user_email, product, amount`). Sample rows: order 101 Alice a@xyz.com iPhone 15 999.00; order 102 Alice AirPods Pro 249.00; order 103 Bob b@xyz.com Kindle 129.00. Alice's name and email now repeat on every order, which is the cost of skipping the join.
- **CDN (concept 23).** A world map: one **origin server** (in North America) and several **CDN servers** near users on every continent. Each user connects to the nearest CDN server; only a miss goes back to the origin.
- **Webhooks (concept 25).** A user pays a provider. The provider then sends `POST /api/webhooks/payment HTTP/1.1` to the receiver's registered webhook URL (`https://myapp.com/api/webhooks/payment`).
- **WebSockets (concept 24).** Four steps on one long-lived connection: initiating handshake, connection established, data transfer (both directions), connection closure.
- **Microservices (concept 26).** Order, Payment, Inventory and Shipping services, each with its **own database**, each drawn as several replicas.
- **Message queues (concept 27).** Producers 1-3 write into a **broker** that holds Queue 1 and Queue 2. Consumers 1-3 pull messages and send an **ACK** back so the broker knows the message was processed (and can redeliver if no ACK arrives).
- **API gateway (concept 29).** Clients all go through one gateway that does authentication, rate limiting, logging, monitoring and request routing, then forwards to the right microservice.

---

## Part 3 — AlgoMaster System Design Interview Handbook (75 pages)

By Ashish Pratap Singh, AlgoMaster.io. Three groups of building blocks, then an interview template, 40 tips and 10 practice questions.

### 3.1 Fundamentals (20)

1. **Scalability.** The ability to handle a growing amount of load by adding resources. A system that can keep evolving to support more work is scalable.
2. **Availability.** The share of time a system is operational and reachable. `Availability = Uptime / (Uptime + Downtime)`.

   | Availability | Downtime per year | Called |
   |---|---|---|
   | 99% | 3.65 days | two nines |
   | 99.9% | 8.76 hours | three nines |
   | 99.99% | 52.56 minutes | four nines |
   | 99.999% | 5.26 minutes | five nines |
   | 99.9999% | 31.5 seconds | six nines |
3. **Latency vs throughput.** *Latency* is the time one request takes (low latency = responsive). *Throughput* is work done per unit time, usually requests per second (RPS) or transactions per second (TPS).
4. **CAP theorem.** A distributed data store cannot guarantee all three at once.
   - **Consistency:** every read gets the most recent write, or an error.
   - **Availability:** every request gets a non-error response, with no promise that it holds the latest write.
   - **Partition tolerance:** the system keeps working even when the network drops or delays messages between nodes.
5. **Load balancers.** Spread incoming traffic across servers so none is overwhelmed. Algorithms: **Round Robin** (circular order), **Weighted Round Robin** (by server capacity), **Least Connections** (fewest active connections), **Least Response Time** (fastest server), **IP Hash** (client IP decides the server).
6. **Databases.** An organized collection of data that can be accessed, managed and updated. Types: relational (RDBMS), NoSQL, in-memory, graph, time series, spatial.
7. **CDN.** A geographically distributed network of servers that delivers HTML, JS, CSS, images and video from the location nearest the user. This cuts the distance, so latency drops and load times improve. Requests are redirected to the nearest server.
8. **Message queues.** Let parts of a system exchange messages **asynchronously**. Producers send a message and move on. Several consumers can pull from the queue, which spreads the work.
9. **Rate limiting.** Protects services from being overwhelmed by one client. Algorithms: **Token Bucket** (allows bursts within an overall rate), **Leaky Bucket** (smooths traffic to a constant rate), **Fixed Window Counter** (limit per fixed interval), **Sliding Window Log** (tracks requests in a rolling window), **Sliding Window Counter** (smooths between adjacent fixed windows).
10. **Database indexes.** A lookup table of indexed column values plus pointers to rows. Without one the database scans every row; with one it jumps to the exact location.
11. **Caching.** Keeps copies of data in a fast layer to cut latency and offload the main store.
    - **Strategies:** *Read-Through* (cache fetches missing data from the source itself), *Write-Through* (write to cache and source together), *Write-Back* (write to cache first, update the source later), *Cache-Aside* (the application manages reads and cache population).
    - **Eviction policies:** *LRU* (least recently used), *LFU* (least frequently used), *FIFO* (oldest first), *TTL* (expire after a set time).
12. **Consistent hashing.** Spreads data across a cluster so that adding or removing a node moves only a small share of the data. Picture a ring from 0 to 2^n−1. Servers and data items are both hashed onto the ring, and an item lives on the first server found moving **clockwise** from its position.
13. **Database sharding.** Horizontal scaling that splits one large database into smaller independent **shards** on separate servers, each owning a subset of the data. Less load per server, faster queries.
14. **Consensus algorithms.** Make all nodes agree on the same state or sequence of events despite latency, crashes or asynchrony. **Paxos:** a leader proposes a value and a majority of nodes accepts it. **Raft:** one node is the leader, manages log replication and keeps the cluster consistent.
15. **Proxy servers.** Intermediaries between users and the internet. **Forward proxy** sits in front of the client. **Reverse proxy** sits in front of web servers.
16. **Heartbeats.** Periodic messages between components to monitor health. Without them, failure detection is slow, which means delayed recovery, more downtime and less reliability.
17. **Checksums.** A fingerprint attached to data before sending. The receiver recomputes it. A match means the data was not modified or damaged.
18. **Service discovery.** Lets services find each other dynamically without hard-coded network locations. Services register in a **service registry**, the single source of truth that others query.
19. **Bloom filters.** A probabilistic structure that answers "**definitely not** in the set" or "**possibly** in the set". Start with `m` bits set to 0 and `k` hash functions. To add an item, set the `k` bit positions to 1. To query, check the same positions: any 0 means definitely absent; all 1s means present or a false positive.
20. **Gossip protocol.** Decentralized spread of information, like word of mouth. A node holds some information; at regular intervals each node picks another at random and shares it; receivers merge what they hear; eventually every node converges on the same information.

### 3.2 Trade-offs (11)

| Pair | Option A | Option B |
|---|---|---|
| Vertical vs horizontal scaling | **Vertical:** a bigger machine (CPU, RAM, storage). Simple, but there is a physical limit and it is a single point of failure | **Horizontal:** more servers. Near-limitless scale, but you now manage a distributed system |
| Strong vs eventual consistency | **Strong:** once a write is acknowledged, every later read sees it | **Eventual:** given enough time all nodes converge, with no promise of when |
| Stateful vs stateless | **Stateful:** the server remembers the client between requests (sessions, transaction details) | **Stateless:** every request is independent and carries everything the server needs |
| Read-through vs write-through cache | **Read-through:** the cache sits between app and store; on a miss the cache loads, stores and returns the data | **Write-through:** every write goes to the cache and the database; it counts as done only when both succeed |
| SQL vs NoSQL | **SQL:** predefined schema; best for complex queries, ACID transactions (finance) and stable structure. MySQL, PostgreSQL, Oracle | **NoSQL:** flexible and scalable; best for big data, fast iteration, horizontal scale. MongoDB, Cassandra, Redis |
| REST vs RPC | **REST:** resource-based URLs, standard HTTP methods, stateless, JSON or XML | **RPC:** action-based, many protocols (HTTP, TCP), often custom methods and formats |
| Synchronous vs asynchronous | **Sync:** tasks run in order; easy to reason about (reading a file line by line) | **Async:** tasks run concurrently; better responsiveness for I/O-bound work (background jobs) |
| Batch vs stream processing | **Batch:** large volumes at scheduled times; high latency; ETL, reporting, backups | **Stream:** processed as it arrives in milliseconds to seconds; fraud detection, live feeds, IoT |
| Long polling vs WebSockets | **Long polling** (as the handbook describes it): the client keeps asking the server for updates, so there is extra latency and load even when nothing is new. (In the classic form the server holds each request open until data exists.) | **WebSockets:** one persistent full-duplex connection; both sides send at any time without HTTP overhead |
| Normalization vs denormalization | **Normalization:** split data into related tables so each fact is stored once (less redundancy, better integrity). Example: customers and orders in separate tables | **Denormalization:** combine tables to speed queries, accepting duplicate data. Example: store the latest comments with each blog post |
| TCP vs UDP | **TCP:** reliable, ordered, connection-oriented, slower (web, file transfer) | **UDP:** fast, connectionless, no guarantees (video streaming, gaming) |

### 3.3 Architectural patterns (5)

1. **Client-server.** Clients (browser, mobile app, desktop app) send requests and show results. Servers process requests and manage resources such as databases.
2. **Microservices.** A set of loosely coupled, independently deployable services. Each handles one business function, talks over lightweight protocols (HTTP/REST or queues) and has **its own database**.
3. **Serverless.** The cloud provider runs the infrastructure and scaling. You deploy functions triggered by events and pay only for compute time used. Good for file processing, workflows and real-time streams.
4. **Event-driven (EDA).** Components react to events (state changes), communicate asynchronously and stay decoupled. Many consumers can process events in parallel.
5. **Peer-to-peer.** No central server. Every peer is both client and server, sharing resources directly. No single point of failure, and it scales as peers join.

### 3.4 The interview template: 7 steps

1. **Clarify requirements.**
   - *Functional:* core features; who the users are (customers, internal teams); how they interact (web, mobile, API); key data types (text, images, structured); external or third-party integrations.
   - *Non-functional:* read-heavy or write-heavy and the ratio; allowed downtime or high availability; latency targets; how critical consistency is; whether to rate limit.
2. **Capacity estimation** (check with the interviewer that it is wanted). Daily and monthly users and peak concurrency; reads and writes per second; storage; cache memory; network bandwidth.
3. **High-level design.** Draw the blocks: clients, application servers, load balancers, services, databases, storage (files, images, video), caching, message queues (if async), external services (such as payment gateways).
4. **Database design.**
   - *Data modeling:* entities (users, products, orders), relationships, attributes, primary keys, normalization for integrity.
   - *Choose storage:* relational for structured data with complex relationships and ACID; NoSQL for unstructured or semi-structured data, high scale and eventual consistency; combine both if the data differs.
5. **API design.** List the APIs to expose and pick a style (REST, GraphQL, RPC). Pick protocols: **HTTPS** for REST and web, **WebSockets** for real-time two-way (chat), **gRPC** for efficient service-to-service calls, **AMQP / MQTT** for async messaging with queues.
6. **Dive deep into key components.** Follow the interviewer. A URL shortener means the short-URL generation algorithm; a chat app means real-time send and receive. Common areas: databases (sharding, replicas), application servers (more servers behind the load balancer), caching (where to add it, how to invalidate).
7. **Address key concerns.**
   - *Scalability and performance:* scale up or out with load balancers, caching, indexes, denormalization where needed, partitioning and sharding, asynchronous processing.
   - *Reliability:* find single points of failure; add redundancy (multiple load balancers, replicas); geographic redundancy; replication for availability and durability; circuit breakers to stop cascading failures; retries with exponential backoff; monitoring and alerting.

### 3.5 The 40 interview tips

1. Understand functional and non-functional requirements before designing.
2. Define the use cases and constraints clearly.
3. There is no perfect solution. It is all trade-offs.
4. Assume everything can and will fail. Make it fault tolerant.
5. Keep it simple. Avoid over-engineering.
6. Design for scalability from the ground up.
7. Prefer horizontal over vertical scaling.
8. Use load balancers for availability and to distribute traffic.
9. Use SQL for structured data and ACID transactions.
10. Use NoSQL for unstructured data.
11. Use a graph database for highly connected data.
12. Shard to scale SQL databases horizontally.
13. Index to speed up read queries.
14. Assume everything can and will fail (it is tip 4 again, repeated in the handbook).
15. Rate limit to prevent overload and DoS attacks.
16. Use WebSockets for real-time communication.
17. Use heartbeats to detect failures.
18. Use a message queue for asynchronous communication.
19. Partition and shard large datasets.
20. Denormalize for read-heavy workloads.
21. Use Bloom filters to check membership in a large dataset quickly.
22. Use CDNs to cut latency for a global user base.
23. Use caching to reduce database load and response time.
24. Use a **write-through** cache for write-heavy applications.
25. Use a **read-through** cache for read-heavy applications.
26. Use object storage such as S3 for large datasets and media.
27. Replicate data and add redundancy to avoid single points of failure.
28. Use autoscaling to absorb traffic spikes.
29. Use asynchronous processing for background tasks.
30. Use batch processing for non-urgent work.
31. Make operations **idempotent** to simplify retries and error handling.
32. Use a data lake or warehouse for analytics and reporting.
33. Log and monitor comprehensively.
34. Use circuit breakers so one failing service cannot take down the system.
35. Practise chaos engineering to find weaknesses.
36. Design for statelessness when possible.
37. Use failover to switch automatically to a redundant system.
38. Spread across several data centers to survive local failures.
39. Use TTLs to expire cached data and limit staleness.
40. Pre-populate critical data in the cache to avoid cold starts.

### 3.6 The 10 most common interview questions (requirements to state)

| # | System | Functional requirements | Non-functional requirements |
|---|---|---|---|
| 1 | **URL shortener (TinyURL)** | Unique short URL for a long URL; redirect to the original; custom short URLs (optional); link expiration; usage analytics (optional) | 99.9% availability; redirects in milliseconds; millions of requests per day; durable for years; security against phishing |
| 2 | **Chat app (WhatsApp)** | One-on-one and group chats; online/offline status; delivery status (sent, delivered, read); media messages (images, video, voice notes, documents); push notifications (optional) | Real-time delivery with minimal latency; millions of concurrent users; highly available (may trade availability for consistency); durable, so no lost messages |
| 3 | **Social media (Instagram)** | Upload images and videos; like, comment, share; follow and unfollow; news feed from followed users; tagging in posts and comments | 99.9% availability; low-latency feed generation; millions of concurrent users; durable uploads; **eventual consistency** is fine (a photo can appear late) |
| 4 | **Video streaming (YouTube)** | Upload videos with titles, descriptions, tags, thumbnails; on-demand streaming; search videos, channels, playlists; like, dislike, comment, share; view counts | 99.99% availability; real-time streaming without lag; horizontal scaling; durable uploads |
| 5 | **E-commerce (Amazon)** | Sellers list products (title, description, price, images, specs); cart and wishlist; search by keyword, category, brand; place orders; ratings and reviews | Millions of users, products and transactions; 99.9% availability; low latency for page load, search and checkout; durable critical data |
| 6 | **Ride sharing (Uber)** | See nearby drivers; book with pickup and drop-off; match riders and drivers in real time; real-time fare and ETA estimates (distance, traffic, demand); live ride tracking | Millions of users and rides; low latency for matching, GPS and requests; 99.9% availability; riders and drivers see a consistent view |
| 7 | **File storage (Google Drive)** | Upload files of any type and size; download; share by link or email; search by name, type, content, metadata; sync across devices | Millions of users and billions of files; low-latency upload, download and search; high availability; consistent sync across devices; durable |
| 8 | **Web crawler** | Fetch URLs efficiently; handle text, images, multimedia; prioritize URLs (importance, freshness); store crawled data in a database or file system | Scale to millions or billions of pages; low latency in fetching and processing; high throughput (pages per unit time) |
| 9 | **Notification system** | Email, SMS, push (mobile and web) and in-app channels; transactional, promotional and informational types; scheduled delivery; bulk sending for campaigns; automatic retries | Millions per minute at peak; 99.99% availability; low latency for real-time and high-priority messages; reliable delivery on every channel |
| 10 | **Logging and monitoring** | Collect logs from apps, servers, databases, microservices; support JSON, plaintext, XML; archive old logs to cold storage; query by time, level, source; alerts on patterns, thresholds, anomalies | Scale horizontally with volume; low-latency ingestion for real-time monitoring; 99.99% availability; durable with replication across nodes or data centers |

---

## Part 4 — "System Design Interview Questions and Answers (50)" (from your screenshots)

The guide has **20 beginner, 20 intermediate and 10 difficult** questions with Mermaid architecture diagrams. Your four screenshots capture only part of the beginner section. What they show:

**Q1. What is system design?** The process of defining architecture, components, data flow and trade-offs to build scalable, reliable software. Key goals: meet functional requirements (what the system does); meet non-functional requirements (scale, latency, reliability, security); balance trade-offs (cost vs performance, consistency vs availability).

**Q2. Horizontal vs vertical scaling?** *Vertical (scale up):* add more CPU/RAM to one server. *Horizontal (scale out):* add more servers and distribute traffic. Horizontal is usually preferred for internet-scale systems because it avoids single-machine limits.

**Q4 (diagram only, title not captured).** User → Application → Cache. On a **hit** the cache returns the data to the application. On a **miss** the application goes to the Database.

**Q5. What is a CDN?** A globally distributed set of edge servers that serve static content closer to users. Benefits: lower latency, reduced origin-server load, better global performance.

**Q6. What is database indexing?** A data structure (often a B-tree) that speeds up queries by avoiding full table scans. Trade-off: faster reads, but slightly slower writes and more storage.

**Q7. SQL vs NoSQL: when to use each?** *SQL:* strong schema, joins, ACID transactions, relational data. *NoSQL:* flexible schema, high write throughput, horizontal scaling, denormalized data. Choose based on access patterns, consistency needs and scale.

**Q8. What is replication in databases?** Copies data from a primary database to one or more replicas. Benefits: read scaling (serve reads from replicas), high availability, disaster recovery.

**Q9. What is sharding?** Splits data across multiple database nodes using a **shard key**. Benefits: higher read and write throughput, better storage scalability. Challenge: cross-shard queries and rebalancing complexity. Diagram: Application → Shard Router → Shard 1, 2, 3.

**Q10. What is CAP theorem?** In a distributed system under a network partition you can guarantee at most two of the three properties. (The screenshot ends before the list; see Part 3.1 item 4.)

**Q14 (title not captured; options visible).** Load-balancing algorithms: round robin, least connections, IP hash, weighted routing. "Choice depends on traffic pattern and server heterogeneity."

**Q15. What is the role of an API gateway?** An entry point for clients to backend services. It handles authentication and authorization, rate limiting, routing, and request and response transformation.

**Q16. What is a message queue?** Decouples producers and consumers via asynchronous communication. Benefits: smoother traffic spikes, better fault isolation, retry and dead-letter mechanisms. Diagram: Producer → Message Queue → Consumer 1 and Consumer 2.

**Not captured by the screenshots:** Q3, Q11-Q13 and Q17-Q50, plus the start of Q4 and the options of Q10.

---

## Part 5 — Low-level design (LLD) and design-pattern guide (9 pages)

By @adarschetan. Read from the image pages of `systemdesignpattern.pdf`.

### 5.1 Why design patterns, and the design flow

Patterns are proven solutions to common design problems. They improve reusability, maintainability and scalability, reduce complexity, and help you think like a senior engineer. They are **not copy-paste code**; they are about solving problems in the best possible way. Flow: **1 Requirements → 2 Identify entities → 3 Define relationships → 4 Apply patterns → 5 Design the solution.**

Pattern families (Gang of Four): **Creational** (how objects are created), **Structural** (how classes and objects are composed), **Behavioral** (how objects communicate).

### 5.2 The top 10 LLD design patterns

| Pattern | Problem it solves | Idea | Use cases |
|---|---|---|---|
| **Singleton** | Ensure a class has only one instance with a global access point | Private constructor plus a static `getInstance()` | Logger, config manager, cache, DB connection pool |
| **Factory** | Create objects without exposing the creation logic | A factory class or method `create(type)` returns Product A, B or C | Notification system, payment gateway, vehicle factory, UI components |
| **Strategy** | Define a family of interchangeable algorithms | A `Strategy` interface with concrete strategies; a `Context` holds one and calls `execute()` | Payment methods, sorting algorithms, pricing engine, discount calculation |
| **Observer** | One-to-many dependency: when one object changes, all dependents are notified | A `Subject` with `attach / detach / notify`; observers implement `update()` | Notification service, event bus, stock price updates, chat apps |
| **Builder** | Construct a complex object step by step | A `Director` drives a `Builder` (`buildPartA`, `buildPartB`, `getResult`) to produce the Product | User builder, SQL query builder, HTTP request builder, document generator |
| **Decorator** | Add behavior to an object dynamically without changing its structure | Wrap the object in decorators that add responsibilities | Coffee machine, pizza toppings, logging, compression, encryption |
| **Adapter** | Make incompatible interfaces work together | An adapter converts one interface into the one the client expects | Third-party APIs, payment providers, legacy systems, database migration |
| **Command** | Encapsulate a request as an object | The invoker executes command objects; each command calls a receiver | Undo/redo, task scheduler, queue processing, remote controls |
| **State** | Let an object change behavior when its internal state changes | State classes handle behavior per state; the context delegates | ATM machine, elevator, vending machine |
| **Chain of Responsibility** | Avoid coupling the sender of a request to its receiver | Pass the request along a chain of handlers until one handles it | Authentication, logging, approval workflow |

**Pattern selection guide.** Need only one instance → Singleton. Create objects based on type → Factory. Multiple algorithms for the same work → Strategy. One-to-many notifications → Observer. Complex object creation → Builder. Add responsibilities dynamically → Decorator. Incompatible interfaces → Adapter. Request as an object → Command. Behavior changes with state → State. Pass a request along a chain → Chain of Responsibility.

**Best practices.** Prefer composition over inheritance. Program to interfaces, not implementations. Keep classes small and focused. Follow SOLID. Choose the right pattern, not any pattern. Do not overuse patterns. Understand the problem before the pattern. Document pattern usage with examples. *Patterns are tools, not rules.*

### 5.3 The LLD design process (10 steps)

1. **Requirement gathering:** understand the problem and the functional and non-functional requirements.
2. **Identify entities and responsibilities:** nouns become entities; decide what each is responsible for.
3. **Identify relationships:** associations (uses, has-a, belongs-to).
4. **Design classes and interfaces:** attributes, methods and interfaces.
5. **Define interactions:** low-level flow of how objects cooperate.
6. **Handle edge cases and validations:** error scenarios and constraints.
7. **Draw UML diagrams:** class, sequence, activity, and state if needed.
8. **Review and refactor:** remove duplication, simplify.
9. **Implementation:** translate to clean, maintainable, extensible code.
10. **Testing:** unit tests and different scenarios.

**Key principles:** simple; loose coupling (objects independent, minimal dependencies); high cohesion (each class has one responsibility); encapsulation (hide details, expose only what is needed); abstraction (focus on essentials); reusability; extensibility.

**Choosing objects.** Look for **nouns** in the problem statement. Example, "Design a Parking Lot System": ParkingLot, Vehicle, ParkingSpot, Ticket, Payment, Entrance, Exit. Do not blindly create classes: think about responsibility, one class = one responsibility (SRP), avoid "god" classes, prefer composition over inheritance, program to interfaces.

**Relationship types:** Association (uses), Aggregation (has-a, weak), Composition (strong has-a), Inheritance (is-a), Dependency (depends on).

**Multiplicities:** `1` exactly one; `0..1` zero or one; `*` zero or more; `1..*` one or more; `m..n` between m and n; `n` exactly n. Example: `ParkingLot 1 — has — * ParkingSpot`.

### 5.4 HLD vs LLD

| | High-Level Design | Low-Level Design |
|---|---|---|
| Goal | Overall system design and architecture | Detailed design of individual components and classes |
| Focus | System components and their relationships | Classes, methods, attributes and their interactions |
| Level | System-level (macro) | Module-level (micro) |
| Created by | Solution architect | Developers / designers |
| Contains | Modules, components, data flow, technologies | Classes, objects, methods, interfaces, relationships |
| Diagrams | Architecture, component, deployment | Class, sequence, activity, state |
| Example | The architecture of BookMyShow | The Booking, Payment and Seat Management modules |

**HLD answers "what"; LLD answers "how".** Ride-booking app example: HLD = User, Driver, Payment and Notification services, DB, APIs. LLD = User, Driver, Booking and Payment classes with methods, attributes and relations.

**LLD interview tips:** understand the requirements; identify entities, attributes and responsibilities; choose the right objects and classes; apply SOLID; use design patterns where required; draw diagrams; handle edge cases; keep the design extensible and maintainable; communicate your thought process; review and refine. *Good design is simple, flexible and easy to extend.*

### 5.5 UML and the 10 diagram types

UML (Unified Modeling Language) is a standard visual language for modeling software: a common way to visualize systems, better team communication, and a blueprint for developers. You do not need every diagram every time; use the ones that add the most value.

| # | Diagram | Shows | Use for |
|---|---|---|---|
| 1 | **Class** | Classes, attributes, methods, relationships | Structure of classes and relationships |
| 2 | **Sequence** | Object interactions in time order | How objects interact over time |
| 3 | **Activity** | Flow of activities or business processes | Workflows and business processes |
| 4 | **State** | States of an object and transitions | State transitions of objects |
| 5 | **Use case** | System functionality from the user's view | Requirements and system scope |
| 6 | **Component** | System components and dependencies | Components and their dependencies |
| 7 | **Deployment** | Physical deployment of artifacts on hardware nodes | Deployment architecture |
| 8 | **Package** | How packages are organized and depend on each other | Organizing model elements |
| 9 | **Communication** | Object interactions and the links between them | Alternative to a sequence diagram (focus on links) |
| 10 | **Object** | Instances of classes at a point in time | A snapshot of objects and their values |

**Visibility notation:** `+` public (everywhere), `-` private (within the class), `#` protected (class and subclasses), `~` package (within the package). **Class notation:** a box with the class name, attributes (`- attribute: Type`) and methods (`+ method(): Type`).

### 5.6 OOP concepts (the foundation of LLD)

OOP is a paradigm built on **objects** that contain data (attributes) and code (methods). Benefits: modularity, reusability, maintainability, scalability, flexibility, real-world modeling.

| Pillar | Meaning | Example |
|---|---|---|
| **Encapsulation** | Bundle data and the methods that operate on it into one unit and restrict direct access | `Account` with private `balance` and `pin`, public `deposit()` / `withdraw()` |
| **Abstraction** | Hide unnecessary detail and show only essentials | `Shape` with `draw()`, implemented by `Circle` and `Rectangle` |
| **Inheritance** | A child class inherits properties and behavior from a parent | `Car` is a `Vehicle` (`start`, `stop`, plus `drive`) |
| **Polymorphism** | One interface, many forms | `Payment.pay()` implemented by `UPIPayment`, `CardPayment`, `WalletPayment` |

**Class vs object:** a class is the blueprint; an object is an instance. Example: class `Student (name, rollNo, study())` creates objects `s1` (Abhi, 101) and `s2` (Rohit, 102).

**Access modifiers**

| Modifier | Same class | Same package | Subclass (other package) | Other package |
|---|---|---|---|---|
| public | yes | yes | yes | yes |
| protected | yes | yes | yes | no |
| default (package-private) | yes | yes | no | no |
| private | yes | no | no | no |

**Best practices:** follow SOLID; keep classes small and focused; prefer composition over inheritance; program to interfaces; write clean, readable, maintainable code. *Treat objects as real-world entities. Focus on what they do, not how they do it. OOP is a tool, not a rule.*

**When to use OOP in LLD:** many related entities; a system expected to grow and change; need for reusability and extensibility; modeling real-world scenarios.

### 5.7 SOLID principles

| Principle | Rule | Example |
|---|---|---|
| **S** Single Responsibility | A class has one reason to change | `Invoice` calculates the total; `InvoicePrinter` prints it |
| **O** Open/Closed | Open for extension, closed for modification | A `Shape` interface lets you add new shapes without changing existing code |
| **L** Liskov Substitution | Subclass objects can replace superclass objects without breaking the app | `Penguin` is not a `Bird` that can `fly()`, so it should not inherit a `fly()` it cannot do |
| **I** Interface Segregation | Do not force a class to implement interfaces it does not use | Split a fat `Worker` (work, eat, sleep) so `Robot` implements only `work` |
| **D** Dependency Inversion | High-level modules should not depend on low-level ones; both depend on abstractions | `OrderService` depends on a `PaymentGateway` interface, not on Razorpay or PayPal directly |

Why SOLID matters: less coupling between classes, better readability, better reusability and testability, easier change and extension.

**Common OOP vocabulary:** Class (blueprint, `class Car {}`); Object (instance, `Car c1 = new Car();`); Attribute (property, `String name;`); Method (behavior, `void start();`); Constructor (initializer, `Car() {}`); Encapsulation (`private String name;`); Abstraction (`interface Shape {}`); Inheritance (`class Bike extends Vehicle {}`); Polymorphism (`Shape s = new Circle(); s.draw();`).

---

## Part 6 — The big interview book and the "System Design Basics" section

### 6.1 Finding things in `SYSTEM-DESIGN-INTERVIEW-BOOK-DIGEST.md`

- **Concept chapters (1-217, in Parts 1-10):** Foundations 1-20, Networking 21-59, Databases 60-96, Caching 97-116, Messaging 117-138, Microservices 139-153, Cloud 154-172, Design Patterns 173-192, Security 193-204, Monitoring 205-217.
- **17 LLD systems:** Parking Lot, Library Management, Hotel Management, Cab Booking, Food Delivery, Movie Ticket Booking, ATM Machine, Elevator, Chess, Snake Game, Splitwise, BookMyShow, Amazon Shopping Cart, WhatsApp, Instagram, Netflix, Uber.
- **12 HLD systems:** TinyURL, YouTube, Netflix, WhatsApp, Instagram, Twitter/X, Uber, Google Drive / Dropbox, Zoom, Notification Service, Distributed Rate Limiter, Web Crawler.
- **Interview prep:** 100 FAANG-style questions, 20 incident scenarios, 20 MCQs, mistakes to avoid, the 6-step framework (Clarify → Estimate → High-level design → Deep dive → Failure and trade-offs → Wrap-up).
- **Deep dives (218-244):** Raft and Paxos, distributed transactions (2PC/3PC), logical and vector clocks, gossip, write-ahead logs, B-trees vs LSM-trees, storage engines, query planning, Kafka internals, consumer-group rebalancing, stream processing, exactly-once, Redis internals and cluster, cache coherence, L4 vs L7 load balancing, gateway patterns, bulkhead and backpressure, strangler fig migration, Kubernetes (pods, networking, operators, multi-cluster and GitOps), AWS Well-Architected, multi-region DR, serverless event-driven architecture, cost optimization.

### 6.2 "System Design Basics" (from the campus-placement guide in the same PDF, p. 1314)

- **Scalability.** Vertical: add resources to one server (easy; hardware limit and single point of failure). Horizontal: add servers (near-unlimited and redundant; more complexity and data-consistency issues). Example architecture: Load Balancer → Server 1, 2, 3 → Database (replicated) → Cache (Redis/Memcached).
- **Load balancing.** Distributes traffic. Algorithms: Round Robin (equal), Weighted Round Robin (by capacity), Least Connections (least loaded), IP Hash (same client, same server). Types: Layer 4 (transport: TCP/UDP) and Layer 7 (application: HTTP, content rules).
- **Caching.** Stores frequently used data. Types: client-side (browser cache, local storage), server-side (Redis, Memcached), CDN cache (distributed edge servers). Invalidation: TTL (auto-expire), LRU (remove unused), explicit invalidation (manual clearing).
- **Database sharding.** Strategies: range-based (e.g. user ID ranges), hash-based (a hash function), directory-based (a lookup table). Example: users 1-1000 → DB1, 1001-2000 → DB2, 2001-3000 → DB3.
- **CDN.** Serves content from the closest server: less latency, less server load, global availability.
- **Microservices.** Break a monolith into small independent services. Benefits: independent scaling, technology flexibility, fault isolation. Challenges: distributed-system complexity, data consistency, network latency.
- **Takeaways.** Horizontal scaling for large systems; load balancing distributes traffic; caching improves performance; sharding handles scale; a CDN reduces global latency; microservices give flexibility at the cost of complexity.

---

## Part 7 — One-page recall: where each idea lives

| If the question is about... | Start with |
|---|---|
| Reaching a server (DNS, HTTP/HTTPS, proxies, latency) | Part 1 items 1-6; book chapters 21-46 |
| API style (REST, GraphQL, gRPC, RPC) | Part 1 items 7-9; Part 3.2; book chapters 31-33 |
| Database choice, indexing, replication, sharding, denormalization | Part 1 items 10-20; Part 3.1 items 6, 10, 13; book chapters 60-96 |
| Scaling and load balancing | Part 1 items 12-14; Part 3.1 items 1, 5; book chapters 14-15, 42, 233 |
| Caching, eviction, consistent hashing, Bloom filters | Part 1 item 19; Part 3.1 items 11, 12, 19; book chapters 97-116 |
| Consistency, CAP, consensus | Part 1 item 21; Part 3.1 items 4, 14; book chapters 16-19, 218-219 |
| Async messaging, webhooks, WebSockets, event-driven | Part 1 items 24-27; Part 3.2; book chapters 117-138 |
| Protecting a system (rate limiting, gateway, idempotency, circuit breakers) | Part 1 items 28-30; Part 3.4 step 7; book chapters 55-59, 139-153 |
| How to run the interview | Part 3.4 (7 steps), 3.5 (40 tips), Part 6 framework; book Part 13 |
| Practice systems | Part 3.6 (10 questions); book HLD 1-12 and 100 FAANG questions |
| Object-oriented / low-level design | Part 5; book LLD 1-17 |

*Gaps to fill if you want more:* the 50-question guide (only about 12 questions were captured) and the four other books bundled in the Topmate PDF (cloud computing, DSA, SQL, placement guide), which are outside system design.
