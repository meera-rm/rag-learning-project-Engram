---
title: Spring Boot project structure — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Spring Boot Project Structure — Study Notes

## Standard layout (Maven)

```
my-app/
├── pom.xml                         # dependencies and build settings
├── src/main/java/com/example/app/
│   ├── AppApplication.java         # main class with @SpringBootApplication
│   ├── controller/                 # REST endpoints (@RestController)
│   ├── service/                    # business logic (@Service)
│   ├── repository/                 # database access (@Repository / Spring Data interfaces)
│   ├── model/ or entity/           # JPA entities (@Entity)
│   ├── dto/                        # objects sent to / received from clients
│   ├── config/                     # @Configuration classes, security setup
│   └── exception/                  # custom exceptions and @ControllerAdvice handlers
├── src/main/resources/
│   ├── application.properties      # or application.yml
│   ├── static/                     # CSS, JS, images
│   └── templates/                  # server-side templates (e.g. Thymeleaf)
└── src/test/java/com/example/app/  # tests mirror the main package structure
```

## Why the main class sits at the top package

`@SpringBootApplication` turns on **component scanning** for its own package and every sub-package. Put it in `com.example.app` and Spring finds `com.example.app.controller.*`, `com.example.app.service.*`, and so on. A class in an unrelated package (e.g. `com.other`) won't be found unless you configure scanning.

## The layers and how a request flows

1. **Controller** receives the HTTP request, validates input, and calls the service. It shouldn't contain business rules.
2. **Service** holds business logic and transactions (`@Transactional`).
3. **Repository** talks to the database.
4. The result goes back up; the controller turns it into a DTO/JSON response.

```java
@RestController
@RequestMapping("/api/books")
class BookController {
    private final BookService service;
    BookController(BookService service) { this.service = service; }   // constructor injection

    @GetMapping("/{id}")
    BookDto get(@PathVariable Long id) { return service.findById(id); }
}
```

## Package by layer vs package by feature

| Package by layer | Package by feature |
| --- | --- |
| `controller/`, `service/`, `repository/` | `book/`, `author/`, `order/` (each with its own controller, service, repository) |
| Simple, familiar for small apps | Scales better: related code stays together, fewer cross-package dependencies |

## Configuration files

- `application.properties` / `application.yml`: port, database URL, logging levels.
- Profile-specific files: `application-dev.yml`, `application-prod.yml`, activated with `spring.profiles.active=dev`.
- Never commit real passwords; use environment variables.

## Tests

`src/test/java` mirrors the main packages. Unit tests test one class with mocks; `@SpringBootTest` starts the whole application context for integration tests; `@WebMvcTest` loads only the web layer.
