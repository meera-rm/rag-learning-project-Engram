---
title: Low-level design (LLD) and design patterns — study notes
topic: system-design
source_type: my-notes
note_kind: study-notes
---

# Low-Level Design (LLD) and Design Patterns — Study Notes

## HLD vs LLD

| High-level design (HLD) | Low-level design (LLD) |
| --- | --- |
| Services, databases, caches, queues, how they connect | Classes, interfaces, methods, relationships inside one service |
| Scale, availability, data flow | Clean code structure, extensibility, correctness |
| Example: "a URL shortener with a load balancer, app servers, a key-value store" | Example: "`ShortUrlService`, `KeyGenerator` interface, `UrlRepository`" |

## An LLD interview process

1. **Clarify requirements** — functional (what it must do) and constraints (scale, concurrency, extensibility).
2. **Identify entities** — nouns in the requirements become candidate classes (parking lot: `ParkingLot`, `Level`, `Spot`, `Vehicle`, `Ticket`).
3. **Define relationships and responsibilities** — who owns whom, which class does what.
4. **Design classes and interfaces** — fields, key methods, where an interface allows future change.
5. **Apply patterns where they help** — not for decoration.
6. **Walk through use cases** — e.g. "car enters, gets a ticket, leaves, pays".
7. **Discuss testing and edge cases** — full lot, lost ticket, concurrent entry.

## OOP pillars recap

Encapsulation (hide state), abstraction (expose what, not how), inheritance (reuse), polymorphism (one interface, many forms). Prefer **composition over inheritance**: a `Car` *has an* `Engine` rather than *is a* subclass of it — easier to change.

## SOLID in practice

- **Single responsibility**: `InvoiceCalculator` computes; `InvoicePrinter` prints.
- **Open/closed**: add a `UpiPayment` class implementing `Payment` instead of editing a big `if/else`.
- **Liskov**: a `Square` that breaks `Rectangle`'s `setWidth` behaviour violates it.
- **Interface segregation**: split a fat `Machine` interface into `Printer`, `Scanner`.
- **Dependency inversion**: services depend on a `NotificationSender` interface, not on `SmtpClient` directly.

## UML diagrams

| Diagram | Shows | Use in interviews |
| --- | --- | --- |
| Class | Classes, fields, methods, relationships (association, aggregation, composition, inheritance) | The main LLD diagram |
| Sequence | Messages between objects over time | Walk through one use case |
| Use case | Actors and what they can do | Clarify scope |
| Activity | Workflow steps and decisions | Business processes |
| State | States of one object and transitions | Order: created → paid → shipped → delivered |

**Aggregation** vs **composition**: both are "has-a"; with composition the part can't exist without the whole (a room in a house), with aggregation it can (a player in a team).

## Design patterns

### Creational
| Pattern | Idea | Example |
| --- | --- | --- |
| Singleton | Exactly one instance | A configuration registry (use carefully — hidden global state, hard to test) |
| Factory method | A method decides which subclass to create | `NotificationFactory.create("sms")` |
| Abstract factory | Families of related objects | UI widgets for light/dark themes |
| Builder | Build complex objects step by step | `Pizza.builder().size(L).addTopping(...).build()` |
| Prototype | Clone an existing object | Copying a configured document template |

### Structural
| Pattern | Idea | Example |
| --- | --- | --- |
| Adapter | Make an incompatible interface fit | Wrap a third-party payment SDK behind your `Payment` interface |
| Decorator | Add behaviour by wrapping | Add logging or compression to a data stream |
| Facade | One simple interface over a complex subsystem | `OrderFacade.placeOrder()` calls inventory, payment, shipping |
| Proxy | Stand-in that controls access | Lazy-loading image, caching proxy |
| Composite | Treat a tree of objects uniformly | Files and folders |

### Behavioural
| Pattern | Idea | Example |
| --- | --- | --- |
| Strategy | Swap algorithms at runtime | Pricing strategies: regular, holiday, member |
| Observer | Notify subscribers of changes | Stock price alerts, event listeners |
| Command | Wrap a request as an object | Undo/redo in an editor, job queues |
| State | Behaviour changes with internal state | Vending machine: idle, has-coin, dispensing |
| Template method | Fixed skeleton, customisable steps | Data import: read → validate → save, with different readers |
| Chain of responsibility | Pass a request along handlers | Support ticket escalation, middleware |
| Iterator | Traverse without exposing internals | Custom collection iteration |

## Quality attributes and the patterns behind them

- **Scalability**: stateless services, horizontal scaling, caching, sharding.
- **Reliability**: retries with backoff, timeouts, circuit breakers, idempotent operations.
- **Availability**: redundancy, health checks, failover, multiple zones.
- **Maintainability**: clear module boundaries, SOLID, tests.

## Common LLD practice problems

Parking lot, elevator system, library management, LRU cache, vending machine, chess, ride sharing, movie ticket booking, splitwise-style expense sharing, rate limiter, logger.
