---
title: Web development security — study notes
topic: javascript-web
source_type: my-notes
note_kind: study-notes
---

# Web Development Security — Study Notes

## Core principles

- **Never trust input**: anything from the browser (forms, URLs, headers, cookies, uploaded files) can be forged.
- **Defence in depth**: several layers, so one failure isn't fatal.
- **Least privilege**: every user, service and database account gets only the access it needs.
- **Secure by default**: deny unless explicitly allowed.

## HTTPS and TLS

HTTPS = HTTP over **TLS**. TLS gives:
- **Encryption** — eavesdroppers on the network can't read the traffic.
- **Integrity** — data can't be changed in transit unnoticed.
- **Authentication** — the certificate proves you're talking to the real server.

Add **HSTS** (`Strict-Transport-Security` header) so browsers always use HTTPS for your site, and mark cookies `Secure` so they're never sent over plain HTTP.

## Cross-site scripting (XSS)

An attacker gets their JavaScript to run in another user's browser on your site — it can then steal session data or act as the user.

| Type | How it happens |
| --- | --- |
| Stored | Malicious script saved in the database (e.g. a comment) and shown to every visitor |
| Reflected | Script in a URL parameter echoed back in the page |
| DOM-based | Front-end code writes untrusted data into the page (e.g. `element.innerHTML = location.hash`) |

Defences:
- **Escape output** for its context (HTML, attribute, JavaScript, URL). Frameworks like React escape by default — avoid bypasses such as `dangerouslySetInnerHTML` with untrusted data.
- Use `textContent` instead of `innerHTML` for plain text.
- Sanitise HTML when you must allow some (with a library like DOMPurify).
- **Content Security Policy** as a second layer.
- `HttpOnly` cookies so scripts can't read the session cookie.

## Cross-site request forgery (CSRF)

A malicious site makes the victim's browser send a request to your site; the browser attaches the victim's cookies automatically, so the request looks legitimate (e.g. "transfer money").

Defences:
- **`SameSite` cookies** (`Lax` or `Strict`) so cookies aren't sent on cross-site requests.
- **CSRF tokens**: a random value in the form that the attacker's site can't read or guess.
- Never change state with GET requests.
- APIs using `Authorization: Bearer` headers instead of cookies are not exposed to classic CSRF.

## SQL injection

Untrusted input is concatenated into SQL, so the input changes the query itself.

```javascript
// Vulnerable
db.query("SELECT * FROM users WHERE email = '" + email + "'");

// Safe: parameterised query
db.query("SELECT * FROM users WHERE email = $1", [email]);
```

Also: use ORMs carefully (raw queries can still be vulnerable), give the database user minimal permissions, and validate input types. The same idea applies to NoSQL injection and command injection.

## Authentication and passwords

- Store passwords with a slow, salted hashing algorithm: **bcrypt**, **scrypt** or **Argon2** — never plain text, never fast hashes like MD5/SHA-1.
- Rate-limit login attempts and consider lockouts or CAPTCHAs.
- Offer **multi-factor authentication**.
- Use generic error messages ("invalid email or password") so attackers can't discover which emails exist.
- Secure password reset: single-use, short-lived, random tokens.

## Sessions and JWT

| Server sessions | JWT (JSON Web Token) |
| --- | --- |
| Random session id in a cookie; data stored on the server | Signed token holding claims; server verifies the signature |
| Easy to revoke (delete the session) | Hard to revoke before expiry — keep lifetimes short, use refresh tokens |
| Needs shared session storage when scaled | Stateless |

For cookies: `HttpOnly`, `Secure`, `SameSite`. For JWT: always verify the signature and algorithm, check expiry, don't put secrets in the payload (it's only encoded, not encrypted).

## Authorisation

Authentication says who you are; **authorisation** decides what you can do. Check permissions **on the server for every request**. A classic bug is **IDOR** (insecure direct object reference): `/api/orders/1043` returns any user's order because the server only checks that you're logged in, not that the order is yours.

## CORS

The browser's **same-origin policy** blocks scripts from reading responses from other origins. **CORS** headers let a server relax this for specific origins. Allow only known front-end origins; never combine `Access-Control-Allow-Origin: *` with credentials. CORS is a browser rule — it doesn't protect your API from non-browser clients.

## Security headers and CSP

| Header | Purpose |
| --- | --- |
| `Content-Security-Policy` | Limits where scripts, styles, images can load from; blocks inline scripts |
| `Strict-Transport-Security` | Forces HTTPS |
| `X-Content-Type-Options: nosniff` | Stops the browser guessing file types |
| `X-Frame-Options` / CSP `frame-ancestors` | Prevents clickjacking by forbidding framing |
| `Referrer-Policy` | Controls how much URL info leaks to other sites |

## API security

- Authenticate every endpoint that isn't meant to be public.
- **Rate limiting** to slow brute force and abuse.
- Validate request bodies against a schema; reject unknown fields.
- Don't leak internal details (stack traces) in error messages.
- Pagination limits so one request can't dump the whole database.

## File uploads and path traversal

- Check file type by content, not just extension; limit size.
- Rename files on the server; never use the user's file name in a path — `../../etc/passwd` is **path traversal**.
- Store uploads outside the web root or in object storage, and serve them with a safe content type.

## Secrets management

- Never commit API keys or passwords to Git; use environment variables or a secrets manager.
- Keep `.env` in `.gitignore`.
- Rotate keys if they leak; scan repositories for secrets.
- Front-end code is public — anything in browser JavaScript is not a secret.

## Dependencies and deployment

- Keep libraries updated; run `npm audit` or a dependency scanner in CI.
- Use lock files for reproducible builds.
- Run containers as non-root, keep images small, close unused ports.
- Log security events (failed logins, permission errors) and monitor them.

## OWASP Top 10 (themes)

Broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable/outdated components, identification and authentication failures, software and data integrity failures, security logging and monitoring failures, and server-side request forgery (SSRF — tricking the server into fetching internal URLs).
