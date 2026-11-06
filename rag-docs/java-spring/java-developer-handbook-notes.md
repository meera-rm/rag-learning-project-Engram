---
title: Java developer handbook — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Java Developer Handbook — Study Notes

A broad tour of what a working Java developer uses: the language, OOP, the JVM, I/O, databases, build tools, Git, Spring and Docker.

## Java fundamentals

- **Compiled to bytecode**: `javac` turns `.java` into `.class` bytecode; the **JVM** runs it on any OS ("write once, run anywhere").
- **JDK vs JRE vs JVM**: JDK = tools to develop (compiler, debugger) + JRE; JRE = libraries + JVM to run; JVM = the engine executing bytecode.
- **Primitive types**: `int`, `long`, `double`, `boolean`, `char`, `byte`, `short`, `float`. Everything else is an object reference.
- **Control flow**: `if/else`, `switch` (including switch expressions in modern Java), `for`, enhanced `for`, `while`, `do-while`, `break`, `continue`.
- **Strings are immutable**; build strings in a loop with `StringBuilder`.
- **`==` vs `.equals()`**: `==` compares references for objects; `.equals()` compares content.

## Object-oriented programming

| Pillar | Idea | Example |
| --- | --- | --- |
| Encapsulation | Hide fields, expose methods | `private double balance;` with `deposit()` that checks the amount |
| Inheritance | A class reuses another's behaviour | `SavingsAccount extends Account` |
| Polymorphism | One interface, many implementations | `List<String> list = new ArrayList<>();` — swap for `LinkedList` without changing callers |
| Abstraction | Expose what, hide how | An `interface PaymentGateway { void charge(Money m); }` |

**Overloading** = same method name, different parameters (compile time). **Overriding** = subclass replaces a parent method (runtime).

**Abstract class vs interface**: an abstract class can hold state and constructors and supports single inheritance; an interface defines a contract, a class can implement many, and it can have `default` methods.

### SOLID
- **S**ingle responsibility: one reason to change per class.
- **O**pen/closed: extend behaviour without editing existing code (e.g. add a new `PaymentGateway` implementation).
- **L**iskov substitution: a subclass must work wherever the parent works.
- **I**nterface segregation: many small interfaces beat one huge one.
- **D**ependency inversion: depend on interfaces, not concrete classes (what Spring's dependency injection makes easy).

## Collections

| Interface | Common implementation | Notes |
| --- | --- | --- |
| `List` | `ArrayList` | Fast random access; `LinkedList` for frequent inserts at the ends |
| `Set` | `HashSet`, `TreeSet` | No duplicates; `TreeSet` is sorted |
| `Map` | `HashMap`, `TreeMap`, `LinkedHashMap` | Key → value; `LinkedHashMap` keeps insertion order |
| `Queue`/`Deque` | `ArrayDeque`, `PriorityQueue` | FIFO, stack, priority order |

`HashMap` relies on `hashCode()` and `equals()` — override both together.

## Java 8+ features

- **Lambdas**: `list.forEach(x -> System.out.println(x));`
- **Streams**: declarative pipelines.

```java
List<String> names = people.stream()
    .filter(p -> p.getAge() >= 18)
    .map(Person::getName)
    .sorted()
    .toList();
```

- **Optional**: a box that may be empty, to avoid returning `null`.
- **New date/time API**: `LocalDate`, `LocalDateTime`, `Duration`.
- Later versions: `var`, records (`record Point(int x, int y) {}`), text blocks, pattern matching, virtual threads.

## JVM internals

- **Memory areas**: heap (objects, shared), stack (per thread: frames, local variables), metaspace (class metadata).
- **Garbage collection**: frees objects no longer reachable. The heap is split into young and old generations because most objects die young. Collectors include G1 (the common default) and ZGC (very low pause times).
- **Class loading**: bootstrap → platform → application class loaders.
- **JIT compiler**: compiles frequently-run bytecode to native code at runtime.
- **Tuning flags**: `-Xms`/`-Xmx` (starting/maximum heap), `-XX:+UseG1GC` (pick a collector), heap dumps on out-of-memory for debugging.

## Files, I/O and serialization

- `java.nio.file.Files` and `Path` are the modern API: `Files.readAllLines(path)`, `Files.writeString(path, text)`.
- Always close streams (try-with-resources).
- **Serialization** turns an object into bytes (`implements Serializable`); in practice JSON (Jackson) is more common for data exchange.

## Databases and JDBC

**JDBC** is the low-level API for SQL from Java:

```java
String sql = "SELECT name FROM users WHERE id = ?";
try (Connection conn = DriverManager.getConnection(url, user, pass);
     PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setLong(1, 42L);
    try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) System.out.println(rs.getString("name"));
    }
}
```

- Use `PreparedStatement` with `?` placeholders to avoid SQL injection.
- Use a **connection pool** (e.g. HikariCP) in real apps.
- Higher-level options: JPA/Hibernate, Spring Data.

## Web fundamentals

HTTP methods (GET, POST, PUT, PATCH, DELETE), status codes (2xx success, 4xx client error, 5xx server error), headers, JSON bodies, and REST resource naming (`/users/42/orders`).

## Build tools: Maven and Gradle

| | Maven | Gradle |
| --- | --- | --- |
| Config | `pom.xml` (XML) | `build.gradle` (Groovy/Kotlin) |
| Style | Fixed lifecycle: `validate → compile → test → package → install → deploy` | Flexible task graph, incremental builds |
| Common commands | `mvn clean package`, `mvn test` | `./gradlew build`, `./gradlew test` |

Both download dependencies from repositories such as Maven Central.

## Git essentials

- Everyday flow: `git status`, `git add`, `git commit -m`, `git pull`, `git push`, branches with `git switch -c feature/x`.
- **Merge vs rebase**: merge keeps the full history with a merge commit; rebase replays your commits on top of the target for a straight history — don't rebase commits others already pulled.
- `.gitignore` keeps build output (`target/`, `build/`), IDE files and secrets out of the repo.

## Spring and Spring Boot (overview)

- **Dependency injection**: Spring creates objects (beans) and hands them to the classes that need them.
- **Spring Boot**: auto-configuration, starter dependencies, an embedded server, and production features.
- **Profiles**: different settings per environment (`dev`, `prod`).
- **Actuator**: endpoints like `/actuator/health` and `/actuator/metrics` for monitoring.

## Docker and CI

- A **multi-stage Dockerfile** builds the JAR in a JDK image, then copies only the JAR into a small JRE image — the final image is much smaller.
- **Docker Compose** runs the app plus its database together for local development.
- **CI** (e.g. GitHub Actions) builds and tests on every push so broken code is caught before merging.
