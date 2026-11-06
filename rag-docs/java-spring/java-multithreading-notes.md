---
title: Java multithreading and exceptions — study notes
topic: java-spring
source_type: my-notes
note_kind: study-notes
---

# Java Multithreading and Exceptions — Study Notes

## Threads: the basics

A **thread** is an independent path of execution inside one process. All threads of a program share the same heap memory (objects), but each has its own stack (local variables, method calls). Sharing memory is what makes threads fast — and dangerous.

Two ways to define work for a thread:

```java
// 1. Implement Runnable (preferred: your class can still extend something else)
Runnable task = () -> System.out.println("working in " + Thread.currentThread().getName());
new Thread(task).start();

// 2. Extend Thread
class Worker extends Thread {
    public void run() { System.out.println("worker running"); }
}
new Worker().start();
```

Always call `start()`, not `run()`. `run()` just executes the method on the current thread.

## Thread lifecycle

| State | Meaning |
| --- | --- |
| NEW | Created, `start()` not called yet |
| RUNNABLE | Running or ready to run |
| BLOCKED | Waiting to enter a `synchronized` block held by another thread |
| WAITING | Waiting indefinitely (`wait()`, `join()`) |
| TIMED_WAITING | Waiting with a timeout (`sleep(ms)`, `wait(ms)`) |
| TERMINATED | `run()` finished |

## Useful thread methods

- `sleep(ms)`: pause the current thread; it keeps any locks it holds.
- `join()`: wait for another thread to finish.
- `setPriority(n)`: a hint to the scheduler (1–10); not a guarantee.
- `setDaemon(true)`: a background thread that doesn't keep the JVM alive (e.g. a cleanup thread).
- `interrupt()`: politely ask a thread to stop; blocking calls throw `InterruptedException`.

## Race conditions and `synchronized`

A **race condition** happens when the result depends on the timing of threads. `count++` looks atomic but is three steps: read, add, write. Two threads can both read 5 and both write 6.

```java
class Counter {
    private int count = 0;
    public synchronized void increment() { count++; }   // one thread at a time per object
    public synchronized int get() { return count; }
}
```

`synchronized` uses the object's **monitor lock**: only one thread can be inside any synchronized method of that object at a time. A `synchronized(lockObject) { ... }` block locks a smaller region.

## Deadlock

Two threads each hold one lock and wait for the other's. Neither can continue.

Prevention:
- Always acquire locks in the **same global order**.
- Use `tryLock(timeout)` from `ReentrantLock` so a thread can give up.
- Hold locks for as short a time as possible.

## `wait` / `notify`

Threads coordinate on a shared condition (e.g. producer/consumer): the consumer calls `wait()` while the queue is empty; the producer calls `notifyAll()` after adding. Both must be inside `synchronized` on the same object, and `wait()` should always be in a `while` loop because a thread can wake up without the condition being true. In modern code, a `BlockingQueue` does this for you.

## `volatile`

`volatile` guarantees **visibility**: a write by one thread is immediately visible to others (no stale CPU cache copy). It does **not** make compound operations like `count++` atomic. Typical use: a `volatile boolean running` flag to stop a loop.

## Locks

`ReentrantLock` is a more flexible alternative to `synchronized`:

```java
Lock lock = new ReentrantLock();
lock.lock();
try {
    // critical section
} finally {
    lock.unlock();   // always unlock in finally
}
```

Extras: `tryLock`, fairness, and `ReadWriteLock` (many readers or one writer).

## Executors and thread pools

Creating a thread per task is expensive. An **ExecutorService** keeps a pool of reusable threads.

```java
ExecutorService pool = Executors.newFixedThreadPool(4);
Future<Integer> result = pool.submit(() -> 6 * 7);   // Callable returns a value
System.out.println(result.get());                    // blocks until done
pool.shutdown();
```

- `Runnable` returns nothing; `Callable` returns a value and can throw checked exceptions.
- `Future.get()` waits for the result.
- Always `shutdown()` the pool.

## CompletableFuture

Chains asynchronous steps without blocking:

```java
CompletableFuture.supplyAsync(() -> fetchUser(42))
    .thenApply(user -> user.getEmail())
    .thenAccept(System.out::println)
    .exceptionally(ex -> { System.err.println(ex); return null; });
```

Use `thenCombine` to merge two independent async results and `allOf` to wait for many.

## Concurrent collections and atomics

| Tool | Use |
| --- | --- |
| `ConcurrentHashMap` | Thread-safe map with fine-grained locking; much faster than a synchronized `HashMap` |
| `CopyOnWriteArrayList` | Lists read very often, written rarely |
| `BlockingQueue` | Producer/consumer hand-off |
| `AtomicInteger`, `AtomicLong` | Lock-free counters (`incrementAndGet()`) |
| `CountDownLatch` | Wait until N tasks finish |

## Exceptions

### Checked vs unchecked
- **Checked** (subclasses of `Exception`, not `RuntimeException`): the compiler forces you to catch or declare them — `IOException`, `SQLException`. Use for recoverable conditions outside your control.
- **Unchecked** (`RuntimeException` subclasses): programming errors — `NullPointerException`, `IllegalArgumentException`, `ArrayIndexOutOfBoundsException`.
- **Errors** (`OutOfMemoryError`, `StackOverflowError`): serious JVM problems; don't catch normally.

### try / catch / finally and try-with-resources

```java
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    System.out.println(reader.readLine());
} catch (IOException e) {
    System.err.println("Could not read file: " + e.getMessage());
} finally {
    System.out.println("runs whether or not an exception happened");
}
```

Try-with-resources closes the reader automatically.

### throw vs throws
- `throw new IllegalArgumentException("age must be positive")` — actually raises an exception.
- `void load() throws IOException` — declares that a method may raise it.

### Custom exceptions

```java
class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) { super(message); }
}
```

Good practice: catch the most specific exception, never swallow exceptions silently, and include context in the message.

## Interview quick checks

- `sleep` vs `wait`: `sleep` keeps locks and is on `Thread`; `wait` releases the lock and is on `Object`.
- `synchronized` vs `volatile`: mutual exclusion + visibility vs visibility only.
- Why a thread pool? Reuse threads, limit concurrency, avoid creation overhead.
- How to avoid deadlock? Consistent lock ordering, timeouts, fewer shared locks.
