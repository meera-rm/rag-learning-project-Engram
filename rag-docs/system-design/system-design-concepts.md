---
title: SYSTEM-DESIGN-30-CONCEPTS
topic: system-design
source_type: my-notes
source_file: systemdesign/SYSTEM-DESIGN-CONCEPTS.md
---

# System Design Concepts (Study Notes)


**How to read this:** each concept has *What*, *Why it matters*, a *Real-world example*, and the matching *AWS service* (handy for AWS certs).

---

## The big picture: one request's journey

```
User → DNS lookup → CDN (static files) → API Gateway / Reverse Proxy (auth, rate limit)
     → Load Balancer → App servers (horizontally scaled, microservices)
     → Cache (Redis) → Database (primary + read replicas, sharded)
     → Message Queue → background workers   |   Blob storage (S3) for files
```

---

## Part 1 — Basics: how a client reaches a server

### 1. Client-Server Architecture
- **What:** A client (browser, mobile app) sends a request. A server that is always running processes it and sends back a response.
- **Why:** Almost every system design starts from this.
- **Example:** A React app calls `GET /books` on an Express server, which returns JSON.

### 2. IP Address
- **What:** A unique address for a machine on a network, similar to a phone number.
- **Problem:** People can't remember IPs, and they change when you migrate servers. DNS solves this.

### 3. DNS (Domain Name System)
- **What:** Turns `algomaster.io` into an IP address. The browser asks DNS first and then connects to that IP.
- **Try it:** `ping google.com` shows the IP it resolves to.
- **AWS:** Route 53

### 4. Proxy vs Reverse Proxy
| | Forward Proxy | Reverse Proxy |
|---|---|---|
| Sits in front of | Clients | Servers |
| Hides | The client's IP | The servers' IPs |
| Used for | Privacy, corporate filtering, VPN-style access | Security, DDoS filtering, load balancing, SSL termination |
- **Example:** NGINX in front of your Node app.

### 5. Latency
- **What:** The round-trip delay between client and server. Physical distance is the main cause (e.g., NY ↔ India).
- **Fix:** Deploy to several data centers or regions and use CDNs so users connect to the nearest one.
- **AWS:** Multi-region deployments, CloudFront

### 6. HTTP / HTTPS
- **HTTP:** The request/response protocol. A request has a method, headers and an optional body. A response has a status code, headers and a body.
- **HTTPS:** HTTP encrypted with SSL/TLS, so passwords and card numbers can't be read in transit.
- **AWS:** ACM (certificates) on an ALB or CloudFront

---

## Part 2 — APIs

### 7. APIs
- **What:** A contract that lets a client use a server without knowing how it works inside. Usually returns JSON.

### 8. REST
- **What:** Resource-based URLs (`/users`, `/orders/42`) with standard methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove).
- **Key rule:** Stateless. Every request carries everything the server needs.
- **Pros:** Simple, scalable, cacheable. **Cons:** Over-fetching, or needing several calls for related data.

### 9. GraphQL
- **What:** One endpoint where the client asks for exactly the fields it needs (introduced by Facebook in 2015).
- **Example:** User + profile + posts takes 3 REST calls but only 1 GraphQL query.
- **Cons:** More work on the server, and caching is harder.
- **AWS:** AppSync

---

## Part 3 — Databases & scaling

### 10. Databases
- **Why:** Memory is fine for tiny data. Real data needs durable, queryable storage.

### 11. SQL vs NoSQL
| SQL | NoSQL |
|---|---|
| Tables with a fixed schema | Flexible schema |
| ACID transactions | Scales horizontally with ease |
| MySQL, PostgreSQL | Key-value (Redis), Document (MongoDB), Graph (Neo4j), Wide-column (Cassandra) |
| Banking, orders | Feeds, recommendations, sessions |
- **Real systems often use both:** SQL for orders, NoSQL for recommendations.
- **AWS:** RDS/Aurora (SQL), DynamoDB (NoSQL)

### 12. Vertical Scaling (scale UP)
- **What:** Give one machine more CPU, RAM or disk.
- **Cons:** There's a hardware ceiling, cost rises sharply at the top end, and it's a **single point of failure**.
- **AWS:** Move from t3.micro to m5.4xlarge

### 13. Horizontal Scaling (scale OUT)
- **What:** Add more machines that share the work.
- **Pros:** Fault tolerant (others take over if one fails) and uses cheap commodity machines.
- **New problem:** Which server should the client talk to? A load balancer answers that.
- **AWS:** EC2 Auto Scaling Groups

### 14. Load Balancers
- **What:** Spread traffic across servers and skip unhealthy ones (via health checks).
- **Algorithms:**
  - **Round Robin:** Servers take turns.
  - **Least Connections:** Send to the server with the fewest active connections.
  - **IP Hash:** The same client always goes to the same server ("sticky" sessions).
- **AWS:** ALB (layer 7, HTTP), NLB (layer 4, TCP)

### 15. Database Indexing
- **What:** A lookup structure (like a book's index) that points straight to rows, so the database doesn't scan the whole table.
- **Index:** Primary keys, foreign keys, and columns used in WHERE / JOIN / ORDER BY.
- **Trade-off:** Reads get faster, but INSERT, UPDATE and DELETE get slower. Only index the columns you actually query.
- **Example:** `CREATE INDEX idx_users_email ON users(email);`

### 16. Replication
- **What:** One **primary** handles writes and copies them to **read replicas**, which handle SELECTs.
- **Pros:** More read throughput, and high availability because a replica can be promoted if the primary dies.
- **Watch out:** Replication lag means a replica can briefly return stale data.
- **AWS:** RDS Read Replicas, Multi-AZ

### 17. Sharding (horizontal partitioning)
- **What:** Split the **rows** across several databases using a **shard key** (e.g., `user_id % 4`).
- **Pros:** Each database handles less load. **Cons:** Cross-shard queries and joins are hard, and a bad key creates "hot" shards.
- **AWS:** DynamoDB partitions data automatically by partition key

### 18. Vertical Partitioning
- **What:** Split a table by **columns** according to how they're used.
- **Example:** `User` becomes `User_Profile` + `User_Login` + `User_Billing`.
- **Pro:** Queries read fewer columns, so there's less disk I/O.

### 19. Caching
- **What:** Keep hot data in memory so you don't hit the database every time.
- **Cache-aside pattern:**
  1. Check the cache. On a hit, return it.
  2. On a miss, read from the database, write the result to the cache, then return it.
- **TTL (time-to-live):** Expires entries so stale data gets refreshed.
- **Tools:** Redis, Memcached. **AWS:** ElastiCache, DAX (for DynamoDB)

### 20. Denormalization
- **What:** Deliberately duplicate data into one table to avoid expensive JOINs.
- **Trade-off:** Reads get faster, but you use more storage and updates get more complex. Best for **read-heavy** systems.
- **Example:** A `UserOrders` table that stores the user name next to each order.

### 21. CAP Theorem
- **The rule:** A distributed system can guarantee only 2 of these 3: **C**onsistency (everyone sees the same data), **A**vailability (every request gets a response) and **P**artition tolerance (it keeps working when the network splits).
- **Since partitions always happen, the real choice is CP or AP:**
  - **CP:** Banking, inventory (correctness matters most)
  - **AP:** Social feeds, likes (being up matters most), e.g., Cassandra, DynamoDB
- **Eventual consistency:** A write is acknowledged right away, then spreads to replicas, and they all converge over time.

### 22. Blob Storage
- **What:** Stores big unstructured files (images, video, PDFs) in buckets, and each object gets a URL.
- **Pros:** Scales to petabytes, pay-as-you-go, replicated automatically.
- **Rule:** Don't put large files in your database. Store them in S3 and keep the URL in the database.
- **AWS:** S3

### 23. CDN (Content Delivery Network)
- **What:** Edge servers around the world cache static content (HTML, JS, CSS, images, video) close to users.
- **Example:** A user in India streams a video hosted in California from a nearby Indian edge node.
- **AWS:** CloudFront (often with S3 as the origin)

---

## Part 4 — Real-time & communication

### 24. WebSockets
- **Problem:** With plain HTTP the client has to keep polling ("anything new?"), and most answers are empty, which wastes bandwidth.
- **What:** One persistent, **two-way** connection that lets the server push updates instantly.
- **Use for:** Chat, live stock prices, multiplayer games.
- **AWS:** API Gateway WebSocket APIs

### 25. Webhooks
- **What:** Server-to-server push. A provider sends an HTTP POST to your URL when an event happens.
- **Examples:** Stripe → "payment succeeded". GitHub push → triggers CI/CD (Jenkins / GitHub Actions).
- **WebSocket vs Webhook:** A WebSocket is a live connection to a client. A webhook is a one-off callback between servers.

### 26. Microservices
- **Monolith problem:** One codebase. One bug or a risky deploy can take down everything.
- **Microservices:** Small independent services with one job each, their **own database**, and independent scaling and deploys.
- **They talk via:** APIs (synchronous) or message queues (asynchronous).
- **AWS:** ECS/EKS, Lambda

### 27. Message Queues
- **What:** A producer puts a message on a queue, and a consumer processes it later (**asynchronous**).
- **Example:** The checkout service drops an "order placed" message and the payment and email services pick it up.
- **Pros:** Decoupled services, absorbs traffic spikes, keeps messages safe if a consumer is down.
- **Tools:** Kafka, RabbitMQ. **AWS:** SQS (queue), SNS (pub/sub), Kinesis/MSK (streams)

### 28. Rate Limiting
- **What:** Caps requests per client in a time window (e.g., 100 requests/min). Going over returns **HTTP 429 Too Many Requests**.
- **Algorithms:**
  - **Fixed Window:** Count per minute. Simple, but allows bursts at window edges.
  - **Sliding Window:** Smooths out those edge bursts.
  - **Token Bucket:** Tokens refill at a fixed rate and each request spends one. Allows controlled bursts.
- **AWS:** API Gateway throttling, WAF rate-based rules

### 29. API Gateway
- **What:** The single front door for microservices. It handles **auth, rate limiting, logging, monitoring and routing**.
- **Flow:** Client → Gateway (validate) → the right service → response.
- **Tools:** NGINX, Kong. **AWS:** API Gateway

### 30. Idempotency
- **What:** Sending the same request twice has the same effect as sending it once.
- **Why:** Retries, double-clicks and refreshes could otherwise charge a card twice.
- **How:** The client sends a unique **idempotency key**. The server checks whether it has seen that key: if so, it returns the stored result; if not, it processes the request and saves the key.
- **Note:** GET, PUT and DELETE are idempotent by design. POST is not, so it needs a key.

---

## Quick recall sheet
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
