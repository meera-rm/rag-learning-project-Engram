---
title: Building a REST API back end with Spring Boot — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Building a REST API Back End with Spring Boot — Study Notes

The path from an empty project to a secured, database-backed API with user management.

## 1. Getting started

- Generate a project with **Spring Initializr** (start.spring.io): choose Maven or Gradle, Java version, and starters such as *Spring Web*, *Spring Data JPA*, *Validation*, *Spring Security*, and a database driver.
- Run it with `./mvnw spring-boot:run`. The embedded Tomcat starts on port 8080.
- A first endpoint:

```java
@RestController
class HelloController {
    @GetMapping("/hello")
    String hello() { return "Hello"; }
}
```

## 2. Designing the sample app

Decide the **resources** first (e.g. `users`, `tasks`) and their URLs:

| Method | URL | Action |
| --- | --- | --- |
| GET | `/api/users` | List users |
| GET | `/api/users/{id}` | One user |
| POST | `/api/users` | Create |
| PUT | `/api/users/{id}` | Replace/update |
| DELETE | `/api/users/{id}` | Delete |

Nouns in URLs, HTTP methods for the verbs, plural resource names.

## 3. User management

- A `User` entity (id, username, email, password hash, roles).
- A `UserRepository extends JpaRepository<User, Long>`.
- A `UserService` with registration logic: check the username isn't taken, **hash the password** (BCrypt), assign a default role.
- Never return the password hash in responses — use a DTO.

## 4. The user REST controller

```java
@RestController
@RequestMapping("/api/users")
class UserController {
    private final UserService users;
    UserController(UserService users) { this.users = users; }

    @PostMapping
    ResponseEntity<UserDto> register(@Valid @RequestBody RegisterRequest req) {
        UserDto created = users.register(req);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @GetMapping("/{id}")
    UserDto get(@PathVariable Long id) { return users.findById(id); }
}
```

Return proper status codes: `201 Created` after POST, `404 Not Found` for a missing id, `400 Bad Request` for invalid input.

## 5. Securing the API

- Add **Spring Security**; by default every endpoint requires authentication.
- Configure which paths are public (registration, login) and which need a role.
- **Token-based auth**: the client logs in, receives an access token (OAuth2 / JWT), and sends it in `Authorization: Bearer <token>` on each request. The server stays **stateless** — no session stored.
- Protect admin actions with roles: `@PreAuthorize("hasRole('ADMIN')")`.
- Use HTTPS so tokens and passwords aren't sent in plain text.

## 6. Moving to a real database

- Development often starts with an in-memory database (H2); production uses PostgreSQL or MySQL.
- Configure `spring.datasource.url`, username and password (from environment variables).
- Manage schema changes with a migration tool (**Flyway** or **Liquibase**) instead of letting Hibernate auto-create tables in production.

## 7. Validation

Bean Validation annotations on request objects:

```java
record RegisterRequest(
    @NotBlank @Size(min = 3, max = 30) String username,
    @Email @NotBlank String email,
    @Size(min = 8) String password) {}
```

`@Valid` on the controller parameter triggers the checks. A `@RestControllerAdvice` turns `MethodArgumentNotValidException` into a clear JSON error listing each bad field.

## 8. File upload

- Accept files with `@RequestParam("file") MultipartFile file`.
- Check size and content type; set limits with `spring.servlet.multipart.max-file-size`.
- Store files outside the web root (or in object storage like S3), generate your own file names to avoid path traversal, and save only the metadata in the database.

## Checklist for a production-ready API

- Consistent error format, correct status codes.
- Input validation on every endpoint.
- Authentication, authorisation by role, HTTPS.
- Database migrations, connection pooling.
- Pagination for list endpoints (`Pageable`).
- Tests: unit tests for services, `@WebMvcTest` for controllers.
