---
title: Enterprise Spring Boot course — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Enterprise Spring Boot Course — Study Notes

## Frameworks and builds

A **framework** calls your code (inversion of control); a **library** is code you call. Spring is a framework: you write beans and Spring wires and runs them.

- A plain **JAR** contains your compiled classes. Spring Boot builds an **executable "fat" JAR** that also contains every dependency and an embedded server, so `java -jar app.jar` is enough to run it.
- Maven builds it in the `package` phase via the Spring Boot plugin.

## Dependency injection

Spring keeps an **application context** — a container of objects called **beans** — and injects them where they're needed.

Ways to define beans:
- **Component scanning**: annotate a class with `@Component`, `@Service`, `@Repository` or `@Controller`.
- **`@Bean` methods** in a `@Configuration` class: for third-party classes you can't annotate, or when creation needs logic.

```java
@Configuration
class ClockConfig {
    @Bean
    Clock clock() { return Clock.systemUTC(); }
}
```

**Constructor injection** is preferred over field injection (`@Autowired` on a field): dependencies are explicit, fields can be `final`, and tests can pass mocks directly.

## Properties and profiles

- `@Value("${app.greeting}")` injects a single property.
- **`@ConfigurationProperties(prefix = "app")`** binds a whole group of properties to a typed class — safer and easier to validate.
- Property sources have an order of precedence: command-line arguments and environment variables override `application.yml`.
- **Profiles** (`@Profile("dev")`, `application-dev.yml`) switch beans and settings per environment.

## Auto-configuration

Spring Boot looks at the classpath and existing beans and configures sensible defaults: add the JPA starter and a database driver, and a `DataSource` and `EntityManager` appear. It uses **conditional annotations**:

- `@ConditionalOnClass` — only if a class is on the classpath
- `@ConditionalOnMissingBean` — only if you haven't defined your own
- `@ConditionalOnProperty` — only if a property has a value

Defining your own bean usually switches the default off.

## Logging

- Spring Boot uses SLF4J with Logback by default.
- **Levels**: TRACE < DEBUG < INFO < WARN < ERROR. Set per package: `logging.level.com.example=DEBUG`.
- **Appenders** decide where logs go (console, file, rolling file).
- **MDC** (Mapped Diagnostic Context) attaches values like a request id to every log line of a request — very useful when tracing one user's request through many log lines.

## Testing

- **JUnit 5**: `@Test`, `@BeforeEach`, `@ParameterizedTest`, assertions.
- **Mockito**: `mock()`, `when(...).thenReturn(...)`, `verify(...)`.
- **BDD style**: given / when / then structure (`given(...).willReturn(...)` with BDDMockito; AssertJ `assertThat`).
- **Spring test slices**: `@SpringBootTest` (full context), `@WebMvcTest` (controllers only), `@DataJpaTest` (repositories with an in-memory database).
- `@TestConfiguration` adds or replaces beans just for tests.

## REST concepts

- **Richardson Maturity Model**: level 0 (one endpoint, RPC style) → level 1 (resources) → level 2 (HTTP methods + status codes, where most APIs sit) → level 3 (hypermedia links, HATEOAS).
- **Safe** methods don't change state (GET, HEAD). **Idempotent** methods give the same result when repeated (GET, PUT, DELETE); POST is neither.
- Status codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized (not authenticated), 403 Forbidden (authenticated but not allowed), 404 Not Found, 409 Conflict, 500 Internal Server Error.

## Controllers, clients and error handling

- `@RestController` + `@GetMapping`/`@PostMapping`, `@PathVariable`, `@RequestParam`, `@RequestBody`, `ResponseEntity` for full control of status and headers.
- Calling other services: **RestTemplate** (older, blocking), **WebClient** (reactive, non-blocking), and the newer **RestClient**.
- **`@RestControllerAdvice`** with `@ExceptionHandler` methods centralises error responses so every controller returns the same error shape.

## DTOs and JSON/XML

- **DTOs** separate the API shape from internal entities: you can rename or hide fields without changing the database model.
- **Jackson** converts objects ↔ JSON (and XML with an extra module). Annotations like `@JsonProperty`, `@JsonIgnore`, `@JsonFormat` control the output.
- **Springdoc / Swagger** generates OpenAPI docs and an interactive UI from your controllers.

## Spring Security

- Requests pass through a **filter chain** before reaching controllers.
- **Authentication** = who are you; **authorisation** = what may you do.
- `UserDetailsService` loads a user; a `PasswordEncoder` (BCrypt) checks the hashed password.
- **Authorities/roles** grant access; method security with `@PreAuthorize("hasRole('ADMIN')")`, `@Secured`, or JSR-250 `@RolesAllowed`.
- **JWT**: a custom filter reads the `Authorization: Bearer` header, validates the token's signature and expiry, and sets the authenticated user for the request.
- **HTTPS/TLS**: configure a keystore (`server.ssl.*`) or terminate TLS at a load balancer.

## AOP (aspect-oriented programming)

AOP adds cross-cutting behaviour (logging, timing, transactions, security) without editing each method.

- **Aspect**: the class holding the extra behaviour.
- **Pointcut**: which methods it applies to (e.g. all methods in `..service..`).
- **Advice types**: `@Before`, `@After`, `@AfterReturning`, `@AfterThrowing`, `@Around`.
- Spring implements AOP with **proxies** (JDK dynamic proxies for interfaces, CGLIB subclasses otherwise). Consequence: calling a `@Transactional` method from another method in the **same class** skips the proxy, so the transaction doesn't apply.

## Deployment and containers

- Platform-as-a-service deploys (e.g. Heroku-style) run the JAR and inject the port and database URL as environment variables.
- **Docker images** are built in **layers**; put rarely-changing layers (dependencies) before frequently-changing ones (your classes) so rebuilds are fast. Spring Boot can produce layered JARs and build images directly.
- **Docker Compose** runs the app with its database.

## Data access

- **Schema migration** with Flyway/Liquibase: versioned SQL scripts applied in order.
- **JDBC / JdbcTemplate** for direct SQL.
- **JPA entities**: `@Entity`, `@Id`, `@GeneratedValue`, relationships (`@OneToMany`, `@ManyToOne`), lazy vs eager loading.
- **Transactions**: `@Transactional` on service methods; everything inside commits or rolls back together.
- **Spring Data JPA**: extend `CrudRepository`/`JpaRepository` and get CRUD for free; **derived queries** from method names (`findByLastNameAndAgeGreaterThan`), `@Query` for custom JPQL/SQL, **paging and sorting** with `Pageable`, and **query by example**.
- Spring Data also supports **MongoDB** with `MongoRepository` and `MongoTemplate`.

## Layered architecture

Controller → **service tier** (business rules, transactions) → repository. **Mappers** convert between business objects/entities and DTOs (by hand or with a library such as MapStruct).
