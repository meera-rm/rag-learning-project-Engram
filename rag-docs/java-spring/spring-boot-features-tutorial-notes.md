---
title: Spring Boot features tour — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Spring Boot Features Tour — Study Notes

A walk through Spring Boot features from first project to microservices.

## What Spring Boot adds to Spring

- **Starters**: one dependency pulls in a consistent set of libraries (`spring-boot-starter-web`, `-data-jpa`, `-security`, `-test`).
- **Auto-configuration**: sensible defaults based on what's on the classpath.
- **Embedded server**: Tomcat (or Jetty/Undertow) runs inside the app.
- **Production features**: health checks, metrics, externalised config.

## Bootstrapping and runners

- The main class has `@SpringBootApplication` (= `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`) and calls `SpringApplication.run(...)`.
- **`CommandLineRunner` / `ApplicationRunner`** beans run code once the app has started — handy for seeding demo data.

## Deploying to an external Tomcat

The default is an executable JAR. To deploy as a WAR to an existing Tomcat server: change packaging to `war`, mark the embedded Tomcat dependency as `provided`, and extend `SpringBootServletInitializer`.

## Build systems

Maven or Gradle, both with a Spring Boot plugin and a dependency management BOM so you don't specify versions for each Spring library.

## Properties and logging

- `server.port=9090` changes the port (or `server.port=0` for a random one).
- Properties can come from `application.properties`/`.yml`, environment variables, or command-line flags (`--server.port=9090`).
- Logging levels per package and log file output are set in the same file.

## Building REST services

`@RestController`, request mappings, path variables, request params, request bodies, `ResponseEntity`. Exceptions are handled globally with `@ControllerAdvice` + `@ExceptionHandler`.

## Interceptors vs servlet filters

| | Servlet filter | Spring `HandlerInterceptor` |
| --- | --- | --- |
| Level | Servlet container, before Spring MVC | Inside Spring MVC, around controller calls |
| Knows the controller method? | No | Yes |
| Typical use | Encoding, CORS, security, request logging | Auth checks per handler, timing controller calls, adding model data |
| Hooks | `doFilter` | `preHandle`, `postHandle`, `afterCompletion` |

## Consuming REST APIs

`RestTemplate` (blocking, older), `WebClient` (non-blocking), or `RestClient` (newer, fluent and blocking). Set timeouts and handle error responses.

## File handling

Upload with `MultipartFile`; download by returning a `Resource` with a `Content-Disposition` header. Validate file size and type.

## Service components

Business logic goes in `@Service` classes, injected into controllers — keeps controllers thin and logic testable.

## Thymeleaf (server-side pages)

A template engine for HTML pages rendered on the server: a `@Controller` (not `@RestController`) adds data to a `Model` and returns a template name; templates live in `src/main/resources/templates`.

## CORS

Browsers block JavaScript from calling an API on a different origin unless the server allows it. Enable per controller with `@CrossOrigin(origins = "https://myfrontend.com")` or globally via a `WebMvcConfigurer`. Never allow `*` together with credentials.

## Internationalisation (i18n)

Messages in `messages.properties`, `messages_fr.properties`, etc. A `LocaleResolver` picks the language (from a header, cookie or URL parameter), and a `MessageSource` looks up the text.

## Scheduling

`@EnableScheduling` plus `@Scheduled(fixedRate = 60000)` or `@Scheduled(cron = "0 0 2 * * *")` runs a method on a timer (e.g. a nightly cleanup). In a multi-instance deployment, guard against every instance running the job (e.g. with a distributed lock).

## HTTPS

Create a keystore, then set `server.ssl.key-store`, its password and `server.port=8443`. In the cloud, TLS is often terminated at the load balancer instead.

## Microservices with Spring Cloud

| Concern | Tool | What it does |
| --- | --- | --- |
| Service registry | **Eureka** server | Services register themselves; clients look up others by name instead of hard-coded hosts |
| Service registration | Eureka client | A service announces its address and sends heartbeats |
| API gateway | Zuul (older) / **Spring Cloud Gateway** (current) | One entry point that routes requests to the right service, plus cross-cutting filters |
| Central config | **Spring Cloud Config** server | Serves configuration from a Git repo to all services; change config without rebuilding |

## Monitoring

**Actuator** exposes `/actuator/health`, `/actuator/info`, `/actuator/metrics` and more; expose only what's needed and secure the rest. Admin dashboards and Prometheus/Grafana can read these metrics.

## Other features worth knowing

- Sending email with `JavaMailSender`.
- Batch processing with Spring Batch.
- Caching with `@EnableCaching` and `@Cacheable`.
- Database access with Spring Data JPA and JDBC.
- Unit and integration testing with `spring-boot-starter-test`.
