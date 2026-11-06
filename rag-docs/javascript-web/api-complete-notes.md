---
title: API-COMPLETE-NOTES
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/API-COMPLETE-NOTES.md
---

# API & REST — Complete Study Notes

---

## 1. Foundations

### What is an API?
An **API (Application Programming Interface)** is a set of rules and protocols that lets two applications talk
to each other. It is the intermediary between **client** and **server** — it exposes *what* you can do and
hides *how* it's done.

Why they matter:
- Apps and websites share data and features without sharing code.
- Development gets faster: you connect to an existing service instead of rebuilding it.

### What is REST?
**REST (Representational State Transfer)** is an *architectural style* — not a protocol — for designing
networked applications. It rides on standard HTTP methods to perform **CRUD** operations on **resources**.

### REST vs SOAP

| | REST | SOAP |
|---|---|---|
| Nature | Architectural style | Protocol |
| Transport | HTTP only | HTTP, SMTP, TCP, etc. |
| Weight | Lightweight | Heavyweight |
| Formats | JSON, XML, plain text, HTML | XML only |
| State | Stateless | Can be stateful |
| Performance | Better performance & scalability | Lower performance |
| Where used | Web + mobile apps | Enterprise applications |

Interview line: *REST is a style over HTTP; SOAP is a strict XML protocol with built-in standards (WS-Security,
WS-AtomicTransaction) that you pay for in verbosity.*

### Client–Server architecture
Client and server are **independent** — either can be rewritten as long as the contract holds.
- **Client**: sends requests, handles the UI.
- **Server**: processes requests, manages data, sends responses.

### Resource-based architecture
Everything in REST is a **resource**, identified by a unique **URI**. The URI identifies the resource;
the **representation** (JSON / XML / HTML / plain text) is the current state of it.

```
Resources          Representations
/users             JSON
/users/1           XML
/products/10       Plain text
/orders/100        HTML
```

### The 5 REST constraints
1. **Client–Server** — separation of concerns between client and server.
2. **Stateless** — every request carries all information needed; the server stores no client session state.
3. **Cacheable** — responses must declare themselves cacheable or non-cacheable.
4. **Uniform Interface** — one consistent way to interact: resources, methods, representations.
5. **Layered System** — the client cannot tell whether it's connected to the end server or to an intermediary
   (proxy, load balancer, gateway).

> A sixth, *optional* constraint in Fielding's original thesis is **Code on Demand** (server ships executable
> code to the client). It is not in the source notes; mention it only if asked.

### Why REST is widely used
Simple to understand · uses standard HTTP methods · lightweight and flexible · multiple data formats ·
stateless → scales horizontally · works well for mobile and web · easy to test and maintain.

### How a REST API works
```
Client  --1. HTTP Request (GET/POST/PUT/DELETE)-->  REST API
REST API --2. Process request-->  Database / Data source
Database --3. HTTP Response (JSON/XML)--> Client
```

---

## 2. HTTP Methods

HTTP methods (verbs) perform operations on the resource identified by the URI.

| Method | Purpose | Idempotent | Safe | Example | Typical use |
|---|---|---|---|---|---|
| **GET** (Read) | Retrieve data | Yes | Yes | `GET /users`, `GET /users/10` | List all users, get user by id |
| **POST** (Create) | Create a new resource | **No** | **No** | `POST /users` | Create user, submit form data |
| **PUT** (Update) | Update/replace a resource entirely | Yes | No | `PUT /users/10` | Full update, replace user info |
| **PATCH** (Partial update) | Partially update a resource | Yes* | No | `PATCH /users/10` | Change a single field |
| **DELETE** | Delete a resource | Yes | No | `DELETE /users/10` | Remove resource |
| **OPTIONS** (Info) | Which methods are supported | Yes | Yes | `OPTIONS /users` | CORS preflight |
| **HEAD** | Like GET but headers only, no body | Yes | Yes | `HEAD /users/10` | Check existence, get metadata |

\* The source sheet lists PATCH as idempotent in one table and non-idempotent in another. **The correct answer
for an interview: PATCH is *not guaranteed* idempotent** — it depends on the patch document. `{"status":"active"}`
is idempotent; `{"op":"increment","field":"views"}` is not. Say that and you've beaten the flashcard.

**Idempotent** = calling it N times produces the same result as calling it once, with no extra side effects.
Example: `PUT /users/10` with the same body 5 times → the same user data.

**Safe** = does not change server state. Safe methods: **GET, HEAD, OPTIONS**.

### CRUD mapping
| Method | Create | Read | Update | Delete | Idempotent | Safe |
|---|---|---|---|---|---|---|
| GET | | ✓ | | | ✓ | ✓ |
| POST | ✓ | | | | ✗ | ✗ |
| PUT | | | ✓ | | ✓ | ✗ |
| PATCH | | | ✓ | | ~ | ✗ |
| DELETE | | | | ✓ | ✓ | ✗ |
| OPTIONS | | | | | ✓ | ✓ |
| HEAD | | ✓ | | | ✓ | ✓ |

**Interview tips:** use the correct method for the operation · GET must never change data ·
PUT replaces the whole resource, PATCH updates part of it.

---

## 3. HTTP Status Codes

### 2xx — Success
| Code | Name | Meaning |
|---|---|---|
| 200 | OK | Request was successful |
| 201 | Created | Resource created successfully |
| 204 | No Content | Success, nothing to return (typical for DELETE) |
| 205 | Reset Content | Success, client should reset the form |

### 3xx — Redirection
| Code | Name | Meaning |
|---|---|---|
| 301 | Moved Permanently | Resource permanently at a new URL |
| 302 | Found | Temporarily moved to another URL |
| 304 | Not Modified | Unchanged since last request (caching) |
| 307 | Temporary Redirect | Like 302, but method and body are preserved |

### 4xx — Client errors
| Code | Name | Meaning |
|---|---|---|
| 400 | Bad Request | Invalid syntax; server can't process it |
| 401 | Unauthorized | Authentication missing or failed |
| 403 | Forbidden | Authenticated, but not allowed |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Method known but unsupported for this resource |
| 409 | Conflict | Conflicts with current state (duplicate, version clash) |
| 422 | Unprocessable Entity | Syntactically valid, semantically wrong |

**401 vs 403** is the classic trap: 401 = *who are you?* 403 = *I know who you are, and no.*

### 5xx — Server errors
| Code | Name | Meaning |
|---|---|---|
| 500 | Internal Server Error | Unexpected condition on the server |
| 502 | Bad Gateway | Gateway/proxy got an invalid upstream response |
| 503 | Service Unavailable | Not ready — overloaded or down |
| 504 | Gateway Timeout | Gateway/proxy got no timely upstream response |
| 505 | HTTP Version Not Supported | Protocol version unsupported |

Summary: **2xx** success · **3xx** redirection · **4xx** client error · **5xx** server error.

**Interview tip:** never return `200 OK` for everything. The status code is part of your API contract.

---

## 4. Request & Response Anatomy

### HTTP Request — 5 parts
1. **URL** — the endpoint. `POST /api/users`
2. **Query parameters** (`?`) — optional filter / sort / search. `/api/users?page=1&limit=10`
3. **Path parameters** — values inside the path. `/api/users/10`
4. **Headers** — metadata:
   - `Authorization: Bearer <token>`
   - `Content-Type: application/json`
   - `Accept: application/json`
5. **Body (payload)** — data sent to the server (POST, PUT, PATCH), usually JSON.

```http
POST /api/users HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json
Accept: application/json

{
  "name": "John Doe",
  "email": "john@email.com",
  "age": 25,
  "isActive": true
}
```

### HTTP Response — 3 parts
1. **Status line** — HTTP version + status code + status message
2. **Headers** — metadata about the response
3. **Body** — the actual data, usually JSON

```http
HTTP/1.1 201 Created
Content-Type: application/json
Date: Sun, 12 May 2024 10:30:00 GMT
Content-Length: 112

{
  "id": 1,
  "name": "John Doe",
  "email": "john@email.com",
  "age": 25,
  "isActive": true,
  "createdAt": "2024-05-12T10:30:00.00Z"
}
```

### When each code occurs
| Code | When |
|---|---|
| 200 OK | Successful GET, PUT, PATCH |
| 201 Created | New resource created (POST) |
| 204 No Content | Resource deleted (DELETE) |
| 400 Bad Request | Invalid data or parameters |
| 401 Unauthorized | No token / invalid token |
| 403 Forbidden | Not allowed to access the resource |
| 404 Not Found | Resource does not exist |
| 500 Internal Server Error | Unexpected server error |

**Notes:** headers and body are optional for some methods (e.g. GET) · send data as JSON ·
use the appropriate method · keep requests stateless.

**Flow:** Client → HTTP request → REST API → process → Database → fetch/save → REST API → HTTP response → Client.

---

## 5. REST API Best Practices

### 1. Use nouns, not verbs
URIs represent *resources*, not actions.

| ✗ Avoid | ✓ Use |
|---|---|
| `/getUsers` | `/users` |
| `/createUser` | `/users` |
| `/deleteUser/10` | `/users/10` |

The verb is already in the HTTP method. Repeating it in the URI is redundant.

### 2. Use plural nouns, nest for relationships
```
/users              (collection)
/users/10           (specific user)
/users/123/orders   (that user's orders)
/products
/categories/5/products
/products/456/reviews
```

### 3. Use proper HTTP methods
See §2. GET reads, POST creates, PUT replaces, PATCH partially updates, DELETE removes.

### 4. Filtering, sorting, searching — via query params
```
/users?role=admin
/users?status=active&role=admin
/users?sort=name&order=asc
/users?search=john
/products?category=books&sort=price&order=desc
/orders?dateFrom=2024-01-01&dateTo=2024-01-31
```
Keep it simple and consistent across every endpoint.

### 5. Pagination
Return large datasets in chunks; include the total count when you can.
```
/users?page=1&limit=10
/users?page=2&limit=10&sort=name
/users?limit=20&offset=40
```
```json
{
  "data": [ ... ],
  "pagination": { "page": 2, "limit": 10, "total": 150, "totalPages": 15 }
}
```
`page/limit` and `limit/offset` are two styles of the same idea — pick one and stay with it.

### 6. Version your API
Versioning lets you ship breaking changes without breaking existing clients.
```
/api/v1/users
/api/v2/users
/api/v1/products/10
```

### 7. Consistent error handling
Proper status codes, meaningful messages, one shape everywhere.
```json
{
  "success": false,
  "statusCode": 404,
  "message": "User not found",
  "errors": []
}
```

### 8. Standard response format
```json
{
  "success": true,
  "message": "User retrieved successfully",
  "data": { "id": 10, "name": "John Doe", "email": "john@email.com" }
}
```
Consistency is what makes clients easy to write. Return relevant data only.

### 9. Security best practices
HTTPS always · authenticate requests · authorize access · validate all inputs · prevent SQLi/XSS/CSRF ·
rate limit to prevent abuse · never expose sensitive data.

### 10. Log & monitor
Log request method & URL, request/response time, status code, errors & exceptions, user/IP.
Logging is what makes debugging and auditing possible after the fact.

---

## 6. Authentication & Security

### Authentication vs Authorization
| Authentication | Authorization |
|---|---|
| *Are you who you claim to be?* | *Do you have permission?* |
| Confirms identity (login) | Checks permissions (access control) |
| Login, JWT, API key | Roles, policies, claims |

Authentication always comes first; authorization decides what happens next.

### Authentication methods
1. **JWT (JSON Web Token)** — stateless. The token carries user claims and is digitally signed.
   No server-side session store needed.
2. **Bearer Token** — the transport convention: `Authorization: Bearer <token>`.
3. **OAuth 2.0** — an authorization framework for *delegated* access. Powers "Sign in with Google/GitHub".
4. **API Key** — a simple key in a header or query string. Fine for server-to-server.

### JWT authentication flow
```
1. Client logs in (username/password)
2. Auth server validates credentials
3. Auth server generates a JWT
4. Client sends the token on each request: Authorization: Bearer <token>
5. REST API validates the token and processes the request (hits the DB)
6. API returns the response
```
JWT is stateless → no sessions stored on the server → easy horizontal scaling.

### HTTPS (SSL/TLS)
Always. Encrypts data in transit; prevents eavesdropping and man-in-the-middle attacks.

### CORS (Cross-Origin Resource Sharing)
Allows or restricts requests from a domain other than the API's own.
```
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```
This is where `OPTIONS` earns its keep — the browser sends a **preflight** `OPTIONS` request first.

### Rate limiting
Cap requests per client per time window (e.g. 100 req/min, or 100 requests / IP / 15 minutes).
Prevents abuse and brute force. Key it by IP, user, or API key.

### Input validation
Validate everything **server side**. Check data type, length, format, range. Prevents injection attacks.
Client-side validation is UX; server-side validation is security.

### Common threats → mitigations
| Threat | Mitigation |
|---|---|
| SQL Injection | Parameterized queries |
| XSS (Cross-Site Scripting) | Encode output |
| CSRF (Cross-Site Request Forgery) | Anti-forgery tokens |
| Broken authentication | Strong auth (JWT / OAuth) |
| Sensitive data exposure | Encrypt sensitive data |
| Mass assignment | Validate and whitelist fields |
| Security misconfiguration | Secure configurations |

### Other practices
Strong password hashing (BCrypt, Argon2) · short-lived tokens + refresh tokens · secrets in environment
variables · log and monitor security events · keep dependencies updated · error handling that leaks nothing.

---

## 7. Testing & Documentation

### Testing tools
| Tool | What it's for |
|---|---|
| **Postman** | Send requests, view responses, set headers, write tests |
| **Swagger UI** | Interactive API testing from the spec |
| **curl** | Command-line |
| **Insomnia** | Lightweight REST client |
| **Thunder Client** | VS Code extension |

### Postman workflow
1. Create request (`GET /users`)
2. Set headers (key/value)
3. Add params / body
4. Send
5. Validate response (status 200 OK, body)
6. Write tests

Sample request:
```
GET https://api.example.com/users/1
Authorization: Bearer <token>
Accept: application/json
?include=orders
```

### Automated tests (Postman scripts)
```js
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response time is less than 500ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Response has name", function () {
  var jsonData = pm.response.json();
  pm.expect(jsonData.name).to.exist;
});
```

### What to document
Base URL · authentication · endpoints · request (headers, params, body) · response (status codes, body) ·
error codes · examples.

### OpenAPI / Swagger
OpenAPI (formerly Swagger) is the specification for documenting REST APIs. It generates interactive docs
(Swagger UI) and supports request/response schemas, models, and auth.

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get all users
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
```

**Best practices:** test positive *and* negative cases · validate status codes and response data ·
use environment variables in Postman · automate for regression · keep docs in sync with the API.

---

## 8. Types of APIs

### 1) REST API — Representational State Transfer
A widely used web architecture for communication over HTTP.
**Use when:** you need a simple, stateless API over HTTP methods; best for CRUD.
```js
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### 2) SOAP API — Simple Object Access Protocol
A protocol for exchanging structured information, common in enterprise apps.
**Use when:** strict standards and high security are required — financial services, payment gateways,
enterprise-level systems.
```js
const soap = require('soap');
const url = 'https://example.com/service?wsdl';
soap.createClient(url, (err, client) => {
  client.MyFunction(args, (err, result) => {
    console.log(result);
  });
});
```

### 3) GraphQL API
A query language for APIs; the client requests exactly the fields it needs.
**Use when:** you want control over what you fetch (avoiding over-fetching), or you have complex
data relationships.
```js
const query = `
  query {
    posts {
      id
      title
      author { name }
    }
  }
`;
fetch('https://example.com/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query })
})
  .then(response => response.json())
  .then(data => console.log(data));
```
Note the shape: GraphQL is one endpoint, always POST, and the "method" lives in the query body.

### 4) WebSocket API
Real-time, two-way communication over a persistent connection.
**Use when:** chat, live updates, low latency, continuous data flow.
```js
const socket = new WebSocket('wss://example.com/socket');
socket.onopen = () => socket.send('Hello Server');
socket.onmessage = (event) => console.log('Message from server:', event.data);
```

### Which one to choose?
- **REST** — most web applications and services. Simple, flexible, universally supported.
- **SOAP** — legacy enterprise systems with strict standards. More setup, more security and reliability.
- **GraphQL** — complex data fetching; clients specify exactly what they need. Good for evolving schemas.
- **WebSocket** — anything real-time and bidirectional.

### Key decision factors
1. **Data complexity** — REST is simple; GraphQL is flexible for complex data; SOAP for strict predefined structures.
2. **Real-time needs** — WebSocket for two-way real-time.
3. **Security** — SOAP offers higher built-in security for financial/enterprise use.
4. **Scalability** — REST is highly scalable, the default for most web apps.

---

## 9. Free APIs to Practice With

| # | API | What it gives you | Good for |
|---|---|---|---|
| 1 | **JSONPlaceholder** | Fake posts and users | Front-end testing with no backend |
| 2 | **OpenWeatherMap** | Real-time weather + forecasts | Weather apps |
| 3 | **CoinGecko** | Crypto prices, market caps | Crypto dashboards |
| 4 | **Unsplash** | High-quality free photos | Visually rich apps |
| 5 | **The Cat API** | Random cat images and facts | Fun / pet projects |
| 6 | **Giphy** | Millions of GIFs | Animated content, search features |
| 7 | **NewsAPI** | Live news headlines and articles | News apps, aggregators |
| 8 | **PokeAPI** | Pokémon species and abilities | Games, fan projects |
| 9 | **JokeAPI** | Random jokes by category | Entertainment apps |
| 10 | **REST Countries** | Population, currencies, country data | Travel, geography apps |
| 11 | **Dog CEO's Dog API** | Random dog images by breed | Pet apps, image generators |
| 12 | **ReqRes** | Mock user data, HTTP request testing | Frontend workflow testing |
| 13 | **IPify** | Public IP address of the user | Geolocation, IP features |
| 14 | **RandomUser.me** | Random names, avatars, user data | Auth and profile page testing |
| 15 | **Open Library** | Books and authors database | Book / education apps |
| 16 | **NASA Open APIs** | Astronomy pictures, planetary data | Educational, space apps |
| 17 | **Genderize.io** | Predicts gender from a name | Demographic analysis |
| 18 | **Currency Exchange Rates** | Real-time conversion data | Finance, global markets |
| 19 | **MealDB** | Meals and recipes | Food apps, cooking blogs |
| 20 | **NumbersAPI** | Random facts about numbers | Fun / educational |
| 21 | **Universities API** | Universities worldwide | Education apps |
| 22 | **IPGeoLocation** | Geolocation from IP | Personalization |
| 23 | **Fun Translations** | Yoda-speak, Minion-speak | Light-hearted projects |
| 24 | **Open Trivia Database** | Trivia questions by category | Quiz apps |
| 25 | **Bored API** | Random activity suggestions | Recreation apps |

**Practice path that maps to your stack:** JSONPlaceholder → learn request/response shapes ·
ReqRes → practice POST/PUT/DELETE and auth flows · OpenWeatherMap or CoinGecko → build a real
ingestion job (paginate, rate limit, retry, land raw JSON to S3, then flatten with Spark).

---

## 10. Quick Recall Sheet

**5 REST constraints:** Client–Server · Stateless · Cacheable · Uniform Interface · Layered System.

**Safe methods:** GET, HEAD, OPTIONS.
**Idempotent methods:** GET, PUT, DELETE, HEAD, OPTIONS (PATCH: depends).
**Neither:** POST.

**Status codes worth memorizing cold:** 200, 201, 204 · 301, 304 · 400, 401, 403, 404, 405, 409, 422 · 500, 502, 503, 504.

**401 vs 403:** unauthenticated vs unauthorized.
**PUT vs PATCH:** full replace vs partial update.
**POST vs PUT:** POST creates (server assigns the id, not idempotent); PUT replaces at a known URI (idempotent).
**REST vs GraphQL:** many endpoints, fixed shapes vs one endpoint, client-defined shape.

**URI rules:** nouns · plural · nested for relationships · no verbs · version prefix (`/api/v1/`).

---

## 11. Progressive Quiz

1. What does REST stand for, and is it a protocol or a style?
2. Which HTTP methods are safe? Which are idempotent?
3. `POST /users` twice with the same body — how many users exist? Why?
4. When does a DELETE return 204 rather than 200?
5. A client sends a valid JSON body with an email of `"notanemail"`. 400 or 422? Justify.
6. Why is statelessness what makes a REST API horizontally scalable?
7. A browser calls your API from another origin and you see an `OPTIONS` request you never wrote. Explain.
8. You must add a required field to a response used by mobile clients you can't force-update. What do you do?
9. Design pagination for a 10-million-row table where `offset` gets slow. What replaces `page/limit`?
10. When would you pick GraphQL over REST, and what does it cost you? (Hint: caching, rate limiting, query complexity.)

Answers 1–7 are in these notes. 8–10 are the ones that separate a junior from a senior — write your own
answer first, then ask for a grade.

---

## Sources
- `api/restapi.pdf` — *Master REST APIs Before Your Next Interview*, Touseef Asif (§1–7)
- `api/different aPi.pdf` — *Types of APIs*, @MohitDecodes (§8)
- `api/free apis.pdf` — *25+ Free APIs You Should Know*, @MohitDecodes (§9)

Related: [[NODEJS-COMPLETE-NOTES]] · [[java-springboot-complete-notes]] · [[REACT-COMPLETE-NOTES]]
