---
title: JAVA-COMPLETE-NOTES
topic: java-spring
source_type: my-notes
source_file: STUDYNOTEs/JAVA-COMPLETE-NOTES.md
---

# Java — Complete Step-by-Step Notes for Beginners

> One combined study guide built from every file in the `javanotes` folder (22 PDFs + 1 diagram).
> Read top to bottom. Each part builds on the one before it.
> All interview questions have been separated into **JAVA-INTERVIEW-QUESTIONS.md**.

---

## How to use this guide

| Stage | Parts | What you can do after it |
|---|---|---|
| Absolute beginner | 1 – 7 | Write, compile and run programs with variables, loops and arrays |
| Core Java | 8 – 16 | Strings, methods, OOP, exceptions, collections — enough for a junior job |
| Serious Java | 17 – 23 | Threads, streams, files, JDBC, reflection, DSA patterns |
| Backend developer | 24 – 28 | Spring Boot, REST APIs, databases, security, system design |

Rule used throughout: **type every code sample yourself.** Reading Java does not teach Java.

### Table of contents

1. What Java Is and How It Runs
2. Your First Program, Syntax and Comments
3. Variables and Data Types
4. Operators
5. Input and Output
6. Control Flow — Decisions and Loops
7. Arrays
8. Strings, StringBuilder and StringBuffer
9. Methods
10. OOP Part 1 — Classes, Objects, Constructors, `this`, `static`, `final`
11. OOP Part 2 — Inheritance and Polymorphism
12. OOP Part 3 — Abstraction: Abstract Classes and Interfaces
13. OOP Part 4 — Encapsulation, Packages and Access Modifiers
14. The `Object` Class and Other Built-in Helpers
15. Exception Handling
16. The Collections Framework
17. Multithreading and Concurrency
18. Garbage Collection and the Runtime
19. Modern Java (8+): Lambdas, Streams, Optional, Date/Time, Regex, Enums, Annotations
20. File Handling, I/O and Serialization
21. JDBC and Databases
22. Reflection
23. Problem Solving — DSA Patterns and Complexity
24. Backend Development Fundamentals
25. REST APIs and HTTP in Depth
26. Spring and Spring Boot
27. System Design Fundamentals
28. Study Plan and Practice Checklist

**Added in the second revision — deeper and more advanced material:**

29. Spring Boot in Depth — The Senior-Level Field Guide (defaults, traps and corrections)
30. JVM Internals
31. The Developer Toolchain — Build Tools, Git, NIO and Jackson
32. The Distributed Systems Toolkit — Microservices, Spring Cloud, Kafka, Redis, Docker, CI/CD, Cloud, Observability
33. Design Patterns
34. Debugging & Troubleshooting Handbook
35. Performance Optimization
36. Clean Code & Professional Practice
37. Projects, Roadmaps and Job Preparation
38. Rapid Revision Cheat Sheets

---
---

# Part 1 — What Java Is and How It Runs

## 1.1 What is Java?

Java is a **high-level, class-based, object-oriented, secure and robust programming language**, and also a **platform**.

- Developed by **Sun Microsystems** (now owned by Oracle), released in **1995**.
- **James Gosling** is known as the father of Java.
- A *platform* is any hardware or software environment where a program runs. Java is called a platform because it ships with its own runtime environment (JRE) and API.
- Design goal: "write once, run anywhere" — compiled Java runs on every platform that supports Java, with no recompilation.

## 1.2 Where Java is used

1. Desktop applications — Acrobat Reader, media players, antivirus (AWT, Swing)
2. Web applications — irctc.co.in, javatpoint.com (Servlets, JSP)
3. Enterprise applications — banking, e-commerce
4. Mobile applications — Android apps
5. Embedded systems and IoT devices
6. Smart cards
7. Robotics
8. Games and multimedia
9. Scientific applications

## 1.3 Features of Java (know all ten)

| Feature | What it really means |
|---|---|
| **Simple** | Syntax is based on C++ but the complicated parts were removed — no explicit pointers, no operator overloading, and automatic garbage collection |
| **Object-Oriented** | Software is organised as objects that hold both data and behaviour |
| **Platform Independent** | Java compiles to **bytecode**, not machine code, so the same `.class` file runs on any OS that has a JVM |
| **Secure** | No explicit pointers; programs run inside a JVM sandbox |
| **Robust** | Strong memory management, no pointers, automatic garbage collection, strong exception handling |
| **Architecture Neutral** | No implementation-dependent features — an `int` is 4 bytes everywhere |
| **Portable** | Bytecode can be carried to any platform without change |
| **High Performance** | Bytecode is "close" to native code, so it is faster than traditional interpreted languages |
| **Distributed** | Built-in support for distributed applications (RMI, networking) |
| **Multi-threaded** | A thread is a separate lightweight path of execution; Java can do many tasks at once |
| **Dynamic** | Classes are loaded on demand; supports native C/C++ functions |

Extra features often listed in interviews: automatic memory management, a rich API, and scalability.

## 1.4 JDK vs JRE vs JVM — the classic confusion

```
JDK  =  JRE  +  development tools (javac, debugger, javadoc)
JRE  =  JVM  +  class libraries / supporting files
JVM  =  the abstract machine that actually executes bytecode
```

- **JVM (Java Virtual Machine)** — an *abstract* machine. It does not physically exist; it is a **specification** that provides a runtime environment. It executes bytecode and is what makes Java platform independent. Every platform has its own JVM implementation.
- **JRE (Java Runtime Environment)** — the software needed to **run** Java programs: JVM + class libraries + supporting files.
- **JDK (Java Development Kit)** — physically exists on disk. It is the JRE **plus** development tools: the compiler (`javac`), debugger, documentation generator. You need this to **write** Java.

Java programs will not run at all without a JVM. The JVM is included in both the JDK and the JRE.

## 1.5 The compilation process

```
Hello.java  --javac-->  Hello.class  --JVM-->  Output
(source)    (compiler)  (bytecode)  (on any platform)
```

1. You write Java source in a `.java` file.
2. The compiler `javac` converts it into **bytecode** (a `.class` file).
3. The JVM executes that bytecode on any platform.
4. Because step 3 is platform-specific but steps 1–2 are not, **Java is platform independent**.

---

# Part 2 — Your First Program, Syntax and Comments

## 2.1 Hello World

```java
// Hello World Program
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

Every single word explained:

| Token | Meaning |
|---|---|
| `class` | Keyword used to declare a class |
| `public` | Access modifier meaning "visible to everyone" |
| `static` | The method belongs to the class, not an object. The JVM can call `main()` without creating an object first — this saves memory |
| `void` | Return type — this method returns nothing |
| `main` | The starting point of the program; the JVM looks for exactly this name |
| `String[] args` | Command-line arguments passed into the program |
| `System.out.println()` | `System` is a class, `out` is an object of `PrintStream`, `println()` is a method of `PrintStream` |

**Q: Why is `main` static?**
Because an object is not required to call a static method. If `main()` were non-static, the JVM would have to create an object *before* calling it — extra, pointless memory allocation.

**Q: Can you run a program without `main()`?**
No. A static block worked up to JDK 1.6; since JDK 1.7 it is not possible.

**Q: Can you save a Java file under a different name than the class?**
Yes — but only if the class is **not** `public`.

**Q: Can one file hold multiple classes?**
Yes. Only one may be `public`, and its name must match the file name.

## 2.2 Syntax rules

- Java is **case-sensitive** (`age`, `Age`, `AGE` are three different things).
- Every statement ends with a **semicolon** `;`.
- Code blocks are wrapped in **curly braces** `{ }`.
- The `main` method is the entry point.

## 2.3 Comments

```java
// A. Single-line comment

/* B. Multi-line
   comment */

/**
 * C. Documentation comment.
 * Used by javadoc to generate API docs.
 */
```

## 2.4 Keywords (reserved words)

Keywords are predefined words that act as a key to your code. **You can never use them as a variable, class, method or object name.**

```
abstract  assert     boolean    break      byte
case      catch      char       class      const*
continue  default    do         double     else
enum      extends    final      finally    float
for       goto*      if         implements import
instanceof int       interface  long       native
new       package    private    protected  public
return    short      static     strictfp   super
switch    synchronized this     throw      throws
transient try        void       volatile   while
```
(*`const` and `goto` are reserved but not used.)

## 2.5 Identifiers

Identifiers are names you give to classes, methods and variables.

**Rules**
1. Must start with a letter, `$` or `_`
2. Can contain letters, digits, `$` and `_`
3. Cannot start with a number
4. Cannot be a keyword
5. Case-sensitive

| Valid | Invalid |
|---|---|
| `myVar` | `my Var` (space) |
| `_count` | `my-var` (hyphen) |
| `$value1` | `@count` (special character) |
| `totalSum` | `1value` (starts with a digit) |
| `studentName1` | `class` (keyword) |

---

# Part 3 — Variables and Data Types

## 3.1 What is a variable?

A variable is a **container that holds a value** while the program runs. It is the name of a memory location, and it always has a data type. Every variable must be declared before use.

```java
dataType variableName = value;

double price  = 19.99;   // decimal
char   grade  = 'A';     // character
boolean isPass = true;   // boolean
String name   = "Abhi";  // string
int    myNum  = 5;
float  myFloatNum = 5.99f;
```

## 3.2 The three kinds of variables

| Kind | Declared where | Lifetime |
|---|---|---|
| **Local** | Inside a method, constructor or block | Created when the block is entered, destroyed when it exits. Visible only inside that block. **Cannot be `static`.** |
| **Instance** | Inside a class but outside any method, without `static` | Created with the object, destroyed with the object. Each object gets its own copy. |
| **Static** | Inside a class with the `static` keyword | Created when the class is loaded, destroyed when the class is unloaded. **One copy shared by all objects.** |

```java
public class MyClass {
    private int myInstanceVariable;        // instance
    private static int myStaticVariable;   // static

    public void myMethod() {
        int myLocalVariable = 10;          // local
        myInstanceVariable  = 20;
        myStaticVariable    = 30;
    }
}
```

## 3.3 Primitive data types (all 8)

| Type | Size | Range | Default | Example |
|---|---|---|---|---|
| `byte` | 1 byte | −128 to 127 | `0` | `byte b = 10;` |
| `short` | 2 bytes | −32,768 to 32,767 | `0` | `short s = 1000;` |
| `int` | 4 bytes | −2^31 to 2^31−1 | `0` | `int a = 100000;` |
| `long` | 8 bytes | −2^63 to 2^63−1 | `0L` | `long l = 123456789L;` |
| `float` | 4 bytes | ~6–7 decimal digits | `0.0f` | `float f = 5.5F;` |
| `double` | 8 bytes | ~15 decimal digits | `0.0d` | `double d = 12.345;` |
| `char` | 2 bytes | ` ` to `￿` | ` ` | `char ch = 'A';` |
| `boolean` | 1 bit | `true` / `false` | `false` | `boolean flag = true;` |

Use `int` for general calculations and `double` for decimals unless you have a reason not to.

## 3.4 Non-primitive (reference) data types

These store references to objects rather than raw values, and are created with `new`.

From the folder's **non-primitive data types diagram**:

```
NON-PRIMITIVE DATA TYPES
├── String
├── Array
├── Class
│   ├── Interface
│   │   ├── Wrapper Classes
│   │   └── List ──► List / Set / Map
│   └── Enum
└── Object
```

1. **String** — a sequence of characters
2. **Array** — a collection of elements of the same type
3. **Class** — a blueprint of objects
4. **Interface** — a contract of methods
5. **Enum** — a special class with a fixed set of constants
6. **Wrapper classes** — an object representation of primitives
7. **Collection framework** — List, Set, Map, etc.

```java
String name = "Abhi";
int[] numbers = {1, 2, 3, 4, 5};
ArrayList<Integer> list = new ArrayList<>();
MyClass obj = new MyClass();
```

## 3.5 The Unicode system

Before Unicode there were many incompatible standards: ASCII (US), ISO 8859-1 (Western Europe), KOI-8 (Russian), GB18030 and BIG-5 (Chinese).

Two problems this caused:
1. The same code value meant different letters in different standards.
2. Encodings for large character sets had variable length — some characters were one byte, others two or more.

**Solution:** Unicode, one universal encoding. In Unicode a character holds **2 bytes**, which is why a Java `char` is 2 bytes.
- Lowest value: ` `
- Highest value: `￿`

## 3.6 Type casting

**Widening (implicit)** — no data loss, done automatically:
```
byte -> short -> int -> long -> float -> double
char -> int -> long -> float -> double
```
```java
int i = 100;
long l = i;      // int -> long
float f = l;     // long -> float
double d = f;    // float -> double
```

**Narrowing (explicit)** — may lose data, so you must write the target type in parentheses:
```
double -> float -> long -> int -> short -> byte
double -> float -> long -> int -> char
```
```java
double d = 10.99;
int i = (int) d;      // i = 10, the decimal part is lost
char ch = (char) i;
byte b = (byte) i;
```

## 3.7 Wrapper classes

Wrapper classes **convert a primitive into an object and back**. They live in `java.lang`.

| Primitive | Wrapper | | Primitive | Wrapper |
|---|---|---|---|---|
| `byte` | `Byte` | | `float` | `Float` |
| `short` | `Short` | | `double` | `Double` |
| `int` | `Integer` | | `char` | `Character` |
| `long` | `Long` | | `boolean` | `Boolean` |

**Why you need them**
1. **Collections only hold objects.** `ArrayList<int>` does not compile; `ArrayList<Integer>` does.
2. **To represent null.** A primitive `int` can never be null; `Integer a = null;` can.
3. **Utility methods.** `Integer.parseInt("123")`, `Integer.toString(123)`.

**Autoboxing** — automatic conversion of a primitive into its wrapper (`int` to `Integer`, `char` to `Character`, and so on).
**Unboxing** — the reverse (`Integer` to `int`). Both were added in J2SE 5.0.

Common pitfall: unboxing a `null` wrapper throws `NullPointerException`.

## 3.8 Constants with `final`

```java
final int MAX = 100;
final double PI = 3.14159;
final int DAYS = 7;
```
A `final` variable cannot be reassigned.

## 3.9 `strictfp`

The `strictfp` keyword guarantees you get **the same floating-point result on every platform**.

## 3.10 `volatile` and `transient` (preview — details in Parts 17 and 20)

- **`volatile`** marks a variable whose value may be changed by different threads. It ensures a write by one thread is immediately visible to all others.
- **`transient`** tells the JVM to **exclude** a field from serialization — it will not be saved in the serialized form of the object.

---

# Part 4 — Operators

An operator is a symbol that performs an operation. Java's operator families: unary, arithmetic, shift, relational, bitwise, logical, ternary and assignment.

## 4.1 Arithmetic

| Op | Name | Example |
|---|---|---|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus (remainder) | `a % b` |
| `++` | Increment | `a++` |
| `--` | Decrement | `a--` |

```java
int a = 10, b = 3;
int sum = a + b;   // 13
int rem = a % b;   // 1
```

## 4.2 Unary

| Op | Name | Example | Behaviour |
|---|---|---|---|
| `+` | Unary plus | `+a` | Unchanged |
| `-` | Unary minus | `-a` | Negates |
| `++` | Pre / post increment | `++a`, `a++` | Pre: increase then use. Post: use then increase |
| `--` | Pre / post decrement | `--a`, `a--` | Same idea |
| `!` | Logical NOT | `!flag` | Inverts a boolean |
| `~` | Bitwise NOT | `~a` | Two's complement |

```java
int a = 10;
int b = -a;    // -10
int c = ++a;   // pre-increment  -> a = 11, c = 11
int d = a++;   // post-increment -> d = 11, a = 12
boolean e = !true;   // false
int f = ~a;    // -13 (two's complement)
```

## 4.3 Relational (comparison)

| Op | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

```java
int a = 10, b = 20;
System.out.println(a < b);    // true
System.out.println(a == b);   // false
```

## 4.4 Logical

| Op | Meaning | Example |
|---|---|---|
| `&&` | Logical AND — true if **both** are true | `(a > 0 && b > 0)` |
| `\|\|` | Logical OR — true if **either** is true | `(a > 0 \|\| b > 0)` |
| `!` | Logical NOT | `!(a > 0)` |

`&&` and `||` are **short-circuit**: if the left side already decides the answer, the right side is never evaluated.

## 4.5 Assignment

| Op | Example | Same as |
|---|---|---|
| `=` | `a = b` | — |
| `+=` | `a += b` | `a = a + b` |
| `-=` | `a -= b` | `a = a - b` |
| `*=` | `a *= b` | `a = a * b` |
| `/=` | `a /= b` | `a = a / b` |
| `%=` | `a %= b` | `a = a % b` |

## 4.6 Bitwise and shift

With `a = 5` (binary `0101`) and `b = 3` (binary `0011`):

| Op | Meaning | Example | Result |
|---|---|---|---|
| `&` | Bitwise AND | `a & b` | `1` (`0001`) |
| `\|` | Bitwise OR | `a \| b` | `7` (`0111`) |
| `^` | Bitwise XOR | `a ^ b` | `6` (`0110`) |
| `~` | Bitwise NOT | `~a` | `-6` |
| `<<` | Left shift | `a << 1` | `10` (`1010`) |
| `>>` | Right shift | `a >> 1` | `2` (`0010`) |
| `>>>` | Unsigned right shift | `a >>> 1` | `2` (fills 0 from the left) |

## 4.7 Ternary operator

A shorthand `if-else`.

```java
condition ? valueIfTrue : valueIfFalse;

int age = 18;
String status = (age >= 18) ? "Adult" : "Minor";
System.out.println(status);   // Adult
```

## 4.8 Operator precedence (high to low)

```
1.  ()                          parentheses
2.  ++  --  ~  !                unary
3.  *  /  %                     multiplicative
4.  +  -                        additive
5.  <<  >>  >>>                 shift
6.  <  <=  >  >=  instanceof    relational
7.  ==  !=                      equality
8.  &                           bitwise AND
9.  ^                           bitwise XOR
10. |                           bitwise OR
11. &&                          logical AND
12. ||                          logical OR
13. ?:                          ternary
14. =  +=  -=  *=  /=  %=       assignment
```

---

# Part 5 — Input and Output

## 5.1 Output

```java
System.out.print("no newline");
System.out.println("with newline");
System.out.printf("Name: %s, Age: %d%n", name, age);
```

## 5.2 Input with `Scanner`

`Scanner` lives in `java.util`.

```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);

System.out.print("Enter name : ");
String name = sc.nextLine();

System.out.print("Enter age : ");
int age = sc.nextInt();

System.out.println("Hello, " + name);
```

Common `Scanner` methods: `nextLine()`, `next()`, `nextInt()`, `nextDouble()`, `nextBoolean()`.

---

# Part 6 — Control Flow

Java has three families of control-flow statements:
1. **Decision making** — `if`, `switch`
2. **Loops** — `for`, `while`, `do-while`, for-each
3. **Jump** — `break`, `continue`

## 6.1 `if`

```java
if (condition) {
    // runs only when condition is true
}

int age = 18;
if (age >= 18) {
    System.out.println("Adult");
}
```

## 6.2 `if-else`

```java
int n = 10;
if (n % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```

## 6.3 `else-if` ladder

A chain of conditions forming a decision tree — the first true branch wins, the rest are skipped.

```java
int marks = 85;
if (marks >= 90)      System.out.println("Grade: A");
else if (marks >= 75) System.out.println("Grade: B");
else if (marks >= 50) System.out.println("Grade: C");
else                  System.out.println("Grade: D");
```

## 6.4 Nested `if`

An `if` inside another `if`.

```java
int age = 20;
if (age >= 18) {
    if (age >= 21) {
        System.out.println("Can vote and drink");
    } else {
        System.out.println("Can vote but not drink");
    }
}
```

## 6.5 `switch`

Use `switch` when **one variable** is compared against multiple constant options.

```java
int day = 3;
switch (day) {
    case 1: System.out.println("Mon"); break;
    case 2: System.out.println("Tue"); break;
    case 3: System.out.println("Wed"); break;
    default: System.out.println("Invalid");
}
```
Forgetting `break` causes *fall-through* — execution continues into the next case.

## 6.6 `for` loop

Use when you **know how many iterations** you need. Initialisation, condition and increment all live on one line.

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
// 1 2 3 4 5
```

## 6.7 `while` loop

Use when the number of iterations is **not known in advance**; the condition is checked first.

```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
```

## 6.8 `do-while` loop

Checks the condition **at the end**, so the body always runs **at least once**. Also called the *exit-controlled* loop.

```java
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

## 6.9 Enhanced `for` (for-each)

Traverses arrays and collections without a loop counter. You do not update the loop variable.

```java
for (dataType var : arrayOrCollection) {
    // statements
}

int[] nums = {10, 20, 30, 40, 50};
for (int n : nums) System.out.println(n);
```

## 6.10 Nested loops

A loop inside a loop — used for patterns, matrices and grid logic.

```java
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print("*");
    }
    System.out.println();
}
/*
*
**
***
*/
```

## 6.11 `break` and `continue`

- **`break`** — terminates the loop or `switch` immediately; control jumps to the statement after it.
- **`continue`** — skips only the current iteration and jumps to the next one.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;              // stops at 5 -> prints 1 2 3 4
    System.out.print(i + " ");
}

for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;           // skips 3 -> prints 1 2 4 5
    System.out.print(i + " ");
}
```

## 6.12 Choosing the right construct

- `if` / `else` — general decision making
- `switch` — one variable, many constant options
- `for` — iteration count is known
- `while` — iteration count unknown, condition checked first
- `do-while` — must execute at least once
- Nested loops — patterns and complex logic

---

# Part 7 — Arrays

## 7.1 What is an array?

A Java array is an **object** that holds a fixed number of elements **of the same data type**, stored in **contiguous memory**. It is index-based, and the first element sits at index **0**.

**Advantages**
- *Code optimization* — you can retrieve and sort data efficiently
- *Random access* — you can get any element by its index in O(1)

**Disadvantage**
- *Size limit* — the size is fixed at creation and cannot grow at runtime. The Collections Framework (e.g. `ArrayList`) solves this.

The theoretical maximum Java array size is `2,147,483,647` elements.

## 7.2 Declaring and initialising

```java
// Method 1 - with values
int[] myNum = {10, 20, 30, 40};
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Method 2 - with new
int[] marks = new int[5];
marks[0] = 85;
marks[1] = 90;
marks[2] = 78;
marks[3] = 88;
marks[4] = 92;
```

Default values in a new array: `int` -> `0`, `double`/`float` -> `0.0`, `char` -> ` `, `boolean` -> `false`, object -> `null`.

## 7.3 Length and traversal

`length` is a **property**, not a method (no parentheses):

```java
int[] arr = new int[5];
System.out.println(arr.length);   // 5

for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + " ");
for (int x : arr) System.out.print(x + " ");
```

## 7.4 Two-dimensional arrays

An array of arrays — a matrix or table.

```java
int[][] mat = {{1,2,3}, {4,5,6}, {7,8,9}};

for (int i = 0; i < mat.length; i++) {
    for (int j = 0; j < mat[i].length; j++) {
        System.out.print(mat[i][j] + " ");
    }
    System.out.println();
}
/*
1 2 3
4 5 6
7 8 9
*/
```

## 7.5 The `Arrays` utility class (`java.util.Arrays`)

| Method | Description |
|---|---|
| `Arrays.sort(arr)` | Sorts ascending |
| `Arrays.binarySearch(arr, key)` | Binary search on a **sorted** array |
| `Arrays.fill(arr, val)` | Fills every element with `val` |
| `Arrays.copyOf(arr, n)` | Copies into a new array of size `n` |
| `Arrays.equals(a, b)` | Compares two arrays |
| `Arrays.toString(arr)` | Readable string form |

```java
int[] a = {5, 3, 1, 4, 2};
Arrays.sort(a);                        // [1, 2, 3, 4, 5]
int idx = Arrays.binarySearch(a, 5);   // 4
Arrays.fill(a, 7);                     // [7, 7, 7, 7, 7]
int[] b = Arrays.copyOf(a, 3);         // [7, 7, 7]
boolean eq = Arrays.equals(a, b);      // false
```

## 7.6 Array vs ArrayList

| Array | ArrayList |
|---|---|
| Fixed size | Resizable |
| Stores primitives **and** objects | Objects only (use wrapper classes) |
| Accessed with `arr[i]` | Accessed with `get()`, `add()`, `remove()` |
| Insert and delete are slow and awkward | Insert and delete are efficient |
| Sorted with `Arrays.sort()` | Sorted with `Collections.sort()` |
| Can be multidimensional | Single-dimensional only |
| Cannot store nulls (for primitives) | Can store `null` |
| Faster, less flexible | Slower, more flexible |

---

# Part 8 — Strings, StringBuilder and StringBuffer

## 8.1 What is a String?

In Java a String is an **object that represents a sequence of char values**. An array of characters works the same way.

```java
char[] ch = {'j','a','v','a'};
String s = new String(ch);
```

## 8.2 Two ways to create a String

```java
// 1. String literal (preferred)
String s1 = "welcome";

// 2. new keyword - creates two objects and one reference variable
String s2 = new String("Welcome");
```

String literals are stored in the **String pool**, a shared area of memory. If the same literal already exists, the reference is reused. `new String(...)` always creates a fresh object outside the pool.

## 8.3 Immutability

**Java Strings are immutable** — once created, the value can never be changed. Any "modification" creates a brand new String object.

This matters because String references are used to store attributes like usernames and passwords. All wrapper classes (`Boolean`, `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`) and `String` are immutable.

## 8.4 String indexing

Indexing starts at 0.

```java
String s = "Java";
char c  = s.charAt(0);  // 'J'
char c1 = s.charAt(2);  // 'v'
```
An index out of range throws `StringIndexOutOfBoundsException`.

## 8.5 Common String methods

| Method | Description |
|---|---|
| `length()` | Returns the length of the string |
| `charAt(i)` | Returns the char at index `i` |
| `substring(i)` | Substring from `i` to the end |
| `substring(i, j)` | Substring from `i` to `j-1` |
| `equals(str)` | Compares content (case-sensitive) |
| `equalsIgnoreCase(str)` | Compares content, ignoring case |
| `compareTo(str)` | Lexicographic comparison; returns <0, 0 or >0 |
| `toUpperCase()` | Converts to uppercase |
| `toLowerCase()` | Converts to lowercase |
| `trim()` | Removes leading and trailing whitespace |
| `indexOf(c)` | First index of a character or substring |
| `lastIndexOf(c)` | Last index of a character or substring |
| `replace(old, new)` | Replaces every occurrence |
| `split(regex)` | Splits into a String array |
| `contains(str)` | True if the substring is present |

```java
String str1 = "Hello";
String str2 = "World";
String str3 = str1 + str2;           // concatenation
int length  = str3.length();
int index   = str3.indexOf('o');
String sub  = str3.substring(0, 5);
boolean isEqual = str1.equals(str2);

int result = str1.compareTo(str2);
// < 0 -> str1 comes before str2
// = 0 -> equal
// > 0 -> str1 comes after str2
```

## 8.6 String formatting

```java
String name = "Abhi";
int age = 21;

// Concatenation
String msg = "My name is " + name + " and age is " + age;

// format()  -  better for complex formatting
String s = String.format("%s is %d years old", name, age);
System.out.println(s);
```

## 8.7 StringBuilder — mutable, not synchronized

```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" Java");
sb.insert(5, ",");
sb.replace(0, 5, "Hi");
sb.delete(0, 3);
sb.reverse();
System.out.println(sb);
```

| Method | Description |
|---|---|
| `append(x)` | Adds at the end |
| `insert(i, x)` | Inserts at index `i` |
| `replace(i, j, s)` | Replaces from `i` to `j-1` |
| `delete(i, j)` | Deletes from `i` to `j-1` |
| `reverse()` | Reverses the string |

Introduced in **Java 5**. **Non-synchronized**, therefore **faster**, and best for single-threaded code.

## 8.8 StringBuffer — mutable and synchronized

`StringBuffer` has exactly the same methods as `StringBuilder`, but every method is **synchronized**.

## 8.9 String vs StringBuffer vs StringBuilder

| | String | StringBuffer | StringBuilder |
|---|---|---|---|
| Mutable | No | Yes | Yes |
| Thread-safe | Yes (immutable) | Yes (synchronized) | No |
| Speed | Slow for repeated edits | Slower | Fastest |
| Stored in String pool | Yes (literals) | No | No |
| Since | 1.0 | 1.0 | Java 5 |

**Rule of thumb:** use `String` for fixed text, `StringBuilder` for building text in a single thread, and `StringBuffer` only when multiple threads share the same buffer.

## 8.10 `toString()`

`toString()` returns the String representation of an object. When you print any object, the compiler internally calls `toString()` on it. Overriding it lets you print meaningful values.

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) { this.name = name; this.age = age; }

    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
}
Person p = new Person("John Doe", 30);
System.out.println(p);   // Person{name='John Doe', age=30}
```

Without overriding it, the default prints the class name, `@`, and the hash code.

## 8.11 StringTokenizer

`java.util.StringTokenizer` breaks a String into tokens. It is a legacy class — modern code uses `split()`.

## 8.12 How to make an immutable class

Make the class `final`, make all fields `private final`, do not provide setters, and initialise everything through the constructor. `String` and all wrapper classes follow this pattern.

## 8.13 Array vs String

| Array | String |
|---|---|
| Fixed size, mutable elements | Immutable |
| Index based (0) | Index based (0) |
| Stores primitives or objects | Characters only |
| `int[]`, `char[]` | `"Hello"` |

---

# Part 9 — Methods

## 9.1 What is a method?

A method is a **reusable block of code that performs one task**. It gives you code reuse and makes the program modular. It runs only when it is called.

**Types:** instance methods (bound to an object), static methods (bound to the class), and constructors.

## 9.2 Syntax

```java
[modifiers] returnType methodName(type p1, type p2, ...) [throws Exception] {
    // body
    return value;   // if returnType is not void
}
```

```java
void greet(String name) {
    System.out.println("Hello, " + name);
}

int add(int a, int b) {
    int sum = a + b;
    return sum;
}
```

## 9.3 Parameters vs arguments

- **Parameters** are the variables declared in the method definition.
- **Arguments** are the actual values sent when the method is called.

## 9.4 Return types

- `void` means the method returns nothing.
- Any other return type means the returned value **must match the declared type**.

## 9.5 Modifiers you can put on a method

- **Access:** `public`, `private`, `protected`, default (package-private)
- **Other:** `static`, `final` (cannot be overridden), `abstract` (no body), `synchronized`, `native`, `strictfp`

## 9.6 Method overloading

Two or more methods in the same class with the **same name but different parameters** (different count, or different types). It is a form of **compile-time polymorphism** and it improves readability.

```java
class Adder {
    static int add(int a, int b) { return a + b; }
    static double add(double a, double b) { return a + b; }
    static int add(int a, int b, int c) { return a + b + c; }
}
System.out.println(Adder.add(11, 11));      // 22
System.out.println(Adder.add(12.3, 12.6));  // 24.9
```

**Why you cannot overload by return type alone:** it would be ambiguous — the compiler could not tell which method you meant from the call site.

**Can you overload `main()`?** Yes, any number of times. But the JVM only ever calls the one that takes `String[]`.

## 9.7 Variable arguments (varargs)

Varargs let a method accept any number of arguments. The varargs parameter must be **last**.

```java
int sum(int... numbers) {
    int s = 0;
    for (int n : numbers) s += n;
    return s;
}
System.out.println(sum(1, 2));          // 3
System.out.println(sum(1, 2, 3, 4));    // 10
```

## 9.8 Java is always pass-by-value

A **copy of the value** is passed to the method. For objects, the *reference* is copied — so you can mutate the object, but reassigning the parameter does not affect the caller.

```java
void change(int a) { a = 100; }   // only the local copy changes

int x = 10;
change(x);
System.out.println(x);   // 10
```

## 9.9 Static vs non-static methods

| Static method | Non-static (instance) method |
|---|---|
| Called with the class name: `MathUtil.square(5)` | Called with an object: `obj.display()` |
| Declared with `static` | No `static` keyword |
| Can access only static members directly | Can access all members |
| No object needed | Object required |
| Example: `Math.sqrt()` | Example: `obj.display()` |

```java
class MathUtil {
    static int square(int x) { return x * x; }
}
int val = MathUtil.square(5);   // 25
```

## 9.10 Recursion

A method that calls itself. **Every recursion must have a base case** or it will never stop.

```java
returnType methodName(parameters) {
    if (baseCondition) return;      // base case
    methodName(smaller input);      // recursive case
}
```

**Factorial** — `n! = n * (n-1)!`, with `0! = 1` and `1! = 1`:

```java
int fact(int n) {
    if (n == 0 || n == 1) return 1;   // base case
    return n * fact(n - 1);           // recursive case
}
// fact(4) = 4 * (3 * (2 * 1)) = 24
// fact(5) = 120
```

**Sum of first n numbers:**

```java
int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
```

**Fibonacci** — `fib(n) = fib(n-1) + fib(n-2)`, with `fib(0)=0` and `fib(1)=1`:

```java
int fib(int n) {
    if (n == 0) return 0;   // base case 1
    if (n == 1) return 1;   // base case 2
    return fib(n - 1) + fib(n - 2);
}
// fib(5) -> fib(4)+fib(3) -> ... -> 5
```

## 9.11 Common method pitfalls

- `NullPointerException` from unboxing a null wrapper.
- `this` is required to resolve a shadowed variable (a parameter with the same name as a field).
- Static methods cannot access instance fields or methods directly.
- Static methods **cannot be overridden** — they are *hidden*.
- Abstract methods cannot be `private` (they must be inheritable).
- `final` on a method means it cannot be overridden.

---

# Part 10 — OOP Part 1: Classes, Objects, Constructors

## 10.1 The core OOP concepts

**Object-Oriented Programming** is a paradigm that organises software as a combination of objects that hold both data and behaviour. It exists to model real-world entities.

| Concept | Definition |
|---|---|
| **Object** | Any entity that has **state** and **behaviour** — a chair, a pen, a bike. Can be physical or logical. |
| **Class** | A blueprint or template from which objects are created. A logical entity. |
| **Inheritance** | When one object acquires all the properties and behaviours of a parent object. Gives code reusability. |
| **Polymorphism** | Performing one task in many different ways. |
| **Abstraction** | Hiding internal details and showing only functionality. Example: making a phone call — you don't see the internals. |
| **Encapsulation** | Binding data and code together into a single unit, like a capsule. |
| **Coupling** | How much one class knows about (depends on) another class. Low coupling is better. |
| **Cohesion** | How focused a component is on a single well-defined task. High cohesion is better. |
| **Association** | A relationship between objects — one-to-one, one-to-many, and so on. |
| **Aggregation** | A way to achieve association: one object contains other objects as part of its state (a HAS-A relationship, weak ownership). |
| **Composition** | A stronger form of aggregation, where the contained object cannot exist independently. |

**The four pillars of OOP:** Inheritance, Polymorphism, Encapsulation, Abstraction.

## 10.2 Class vs Object

| Object | Class |
|---|---|
| An instance of a class | A blueprint/template from which objects are created |
| A real-world entity (pen, laptop, mobile) | A group of similar objects |
| Physical entity | Logical entity |
| Created with `new` (mainly) | Declared with the `class` keyword |
| Created many times as needed | Declared once |
| Allocates memory when created | Does not allocate memory when declared |
| Many ways to create it: `new`, `newInstance()`, `clone()`, factory method, deserialization | Only one way to define it: `class` |

## 10.3 Writing a class and creating an object

```java
class Student {              // class
    int roll;                // data member (attribute)
    String name;             // data member

    void display() {         // method (behaviour)
        System.out.println(roll + " - " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();   // object creation
        s1.roll = 101;
        s1.name = "Sanskaar";
        s1.display();
    }
}
```

**Five ways to create an object in Java:**
1. `new` keyword
2. `newInstance()` method of `Class`
3. `newInstance()` method of `Constructor`
4. `clone()` method
5. Deserialization

What each way does (run on Java 21):

| # | Way | Constructor runs? | Notes |
|---|---|---|---|
| 1 | `new` | **yes** | the normal way |
| 2 | `Class.newInstance()` | yes | **deprecated since Java 9**; it still works but the compiler warns |
| 3 | `Constructor.newInstance()` | yes | the modern replacement for #2, through `getDeclaredConstructor()`. Used by reflection and frameworks (for example, Spring creating beans) |
| 4 | `clone()` | **no** | copies the fields of an existing object; needs `implements Cloneable` |
| 5 | deserialization | **no** | rebuilds an object from saved bytes; needs `implements Serializable` |

```java
import java.io.*;

public class FiveWays {
    static class Question implements Cloneable, Serializable {
        String text;
        int[] tags;
        transient int cache;           // transient: skipped by serialization

        public Question() {
            this.text = "default";
            this.tags = new int[]{1, 2};
            this.cache = 7;
            System.out.println("  constructor ran");
        }

        @Override
        protected Question clone() throws CloneNotSupportedException {
            return (Question) super.clone();     // copies the fields without running a constructor
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("1. new");
        Question a = new Question();

        System.out.println("2. Class.newInstance (deprecated since Java 9)");
        @SuppressWarnings("deprecation")
        Question b = (Question) Class.forName("FiveWays$Question").newInstance();

        System.out.println("3. Constructor.newInstance");
        Question c = Question.class.getDeclaredConstructor().newInstance();

        System.out.println("4. clone()");
        Question d = a.clone();
        System.out.println("  same object? " + (d == a) + " | same tags array? " + (d.tags == a.tags));

        System.out.println("5. deserialization");
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        try (ObjectOutputStream out = new ObjectOutputStream(bytes)) {
            a.text = "saved";
            a.cache = 99;
            out.writeObject(a);
        }
        Question e;
        try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(bytes.toByteArray()))) {
            e = (Question) in.readObject();
        }
        System.out.println("  text=" + e.text + " | cache=" + e.cache + " (transient: not saved, so it is 0)");
    }
}
```

Output:

```
1. new
  constructor ran
2. Class.newInstance (deprecated since Java 9)
  constructor ran
3. Constructor.newInstance
  constructor ran
4. clone()
  same object? false | same tags array? true
5. deserialization
  text=saved | cache=0 (transient: not saved, so it is 0)
```

Points to remember:

- **Only `clone()` and deserialization skip the constructor.** `new`, `Class.newInstance()` and `Constructor.newInstance()` all run it.
- **`clone()` is a shallow copy.** The copy is a different object (`d == a` is `false`), but the arrays and objects its fields point to are shared (`d.tags == a.tags` is `true`), so changing one changes the other.
- **Deserialization skips `transient` fields.** After reading the object back, `text` was `"saved"` but the `transient int cache` was `0` (the default), not the `99` that was set. Use `transient` to keep passwords and caches out of a saved object.
- **`Class.newInstance()` is deprecated** because it could throw checked exceptions from the constructor without declaring them. `Constructor.newInstance()` replaced it.
- **In everyday code you use `new`.** For copying, many teams prefer a **copy constructor** (`new Question(other)`) over `clone()`, which has awkward rules.

## 10.4 Attributes (data members)

Attributes describe the **state** of an object. Uninitialised fields get their type's default value.

```java
class Car {
    String brand;    // default null
    int speed;       // default 0
    double price;    // default 0.0
}
```

## 10.5 Constructors

A constructor is a special block of code, similar to a method, that is **called when an instance of the class is created**. At that moment memory for the object is allocated. Use it to set initial values.

**Rules**
- Its name must be exactly the class name.
- It has **no return type** (not even `void`).
- It is called automatically when an object is created.

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
Person person = new Person("John Doe", 30);
```

### Default vs parameterized constructor

| Default constructor | Parameterized constructor |
|---|---|
| Takes no parameters | Takes one or more parameters |
| Supplied implicitly by the compiler if you define no constructor at all | You must write it yourself |
| Initialises instance variables to defaults | Lets you set specific values at creation time |

```java
class Student {
    int id;
    String name;

    Student() { id = 0; name = "null"; }             // default
    Student(int id, String name) {                    // parameterized
        this.id = id;
        this.name = name;
    }
}
Student s1 = new Student();
Student s2 = new Student(1, "John Doe");
```

### Constructor overloading

Having more than one constructor with different parameter lists — exactly like method overloading.

### Constructor vs method

| Constructor | Method |
|---|---|
| Same name as the class | Any valid name |
| No return type | Must declare a return type |
| Called automatically on object creation | Called explicitly |
| Initialises an object | Defines behaviour |
| Never inherited, and **cannot be `final`** | Can be inherited and overridden |

### Private constructors

A constructor can be declared `private`. Consequences:
- The class cannot be sub-classed (extending it is a compile-time error).
- Objects cannot be created from outside the class.
- It cannot be accessed from any other class.

Use cases: static-members-only classes, utility/constant classes, **singleton classes**, named factory methods, and preventing sub-classing.

### Singleton design pattern

"Define a class that has only one instance and provides a global point of access to it."

Two forms:
- **Early instantiation** — the instance is created at class-load time.
- **Lazy instantiation** — the instance is created only when it is first required.

**Advantage:** saves memory, because the object is not created on each request — a single instance is reused.

## 10.6 The `this` keyword

`this` is a **reference variable that refers to the current object**.

**Use 1 — resolve a naming conflict** between a field and a parameter:
```java
class User {
    String name;
    User(String name) {
        this.name = name;   // this.name = field, name = parameter
    }
}
```

**Use 2 — call another constructor of the same class:**
```java
class User {
    String name; int age;
    User() { this("Guest", 18); }        // calls the other constructor
    User(String name, int age) { this.name = name; this.age = age; }
}
```

## 10.7 The `static` keyword

`static` is used mainly for **memory management**. A static member belongs to the **class** rather than to any instance. It can be applied to variables, methods, blocks and nested classes.

### Static variable
- Represents a common property of all objects — a company name for employees, a college name for students.
- Gets memory **only once**, in the class area, at class-loading time.

```java
class Counter {
    static int count = 0;
    Counter() { count++; }
    static void showCount() { System.out.println("Count = " + count); }
}
Counter c1 = new Counter();   // count = 1
Counter c2 = new Counter();   // count = 2
Counter.showCount();          // Count = 2
```

### Static method
- Belongs to the class, not an object.
- Can be invoked without creating an instance.
- Can access and change static data members.
- **Cannot** access non-static variables or methods directly.
- Typically used for utility functions (`Math.sqrt`, string helpers).

### Static block
- Used to initialise static data members.
- Executed **before** the `main` method, at class-loading time.

```java
class Task {
    static { System.out.print("A"); }        // runs first, at class load
    public Task() { System.out.print("B"); } // runs on each object creation
}
```

## 10.8 Instance initializer block

An instance initializer block initialises **instance** data members. It runs **every time an object is created**, before the constructor body.

## 10.9 The `final` keyword

`final` restricts the user. It can be applied in three places:

1. **final variable** — the value cannot be changed; it becomes a constant.
2. **final method** — it cannot be overridden.
3. **final class** — it cannot be extended.

Questions that come up constantly:
- **Is a final method inherited?** Yes — inherited, but not overridable.
- **What is a blank (uninitialised) final variable?** A final variable that is not initialised at declaration.
- **Can you initialise a blank final variable?** Yes, but **only in the constructor**.
- **What is a final parameter?** A parameter whose value cannot be changed inside the method.
- **Can a constructor be final?** No — constructors are never inherited, so it would be meaningless.

## 10.10 Practice: classes and objects

Seven practice problems on classes. Write each class as a **top-level, non-public class** in one `Main.java` (with `public class Main` last), not nested inside `Main`: nested classes can read each other's `private` members, so `private` would not be enforced. As top-level classes it is. Run with `javac Main.java && java Main`. Each solution below is a complete file with the class and its test, and every printed line was run on Java 21.

### Problem 1: `BankAccount`: private fields and validation

**Describe:** Why are the fields `private`? Why validate in the constructor and in each method?

**Write:** A class with `private final String owner` and `private double balance`. The constructor takes `(owner, opening)` and rejects a negative opening balance. `deposit` and `withdraw` reject non-positive amounts, and `withdraw` rejects more than the balance. Add `getBalance()` and a `toString()` that returns `owner: balance`. Errors are `IllegalArgumentException` with the messages in the answer.

<details>
<summary>Answer</summary>

`private` means other classes can only change the balance through your methods, so every change goes through the checks. Each method validates **before** it changes anything, so a bad value never reaches the line that updates the balance.

```java
class BankAccount {
    private final String owner;
    private double balance;

    BankAccount(String owner, double opening) {
        if (opening < 0) {
            throw new IllegalArgumentException("opening balance cannot be negative");
        }
        this.owner = owner;
        this.balance = opening;
    }

    void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("deposit must be positive");
        }
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("withdrawal must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("insufficient funds");
        }
        balance -= amount;
    }

    double getBalance() {
        return balance;
    }

    @Override
    public String toString() {
        return owner + ": " + balance;
    }
}

public class Practice1 {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Ann", 100);
        acc.deposit(50);
        acc.withdraw(30);
        System.out.println(acc);                       // => Ann: 120.0
        try { acc.withdraw(500); } catch (IllegalArgumentException e) { System.out.println("error: " + e.getMessage()); }   // => error: insufficient funds
        try { acc.deposit(-5); } catch (IllegalArgumentException e) { System.out.println("error: " + e.getMessage()); }     // => error: deposit must be positive
        try { new BankAccount("Bo", -1); } catch (IllegalArgumentException e) { System.out.println("error: " + e.getMessage()); }   // => error: opening balance cannot be negative
        System.out.println(acc.getBalance());          // => 120.0
        // acc.balance = 5;                            // ❌ error: balance has private access in BankAccount
    }
}
```
</details>

### Problem 2: `Student`: a static counter and a final id

**Describe:** Why is `id` `final` but `nextId` not? Why can `count()` be `static`?

**Write:** Each new student gets the next id (1, 2, 3...). Fields: `private static int nextId`, `private final int id`, `private final String name`. `static int count()` says how many students exist. `toString()` returns `#id name`.

<details>
<summary>Answer</summary>

`id` is `final` because a student's id is assigned once, in the constructor, and must never change. `nextId` is shared by the whole class and has to go up every time a student is created, so it can't be `final`. `count()` can be `static` because it only reads the class-level counter and needs no particular student.

```java
class Student {
    private static int nextId = 1;        // shared by every student
    private final int id;
    private final String name;

    Student(String name) {
        this.id = nextId++;               // take the current value, then increase it
        this.name = name;
    }

    static int count() {
        return nextId - 1;
    }

    @Override
    public String toString() {
        return "#" + id + " " + name;
    }
}

public class Practice2 {
    public static void main(String[] args) {
        Student s1 = new Student("Ann"), s2 = new Student("Bo"), s3 = new Student("Cy");
        System.out.println(s1 + " | " + s2 + " | " + s3 + " | count=" + Student.count());   // => #1 Ann | #2 Bo | #3 Cy | count=3
    }
}
```
</details>

### Problem 3: `Question`: constructor chaining

**Describe:** How do several constructors share one piece of code? What rule applies to `this(...)`?

**Write:** A `Question` with `private final` `text` and `difficulty`. Three constructors: `(text, difficulty)`, `(text)` that defaults the difficulty to `"easy"`, and `()` that uses the text `"untitled"`. The shorter ones must use `this(...)` and not repeat the assignments.

<details>
<summary>Answer</summary>

Put the real work in one constructor and make the others call it with `this(...)`. `this(...)` must be the **first statement** in the constructor.

```java
class Question {
    private final String text;
    private final String difficulty;

    Question(String text, String difficulty) {
        this.text = text;
        this.difficulty = difficulty;
    }

    Question(String text) {
        this(text, "easy");
    }

    Question() {
        this("untitled");                 // calls Question(String), which calls Question(String, String)
    }

    @Override
    public String toString() {
        return text + " (" + difficulty + ")";
    }
}

public class Practice3 {
    public static void main(String[] args) {
        System.out.println(new Question("What is a closure?", "hard"));   // => What is a closure? (hard)
        System.out.println(new Question("What is hoisting?"));            // => What is hoisting? (easy)
        System.out.println(new Question());                               // => untitled (easy)
    }
}
```
</details>

### Problem 4: `Counter`: a fluent class with `return this`

**Describe:** What type do `inc()`, `dec()` and `add(int)` return, and why does returning `this` allow chaining?

**Write:** Methods `inc()`, `dec()` and `add(int n)` each return the same object so that calls chain. `get()` returns the value.

<details>
<summary>Answer</summary>

They return `Counter`, the object they were called on. `return this;` hands the same object back, so the next call in the chain is made on it.

```java
class Counter {
    private int value;

    Counter inc() { value++; return this; }
    Counter dec() { value--; return this; }
    Counter add(int n) { value += n; return this; }
    int get() { return value; }
}

public class Practice4 {
    public static void main(String[] args) {
        System.out.println(new Counter().inc().inc().add(10).dec().get());   // => 11
    }
}
```
</details>

### Problem 5: `Point`: an immutable class

**Describe:** What makes a class immutable? How do you "change" an immutable object?

**Write:** A `final` class with `private final int x, y`, getters and no setters. `withX(int newX)` returns a new `Point` with the changed x. `plus(Point other)` returns a new `Point`. `toString()` returns `(x, y)`.

<details>
<summary>Answer</summary>

Make the class `final` (so no subclass can add mutable state), make every field `private final`, set them only in the constructor, and provide no setters. To "change" a value you build a **new** object and leave the old one alone.

```java
final class Point {
    private final int x;
    private final int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    int getX() { return x; }
    int getY() { return y; }

    Point withX(int newX) { return new Point(newX, y); }
    Point plus(Point other) { return new Point(x + other.x, y + other.y); }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

public class Practice5 {
    public static void main(String[] args) {
        Point p = new Point(1, 2);
        Point q = p.withX(9);
        System.out.println(p + " " + q + " " + p.plus(new Point(10, 10)));   // => (1, 2) (9, 2) (11, 12)
        // p.x = 5;                                                           // ❌ error: x has private access in Point
    }
}
```
The original `p` stays `(1, 2)`. `String` is immutable in the same way.
</details>

### Problem 6: `Temperature`: a private constructor and static factory methods

**Describe:** Why use `ofCelsius` and `ofFahrenheit` instead of two constructors that both take a `double`?

**Write:** A class whose constructor is `private`. Objects are created only through `Temperature.ofCelsius(double)` and `Temperature.ofFahrenheit(double)`. `celsius()` and `fahrenheit()` convert back.

<details>
<summary>Answer</summary>

Two constructors with the same parameter list (`double`) are not allowed, and even if they were, `new Temperature(5)` doesn't say which unit `5` is. A named factory method says it: `Temperature.ofFahrenheit(212)`. Making the constructor `private` forces everyone to use the factories.

```java
class Temperature {
    private final double celsius;

    private Temperature(double celsius) {
        this.celsius = celsius;
    }

    static Temperature ofCelsius(double c) {
        return new Temperature(c);
    }

    static Temperature ofFahrenheit(double f) {
        return new Temperature((f - 32) * 5 / 9);
    }

    double celsius() { return celsius; }
    double fahrenheit() { return celsius * 9 / 5 + 32; }
}

public class Practice6 {
    public static void main(String[] args) {
        Temperature t = Temperature.ofFahrenheit(212);
        System.out.println(t.celsius() + " " + Temperature.ofCelsius(0).fahrenheit());   // => 100.0 32.0
        // new Temperature(5);                                                           // ❌ error: Temperature(double) has private access in Temperature
    }
}
```
</details>

### Problem 7: `Library`: objects in an array

**Describe:** How does a class hold several objects of another class? What does `find` return when nothing matches?

**Write:** A `Book` has a `final String title` and a `boolean available` that starts `true`. A `Library` is built from several books (`Library(Book... books)`) with `find(title)` (the `Book`, or `null`), `checkOut(title)` (`true` and mark it unavailable if it exists and is available, otherwise `false`), and `availableCount()`.

<details>
<summary>Answer</summary>

`Book... books` is a varargs parameter, and inside the method it is an array. `find` returns `null` when nothing matches, so `checkOut` must handle `null` before using the result.

```java
class Book {
    final String title;
    boolean available = true;

    Book(String title) {
        this.title = title;
    }
}

class Library {
    private final Book[] books;

    Library(Book... books) {
        this.books = books;
    }

    Book find(String title) {
        for (Book b : books) {
            if (b.title.equals(title)) return b;
        }
        return null;
    }

    boolean checkOut(String title) {
        Book b = find(title);
        if (b == null || !b.available) return false;
        b.available = false;
        return true;
    }

    int availableCount() {
        int n = 0;
        for (Book b : books) {
            if (b.available) n++;
        }
        return n;
    }
}

public class Practice7 {
    public static void main(String[] args) {
        Library lib = new Library(new Book("Dune"), new Book("Emma"), new Book("Ulysses"));
        System.out.println(lib.checkOut("Dune") + " " + lib.checkOut("Dune") + " " + lib.checkOut("Nope") + " " + lib.availableCount());   // => true false false 2
    }
}
```
Compare strings with `.equals()`, never `==` (the same rule as in your notes).
</details>

---

# Part 11 — OOP Part 2: Inheritance and Polymorphism

## 11.1 Inheritance

Inheritance is the mechanism where **one object acquires all the properties and behaviours of a parent object**. It represents an **IS-A** relationship (a parent-child relationship) and is implemented with the `extends` keyword.

**Why use it**
1. **Method overriding** — which is how runtime polymorphism is achieved
2. **Code reusability**

The subclass inherits all the `public` and `protected` members of the superclass — fields, methods and constructors.

```java
class Animal {
    String name;
    int age;
    void eat() { System.out.println("Animal is eating"); }
}

class Dog extends Animal {
    String breed;
    void bark() { System.out.println("Dog is barking"); }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.name  = "Fido";
        dog.age   = 5;
        dog.breed = "Labrador";
        dog.eat();    // Animal is eating   (inherited)
        dog.bark();   // Dog is barking
    }
}
```

## 11.2 Types of inheritance

1. **Single** — one class inherits one class.
2. **Multilevel** — a chain: A -> B -> C.
3. **Hierarchical** — two or more classes inherit from one class.

**Why is multiple inheritance not supported in Java?**
To reduce complexity and simplify the language (the classic "diamond problem"). Multiple inheritance of *type* is achieved instead through **interfaces**.

## 11.3 Aggregation

If a class has an entity reference (holds another object as a field), that is **aggregation**. It represents a **HAS-A** relationship, in contrast to inheritance's IS-A.

## 11.4 The `super` keyword

`super` is a reference variable that refers to the **immediate parent class object**. Three uses:

1. `super.variable` — access a parent field
2. `super.method()` — call a parent method
3. `super(args)` — call the parent constructor (must be the first statement)

```java
class Superclass {
    public Superclass(int x) {
        System.out.println("Superclass constructor called with x = " + x);
    }
}

class Subclass extends Superclass {
    public Subclass(int x, int y) {
        super(x);   // call the superclass constructor
        System.out.println("Subclass constructor called with y = " + y);
    }
}
// Output:
// Superclass constructor called with x = 10
// Subclass constructor called with y = 20
```

## 11.5 Polymorphism

Polymorphism comes from Greek: *poly* = many, *morph* = forms. It is the ability of objects to take many forms — different objects responding to the same method call in different ways.

**Two types:**
1. **Compile-time polymorphism** — method **overloading**
2. **Runtime polymorphism** — method **overriding**

```java
public class Animal {
    public void makeSound() { System.out.println("Animal sound"); }
}
public class Dog extends Animal {
    @Override public void makeSound() { System.out.println("Woof!"); }
}
public class Cat extends Animal {
    @Override public void makeSound() { System.out.println("Meow!"); }
}

Animal animal = new Animal();  animal.makeSound();   // Animal sound
Dog dog = new Dog();           dog.makeSound();      // Woof!
Cat cat = new Cat();           cat.makeSound();      // Meow!
```

## 11.6 Method overriding

When a subclass provides its **own specific implementation** of a method already declared in its parent class.

**Rules**
- Same method name
- Same parameter list
- Same return type (or a **covariant** return type — a subtype)
- The access level cannot be **more restrictive** than the parent's
- Use `@Override` so the compiler catches mistakes

```java
class Animal {
    public void move() { System.out.println("Animals can move"); }
}
class Dog extends Animal {
    @Override public void move() { System.out.println("Dogs can walk and run"); }
}

Animal a = new Animal();
Animal b = new Dog();      // upcasting
a.move();   // Animals can move
b.move();   // Dogs can walk and run  <- the Dog version runs
```

## 11.7 Overloading vs overriding

| Feature | Method Overloading | Method Overriding |
|---|---|---|
| Purpose | Increase readability — same name, different tasks | Give a specific implementation of an inherited method |
| Where | Within one class | Between two classes with an IS-A relationship |
| Parameters | **Must differ** | **Must be the same** |
| Return type | Can be same or different | Must be the same or covariant |
| Polymorphism type | Compile-time | Runtime |
| Inheritance | Not required | Required |
| Can you overload by return type alone? | No — ambiguous | N/A |

## 11.8 Upcasting

When a reference variable of the parent class refers to an object of the child class:

```java
Animal a = new Dog();   // upcasting
```

## 11.9 Static binding vs dynamic binding

Connecting a method call to a method body is called **binding**.

- **Static binding (early binding)** — the type of the object is determined at **compile time**. Applies to `private`, `static` and `final` methods.
- **Dynamic binding (late binding)** — the type of the object is determined at **runtime**. This is how overridden methods work.

**Runtime polymorphism** (also called *dynamic method dispatch*) is the process where a call to an overridden method is resolved at runtime rather than compile time.

## 11.10 Covariant return type

The return type of an overriding method may **vary in the same direction as the subclass** — that is, it may return a subtype of the original return type.

## 11.11 The `instanceof` operator

`instanceof` tests whether an object is an instance of a specified type (class, subclass or interface). It is also called the *type comparison operator*, and it returns `true` or `false`.

```java
if (myObject instanceof Dog) {
    // myObject is a Dog
} else if (myObject instanceof Animal) {
    // an Animal but not a Dog
} else {
    // not an Animal at all
}
```

---

# Part 12 — OOP Part 3: Abstraction

## 12.1 What is abstraction?

Abstraction is **hiding the implementation details and showing only the functionality** to the user. Focus on *what* to do, not *how* to do it.

Two ways to achieve it in Java:
1. **Abstract class** — 0 to 100% abstraction (partial)
2. **Interface** — 100% abstraction (full)

## 12.2 Abstract classes

A class declared with the `abstract` keyword. It **cannot be instantiated** — to use it, another class must inherit from it.

- It can have **both** abstract methods (no body) and concrete methods (with a body).
- It can have constructors, static methods and instance variables.

```java
abstract class Shape {
    abstract void draw();   // abstract method - no body
}

class Circle extends Shape {
    @Override void draw() { System.out.println("Drawing a circle"); }
}

class Rectangle extends Shape {
    @Override void draw() { System.out.println("Drawing a rectangle"); }
}

public class Main {
    public static void main(String[] args) {
        new Circle().draw();      // Drawing a circle
        new Rectangle().draw();   // Drawing a rectangle
    }
}
```

Abstract class with state and a constructor:

```java
abstract class Vehicle {
    String brand;
    Vehicle(String brand) { this.brand = brand; }
    abstract void start();                                   // abstract
    void stop() { System.out.println("Vehicle stopped"); }   // concrete
}

class Car extends Vehicle {
    Car(String brand) { super(brand); }
    void start() { System.out.println("Car started"); }
}
```

Another worked example:

```java
abstract class Animal {
    private String name;
    public Animal(String name) { this.name = name; }
    public abstract void makeSound();
    public String getName() { return name; }
}
class Dog extends Animal {
    public Dog(String name) { super(name); }
    public void makeSound() { System.out.println(getName() + " barks"); }
}
class Cat extends Animal {
    public Cat(String name) { super(name); }
    public void makeSound() { System.out.println(getName() + " meows"); }
}
Animal myDog = new Dog("Buddy");   myDog.makeSound();  // Buddy barks
Animal myCat = new Cat("Fluffy");  myCat.makeSound();  // Fluffy meows
```

## 12.3 Interfaces

An interface is a **blueprint of a class**. It declares behaviour that implementing classes must provide — similar to protocols in other languages.

- All methods are `public` and `abstract` by default.
- All variables are `public static final` (constants).
- No constructors, no instance variables.
- A class implements it with the `implements` keyword.
- A class can implement **multiple** interfaces (comma-separated).
- An interface can only `extends` another interface.
- Since **Java 8** interfaces may also have `default` and `static` methods.

```java
interface Drawable {
    void draw();               // implicitly public abstract
    int MAX_SIZE = 100;        // implicitly public static final
}

class Circle implements Drawable {
    public void draw() { System.out.println("Drawing Circle"); }
}

Drawable d = new Circle();
d.draw();
```

**Why use interfaces?**
1. To achieve abstraction
2. To support the functionality of multiple inheritance
3. To achieve loose coupling

**Marker (tagged) interface** — an interface with no members at all, for example `Serializable`, `Cloneable`, `Remote`. They exist to give the JVM information so it can perform some useful operation.

## 12.4 Abstract class vs interface

| Abstract class | Interface |
|---|---|
| Can have abstract **and** non-abstract methods | Only abstract methods (plus `default`/`static` since Java 8) |
| Does **not** support multiple inheritance | Supports multiple inheritance |
| Can have `final`, non-final, `static` and non-static variables | Only `static final` variables (constants) |
| Can provide the implementation of an interface | Cannot provide the implementation of an abstract class |
| Declared with `abstract` | Declared with `interface` |
| Can extend one class and implement many interfaces | Can only extend other interfaces |
| Extended with `extends` | Implemented with `implements` |
| Members can be `private`, `protected`, etc. | Members are `public` by default |
| Can have constructors | No constructors |
| Can have instance variables | No instance variables |
| 0–100% abstraction | 100% abstraction |

**When to use which:** use an abstract class when you want to share code and state among closely related classes; use an interface when you want to define a contract that unrelated classes can implement.

---

# Part 13 — OOP Part 4: Encapsulation, Packages, Access Modifiers

## 13.1 Encapsulation

Encapsulation is **wrapping code and data together into a single unit** — like a capsule containing several medicines. Data members are made `private` and exposed through `public` getters and setters.

```java
public class Person {
    private String name;
    private int age;

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**Advantages**
- You can make a class **read-only** (only a getter) or **write-only** (only a setter).
- You get **control over the data** — validation logic can live inside the setter (for example, "id must be greater than 100").
- It achieves **data hiding**, because other classes cannot touch the private fields directly.

## 13.2 Packages

A Java package is a **group of similar classes, interfaces and sub-packages**. It organises related code and prevents naming conflicts.

Two categories:
- **Built-in packages** — `java.lang`, `java.util`, `java.io`, `java.net`, `java.sql`, `java.awt`, `javax.swing`
- **User-defined packages** — your own

| Package | Purpose |
|---|---|
| `java.lang` | Core classes (`String`, `Object`, `Math`) — imported automatically |
| `java.util` | Collections, `Scanner`, `Date` |
| `java.io` | Input/output classes |
| `java.net` | Networking classes |
| `java.sql` | JDBC / database classes |

### Declaring a package

```java
package com.example.demo;   // must be the FIRST statement in the file

public class Demo {
    public void show() { System.out.println("Inside custom package!"); }
}
```

Convention: use the reverse domain-name convention (`com.example.demo`), and mirror that as a folder structure `com/example/demo`.

A **sub-package** is a package inside a package, used to categorise further.

### Importing

The `import` statement tells Java where to find a class so you can use its short name. It must be written **after** the package statement.

```java
import java.util.List;              // one class
import java.util.*;                 // everything in the package
import static java.lang.Math.PI;    // a static member
```

## 13.3 Access modifiers

There are two kinds of modifiers in Java: **access modifiers** and **non-access modifiers** (`static`, `final`, `abstract`, `synchronized`, `transient`, `volatile`).

The four access modifiers, weakest to strongest:

1. **`private`** — accessible only within the same class.
2. **default** (no keyword) — accessible only within the same package.
3. **`protected`** — accessible within the package, and outside the package **through a subclass**.
4. **`public`** — accessible from everywhere.

| Modifier | Within class | Within package | Outside package (subclass only) | Outside package |
|---|---|---|---|---|
| `private` | Yes | No | No | No |
| default | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes | No |
| `public` | Yes | Yes | Yes | Yes |

```java
public class AccessExample {
    public    int a = 1;   // everywhere
    protected int b = 2;   // same package and subclasses
              int c = 3;   // default: same package only
    private   int d = 4;   // this class only
}
```

**Why they matter:** they control visibility, improve security, and keep code maintainable.

---

# Part 14 — The `Object` Class and Other Built-in Helpers

## 14.1 The `Object` class

`Object` is the **parent class of every class in Java** — the topmost class. It is useful when you want to refer to an object whose type you do not know:

```java
Object obj = getObject();   // we don't know what this returns
```

A parent-class reference can point at a child-class object (upcasting).

### `toString()`
Returns a String representation. By default it prints `ClassName@hashcode`. Override it to return useful values (see Part 8.10).

### `equals()`
Compares the **value / content** of two objects. It is an instance method of `Object`, so it works on any object.

```java
String str1 = "Hello, World!";
String str2 = "Hello, World!";
boolean areEqual = str1.equals(str2);   // true
```

`==` compares **references**; `equals()` compares **content**.

### `hashCode()`
Returns an `int` hash code representing the object's value. It plays a crucial role in data retrieval in hash-based collections like `HashMap` and `HashSet`.

```java
int hash = "Hello, world!".hashCode();
```
Rule: if you override `equals()`, you must also override `hashCode()`.

### `getClass()`
Returns the runtime class of `this`.

```java
Object obj = new String("Hello, world!");
Class c = obj.getClass();
System.out.println(c.getName());   // java.lang.String
```

### `clone()` — object cloning
`clone()` creates an **exact copy of an object**. In Java there is no operator for copying an object — the assignment operator duplicates the *reference*, not the object. `clone()` fills that gap.

To use it, the class must implement `java.lang.Cloneable`, otherwise `clone()` throws `CloneNotSupportedException`.

**Why use it:** it saves the extra processing of building the copy field by field with `new`, which takes much longer.

**Advantages**
- No lengthy, repetitive copy code — one short `clone()` method
- The easiest and most efficient way to copy objects, especially in existing projects
- The fastest way to copy an array

**Disadvantages**
- You have to change a lot of syntax: implement `Cloneable`, define `clone()`, handle `CloneNotSupportedException`
- You must implement `Cloneable` even though it has no methods (it is a marker interface)

### `finalize()`
Invoked once before an object is garbage collected; used for cleanup. Defined as `protected void finalize(){}`.

## 14.2 The `Math` class

`java.lang.Math` provides methods for maths calculations: `min()`, `max()`, `abs()`, `round()`, `ceil()`, `floor()`, `sqrt()`, `pow()`, `sin()`, `cos()`, `tan()`, and constants like `Math.PI`.

Unlike `StrictMath`, `Math` implementations are not required to return bit-for-bit identical results across platforms.

---

# Part 15 — Exception Handling

## 15.1 What is an exception?

An **exception** is an event that disrupts the normal flow of a program. It is an **object** thrown at runtime.

**Exception handling** is the mechanism that handles runtime errors so the normal flow of the application can be maintained.

Five keywords: **`try`, `catch`, `finally`, `throw`, `throws`**.

## 15.2 The exception hierarchy

```
                Throwable
                /        \
           Error          Exception
      (unrecoverable)     /        \
                  Checked          RuntimeException
                  (compile-time)   (unchecked, runtime)
```

- **`Throwable`** — the superclass of all errors and exceptions.
- **Error** — serious problems, not meant to be handled: `OutOfMemoryError`, `VirtualMachineError`, `AssertionError`. Irrecoverable.
- **Checked exceptions** — classes that directly inherit `Throwable` **except** `RuntimeException` and `Error`: `IOException`, `SQLException`, `FileNotFoundException`, `ClassNotFoundException`. **Checked at compile time — you must handle or declare them.**
- **Unchecked exceptions** — classes inheriting `RuntimeException`: `ArithmeticException`, `NullPointerException`, `ArrayIndexOutOfBoundsException`, `NumberFormatException`, `NoSuchElementException`. Not checked at compile time; checked at runtime.

## 15.3 Checked vs unchecked

| Checked Exception | Unchecked Exception |
|---|---|
| Detected at compile time | Occurs at runtime |
| The compiler checks for it | The compiler does not check |
| Can be handled at compilation time | Cannot be caught or handled at compile time |
| The JVM requires it to be caught or declared | The JVM does not require handling |
| Usually caused by external factors | Usually caused by programming mistakes |
| Example: `FileNotFoundException` | Example: `NoSuchElementException` |

## 15.4 Common exceptions you will meet

| Exception | Cause |
|---|---|
| `ArithmeticException` | Division by zero |
| `NullPointerException` | Accessing a member on a null reference |
| `ArrayIndexOutOfBoundsException` | Invalid array index |
| `StringIndexOutOfBoundsException` | Invalid string index |
| `NumberFormatException` | Invalid string-to-number conversion |
| `ClassCastException` | Invalid cast |
| `IOException` | Input/output failure |
| `IllegalArgumentException` | An argument violates a rule |

## 15.5 `try` and `catch`

The `try` block encloses code that might throw an exception. It must be followed by at least one `catch` block or a `finally` block.

```java
try {
    // code that may throw an exception
} catch (ExceptionType e) {
    // handle it
}
```

```java
public class Demo {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;             // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

## 15.6 Multiple catch blocks

A `try` can be followed by many `catch` blocks, each handling a different exception type. **The most general type (`Exception`) must come last.**

```java
try {
    int a = 10 / 0;
    int[] arr = {1, 2};
    System.out.println(arr[5]);
} catch (ArithmeticException e) {
    System.out.println("Arithmetic : " + e);
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array Index : " + e);
} catch (Exception e) {
    System.out.println("Other Exception : " + e);   // must be last
}
```

## 15.7 Nested try

A `try` block inside another `try` block. Useful when part of a block may cause one error while the whole block may cause another.

## 15.8 `finally`

The `finally` block holds important cleanup code — closing a file, closing a connection. **It always executes, whether an exception was thrown or not, and whether it was handled or not.**

- Follows a `try` or a `catch`.
- Each `try` can have zero or more `catch` blocks but **only one** `finally`.
- It will **not** run if the program exits via `System.exit()` or a fatal error aborts the process.

```java
public class FileInputStreamExample {
    public static void main(String[] args) {
        FileInputStream fis = null;
        try {
            File file = new File("sample.txt");
            fis = new FileInputStream(file);
            int content;
            while ((content = fis.read()) != -1) {
                System.out.print((char) content);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try { fis.close(); } catch (IOException e) { e.printStackTrace(); }
            }
        }
    }
}
```

## 15.9 `throw`

`throw` **explicitly throws** an exception from a method or block. It is followed by an *instance* of an exception. You can throw either checked or unchecked exceptions; it is mainly used for custom exceptions.

```java
public class ThrowExample {
    private int age;

    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative!");
        }
        this.age = age;
    }

    public static void main(String[] args) {
        ThrowExample person = new ThrowExample();
        try {
            person.setAge(-5);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
// Error: Age cannot be negative!
```

## 15.10 `throws`

`throws` **declares** an exception. It does not throw anything itself — it warns the caller that this method might throw. It passes the responsibility up to the caller.

```java
returnType methodName() throws ExceptionType {
    // method code
}

void readFile() throws IOException { ... }
```

## 15.11 `throw` vs `throws`

| `throw` | `throws` |
|---|---|
| Actually throws an exception | Declares that a method may throw |
| Followed by an **instance** | Followed by a **class name** |
| Used inside a method body | Used in the method signature |
| Cannot throw multiple exceptions at once | Can declare multiple, comma-separated |

## 15.12 `final` vs `finally` vs `finalize`

| Keyword | What it is | Purpose |
|---|---|---|
| `final` | A keyword | Restricts modification of a variable, method or class |
| `finally` | A block | Ensures a section of code always executes |
| `finalize` | A method | Cleanup on an object just before it is garbage collected |

## 15.13 Exception propagation

Exception propagation happens when an exception is thrown from the top of the call stack and, if not caught, moves down the stack to the previous method, and so on, until it is caught or the program terminates.

## 15.14 try-with-resources

A `try` statement that **declares one or more resources**. A resource is an object that must be closed after use. The statement guarantees each resource is closed at the end, so you cannot leak file handles or connections. The resource must implement `AutoCloseable`.

```java
try (BufferedReader br = new BufferedReader(new FileReader("myfile.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}
// br is closed automatically
```

## 15.15 Custom exceptions

Creating your own exception is known as a **custom** or **user-defined exception**. Java's built-in exceptions cover most general cases, but sometimes you need domain-specific meaning.

```java
class InvalidAgeException extends Exception {
    InvalidAgeException(String message) { super(message); }
}

public class Test {
    static void validate(int age) throws InvalidAgeException {
        if (age < 18) throw new InvalidAgeException("Age must be 18+");
        else System.out.println("Valid Age");
    }

    public static void main(String[] args) {
        try {
            validate(15);
        } catch (InvalidAgeException e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
```

## 15.16 Best practices

- Handle **specific** exceptions first, general ones last.
- Avoid catching the bare `Exception` class where you can name the real one.
- Always provide meaningful messages.
- Use `finally` (or try-with-resources) to close files and connections.
- Never swallow an exception silently.

---

# Part 16 — The Collections Framework

## 16.1 What is the Collections Framework?

The **Collection** in Java is a framework that provides an architecture to **store and manipulate a group of objects**. It supports searching, sorting, insertion, manipulation and deletion.

A **Collection** represents a single unit of objects — a group.

A **framework** provides readymade architecture: a set of classes and interfaces. Using it is optional.

The Collection framework has two parts: **interfaces and their implementing classes**, and **algorithms**.

## 16.2 The hierarchy

```
                    Iterable (root interface)
                        |
                   Collection (interface)                  Map (interface)
        ______________|______________                       |
       |        |         |         |              HashMap  LinkedHashMap  TreeMap
     List      Set      Queue     Deque                     Hashtable
   (interface)(interface)(iface)  (iface)
       |        |         |         |
  ArrayList  HashSet  PriorityQueue ArrayDeque
  LinkedList LinkedHashSet
  Vector     TreeSet
  Stack
```

Note that **`Map` is not a `Collection`** — it sits beside it in the hierarchy.

## 16.3 The four big families

| Interface | Purpose | Key traits | Common classes |
|---|---|---|---|
| **List** | Ordered collection | Allows duplicates, index-based access | ArrayList, LinkedList, Vector, Stack |
| **Set** | Collection of unique elements | No duplicates, order not guaranteed | HashSet, LinkedHashSet, TreeSet |
| **Map** | Key-value pairs | Keys are unique | HashMap, LinkedHashMap, TreeMap, Hashtable |
| **Queue** | FIFO order | Elements removed from the front | LinkedList, PriorityQueue, ArrayDeque |

## 16.4 Generics

Before JDK 1.5 the framework was non-generic. Since 1.5 it is **generic**, so a collection can hold only one type of object. This gives **type safety at compile time** and removes the need for typecasting at runtime.

```java
ArrayList list = new ArrayList();                    // old, non-generic
ArrayList<String> list = new ArrayList<String>();    // generic, type-safe

List<Integer> nums = new ArrayList<>();
nums.add(10);
// nums.add("Hello");   // compile error - caught early
```

Benefits: checked at compile time, no typecasting, code reusability.

## 16.5 `ArrayList`

`ArrayList` uses a **dynamic array** internally. It behaves like an array but has no size limit — you can add or remove elements at any time. It lives in `java.util`.

```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, Serializable
```

You cannot create an ArrayList of primitives — use wrapper classes.

```java
ArrayList<String> list = new ArrayList<>();
list.add("Java");        // index 0
list.add("Python");      // index 1
list.add("C++");         // index 2

list.get(0);             // "Java"
list.set(0, "Kotlin");
list.add(1, 15);         // insert at index
list.remove(2);
list.size();
list.isEmpty();
list.contains("Java");
list.clear();
```

| Method | Description |
|---|---|
| `add(e)` | Adds at the end |
| `add(index, e)` | Adds at a specific index |
| `get(index)` | Returns the element at that index |
| `set(index, e)` | Replaces the element at that index |
| `remove(index)` | Removes at that index |
| `indexOf(o)` | First index of that object |
| `size()` | Number of elements |
| `isEmpty()` | Whether it is empty |
| `contains(o)` | Whether the object exists |
| `clear()` | Removes all elements |

**Traversal:**
```java
for (int i = 0; i < list.size(); i++) System.out.println(list.get(i));
for (String s : list) System.out.println(s);
```

**Key points about ArrayList:** allows duplicates, allows multiple `null` values, is **not synchronized** (not thread-safe), provides index-based access, has less memory overhead than LinkedList, and starts with a default capacity of 10.

### Making a list immutable

```java
// final only stops reassignment, not modification
final ArrayList<String> list = new ArrayList<>();
list.add("One");                     // allowed
// list = new ArrayList<>();         // compile error

// Truly immutable
List<String> immutableList = Collections.unmodifiableList(list);
// immutableList.add("Yellow");      // runtime error
```

## 16.6 `LinkedList`

`LinkedList` uses a **doubly linked list**. It extends `AbstractSequentialList` and implements `List` and `Deque` — so it can act as a list, a stack **or** a queue.

```java
public class LinkedList<E> extends AbstractSequentialList<E>
        implements List<E>, Deque<E>, Cloneable, Serializable
```

Key points: allows duplicates, maintains insertion order, is non-synchronized, and manipulation is fast because no shifting is needed.

```java
LinkedList<Integer> l = new LinkedList<>();
l.add(10); l.add(20);
l.addFirst(5);       // [5, 10, 20]
l.removeLast();      // [5, 10]
```

## 16.7 ArrayList vs LinkedList

| ArrayList | LinkedList |
|---|---|
| Uses a **dynamic array** | Uses a **doubly linked list** |
| Manipulation is **slow** — removing an element shifts all the others | Manipulation is **faster** — no bit shifting required |
| Can act as a List only (implements `List`) | Can act as a List **and** a Queue (implements `List` and `Deque`) |
| Better for **storing and accessing** data | Better for **manipulating** data |
| Memory locations are contiguous | Memory locations are not contiguous |
| Default capacity of 10 on initialisation | No default capacity — starts empty |
| A resizable array | A doubly linked list implementation of the List interface |

## 16.8 The `List` interface

`List` maintains an **ordered collection**. It has index-based methods to insert, update, delete and search. It allows duplicates **and** null elements. It is found in `java.util` and inherits `Collection`. It is a factory for `ListIterator`, which can iterate forwards **and** backwards.

Implementations: `ArrayList`, `LinkedList`, `Stack`, `Vector`.

## 16.9 `Vector`

`Vector` is like a dynamic array that can grow or shrink; it has no size limit. It is part of the Collection framework since Java 1.2 and implements `List`.

- It is **synchronized** — use it only when you actually need a thread-safe implementation. Otherwise use `ArrayList`, which performs better.
- Its iterators are **fail-fast**: on concurrent modification it throws `ConcurrentModificationException`.

## 16.10 `Stack`

`Stack` is a linear structure based on **LIFO (Last-In-First-Out)**. It extends `Vector`.

Operations: `push()`, `pop()`, `peek()`, `empty()`, `search()`.

```java
Stack<String> stack = new Stack<>();
stack.push("A");
stack.push("C");
System.out.println(stack.pop());   // C
```

Modern alternative — use `ArrayDeque` as a stack:
```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10); st.push(20);
st.pop();     // 20
st.peek();    // 10
```

## 16.11 `HashSet`

`HashSet` creates a collection that uses a **hash table** for storage. It extends `AbstractSet` and implements `Set`.

Key points:
- Stores elements using **hashing**
- Contains **unique elements only**
- Allows **one null** value
- **Non-synchronized**
- **Does not maintain insertion order** — elements are placed by hash code
- Best choice for **search** operations
- Initial default capacity **16**, load factor **0.75**

```java
HashSet<String> set = new HashSet<>();
set.add("Java");
set.add("Python");
set.add("C++");
set.add("Java");    // duplicate ignored
set.add(null);      // allowed
System.out.println(set);   // [null, Java, C++]  (no guaranteed order)

set.contains("Java");
set.remove("Java");
set.size();
set.isEmpty();
set.clear();
```

### Set operations — union, intersection, difference

With `A = {1,2,3,4}` and `B = {3,4,5,6}`:

```java
// Union (A ∪ B)
HashSet<Integer> union = new HashSet<>(A);
union.addAll(B);           // {1, 2, 3, 4, 5, 6}

// Intersection (A ∩ B)
HashSet<Integer> inter = new HashSet<>(A);
inter.retainAll(B);        // {3, 4}

// Difference (A - B)
HashSet<Integer> diff = new HashSet<>(A);
diff.removeAll(B);         // {1, 2}
```

## 16.12 `LinkedHashSet`

A hash table **and** linked list implementation of `Set`. It inherits `HashSet` and implements `Set`.

- Unique elements only, like `HashSet`
- Permits null elements
- Non-synchronized
- **Maintains insertion order** — this is the difference from `HashSet`

## 16.13 `TreeSet`

`TreeSet` implements `Set` using a **tree** (red-black tree). It extends `AbstractSet` and implements `NavigableSet`. Objects are stored in **ascending order**.

- Unique elements only
- Access and retrieval times are quite fast
- **Does not allow null**
- Non-synchronized
- Maintains ascending order

```java
TreeSet<String> names = new TreeSet<>();
names.add("Alice"); names.add("Bob"); names.add("Carol"); names.add("Dave");
for (String n : names) System.out.println(n);   // Alice Bob Carol Dave (sorted)
names.contains("Alice");   // true
names.remove("Bob");
```

`add()` returns `false` if the element is already present; `remove()` returns `false` if it is absent.

## 16.14 `EnumSet`

A specialised `Set` implementation for use with **enum types**. It extends `AbstractSet` and implements `Set`.

```java
public abstract class EnumSet<E extends Enum<E>> extends AbstractSet<E>
        implements Cloneable, Serializable
```

## 16.15 The `Queue` interface

`Queue` is in `java.util` and extends `Collection`. It holds elements processed in **First-In-First-Out (FIFO)** order: insertion at the end, removal at the beginning.

Features:
- Supports all `Collection` methods
- The most frequently used implementations are `PriorityQueue`, `ArrayBlockingQueue` and `LinkedList`
- These implementations are **not thread-safe** — for a thread-safe option use `PriorityBlockingQueue`
- `NullPointerException` is raised if a null operation is done on a `BlockingQueue`
- Queues in `java.util` are **unbounded**; queues in `java.util.concurrent` are **bounded**
- All queues except deques allow insertion at the tail and removal from the head; deques allow both at both ends

```java
Queue<Integer> q = new LinkedList<>();
q.add(10); q.add(20); q.add(30);
q.remove();   // 10
q.poll();     // 20  (returns null if empty, instead of throwing)
q.peek();     // 30
```

## 16.16 `PriorityQueue`

`PriorityQueue` processes objects **by priority** rather than strictly FIFO.

## 16.17 The `Deque` interface

`Deque` ("double-ended queue") is a subtype of `Queue` in `java.util`. It supports adding **and** removing at **both ends**, so it can be used as a stack (LIFO) or a queue (FIFO). Common implementation: `ArrayDeque`.

## 16.18 The `Map` interface

A `Map` holds values on the basis of a **key** — a key-value pair. Each pair is called an **entry**. A Map contains **unique keys** but may contain duplicate values.

Use a Map when you need to search, update or delete elements on the basis of a key.

A Map **cannot be traversed directly** — convert it to a Set with `keySet()` or `entrySet()` first.

Two interfaces (`Map`, `SortedMap`) and three main classes (`HashMap`, `LinkedHashMap`, `TreeMap`). `HashMap` and `LinkedHashMap` allow null keys and values; `TreeMap` allows neither a null key nor null values.

## 16.19 `HashMap`

`HashMap` implements `Map` and stores key-value pairs where keys must be unique. Inserting a duplicate key **replaces** the value of that key. It extends `AbstractMap`.

Key points:
- Contains values based on the key
- **Unique keys only**
- May have **one null key** and **multiple null values**
- **Non-synchronized**
- **Maintains no order**
- Initial default capacity **16**, load factor **0.75**
- Since Java 5 it is generic: `HashMap<K,V>`

```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 10);
map.put("B", 20);
map.put("C", 30);

map.get("B");              // 20
map.containsKey("A");      // true
map.containsValue(30);     // true
map.remove("B");
map.keySet();              // [A, C]
map.values();              // [10, 30]
map.isEmpty();
map.clear();
```

| Method | Description |
|---|---|
| `put(k, v)` | Adds or updates a pair; returns the previous value or null |
| `get(k)` | Returns the value for key `k`, or null |
| `remove(k)` | Removes the mapping and returns the previous value |
| `containsKey(k)` | Whether the key exists |
| `containsValue(v)` | Whether the value exists |
| `keySet()` | All keys as a Set |
| `values()` | All values |
| `entrySet()` | All entries as a Set |
| `isEmpty()` / `clear()` | Standard |

### `entrySet()` and iteration

`entrySet()` converts the map's entries into a Set, which is the natural way to iterate:

```java
HashMap<String, Integer> map = new HashMap<>();
map.put("one", 1);
map.put("two", 2);
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " : " + entry.getValue());
}

// It can also remove entries:
map.entrySet().removeIf(e -> e.getKey().equals("one"));
```

### A useful idiom — counting frequency

```java
static Map<Integer, Integer> freq(int[] arr) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int x : arr) {
        map.put(x, map.getOrDefault(x, 0) + 1);
    }
    return map;
}
```

## 16.20 `Hashtable`

`Hashtable` implements a hash table mapping keys to values. It extends `Dictionary` and implements `Map`.

- A Hashtable is an array of lists; each list is a **bucket**. The bucket position is found by calling `hashCode()`.
- Contains unique elements
- **Does not allow a null key or a null value**
- **Synchronized**
- Initial default capacity **11**, load factor **0.75**

## 16.21 HashMap vs Hashtable

| HashMap | Hashtable |
|---|---|
| Non-synchronized, not thread-safe | Synchronized, thread-safe |
| Allows one null key and multiple null values | Allows no null key or value |
| New class introduced in JDK 1.2 | Legacy class |
| Fast | Slow |
| Can be synchronized with `Collections.synchronizedMap(map)` | Internally synchronized; cannot be unsynchronized |
| Traversed by `Iterator` | Traversed by `Enumerator` and `Iterator` |
| The iterator is **fail-fast** | The enumerator is **not** fail-fast |
| Inherits `AbstractMap` | Inherits `Dictionary` |

## 16.22 `LinkedHashMap`

A hash table and linked list implementation of `Map`, with **predictable iteration order**. It extends `HashMap`.

- Contains values based on the key, unique keys
- May have one null key and multiple null values
- Non-synchronized
- **Maintains insertion order** — the difference from `HashMap`
- Default capacity 16, load factor 0.75

## 16.23 `TreeMap`

`TreeMap` is a **red-black tree** based implementation. It stores key-value pairs in **sorted order**. It implements `NavigableMap` and extends `AbstractMap`.

- Values are based on the key; unique elements only
- **Cannot have a null key**, but can have multiple null values
- Non-synchronized
- **Maintains ascending order**

## 16.24 Nested collections

Collections can be nested inside one another.

```java
// Set of Lists
HashSet<List<String>> setOfLists = new HashSet<>();
List<String> l1 = Arrays.asList("A", "B");
List<String> l2 = Arrays.asList("C", "D");
List<String> l3 = Arrays.asList("A", "B");
setOfLists.add(l1);
setOfLists.add(l2);
setOfLists.add(l3);   // duplicate list ignored
System.out.println(setOfLists);   // [[A, B], [C, D]]

// Map of Sets
HashMap<String, HashSet<Integer>> map = new HashMap<>();
map.put("Numbers1", new HashSet<>(Arrays.asList(1, 2)));
map.put("Numbers2", new HashSet<>(Arrays.asList(3, 4)));
```

## 16.25 The `Iterator` interface

`Iterator` lets you access and traverse the elements of a collection (Map, List or Set) and perform operations on each element.

Three methods:
- `hasNext()` — true if more elements remain
- `next()` — returns the next element
- `remove()` — removes the last element returned by `next()`

```java
ArrayList<String> names = new ArrayList<>();
names.add("Alice"); names.add("Bob"); names.add("Charlie");

Iterator<String> iterator = names.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```

## 16.26 The `Collections` utility class

`java.util.Collections` contains **static methods that operate on or return collections**. It supports polymorphic algorithms, and throws `NullPointerException` if the collections or objects given to it are null.

Useful methods: `Collections.sort(list)`, `Collections.sort(list, comparator)`, `Collections.reverse()`, `Collections.shuffle()`, `Collections.max()`, `Collections.min()`, `Collections.unmodifiableList()`, `Collections.synchronizedMap()`.

## 16.27 `Comparable` vs `Comparator`

Both are interfaces used to sort collection elements.

**`Comparable`** — defines the class's **natural sorting order**. Implemented by the class whose objects are being compared, using `compareTo()`.

```java
class Student implements Comparable<Student> {
    int id;
    String name;
    public int compareTo(Student s) {
        return this.id - s.id;      // ascending by id
    }
}
Collections.sort(list);
```

**`Comparator`** — defines a **custom sorting order** without modifying the original class, using `compare()`.

```java
Comparator<Student> byName = new Comparator<Student>() {
    public int compare(Student s1, Student s2) {
        return s1.getName().compareTo(s2.getName());
    }
};
Collections.sort(list, byName);
```

Sorting by more than one field:

```java
public class StudentComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        int nameComparison = s1.getName().compareTo(s2.getName());
        if (nameComparison == 0) {
            return s1.getAge() - s2.getAge();   // tie-break on age
        }
        return nameComparison;
    }
}
students.sort(new StudentComparator());
```

| Comparable | Comparator |
|---|---|
| A **single** sorting sequence | **Multiple** sorting sequences |
| Affects the original class — the class is modified | Does not affect the original class |
| Provides `compareTo()` | Provides `compare()` |
| In `java.lang` | In `java.util` |
| Used by `Collections.sort(List)` | Used by `Collections.sort(List, Comparator)` |

`compare()` and `compareTo()` return: `< 0` if the first is smaller, `0` if equal, `> 0` if the first is greater.

## 16.28 Quick summary table

| Interface / Class | Purpose | Key trait |
|---|---|---|
| List | Ordered collection | Allows duplicates |
| Set | Unique elements | No duplicates, order not guaranteed |
| Map | Key-value pairs | Unique keys |
| Queue | FIFO | Removal from the front |
| Stack | LIFO | Push and pop |
| Collections framework | Interfaces + classes | Unified architecture |
| Generics | Type safety | Compile-time checking |

---

# Part 17 — Multithreading and Concurrency

## 17.1 Multitasking, processes and threads

**Multitasking** is executing multiple tasks simultaneously to use the CPU well. It comes in two forms:

**1. Process-based multitasking (multiprocessing)**
- Each process has its own address space in memory
- A process is **heavyweight**
- The cost of communication between processes is **high**

**2. Thread-based multitasking (multithreading)**
- Threads **share the same address space**
- A thread is **lightweight**
- The cost of communication between threads is **low**

## 17.2 What is a thread?

A thread is a **lightweight sub-process — the smallest unit of processing**, and a separate path of execution. Threads are independent: an exception in one thread does not affect the others. They use a shared memory area.

Every program has at least one thread, the **main thread**, provided by the JVM when execution starts.

**Multithreading** is the process of executing multiple threads simultaneously.

## 17.3 Thread vs process

| Feature | Thread | Process |
|---|---|---|
| Memory space | Shares the process's memory space | Has its own memory space |
| Stack | Has its own stack | Has its own stack |
| Weight | Lightweight | Heavyweight |
| Creation | Created and destroyed by the JVM | Created and destroyed by the OS |
| Communication | Through shared memory | Through IPC (pipes, sockets, shared memory) |

## 17.4 Thread lifecycle (thread states)

A thread always exists in exactly one of these states:

1. **New** — the thread object has been created but `start()` has not been called.
2. **Runnable** — ready to run, waiting to be scheduled.
3. **Running** — the thread scheduler has given it the CPU.
4. **Blocked** — waiting for a monitor lock or for I/O.
5. **Waiting / Timed Waiting** — inactive for a span of time, waiting for another thread to signal or for a timeout.
6. **Terminated (Dead)** — finished normally, or ended abnormally through an unhandled exception.

"Active" covers *runnable* plus *running*. `start()` moves a thread from **new** to **runnable**.

```java
Thread thread = new Thread();
Thread.State state = thread.getState();
```

## 17.5 Two ways to create a thread

**1. Extend the `Thread` class**

```java
public class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Hello from MyThread!");
    }
}

MyThread thread = new MyThread();
thread.start();
```

**2. Implement the `Runnable` interface** (preferred)

`Runnable` has a single method, `run()`. Any class whose instances are meant to be run by a thread should implement it.

```java
public class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Hello from MyRunnable!");
    }
}

Thread thread = new Thread(new MyRunnable());
thread.start();
```

**Why `Runnable` is usually better:** Java allows only single inheritance, so extending `Thread` uses up your one `extends` slot. If your class already extends something else, `Runnable` is the only option. It also separates the *task* from the *thread that runs it*, which is what `ExecutorService` and lambdas rely on.

With a lambda:
```java
Thread t = new Thread(() -> System.out.println("Running"));
t.start();
```

## 17.6 `start()` vs calling `run()` directly

`start()` does three things:
1. Starts a new thread with a **new call stack**
2. Moves the thread from *new* to *runnable*
3. When scheduled, the JVM calls its `run()` method

If you call `run()` **directly**, no new thread is created at all — `run()` simply executes on the current call stack like an ordinary method call.

**Can a thread be started twice?** No. Doing so throws `IllegalThreadStateException`. The thread runs once; the second `start()` throws.

## 17.7 `Thread` class constructors and methods

**Constructors:** `Thread()`, `Thread(String name)`, `Thread(Runnable r)`, `Thread(Runnable r, String name)`

**Commonly used methods:**

| Method | Description |
|---|---|
| `void run()` | The action performed by the thread |
| `void start()` | Starts execution; the JVM calls `run()` |
| `static void sleep(long ms)` | Pauses the current thread for the given milliseconds |
| `void join()` | Waits for this thread to die |
| `void join(long ms)` | Waits for it to die, up to a limit |
| `int getPriority()` / `setPriority(int)` | Get/change priority |
| `String getName()` / `setName(String)` | Get/change name |
| `static Thread currentThread()` | Reference to the currently executing thread |
| `long getId()` | Thread id |
| `Thread.State getState()` | Current state |
| `boolean isAlive()` | Whether it is still alive |
| `static void yield()` | Pause temporarily to let other threads run |
| `boolean isDaemon()` / `setDaemon(boolean)` | Daemon status |
| `void interrupt()` | Interrupts the thread |
| `boolean isInterrupted()` | Whether it has been interrupted |
| `static boolean interrupted()` | Whether the current thread was interrupted (and clears the flag) |
| `suspend()`, `resume()`, `stop()` | **Deprecated** — do not use |

## 17.8 `sleep()`

`sleep()` halts a thread for a given amount of time. After the sleeping time is over, the thread resumes from where it left off.

```java
public static void sleep(long mls) throws InterruptedException
public static void sleep(long mls, int n) throws InterruptedException
```

## 17.9 `join()`

`join()` lets one thread **wait until another finishes**. If `th.join()` is called, the current thread stops and waits until `th` reaches its dead state.

```java
public final void join() throws InterruptedException
```

Overloaded versions let you specify a maximum waiting period.

Practical use: ensure the JVM waits for critical work before exiting.

## 17.10 Naming threads and `currentThread()`

By default threads are named `thread-0`, `thread-1`, and so on.

```java
public String getName();
public void setName(String name);
public static Thread currentThread();   // reference to the running thread
```

## 17.11 Thread priority

Every thread has a priority between **1 and 10**. Higher priority means a better chance of being picked by the scheduler — but it is **not guaranteed**, because it depends on the JVM implementation.

```java
public static int MIN_PRIORITY  = 1;
public static int NORM_PRIORITY = 5;   // the default
public static int MAX_PRIORITY  = 10;
```

`setPriority(int)` throws `IllegalArgumentException` if the value is outside 1–10. Never rely on priorities for correctness — scheduling is not guaranteed across operating systems.

## 17.12 The thread scheduler

The thread scheduler is the JVM component that decides which thread runs and which waits. It only chooses among threads in the **runnable** state.

Two factors:
- **Priority** — higher priority means a better chance
- **Time of arrival** — used as a tie-break when priorities are equal

**Scheduling algorithms:**

1. **First Come First Serve (FCFS)** — the thread that arrived first in the runnable queue runs first. It is non-preemptive, which risks infinite blocking (*starvation*).
2. **Time-slicing** — each thread gets a fixed time slice (say 2 seconds); when it expires the running thread gives up the CPU so others get a turn. This fixes FCFS starvation.
3. **Preemptive-priority scheduling** — the scheduler always picks the highest-priority runnable thread. If a higher-priority thread becomes runnable, the current thread is pre-empted.

When two threads have the same priority and arrival time, FCFS decides.

## 17.13 Daemon threads

A **daemon thread** is a service-provider thread that supports user threads in the background. Its life depends on user threads: **when all user threads die, the JVM terminates daemon threads automatically.**

- It provides background support and has no other purpose
- It is a **low-priority** thread
- Examples running automatically: the garbage collector, the finalizer

**Why does the JVM kill daemon threads?** Because their only job is to serve user threads. If no user threads remain, there is no reason to keep them running.

## 17.14 Synchronization

**Synchronization** is the ability to control the access of multiple threads to a shared resource. When several threads modify shared state at once, you get **inconsistent results** — a *race condition*. Synchronization is necessary for reliable communication between threads.

**The `synchronized` keyword** defines critical sections that only one thread may enter at a time. It can be applied to methods or to blocks.

**Three forms:**

| Form | Syntax | What it locks |
|---|---|---|
| Synchronized method | `public synchronized void display() { }` | The object |
| Synchronized block | `synchronized (this) { }` | A block, on the given object |
| Static synchronized | `public static synchronized void m() { }` | The **class** |

Classic race condition — an online ticket booking system where two threads decrement the seat count at the same time and cause overbooking:

```java
class TicketCounter {
    private int seats = 1;

    public synchronized boolean bookSeat(String user) {
        if (seats > 0) {
            seats--;
            System.out.println(user + " successfully booked a seat.");
            return true;
        }
        System.out.println(user + " failed to book. No seats left.");
        return false;
    }
}

TicketCounter counter = new TicketCounter();
new Thread(() -> counter.bookSeat("User-1")).start();
new Thread(() -> counter.bookSeat("User-2")).start();
```

`synchronized` guarantees only one thread is inside `bookSeat()` at a time, so two users cannot book the last seat simultaneously.

Guidance from the concurrency workbook:
- For simple counters, `AtomicInteger` is lighter than synchronization.
- Use `ReadWriteLock` when reads dominate writes.
- In distributed systems, combine Java synchronization with database-level locking or optimistic concurrency.
- Keep the critical section as small as possible.

## 17.15 `volatile`

`volatile` marks a variable whose value may be modified by different threads. It guarantees that a write by one thread is **immediately visible** to all others (no per-CPU caching of stale values).

```java
public class VolatileExample extends Thread {
    private volatile boolean running = true;

    public void run() {
        while (running) { System.out.println("Running"); }
    }
    public void stopRunning() { running = false; }
}
```

Without `volatile`, the loop might never see the update and would spin forever.

`volatile` gives **visibility**, not **atomicity**. `count++` on a volatile field is still not thread-safe.

## 17.16 `wait()`, `notify()` and `notifyAll()`

These three methods, from the `Object` class, implement **inter-thread communication**.

- **`wait()`** — causes the current thread to wait until another thread calls `notify()` or `notifyAll()` on the same object
- **`notify()`** — wakes up a single thread waiting on that object's monitor
- **`notifyAll()`** — wakes up all threads waiting on that object's monitor

**The three rules that catch people out:**
1. They must be called **while holding the object's monitor** — inside `synchronized` on the same object — otherwise you get `IllegalMonitorStateException`.
2. Always wait in a **`while` loop**, never an `if`. This protects against *spurious wakeups* and missed signals.
3. Prefer `notifyAll()` when there may be multiple waiters; `notify()` risks a lost wakeup.

Producer–consumer with `wait`/`notifyAll`:

```java
class Factory {
    private boolean partAvailable = false;

    public synchronized void produce() throws InterruptedException {
        while (partAvailable) wait();       // producer waits until consumed
        partAvailable = true;
        System.out.println("Part produced");
        notifyAll();
    }

    public synchronized void assemble() throws InterruptedException {
        while (!partAvailable) wait();      // consumer waits until produced
        partAvailable = false;
        System.out.println("Car assembled");
        notifyAll();
    }
}
```

In production code, prefer a `BlockingQueue` or `ReentrantLock` + `Condition` over raw `wait`/`notify`.

## 17.17 Deadlock

**Deadlock** is a condition where two or more threads are blocked forever, each waiting for the other. It usually happens when multiple threads need the same locks but **acquire them in different orders**.

**How to prevent deadlock:**
1. **Avoid unnecessary locking** — lock only when you must, release as soon as possible
2. **Acquire locks in a consistent order** — a global lock ordering removes cycles entirely
3. **Avoid nested locks** — do not take a second lock while holding another
4. **Use timeouts** — `tryLock(timeout)` instead of blocking indefinitely
5. **Use lock-free data structures** where possible
6. Use a deadlock detection and avoidance algorithm as a last resort

Additional guidance: use proper synchronization techniques, be aware of the risk when designing, and test thoroughly.

Classic case: a two-way money transfer where thread A locks account 1 then account 2, while thread B locks account 2 then account 1. Fix it by always locking accounts in a fixed order (for example by account id).

## 17.18 Livelock and starvation

- **Starvation** — a thread never gets the lock because greedier threads keep grabbing it. **Fix:** a **fair** lock, `new ReentrantLock(true)`, which hands the lock out roughly in arrival (FIFO) order. Fairness trades throughput for predictability. Also reduce lock hold time, add backoff, and remove unbounded retries.
- **Livelock** — threads are active and responsive but make **zero forward progress**, because they keep politely stepping aside for each other. CPU is busy but nothing completes. **Fix:** introduce **randomness or backoff with jitter** before retrying, or change the protocol so one side eventually wins (a tie-breaker).

```java
class FairLogWriter {
    private final Lock lock = new ReentrantLock(true);   // fair mode
    public void writeBatch(String who) {
        lock.lock();
        try { /* work */ } finally { lock.unlock(); }
    }
}
```

## 17.19 Explicit locks — `ReentrantLock`

`ReentrantLock` is a more capable alternative to `synchronized`:
- `tryLock(timeout, unit)` — avoid blocking forever
- Interruptible acquisition — clean for service shutdowns
- Fair mode — `new ReentrantLock(true)`
- `Condition` objects — explicit `await()` / `signal()` queues

**Always unlock in a `finally` block** so an exception does not leave the lock held. Keep the lock **private** so external code cannot create lock-ordering cycles.

```java
class CustomerWalletService {
    private final Lock dbLock = new ReentrantLock();

    public void applyCredit(String customerId, int amount) {
        boolean acquired = false;
        try {
            acquired = dbLock.tryLock(200, TimeUnit.MILLISECONDS);
            if (!acquired) throw new IllegalStateException("Busy, try again");

            int current = readBalance(customerId);
            writeBalance(customerId, current + amount);
            audit(customerId, "CREDIT", amount);
        } catch (InterruptedException ie) {
            Thread.currentThread().interrupt();     // preserve interrupt status
            throw new RuntimeException("Interrupted while waiting for lock", ie);
        } finally {
            if (acquired) dbLock.unlock();
        }
    }
}
```

## 17.20 `ReadWriteLock` and `StampedLock`

When **many threads read and few write**, a `ReadWriteLock` lets all readers proceed in parallel while writers get exclusive access. `StampedLock` adds optimistic reads for even better read-heavy performance.

## 17.21 Atomic classes

For simple single-variable updates, the lock-free atomic classes in `java.util.concurrent.atomic` are the right tool.

```java
class RequestCounter {
    private final AtomicInteger count = new AtomicInteger();
    public int incrementAndGet() { return count.incrementAndGet(); }
    public int snapshot() { return count.get(); }
}
```

- **`AtomicInteger` / `AtomicLong`** — perfect for single-variable atomic operations, no blocking, good scalability.
- **`LongAdder`** — better under *very high write contention*; it spreads contention across cells. Reads (`sum()`) may be slightly stale, which is fine for metrics.
- **When the update has rules** (a cap, an invariant), you need a lock, not an atomic:

```java
class CappedCounter {
    private final ReentrantLock lock = new ReentrantLock();
    private int value = 0;
    private final int cap;
    CappedCounter(int cap) { this.cap = cap; }

    public boolean tryIncrement() {
        lock.lock();
        try {
            if (value >= cap) return false;
            value++;
            return true;
        } finally { lock.unlock(); }
    }
}
```

Never do a naive "read, then write" without atomicity — it invites lost updates. If you must update based on the current value, use `compareAndSet` in a small loop.

## 17.22 Concurrent collections

- **`ConcurrentHashMap`** — thread-safe map for caching, far better than `Collections.synchronizedMap`
- **`BlockingQueue`** (`ArrayBlockingQueue`, `LinkedBlockingQueue`) — thread-safe handoff between producers and consumers, with built-in **backpressure** when bounded
- **`CopyOnWriteArrayList`** — for read-heavy lists
- **`ThreadLocal`** — gives each thread its own copy of a variable; ideal for request-scoped data

## 17.23 Thread pools and `ExecutorService`

A **thread pool** is a group of worker threads that wait for jobs and are **reused many times**. A fixed-size group is created up front; the service provider pulls a thread out of the pool and assigns it a job.

**Advantage:** better performance — it saves time because a new thread does not have to be created for each task. Creating a thread per task does not scale.

**Real usage:** Servlet and JSP containers create a thread pool to process requests.

**Factory methods:**

| Method | Description |
|---|---|
| `newFixedThreadPool(int n)` | A pool of exactly `n` threads |
| `newCachedThreadPool()` | Creates new threads as needed, reusing idle ones |
| `newSingleThreadExecutor()` | A single worker thread |
| `newScheduledThreadPool(int n)` | For delayed and recurring tasks |

### Graceful shutdown

The sequence is **`shutdown()` -> `awaitTermination()` -> (if needed) `shutdownNow()`**.

```java
ExecutorService pool = Executors.newFixedThreadPool(3);

for (int i = 0; i < 5; i++) {
    pool.submit(() -> {
        try {
            System.out.println(Thread.currentThread().getName() + " working");
            Thread.sleep(300);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();   // respond to shutdownNow
        }
    });
}

pool.shutdown();                                  // stop accepting new tasks
try {
    if (!pool.awaitTermination(2, TimeUnit.SECONDS)) {
        List<Runnable> dropped = pool.shutdownNow();   // cancel queued, interrupt running
        System.out.println("Cancelled queued: " + dropped.size());
        if (!pool.awaitTermination(2, TimeUnit.SECONDS)) {
            System.err.println("Pool did not terminate cleanly");
        }
    }
} catch (InterruptedException ie) {
    pool.shutdownNow();
    Thread.currentThread().interrupt();
}
```

- `shutdown()` is idempotent: it rejects new tasks but lets running ones finish.
- `shutdownNow()` interrupts running tasks and drains the queue; well-written tasks check the interrupt flag and exit quickly.
- **Always restore the interrupt status** when catching `InterruptedException`, so higher layers can observe it.

## 17.24 `Callable` and `Future`

`Runnable` returns nothing. **`Callable<V>`** returns a value and may throw a checked exception. Submitting a `Callable` gives you a **`Future<V>`**.

- `future.get()` — blocks until the result is ready
- `future.get(timeout, unit)` — enforces a time limit
- `future.cancel(true)` — attempts cancellation
- `future.isCancelled()`, `future.isDone()`

## 17.25 `ExecutorCompletionService`

A plain `ExecutorService` returns futures in **submission order**. `ExecutorCompletionService` wraps an executor with an internal `BlockingQueue` of *finished* tasks, so you can handle results **in completion order** — process whichever comes back first.

```java
ExecutorService pool = Executors.newFixedThreadPool(3);
ExecutorCompletionService<String> ecs = new ExecutorCompletionService<>(pool);

ecs.submit(new MarketDataTask("Stocks", 1200));
ecs.submit(new MarketDataTask("Forex", 500));
ecs.submit(new MarketDataTask("Crypto", 800));

for (int i = 0; i < 3; i++) {
    Future<String> f = ecs.take();   // waits for whichever finishes next
    System.out.println(f.get());
}
pool.shutdown();
```

Use `poll(timeout)` instead of `take()` to avoid blocking forever.

## 17.26 Concurrency utilities

| Utility | What it does | Typical use |
|---|---|---|
| **`CountDownLatch`** | A one-shot gate; threads wait until the count reaches zero | Do not start the app until all subsystems are ready |
| **`CyclicBarrier`** | A reusable rendezvous point for a **fixed** number of threads | Multi-phase workers that must meet at each step |
| **`Phaser`** | Like a barrier but supports a **variable** number of participants across phases | Dynamic team size across phases |
| **`Semaphore`** | Limits concurrent access with permits | Cap concurrent client connections, throttle API calls |
| **`BlockingQueue`** | Thread-safe handoff with backpressure | Producer–consumer pipelines |
| **`Exchanger`** | Atomically swaps objects between exactly two threads | Double-buffer handoff, no copying |
| **`ForkJoinPool`** | Divide-and-conquer work stealing | Parallel aggregation over large datasets |

### Poison pill shutdown

To shut down a multi-consumer `BlockingQueue` pipeline cleanly, insert **one poison pill per consumer** after production ends. Each consumer exits when it dequeues a pill — no fragile shared flags, no timing races.

```java
private static final String PILL = "__STOP__";

BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
ExecutorService pool = Executors.newFixedThreadPool(3);

for (int i = 0; i < 3; i++) {
    pool.submit(() -> {
        try {
            for (;;) {
                String msg = q.take();
                if (PILL.equals(msg)) break;
                System.out.println(Thread.currentThread().getName() + " -> " + msg);
            }
        } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    });
}

for (int i = 1; i <= 20; i++) q.put("job-" + i);
for (int i = 0; i < 3; i++) q.put(PILL);      // one pill per consumer

pool.shutdown();
pool.awaitTermination(5, TimeUnit.SECONDS);
```

### `Exchanger` example

```java
Exchanger<List<Integer>> ex = new Exchanger<>();
// producer: buf = ex.exchange(fullBuffer);   -> receives an empty one back
// consumer: buf = ex.exchange(emptyBuffer);  -> receives the full one
```
The swap is atomic — no copying, minimal GC — and both sides synchronize naturally at each exchange.

## 17.27 `CompletableFuture` — asynchronous composition

`CompletableFuture` is the modern way to run independent work concurrently and compose the results without blocking.

| Method | Purpose |
|---|---|
| `supplyAsync(supplier, executor)` | Start an async task that returns a value |
| `thenApply(fn)` | Transform the result |
| `thenCompose(fn)` | Chain a **dependent** async task (B waits for A) |
| `thenCombine(other, fn)` | Merge two **independent** futures |
| `allOf(...)` | Wait for all of them |
| `anyOf(...)` | Complete when the first one does |
| `exceptionally(fn)` | Recover from a failure |
| `handle((res, ex) -> ...)` | Handle both success and failure |
| `join()` | Get the result (unchecked exception) |
| `get(timeout, unit)` | Get with a checked exception and timeout |

**Aggregating three parallel service calls:**

```java
private static final ExecutorService ioPool = Executors.newFixedThreadPool(10);

CompletableFuture<String> fProduct   = CompletableFuture.supplyAsync(() -> fetchProduct(id), ioPool);
CompletableFuture<String> fPrice     = CompletableFuture.supplyAsync(() -> fetchPrice(id), ioPool);
CompletableFuture<String> fInventory = CompletableFuture.supplyAsync(() -> fetchInventory(id), ioPool);

CompletableFuture<Map<String, String>> combined =
    CompletableFuture.allOf(fProduct, fPrice, fInventory)
        .thenApply(v -> Map.of(
            "product",   fProduct.join(),     // safe: allOf has completed
            "price",     fPrice.join(),
            "inventory", fInventory.join()))
        .exceptionally(ex -> {
            System.err.println("Aggregation failed: " + ex);
            return Map.of("error", "partial/unavailable");
        });
```

**Dependent tasks — payment then dispatch:**

```java
CompletableFuture<String> dispatch = payment.thenCompose(result ->
    CompletableFuture.supplyAsync(() -> {
        System.out.println("Starting dispatch after: " + result);
        return "Order dispatched";
    }, pool));
```

Key practices from the workbook:
- Use a **custom executor** for I/O so these tasks do not fight the common ForkJoin pool.
- Prefer `join()` inside pipelines (unchecked) and `get()` when you need checked exceptions or a timeout.
- Avoid blocking calls inside async stages unless you are on a dedicated I/O pool — blocking the common pool risks thread starvation.
- Attach error handling at the right granularity: per-future with `exceptionally`, or globally on the combined stage.
- Add circuit breakers and bulkheads (Resilience4j) for flaky upstreams.
- `thenCompose` for **dependent** calls; `thenCombine` for **independent** ones you merge.

## 17.28 Parallel streams

`list.parallelStream()` splits work across the common ForkJoin pool. Two warnings from the workbook:
- **Parallel streams corrupt shared mutable state.** Use collectors and reductions, never a shared accumulator.
- **A parallel stream is slower than sequential on small data** — the coordination overhead dominates.

## 17.29 Handling `InterruptedException` correctly

Never swallow it. Either rethrow it, or restore the flag:

```java
catch (InterruptedException e) {
    Thread.currentThread().interrupt();   // restore the interrupt status
}
```

## 17.30 Doing one task vs many tasks with multiple threads

- To perform **a single task** with many threads, write **one** `run()` method and give it to all of them.
- To perform **multiple tasks** with multiple threads, write **multiple** `run()` methods.

## 17.31 `ThreadGroup`

`java.lang.ThreadGroup` groups multiple threads into a single object, so you can suspend, resume or interrupt a whole group in one call. Thread groups form a tree — every group except the initial one has a parent. A thread can read information about its own group but not about its parent group or any other group.

Constructors:
- `ThreadGroup(String name)`
- `ThreadGroup(ThreadGroup parent, String name)`

## 17.32 The concurrency scenario index (70 real-world problems)

The concurrency workbook in this folder is organised as 70 interview scenarios. Use this as a practice checklist — the technique to reach for is in the right column.

| # | Scenario | Technique |
|---|---|---|
| 1 | Thread lifecycle in action | Thread basics |
| 2 | Runnable vs Thread in a web application | Runnable composition |
| 3 | Synchronization for a shared resource | `synchronized` |
| 4 | Aggregate multiple API calls asynchronously | `CompletableFuture` + `allOf` |
| 5 | Correctly updating a shared counter under contention | `AtomicInteger` / `LongAdder` |
| 6 | Exclusive DB update without collisions | `ReentrantLock` + `tryLock` |
| 7 | Producer makes parts, assembler must wait | `wait` / `notifyAll` |
| 8 | Gracefully shutting down an ExecutorService | `shutdown` / `awaitTermination` |
| 9 | Dependent asynchronous tasks | `thenCompose` |
| 10 | Retrying flaky API calls with timeout | `get(timeout)` + retry loop |
| 11 | Phase-by-phase coordination across threads | `CyclicBarrier` |
| 12 | Enforce per-task time limits with clean cancellation | `Future.cancel` |
| 13 | Chain dependent async steps without blocking | `CompletableFuture` chaining |
| 14 | Limit concurrent access with permits | `Semaphore` |
| 15 | Heavy computation in parallel with limited threads | Fixed thread pool |
| 16 | Many readers, few writers | `ReadWriteLock` |
| 17 | Graceful cancellation of long-running tasks | Interruption |
| 18 | Orchestrating interdependent tasks (DAG style) | `CompletableFuture` graph |
| 19 | Strict task order A -> B -> C | Chained futures |
| 20 | Keep the pipeline running when some tasks fail | `exceptionally` / `handle` |
| 21 | Fire many independent tasks, resume when all finish | `allOf` / `invokeAll` |
| 22 | Prevent starvation when many threads compete | Fair `ReentrantLock(true)` |
| 23 | Threads keep dodging each other, no progress | Livelock — backoff with jitter |
| 24 | Enforce a hard deadline for work | Timeout |
| 25 | Handling `InterruptedException` the right way | Restore interrupt status |
| 26 | Multi-phase work with a rendezvous | `CyclicBarrier` |
| 27 | Many CPU-heavy tasks without melting the machine | Pool sized to cores |
| 28 | Server handling many requests without thread-per-request | Thread pool / virtual threads |
| 29 | Separate high/low priority pipelines, served in order | Priority queues |
| 30 | Two-way money transfers freeze the system | Deadlock — lock ordering |
| 31 | Mixed-duration jobs with limited workers | Pool tuning |
| 32 | Cap concurrent client connections | `Semaphore` |
| 33 | Handle results the moment they are ready | `ExecutorCompletionService` |
| 34 | Producer hands off data; consumer waits | `BlockingQueue` |
| 35 | Threads grab different locks and wait forever | Deadlock analysis |
| 36 | Many quick tasks — do not spawn a thread per task | Thread pooling |
| 37 | Do not start the app until all subsystems are ready | `CountDownLatch` |
| 38 | Multi-phase workers rendezvous at each step | `CyclicBarrier` |
| 39 | Speed up independent element processing over a big list | Parallel streams |
| 40 | Ensure the JVM waits for critical work before exit | `join()` / non-daemon threads |
| 41 | Class already extends a base type but must run concurrently | Implement `Runnable` |
| 42 | Prevent an inconsistent balance | Synchronization |
| 43 | Consumer waits forever despite data being present | Fix the missed notify |
| 44 | Avoid deadlock in a two-account transfer | Consistent lock ordering |
| 45 | Prevent starvation under heavy contention | Fair lock |
| 46 | Run recurring tasks reliably | `ScheduledExecutorService` |
| 47 | Fan out to multiple services and aggregate safely | `CompletableFuture.allOf` |
| 48 | Producer–consumer with backpressure, many consumers | Bounded `BlockingQueue` |
| 49 | Dynamic team size across phases | `Phaser` |
| 50 | Time-box and cancel an async pipeline | `CompletableFuture` timeout |
| 51 | Parallel stream corrupts shared state | Avoid shared mutable state |
| 52 | Threads must finish init before main continues | `CountDownLatch` / `join` |
| 53 | Parallel and sequential phases in one pipeline | ForkJoin / custom executor |
| 54 | Cancel long-running tasks past a deadline | `Future.cancel` + timeout |
| 55 | Parallel stream slower than sequential on small data | Performance tuning |
| 56 | Multiple readers, single writer, high read frequency | `ReadWriteLock` |
| 57 | Coordinating ordered tasks | Chained futures |
| 58 | Detect and recover from livelock | Livelock detection |
| 59 | Cancel tasks cleanly in an ExecutorService | Graceful shutdown |
| 60 | Parallel aggregation of large datasets | `ForkJoinPool` |
| 61 | Throttle API calls with limited concurrency | `Semaphore` / rate limiter |
| 62 | Coordinate variable participants across phases | `Phaser` |
| 63 | Task dependencies with CompletableFuture | Dependency chaining |
| 64 | Handle starvation in a lock-heavy system | Lock tuning / fairness |
| 65 | Run thousands of tasks efficiently | `ThreadPoolExecutor` tuning |
| 66 | Divide-and-conquer over a big array | ForkJoin framework |
| 67 | Process results as soon as they finish | `ExecutorCompletionService` |
| 68 | Robust async pipeline with fallbacks | `CompletableFuture` + fallback |
| 69 | Double-buffer handoff between two threads | `Exchanger` |
| 70 | Graceful shutdown of a multi-consumer pipeline | `BlockingQueue` + poison pill |

---

# Part 18 — Garbage Collection and the Runtime

## 18.1 Garbage collection

In Java, **garbage** means **unreferenced objects**. Garbage collection is the process of **reclaiming unused runtime memory automatically** — destroying objects nobody is using any more.

**Advantages**
- Makes Java memory efficient, because the collector removes unreferenced objects from the heap
- It is automatic (a part of the JVM), so you do not have to make extra effort

## 18.2 How an object becomes unreferenced

**1. By nulling the reference**
```java
Employee e = new Employee();
e = null;
```

**2. By assigning a reference to another**
```java
Employee e1 = new Employee();
Employee e2 = new Employee();
e1 = e2;   // the first object is now available for garbage collection
```

**3. By using an anonymous object**
```java
new Employee();
```

## 18.3 `finalize()` and `gc()`

- **`finalize()`** is invoked each time **before** an object is garbage collected. Use it for cleanup processing. Defined in `Object` as `protected void finalize(){}`.
- **`gc()`** requests the garbage collector to perform cleanup. It is found in the `System` and `Runtime` classes: `public static void gc(){}`. It is only a *hint* — the JVM decides.

## 18.4 The `Runtime` class

`java.lang.Runtime` lets you interact with the Java runtime environment: execute a process, invoke the GC, query memory. There is exactly **one instance per Java application**.

| Method | Description |
|---|---|
| `public static Runtime getRuntime()` | Returns the Runtime instance |
| `public void exit(int status)` | Terminates the current JVM |
| `public void addShutdownHook(Thread hook)` | Registers a new hook thread |
| `public Process exec(String command)` | Executes the command in a separate process |
| `public int availableProcessors()` | Number of available processors |
| `public long freeMemory()` | Free memory in the JVM |
| `public long totalMemory()` | Total memory in the JVM |

## 18.5 Shutdown hooks

A **shutdown hook** lets you add code that runs when the JVM is shutting down — very handy for cleanup work.

**The JVM shuts down when:**
- The user presses Ctrl+C at the command prompt
- `System.exit(int)` is invoked
- The user logs off
- The machine shuts down

```java
public void addShutdownHook(Thread hook) { }
```

---

# Part 19 — Modern Java (8+)

## 19.1 Lambda expressions

A lambda expression is a **short block of code** used to implement a functional interface.

```java
(parameters) -> expression
(parameters) -> { statements; }
```

```java
// Without lambda
Runnable r1 = new Runnable() {
    public void run() { System.out.println("Hello"); }
};

// With lambda
Runnable r2 = () -> System.out.println("Hello");
r2.run();
```

Lambdas can capture **final or effectively-final** variables from the enclosing scope.

## 19.2 Functional interfaces

A **functional interface** is an interface with exactly **one abstract method**. It can have any number of `default` and `static` methods. Mark it with `@FunctionalInterface` so the compiler enforces the rule.

```java
@FunctionalInterface
interface Hello {
    void show(String msg);
}

Hello h = msg -> System.out.println(msg);
h.show("Functional Interface!");
```

**Common built-in functional interfaces:**

| Interface | Method | Description |
|---|---|---|
| `Runnable` | `run()` | No arguments, no return |
| `Callable<V>` | `call()` | No arguments, returns V, may throw |
| `Comparator<T>` | `compare(a, b)` | Compares two objects |
| `Function<T,R>` | `apply(T t)` | Takes T, returns R |
| `Predicate<T>` | `test(T t)` | Takes T, returns boolean |
| `Consumer<T>` | `accept(T t)` | Takes T, returns nothing |
| `Supplier<T>` | `get()` | Takes nothing, returns T |

## 19.3 The Streams API

Introduced in **Java 8**, the Streams API provides **functional-style operations** on collections: filtering, mapping, sorting, reducing, collecting. It **does not modify the original data** — streams are immutable by default.

```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);

List<Integer> result = nums.stream()
    .filter(n -> n % 2 == 0)      // even numbers
    .map(n -> n * n)              // square them
    .collect(Collectors.toList());

System.out.println(result);       // [4, 16, 36]
```

| Operation | Description |
|---|---|
| `filter()` | Keeps only matching elements |
| `map()` | Transforms each element |
| `sorted()` | Sorts elements |
| `forEach()` | Performs an action on each element |
| `collect()` | Gathers results into a collection |
| `reduce()` | Reduces to a single value |
| `mapToInt().sum()` | Numeric aggregation |
| `count()`, `min()`, `max()` | Aggregates |

```java
int sum = list.stream().mapToInt(i -> i).sum();
```

## 19.4 `Optional`

Introduced in Java 8, `Optional` represents a value that **may or may not be present**. It exists to help you avoid `NullPointerException`.

```java
Optional<String> name = Optional.of("Abhi");
System.out.println(name.isPresent());   // true
System.out.println(name.get());         // Abhi

Optional<String> empty = Optional.empty();
System.out.println(empty.isPresent());       // false
System.out.println(empty.orElse("Guest"));   // Guest

Optional<String> opt = Optional.ofNullable(null);
System.out.println(opt.orElse("No Value"));  // No Value
```

| Method | Description |
|---|---|
| `of(value)` | Creates an Optional with a non-null value |
| `ofNullable(value)` | Creates one that may be empty |
| `empty()` | Creates an empty Optional |
| `isPresent()` | True if a value is present |
| `get()` | Returns the value (only use if present) |
| `orElse(default)` | The value, or a default |

## 19.5 The Date and Time API (`java.time`)

Introduced in Java 8 (JSR-310). It is **modern, thread-safe and easy to use** — unlike the old `java.util.Date`.

| Class | Purpose |
|---|---|
| `LocalDate` | A date (yyyy-mm-dd) |
| `LocalTime` | A time (hh:mm:ss) |
| `LocalDateTime` | Date and time together |
| `ZonedDateTime` | Date and time with a time zone |
| `Duration` | An amount of time in seconds/nanoseconds |
| `Period` | An amount of time in years/months/days |

```java
LocalDate today = LocalDate.now();
LocalTime time  = LocalTime.now();
LocalDateTime dt = LocalDateTime.now();

DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd-MM-yyyy");
String str = today.format(fmt);      // e.g. 10-08-2026
```

## 19.6 Regular expressions

Regex is used to **match patterns in strings** — validation and search. The classes live in `java.util.regex`: `Pattern` and `Matcher`.

```java
String text = "Abhi123 Rathor2026";
String patternStr = "[A-Za-z]+\\d+";

Pattern p = Pattern.compile(patternStr);
Matcher m = p.matcher(text);
while (m.find()) {
    System.out.println(m.group());
}
// Abhi123
// Rathor2026
```

**Common metacharacters:**

| Pattern | Meaning |
|---|---|
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Word character (a-z, A-Z, 0-9, _) |
| `\s` | Whitespace |
| `^` | Start of line |
| `$` | End of line |
| `[abc]` | Any one of a, b or c |
| `[^abc]` | Any character except a, b or c |
| `*` | Zero or more occurrences |
| `+` | One or more occurrences |
| `?` | Zero or one occurrence |

Email validation example:
```java
String email = "abhirathor@gmail.com";
boolean match = Pattern.matches("[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}", email);
System.out.println(match);   // true
```

## 19.7 Enums

An `enum` is a special class that represents a **fixed set of constants**.

```java
enum Day {
    MONDAY, TUESDAY, WEDNESDAY,
    THURSDAY, FRIDAY, SATURDAY, SUNDAY;
}

Day d = Day.MONDAY;
System.out.println(d);
```

Enums can have fields, constructors and methods:

```java
enum Status {
    SUCCESS(200), FAIL(500);

    private final int code;
    Status(int c) { code = c; }
    public int getCode() { return code; }
}
```

## 19.8 Inner classes

| Type | Description |
|---|---|
| **Member inner class** | A non-static class defined inside another class |
| **Static nested class** | A `static` class inside another class |
| **Local inner class** | A class defined inside a method |
| **Anonymous inner class** | A class with **no name**, declared and instantiated at once |

```java
class Outer {
    private int data = 10;
    class Inner {
        void show() { System.out.println("Data = " + data); }
    }
}
Outer o = new Outer();
Outer.Inner i = o.new Inner();
i.show();   // Data = 10
```

**Anonymous class** — a one-time-use implementation without naming a class:

```java
interface Hello { void sayHello(); }

Hello h = new Hello() {
    public void sayHello() { System.out.println("Hello Java"); }
};
h.sayHello();
```

Common use cases: event handling and thread creation. Lambdas have replaced most of these.

## 19.9 Annotations

Annotations provide **metadata for the compiler and tools**.

| Annotation | Purpose |
|---|---|
| `@Override` | Checks that the method really overrides a parent method |
| `@Deprecated` | Marks an old method that should not be used |
| `@SuppressWarnings` | Suppresses specific compiler warnings |
| `@FunctionalInterface` | Enforces exactly one abstract method |

---

# Part 20 — File Handling, I/O and Serialization

## 20.1 The `File` class

The `File` class represents a file or directory **path**. It does not create the file — it just provides information about it and lets you manage it.

```java
import java.io.File;

File file = new File("notes.txt");
System.out.println("File Name: "    + file.getName());
System.out.println("Exists: "       + file.exists());
System.out.println("Is File: "      + file.isFile());
System.out.println("Is Directory: " + file.isDirectory());
```

Creating a file:
```java
File f = new File("demo.txt");
if (f.createNewFile())
    System.out.println("File created");
else
    System.out.println("File already exists");
```

| Method | Description |
|---|---|
| `exists()` | Whether the file exists |
| `createNewFile()` | Creates the file; returns true if created |
| `delete()` | Deletes the file |
| `length()` | File size in bytes |
| `getName()` | File name |
| `getAbsolutePath()` | Absolute path |
| `renameTo(File)` | Renames the file |
| `mkdir()` | Creates a directory |
| `list()` | Lists the files in a directory |

## 20.2 Streams — the two families

| Stream type | Input (read) | Output (write) | Use |
|---|---|---|---|
| **Byte stream** | `FileInputStream` | `FileOutputStream` | Binary data (images, audio) |
| **Character stream** | `FileReader` | `FileWriter` | Text data |

Byte streams handle raw binary data using `read()` and `write()`.

## 20.3 Reading from a file

`FileReader` reads character streams; `BufferedReader` makes it efficient and reads line by line.

```java
import java.io.*;

public class ReadFile {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("notes.txt"));
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
        br.close();
    }
}
```

## 20.4 Writing to a file

`FileWriter` writes character streams; `BufferedWriter` makes it efficient. `write()` **overwrites** previous content and creates the file if it does not exist.

```java
import java.io.*;

public class WriteFile {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter("demo.txt"));
        bw.write("Hello Java File Handling!\n");
        bw.write("Learning is Fun.");
        bw.close();
    }
}
```

## 20.5 Appending to a file

Pass `true` as the second parameter to `FileWriter` — new data goes at the end.

```java
FileWriter fw = new FileWriter("demo.txt", true);   // true = append
fw.write("Appending new line.\n");
fw.close();
```

## 20.6 Copying a file with byte streams

```java
FileInputStream  fis = new FileInputStream("in.txt");
FileOutputStream fos = new FileOutputStream("out.txt");
int ch;
while ((ch = fis.read()) != -1) {
    fos.write(ch);
}
fis.close();
fos.close();
```

## 20.7 CSV file handling

CSV (Comma Separated Values) stores tabular data — each line is a record, values separated by commas.

**Write:**
```java
BufferedWriter bw = new BufferedWriter(new FileWriter("data.csv"));
bw.write("ID,Name,Age\n");
bw.write("1,Abhi,20\n");
bw.write("2,Rohan,22\n");
bw.close();
```

**Read:**
```java
BufferedReader br = new BufferedReader(new FileReader("data.csv"));
String line;
while ((line = br.readLine()) != null) {
    String[] values = line.split(",");
    for (String v : values) System.out.print(v + " | ");
    System.out.println();
}
br.close();
```

## 20.8 JSON file handling

JSON stores data in key-value format (using the `org.json` library).

**Write:**
```java
JSONObject obj = new JSONObject();
obj.put("name", "Abhi");
obj.put("age", 20);
obj.put("city", "Jaipur");

FileWriter fw = new FileWriter("data.json");
fw.write(obj.toString(4));   // 4-space indent
fw.close();
```

**Read:**
```java
FileReader fr = new FileReader("data.json");
JSONTokener tokener = new JSONTokener(fr);
JSONObject obj = new JSONObject(tokener);
System.out.println(obj.getString("name"));
System.out.println(obj.getInt("age"));
fr.close();
```

## 20.9 try-with-resources for files

Prevents resource leaks — streams close automatically when the block ends.

```java
try (BufferedReader br = new BufferedReader(new FileReader("demo.txt"))) {
    String line;
    while ((line = br.readLine()) != null) System.out.println(line);
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

## 20.10 Checked exceptions in file handling

File operations throw checked exceptions, so you must handle them with `try-catch` or declare `throws`.

## 20.11 Serialization and `transient`

**Serialization** converts an object into a byte stream so it can be saved to a file or sent over a network. The class must implement `java.io.Serializable`.

**`transient`** instructs the JVM to **exclude a field from serialization** — it is not saved.

```java
public class Student implements Serializable {
    String firstName;
    String secondName;
    transient String fullName;     // will NOT be serialized
    String email;
    String password;
    Date dob;
    // constructor, toString ...
}

private static void serialize(Student student) {
    try (FileOutputStream fileOut = new FileOutputStream("student.ser");
         ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
        out.writeObject(student);
    } catch (IOException i) { i.printStackTrace(); }
}

private static void deserialize() {
    try (FileInputStream fileIn = new FileInputStream("student.ser");
         ObjectInputStream in = new ObjectInputStream(fileIn)) {
        Student student = (Student) in.readObject();
        System.out.println("Student deserialized: " + student);
    } catch (IOException | ClassNotFoundException i) { i.printStackTrace(); }
}
```

Result — note that `fullName` comes back as **null** after deserialization, because it was `transient`:

```
Student serializing  : Student{firstName='Salman', secondName='Khan', fullName='Salman Khan', ...}
Student deserialized : Student{firstName='Salman', secondName='Khan', fullName='null', ...}
```

## 20.12 File handling best practices

- Read with `FileReader` + `BufferedReader`
- Write with `FileWriter` + `BufferedWriter`
- Append by passing `true` to `FileWriter`
- Always use **try-with-resources** and close your streams
- Use `BufferedReader`/`BufferedWriter` for efficient buffered I/O

---

# Part 21 — JDBC and Databases

## 21.1 What is JDBC?

**JDBC (Java Database Connectivity)** is a Java API to **connect to a database and execute queries**. It is part of Java SE and lives in the `java.sql` package. It uses **JDBC drivers** to talk to a database.

**Why JDBC and not ODBC?** Before JDBC, the ODBC API was used. But ODBC drivers are written in **C** — platform dependent and unsecured. JDBC is pure Java.

## 21.2 Key interfaces and classes

**Interfaces:** `Driver`, `Connection`, `Statement`, `PreparedStatement`, `CallableStatement`, `ResultSet`, `ResultSetMetaData`, `DatabaseMetaData`, `RowSet`

**Classes:** `DriverManager`, `Blob`, `Clob`, `Types`

## 21.3 The four types of JDBC driver

**1. JDBC-ODBC bridge driver**
Converts JDBC calls into ODBC function calls.
- *Advantages:* easy to use; connects to any database
- *Disadvantages:* degraded performance from the conversion; an ODBC driver must be installed on the client machine

**2. Native-API driver (partially Java)**
Uses the client-side libraries of the database, converting JDBC calls into native database API calls.
- *Advantage:* better performance than the bridge driver
- *Disadvantages:* the native driver and the vendor client library must be installed on each client machine

**3. Network Protocol driver (fully Java)**
Uses middleware (an application server) that converts JDBC calls into the vendor-specific protocol.
- *Advantage:* no client-side library needed; the application server can also do auditing, load balancing and logging
- *Disadvantages:* network support required on the client; database-specific coding in the middle tier; costly maintenance

**4. Thin driver (fully Java)**
Converts JDBC calls **directly** into the vendor-specific database protocol.
- *Advantages:* best performance of all four; no software required on client or server
- *Disadvantage:* the driver depends on the database

## 21.4 Driver classes and connection URLs

| Database | Driver class | Connection URL |
|---|---|---|
| MySQL | `com.mysql.cj.jdbc.Driver` | `jdbc:mysql://localhost:3306/mydb` |
| SQLite | `org.sqlite.JDBC` | `jdbc:sqlite:mydata.db` |
| Oracle | `oracle.jdbc.driver.OracleDriver` | `jdbc:oracle:thin:@localhost:1521:xe` |

MySQL is server-based; SQLite is file-based, serverless and lightweight. JDBC works with both, using different drivers.

## 21.5 Database connectivity in 5 steps

**1. Register the driver class** — `Class.forName()` dynamically loads the driver.
```java
public static void forName(String className) throws ClassNotFoundException
```

**2. Get the connection object** — `DriverManager.getConnection()`.
```java
public static Connection getConnection(String url) throws SQLException
public static Connection getConnection(String url, String user, String password) throws SQLException
```

**3. Create the Statement object** — `connection.createStatement()`.
```java
public Statement createStatement() throws SQLException
```

**4. Execute the query** — `statement.executeQuery()` returns a `ResultSet` with all matching records.
```java
public ResultSet executeQuery(String sql) throws SQLException
```

**5. Close the connection** — closing the connection closes the statement and result set automatically.
```java
public void close() throws SQLException
```

Full example:

```java
import java.sql.*;

public class JDBCExample {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/mydb", "root", "password");
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }
            rs.close(); stmt.close(); con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## 21.6 SQL essentials

SQL is the language used to communicate with databases. Its five command families:

| Family | Commands | Purpose |
|---|---|---|
| **DDL** | `CREATE`, `ALTER`, `DROP` | Define structure |
| **DML** | `INSERT`, `UPDATE`, `DELETE` | Manipulate data |
| **DQL** | `SELECT` | Query data |
| **DCL** | `GRANT`, `REVOKE` | Permissions |
| **TCL** | `COMMIT`, `ROLLBACK` | Transactions |

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO users(id, name, email) VALUES(1, 'Abhi', 'abhi@gmail.com');
SELECT * FROM users WHERE id = 1;
UPDATE users SET name = 'Raj' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

SQL keywords are not case-sensitive, but writing them in uppercase is the convention.

## 21.7 CRUD mapping

| Operation | SQL | Example |
|---|---|---|
| Create | `INSERT` | `INSERT INTO users(...) VALUES(...)` |
| Read | `SELECT` | `SELECT * FROM users` |
| Update | `UPDATE` | `UPDATE users SET name='Raj' WHERE id=1` |
| Delete | `DELETE` | `DELETE FROM users WHERE id=1` |

## 21.8 `PreparedStatement`

A **precompiled** SQL statement with `?` placeholders.

**Why it matters:**
- **Prevents SQL injection** — this is the single most important reason
- Faster on repeated execution, because it is precompiled

```java
String sql = "INSERT INTO users(name, email) VALUES(?, ?)";
PreparedStatement ps = con.prepareStatement(sql);
ps.setString(1, "Abhi");
ps.setString(2, "abhi@gmail.com");
int rows = ps.executeUpdate();
System.out.println(rows + " row inserted");
```

**Setter methods:** `setInt(index, value)`, `setString(index, value)`, `setDouble(index, value)`, `setDate(index, date)`

## 21.9 `ResultSet`

`ResultSet` holds the data returned by a `SELECT` query. The cursor moves row by row: `next()` advances it and returns `true` if a row exists.

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
while (rs.next()) {
    int id       = rs.getInt("id");
    String name  = rs.getString("name");
    String email = rs.getString("email");
    System.out.println(id + " - " + name + " - " + email);
}
```

**Getter methods:** `getInt(columnLabel)`, `getString(...)`, `getDouble(...)`, `getDate(...)` — each also works with a column index.

## 21.10 Statement vs PreparedStatement vs CallableStatement

| Type | Use | Security | Performance |
|---|---|---|---|
| `Statement` | Static SQL | Low | Low |
| `PreparedStatement` | Parameterized queries | **High** | **High** |
| `CallableStatement` | Stored procedures | High | Medium |

```java
CallableStatement cs = con.prepareCall("{call getUser(?)}");
cs.setInt(1, 1);
ResultSet rs = cs.executeQuery();
```

## 21.11 Transactions

By default JDBC is in **auto-commit mode**. Set auto-commit to `false` for manual control.

```java
con.setAutoCommit(false);
try {
    PreparedStatement ps1 = con.prepareStatement(
        "UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    ps1.executeUpdate();

    PreparedStatement ps2 = con.prepareStatement(
        "UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    ps2.executeUpdate();

    con.commit();          // all good
} catch (SQLException e) {
    con.rollback();        // something failed, undo everything
} finally {
    con.setAutoCommit(true);
}
```

**Commit saves changes; rollback undoes them.**

## 21.12 JDBC exception handling

| Exception | Cause |
|---|---|
| `SQLException` | General database errors |
| `SQLIntegrityConstraintViolationException` | Constraint violation (PK, FK, UNIQUE) |
| `SQLTimeoutException` | Query timeout |
| `ClassNotFoundException` | Driver class not found |

## 21.13 JDBC best practices

- JDBC is the bridge between Java and databases
- Use `PreparedStatement` for security and performance
- Handle exceptions and **close resources properly** (use try-with-resources)
- Manage transactions with `commit()` and `rollback()`
- Always close connections to free database resources

---

# Part 22 — Reflection

**Java Reflection** is the process of **examining or modifying the runtime behaviour of a class at runtime**.

The `java.lang.Class` class provides many methods to get metadata, examine and change the runtime behaviour of a class. The `java.lang` and `java.lang.reflect` packages provide the reflection classes.

Reflection is what frameworks like Spring and Hibernate use under the hood to instantiate your classes, inject dependencies and map fields.

---

# Part 23 — Problem Solving: DSA Patterns and Complexity

## 23.1 Searching

**Linear search** — check every element, O(n):
```java
static int linearSearch(int[] arr, int key) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == key) return i;
    }
    return -1;   // not found
}
```

**Binary search** — on a **sorted** array, O(log n):
```java
static int binarySearch(int[] arr, int key) {
    int l = 0, r = arr.length - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}
```

**Modified binary search** — for rotated or shifted sorted data: identify which half is sorted, then binary search that half.
**Binary search on the answer** — search over a range of possible answers rather than array indices (for example, the minimum ship capacity to deliver packages in D days).

## 23.2 Sorting and complexity

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| `Arrays.sort()` | O(n log n) | O(n log n) | O(n log n) |

```java
int[] arr = {5, 2, 9, 1, 5};
Arrays.sort(arr);   // [1, 2, 5, 5, 9]
```

## 23.3 Data structure complexity cheat sheet

| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array (unsorted) | O(1) | O(n) | O(n) | O(n) |
| Array (sorted) | O(1) | O(log n) | O(n) | O(n) |
| HashMap / HashSet | O(1) | O(1) | O(1) | O(1) |
| Stack (ArrayDeque) | O(1) | — | O(1) | O(1) |
| Queue (LinkedList) | O(1) | — | O(1) | O(1) |

## 23.4 The core problem-solving patterns

| Pattern | When to use | Example problems |
|---|---|---|
| **Two Pointers** | Sorted arrays, pair problems | Two Sum II, 3Sum, Container With Most Water |
| **Sliding Window** | Subarrays / substrings | Longest Substring Without Repeating Characters, max sum subarray |
| **Fast & Slow Pointers** | Linked list cycles, find the middle | Linked List Cycle |
| **Merge Intervals** | Overlapping ranges | Merge Overlapping Intervals, meeting rooms |
| **Binary Search** | Sorted arrays or answer space | Koko Eating Bananas |
| **Bit Manipulation** | Bit-level tricks | Single Number |
| **Prefix Sum** | Range queries | Range Sum Query |
| **Hashing** | Frequency, lookup in O(1) | Two Sum, anagrams, duplicates |
| **Stack (monotonic)** | Nested structures, next greater | Valid Parentheses, Next Greater Element, Daily Temperatures |
| **Monotonic Queue** | Sliding window min/max | Sliding Window Maximum |
| **Queue / BFS** | Level-order traversal | Binary Tree Level Order, shortest path in an unweighted graph |
| **DFS** | Explore deeply in each direction | Number of Islands |
| **Backtracking** | Try all combinations | N-Queens, permutations, Sudoku |
| **Recursion & Divide and Conquer** | Break into smaller parts | Merge Sort, Tower of Hanoi |
| **Dynamic Programming (1D)** | Store subproblem results | Climbing Stairs, House Robber |
| **Dynamic Programming (2D)** | Two changing states | Longest Common Subsequence, edit distance, grid problems |
| **Greedy** | Best local choice at each step | Activity Selection |
| **Heap / Priority Queue** | Quick access to min/max | Top K Frequent Elements, Kth largest |
| **Union Find (DSU)** | Connectivity, cycle detection | Redundant Connection, Kruskal's algorithm |
| **Trie (prefix tree)** | String prefix problems | Autocomplete, Implement Trie |
| **Graph patterns** | Graph problems generally | Detect Cycle in Graph |
| **Linked List Reversal** | Reverse pointers | Reverse List, palindrome list |
| **In-Place Linked List Manipulation** | Modify links, no extra structures | Partition List, reordering |

### Worked examples

**Two pointers — pair sum in a sorted array:**
```java
static boolean pairSum(int[] arr, int target) {
    int l = 0, r = arr.length - 1;
    while (l < r) {
        int sum = arr[l] + arr[r];
        if (sum == target) return true;
        else if (sum < target) l++;
        else r--;
    }
    return false;
}
```

**Sliding window — maximum sum of k consecutive elements:**
```java
static int maxSum(int[] arr, int k) {
    int n = arr.length, sum = 0;
    for (int i = 0; i < k; i++) sum += arr[i];
    int max = sum;
    for (int i = k; i < n; i++) {
        sum = sum - arr[i - k] + arr[i];
        max = Math.max(max, sum);
    }
    return max;
}
```

**Hashing — Two Sum:**
```java
int[] arr = {2, 7, 11, 15};
int target = 9;
Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < arr.length; i++) {
    int rem = target - arr[i];
    if (map.containsKey(rem)) {
        System.out.println(map.get(rem) + " " + i);   // 0 1
    }
    map.put(arr[i], i);
}
```

**1D dynamic programming — Climbing Stairs:**
```
dp[n] = dp[n-1] + dp[n-2]
n     : 0  1  2  3  4  5
dp[n] : 1  1  2  3  5  8
Time O(n), space O(n) - can be optimised to O(1)
```

**Quick sort skeleton:**
```java
static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

## 23.5 Practice programs (beginner set)

1. Print Hello World
2. Sum of two numbers
3. Factorial of a number
4. Even or odd
5. Prime number check
6. Reverse a number
7. Fibonacci series
8. Sum of digits
9. Armstrong number
10. Count digits in a number

## 23.6 Pattern printing

Practice star, number and character patterns — right-angled triangle, inverted triangle, pyramid, diamond. They train loop control and are asked in interviews.

```java
// Right-angled triangle
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) System.out.print("* ");
    System.out.println();
}
```

## 23.7 Ten problems worth solving this week

1. Reverse a string without using a library function
2. Find the second largest element in an array
3. Check whether a string is a palindrome
4. Find the missing number in an array
5. Remove duplicates from an array
6. Merge two sorted arrays
7. Find the intersection of two arrays
8. Check if a linked list is a palindrome
9. Implement a Stack using an array or a linked list
10. Serialize and deserialize a binary tree

## 23.8 The problem-solving method

1. **Understand the problem** properly — restate it in your own words
2. **Choose the logic and data structure**
3. **Write clean, simple, working code**
4. **Run sample and edge cases**
5. **Optimise** time and space complexity
6. Analyse the final complexity out loud

Practice platforms: LeetCode, GeeksforGeeks, HackerRank, CodeChef, Codeforces.

---

# Part 24 — Backend Development Fundamentals

## 24.1 What is backend development?

Backend development is the part of software that runs **behind the scenes** — handling data, logic, security and communication — so that the part users see (the frontend) can work correctly.

**The restaurant analogy.** The frontend is the dining area: the menu, the tables, the waiter taking the order. The backend is the **kitchen**, where the food is prepared, ingredients are stored, and the real work happens. The customer never sees the kitchen, but without it nothing arrives at the table.

When you click "Login" or "Buy Now", that click goes to the backend. The backend checks your password, looks up your data, processes your payment, and sends back a result — all in a fraction of a second.

Without a backend an app is like a shop with a beautiful storefront but no warehouse, no staff and no cash register. The frontend can look amazing but it cannot remember anything, calculate anything securely, or talk to other systems on its own.

## 24.2 The three jobs of every backend

1. **Store and manage data.** User accounts, orders, messages, posts — all of it lives in a database the backend reads from and writes to.
2. **Apply business logic.** Rules like "a user cannot order more items than are in stock" or "only logged-in users can post a comment" are enforced entirely by the backend.
3. **Communicate securely.** The backend receives requests from the frontend, validates them, checks permissions and sends back the correct response — safely and quickly, every time.

Almost every backend interview, however advanced, is really testing how well you understand these three jobs.

## 24.3 Frontend vs backend

| Frontend | Backend |
|---|---|
| What the user sees and clicks on | What runs on the server, invisible to the user |
| Layout, colours, buttons, animations | Business logic, data processing, validation |
| Runs entirely in the user's browser | Runs on a remote server, away from the user |
| **Cannot be fully trusted** (the user can change it) | **The source of truth** — always trusted |
| Focuses on user experience and design | Focuses on data integrity, speed and security |
| Fails visibly — the user sees a broken page | Fails silently — the user just sees an error message |

| Frontend technologies | Backend technologies |
|---|---|
| HTML — structure | Python, Java, Node.js, Go, PHP — server logic |
| CSS — styling | PostgreSQL, MySQL, MongoDB — data storage |
| JavaScript — interactivity | REST or GraphQL — communication format |
| React, Vue, Angular | Django, Express, **Spring** |

**Rule of thumb:** if you can see it, touch it or click it on the screen, that is frontend. If it happens somewhere you cannot see, involves checking a password, saving information permanently, or talking to another system, that is backend.

## 24.4 Servers and hosting

A **server** is simply a computer that is always turned on, always connected to the internet, and always listening for incoming requests. It is the same kind of hardware as your laptop, just configured to run constantly and serve many visitors at once.

**Hosting** means renting space on someone else's server (or network of servers) so your application can run online 24 hours a day without owning hardware. Providers: AWS, Google Cloud, Microsoft Azure, and simpler platforms like Render or Vercel.

| Term | Meaning |
|---|---|
| **Cloud server** | A virtual server on shared physical hardware, rented by the minute or hour |
| **Load balancer** | Distributes incoming traffic across multiple servers so no single one is overwhelmed |
| **Uptime** | The percentage of time a server is running and available |
| **Deployment** | Putting your application's code onto a live server |

## 24.5 Databases — SQL vs NoSQL

A **database** is an organised system for storing data permanently, so it survives a server restart. Without one, every user account and every order would disappear the moment the program stopped.

**SQL (relational)** databases store data in **tables with rows and columns**, like a spreadsheet. Each table has a fixed structure, and tables link together through relationships. Examples: PostgreSQL, MySQL, SQLite, Oracle.

**NoSQL (non-relational)** databases store data in flexible formats, often as documents that look like JSON objects. Examples: MongoDB, Cassandra, Redis.

| SQL (Relational) | NoSQL (Non-Relational) |
|---|---|
| Tables with a fixed structure | Flexible documents |
| Strong relationships between tables | Data is often self-contained, fewer relationships |
| Best for structured, predictable data | Best for fast-changing or very large-scale data |
| ACID compliance for high-stakes transactions | Eventual consistency, easier horizontal scaling |
| Powerful for complex queries and joins | Schema-less, allows quicker iteration |
| PostgreSQL, MySQL, Oracle | MongoDB, Cassandra, Redis |

Other database types worth knowing: **in-memory** (Redis), **graph** (Neo4j), **time series**, and **spatial**.

You do not need to memorise every database — what interviewers want is a clear explanation of **why you would choose one over the other** for a given situation.

## 24.6 Authentication vs authorization

These sound similar but answer two completely different questions.

- **Authentication — "Who are you?"** Confirming a user's identity, usually with a username and password. Once confirmed, the system issues a **token** so it does not need the password on every request.
- **Authorization — "What are you allowed to do?"** This happens **after** authentication. A regular user may view their own orders; only an admin may view everyone's orders or delete a product.

**Analogy:** showing your ID card at the front desk is authentication. Whether that card opens the management floor is authorization.

| Method | How it works |
|---|---|
| **Session-based** | The server stores a session after login and gives the browser a session ID |
| **Token-based (JWT)** | The server gives a signed token after login; the client sends it with every request |
| **OAuth** | Lets users log in through another trusted service, like Google or GitHub |
| **API keys** | A simple key in a header or query string; used for server-to-server and public APIs |
| **Basic auth** | `Authorization: Basic base64(username:password)` — internal or legacy systems only, behind TLS |

## 24.7 The full request-response flow (traced through a login)

1. **User action.** The user types their email and password into the login form and clicks "Log In". The frontend collects the values.
2. **Request sent.** The frontend sends an HTTP request to the backend API, usually to `/api/login`.
3. **Server receives.** The backend routes the request to the code that handles logins.
4. **Database lookup.** The backend queries the database for that email and checks whether the submitted password matches the stored hash.
5. **Response sent back.** If correct, a success response plus an authentication token. If not, a clear error message.
6. **Frontend updates.** The frontend shows the dashboard on success, or an error message on failure.

Almost every backend interview question is really asking you to explain one part of this exact flow in more detail — what is checked, what could go wrong, or how to make a step faster or more secure.

## 24.8 Caching and performance

**Caching** means storing a copy of frequently requested data somewhere fast, so the system does not redo expensive work every time. It is like writing an answer on a sticky note instead of phoning your friend again.

| Use case | What gets cached |
|---|---|
| Popular product pages | Product details that rarely change |
| User session data | Login state, so the database is not hit on every click |
| API responses | Results of expensive calculations or external API calls |
| Database query results | Frequently repeated queries |

**Redis** is an extremely fast in-memory data store, the go-to caching tool. Because it stores data in memory rather than on disk, reading from Redis is far faster than querying a traditional database.

**Keeping the cache fresh:** the simple answer is to set an **expiration time (TTL)** so old data is automatically replaced. That bounds the worst case.

**Caching strategies**
1. **Read-Through** — the cache automatically fetches and caches missing data from the source
2. **Write-Through** — writes go to the cache and the database simultaneously; the write completes only when both succeed
3. **Write-Back** — writes go to the cache first, the source is updated later
4. **Cache-Aside** — the application manages retrieval and cache population itself (the most common pattern)

**Eviction policies**
1. **LRU (Least Recently Used)** — removes the item not accessed for the longest time
2. **LFU (Least Frequently Used)** — discards the lowest access frequency
3. **FIFO (First In, First Out)** — removes the oldest item
4. **TTL (Time To Live)** — removes items after a set expiry

## 24.9 Security basics every backend developer must know

1. **SQL injection** — an attacker inserts malicious SQL into an input field to manipulate the database. **Prevent with parameterized queries** (`PreparedStatement`), never by building SQL strings manually.
2. **Password hashing** — passwords must never be stored as plain text. Run them through a one-way hash (bcrypt, Argon2) so even the company cannot see the original.
3. **HTTPS** — encrypts data between browser and server so it cannot be read by anyone intercepting the connection.
4. **Input validation** — always check that user data is in the expected format before processing.
5. **Rate limiting** — restricts how many requests a user can make in a time window, preventing abuse and brute-force attacks.
6. **Cross-Site Scripting (XSS)** — malicious scripts injected into a webpage. Prevent by escaping user-generated content before displaying it.
7. **CSRF (Cross-Site Request Forgery)** — use anti-forgery tokens.
8. **Broken authentication** — use strong auth (JWT, OAuth2).
9. **Sensitive data exposure** — encrypt sensitive data at rest and in transit.
10. **Mass assignment** — validate and whitelist the fields a client is allowed to set.

**The one rule that covers most of it: never trust data coming from the user.** Every form field, URL parameter and uploaded file should be treated as potentially harmful until validated by the backend.

**Other practices:** use strong passwords and hashing, use short-lived tokens with refresh tokens, store secrets in environment variables, and keep dependencies and libraries updated.

## 24.10 Scalability

A system that works perfectly with 10 users but breaks with 10,000 is **not scalable**. Scalability means the system keeps responding quickly and reliably as usage grows — usually by adding resources rather than rewriting everything.

| Approach | Meaning |
|---|---|
| **Vertical scaling (scale up)** | Making a single server more powerful — more memory, faster processor. Simple, but there is a physical limit and it is a single point of failure |
| **Horizontal scaling (scale out)** | Adding more servers to share the load. Almost limitless, but brings distributed-systems complexity |

Key ideas for beginners:
- **Load balancing** — spread requests evenly across servers
- **Database indexing** — organise data so searches are fast, like the index at the back of a book
- **Caching** — avoid repeating expensive work
- **Asynchronous processing** — handle slow tasks in the background instead of making the user wait

You are not expected to design a system for millions of users in your first interview. What matters is that you think about "what happens if this grows".

## 24.11 Asynchronous programming

Synchronous behaviour is a barista who takes your order, then **stands and waits** while your coffee brews before serving the next customer. Asynchronous behaviour is a barista who takes your order, starts the machine, and immediately serves the next person while the coffee brews.

| Synchronous | Asynchronous |
|---|---|
| The server waits for each task to complete | The server starts a task and handles other work while waiting |
| Slow tasks block everything else | Slow tasks run in the background without blocking |
| Wastes server resources while waiting | Makes far better use of available resources |

You do not need complex async code to answer this well in an interview: simply explaining that async lets a server **handle many requests at once instead of one at a time** shows solid understanding.

## 24.12 Common backend tools

| Language | Commonly paired with |
|---|---|
| Java | **Spring Boot** |
| Python | Django, FastAPI, Flask |
| JavaScript / Node.js | Express, NestJS |
| Go | Gin, native net/http |
| PHP | Laravel |

| Database | Type | Best for |
|---|---|---|
| PostgreSQL / MySQL | Relational (SQL) | Structured data with clear relationships |
| MongoDB | Non-relational (NoSQL) | Flexible, fast-changing data |
| Redis | In-memory store | Caching and fast temporary data |
| SQLite | Relational (lightweight) | Small apps, local development, testing |

## 24.13 Architecture patterns

**Monolithic architecture** — a single unified application where all features (user accounts, payments, notifications) live in one codebase and run as one program. Most small-to-medium applications start here because it is simpler to build, test and deploy.

**Microservices architecture** — the application is broken into many small, independent services, each responsible for one business capability. Each can be developed, deployed and scaled independently, and each has its own database to ensure loose coupling.

| Monolith | Microservices |
|---|---|
| Simple to build and deploy initially | Complex to set up, but scales better for large teams |
| One codebase | Many small, independent codebases |
| Easier for small teams and early-stage products | Better for large companies with many teams |
| A bug can affect the whole system | A failure in one service does not always affect others |

There is no universally better choice. Most companies **start as a monolith** and move to microservices only once the team and product justify the added complexity.

**Other architectural patterns**
- **Client-Server** — the classic split: clients send requests and display results, servers process requests and manage resources
- **Serverless** — the cloud provider manages all infrastructure and scaling; you deploy functions triggered by events and are billed only for compute time. Ideal for event-driven work like file processing
- **Event-Driven (EDA)** — components are decoupled and communicate through events handled asynchronously; events can be processed in parallel by multiple consumers
- **Peer-to-Peer (P2P)** — decentralised, every node is both client and server; no central point of failure

## 24.14 Middleware

Middleware is code that runs **between receiving a request and sending a response**. Common uses: checking authentication, logging requests, validating input, rate limiting, and error handling.

```
Request -> Middleware -> Controller -> Response
```

Example: every request to `/api/orders` first verifies the JWT, logs the request, validates the input, and only then processes it.

## 24.15 Interview preparation for backend roles

**What interviewers actually look for**
- Clear communication — can you explain a concept in simple words, not just jargon?
- Problem-solving approach — do you ask clarifying questions before jumping to a solution?
- Real understanding, not memorised answers — can you apply a concept to an unfamiliar scenario?
- Awareness of trade-offs — every technical choice has pros and cons
- Curiosity and willingness to learn

**Common beginner mistakes to avoid**
- Memorising answers word-for-word — follow-up questions will expose the gaps
- Staying silent when stuck — always explain your thinking out loud
- Ignoring the basics to chase "advanced" topics too early
- Not asking questions back — a good interview is a conversation
- Overcomplicating simple answers
- Not practising out loud

**The bottom line:** the goal of a beginner backend interview is not to prove you know everything, but to prove you understand the fundamentals well enough to learn the rest on the job.

---

# Part 25 — REST APIs and HTTP in Depth

## 25.1 What is an API?

An **API (Application Programming Interface)** is a set of rules and protocols that allows different software applications to communicate with each other.

**The restaurant analogy again.** You do not walk into the kitchen yourself — you give your order to a waiter, who takes it to the kitchen and brings back the food. The **waiter is the API**: a messenger that carries your request to the system that can fulfil it, and brings back the result.

A weather app does not calculate the weather itself; it calls a weather API, sends your location, and receives the forecast.

## 25.2 What is an endpoint?

An **endpoint** is a specific address on the backend that performs one particular job. `/api/login` handles logging in; `/api/products` fetches the product list. A backend application is essentially a collection of endpoints, each doing one clear task.

```
Banking application:
GET  /api/accounts          -> List all accounts
GET  /api/accounts/{id}     -> Get a specific account
POST /api/transfers         -> Initiate a money transfer
GET  /api/transactions      -> View transaction history
```

## 25.3 REST

**REST (Representational State Transfer)** is an architectural style for designing networked applications that use HTTP methods to perform operations on resources.

### The six REST constraints

1. **Client-Server** — separation of concerns between client and server
2. **Stateless** — each request from the client must contain all the information needed to process it; the server stores **no** client state between requests
3. **Cacheable** — responses must define themselves as cacheable or non-cacheable
4. **Uniform Interface** — a consistent way for the client to interact with the server (resources, methods, representations)
5. **Layered System** — the client cannot tell whether it is connected directly to the end server or to an intermediary
6. **Code on Demand** (optional) — the server can extend client functionality by sending executable code

### Resource-based architecture

Everything in REST is a **resource**, and it has one or more **representations**:

```
Resources           Representations
/users              JSON
/users/1            XML
/products/{id}      Plain text
/orders/100         HTML
```

**Why REST is widely used:** it uses standard HTTP methods, supports multiple data formats (JSON, XML), works well with mobile and web applications, and is easy to test and maintain.

## 25.4 HTTP methods

| Method | Purpose | Idempotent | Safe | Example | Typical use |
|---|---|---|---|---|---|
| **GET** | Retrieve data (read) | Yes | Yes | `GET /users` | Get all users, get user by id |
| **POST** | Create a new resource | No | No | `POST /users` | Create a new user, submit form data |
| **PUT** | Update or **replace** an existing resource entirely | Yes | No | `PUT /users/10` | Full update |
| **PATCH** | **Partially** update an existing resource | Yes | No | `PATCH /users/10` | Change a single field |
| **DELETE** | Delete a resource | Yes | No | `DELETE /users/10` | Delete a user |
| **OPTIONS** | Ask what methods are supported | Yes | Yes | `OPTIONS /users` | CORS preflight |
| **HEAD** | Like GET but headers only, no body | Yes | Yes | `HEAD /users/10` | Check existence, get metadata |

- **Idempotent methods** — calling them multiple times produces the same result with no additional side effects: **GET, PUT, DELETE, HEAD, OPTIONS**. POST is **not** idempotent (it creates a new resource each time).
- **Safe methods** — methods that do not change server state: **GET, HEAD, OPTIONS**.
- **PUT vs PATCH** — PUT replaces the entire resource; PATCH updates it partially.

**GET vs POST**

| GET | POST |
|---|---|
| Retrieves data | Submits data |
| Parameters visible in the URL | Data in the request body (hidden) |
| Bookmarkable | Not bookmarkable |
| Limited data capacity | Larger data capacity |
| `amazon.com/search?q=laptop` | Submitting a login form |

## 25.5 HTTP status codes

The simple rule: **2xx = success, 3xx = redirect, 4xx = the client made a mistake, 5xx = the server made a mistake.**

**2xx — Success**

| Code | Meaning |
|---|---|
| 200 OK | The request worked exactly as expected |
| 201 Created | A new resource was created (return a `Location` header) |
| 204 No Content | Success, but nothing to return (typical for DELETE) |

**3xx — Redirection**

| Code | Meaning |
|---|---|
| 301 Moved Permanently | The resource moved to another URL |
| 304 Not Modified | Cached version is still valid |
| 307 Temporary Redirect | Temporary move |

**4xx — Client errors**

| Code | Meaning |
|---|---|
| 400 Bad Request | The server cannot process the request — invalid data or parameters |
| 401 Unauthorized | Authentication required and missing or invalid |
| 403 Forbidden | Authenticated, but not allowed to access this |
| 404 Not Found | The resource does not exist |
| 405 Method Not Allowed | The method is not supported by this resource |
| 409 Conflict | Conflict with the current state — a duplicate or version clash |
| 422 Unprocessable Entity | The request is well-formed but semantically wrong |
| 429 Too Many Requests | Rate limit exceeded |

**5xx — Server errors**

| Code | Meaning |
|---|---|
| 500 Internal Server Error | Something went wrong on the server |
| 502 Bad Gateway | Invalid response from an upstream server |
| 503 Service Unavailable | Server overloaded or under maintenance |
| 504 Gateway Timeout | Upstream server timed out |
| 505 HTTP Version Not Supported | Version not supported |

**Codes people get wrong:** 400 (malformed) vs 422 (valid but rejected); 401 (not logged in) vs 403 (logged in but not allowed).

## 25.6 Anatomy of a request

Every REST communication is a request from the client and a response from the server.

1. **HTTP method** — the operation
2. **URL / endpoint** — the resource address, e.g. `POST /api/users`
3. **Query parameters** — optional, after `?`, for filtering, sorting and pagination: `/api/users?page=2&limit=10`
4. **Path parameters** — values inside the URL path identifying a resource: `/api/users/10`
5. **Headers** — metadata about the request
6. **Body (payload)** — the data sent to the server (in POST, PUT, PATCH), usually JSON

```http
POST /api/users HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Accept: application/json
Authorization: Bearer <token>

{
  "name": "John Doe",
  "email": "john@email.com",
  "age": 25
}
```

**Query vs path parameters**

| Feature | Path parameter | Query parameter |
|---|---|---|
| Purpose | Identify a resource | Filter or modify the response |
| Mandatory | Yes | No |
| Position | Part of the URL path | After `?` |
| Example | `/users/10` | `/users?role=admin` |

## 25.7 Headers

Headers are key-value pairs carrying **metadata**. They do not contain the actual data, but tell the server how to process it.

| Header | Purpose |
|---|---|
| `Authorization` | Who the user is — `Bearer <token>` |
| `Content-Type` | The format of the **request** body — `application/json`, `multipart/form-data` |
| `Accept` | The format the client wants **back** |
| `Cache-Control` | Caching behaviour |

Remember the pair: **`Accept` = response format, `Content-Type` = request format.** If the server receives JSON but `Content-Type` is missing or wrong, the request may fail.

## 25.8 A sample response

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "email": "john@email.com",
  "age": 25,
  "isActive": true,
  "createdAt": "2024-05-12T10:30:00Z"
}
```

## 25.9 JSON

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format using key-value pairs. It is widely used in APIs because it is easy for humans to read and machines to parse.

```json
{
  "firstName": "Sarah",
  "lastName": "Chen",
  "email": "sarah@email.com",
  "address": {
    "street": "123 Main St",
    "city": "San Francisco",
    "zipcode": "94107"
  }
}
```

## 25.10 REST API best practices (ten rules)

1. **Use nouns, not verbs, in URIs.** `/users` not `/getUsers`; `/users/10` not `/deleteUser/10`.
2. **Use plural nouns.** `/users` for the collection, `/users/10` for a specific one, `/orders`, `/products`.
3. **Use the proper HTTP method** for each operation.
4. **Use correct status codes** so clients can handle responses correctly.
5. **Keep responses in a consistent structure** so clients can parse them predictably:
   ```json
   { "success": true, "data": { "id": 123, "name": "John Doe" }, "message": "User retrieved successfully" }
   ```
6. **Paginate large datasets.** `GET /users?page=2&limit=10`. Return metadata: `{"page": 2, "total": 150, "totalPages": 15}`. Offset-based is simple; cursor-based is better for very large datasets.
7. **Support filtering, sorting and searching** through query parameters: `?status=active&role=admin`, `?sort=name&order=asc`, `?search=john`.
8. **Version your API** so breaking changes do not break existing clients: `/api/v1/users`, `/api/v2/users`.
9. **Secure it** — OAuth 2.0 or JWT for authentication, role permissions for authorization, HTTPS everywhere, and never trust client-side data.
10. **Validate all inputs and log/monitor everything** — method, URL, request and response time, status code, errors and exceptions.

## 25.11 API security

**Authentication methods**
- **JWT (Bearer token)** — the token contains user claims and is digitally signed; the client sends it in the `Authorization: Bearer <token>` header. Stateless — no need to store the session on the server.
- **API key** — a simple key passed in a header or query string; used for server-to-server communication.
- **OAuth 2.0 / OIDC** — third-party or social login and SSO.
- **Basic auth** — internal tools behind TLS only.

**JWT structure — three parts separated by dots:**
```
Header.Payload.Signature
```
- **Header** — token type and algorithm
- **Payload** — user data (claims), e.g. `{"userId": 123, "role": "admin", "exp": 1700000000}`
- **Signature** — verifies token integrity

**The JWT login flow:**
1. User sends credentials (`POST /login`)
2. Server validates them
3. Server generates a JWT
4. The token is returned to the client
5. The client stores it (localStorage or a cookie)
6. The token is sent with every subsequent request
7. The server verifies the signature and expiry

**The downside of JWT:** a token is valid until it expires — you cannot un-issue it. Keep access tokens short-lived (a few minutes) and pair them with a **refresh token** you can revoke server-side. For immediate logout you need a deny-list, which quietly reintroduces state.

**Never put anything sensitive in the JWT payload — it is base64, not encryption. Anyone can read it.**

**HTTPS (SSL/TLS)** — always use it. It encrypts data in transit and prevents eavesdropping and man-in-the-middle attacks.

**CORS (Cross-Origin Resource Sharing)** — a **browser-side** security feature that lets a server specify which domains may access its resources.
```
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

**Same-origin policy** — a browser rule preventing a page from accessing data from another origin. An origin is **protocol + domain + port**.

**Rate limiting** — limit the number of requests per client (for example 100 requests per minute) to prevent abuse and brute-force attacks. Return `429 Too Many Requests`.

## 25.12 Advanced API concepts

| Concept | Meaning |
|---|---|
| **Idempotency** | Performing the operation multiple times produces the same result. Use an idempotency key on payments so a network retry does not charge twice |
| **HATEOAS** | Responses include links to related actions: `"links": {"track": "/orders/123/track", "cancel": "/orders/123/cancel"}` |
| **API Gateway** | A single entry point managing requests to multiple backend services — authentication, rate limiting, routing, logging |
| **Webhook** | The **server pushes** data to another system when an event occurs (the reverse of an API call, where the client requests) |
| **Event-driven API** | Communication triggered by events (order placed, payment completed) rather than direct requests |
| **Message queue** | Stores messages for asynchronous processing — improves scalability, prevents blocking, handles traffic spikes. Tools: RabbitMQ, Kafka, AWS SQS, Redis Queue |
| **Retry mechanism** | Automatically retrying failed requests |
| **Circuit breaker** | Stops sending requests to a failing service to prevent system collapse; falls back instead |
| **Throttling** | Temporary control over request rates when server load is high |
| **API latency** | Time from request sent to response received. Reduce with caching, DB indexing, CDN and async processing |
| **Distributed tracing** | Tracking one request across many services — essential for microservices debugging |
| **Blue-green deployment** | Deploy the new version alongside the old, switch traffic after testing — zero downtime |
| **Canary release** | Gradually release a new version to a small percentage of users to detect bugs before full rollout |
| **API sandbox** | A safe test environment (PayPal Sandbox, Stripe Test Mode) |
| **Schema registry** | A central repository for API schemas, used in microservices and event-driven systems |
| **API-first approach** | Design the API before building the frontend or backend — better collaboration, clear contracts, parallel development |

## 25.13 REST vs SOAP vs GraphQL vs RPC

| Feature | REST | SOAP |
|---|---|---|
| Protocol | HTTP | XML-based, can use HTTP, SMTP, etc. |
| Format | JSON, XML, plain text | XML only |
| Speed | Fast | Slower |
| Complexity | Simple | Complex |
| State | Stateless | Can be stateful |
| Usage | Modern web and mobile apps | Legacy and enterprise systems (banking) |

**WSDL** describes a SOAP service's structure, operations and endpoints. WSDL is the contract; the API is the implementation.

**GraphQL** is a query language that lets clients request **exactly the data they need**, solving REST's over-fetching and under-fetching problem.
```graphql
{ user(id: 1) { name email } }
```

**RPC (Remote Procedure Call)** is action-based rather than resource-based, can use various protocols, and often uses custom methods and data formats. gRPC is efficient for inter-service communication in microservices.

**When not to use REST:** when the call is fire-and-forget or fans out to many consumers — that is a Kafka event. When clients need very different shapes of the same data — GraphQL fits better.

## 25.14 API testing and documentation

**Tools:** Postman (send requests, view responses, add headers and tokens), Swagger UI (interactive testing), curl (command line), Insomnia, Thunder Client (VS Code extension).

**Postman workflow:** create the request -> set the method and URL -> add headers and body -> send -> validate the response -> write tests.

**Automated tests in Postman:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

**Swagger / OpenAPI** is the standard specification for documenting REST APIs in a readable, interactive format. A frontend developer can open Swagger UI, see all endpoints, test them without Postman, and understand request/response formats. Benefits: interactive testing, auto-generated docs and client SDK generation.

**Other testing concepts:** API mocking (simulating responses so the frontend can work before the backend is ready), contract testing (ensuring provider and consumer follow the same contract), unit tests, integration tests and load tests. Automation tools: Jest, Mocha, Newman, RestAssured.

---

# Part 26 — Spring and Spring Boot

## 26.1 What is Spring Boot?

**Spring Boot** is a Java-based framework built on top of the Spring Framework that simplifies the development of stand-alone, production-ready applications. It is open source, developed by the Pivotal team, and is used to create microservices.

It **minimises configuration** by providing auto-configuration, starter dependencies and embedded servers, so developers write business logic rather than configuration.

**Spring Boot = convention over configuration.**

## 26.2 Features of Spring Boot

| Feature | What it does |
|---|---|
| **Auto Configuration** | Automatically configures Spring beans based on the libraries on the classpath |
| **Starter Dependencies** | Predefined dependency bundles that simplify Maven and Gradle configuration |
| **Embedded Servers** | Built-in Tomcat, Jetty and Undertow — no external deployment needed |
| **Spring Boot Actuator** | Health checks, metrics, monitoring and application information |
| **Spring Boot CLI** | Create and run Spring applications from the command line |
| **Externalized Configuration** | Configure via properties, YAML, environment variables and command-line arguments |
| **DevTools** | Automatic restart, LiveReload and enhanced developer productivity |

**Advantages:** embedded web servers, simplified dependency management, rapid development with auto-configuration, production-ready monitoring via Actuator, easy integration with Spring projects and third-party libraries, and less boilerplate code.

## 26.3 Spring vs Spring Boot

| Feature | Spring Framework | Spring Boot |
|---|---|---|
| Configuration | Mostly manual | Auto configuration |
| Dependency management | Manual | Starter dependencies |
| Embedded server | Not provided | Tomcat, Jetty, Undertow |
| Deployment | WAR file on an external server | Executable JAR or WAR |
| Boilerplate code | More | Less |
| Development speed | Slower | Faster |
| Production features | Requires extra setup | Built-in Actuator |
| Microservices support | Possible | Excellent |

Spring Boot is not a replacement for Spring — it is Spring with sensible defaults.

## 26.4 IoC and Dependency Injection

**IoC (Inversion of Control)** is a design principle where the control of object creation, configuration and lifecycle is **transferred from your code to the Spring container**. You stop calling `new`.

**DI (Dependency Injection)** is the *implementation technique*: the container injects the dependencies a class declares.

**IoC is the idea; DI is the mechanism. All DI is IoC, but not all IoC is DI.**

```
Without DI:  class A -> new B()          (tight coupling)
With DI:     IoC Container -> A(B b)     (injected)
```

**Why it matters**
- Swap implementations without touching class A
- Mock dependencies in unit tests instantly
- One bean reused everywhere (singleton by default)
- Removes hard-coded dependencies, makes the application loosely coupled
- Centralised control over configuration and lifecycle
- Supports AOP, transactions and caching

### The three types of injection

| Type | Verdict |
|---|---|
| **Constructor injection** | **Use this.** Immutable, testable, fails fast, ensures mandatory dependencies are set at creation. Cannot be changed after creation |
| **Setter injection** | Only for genuinely **optional** dependencies. Can be changed after object creation |
| **Field injection (`@Autowired` on a field)** | **Avoid.** Hides dependencies, blocks `final` fields, hard to test |

```java
// Constructor injection - preferred
@Autowired
public UserService(UserRepository repo) { this.repo = repo; }

// Setter injection - optional dependencies
@Autowired
public void setRepo(UserRepository repo) { this.repo = repo; }
```

**Say "constructor injection" in the interview, and say why.**

## 26.5 Auto-configuration

At startup, Spring Boot reads a list of auto-configuration classes shipped in the starters, then evaluates **conditions** on each one. If the required class is on the classpath and you have **not** defined that bean yourself, it creates it.

```
@SpringBootApplication -> AutoConfiguration.imports -> @Conditional... -> Beans
(Config + EnableAutoConfig + Scan)   candidate list    OnClass, OnMissingBean   Tomcat, DataSource, JPA
```

**Your own `@Bean` always wins** — auto-config backs off when you define one.

**The three conditions**

| Annotation | Meaning |
|---|---|
| `@ConditionalOnClass` | A class is on the classpath |
| `@ConditionalOnMissingBean` | You did **not** define that bean |
| `@ConditionalOnProperty` | A property has a given value |

**Examples:**
- If `spring-boot-starter-web` is on the classpath, Tomcat and Spring MVC are auto-configured
- If `spring-boot-starter-data-jpa` is present, `DataSource`, `EntityManagerFactory` and JPA are auto-configured

**Debugging:** run with `--debug` to print the **condition evaluation report**, which shows exactly what matched and why.

**Disabling auto-configuration** (three ways):
1. `@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})`
2. `spring.autoconfigure.exclude=...` in the properties file
3. `@EnableAutoConfiguration(exclude = ...)` on a `@Configuration` class

Disable only when you need full control or want to replace default behaviour.

## 26.6 Starter dependencies

Starters are preconfigured dependency descriptors that include commonly used libraries for a specific job.

| Starter | Purpose |
|---|---|
| `spring-boot-starter-web` | Web and REST applications |
| `spring-boot-starter-data-jpa` | Database access using JPA |
| `spring-boot-starter-security` | Authentication and authorization |
| `spring-boot-starter-test` | Unit and integration testing |
| `spring-boot-starter-thymeleaf` | Thymeleaf template engine |
| `spring-boot-starter-validation` | Bean validation |
| `spring-boot-starter-actuator` | Monitoring and health checks |

Starters save time, reduce boilerplate and ensure version compatibility. But more starters means more dependencies, higher memory use and slower startup — only add what you need.

## 26.7 How a Spring Boot application starts

1. The `main()` method is the entry point.
2. It calls `SpringApplication.run()`, which bootstraps the application.
3. Spring Boot starts the **embedded server** (Tomcat/Jetty/Undertow).
4. The **application context** is created and all beans are initialised.
5. **Dependency injection** is performed and the application is wired.
6. The application is ready to handle incoming requests.

```java
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
```

## 26.8 `@SpringBootApplication`

A single annotation that combines three:

| Annotation | Purpose |
|---|---|
| `@Configuration` | Marks the class as a source of bean definitions |
| `@EnableAutoConfiguration` | Enables Spring Boot auto-configuration |
| `@ComponentScan` | Scans the current package and sub-packages for components |

## 26.9 The internal working — layered architecture

```
Client -> Controller -> Service -> Repository -> Database
          (@RestController)  (@Service)  (@Repository)
                          <- Response (JSON / XML / View)
```

1. The client sends an HTTP request (GET, POST, PUT, DELETE)
2. The request is mapped to the appropriate controller method
3. The controller forwards it to the **service** layer
4. The service executes business logic
5. The service uses the **repository** (JPA/Hibernate) for database operations
6. The repository talks to the database and returns the result

**Layer responsibilities**

| Layer | Responsibility |
|---|---|
| **Controller** | HTTP in and out, validation, status codes. Stays thin — no business logic |
| **Service** | Business rules, `@Transactional` |
| **Repository** | Queries only |
| **DTO** | What leaves the application — **never** the entity |

Spring Boot follows a layered architecture for separation of concerns, easier debugging, and scalable design.

## 26.10 Spring MVC request flow

`DispatcherServlet` is the **front controller** — it routes, converts and handles errors.

```
Client HTTP -> DispatcherServlet -> HandlerMapping -> Controller (@GetMapping)
            -> Service -> Repository -> DB
            -> MessageConverter (Jackson -> JSON) -> Response
```

- **Filters** run before the servlet.
- **Interceptors** run around the handler.
- `@ControllerAdvice` centralises error handling.
- The same pipeline serves both MVC and REST.

**A common trap:** returning your JPA entity straight from the controller leaks the database schema and triggers lazy-loading errors. **Map to a DTO.**

## 26.11 The essential annotations

### Stereotypes

| Annotation | Purpose | Layer |
|---|---|---|
| `@Component` | A generic Spring-managed bean | Any |
| `@Service` | Business logic | Service |
| `@Repository` | Data access. **Also translates database exceptions into Spring's `DataAccessException`** | Persistence |
| `@Controller` | Handles web requests, returns views (HTML/Thymeleaf) | Web |
| `@RestController` | `@Controller` + `@ResponseBody` — returns JSON/XML directly | Web |
| `@Configuration` | A class containing `@Bean` methods |  |

`@Service`, `@Repository` and `@Controller` are **specializations of `@Component`** with clearer intent and better readability. Functionally almost identical — except `@Repository`, which adds real behaviour (exception translation).

Prefer the specific annotation over plain `@Component` for readability and role clarity.

**Gotcha:** `@Configuration` is proxied with CGLIB, plain `@Component` is not — calling one `@Bean` method from another only stays a singleton inside `@Configuration`.

### Mapping annotations

| Annotation | Purpose |
|---|---|
| `@RequestMapping` | Maps requests to a handler method or class; works at class or method level; supports all HTTP methods |
| `@GetMapping` | Handles GET (fetch data) |
| `@PostMapping` | Handles POST (create data) |
| `@PutMapping` | Handles PUT (update data) |
| `@DeleteMapping` | Handles DELETE |
| `@PatchMapping` | Handles PATCH |

```java
@RestController
@RequestMapping("/api/products")
public class ProductController {

    @GetMapping("/all")
    public List<Product> getAll() { ... }

    @PostMapping
    public Product create(@RequestBody Product p) { ... }
}
```

### Parameter binding

| Annotation | Purpose | Example |
|---|---|---|
| `@PathVariable` | Extracts a value from the URI template | `GET /users/101` -> `id = 101` |
| `@RequestParam` | Extracts query parameters from the URL | `/search?name=mobile&page=1` |
| `@RequestBody` | Binds the JSON request body to a Java object | POST, PUT, PATCH |
| `@Valid` | Triggers bean validation on the bound object |  |

```java
@GetMapping("/users/{id}")
public ResponseEntity<User> getUser(@PathVariable Long id) {
    return ResponseEntity.ok(userService.findById(id));
}

@GetMapping("/search")
public List<Product> search(@RequestParam String name,
                            @RequestParam(defaultValue = "0") int page) { ... }

@PostMapping("/users")
public ResponseEntity<User> createUser(@RequestBody @Valid User user) {
    User saved = userService.save(user);
    return ResponseEntity.status(HttpStatus.CREATED).body(saved);
}
```

- The `{ }` name and the parameter name must match, or use `@PathVariable("name")`.
- Use `required = false` or `defaultValue` for optional query parameters.
- The request body is converted using an `HttpMessageConverter`; the `Content-Type` should be `application/json`.

### Injection and configuration

| Annotation | Purpose |
|---|---|
| `@Autowired` | Automatic dependency injection, **by type** |
| `@Qualifier` | Resolves ambiguity when multiple beans of the same type exist |
| `@Primary` | Marks one bean as the default choice |
| `@Value` | Injects a value from properties, environment variables or a SpEL expression |
| `@Bean` | Declares a bean explicitly inside a `@Configuration` class |
| `@ConfigurationProperties` | Binds a whole group of properties to a typed class |
| `@Profile` | Activates a bean only under a given profile |

```java
@Autowired
private UserService userService;          // by type

@Autowired
@Qualifier("smsService")
private MessageService messageService;    // pick a specific bean by name

@Value("${server.port}")
private int port;

@Value("${app.name:MyApp}")               // with a default value
private String appName;
```

**`@Autowired` vs `@Resource`**

| | `@Autowired` | `@Resource` |
|---|---|---|
| Package | `org.springframework.beans.factory.annotation` | `jakarta.annotation` |
| Injects | By **type** (default) | By **name** (default) |
| Multiple beans | Must use `@Qualifier` | Matches by name |
| Used on | Fields, setters, constructors | Fields, setters |

**`@Primary` vs `@Qualifier`**

| | `@Primary` | `@Qualifier` |
|---|---|---|
| Resolves | Which bean is the default | Exactly which bean, by name |
| Where | Class level, on the bean definition | At the injection point |
| Use when | One clearly preferred bean exists | You need a specific one out of many |

**`@Bean` vs `@Component`**

| | `@Bean` | `@Component` |
|---|---|---|
| Level | Method level, inside `@Configuration` | Class level |
| How | You write the creation logic | Spring creates it via component scanning |
| Flexibility | More — you control creation manually | Less |
| Dependencies | Passed as method parameters | Injected with `@Autowired` |
| Use when | Fine-grained control, or you do not own the class (third-party objects) | You want Spring to manage your own class automatically |

## 26.12 Bean scopes

A bean scope defines the lifecycle and visibility of a bean in the container.

| Scope | Meaning | Use case |
|---|---|---|
| **singleton** | **Default.** One instance per Spring container | Most common |
| **prototype** | A new instance every time the bean is requested | When a fresh instance is required |
| **request** | A new instance per HTTP request | Web applications |
| **session** | A new instance per HTTP session | User-specific data in session |
| **application** | One instance per ServletContext | Application-wide objects |
| **websocket** | A new instance per WebSocket connection | WebSocket-specific data |

Singleton is the default; the rest are web-aware scopes.

## 26.13 Bean lifecycle

```
1. Instantiation  ->  2. Populate properties  ->  3. Initialization  ->  4. Bean in use  ->  5. Destruction
   (constructor)      (dependencies injected)     (@PostConstruct or        (available)      (@PreDestroy or
                                                   afterPropertiesSet())                       destroy())
```

The Spring IoC container manages the entire lifecycle. Initialization and destruction callbacks are optional, and the scope affects the lifecycle (singleton vs prototype).

## 26.14 Configuration — properties and YAML

`application.properties` (or `application.yml`) holds externalized configuration, stores environment-specific settings, and supports placeholders, profiles and command-line overrides — all without code changes.

```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=secret
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
management.endpoints.web.exposure.include=health,info
```

```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: secret
```

| Feature | `application.properties` | `application.yml` |
|---|---|---|
| Format | Key-value pairs | YAML, hierarchical |
| Readability | Less readable for complex data | More readable for nested data |
| Data types | Only String | String, List, Map, etc. |
| Structure | Flat | Hierarchical |
| Use case | Simple configuration | Complex configuration |

**Configuration source priority (high to low):**
1. Command-line arguments
2. Environment variables
3. `application-{profile}.yml` / `.properties`
4. `application.yml` / `.properties`
5. `@PropertySource` and random value sources
6. Default properties

**Profiles** let you switch between dev, test and prod without changing code.

## 26.15 Spring Data JPA and Hibernate

You declare an interface; Hibernate writes the SQL. No implementation class — Spring generates a proxy at startup.

```
@Entity User -> JpaRepository -> Hibernate -> JDBC -> DB
(maps to a table)  findByEmail(String)   JPQL -> SQL
```

```java
@Entity
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    // getters and setters
}

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByEmail(String email);
    List<User> findByNameContainingIgnoreCase(String name);
}
```

**Repository interfaces:** `CrudRepository` -> `PagingAndSortingRepository` -> `JpaRepository` (each adds more).

**What you get free:** CRUD, paging and sorting, derived queries from method names, `@Query` for custom JPQL or native SQL, query by example, and named queries.

**Derived query naming:** `findByFieldName`, `findByFieldOneAndFieldTwo`, `findByTitleContainingIgnoreCase` — Spring parses the method name and builds the query.

`@Repository` marks the data-access layer, acts as the bridge between the application and the database, and **automatically translates database exceptions into Spring's `DataAccessException` hierarchy**.

### The N+1 problem

You load a list of parents, then every access to a lazy child fires its **own** query — one query becomes N plus one.

| Symptom | Fix |
|---|---|
| 1 query + N per row | `JOIN FETCH` in `@Query` |
| `LazyInitializationException` | Fetch inside the transaction |
| Slow list endpoints | `@EntityGraph` or a projection |
| Cannot see the SQL | `spring.jpa.show-sql=true`, p6spy in dev |

**The trap:** `FetchType.EAGER` looks like the fix but drags the whole object graph on every single read. Use `JOIN FETCH`, not `EAGER`. And check the **generated SQL** rather than assuming.

## 26.16 Transactions and ACID

`@Transactional` wraps the method in a proxy: **commit on normal return, rollback on a runtime exception**.

```java
@Transactional
public void transfer(Long from, Long to, BigDecimal amount) {
    debit(from, amount);
    credit(to, amount);
    writeLedger(from, to, amount);
}
```

**ACID in one line each**
- **Atomic** — all steps land or none do
- **Consistent** — constraints hold before and after
- **Isolated** — concurrent transactions do not see each other's mess
- **Durable** — once committed, it survives a crash

**Propagation**

| Value | Behaviour |
|---|---|
| `REQUIRED` | Join an existing transaction, else start one (**default**) |
| `REQUIRES_NEW` | Suspend the caller's transaction, run independently |
| `NESTED` | Savepoint — partial rollback possible |
| `MANDATORY` | Throw if no transaction is already running |

**Why did `@Transactional` not roll back?** Usually one of three reasons:
1. The exception was **checked** and you did not set `rollbackFor` — checked exceptions do **not** roll back by default
2. The method was called **from inside the same class**, so the proxy was bypassed (**self-invocation** — the most common cause)
3. The method was not `public`

**Across microservices there is no distributed rollback.** You need a **Saga** with compensating actions, not `@Transactional`.

## 26.17 Spring Security and JWT

Log in once, carry a signed token, prove yourself on every request.

```
POST /auth/login -> AuthenticationManager (verify + BCrypt) -> Signed JWT
Authorization: Bearer ... -> JWT filter (validate signature + expiry) -> SecurityContext -> @PreAuthorize checks role
```

**No server session — the token carries the identity.**

**Why it matters:** it scales horizontally (any instance can verify the token), works cleanly across microservices, and BCrypt hashes passwords with a per-user salt. Spring Security 7 uses a lambda DSL with no adapter class.

**Pick your scheme**

| Scheme | Best for |
|---|---|
| JWT | Stateless APIs, service-to-service |
| OAuth2 / OIDC | Third-party or social login, SSO |
| Session cookie | Server-rendered apps, easy revocation |
| Basic | Internal tools behind TLS only |

**Security building blocks in Spring:** `AuthenticationManager`, `UserDetails` and `UserDetailsService`, `PasswordEncoder` (BCrypt), the security `FilterChain`, path-based authorization, `@Secured`, `@PreAuthorize`, JSR-250 annotations, role inheritance, and CORS configuration.

## 26.18 Caching with Redis

The fastest query is the one you never run. Cache at the **service** layer, key it well, and always set a TTL.

```
Service call -> @Cacheable -> HIT: return from Redis
                           -> MISS: query DB, store, return
```

Add `@EnableCaching` on a configuration class.

| Annotation | Behaviour |
|---|---|
| `@Cacheable` | Skip the method if the key is already cached |
| `@CachePut` | Always run, then refresh the entry |
| `@CacheEvict` | Remove the entry — use on delete and update |

**Good candidates:** read-heavy and rarely changing data (catalogues, config), expensive joins or aggregations, session and rate-limit counters. **Not** data that must be exact to the millisecond.

**Keeping the cache fresh:** every entry gets a TTL so the worst case is bounded. On writes, evict or update the key in the same flow as the database write. For data where a few seconds of staleness is fine, a **short TTL** is far easier to reason about than complex invalidation.

**Gotcha:** `@Cacheable` on a method called from inside the same class does nothing — the proxy is bypassed, the same trap as `@Transactional`.

## 26.19 Kafka and async messaging

Publish a fact. Whoever cares consumes it, at their own pace.

```
booking-service (KafkaTemplate.send()) -> topic: booking-events (partitions P0 P1 P2)
                                       -> @KafkaListener: email, invoice, analytics
```

Events are retained and replayable. **The same key goes to the same partition, so order is preserved within a partition.**

**Why it matters:** the producer does not wait for the consumer; bursts get buffered instead of dropped; you can add a new consumer without touching the producer; you can replay from an offset after a bug fix.

**REST or Kafka?**

| Use REST when | Use Kafka when |
|---|---|
| The caller needs the answer now | Fire and forget |
| One-to-one call | One-to-many fan-out |
| Failure means showing an error | Failure means retry then dead-letter queue |
| Simple request/response | Ordering and replay matter |

**How do you guarantee a message is not lost or processed twice?**
Producer side: `acks=all` with retries so the write lands on every replica. Consumer side: commit the offset **only after** the work succeeds, and make the handler **idempotent** — usually by storing the event id and skipping duplicates. **Delivery is at-least-once, so idempotency is what actually saves you.**

**Gotcha:** ordering is only guaranteed within a partition. No key means round-robin, and your events arrive out of order.

## 26.20 Actuator and observability

Spring Boot Actuator provides production-ready features to monitor and manage your application.

| Endpoint | Purpose |
|---|---|
| `/actuator/health` | Application health status and component detail |
| `/actuator/info` | Build and git metadata |
| `/actuator/metrics` | JVM, HTTP and connection-pool stats |
| `/actuator/beans` | Beans in the context |
| `/actuator/env` | Environment properties |
| `/actuator/loggers` | View and change log levels at runtime |

```
Actuator -> Prometheus (scrapes time series) -> Grafana (dashboards) -> Alerts (p95, error rate)
```
Logs (ELK) tell you *what* happened; metrics tell you *that* something is happening.

**Advantages:** health monitoring, metrics collection, application information, easier troubleshooting in production, and friendly integration with Prometheus and Grafana.

**Securing the endpoints:** use Spring Security to restrict access, expose only what you need, use roles for sensitive endpoints, and use HTTPS in production.

```properties
management.endpoints.web.exposure.include=health,info
management.endpoints.web.base-path=/actuator
```

**Never expose all endpoints in production without security** — leaving `/env` or `/heapdump` open is a real data leak.

**Liveness vs readiness (Kubernetes):** liveness answers "should this pod be restarted?" — the process is wedged. Readiness answers "can it take traffic right now?", which may be false while warming caches or when a downstream is down. Getting them backwards means Kubernetes restarts a healthy pod that was just busy.

## 26.21 Testing, Docker and Kubernetes

**The test pyramid:** many fast unit tests, some integration tests, very few end-to-end.

```
Unit (JUnit 5 + Mockito, milliseconds)
  -> Slice (@WebMvcTest, @DataJpaTest)
    -> Integration (@SpringBootTest + Testcontainers)
```

| Situation | Test to write |
|---|---|
| One class, mocked dependencies | JUnit 5 + Mockito |
| Controller layer only | `@WebMvcTest` + MockMvc |
| Repository against a real DB | `@DataJpaTest` + `replace=NONE` |
| Full context | `@SpringBootTest` — use sparingly, it is slow |

**Testcontainers** spins up a real Postgres/Kafka in Docker, so you test the SQL that actually runs in production rather than H2's dialect.

**Gotcha:** `@DataJpaTest` swaps in an embedded database by default — add `@AutoConfigureTestDatabase(replace=NONE)` or Testcontainers is silently ignored.

**Docker and Kubernetes:** a multi-stage Dockerfile on a JRE base keeps the image small; build the image once and deploy it identically everywhere; Kubernetes handles deployment and service objects.

## 26.22 Microservices with Spring Cloud

Split by business capability, give each service its own database, keep them loosely coupled.

```
Client -> API Gateway (routing, auth, rate limit) -> Service Discovery (Eureka registry)
       -> user-service | payment-service | booking-service   (each with its OWN DB)
       -> Kafka (async events)
```

**How Spring Boot helps microservices:** lightweight and fast startup, embedded servers, auto-configuration, Actuator per service, easy integration with databases, Redis, Kafka and RabbitMQ, and Spring Cloud for discovery, config, routing and scaling.

**Benefits:** independent deployment, fault isolation, scalability, technology flexibility, easier maintenance, high availability.

**Honest trade-offs**

| You gain | You pay |
|---|---|
| Independent deploys | Network latency and retries |
| Fault isolation | Distributed tracing becomes necessary |
| Team autonomy | **No cross-service transactions** |
| Targeted scaling | Much heavier operations burden |

**When NOT to go microservices:** a small team, a single product, no scaling pain — a well-modularised monolith wins. Microservices trade code complexity for **operational** complexity, and you need the CI/CD, monitoring and tracing to pay for it. Start modular and split along the seams that actually hurt.

**Gotcha:** a shared database between services is a **distributed monolith** — you get the latency without the independence.

**Best practices:** keep services small and single-purpose, use meaningful service names, monitor each service, use centralized config management, and secure services (SSL, OAuth2, roles).

## 26.23 Exception handling in Spring Boot

Centralise error handling with `@RestControllerAdvice` (or `@ControllerAdvice`) and `@ExceptionHandler`.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(
                FieldError::getField,
                FieldError::getDefaultMessage,
                (existing, replacement) -> existing));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

Instead of a wall of unreadable error output, the client gets:
```json
{ "title": "Title is required", "author": "Author is required" }
```

**Benefits of centralized error handling:** cleaner code, consistent error responses, easier debugging.

## 26.24 DTOs and validation

Do not accept or return your entity directly. Introduce DTOs:
- A **request DTO** for incoming data, carrying validation annotations
- A **response DTO** shaping what the API returns

**Benefits:** validate input early without touching the domain model, avoid exposing internal fields, and evolve the API without breaking clients.

```java
public record BookRequest(
    @NotBlank(message = "Title is required")
    @Size(max = 200, message = "Title must not exceed 200 characters")
    String title,

    @NotBlank(message = "Author is required")
    String author
) {}

public record BookResponse(String id, String title, String author) {
    public static BookResponse from(Book book) {
        return new BookResponse(book.getId().toHexString(), book.getTitle(), book.getAuthor());
    }
}
```

`@Valid` on a method argument makes Spring validate it automatically and throw `MethodArgumentNotValidException` (a 400) if it fails.

## 26.25 A complete REST controller example (Spring Boot + MongoDB)

**Setup.** Generate the project with Spring Initializr, Java 17+, with dependencies: Spring Web, Spring Data MongoDB, Validation.

```properties
spring.data.mongodb.uri=YOUR_CONNECTION_STRING
spring.data.mongodb.database=library
```

**Model**
```java
@Document(collection = "books")
public class Book {
    @Id private ObjectId id;
    private String title;
    private String author;
    // constructors, getters, setters
}
```
`@Document` tells Spring this class maps to a MongoDB document; `@Id` marks the primary key.

**Repository** — extending `MongoRepository` gives you `findAll()`, `findById()`, `save()`, `deleteById()` with no implementation code:
```java
@Repository
public interface BookRepository extends MongoRepository<Book, ObjectId> {
    List<Book> findByTitleContainingIgnoreCase(String title);
}
```

**Controller**
```java
@RestController
@RequestMapping("/api/books")
public class BookController {

    private final BookRepository bookRepository;

    public BookController(BookRepository bookRepository) {   // constructor injection
        this.bookRepository = bookRepository;
    }

    @PostMapping
    public ResponseEntity<Book> createBook(@RequestBody Book book) {
        Book saved = bookRepository.save(book);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }

    @GetMapping
    public ResponseEntity<List<Book>> getAllBooks() {
        return ResponseEntity.ok(bookRepository.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Book> getBookById(@PathVariable ObjectId id) {
        return bookRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping("/{id}")
    public ResponseEntity<Book> updateBook(@PathVariable ObjectId id, @RequestBody Book details) {
        return bookRepository.findById(id)
                .map(book -> {
                    book.setTitle(details.getTitle());
                    book.setAuthor(details.getAuthor());
                    return ResponseEntity.ok(bookRepository.save(book));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteBook(@PathVariable ObjectId id) {
        if (bookRepository.existsById(id)) {
            bookRepository.deleteById(id);
            return ResponseEntity.noContent().build();   // 204
        }
        return ResponseEntity.notFound().build();        // 404
    }
}
```

## 26.26 Connecting Spring Boot to MySQL (step by step)

This is the workflow from the course guide in the folder.

**1. Create a MySQL instance** (locally, or on AWS RDS: RDS -> Launch -> MySQL -> Dev/Test -> `db.t2.micro` -> set identifier, master username, master password -> enable public accessibility -> note the **endpoint** and **port 3306** -> open the inbound security group).

**2. Connect with MySQL Workbench.** Create a new connection using the server hostname, port, username and password. Create a schema, then a table:
```sql
CREATE SCHEMA `cs4500`;

CREATE TABLE `cs4500`.`sample` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

INSERT INTO `cs4500`.`sample` (`id`, `message`) VALUES (1, 'Hello');
SELECT * FROM cs4500.sample;
```

**3. Configure `application.properties`:**
```properties
spring.datasource.url=jdbc:mysql://SERVER/SCHEMA
spring.datasource.username=USERNAME
spring.datasource.password=PASSWORD
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.hibernate.ddl-auto=create
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
spring.datasource.testWhileIdle=true
spring.datasource.validationQuery=SELECT 1
```

**4. Add the MySQL connector to `pom.xml`:**
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

**5. Map a POJO to a table with JPA:**
```java
@Entity(name = "hello")
public class HelloObject {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String message;
    // constructors, getters, setters
}
```
`@Entity` maps the class to a table; all properties map to fields of the same name. `@Id` marks the primary key. `@GeneratedValue` makes the database generate it (`AUTO_INCREMENT`).

**6. Create the repository:**
```java
public interface HelloRepository extends JpaRepository<HelloObject, Integer> { }
```

**7. Use it in a controller:**
```java
@RestController
public class HelloController {

    @Autowired
    HelloRepository helloRepository;

    @RequestMapping("/api/hello/insert")
    public HelloObject insertHelloObject() {
        HelloObject obj = new HelloObject("Hello!");
        helloRepository.save(obj);
        return obj;
    }

    @RequestMapping("/api/hello/insert/{msg}")
    public HelloObject insertMessage(@PathVariable("msg") String message) {
        HelloObject obj = new HelloObject(message);
        helloRepository.save(obj);
        return obj;
    }

    @RequestMapping("/api/hello/select/all")
    public List<HelloObject> selectAllHelloObjects() {
        return helloRepository.findAll();
    }
}
```

**8. Build and run:** `mvn clean install`, then run the main class. Test at `http://localhost:8080/api/hello/insert` and `http://localhost:8080/api/hello/select/all`.

To deploy a WAR to an external Tomcat, extend `SpringBootServletInitializer` in your main application class and override `configure()`.

## 26.27 Spring Boot CLI and DevTools

**Spring Boot CLI** is a command-line tool for developing and testing Spring Boot applications quickly.

| Command | Purpose |
|---|---|
| `spring --version` | Check the CLI version |
| `spring init <project>` | Create a project from a template |
| `spring run <file>` | Run an application |
| `spring shell` | Open an interactive shell |

**DevTools** improves developer productivity: automatic restart on code changes, LiveReload for the browser, disabled caching, and global settings. Add `spring-boot-devtools` to `pom.xml`. It is enabled in development but **not in production**.

## 26.28 The full Spring Boot topic map

The two reference books in this folder cover the following, in this order. Use it as a study checklist.

**Tutorial book (49 chapters):**
Introduction and microservices -> Quick start and CLI -> Bootstrapping (Spring Initializr, Maven, Gradle) -> Tomcat deployment -> Build systems -> Code structure -> Beans and Dependency Injection -> Runners (`ApplicationRunner`, `CommandLineRunner`) -> Application properties, YAML, `@Value`, profiles -> Logging (format, levels, Logback) -> Building RESTful web services (`@RestController`, request mapping, request body, path variable, request parameter, GET/POST/PUT/DELETE) -> Exception handling (`@ControllerAdvice`, `@ExceptionHandler`) -> Interceptors -> Servlet filters -> Tomcat port configuration -> `RestTemplate` -> File handling -> Service components -> Thymeleaf -> Consuming RESTful services -> CORS support -> Internationalization -> Scheduling (fixed rate, fixed delay) -> Enabling HTTPS -> Eureka server -> Service registration with Eureka -> Zuul proxy and routing -> Spring Cloud config server and client -> Actuator -> Admin server and client -> Swagger2 -> Docker images -> Tracing microservice logs (Sleuth, Zipkin) -> Flyway database migrations -> Sending email -> Hystrix -> WebSocket -> Batch service -> Spring for Apache Kafka -> Twilio -> Unit tests with Mockito -> REST controller unit tests -> Database handling (H2, MySQL, Redis, `JdbcTemplate`, multiple data sources) -> Securing web applications -> OAuth2 with JWT -> Google Cloud Platform -> Google OAuth2 sign-in.

**Enterprise Java course notes (433 sections):**
Development environment setup -> Enterprise Java frameworks (code reuse, framework enablers, DI, POJO, component, bean, container, interpose) -> Pure Java main application and Maven -> Simple Spring Boot application -> Bean factory and dependency injection -> Value injection -> Property source and profiles -> Configuration properties (`@ConfigurationProperties`, metadata, constructor binding, validation, Lombok, relaxed binding, nested properties) -> Auto configuration (conditional configuration, `@Primary`, class conditions, exclusions, debugging) -> Logging (levels, patterns, loggers, appenders, MDC, markers, file logging) -> Testing (JUnit 5, Mockito, BDD, `@TestConfiguration`) -> HTTP API (REST, RMM level 2, resources, URIs, methods, safety, idempotency, status codes, representations, links) -> Spring MVC (annotated controllers, `RestTemplate`, `WebClient`, parameters, responses, client error handling) -> Controller/service interface and exception advice -> API data formats (DTO pattern, Jackson, JSON, XML, date/time) -> Swagger -> Spring Security introduction, authentication, `UserDetails`, `PasswordEncoder`, authorization (roles, permissions, `@Secured`, JSR-250, expressions) -> JWT/JWS token authentication and authorization -> Enabling HTTPS -> Spring AOP and method proxies (reflection, JDK dynamic proxies, CGLIB, pointcuts, advice types) -> Heroku deployments -> Docker images and layering -> Docker Compose -> RDBMS (schema concepts, migration, SQL CRUD, JDBC) -> JPA (entities, CRUD, transactions) -> Spring Data JPA repositories (`CrudRepository`, `PagingAndSortingRepository`, query by example, derived queries, JPA-QL named queries, `@Query`, custom queries) -> End-to-end JPA application (BO/DTO architecture, mappers, service tier, REST controller) -> MongoDB with the Mongo shell -> `MongoTemplate` -> Spring Data MongoDB repositories -> End-to-end Mongo application -> Bean validation (declarative constraints, programmatic validation, graphs, groups, custom validation, cross-parameter validation, web/JPA/Mongo integration) -> Integration unit testing -> Docker Compose integration testing -> Testcontainers -> Testcontainers with Spock.

## 26.29 The five answers that carry a Spring interview

1. **Constructor injection** — always say *why* (immutable, testable, fails fast)
2. **Auto-config = classpath + conditions + your bean wins**
3. **N+1 is fixed with `JOIN FETCH`, not `EAGER`**
4. **Self-invocation breaks `@Transactional` and `@Cacheable`**
5. **Kafka is at-least-once, so handlers must be idempotent**

> "Anyone can define it. Seniors explain the trade-off." Say what you would give up, and why.

---

# Part 27 — System Design Fundamentals

## 27.1 Core concepts

**Scalability** — the property of a system to handle a growing amount of load by adding resources. As a system grows, performance degrades unless you adapt it.

**Availability** — the proportion of time a system is operational and accessible.
```
Availability = Uptime / (Uptime + Downtime)
```

**Latency vs Throughput**
- **Latency** — the time a single operation takes to complete. Low latency means faster response times; high latency causes lag and poor user experience.
- **Throughput** — the amount of work done in a period, usually requests per second (RPS) or transactions per second (TPS).

**CAP theorem** — it is impossible for a distributed data store to simultaneously guarantee all three of:
- **Consistency (C)** — every read receives the most recent write, or an error
- **Availability (A)** — every request receives a non-error response, without guaranteeing it has the most recent write
- **Partition Tolerance (P)** — the system keeps operating despite dropped or delayed network messages between nodes

**Load balancers** distribute incoming traffic across multiple servers so no single one is overwhelmed.

| Algorithm | Behaviour |
|---|---|
| Round Robin | Distributes requests evenly, in circular order |
| Weighted Round Robin | Distributes based on server capacity weights |
| Least Connections | Sends to the server with the fewest active connections |
| Least Response Time | Routes to the fastest-responding server |
| IP Hash | Assigns based on a hash of the client IP |

**CDN (Content Delivery Network)** — a geographically distributed network of servers that delivers web content based on the user's location. It redirects the request to the nearest server, reducing latency and improving load times.

**Message queues** enable asynchronous communication. Producers send messages and move on without waiting; multiple consumers pull messages, distributing and balancing the work.

**Rate limiting** protects services from being overwhelmed by too many requests from one client.

| Algorithm | Behaviour |
|---|---|
| Token Bucket | Allows bursts within an overall rate limit |
| Leaky Bucket | Smooths traffic flow at a constant rate |
| Fixed Window Counter | Limits requests in fixed time intervals |
| Sliding Window Log | Tracks requests within a rolling time window |
| Sliding Window Counter | Smooths the rate between adjacent fixed windows |

**Database indexes** — a super-efficient lookup table holding indexed column values plus pointers to the rows. Without an index the database scans every row; with one it goes straight to the data.

**Consistent hashing** — a hashing technique that distributes data across a cluster so that **only a small portion of the data must be reassigned when nodes are added or removed**.
1. **Hash space** — imagine a circular ring from 0 to 2^n−1
2. **Mapping servers** — each server is hashed to one or more points on the ring
3. **Mapping data** — each data item is hashed onto the ring
4. **Assignment** — an item is stored on the first server found moving clockwise from its position

**Database sharding** — a horizontal scaling technique that splits a large database into smaller independent pieces (shards) distributed across servers, each responsible for a subset of the data.

**Consensus algorithms** ensure all nodes agree on the same state despite latency, failures and asynchrony.
- **Paxos** — elects a leader that proposes a value, accepted by a majority of nodes
- **Raft** — designates one node as leader to manage log replication and ensure consistency

**Proxy servers** act as a gateway between you and the internet.
- **Forward proxy** — sits in front of a client, forwarding requests on the client's behalf
- **Reverse proxy** — sits in front of a web server, forwarding client requests to it

**Heartbeats** — periodic messages between components to monitor health. Without them, failure detection is slow, causing delayed recovery, more downtime and lower reliability.

**Checksums** — a unique fingerprint attached to data before transmission. It is recalculated on arrival; if it matches, the data was not modified or damaged.

**Service discovery** — lets services find and communicate with each other dynamically. A **service registry** acts as a single source of truth that services query.

**Bloom filters** — a probabilistic data structure that tells you an element is **definitely not** in a set, or **possibly** in it.
1. Start with a bit array of m bits (all 0) and k hash functions
2. To add an element, hash it k times and set those k bits to 1
3. To query, hash it k times: if **any** bit is 0 the element is definitely absent; if all are 1 it is either present or a false positive

**Gossip protocol** — a decentralized protocol that spreads information across all nodes, inspired by word-of-mouth. Each node periodically picks a random node and shares its current information; the process repeats until every node converges on the same state.

## 27.2 The trade-offs

| Trade-off | Summary |
|---|---|
| **Vertical vs Horizontal Scaling** | Vertical boosts one machine (simpler, but has a physical limit and a single point of failure). Horizontal adds servers (almost limitless, but brings distributed complexity) |
| **Strong vs Eventual Consistency** | Strong: any read returns the most recent write. Eventual: given enough time all nodes converge, with no guarantee when |
| **Stateful vs Stateless Design** | Stateful remembers client data between requests. Stateless treats each request as independent — every request must carry everything needed |
| **Read-Through vs Write-Through Cache** | Read-through: on a miss, the cache loads from the store, caches it and returns it. Write-through: writes go to cache and database simultaneously and complete only when both succeed |
| **SQL vs NoSQL** | SQL for complex queries, ACID compliance and stable structure. NoSQL for big data, rapid iteration and easier horizontal scaling |
| **REST vs RPC** | REST is resource-based, stateless, uses standard HTTP methods and returns JSON/XML. RPC is action-based, can use various protocols and often custom formats |
| **Synchronous vs Asynchronous** | Sync executes sequentially — easier to reason about, needed when order matters. Async executes concurrently — better responsiveness for I/O-bound work and background jobs |
| **Batch vs Stream Processing** | Batch processes large volumes at scheduled intervals — efficient, but high latency (ETL, reporting, backups). Stream processes in real time — minimal latency (fraud detection, live feeds, IoT) |
| **Long Polling vs WebSockets** | Long polling repeatedly requests updates, holding the connection until data is available — higher latency and server load. WebSockets establish a persistent full-duplex connection so both sides can send messages continuously |
| **Normalization vs Denormalization** | Normalization splits data into related tables to reduce redundancy and improve integrity. Denormalization combines data back into fewer tables to improve query performance, reintroducing redundancy |
| **TCP vs UDP** | TCP is reliable, ordered and connection-oriented but slower (web browsing, file transfer). UDP is fast, connectionless and unreliable (video streaming, gaming) |

## 27.3 The system design interview template

**Step 1 — Clarify requirements**

*Functional:* What core features must the system support? Who are the users? How will they interact (web, mobile, API)? What key data types must it handle? Are there external systems or third-party services to integrate with?

*Non-functional:* Is the system read-heavy or write-heavy, and what is the read-to-write ratio? Can it have downtime, or must it be highly available? Are there specific latency requirements? How critical is data consistency? Should users be rate limited?

**Step 2 — Capacity estimation**
How many daily and monthly users, and peak concurrent users? Expected read/write requests per second? Storage required? Memory needed for the cache? Network bandwidth?
(Check with the interviewer whether estimation is necessary.)

**Step 3 — High-level design**
Sketch a block diagram with: clients, application servers, load balancers, services, databases, storage, caching, message queues, external services.

**Step 4 — Database design**
Model the data (entities, relationships, attributes, primary keys, normalization), then choose the right storage based on structure, scalability, performance, consistency and query patterns. Consider a combination of databases if different data subsets have distinct requirements.

**Step 5 — API design**
List the APIs to expose. Select a style (REST, GraphQL, RPC). Choose protocols: HTTPS for REST, WebSockets for real-time bidirectional communication, gRPC for inter-service calls, AMQP/MQTT for asynchronous messaging.

**Step 6 — Dive deep into key components**
The interviewer will focus on specific areas. For a URL shortener, the short-URL generation algorithm. For a chat app, real-time message delivery. Common deep dives: database sharding and replication, adding servers behind the load balancer, where to add caching and how to invalidate it.

**Step 7 — Address key concerns**

*Scalability and performance:* scale up, scale out with load balancers, cache, optimise queries with indexes, denormalize where needed, partition and shard, use asynchronous models.

*Reliability:* identify single points of failure, design redundancy (multiple load balancers, database replicas), consider geographic redundancy, replicate data, use circuit breakers to prevent cascading failures, use retries with exponential backoff, and implement comprehensive monitoring and alerting.

## 27.4 Forty system design principles

1. Understand the functional and non-functional requirements before designing
2. Clearly define use cases and constraints
3. There is no perfect solution — it is all about trade-offs
4. Assume everything can and will fail; make it fault tolerant
5. Keep it simple; avoid over-engineering
6. Design for scalability from the ground up
7. Prefer horizontal scaling over vertical
8. Use load balancers for high availability and traffic distribution
9. Use SQL databases for structured data and ACID transactions
10. Use NoSQL databases for unstructured data
11. Use a graph database for highly connected data
12. Use sharding to scale SQL databases horizontally
13. Use indexing to optimise read queries
14. Design for fault tolerance
15. Use rate limiting to prevent overload and DoS attacks
16. Use WebSockets for real-time communication
17. Use heartbeat mechanisms to detect failures
18. Use a message queue for asynchronous communication
19. Implement data partitioning and sharding for large datasets
20. Denormalize for read-heavy workloads
21. Use bloom filters to check membership in a large dataset quickly
22. Use CDNs to reduce latency for a global user base
23. Use caching to reduce database load and improve response times
24. Use a write-through cache for write-heavy applications
25. Use a read-through cache for read-heavy applications
26. Use object storage like S3 for large datasets and media files
27. Implement replication and redundancy to avoid single points of failure
28. Implement autoscaling to handle traffic spikes
29. Use asynchronous processing for background tasks
30. Use batch processing for non-urgent tasks
31. Make operations idempotent to simplify retry logic
32. Use a data lake or warehouse for analytics and reporting
33. Implement comprehensive logging and monitoring
34. Implement circuit breakers to stop one failing service bringing down the system
35. Practise chaos engineering to test resilience
36. Design for statelessness where possible
37. Use failover mechanisms to switch to a redundant system automatically
38. Distribute across data centres to prevent localized failures
39. Use TTL values to expire cached data and reduce staleness
40. Pre-populate critical data in the cache to avoid cold starts

## 27.5 The ten most common system design questions

Each is listed with its typical requirements. Practise structuring an answer for each using the seven-step template.

**1. URL Shortener (TinyURL)**
*Functional:* generate a unique short URL; redirect to the original; optional custom short URLs; link expiration; optional usage analytics.
*Non-functional:* 99.9% availability; millisecond latency for shortening and redirects; millions of requests per day; durability for years; security against phishing.

**2. Chat Application (WhatsApp)**
*Functional:* one-on-one and group conversations; online/offline status; delivery statuses (sent, delivered, read); multimedia messages; push notifications.
*Non-functional:* real-time delivery with minimal latency; millions of concurrent users; high availability (availability may be compromised for consistency); durability — messages must not be lost.

**3. Social Media Platform (Instagram)**
*Functional:* upload and share images and videos; like, comment and share; follow and unfollow; generate a news feed; tagging.
*Non-functional:* 99.9% availability; low latency for feed generation; millions of concurrent users; high durability for uploads; eventual consistency is acceptable.

**4. Video Streaming Service (YouTube)**
*Functional:* upload videos with titles, descriptions, tags and thumbnails; on-demand streaming; search; like, dislike, comment and share; view counts.
*Non-functional:* 99.99% uptime; low-latency, lag-free streaming; horizontal scalability; high durability.

**5. E-commerce Platform (Amazon)**
*Functional:* sellers list products; cart and wishlist; search by product, category and brand; place orders; rate and review.
*Non-functional:* millions of users, products and transactions; 99.9% availability; low latency for page loads, search and checkout; high durability for user data, listings and orders.

**6. Ride-Sharing Service (Uber)**
*Functional:* see nearby available drivers; book a ride with pickup and drop-off; real-time matching; real-time cost and ETA estimation based on distance, traffic and demand; real-time tracking.
*Non-functional:* millions of concurrent users and rides; low latency for matching, GPS tracking and requests; 99.9% uptime; consistent view of the system for riders and drivers.

**7. File Storage Service (Google Drive)**
*Functional:* upload files of various types and sizes; download on demand; share files and folders via links or email; search by name, type, content or metadata; synchronization across devices.
*Non-functional:* millions of users and billions of files; low latency for uploads, downloads and search; high availability; consistency across devices during sync; durability.

**8. Web Crawler**
*Functional:* fetch URLs efficiently; handle different content types; prioritise URLs by importance and freshness; store crawled data efficiently.
*Non-functional:* scale to millions or billions of pages; minimal fetch and processing latency; maximise pages crawled per unit of time.

**9. Notification System**
*Functional:* multiple channels (email, SMS, push, in-app); different types (transactional, promotional, informational); scheduling; bulk sending for campaigns; automatic retries for failures.
*Non-functional:* millions of notifications per minute at peak; 99.99% uptime; low latency for real-time and high-priority notifications; reliable delivery across channels.

**10. Logging and Monitoring System**
*Functional:* collect logs from applications, servers, databases and microservices; support multiple formats (JSON, plaintext, XML); archive old logs to cold storage; powerful querying by time range, log level and source; alerts on patterns, thresholds or anomalies.
*Non-functional:* horizontal scalability for growing log volume; low-latency ingestion for real-time monitoring; 99.99% uptime; durability with replication across nodes or data centres.

---

# Part 28 — Study Plan and Practice Checklist

## 28.1 A 20-hour Pareto plan (the 20% that gives 80% of the results)

Ten two-hour sessions, each ending with a 15-minute review.

| Session | Topic | Practice at the end |
|---|---|---|
| 1 | Setup, first program, syntax, variables, data types, operators (Parts 1–4) | Write 10 tiny programs: sum, even/odd, swap, area, temperature conversion |
| 2 | Control flow and loops (Part 6) | Patterns, factorial, Fibonacci, prime check, reverse a number |
| 3 | Arrays and Strings (Parts 7–8) | Reverse a string, palindrome, second largest, remove duplicates |
| 4 | Methods and recursion (Part 9) | Overloading, varargs, factorial and Fibonacci recursively |
| 5 | OOP part 1 — classes, objects, constructors, `this`, `static`, `final` (Part 10) | Build a `BankAccount` class with encapsulation |
| 6 | OOP part 2 — inheritance, polymorphism, abstraction, interfaces (Parts 11–13) | Shape hierarchy with `draw()`, `Animal` hierarchy with `makeSound()` |
| 7 | Exceptions and file handling (Parts 15, 20) | Read a CSV, handle errors, write a custom exception |
| 8 | Collections (Part 16) | Word frequency counter with HashMap, sort objects with Comparator |
| 9 | Streams, lambdas, Optional, date/time (Part 19) | Rewrite session 8's solutions using streams |
| 10 | Multithreading basics and JDBC (Parts 17, 21) | Producer-consumer with `BlockingQueue`; a CRUD app on MySQL |

Then move to Parts 24–27 for backend and system design.

## 28.2 The learning ladder — five levels

| Level | You can... | Milestone |
|---|---|---|
| **1 — Beginner** | Write, compile and run programs; use variables, loops, arrays and methods | Solve 20 basic programs without help |
| **2 — Core** | Use OOP properly, handle exceptions, use collections | Build a console-based library or bank management app |
| **3 — Intermediate** | Use streams, threads, file I/O, JDBC; write unit tests | Build a CRUD app backed by a real database |
| **4 — Advanced** | Build REST APIs with Spring Boot, secure them, test them, containerise them | Deploy a Spring Boot API with JWT auth and a MySQL/Mongo backend |
| **5 — Systems** | Design for scale — caching, queues, microservices, monitoring | Design and explain a full system (URL shortener, chat app) end to end |

## 28.3 Topic checklist for interviews

| Topic | What is usually asked |
|---|---|
| Basics | What is Java? JDK vs JRE vs JVM? Features? |
| OOP | The four pillars; overloading vs overriding; abstract class vs interface |
| Inheritance | Why no multiple inheritance? `super`, upcasting, binding |
| Strings | Immutability; String vs StringBuilder vs StringBuffer; the String pool |
| Collections | ArrayList vs LinkedList; HashMap vs Hashtable; Comparable vs Comparator |
| Exceptions | Checked vs unchecked; `throw` vs `throws`; `final` vs `finally` vs `finalize` |
| Multithreading | Thread lifecycle; `synchronized`; `wait`/`notify`; deadlock; thread pools |
| Java 8 | Lambdas; functional interfaces; streams; `Optional` |
| JDBC | The five steps; `PreparedStatement`; transactions |
| Spring Boot | IoC and DI; auto-configuration; annotations; `@Transactional`; N+1 |
| REST | HTTP methods; status codes; idempotency; versioning; security |
| System design | CAP; caching; load balancing; SQL vs NoSQL; monolith vs microservices |

## 28.4 Best practices to carry into every project

- Understand the problem properly before you write code
- Write clean, simple, optimized code — if 200 lines could be 50, rewrite it
- Test with edge cases
- Analyse time and space complexity
- Handle specific exceptions first and give meaningful messages
- Always close resources (use try-with-resources)
- Never trust user input on the backend
- Never store passwords in plain text
- Use constructor injection, DTOs and centralized error handling in Spring
- Make retryable operations idempotent
- Log and monitor everything in production

## 28.5 Where each part of this guide came from

| Source file in `javanotes/` | Contributed to |
|---|---|
| `1787045175993.pdf` — Java programming (79 pp) | Parts 1–8, 10–18, 21 |
| `java.pdf` — Java Notes 1–20 by Abhishek Rathor (20 pp, scanned) | Parts 1–23 |
| `javanotes1.pdf` — Java notes 1–10 (10 pp, scanned) | Parts 1–16, 20 |
| `Java_Methods_Cheat_Sheet.pdf` | Part 9 |
| `java diagram.png` | Part 3.4 |
| `java multithreading and concurrency.pdf` (147 pp) | Part 17 |
| `1788750814441.pdf` — DSA patterns (scanned) | Part 23 |
| `systemdesignpatterns.pdf` — System Design Handbook (75 pp) | Part 27 |
| `1788540851430.pdf` / `backenddevelopementnotes.pdf` (identical) | Part 24 |
| `restapi.pdf` — REST API notes (scanned) | Part 25 |
| `apiinterviewquestions.pdf` — 100 API questions | Part 25 + interview file |
| `1787731829904.pdf` — Spring Boot Field Notes | Part 26 |
| `javabackend notes.pdf` / `topspringquestions.pdf` (identical) — Top 50 Backend Questions | Part 26 + interview file |
| `spring_boot_tutorial_tutorialspoint.pdf` (332 pp) | Part 26.28 |
| `jhu784-notes-javaspringbootnotes.pdf` (1336 pp) | Part 26.28 |
| `Building REST APIs in Java with Spring Boot.pdf` | Part 26.25 |
| `Integrating-Spring-Boot-with-MySQL.pdf` | Part 26.26 |
| `dev_man_springbootjava.pdf` | Part 26 (environment setup) |
| `javainterviewnotes.pdf` — 94 Java questions | Interview file |

Two files in the folder are **not** Java material and were excluded: `img20241001_22125387.pdf` and `img20241001_22183202.pdf` are a scanned Prep for Prep Summer Internship Program agreement form.

---

---
---

# Part 29 — Spring Boot in Depth: The Senior-Level Field Guide

> Source: *Spring Boot Complete Notes, Parts 1–4* (mellaithy) — 36 pages covering the core, data, security and delivery layers.
> This part goes deeper than Part 26 and deliberately focuses on **defaults, traps and corrections** — the things that are wrong in most circulated cheat sheets.
> Verified against current Spring Boot (3.5.x) and Spring Security 6.

## 29.1 What Spring Boot actually is

Spring Boot is an **opinionated layer on top of the Spring Framework**. It does not replace Spring — it removes the setup ceremony so you go from an empty folder to a running, production-shaped service in minutes.

**The distinction that matters:**
- **Spring** gives you the **programming model** — IoC, DI, AOP, MVC.
- **Boot** gives you the **delivery model** — defaults, packaging, and runtime wiring.

**The four pillars.** Everything else Boot does is a consequence of these:

| Pillar | What it removes | How |
|---|---|---|
| Auto-configuration | Manual bean definitions | Conditional beans based on the classpath |
| Starter dependencies | Version conflicts | Curated, tested dependency sets |
| Embedded server | External deployment | Tomcat / Jetty / Undertow inside the jar |
| Actuator | Custom health plumbing | Ready-made ops endpoints |

**What it is not**
- Not a replacement for the Spring Framework
- Not a code generator — nothing is scaffolded into your source tree
- Not an application server
- Not magic — every auto-configuration is a conditional `@Bean` you can inspect

**Interview answer:** "Boot reduces the time between deciding to build a service and having one that runs. It does that with sensible defaults you can always override — nothing is hidden, just pre-decided."

**Prove it to yourself:** run with `--debug` and Boot prints a full auto-configuration report — what matched, what did not, and why.

**Vocabulary**

| Term | Means |
|---|---|
| Bean | An object whose lifecycle the container owns |
| Context | The container instance holding all beans |
| Starter | A dependency bundle with curated versions |
| Auto-configuration | Conditional beans registered from the classpath |
| Fat jar | One executable jar with every dependency inside |

**Version reality:** Boot 3.x requires **Java 17 or newer** and runs on the **`jakarta.*`** namespace, not `javax.*`. Anything written for Boot 2.x needs both changes before it will compile.

## 29.2 Spring Framework vs Spring Boot — the honest comparison

**What plain Spring costs you:** dependency versions chosen and aligned by hand; component scanning, view resolvers and data sources declared explicitly; a servlet container installed, configured and deployed to separately; health, metrics and externalised config built yourself.

None of that is a flaw — it is **explicit control**. Boot trades some of that control for speed, and lets you take it back one property at a time.

| Concern | Spring Framework | Spring Boot |
|---|---|---|
| Configuration | Explicit XML or Java config | Auto-configuration, overridable |
| Dependencies | Managed manually | Starters with curated versions |
| Server | External (deploy a WAR) | Embedded (run an executable jar) |
| Time to first run | Hours | Minutes |
| Observability | Assembled yourself | Actuator out of the box |
| Config per environment | Custom mechanism | Profiles + property precedence |
| Best suited to | Legacy estates, bespoke architecture | Services, APIs, cloud-native apps |

**Choosing, honestly:** reach for Boot for anything greenfield. Stay on plain Spring inside an existing estate that already owns its wiring, or when a hard requirement conflicts with an auto-configuration you would end up disabling anyway.

**Taking control back** — auto-configuration is not all-or-nothing:
```java
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })
public class App { }
```

**Rule of thumb:** define a bean yourself and Boot backs off — most auto-configurations are `@ConditionalOnMissingBean`.

**Interview answer:** "Boot is Spring with the assembly already done. Same core container, same beans, same lifecycle — the difference is who writes the configuration."

## 29.3 The startup sequence

```
SpringApplication.run()
  -> Prepare Environment
    -> Create ApplicationContext
      -> Run auto-config
        -> Instantiate beans
          -> Start embedded server
            -> Ready
```

The **Environment is built first**, which is why properties and profiles are already resolved by the time any bean is created.

**Common misconception:** the embedded server starts near the **end**. If a bean fails to construct, the port never opens — that is deliberate **fail-fast** behaviour.

**Interview answer:** "SpringApplication prepares the environment, creates the context, applies auto-configuration, instantiates singletons, then starts the server. Fail-fast: a bad bean means no listening port."

## 29.4 Creating a project properly

Generate from `https://start.spring.io` or from your IDE. Choose Maven or Gradle, take the **latest GA** Boot version (not a snapshot), pick the Java LTS your runtime actually has (17 or 21), and add only the starters you need today.

| | Maven | Gradle |
|---|---|---|
| Config | XML (`pom.xml`) | Groovy / Kotlin DSL |
| Build speed | Slower | Faster (incremental + cache) |
| Learning curve | Gentle | Steeper |
| Flexibility | Convention-bound | Highly programmable |
| Typical fit | Enterprise, stable estates | Large or multi-module builds |

Either is fine — pick what your team already runs in CI. Consistency beats micro-optimisation.

**Generated layout**
```
my-app/
├─ src/main/java/
│   └─ com/example/demo/
│       └─ DemoApplication.java
├─ src/main/resources/
│   ├─ application.yml
│   ├─ static/
│   └─ templates/
├─ src/test/java/
└─ pom.xml
```

**Package placement matters.** Keep `DemoApplication` in the **root package**. Component scanning starts from its package downwards — beans in sibling packages are **silently ignored**.

**Minimal pom.xml**
```xml
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.5.x</version>
</parent>

<properties>
  <java.version>21</java.version>
</properties>

<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
</dependencies>
```

**Why no version tags?** The parent POM supplies them. Overriding a single starter version by hand is the fastest way to break a working dependency set.

**Running it**
```bash
mvn spring-boot:run              # dev loop
mvn clean package                # build the jar
java -jar target/my-app.jar      # run it anywhere
```
Defaults to `http://localhost:8080`. Change with `server.port`, or set it to **0 for a random free port** — useful in tests.

**Setup checklist:** latest GA Boot version and Java 17/21 · main class in the root package · only the starters you use · `application.yml` over `.properties` for anything nested · a dev profile committed, secrets kept out of the repo.

## 29.5 Dependency injection, in detail

The Spring IoC container creates, configures, wires and destroys beans. `ApplicationContext` is the interface you meet; `BeanFactory` is the lower-level one beneath it.

**A bean is just an object.** Nothing is special about the class — a bean is any object whose lifecycle the container owns, declared via a stereotype annotation, a `@Bean` method, or configuration.

| Style | Verdict |
|---|---|
| **Constructor** | **Recommended** — immutable, testable, fails fast |
| Setter | Acceptable for genuinely optional collaborators |
| Field | **Avoid** — hides dependencies, blocks `final`, hard to test |

**Correction worth knowing:** since **Spring 4.3**, `@Autowired` is **optional** on a class with a single constructor. Most tutorials still show it — it is redundant noise.

```java
@Service
public class UserService {

    private final UserRepository repository;
    private final EmailSender emailSender;

    // no @Autowired needed: single constructor
    public UserService(UserRepository repository, EmailSender emailSender) {
        this.repository = repository;
        this.emailSender = emailSender;
    }
}
```

**Why `final` matters:** final fields cannot be reassigned or left null. The compiler enforces what would otherwise be a runtime `NullPointerException`.

**Bean scopes**

| Scope | One instance per |
|---|---|
| singleton | Container (**default**) |
| prototype | Request for the bean |
| request | HTTP request |
| session | HTTP session |
| application | ServletContext |
| websocket | WebSocket session |

**Singleton is not the same as thread-safe.** One instance is shared across all threads. Keep mutable state out of your beans — this is the single most common source of production race conditions.

**Bean lifecycle**
```
Definition read -> Instantiate -> Populate dependencies -> Aware callbacks
  -> @PostConstruct -> In use -> @PreDestroy
```

**Spelling that trips people up:** the annotations are `@PostConstruct` and `@PreDestroy` — not `@PreDestrory`. In Boot 3.x they come from **`jakarta.annotation`**, not `javax.annotation`.

**Interview answers**
- *What is IoC?* The container, not your code, owns object creation and wiring.
- *Why constructor injection?* Dependencies are explicit and mandatory, fields can be `final`, and the class is usable without Spring at all — which is exactly what makes it unit-testable.

## 29.6 Annotations that carry the weight

**`@SpringBootApplication`** combines `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.

**Stereotypes**

| Annotation | Marks |
|---|---|
| `@Component` | Any container-managed bean |
| `@Service` | Business logic |
| `@Repository` | Data access — **plus exception translation** |
| `@Controller` | MVC controller returning view names |
| `@RestController` | `@Controller` + `@ResponseBody` |
| `@Configuration` | Class declaring `@Bean` methods |

**`@Repository` earns its keep.** It is not just a label — it translates vendor-specific persistence exceptions into Spring's `DataAccessException` hierarchy, so your service layer never imports a Hibernate exception type.

**Wiring and configuration**

| Annotation | Purpose | Note |
|---|---|---|
| `@Autowired` | Inject a dependency | Optional on a single constructor |
| `@Qualifier` | Disambiguate candidates | Use when two beans match |
| `@Primary` | Default among candidates | Cleaner than `@Qualifier` everywhere |
| `@Value` | Inject one property | Good for a handful of values |
| `@Bean` | Declare a bean manually | For types you do not own |
| `@Profile` | Restrict to environments | e.g. dev-only stubs |

```java
@Service @Primary
class SmsSender implements Notifier {}

@Service("email")
class EmailSender implements Notifier {}

// picks EmailSender explicitly
public Svc(@Qualifier("email") Notifier n) { ... }
```

**Habits worth forming**
- Use the specific stereotype, not bare `@Component` — it documents intent
- Prefer constructor injection; drop the redundant `@Autowired`
- Group related properties with `@ConfigurationProperties` instead of scattering `@Value`
- Keep `@Transactional` on the **service layer**, never on controllers

## 29.7 Configuration and profiles

**`@Value` vs `@ConfigurationProperties`**

| | `@Value` | `@ConfigurationProperties` |
|---|---|---|
| Best for | One or two values | A group of related keys |
| Type safety | String parsing | Bound and converted |
| Validation | Manual | Works with `@Validated` |
| Relaxed names | No | **Yes** |

```java
@Component
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private String name;
    private Duration timeout;
    // getters + setters
}
```

**Precedence — highest first**
1. Command-line arguments
2. OS environment variables
3. Profile-specific files (`application-{profile}.yml`)
4. Base `application.yml` / `.properties`
5. Defaults in `@Value` or the code itself

**Profile-specific wins key by key** — `application-prod.yml` overrides `application.yml` per key; it does **not** replace the file.

**Environment variable mapping (relaxed binding)**

| Property | Environment variable |
|---|---|
| `server.port` | `SERVER_PORT` |
| `spring.datasource.url` | `SPRING_DATASOURCE_URL` |
| `app.retry-count` | `APP_RETRYCOUNT` |

Uppercase, dots to underscores. This is why Kubernetes and Docker configuration works with **no adapter code**, and why one immutable image can behave differently per environment.

**Configuration rules:** secrets from environment or a vault, never committed · `ddl-auto: validate` in production, never `update` · group keys under a prefix and bind them as a type · fail fast on missing required config with `@Validated` · keep `application.yml` as the shared baseline only.

**Production hazard:** `ddl-auto: update` lets Hibernate alter live schema on startup. It silently drifts from your migrations. Use **Flyway or Liquibase** and set `validate`.

**Never keep both a `.properties` and a `.yml` file for the same profile** — the resolution order will surprise someone.

## 29.8 REST APIs and request handling

**The six REST constraints:** client–server · stateless · cacheable · uniform interface · layered system · code on demand (optional, rare).

**Stateless in practice:** no server-side session affinity. This is precisely what makes horizontal scaling and rolling deploys safe.

| Method | Purpose | Body | Idempotent |
|---|---|---|---|
| GET | Read a resource | No | Yes |
| POST | Create / non-idempotent action | Yes | No |
| PUT | Replace a resource wholly | Yes | Yes |
| PATCH | Update part of a resource | Yes | No* |
| DELETE | Remove a resource | No | Yes |

**Idempotent — the definition and the spelling.** *Idempotent* (not "inempotent"): making the same request many times leaves the server in the same state as making it once. *PATCH can be idempotent, but only if you design the patch document that way.

**A controller**
```java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {

    private final UserService service;
    public UserController(UserService service) { this.service = service; }

    @GetMapping
    Page<UserDto> list(Pageable pageable) { return service.list(pageable); }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    UserDto create(@Valid @RequestBody CreateUser req) { return service.create(req); }
}
```

**Keep controllers thin.** A controller should bind input, delegate, and shape the response. The moment business rules appear in one, they become untestable without the web layer.

**URI design**

| | Do | Do not |
|---|---|---|
| Nouns | `/api/users` | `/api/getUsers` |
| Nesting | `/api/users/{id}/orders` | `/api/userOrders?id=` |
| Versioning | `/api/v1/users` | unversioned public API |
| Plurality | consistently plural | mixed `/user` and `/users` |

**Where data arrives from — four places, one annotation each**

| Annotation | Reads from | Example |
|---|---|---|
| `@PathVariable` | URI segment | `/users/{id}` |
| `@RequestParam` | Query string | `?page=0&size=20` |
| `@RequestBody` | Request body | JSON payload |
| `@RequestHeader` | HTTP header | `Authorization` |
| `@CookieValue` | Cookie | session tracking |
| `@ModelAttribute` | Form data | HTML form submit |

```java
@PutMapping("/users/{id}")
UserDto update(@PathVariable Long id,
               @Valid @RequestBody UpdateUser body,
               @RequestParam(defaultValue = "false") boolean notify,
               @RequestHeader("X-Request-Id") String requestId) {
    return service.update(id, body, notify, requestId);
}
```

**Prefer the filter chain:** reading `Authorization` in a controller means auth logic is scattered. Handle it once in Spring Security.

**The classic mistake:** sending a body with GET. Some clients and proxies drop it silently — if you need a complex query, use POST for a search endpoint.

## 29.9 Response handling

**Status codes that carry meaning**

| Code | Meaning | Use when |
|---|---|---|
| 200 | OK | Read or update succeeded |
| 201 | Created | Resource created — **add a `Location` header** |
| 204 | No Content | Success with nothing to return |
| 400 | Bad Request | Malformed or invalid input |
| 401 | Unauthorized | Missing or invalid credentials |
| 403 | Forbidden | Authenticated but not permitted |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | State conflict, e.g. duplicate key |
| 422 | Unprocessable | Syntactically valid, semantically wrong |
| 500 | Server Error | Unhandled fault — your bug |

**Status by operation:** get one/list → 200 · create → 201 · update → 200 · delete → 204 · async accepted → 202.

**The 201 detail people skip:** a 201 should include a `Location` header pointing at the new resource. It is part of the contract, and almost nobody does it.

```java
URI location = ServletUriComponentsBuilder
    .fromCurrentRequest().path("/{id}")
    .buildAndExpand(saved.id()).toUri();

return ResponseEntity.created(location).body(saved);
```

**`ResponseEntity` — you do not always need it.** Returning the DTO directly with `@ResponseStatus` is cleaner for the common case. Reach for `ResponseEntity` when the status varies at runtime.

**A consistent envelope** — pick one response shape and use it everywhere:
```json
{ "timestamp": "2026-08-14T09:20:00Z", "status": 200,
  "data": { "id": 101, "name": "Layla Hassan" } }

{ "timestamp": "2026-08-14T09:20:00Z", "status": 404, "error": "NOT_FOUND",
  "message": "User 101 does not exist", "path": "/api/v1/users/101" }
```

**The anti-pattern:** `200 OK` with `{"success": false}` in the body. It defeats every HTTP-aware layer between you and the client — caches, retries, monitoring, load balancers.

## 29.10 Validation

Validate at the boundary, before a single business rule runs.

| Annotation | Asserts |
|---|---|
| `@NotNull` | Not null (**an empty string passes**) |
| `@NotEmpty` | Not null and not empty |
| `@NotBlank` | Not null and has non-whitespace text |
| `@Size(min,max)` | Length or collection size |
| `@Min` / `@Max` | Numeric bounds |
| `@Positive` / `@Negative` | Sign |
| `@Email` | Well-formed email address |
| `@Pattern(regexp)` | Matches a regular expression |
| `@Past` / `@Future` | Temporal bounds |

**The three null checks:** `@NotNull` allows `""`. `@NotEmpty` allows `" "`. For user-supplied text you almost always want **`@NotBlank`**.

```java
public record CreateUser(
    @NotBlank(message = "name is required") @Size(max = 100) String name,
    @NotBlank @Email String email,
    @Min(18) @Max(120) int age
) {}
```

Records fit this perfectly — immutable, no boilerplate, constraints on the components. Requires `spring-boot-starter-validation`.

**Do not take a `BindingResult` parameter.** Adding one suppresses the exception and forces you to handle errors in every controller. Leave it out, let `MethodArgumentNotValidException` throw, and handle it once globally.

**Nested and collections — cascade is not automatic:**
```java
public record CreateOrder(
    @NotNull @Valid Address shipTo,
    @NotEmpty List<@Valid OrderLine> lines
) {}
```
Without `@Valid` on the nested field, the inner object's constraints are never evaluated.

**Custom constraint**
```java
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = StrongPasswordValidator.class)
public @interface StrongPassword {
    String message() default "password is too weak";
    Class<?>[] groups() default {};                  // required
    Class<? extends Payload>[] payload() default {}; // required
}

public class StrongPasswordValidator
        implements ConstraintValidator<StrongPassword, String> {
    @Override
    public boolean isValid(String v, ConstraintValidatorContext c) {
        if (v == null) return true;   // @NotNull owns null
        return v.length() >= 12 && v.matches(".*[A-Z].*");
    }
}
```

**The flow:** `@Valid` → Hibernate Validator runs → on failure Spring throws `MethodArgumentNotValidException` **before your method body executes** → `@RestControllerAdvice` converts it to a 400 with field-level detail.

## 29.11 Exception handling

Give each failure mode a meaningful type, and extend `RuntimeException` — checked exceptions force every caller to declare or catch, polluting signatures all the way up.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    ApiError notFound(UserNotFoundException ex) {
        return ApiError.of("NOT_FOUND", ex.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    ApiError invalid(MethodArgumentNotValidException ex) {
        List<FieldError> fields = ex.getBindingResult().getFieldErrors().stream()
            .map(e -> new FieldError(e.getField(), e.getDefaultMessage()))
            .toList();
        return ApiError.of("VALIDATION_FAILED", fields);
    }

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    ApiError unexpected(Exception ex) {
        log.error("Unhandled", ex);                       // log the detail
        return ApiError.of("INTERNAL", "Something went wrong"); // return nothing
    }
}
```

**Handler ordering:** Spring picks the most specific matching handler. Keep a broad `Exception.class` handler **last** — it catches anything you forgot, which is exactly its job.

Anything thrown below the controller — service, repository, even a converter — surfaces through the same advice.

**Never leak internals.** No stack traces, no SQL, no class names in the response. Log them server-side with a correlation id and return that id instead.

**Consider `ProblemDetail`** — Spring 6 ships an implementation of RFC 9457 (formerly RFC 7807), giving a standard error shape for free:
```java
@ExceptionHandler(UserNotFoundException.class)
ProblemDetail handle(UserNotFoundException ex) {
    ProblemDetail pd = ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
    pd.setTitle("User not found");
    return pd;
}
```

**Interview answer:** "`@ExceptionHandler` is per-controller. `@RestControllerAdvice` applies across all of them and returns JSON — that is what you want for an API."

## 29.12 Spring Data JPA — the three names and the traps

| Name | What it is |
|---|---|
| **JPA** | A specification — interfaces and rules only |
| **Hibernate** | The most common implementation |
| **Spring Data JPA** | Generates repositories over a JPA provider |

**Why the distinction is asked:** it tests whether you understand you are coding against an interface. You could swap Hibernate for EclipseLink without touching your repositories.

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(unique = true)
    private String email;

    protected User() {}   // required by JPA — may be protected
}
```

It is spelled **`@Column`** (not `@Colmm`), and it controls name, length, nullability and uniqueness.

**What `JpaRepository` gives you**

| Method | Does |
|---|---|
| `save(entity)` | Insert **or update** (merge) |
| `saveAll(entities)` | Batch save |
| `findById(id)` | Returns `Optional<T>` |
| `findAll()` / `findAll(Pageable)` | All, or one page |
| `existsById(id)` | Existence check without loading |
| `count()` | Row count |
| `deleteById(id)` | Delete by primary key |
| `flush()` | Force pending writes to the database |

**`save()` is not always an INSERT.** If the entity has an id that already exists, it becomes an **update**. This surprises people who expect a duplicate-key error.

**Derived query keywords**

| Fragment | Generates |
|---|---|
| `findBy` / `readBy` / `getBy` | SELECT |
| `And` / `Or` | Boolean composition |
| `Between` / `LessThan` / `GreaterThan` | Range comparison |
| `Like` / `Containing` / `StartingWith` | Pattern match |
| `IgnoreCase` | Case-insensitive comparison |
| `OrderBy...Asc` / `Desc` | ORDER BY |
| `Top` / `First` | Limit results |

**Entity rules:** every entity needs `@Id` and a no-arg constructor · return `Optional` from single-result finders · keep entities free of business logic · **never return entities from a controller** · paginate anything unbounded.

**equals/hashCode on entities:** do **not** use generated `equals` over all fields, and do not rely on a database-generated id before it is assigned. Use a business key, or leave both methods alone.

## 29.13 Entity relationships — who owns the foreign key

The **owning side** is the one carrying `@JoinColumn`.

| Mapping | Owner carries |
|---|---|
| One-to-One | `@JoinColumn` |
| Many-to-One | `@JoinColumn` |
| One-to-Many | inverse — `mappedBy` |
| Many-to-Many | `@JoinTable` |

```java
@Entity
class Department {
  @OneToMany(mappedBy = "department", cascade = CascadeType.ALL, orphanRemoval = true)
  private List<Employee> employees = new ArrayList<>();
}

@Entity
class Employee {
  @ManyToOne(fetch = FetchType.LAZY)      // override the EAGER default!
  @JoinColumn(name = "department_id")
  private Department department;          // owner
}
```

**`mappedBy` means "not me".** The side with `mappedBy` is the inverse side. Changes made **only** to the inverse side are not persisted — always update the owner.

**Fetch types and their defaults**

| Mapping | Default fetch | Should be |
|---|---|---|
| `@ManyToOne` | **EAGER** | Set LAZY explicitly |
| `@OneToOne` | **EAGER** | Set LAZY explicitly |
| `@OneToMany` | LAZY | Leave it |
| `@ManyToMany` | LAZY | Leave it |

**The default that costs you:** to-one associations default to EAGER — loading 100 employees silently fetches 100 departments.

**Cascade types:** PERSIST (save of the parent) · MERGE (update) · REMOVE (delete) · REFRESH (reload) · DETACH (removal from context) · ALL (all of the above).

**`CascadeType.ALL` is a loaded gun** — it includes REMOVE. Deleting a `Department` then deletes every `Employee`. Cascade from parent to child only, and **never across an aggregate boundary**.

**Prefer two one-to-manys over `@ManyToMany`.** The moment the join needs an extra column — enrolled date, grade, status — `@ManyToMany` cannot express it. Model the join table as its own entity from the start and avoid a painful migration later.

**N+1 — the problem you will be asked about.** Loading N parents then lazily touching a child on each triggers N extra queries. Fix with a **fetch join** or an **`@EntityGraph`**. Turn on `spring.jpa.show-sql` in dev and you will spot it immediately.

## 29.14 Advanced JPA

**Pagination** — `Pageable` binds automatically from the query string; the page index starts at **0**:
```java
@GetMapping("/users")
Page<UserDto> list(Pageable pageable) {
    return repository.findAll(pageable).map(mapper::toDto);
}
// GET /users?page=0&size=20&sort=createdAt,desc
```

**Sorting** is on **entity properties**, not column names — `createdAt`, not `created_at`. An invalid property throws at runtime, not compile time.

**JPQL vs native**

| | JPQL | Native |
|---|---|---|
| Works on | Entities | Tables |
| Portable | Yes | No |
| Type checked | Partly | No |
| Use for | Most queries | Vendor features, tuning |

```java
// JPQL - operates on entities, portable
@Query("select u from User u where u.status = :status")
List<User> byStatus(@Param("status") Status status);

// fetch join - defeats N+1
@Query("select d from Department d join fetch d.employees where d.id = :id")
Optional<Department> withEmployees(@Param("id") Long id);

// native SQL - database specific
@Query(value = "select * from users where age > :age", nativeQuery = true)
List<User> olderThan(@Param("age") int age);
```

Default to JPQL. Drop to native SQL only for window functions, CTEs, or a query the optimiser cannot express — and note it in a comment when you do.

**Modifying queries need a transaction:**
```java
@Modifying
@Transactional
@Query("update User u set u.status = :status where u.id = :id")
int updateStatus(@Param("id") Long id, @Param("status") Status status);
```
Without `@Transactional` — on the method or the calling service — you get `TransactionRequiredException`. Most notes omit this and the example simply fails at runtime.

**Projections** — do not load a whole entity to read two columns:
```java
public interface UserSummary {
    Long getId();
    String getName();
}
List<UserSummary> findByStatus(Status status);
```
On a wide table this cuts both query time and heap pressure substantially — you stop hydrating columns nobody reads.

**Dynamic queries without string building** — extend `JpaSpecificationExecutor`:
```java
Specification<User> spec = Specification.where(hasStatus(status)).and(nameContains(q));
Page<User> result = repository.findAll(spec, pageable);
```

## 29.15 Testing — the slices

| Annotation | Loads | For |
|---|---|---|
| (none) | Nothing | Pure unit tests |
| `@ExtendWith(MockitoExtension.class)` | Mockito only | Service logic with mocks |
| `@WebMvcTest` | Web layer only | Controllers, MockMvc |
| `@DataJpaTest` | JPA layer only | Repositories, in-memory DB |
| `@SpringBootTest` | Full context | Integration, **sparingly** |

**`@MockitoTest` does not exist.** It appears in a lot of circulated cheat sheets. To enable Mockito with JUnit 5 use `@ExtendWith(MockitoExtension.class)`. There is no `@MockitoTest` annotation in JUnit, Mockito or Spring.

**`@MockBean` is deprecated.** As of Boot 3.4, use **`@MockitoBean`** (and `@MockitoSpyBean`).

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock        UserRepository repository;
    @InjectMocks UserService    service;

    @Test
    void returnsUserWhenPresent() {
        given(repository.findById(1L)).willReturn(Optional.of(new User(1L, "Layla")));

        UserDto result = service.find(1L);

        assertThat(result.name()).isEqualTo("Layla");
        then(repository).should().findById(1L);
    }
}

@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired    MockMvc     mockMvc;
    @MockitoBean  UserService service;

    @Test
    void returns404WhenMissing() throws Exception {
        given(service.find(9L)).willThrow(new UserNotFoundException(9L));
        mockMvc.perform(get("/api/v1/users/9")).andExpect(status().isNotFound());
    }
}
```

**Most of your logic needs no Spring.** A service with constructor-injected dependencies is a plain Java class — test it with JUnit and Mockito, no context, milliseconds per test.

**H2 is not your database.** The in-memory default accepts SQL your production engine rejects. Use **Testcontainers** for anything with real queries.

**Testing rules:** Arrange–Act–Assert visibly separated · name tests after the behaviour, not the method · one reason to fail per test · no shared mutable state · the narrowest slice that proves the point.

## 29.16 Project structure

**Package by layer** (fine for a small service, stops scaling past roughly twenty endpoints):
```
com.example.demo/
├─ controller/    REST endpoints
├─ service/       business logic
├─ repository/    data access
├─ entity/        JPA entities
├─ dto/           request & response
├─ mapper/        entity <-> DTO
├─ config/        @Configuration
├─ exception/     domain exceptions
└─ DemoApplication.java
```

**Package by feature** (scales better):
```
com.example.demo/
├─ user/
│   ├─ UserController.java
│   ├─ UserService.java
│   ├─ UserRepository.java
│   ├─ User.java
│   └─ dto/
├─ order/
└─ shared/
    └─ config, exception, util
```
A change to users touches one directory, package-private visibility becomes meaningful, and extracting a feature into its own service later is a directory move rather than an archaeology project.

**Why DTOs are not optional**
- Entities leak your schema to every client
- Serialising a lazy association triggers a query — or an exception
- Bidirectional relationships serialise into **infinite recursion** (people reach for `@JsonIgnore`; the real fix is not serialising entities at all)
- You cannot evolve a column without breaking the API contract

**Practices worth enforcing in review:** constructor injection everywhere · `@Transactional` on services only · `readOnly = true` as the class default, overridden on writes · DTOs at every boundary · one global `@RestControllerAdvice` · no business logic in entities or controllers · every collection endpoint paginated · configuration externalised, secrets never committed.

## 29.17 Spring Security — the filter chain

**Authentication vs authorization**

| | Authentication | Authorization |
|---|---|---|
| Question | Who are you? | What may you do? |
| Failure code | **401 Unauthorized** | **403 Forbidden** |
| Produces | An `Authentication` object | A granted/denied decision |
| Runs | Early in the chain | After identity is known |

**The two status codes get swapped constantly.** 401 = I do not know who you are. 403 = I know exactly who you are and you still may not do this. Returning 403 for an expired token sends clients down the wrong recovery path.

**The chain**
```
SecurityContextPersistenceFilter
  -> Authentication filters
    -> ExceptionTranslationFilter
      -> AuthorizationFilter
```
`ExceptionTranslationFilter` sits **above** authorization precisely so it can catch the access-denied exception and turn it into a 401 or 403 response.

**The modern configuration**
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

  @Bean
  SecurityFilterChain chain(HttpSecurity http) throws Exception {
    return http
      .csrf(CsrfConfigurer::disable)                 // stateless API only
      .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
      .authorizeHttpRequests(auth -> auth
          .requestMatchers("/api/auth/**").permitAll()
          .requestMatchers("/api/admin/**").hasRole("ADMIN")
          .anyRequest().authenticated())
      .build();
  }
}
```

**What changed in Spring Security 6**

| Removed / renamed | Use instead |
|---|---|
| `WebSecurityConfigurerAdapter` | A `SecurityFilterChain` bean |
| `authorizeRequests()` | `authorizeHttpRequests()` |
| `antMatchers()` / `mvcMatchers()` | `requestMatchers()` |
| `@EnableGlobalMethodSecurity` | `@EnableMethodSecurity` |

**The single biggest source of broken tutorials:** `WebSecurityConfigurerAdapter` was **removed** in Security 6, which ships with Boot 3. Any example extending it will not compile.

**Passwords**
```java
@Bean
PasswordEncoder passwordEncoder() {
    // delegating encoder writes a {bcrypt} prefix, so you can migrate algorithms later
    return PasswordEncoderFactories.createDelegatingPasswordEncoder();
}
```
**Never, in any environment:** `NoOpPasswordEncoder` stores plaintext.

**CSRF, decided properly:** disable for a stateless API authenticated by a bearer token — there is no ambient credential for a browser to attach. **Keep it enabled** for cookies, sessions or cookie-based JWT. `csrf().disable()` gets copied into session-based apps constantly, and that is a real vulnerability.

## 29.18 JWT in depth

**A JWT is signed, not encrypted.** Anyone holding it can read every claim. Paste any token into a decoder and the payload appears in plain text — never put a password or anything you would not print on a postcard into the claims.

**Claims worth setting**

| Claim | Meaning | Why |
|---|---|---|
| `sub` | Subject | Who the token is about |
| `iat` | Issued at | Age checks |
| `exp` | Expiry | **Mandatory** — keep it short |
| `iss` | Issuer | Reject foreign tokens |
| `aud` | Audience | Reject tokens meant for another service |
| `jti` | Token id | Enables targeted revocation |

**Validate `iss` and `aud`.** In a microservice estate, a token issued for service A will otherwise be accepted by service B.

**A verification filter**
```java
@Component
public class JwtAuthFilter extends OncePerRequestFilter {

  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res,
      FilterChain chain) throws ServletException, IOException {

    String h = req.getHeader("Authorization");
    if (h != null && h.startsWith("Bearer ")) {
      try {
        Claims c = jwtService.verify(h.substring(7));
        SecurityContextHolder.getContext().setAuthentication(toAuthentication(c));
      } catch (JwtException ex) {
        // empty context - the chain returns 401
      }
    }
    chain.doFilter(req, res);
  }
}
```

**Extend `OncePerRequestFilter`.** A plain `Filter` can run twice on forwards and async dispatches, re-parsing the token and occasionally clobbering the security context.

**Access vs refresh**

| | Access | Refresh |
|---|---|---|
| Lifetime | 5–15 min | Days |
| Sent on | Every request | Renewal only |
| Stored | Memory | HttpOnly cookie |
| If stolen | Limited window | Serious |

**The revocation problem:** a signed token is valid until it expires. Instant revocation needs server state — a `jti` blocklist. Short expiry mitigates; it does not solve.

**Verification rules:** pin the expected algorithm, never trust the token's `alg` header · reject `alg: none` outright · verify the signature **before** reading any claim · check `exp`, `iss` and `aud` · allow a small clock skew (30–60 s), not minutes.

**The classic attack:** a library that reads `alg` from the token and picks a verifier accordingly can be handed `none`, or an HS256 token signed with the public RSA key. Configure the algorithm on your side.

**Secret handling:** HS256 needs a key of at least 256 bits · keep the key in environment or a vault, never in `application.yml` · prefer RS256 when a separate service issues tokens (verifiers need only the public key) · rotate keys with a `kid` header.

## 29.19 Method security

```java
@Configuration
@EnableMethodSecurity   // Boot 3.x / Security 6
public class MethodSecurityConfig { }
```

| Annotation | Expression | Note |
|---|---|---|
| `@PreAuthorize` | Full SpEL | **Preferred** |
| `@PostAuthorize` | SpEL on `returnObject` | Runs **after** — the work is already done |
| `@PreFilter` / `@PostFilter` | Filters collections | Costly on large results |
| `@Secured` | Role names only | Legacy |
| `@RolesAllowed` | Role names only | Jakarta standard |

**`@PostAuthorize` is a late check.** The method has already executed and may have already written to the database. Use it for reads, not for anything with side effects.

```java
@PreAuthorize("hasRole('ADMIN')")
void deleteUser(Long id) { ... }

// ownership check - the common real requirement
@PreAuthorize("hasRole('ADMIN') or #id == authentication.principal.id")
UserDto get(@P("id") Long id) { ... }

// delegate to a bean for anything non-trivial
@PreAuthorize("@accessPolicy.canEdit(#orderId, authentication)")
void edit(Long orderId) { ... }
```

**Roles vs authorities — the prefix trap**

| Expression | Actually checks |
|---|---|
| `hasRole('ADMIN')` | authority `ROLE_ADMIN` |
| `hasAuthority('ADMIN')` | authority `ADMIN` |
| `hasAuthority('ROLE_ADMIN')` | authority `ROLE_ADMIN` |

`hasRole` silently prepends `ROLE_`; `hasAuthority` does not. Mixing the two produces a 403 that looks like a configuration bug and is really a naming bug.

**Layering the checks:** URL rules as a coarse gate · method security as the real rule, close to the logic · **data filtering in the query itself** — never fetch then discard · deny by default with `anyRequest().authenticated()` last.

**Filter in the query.** Loading every order then removing the ones the user cannot see leaks through timing and pagination counts, and it does not scale. Put the tenant or owner condition in the `where` clause.

## 29.20 Logging

```
Your code -> SLF4J (facade) -> Logback (implementation) -> Console or file
```

| Level | Use for |
|---|---|
| ERROR | Something failed and needs a human |
| WARN | Recovered, but suspicious |
| INFO | Business milestones — order placed |
| DEBUG | Developer detail, off in production |
| TRACE | Very fine detail, rarely enabled |

**There is no FATAL in SLF4J.** Cheat sheets list it because Log4j has it. SLF4J's API stops at ERROR — `log.fatal(...)` **will not compile**.

**Parameterised, always**
```java
// good - argument only formatted if the level is on
log.debug("Loaded order {} for customer {}", orderId, customerId);

// bad - string built even when DEBUG is off
log.debug("Loaded order " + orderId + " for " + customerId);

// exceptions: pass as the LAST argument, no placeholder
log.error("Failed to place order {}", orderId, ex);
```
`log.error("failed: " + ex.getMessage())` **throws away the stack trace**. Pass the exception object itself as the final argument.

**Correlation with MDC**
```java
@Component
public class MdcFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res,
      FilterChain chain) throws ServletException, IOException {

    String id = Optional.ofNullable(req.getHeader("X-Request-Id"))
        .orElseGet(() -> UUID.randomUUID().toString());
    MDC.put("requestId", id);
    try {
      chain.doFilter(req, res);
    } finally {
      MDC.clear();   // MANDATORY
    }
  }
}
```

**Clear the MDC in a `finally` block.** MDC is thread-local and servlet threads are pooled and reused. Forget to clear it and the next request served by that thread inherits the previous request's id — **worse than having no correlation id at all, because the logs now actively lie**.

**Production rules:** log in JSON when an aggregator will parse it · a correlation id on every line · never log passwords, tokens, card numbers or personal data · no `System.out.println` (it bypasses levels, format and rotation) · log the decision, not the whole object graph · keep `show-sql` off in production.

**GDPR is not an abstraction:** an email address in a log line is personal data that has now been replicated to every downstream log store and backup you own.

Change levels without redeploying via Actuator's `/actuator/loggers`.

## 29.21 Actuator and observability

| Endpoint | Shows |
|---|---|
| `/actuator/health` | Aggregated health of the app and its dependencies |
| `/actuator/info` | Build and version metadata |
| `/actuator/metrics` | Micrometer metrics by name |
| `/actuator/prometheus` | Metrics in scrape format |
| `/actuator/loggers` | Read and change log levels live |
| `/actuator/env` | Resolved configuration — **sensitive** |

**Only two are exposed by default over HTTP:** `health` and `info`, and nothing else. Notes showing a long list of live endpoints have quietly assumed `exposure.include=*` was set.

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: when-authorized
      probes:
        enabled: true
  server:
    port: 9090        # separate management port
```

**Never `include: *`.** `/actuator/env` prints your resolved configuration — unauthenticated, that is a credential dump.

**Health for orchestrators**

| Probe | Path | If it fails |
|---|---|---|
| Liveness | `/actuator/health/liveness` | Container is **restarted** |
| Readiness | `/actuator/health/readiness` | Removed from load balancing |

**Using the same endpoint for both is a real outage.** The default `/health` includes the database. Point liveness at it and a brief database blip restarts every pod — turning a recoverable failure into a full outage.

**A custom indicator** — keep it fast, health is polled every few seconds:
```java
@Component
class PaymentGatewayHealth implements HealthIndicator {
  @Override
  public Health health() {
    return gateway.ping()
        ? Health.up().build()
        : Health.down().withDetail("gateway", "unreachable").build();
  }
}
```

**Metrics with Micrometer**
```java
@Service
public class OrderService {
  private final Counter placed;

  OrderService(MeterRegistry registry) {
    this.placed = registry.counter("orders.placed");
  }

  @Timed(value = "orders.place")
  public void place(Order order) {
    placed.increment();
  }
}
```

**Never tag with an unbounded value.** A `userId` tag creates one time series per user. That cardinality explosion takes down monitoring.

**The three signals:** metrics (numbers over time — cheap, aggregate, good for alerting) · logs (discrete events with detail — good for explaining one failure) · traces (one request across services — good for finding which hop is slow).

## 29.22 API documentation with springdoc-openapi

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <!-- v2.x is required for Boot 3 -->
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.x.x</version>
</dependency>
```
UI at `/swagger-ui.html`, raw spec at `/v3/api-docs`.

**Two dead ends people hit:** **Springfox is unmaintained** and does not work with Boot 3 — do not start there. And **springdoc 1.x targets Boot 2**; on Boot 3 it fails at startup because of the jakarta move. Use springdoc **2.x**.

```java
@Tag(name = "Orders", description = "Order lifecycle")
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

  @Operation(summary = "Place an order")
  @ApiResponses({
      @ApiResponse(responseCode = "201", description = "Created"),
      @ApiResponse(responseCode = "400", description = "Invalid payload"),
      @ApiResponse(responseCode = "409", description = "Duplicate order")
  })
  @PostMapping
  OrderDto place(@Valid @RequestBody PlaceOrder req) { ... }
}
```

**Most of it is free:** paths and verbs come from the mappings, schemas from your DTO types, required fields from the validation annotations, status codes from `@ResponseStatus`.

**Document the security scheme** — without it, testers cannot attach a token from the Swagger page:
```java
@Configuration
@SecurityScheme(name = "bearerAuth", type = SecuritySchemeType.HTTP,
                scheme = "bearer", bearerFormat = "JWT")
public class OpenApiConfig {
  @Bean
  OpenAPI api() {
    return new OpenAPI().info(new Info().title("Orders API").version("v1"));
  }
}
```

**Production posture** — public Swagger is reconnaissance; it lists every endpoint, parameter and schema you have:
```yaml
springdoc:
  api-docs: { enabled: false }
  swagger-ui: { enabled: false }
```

**The underused trick:** commit the generated `openapi.json` and diff it in the pipeline — that turns "we broke a client" into a failed build.

## 29.23 Aspect-Oriented Programming

| Term | Means |
|---|---|
| Aspect | The class holding the cross-cutting logic |
| Join point | A point where advice could apply — in Spring, a method call |
| Pointcut | An expression selecting which join points |
| Advice | The code that runs at a matched join point |
| Weaving | Wiring advice in — at runtime, via a proxy |

**Spring AOP is method-level only.** Full AspectJ can advise field access and constructors; Spring AOP intercepts **public method calls on Spring beans** and nothing else — which covers almost every real need.

| Annotation | Runs |
|---|---|
| `@Before` | Before the method |
| `@AfterReturning` | Only on success |
| `@AfterThrowing` | Only on exception |
| `@After` | Always, like a `finally` block |
| `@Around` | Wraps the call — full control |

**`@Around` must call `proceed()`.** Forget `pjp.proceed()` and the target method never runs — the application silently does nothing and returns null.

```java
@Aspect
@Component
public class TimingAspect {

  @Around("@annotation(com.example.Timed)")
  public Object time(ProceedingJoinPoint pjp) throws Throwable {
    long start = System.nanoTime();
    try {
      return pjp.proceed();
    } finally {
      log.info("{} took {} ms", pjp.getSignature().toShortString(),
          (System.nanoTime() - start) / 1_000_000);
    }
  }
}
```

**Pointcut forms**
```java
@annotation(com.example.Timed)                  // by annotation - clearest
execution(* com.example.service..*(..))         // every public method in a package
within(com.example.service..*)                  // anything in a package tree
@within(org.springframework.stereotype.Service) // beans annotated @Service
```
**Annotation pointcuts age best** — a package-pattern pointcut silently stops matching the day someone moves a class.

**The limits you must know:** self-invocation bypasses the proxy entirely · private and final methods cannot be advised · an object created with `new` has no proxy · `final` classes cannot be subclassed by CGLIB.

**How the proxy is chosen**

| Case | Proxy |
|---|---|
| Class implements an interface | CGLIB in Boot (subclass) |
| No interface | CGLIB (subclass) |
| `proxyTargetClass = false` | JDK dynamic proxy |

**Boot changed the default.** Plain Spring prefers JDK proxies when an interface exists; Boot sets `proxyTargetClass=true`, so you get CGLIB subclass proxies by default. That is why a `final` service class breaks in a Boot app even though the documentation said interfaces were enough.

**This is why `@Transactional` silently fails** — it is not a transaction bug, it is the proxy limitation above. Same cause, same fix: call through another bean, or inject a self-reference.

## 29.24 Filters vs interceptors

```
Request -> Filter -> DispatcherServlet -> Interceptor -> Controller
```

| | Filter | Interceptor |
|---|---|---|
| Level | Servlet container | Spring MVC |
| Sees | Every request, **including static** | Only mapped handlers |
| Knows the handler | No | **Yes** |
| Can modify the body | Yes, with wrappers | Awkward |
| Runs | First | After filters |

```java
@Component
public class RequestLogFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res,
      FilterChain chain) throws ServletException, IOException {
    long start = System.currentTimeMillis();
    try {
      chain.doFilter(req, res);         // must be called
    } finally {
      log.info("{} {} -> {} ({} ms)", req.getMethod(), req.getRequestURI(),
          res.getStatus(), System.currentTimeMillis() - start);
    }
  }
}
```

**`postHandle` is not a `finally` block.** If the handler throws, `postHandle` is **skipped** — only `afterCompletion` runs. Cleanup placed in `postHandle` leaks on exactly the requests that failed.

**Choosing:** filter for security, CORS, compression, correlation ids and raw request logging · interceptor when you need to know which controller method was matched, or a handler annotation · neither if it is business logic — that belongs in a service.

**The body-reading trap**
```java
// the request stream can only be read ONCE
String body = req.getReader()...   // controller now gets nothing

// wrap it so the body can be replayed
ContentCachingRequestWrapper wrapped = new ContentCachingRequestWrapper(req);
chain.doFilter(wrapped, res);
```
Read the body in a filter without wrapping and the controller receives an empty stream. Jackson then reports a malformed payload — and the client's payload was perfectly fine.

## 29.25 Application events

```java
public record OrderPlaced(Long orderId, String email) {}

@Service
public class OrderService {
  private final ApplicationEventPublisher events;

  @Transactional
  public void place(PlaceOrder req) {
    Order saved = repository.save(toOrder(req));
    events.publishEvent(new OrderPlaced(saved.getId(), req.email()));
  }
}

@Component
public class OrderListeners {
  @EventListener
  public void sendConfirmation(OrderPlaced event) { ... }

  @EventListener(condition = "#event.orderId > 1000")
  public void audit(OrderPlaced event) { ... }
}
```

Since Spring 4.2 **any object works as an event** — extending `ApplicationEvent` is legacy, and a record is the natural choice.

**Same thread, same transaction.** A plain `@EventListener` runs **inline**. A slow listener slows the publisher, and an exception in the listener propagates back and can roll the publisher's transaction back.

**The transactional listener — the one that matters**
```java
@Component
public class OrderNotifier {
  @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
  public void onPlaced(OrderPlaced event) {
    // runs only once the order is durably committed
    mailer.confirm(event.email(), event.orderId());
  }
}
```

**The bug this prevents:** with a plain listener the email is sent **inside** the transaction. If the transaction then rolls back, the order does not exist — but the customer already has a confirmation email, and you cannot un-send it. `AFTER_COMMIT` is the correct default for anything with an external side effect.

| Phase | Runs |
|---|---|
| `BEFORE_COMMIT` | Before commit — can still veto |
| `AFTER_COMMIT` | **Default** — after durable commit |
| `AFTER_ROLLBACK` | Only when rolled back |
| `AFTER_COMPLETION` | Either outcome |

**Do not write to the database in `AFTER_COMMIT`** — the transaction is finished. A repository call there either joins no transaction or silently opens a new one. If you need a follow-up write, use `REQUIRES_NEW` explicitly.

**Async means the failure disappears.** An exception in an `@Async` listener goes to the executor's uncaught handler — the publisher never learns of it.

**When events are the wrong tool:** anything that *must* happen (use a broker with durability and retries) · anything crossing a process boundary · anything needing ordering guarantees · anything a reader must trace to understand the flow.

**Interview answer:** "In-process events are good for decoupling optional side effects within one service. For anything that must not be lost, I use a broker — events give no delivery guarantee and vanish on restart."

## 29.26 Transactions in depth

```java
@Service
@Transactional(readOnly = true)           // class default
public class OrderService {

    @Transactional                        // writes override
    public OrderDto place(PlaceOrder req) {
        Order order = repository.save(toOrder(req));
        inventory.reserve(order);         // same transaction
        return mapper.toDto(order);
    }
}
```

**The rollback rule people get wrong**

| Thrown | Rolls back? |
|---|---|
| `RuntimeException` | Yes |
| `Error` | Yes |
| **Checked `Exception`** | **No** |

```java
@Transactional(rollbackFor = Exception.class)
public void transfer() throws InsufficientFunds { ... }
```

**Half-written data, no error visible.** Throw a checked exception from a transactional method and Spring **commits everything written before it**. The caller sees a failure, the database sees a success. This is the most damaging default in the framework.

**Propagation**

| Mode | Behaviour | Use when |
|---|---|---|
| `REQUIRED` | Join, or start one (**default**) | Almost always |
| `REQUIRES_NEW` | Suspend caller, start a fresh one | Audit rows that must survive a rollback |
| `SUPPORTS` | Join if present, else none | Read helpers |
| `NOT_SUPPORTED` | Suspend, run without | Long non-transactional work |
| `MANDATORY` | Must already be in one, else throw | Internal-only helpers |
| `NEVER` | Throw if one exists | Guard rails |
| `NESTED` | Savepoint inside the caller | Partial rollback, JDBC only |

**`REQUIRES_NEW` takes a second connection.** The outer transaction stays open while the inner one runs, so both hold a connection. A loop calling a `REQUIRES_NEW` method per row will exhaust a pool of ten and then deadlock waiting on itself.

**Isolation**

| Level | Prevents |
|---|---|
| `READ_UNCOMMITTED` | Nothing |
| `READ_COMMITTED` | Dirty reads |
| `REPEATABLE_READ` | + non-repeatable reads |
| `SERIALIZABLE` | + phantom reads |

**Leave it at the default.** `DEFAULT` uses the database's own setting — `READ_COMMITTED` on PostgreSQL, `REPEATABLE_READ` on MySQL. Raising it costs concurrency; solve write conflicts with **optimistic locking** instead.

**Self-invocation, one last time**
```java
@Service
public class BatchService {
    public void runAll(List<Row> rows) {
        rows.forEach(this::handle);   // NO transaction
    }

    @Transactional
    public void handle(Row row) { ... }
}
```
No exception, no warning — the annotation is simply ignored because the call never left the object. Move `handle` into its own bean and inject it. **If you take one thing from these notes, take this.**

## 29.27 Caching in depth

| Annotation | Runs the method? | Writes cache? |
|---|---|---|
| `@Cacheable` | Only on a miss | On a miss |
| `@CachePut` | Always | Always |
| `@CacheEvict` | Always | Removes |
| `@Caching` | Combines several | — |

```java
@Service
public class ProductService {

    @Cacheable(value = "products", key = "#id", unless = "#result == null")
    public Product find(Long id) { ... }

    @CachePut(value = "products", key = "#product.id")
    public Product update(Product product) { ... }

    @CacheEvict(value = "products", key = "#id")
    public void delete(Long id) { ... }
}
```

**`@Cacheable` caches nulls.** By default a null return value is stored, so every later lookup returns a cached "not found". Add `unless = "#result == null"` unless you specifically want negative caching.

**Do not put `@Cacheable` on an update** — it would skip the update entirely on a cache hit. `@CachePut` exists precisely for the write path.

**The default is not Caffeine.** With no provider on the classpath, Boot uses a **`ConcurrentHashMap`-based cache with no eviction and no TTL** — it grows until the heap runs out. Caffeine is the default only once you add its dependency.

```yaml
# Caffeine - single instance, in process
spring:
  cache:
    type: caffeine
    cache-names: products,users
    caffeine:
      spec: maximumSize=1000,expireAfterWrite=10m

# Redis - shared across instances
spring:
  cache:
    type: redis
  data:
    redis: { host: redis, port: 6379 }
```

**TTL is not part of the abstraction.** Spring's cache API has no expiry concept — every TTL is provider configuration, which is why swapping provider means rewriting it.

| | Caffeine | Redis |
|---|---|---|
| Scope | One JVM | All instances |
| Latency | Nanoseconds | A network hop |
| Consistency | Per instance | Shared |
| Survives restart | No | Yes |
| Values | Any object | Must serialise |

**The stale-across-instances bug:** with a local cache and three instances, evicting on one leaves the other two serving stale values. Users see the update, refresh, and watch it vanish.

**Rules:** cache what is read often and changes rarely · always set a maximum size and a TTL · evict on write, in the same service method · keep cached values small and serialisable · never cache anything permission-dependent without the user in the key · monitor the hit ratio — a cache below ~70% is usually pure cost.

## 29.28 Scheduling and async

```java
@Configuration @EnableScheduling
class SchedulingConfig { }

@Component
public class Jobs {
    @Scheduled(fixedDelay = 60_000)
    void pollQueue() { ... }

    @Scheduled(cron = "0 0 2 * * *", zone = "Africa/Cairo")
    void nightlyReport() { ... }
}
```

| Setting | Next run starts |
|---|---|
| `fixedRate` | Every N ms from the previous **start** |
| `fixedDelay` | N ms after the previous **finish** |
| `cron` | At clock times |

**`fixedRate` can overlap itself.** If the task takes longer than the interval, runs queue up behind each other on the single scheduler thread. `fixedDelay` is the safer default when duration varies.

**The scheduler is single-threaded by default.** One thread runs every scheduled method in the application — a job that takes ten minutes delays every other job for ten minutes. Configure `spring.task.scheduling.pool.size`.

**Spring cron has SIX fields**
```
// sec min hour dom month dow
"0 0 2 * * *"        // 02:00 daily
"0 */15 * * * *"     // every 15 min
"0 0 9 * * MON-FRI"  // 09:00 weekdays
```
Unix cron has **five** fields starting at minutes. Spring adds a seconds field at the front. Paste a five-field expression from crontab and everything shifts by one unit — your daily job becomes hourly.

**`@Async`**
```java
@Configuration @EnableAsync
class AsyncConfig { }

@Service
public class ReportService {
    @Async
    public CompletableFuture<Report> build(Long id) {
        return CompletableFuture.completedFuture(generate(id));
    }
}
```

**A `void` `@Async` swallows every exception.** With a void return there is nothing to carry the failure — it goes to the uncaught handler and is logged and forgotten. Return `CompletableFuture`, or register an `AsyncUncaughtExceptionHandler`.

**Size the executors yourself** — the unbounded default (`SimpleAsyncTaskExecutor` in older Boot versions) creates a new thread per call and never pools:
```yaml
spring:
  task:
    execution:
      pool: { core-size: 8, max-size: 32, queue-capacity: 200 }
    scheduling:
      pool: { size: 4 }
```

**Scheduling across multiple instances.** Three replicas means the nightly job runs **three times** — nothing in `@Scheduled` coordinates instances. Either make the job idempotent, take a distributed lock (ShedLock is the usual choice), or move the trigger out entirely.

## 29.29 Resilience

**Timeouts first**
```java
@Bean
RestClient paymentClient(RestClient.Builder builder) {
  ClientHttpRequestFactorySettings settings = ClientHttpRequestFactorySettings.DEFAULTS
      .withConnectTimeout(Duration.ofSeconds(2))
      .withReadTimeout(Duration.ofSeconds(5));

  return builder
      .requestFactory(ClientHttpRequestFactories.get(settings))
      .baseUrl("https://payments.internal")
      .build();
}
```

**The default is no timeout at all.** An HTTP client with no read timeout waits forever. Every request thread that touches that dependency parks, the pool fills, and your service stops answering anything — **including endpoints that never call it**. This is the single most common cause of a cascading outage.

**The failure ladder, in this order**

| Layer | Protects against |
|---|---|
| Timeout | Waiting forever |
| Retry | Transient blips |
| Circuit breaker | Hammering something already down |
| Bulkhead | One dependency eating every thread |
| Fallback | Degrading instead of failing |

A retry without a timeout multiplies the hang. A circuit breaker without a timeout never opens, because nothing ever *fails* — it just hangs.

```java
@Retry(name = "payments", fallbackMethod = "queueForLater")
@CircuitBreaker(name = "payments")
public Receipt charge(Payment payment) {
  return client.post().body(payment).retrieve().body(Receipt.class);
}

Receipt queueForLater(Payment p, Exception ex) {
  outbox.save(p);
  return Receipt.pending();
}
```

```yaml
resilience4j:
  retry:
    instances:
      payments:
        max-attempts: 3
        wait-duration: 200ms
        enable-exponential-backoff: true
        enable-randomized-wait: true
```

**Add jitter.** Without randomisation every client retries at the same instant — the recovering service is hit by a synchronised wave and falls over again, a thundering herd of your own making.

**Only retry idempotent operations.** Retrying a `POST /charge` that actually succeeded but timed out on the response charges the customer twice.

**Circuit breaker states:** CLOSED (calls pass) → OPEN (fail fast) → HALF-OPEN (probe) → CLOSED (recovered). **Failing fast is the point** — an immediate error lets the caller fall back or shed load; a five-second hang gives it nothing and consumes a thread while doing so.

**Practices:** a timeout on every remote call (HTTP, database, cache, broker) · client timeouts shorter than the caller's own budget · retry only idempotent operations, with backoff and jitter · a separate thread pool per dependency where it matters · decide what "degraded" looks like before you need it · set `server.shutdown=graceful`.

## 29.30 Performance

**The usual order of impact**

| Rank | Cause | Typical fix |
|---|---|---|
| 1 | N+1 queries | Fetch join or `@EntityGraph` |
| 2 | Missing index | Index the filtered/joined column |
| 3 | Fetching too much | Projections, pagination |
| 4 | Connection pool too small | Size it to the workload |
| 5 | No caching on hot reads | Cache with a TTL |
| 6 | Row-by-row writes | JDBC batching |

**Not the JVM.** People reach for GC flags and thread tuning first. In a typical CRUD service the JVM is rarely the constraint — the query plan is.

**Finding N+1** — one list endpoint producing 51 statements for 50 rows is the signature:
```yaml
spring:
  jpa:
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        generate_statistics: true
```
Better in a real project: **assert the query count in a test**. A tool like datasource-proxy fails the build when an endpoint's statement count regresses.

**Connection pool sizing**
```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 10
      connection-timeout: 3000
      max-lifetime: 1800000
      leak-detection-threshold: 20000
```
**Bigger is not faster.** HikariCP defaults to 10. Raising it to 200 does not help — the database has a finite number of cores, and beyond that you add context switching and lock contention. Total pool size **across all instances** must stay under the server's `max_connections`, or new instances simply fail to start.

**Batch writes**
```yaml
spring:
  jpa:
    properties:
      hibernate:
        jdbc: { batch_size: 50 }
        order_inserts: true
        order_updates: true
```
**`IDENTITY` disables batching.** With `GenerationType.IDENTITY` Hibernate must execute each insert to learn the generated id, so it cannot batch them. Use a **SEQUENCE** generator when bulk inserts matter.

**Measure properly:** load test against production-shaped data volume · look at **p95 and p99**, never the average · profile before changing anything (JFR, async-profiler) · change one thing at a time · re-measure, because some fixes make things worse.

## 29.31 File upload and download

```java
@PostMapping(value = "/files", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
@ResponseStatus(HttpStatus.CREATED)
FileDto upload(@RequestParam("file") MultipartFile file) {
    if (file.isEmpty()) throw new BadRequestException("file is empty");
    return storage.store(file);
}
```

**The defaults are small:** Boot caps a single file at **1MB** and the whole request at **10MB**. Uploading a 4MB photo fails out of the box with a confusing `MaxUploadSizeExceededException`.

```yaml
spring:
  servlet:
    multipart:
      max-file-size: 10MB
      max-request-size: 25MB
      file-size-threshold: 2MB
```
Add a handler for `MaxUploadSizeExceededException` in your advice, or an oversized upload returns a raw 500 with no useful message.

**Never trust the filename** — `getOriginalFilename()` is client input, `../` included:
```java
// DANGEROUS - path traversal
Path target = Paths.get("uploads/" + file.getOriginalFilename());
// name = "../../etc/cron.d/evil" writes outside uploads/

// SAFE - generate your own name, keep only the extension
String ext = StringUtils.getFilenameExtension(file.getOriginalFilename());
String safeName = UUID.randomUUID() + (ext == null ? "" : "." + ext);

Path base   = Paths.get(uploadDir).toAbsolutePath().normalize();
Path target = base.resolve(safeName).normalize();
if (!target.startsWith(base)) throw new BadRequestException();
file.transferTo(target);
```

**Validate the content:** enforce the server size limit · do **not** trust `getContentType()` — it is client-supplied · sniff the real type from magic bytes if it matters · allow-list extensions, never deny-list · store outside the served directory.

**Content-Type is a claim, not a fact.** A client can label an executable as `image/png`. If a browser will later render the file, that mislabel becomes stored XSS.

**Authorise the download, not just the upload.** Sequential ids plus no ownership check is the classic direct-object-reference leak: increment the id, read someone else's document.

**Where to put the bytes:** local disk dies with the container; database BLOBs bloat backups. **Object storage is the default** — with pre-signed URLs the client uploads straight to it and your service never touches the bytes.

## 29.32 Containerising

**A layered Dockerfile**
```dockerfile
# --- build ---
FROM eclipse-temurin:21-jdk AS build
WORKDIR /src
COPY pom.xml .
RUN mvn -B dependency:go-offline
COPY src ./src
RUN mvn -B clean package -DskipTests
RUN java -Djarmode=layertools -jar target/*.jar extract

# --- run ---
FROM eclipse-temurin:21-jre
WORKDIR /app
RUN useradd -r -u 1001 appuser
COPY --from=build /src/dependencies/ ./
COPY --from=build /src/spring-boot-loader/ ./
COPY --from=build /src/application/ ./
USER appuser
EXPOSE 8080
ENTRYPOINT ["java", "org.springframework.boot.loader.launch.JarLauncher"]
```

**Copying the fat jar wastes your CI time.** `COPY target/app.jar` puts 60MB of unchanged dependencies in the same layer as your 200KB of code, so every commit re-pushes all of it.

**Or skip the Dockerfile entirely** — Cloud Native Buildpacks produce a layered, non-root image with a tuned JVM:
```bash
mvn spring-boot:build-image
```

**Memory in a container** — the JVM reads cgroup limits since Java 10:
```bash
docker run -m 512m \
  -e JAVA_TOOL_OPTIONS="-XX:MaxRAMPercentage=70" \
  -e SPRING_PROFILES_ACTIVE=prod \
  orders:1.4.0
```
**Heap is not the whole footprint.** Metaspace, thread stacks, code cache and direct buffers live outside the heap. Set `MaxRAMPercentage` around **70–75**, not 100 — otherwise the container is killed by the OOM killer with no Java stack trace to explain it.

**Image rules:** multi-stage, no JDK/Maven/source in the final image · JRE base, not JDK · run as a non-root user · tag with a version (`latest` is not one) · scan in CI and rebuild for base-image CVEs · **no secrets** — a secret removed in a later layer stays in the image history.

## 29.33 Delivery and deployment

**Stages:** Commit → Build & test → Scan → Image → Staging → Production.

**Build once, promote the artefact.** Rebuilding per environment means the thing you tested is not the thing you shipped. The image that passed staging must be the **exact image** that reaches production — same digest, different configuration.

```yaml
name: ci
on: { push: { branches: [main] } }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '21', distribution: temurin, cache: maven }
      - run: mvn -B verify
      - run: mvn -B spring-boot:build-image
```

**Zero-downtime requires two things**
```yaml
# 1. drain in-flight requests on shutdown
server:
  shutdown: graceful
spring:
  lifecycle:
    timeout-per-shutdown-phase: 30s

# 2. tell the orchestrator when you are ready
management:
  endpoint:
    health:
      probes: { enabled: true }
```

**The default kills in-flight requests.** Without `shutdown: graceful`, SIGTERM stops the server immediately and every request being served right then fails. Users experience a rolling deploy as a burst of errors — and it is **one line of configuration**.

**Database changes:** migrations run as part of the deploy (Flyway or Liquibase) · every migration is **additive first** · old and new code must both work against the schema during a rolling deploy · drop columns in a later release.

**Never rename in one step.** During a rolling deploy both versions run at once. Rename a column and the old pods break instantly. Add the new column, backfill, switch reads, then drop — **three releases, zero downtime**.

| Strategy | How | Rollback |
|---|---|---|
| Rolling | Replace instances gradually | Roll forward or back |
| Blue-green | Two environments, switch traffic | Instant |
| Canary | Small share first, widen | Stop at the first sign |

**Release checklist:** migrations backward compatible · graceful shutdown on, readiness probe wired · config and secrets externalised · resource limits set on the container · dashboards and alerts exist **before** the release · a rollback that has actually been tested.

## 29.34 Corrections — what most cheat sheets get wrong

| Commonly seen | Correct | Consequence |
|---|---|---|
| `@MockitoTest` | `@ExtendWith(MockitoExtension.class)` | **The annotation does not exist — will not compile** |
| `@MockBean` | `@MockitoBean` | Deprecated since Boot 3.4 |
| `@PreDestrory` | `@PreDestroy` | Misspelling — the callback never fires |
| `@Colmm` | `@Column` | Misspelling |
| "Inempotent" | **Idempotent** | Wrong term in an interview answer |
| `@Modifying` alone | `@Modifying` + `@Transactional` | `TransactionRequiredException` at runtime |
| Boot 3.2.0 examples | Current GA (3.5.x) | Outdated dependency and Java baseline |
| `@Autowired` on sole constructor | Optional since Spring 4.3 | Redundant, not wrong |
| `javax.annotation` | `jakarta.annotation` | Wrong package in Boot 3.x |
| `WebSecurityConfigurerAdapter` | A `SecurityFilterChain` bean | **Removed in Security 6 — will not compile** |
| `authorizeRequests` / `antMatchers` | `authorizeHttpRequests` / `requestMatchers` | Renamed in Security 6 |
| `@EnableGlobalMethodSecurity` | `@EnableMethodSecurity` | Renamed in Security 6 |
| Springfox, or springdoc 1.x | springdoc-openapi **2.x** | Neither works on Boot 3 |
| "Caffeine is the default cache" | `ConcurrentHashMap`, **no TTL** | The real default never evicts |
| SLF4J FATAL level | ERROR is the maximum | `log.fatal` does not compile |
| Unix 5-field cron | Spring cron has **6** fields | Everything shifts by one unit |
| "All actuator endpoints exposed" | Only `health` and `info` | The rest need opting in |
| Checked exception rolls back | Only unchecked, unless `rollbackFor` | Silent partial commits |

**Two of these do not compile at all.** `WebSecurityConfigurerAdapter` and `log.fatal` are not "outdated style" — they no longer exist. Anything showing them was written for an older major version and has not been checked since.

## 29.35 The proxy rule, in one place

These annotations are **all applied by a proxy**, and all of them are **silently skipped on self-invocation**:

`@Transactional` · `@Cacheable` · `@CacheEvict` · `@Async` · `@PreAuthorize` · `@Retry` · any `@Aspect` advice

**One cause, one fix.** Interviewers ask about this through `@Transactional`, but it is really a question about Spring's **proxy model**. Saying so — and naming the other annotations it affects — is a noticeably stronger answer than reciting the transaction case alone.

## 29.36 Defaults worth memorising

| Thing | Default |
|---|---|
| Hikari pool size | 10 |
| Scheduler threads | **1** |
| Multipart file limit | 1MB |
| Multipart request limit | 10MB |
| `@ManyToOne` fetch | **EAGER** |
| `@OneToMany` fetch | LAZY |
| HTTP client read timeout | **none** |
| Actuator exposed | `health`, `info` |
| Server shutdown | immediate |
| Cache provider (no dependency) | `ConcurrentHashMap`, no TTL, no eviction |
| Bean scope | singleton |
| Transaction propagation | `REQUIRED` |

## 29.37 Questions to rehearse out loud

| Question | The short answer |
|---|---|
| Boot vs Framework? | Same container. Boot pre-writes the configuration. |
| Why constructor injection? | Explicit, `final`, testable without Spring. |
| Default fetch for `@ManyToOne`? | EAGER — override it to LAZY. |
| What is N+1 and how do you fix it? | Lazy access in a loop; fix with a fetch join or `@EntityGraph`. |
| Where does `@Transactional` belong? | The service layer — and never on a self-invoked method. |
| How does Spring Security decide 401 vs 403? | 401 = identity unknown; 403 = known but not permitted. |
| Can you revoke a JWT? | Not without server state — a `jti` blocklist, or short expiry plus a revocable refresh token. |
| `hasRole` vs `hasAuthority`? | `hasRole` prepends `ROLE_`; `hasAuthority` does not. |
| Why did my `@Transactional` not roll back? | Checked exception, or the method was called from within the same class. |
| `REQUIRES_NEW` — what is the risk? | It holds a second connection while the outer transaction waits; loops exhaust the pool. |
| What breaks with a local cache and 3 replicas? | Eviction is per-instance, so the other two serve stale data. |
| Liveness or readiness for the database check? | **Readiness.** A database blip should not restart every pod. |
| Why is a timeout the first resilience control? | Without it, retries multiply the hang and breakers never trip. |
| What makes a rolling deploy zero-downtime? | Graceful shutdown, a readiness probe, and backward-compatible migrations. |

> **Verify, do not trust** — including these notes. Where something matters, confirm it against `docs.spring.io` for the version you actually run.

---
---

# Part 30 — JVM Internals

> Source: *Java + Spring Boot — Zero to Job Ready* (venu-uday), Part 8.

## 30.1 JVM architecture

```
┌─────────────────────────── JVM ───────────────────────────┐
│ Class Loader Subsystem                                     │
│           ↓                                                │
│  Runtime Data Areas: Heap | Stack | Metaspace | PC Register│
│           ↓                                                │
│  Execution Engine: Interpreter | JIT Compiler | GC         │
└────────────────────────────────────────────────────────────┘
```

## 30.2 Class loading

Classes are loaded **lazily, on first use**, in three phases:

1. **Loading** — reading the `.class` file into memory
2. **Linking** — verifying bytecode, allocating memory for static fields, resolving references
3. **Initialization** — running static initializers and static field assignments

A hierarchy of class loaders (**Bootstrap → Platform → Application**) **delegates upward first**, so core Java classes can never be shadowed by application code.

## 30.3 Runtime data areas

| Area | Stores | Shared across threads? |
|---|---|---|
| **Heap** | All objects and arrays (via `new`) | Yes |
| **Stack** | Method call frames — local variables, partial results | No — one per thread |
| **Metaspace** | Class metadata (replaced PermGen since Java 8) | Yes |
| **PC Register** | Address of the current instruction | No — one per thread |

The heap is further divided **generationally**:
- **Young Generation** — Eden + two Survivor spaces, where new objects are born and most die quickly
- **Old Generation** — long-lived objects promoted after surviving several collections

This split exists because **most objects die young** — collecting Young Gen frequently and cheaply is far more efficient than scanning the whole heap every time.

## 30.4 Garbage collectors

| Collector | Strategy | Best for |
|---|---|---|
| **Serial GC** | Single-threaded, stop-the-world | Small heaps, single-core environments |
| **Parallel GC** | Multi-threaded, stop-the-world | Throughput-focused batch workloads |
| **G1 (Garbage First)** | Region-based, mostly concurrent, balances throughput and pause time | **Default for most modern server apps** |
| **ZGC** | Fully concurrent, sub-millisecond pauses even on huge heaps | Very large heaps, strict latency requirements |

```bash
java -Xms512m -Xmx2g -XX:+UseG1GC -jar app.jar
# -Xms: initial heap   -Xmx: max heap   -XX:+UseG1GC: pick the G1 collector
```

Set `-Xms` equal to `-Xmx` in production to avoid runtime heap-resizing pauses.

## 30.5 JIT compilation

The JVM starts by **interpreting** bytecode (slow, but instant startup). The **JIT (Just-In-Time) compiler** monitors which methods run frequently ("hot" methods) and compiles them directly to native machine code at runtime, so repeated execution gets much faster.

This is why long-running Java processes often perform **better the longer they run** — the "warm-up" effect.

## 30.6 Common memory errors

| Error | Cause |
|---|---|
| `StackOverflowError` | Uncontrolled recursion — stack frames pile up past the thread's stack size |
| `OutOfMemoryError: Java heap space` | Heap exhausted — often a memory leak (objects held via a growing static collection, unclosed resources, listeners never unregistered) |
| `OutOfMemoryError: Metaspace` | Too many classes loaded, often from dynamic class generation or classloader leaks |

**Diagnosing a slow leak in production:** it usually shows as a heap-usage graph that **saws upward after every GC** instead of returning to baseline. Take a heap dump (`jmap -dump`) at two points in time and diff the retained objects in a profiler (VisualVM, Eclipse MAT) — the class with the fastest-growing instance count is almost always your leak.

## 30.7 Interview questions — Part 30

1. Walk through what happens from `java -jar app.jar` to your `main()` method running.
2. Why is the heap divided into Young and Old generations?
3. What replaced PermGen in modern Java, and why?
4. `StackOverflowError` vs `OutOfMemoryError` — different causes?
5. What does the JIT compiler do that the interpreter alone cannot achieve efficiently?
6. When would you choose G1 vs ZGC?

**Quick revision**

| Term | One-liner |
|---|---|
| Heap | Shared object storage, garbage-collected |
| Stack | Per-thread call frames, not garbage-collected — unwound on return |
| Metaspace | Class metadata, native memory (off-heap) |
| G1 GC | Default modern collector, balances pause time and throughput |

---
---

# Part 31 — The Developer Toolchain: Build Tools, Git, NIO and Jackson

## 31.1 Maven

A build tool automates compiling code, managing dependencies, running tests, and packaging the application into a deployable artifact.

```xml
<project>
  <groupId>com.example</groupId>
  <artifactId>order-service</artifactId>
  <version>1.0.0</version>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.3.0</version>
  </parent>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>
</project>
```

`spring-boot-starter-parent` pins compatible dependency versions for the whole Spring ecosystem, so you rarely specify a version yourself — this is dependency management at work, and it is exactly what prevents version-conflict headaches.

**Dependency scopes**

| Scope | Available during |
|---|---|
| `compile` (default) | Compilation, testing, runtime — packaged into the final jar |
| `test` | Test compilation and execution only |
| `provided` | Compilation only — expected to be supplied by the runtime environment |
| `runtime` | Execution and testing, not compilation (e.g. a JDBC driver) |

**Build lifecycle** — each phase runs every phase before it, so `mvn package` implicitly compiles and tests first:
```bash
mvn validate   # checks project structure
mvn compile    # compiles source
mvn test       # runs unit tests
mvn package    # produces the .jar/.war
mvn install    # installs the artifact to the local repository
mvn verify     # runs integration checks
```

**Profiles** swap configuration per environment. A **multi-module** project uses a parent `pom.xml` listing child modules — common for splitting a large system into independently buildable pieces (`api-gateway`, `order-service`, `common-lib`) while sharing dependency management.

## 31.2 Gradle, briefly

```kotlin
// build.gradle.kts (Kotlin DSL)
plugins { id("org.springframework.boot") version "3.3.0" }
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
}
```

Gradle uses a **programmable DSL** (Groovy or Kotlin) instead of Maven's declarative XML, and builds **incrementally** with a dependency graph — noticeably faster on large multi-module builds.

**Interview questions:** What does `spring-boot-starter-parent` actually solve? · `compile` vs `provided` vs `runtime` scope, with an example dependency for each · the practical benefit of a multi-module project · Maven vs Gradle, the core structural difference · how you would resolve two dependencies pulling in conflicting versions of the same library.

## 31.3 Git and GitHub

| Term | Meaning |
|---|---|
| Repository | A project's full version history |
| Commit | A saved snapshot of changes with a message |
| Branch | An independent line of development |
| Merge | Combining one branch's history into another |
| Pull request | A request to merge a branch, opened for review |

```bash
git init
git add .
git commit -m "feat: add order creation endpoint"
git branch feature/order-api
git checkout feature/order-api
git push origin feature/order-api
```

**Merge vs rebase**

| | Merge | Rebase |
|---|---|---|
| History | Preserves branch structure, extra merge commit | Linear, cleaner log |
| Safety | Never rewrites history | **Rewrites commit hashes — never rebase a shared/public branch** |
| Use for | Merging a finished feature into main | Cleaning up your own branch before opening a PR |

**Resolving conflicts** — Git marks the conflicting region in both versions; edit to the correct final content, remove the markers, then `git add` the file and continue:
```
<<<<<<< HEAD
int maxRetries = 3;
=======
int maxRetries = 5;
>>>>>>> feature/order-api
```

**Conventional commits**
```
feat: add JWT authentication filter
fix: correct null pointer in OrderService.calculateTotal
docs: update README with Docker instructions
refactor: extract validation logic into a separate class
test: add unit tests for PaymentService
```

**`.gitignore` for a Spring Boot project**
```
target/
*.class
.idea/
*.iml
application-local.yml
.env
```

**GitHub Actions — CI basics**
```yaml
# .github/workflows/build.yml
name: Build and Test
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '21', distribution: 'temurin' }
      - run: mvn -B test
```

## 31.4 NIO — the modern file API

`java.nio.file` is preferred over the legacy `java.io.File` for new code:
```java
Path path = Paths.get("data.txt");
List<String> allLines = Files.readAllLines(path);
Files.writeString(path, "new content", StandardOpenOption.APPEND);
boolean exists = Files.exists(path);
Files.walk(Paths.get("src")).filter(Files::isRegularFile).forEach(System.out::println);
```

## 31.5 Jackson and JSON

Java's built-in `Serializable` (binary, JVM-specific) is rarely used in modern backend work. Spring Boot uses **Jackson** to convert Java objects to and from JSON automatically at the REST boundary.

```java
public record UserDto(String name, int age) {}

ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(new UserDto("Asha", 30));
// {"name":"Asha","age":30}

UserDto parsed = mapper.readValue(json, UserDto.class);
```

In a `@RestController` this happens transparently — a method returning a DTO is serialised by Jackson, and a `@RequestBody` parameter is deserialised the same way, with no manual `ObjectMapper` calls.

**Common mistake:** Jackson needs either a no-args constructor plus setters, or a way to see all the constructor parameter names. This is satisfied automatically for records and Lombok-generated classes, but a hand-written immutable class without annotations can fail with a confusing `InvalidDefinitionException`.

## 31.6 The DAO pattern (pre-JPA)

```java
public interface EmployeeDao {
    Optional<Employee> findById(int id);
    List<Employee> findAll();
    void save(Employee e);
}

public class JdbcEmployeeDao implements EmployeeDao {
    private final DataSource dataSource;
    public JdbcEmployeeDao(DataSource dataSource) { this.dataSource = dataSource; }

    public Optional<Employee> findById(int id) {
        String sql = "SELECT id, name FROM employees WHERE id = ?";
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next()
                    ? Optional.of(new Employee(rs.getInt("id"), rs.getString("name")))
                    : Optional.empty();
            }
        } catch (SQLException e) {
            throw new RuntimeException("Query failed", e);
        }
    }
}
```

The DAO pattern isolates all raw SQL behind an interface, so the rest of the application depends only on that contract — **exactly what `JpaRepository` gives you for free**.

**JDBC batching** — much faster than one-by-one inserts:
```java
PreparedStatement batch = conn.prepareStatement("INSERT INTO logs(msg) VALUES (?)");
for (String msg : messages) {
    batch.setString(1, msg);
    batch.addBatch();
}
batch.executeBatch();   // sends all inserts in one round trip
```

**Connection pooling:** opening a raw database connection is expensive (TCP handshake, authentication). A pool — **HikariCP is Spring Boot's default** — keeps live connections ready to reuse, dramatically cutting per-request latency.

## 31.7 Database fundamentals recap

**Keys and constraints**

| Concept | Meaning |
|---|---|
| Primary key | Uniquely identifies each row; cannot be null or duplicated |
| Foreign key | A column referencing another table's primary key, enforcing referential integrity |
| NOT NULL | The column must always have a value |
| UNIQUE | No two rows may share this value |
| CHECK | A row-level rule (e.g. `price > 0`) enforced by the database |

**Normalization**

| Form | Rule |
|---|---|
| 1NF | Every column holds a single, atomic value — no repeating groups or lists in a cell |
| 2NF | 1NF + every non-key column depends on the **whole** primary key, not part of it |
| 3NF | 2NF + no non-key column depends on another non-key column (no transitive dependency) |

Normalization eliminates duplication and update anomalies, at the cost of needing joins. Real systems sometimes deliberately **denormalize** to optimise read-heavy paths — a tradeoff, not a rule violation.

**Index every foreign key column and every column you frequently filter or sort by.** Do not over-index — every extra index slows down every INSERT/UPDATE on that table.

---
---

# Part 32 — The Distributed Systems Toolkit

> Source: *Zero to Job Ready*, Parts 22–29.

## 32.1 Monolith → modular monolith → microservices

| | Deployment | Scaling | Complexity |
|---|---|---|---|
| **Monolith** | One deployable unit | Scale the whole app together | Low operational, high coupling risk as it grows |
| **Modular monolith** | One deployable, internally modularized | Same as monolith | Disciplined internal boundaries without distributed-systems cost |
| **Microservices** | Many independently deployable services | Scale each service independently | High — network calls, data consistency, observability all become harder |

**Most teams should start with a well-organized modular monolith, not microservices.** Splitting into services adds real operational cost — network failures, distributed transactions, deployment coordination — that only pays off once a team or scaling problem genuinely needs independent deployability.

**Defining service boundaries:** good boundaries follow **business capabilities** (Order Service, Inventory Service, Payment Service), not technical layers (a "database service" or "controller service"). **Each service owns its own data** — no other service reads its database directly.

## 32.2 Inter-service communication

```java
@FeignClient(name = "payment-service", url = "${payment.service.url}")
public interface PaymentFeignClient {
    @GetMapping("/api/payments/{orderId}")
    PaymentStatus getStatus(@PathVariable String orderId);
}

// Usage
PaymentStatus status = paymentFeignClient.getStatus(orderId);
```

**OpenFeign** lets you call another service as if invoking a local interface — the framework handles the actual HTTP call.

Two styles: **synchronous REST** (simple, but couples availability) or **asynchronous messaging** via Kafka (looser coupling, better resilience to a downstream outage).

## 32.3 Resilience4j patterns

```java
@CircuitBreaker(name = "paymentService", fallbackMethod = "paymentFallback")
@Retry(name = "paymentService")
@TimeLimiter(name = "paymentService")
public CompletableFuture<PaymentStatus> checkPayment(String orderId) {
    return CompletableFuture.supplyAsync(() -> paymentFeignClient.getStatus(orderId));
}

private CompletableFuture<PaymentStatus> paymentFallback(String orderId, Throwable t) {
    return CompletableFuture.completedFuture(PaymentStatus.UNKNOWN);   // graceful degradation
}
```

| Pattern | Protects against |
|---|---|
| Circuit breaker | Hammering a failing downstream service — trips open after repeated failures, fails fast |
| Retry | Transient, self-resolving failures |
| Timeout | A slow downstream call hanging your thread indefinitely |
| Bulkhead | One failing dependency exhausting all your threads/connections and taking down unrelated calls |

## 32.4 Spring Cloud

**Service discovery with Eureka**
```
order-service ──registers──► Eureka Server ◄──registers── payment-service
      └────────── "where is payment-service?" ──────────┘
```

```java
@EnableEurekaServer
@SpringBootApplication
public class DiscoveryServerApplication { }
```
```yaml
# order-service application.yml
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
spring:
  application:
    name: order-service
```

Instead of hardcoding a host and port, services ask Eureka for the current address — essential once services scale up and down or move.

**Config Server** centralizes configuration for every service (often backed by a Git repository), so changing a shared property does not mean redeploying every service:
```java
@EnableConfigServer
@SpringBootApplication
public class ConfigServerApplication { }
```
```yaml
spring:
  config:
    import: optional:configserver:http://localhost:8888
```

**API Gateway** — the single entry point clients call, and the natural place to centralize authentication, rate limiting, logging and request/response transformation:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: order-service
          uri: lb://order-service
          predicates: [ Path=/api/orders/** ]
        - id: payment-service
          uri: lb://payment-service
          predicates: [ Path=/api/payments/** ]
```

## 32.5 Kafka and event-driven architecture

In request/response communication the caller waits and both services must be up simultaneously. In **event-driven architecture** a service publishes a fact ("OrderPlaced") without knowing or caring who is listening — decoupling producers from consumers **in both time and knowledge**.

| Term | Meaning |
|---|---|
| **Topic** | A named stream of events (like a table of facts) |
| **Partition** | An ordered, append-only log — a topic is split into partitions for parallelism |
| **Offset** | A message's position within its partition |
| **Consumer group** | A set of consumers sharing the work — each partition is read by exactly **one** consumer within a group |

```java
@Service
public class OrderEventProducer {
    private final KafkaTemplate<String, OrderEvent> kafkaTemplate;

    public void publishOrderPlaced(Order order) {
        OrderEvent event = new OrderEvent(order.getId(), order.getTotal(), Instant.now());
        kafkaTemplate.send("order-events", order.getId().toString(), event);   // key = order id
    }
}

@Component
public class OrderEventConsumer {
    @KafkaListener(topics = "order-events", groupId = "inventory-service")
    public void handle(OrderEvent event) {
        inventoryService.reserveStock(event.orderId());
    }
}
```

Sending with the order id as the **key** guarantees every event for the same order lands in the same partition, preserving per-order ordering even with multiple partitions.

**Dead-letter topics**
```java
@Bean
public DefaultErrorHandler errorHandler(KafkaTemplate<Object, Object> template) {
    var recoverer = new DeadLetterPublishingRecoverer(template);   // failures go to order-events.DLT
    return new DefaultErrorHandler(recoverer, new FixedBackOff(1000L, 3));  // retry 3x, 1s apart
}
```
A dead-letter topic catches messages that repeatedly fail, so a single poison message does not block the whole partition forever.

**Kafka guarantees at-least-once delivery by default** — your consumer will occasionally see the same message twice (e.g. after a rebalance). **Design consumers to be idempotent** rather than assuming exactly-once delivery.

## 32.6 Redis and caching

**Cache-aside (lazy-loading) pattern**
```
read(id):
  value = cache.get(id)
  if value == null:
      value = database.get(id)     // cache miss — go to the source of truth
      cache.put(id, value, ttl)
  return value

write(id, value):
  database.save(id, value)
  cache.evict(id)                  // invalidate — don't leave stale data cached
```

On write, the safest default is to **evict** the entry rather than try to update it in place.

```java
@EnableCaching
@Configuration
public class CacheConfig {}

@Service
public class ProductService {
    @Cacheable(value = "products", key = "#id")
    public ProductResponse getById(Long id) { ... }

    @CacheEvict(value = "products", key = "#id")
    public void update(Long id, ProductRequest request) { ... }

    @CachePut(value = "products", key = "#result.id()")
    public ProductResponse create(ProductRequest request) { ... }
}
```

```yaml
spring:
  data:
    redis: { host: localhost, port: 6379 }
  cache:
    type: redis
    redis:
      time-to-live: 600000   # 10 minutes, in ms
```

**TTL** is the simplest, most robust invalidation strategy for data allowed to be briefly stale (product listings, dashboards) — not for data that must always be perfectly fresh (an account balance).

**In a multi-instance deployment**, an in-memory per-JVM cache gives every instance a different, inconsistent view. Redis's shared external cache means every instance sees the same value — essential once you run more than one replica.

## 32.7 Docker

An **image** is a read-only, versioned snapshot of everything an application needs. A **container** is a running instance of an image — isolated from the host and other containers, but sharing the host's kernel (lighter than a full VM).

```dockerfile
# Multi-stage build — keeps the final image small
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline          # cache dependencies in their own layer
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Essential commands**
```bash
docker build -t order-service:1.0 .
docker run -p 8080:8080 order-service:1.0
docker ps                          # list running containers
docker logs -f <container-id>
docker exec -it <container-id> sh  # shell into a running container
docker volume create order-data    # persistent storage surviving restarts
```

**Docker Compose — a full local environment**
```yaml
services:
  app:
    build: .
    ports: ["8080:8080"]
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/orders
      SPRING_DATA_REDIS_HOST: redis
    depends_on: [db, redis, kafka]

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: orders
      POSTGRES_PASSWORD: secret
    volumes: ["pgdata:/var/lib/postgresql/data"]

  redis:
    image: redis:7-alpine

  kafka:
    image: confluentinc/cp-kafka:7.6.0
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

  zookeeper:
    image: confluentinc/cp-zookeeper:7.6.0

volumes:
  pgdata:
```
```bash
docker compose up -d     # starts everything in the background
docker compose down      # stops and removes containers (-v also removes volumes)
```

One command brings up the application plus every dependency, networked together, with the app referring to them **by service name** (`db`, `redis`, `kafka`) rather than an IP address.

## 32.8 CI/CD

| Term | Meaning |
|---|---|
| **Continuous Integration** | Every push is automatically built and tested — problems surface within minutes, not weeks |
| **Continuous Delivery** | Every change that passes CI is automatically packaged and ready to deploy |
| **Continuous Deployment** | Every passing change is automatically deployed to production, with no manual gate |

```yaml
name: CI/CD
on:
  push:
    branches: [main]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '21', distribution: 'temurin' }
      - run: mvn -B verify

  build-and-push-image:
    needs: build-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
      - run: |
          docker build -t myorg/order-service:$GITHUB_SHA .
          docker push myorg/order-service:$GITHUB_SHA

  deploy:
    needs: build-and-push-image
    runs-on: ubuntu-latest
    steps:
      - run: echo "Trigger deployment to staging/production here"
```

Each job runs only if the previous one (`needs:`) succeeded. **Secrets are stored encrypted in the CI platform and injected as environment variables — never committed.**

| Strategy | How it works | Risk profile |
|---|---|---|
| Rolling | Replace old instances with new ones gradually | Brief mixed-version window |
| Blue-green | Deploy the new version fully alongside the old, then switch traffic at once | Instant rollback, doubles infrastructure briefly |
| Canary | Send a small % of traffic to the new version first, expand gradually | Limits blast radius of a bad release |

**One built artifact should be promotable unchanged from staging to production.** Environment-specific configuration comes from environment variables or a config server, never hardcoded per-environment in the jar.

## 32.9 Cloud fundamentals (AWS)

| Service | What it is for |
|---|---|
| **EC2** | Virtual machines you rent and manage — run your Spring Boot jar directly |
| **ECS / ECR** | Container orchestration (ECS) and a private Docker image registry (ECR) |
| **RDS** | Managed relational database (PostgreSQL/MySQL) — handles backups and patching |
| **S3** | Object storage for files (uploads, static assets, backups) |
| **IAM** | Identity and Access Management — who/what can access which resources |
| **VPC** | An isolated private network for your resources |
| **ALB** | Load balancer distributing traffic across app instances |
| **CloudWatch** | Logs, metrics and alarms |

**A typical deployment topology**
```
Internet → Application Load Balancer → ECS Service (2+ containers, in a VPC)
                                                 ↓
                                          RDS (PostgreSQL)
      CloudWatch collects logs/metrics from all of the above
```

Running **at least two container instances** behind a load balancer means one can fail or be redeployed without downtime — the load balancer simply stops routing to it.

**Least privilege:** IAM roles and policies define exactly what each service may do — the application's role might allow reading from one specific S3 bucket and nothing else. Grant only the permissions a resource genuinely needs.

**Deploying, conceptually:** build the jar and image → push to ECR → update the ECS service to the new image tag → ECS performs a rolling deployment behind the load balancer → the app connects to RDS via a connection string injected from environment variables/secrets, never hardcoded.

## 32.10 Observability

**The three pillars**

| Pillar | Answers | Tooling |
|---|---|---|
| **Logs** | "What exactly happened?" | Structured JSON logs, aggregated centrally |
| **Metrics** | "How is the system behaving, numerically, over time?" | Micrometer → Prometheus → Grafana |
| **Traces** | "Where did this specific request's time go, across services?" | OpenTelemetry, distributed tracing |

**Structured logging** — machine-parseable, so you can search and aggregate by field instead of grepping free text:
```java
log.info("Order placed", kv("orderId", order.getId()), kv("total", order.getTotal()));
// {"level":"INFO","msg":"Order placed","orderId":42,"total":99.90,"traceId":"a1b2c3"}
```

**Distributed tracing**
```
traceId: a1b2c3   (shared across every service the request touches)
┌─ API Gateway         [span: 5ms]
│   └─ order-service      [span: 40ms]
│       └─ payment-service   [span: 30ms]   ← slow — the bottleneck
│       └─ inventory-service [span: 5ms]
```
OpenTelemetry auto-instruments Spring Boot to propagate a trace-id across every HTTP and messaging call, letting Jaeger or Grafana Tempo reconstruct exactly where a slow request spent its time.

**Good alerts fire on symptoms users feel** — elevated error rate, p99 latency spike, health check failing — not on every internal fluctuation.

**The production debugging loop:** check the dashboard for the affected timeframe → correlate with a deploy or traffic spike → drill into traces for a slow/failing request → cross-reference structured logs for that trace-id → fix and verify the metric recovers.

## 32.11 Interview questions — Part 32

**Microservices:** When would you choose microservices over a modular monolith, honestly? · How should service boundaries be drawn? · What does a circuit breaker do, and what state machine does it follow? · Why can naive retries make an outage worse without backoff? · Synchronous REST vs async messaging — tradeoffs? · Why is distributed tracing necessary once you have more than one service?

**Spring Cloud:** What problem does service discovery solve that a hardcoded config file cannot? · What is centralized in a Config Server, and why does that matter operationally? · What responsibilities does an API Gateway take on beyond routing? · How do OpenFeign + Eureka let you call a service by name instead of an IP?

**Kafka:** Topic vs partition? · How does a consumer group enable parallel processing while preserving per-partition order? · Why publish with a message key, and what does it control? · What is a dead-letter topic for? · Why must Kafka consumers be idempotent? · REST vs Kafka — when would you pick each?

**Redis:** Explain the cache-aside pattern · `@Cacheable` vs `@CachePut` vs `@CacheEvict` · Why is TTL effective, and when is it insufficient? · Why does a distributed cache matter once you scale to multiple instances? · What is the risk of caching frequently-changing data?

**Docker:** Image vs container? · Why a multi-stage Dockerfile? · What does a volume solve? · How do containers in the same Compose file reach each other by name? · Why is a container lighter than a VM?

**CI/CD:** Continuous delivery vs continuous deployment? · Why should tests run before an image is built? · Blue-green vs canary? · How should secrets be handled? · Why promote the same artifact instead of rebuilding per environment?

**Cloud:** Why RDS instead of PostgreSQL on EC2? · What does a load balancer protect you against operationally? · What is least privilege, and how does IAM enforce it? · VPC vs the public internet? · Why run 2+ instances even for a low-traffic app?

**Observability:** Logs vs metrics vs traces — what distinct question does each answer? · What does Actuator give you without custom code? · Why structured JSON logs? · What does a trace-id let you do that logs alone cannot? · What makes a good alert vs a noisy one?

---
---

# Part 33 — Design Patterns

> Source: *Zero to Job Ready*, Part 31. Each pattern with the problem, the Java solution, and the Spring Boot connection.

## 33.1 Creational patterns

| Pattern | Problem | Solution |
|---|---|---|
| **Singleton** | Need exactly one instance of a class | Private constructor + static accessor — **Spring beans are singletons by default**, so you rarely hand-write this |
| **Factory** | Object creation logic is complex or must vary by input | A method returning different concrete types behind one interface |
| **Builder** | A constructor with many optional parameters becomes unreadable | Chain setter-style calls, then `build()` the final immutable object |

```java
// Factory
public interface NotificationSender { void send(String to, String msg); }

public class NotificationFactory {
    public static NotificationSender create(String channel) {
        return switch (channel) {
            case "email" -> new EmailSender();
            case "sms"   -> new SmsSender();
            default -> throw new IllegalArgumentException("Unknown channel: " + channel);
        };
    }
}

// Builder
Order order = Order.builder()
    .customerId(1L)
    .addItem("Widget", 2)
    .shippingAddress(address)
    .build();
```

**Spring's `ApplicationContext` is itself a giant Factory + Singleton registry** — `@Bean` methods are factory methods, and by default the container hands back the same singleton instance every time.

## 33.2 Structural patterns

| Pattern | Problem | Solution |
|---|---|---|
| **Adapter** | Two incompatible interfaces need to work together | A wrapper translating one interface's calls into another's |
| **Decorator** | Add behaviour to an object without altering its class or affecting other instances | Wrap the object in another implementing the same interface, adding behaviour around delegated calls |
| **Facade** | A subsystem has many complex parts callers should not need to know about | One simple class exposing a small, high-level API over the complexity |
| **Proxy** | Need to control or intercept access to an object (lazy loading, security, logging) | A stand-in implementing the same interface, forwarding to the real one |

```java
// Decorator
public interface DataSource { String read(); }

public class EncryptedDataSource implements DataSource {
    private final DataSource wrapped;
    public EncryptedDataSource(DataSource wrapped) { this.wrapped = wrapped; }
    public String read() { return decrypt(wrapped.read()); }   // adds behaviour around the original
}
```

**Every Spring `@Transactional` or `@Cacheable` bean is wrapped in a dynamic Proxy at startup** — calling the method actually calls the proxy first, which opens a transaction or checks the cache, then delegates to your real method. **This is exactly why calling a `@Transactional` method from another method in the same class does not trigger the transaction** — the call bypasses the proxy entirely.

## 33.3 Behavioral patterns

| Pattern | Problem | Solution |
|---|---|---|
| **Strategy** | An algorithm needs to vary independently of the client using it | Extract each variant behind a common interface, inject the chosen one |
| **Observer** | Multiple parts of the system need to react when something happens | Subjects notify registered listeners — **the basis of Spring's `ApplicationEvent`** |
| **Template Method** | Several algorithms share the same skeleton but differ in specific steps | An abstract class defines the skeleton, subclasses override the varying steps |
| **Chain of Responsibility** | A request should pass through a series of handlers until one handles it | Each handler either processes the request or passes it on — **literally how Spring Security's filter chain works** |

```java
// Strategy
public interface DiscountStrategy { BigDecimal apply(BigDecimal price); }

public class PercentageDiscount implements DiscountStrategy {
    public BigDecimal apply(BigDecimal price) {
        return price.multiply(BigDecimal.valueOf(0.9));
    }
}

@Service
public class PricingService {
    private final DiscountStrategy discountStrategy;   // injected — swap without touching this class
    public PricingService(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
    }
}

// Observer — Spring's built-in event mechanism
@Component
public class OrderPlacedListener {
    @EventListener
    public void onOrderPlaced(OrderPlacedEvent event) {
        emailService.sendConfirmation(event.getOrder());
    }
}
applicationEventPublisher.publishEvent(new OrderPlacedEvent(order));
```

## 33.4 Interview questions — Part 33

1. Why are Spring beans singletons by default, and how does that relate to the Singleton pattern?
2. Decorator vs Proxy — what is structurally different about their intent?
3. Explain how `@Transactional`'s proxy-based implementation explains the self-invocation gotcha.
4. Give a real use of the Strategy pattern in a Spring Boot app you might build.
5. How does Spring Security's filter chain resemble Chain of Responsibility?
6. When would you reach for Builder instead of a telescoping constructor?

---
---

# Part 34 — Debugging & Troubleshooting Handbook

> Symptom → cause → fix, for the errors you will actually hit.

| Error | Common cause | Fix |
|---|---|---|
| `NullPointerException` | Calling a method on a reference never assigned, or a lazy-loaded relationship accessed outside its session | Use `Optional` at API boundaries; add null checks at the **edges** of the system, not everywhere internally |
| `BeanCreationException` | A required bean is missing, misconfigured, or there is a circular dependency | Read the **"Caused by"** chain — it names the actual missing/circular bean; check `@Profile`/`@ConditionalOn*` guards |
| Port already in use | A previous instance still holds the port | `lsof -i :8080` then kill the process, or change `server.port` |
| Database connection failures | Wrong URL/credentials, DB not started, pool exhausted | Verify the connection string, check the DB is reachable with a plain client first, check HikariCP pool size vs concurrent load |
| `LazyInitializationException` | Accessing a lazy relationship after the persistence context has closed | Fetch what you need **within** the transactional method, use a fetch join/`@EntityGraph`, or map to a DTO before returning |
| Transaction rolled back unexpectedly | An unchecked exception was thrown inside a `@Transactional` method (by design), or the transaction spans a self-invoked call | Confirm the exception is expected to roll back; check for the self-invocation proxy gotcha |
| JWT errors (401 with a valid-looking token) | Clock skew, wrong signing key, or expired token | Log the specific JJWT exception type; verify server clocks are synced (NTP); confirm the signing secret matches across services |
| CORS errors | Frontend origin not in the allowed-origins list, or preflight (OPTIONS) not handled | Configure a `CorsConfigurationSource` explicitly rather than a wildcard in production |
| 401 vs 403 confusion | 401 = not authenticated at all; 403 = authenticated but lacking permission | Return the correct one — conflating them confuses API consumers debugging their own auth flow |
| 409 Conflict | A uniqueness constraint violated, or an optimistic-locking version mismatch | Catch the specific `DataIntegrityViolationException`/`OptimisticLockException` and translate to a clear 409 |
| 500 with no clear cause in logs | An exception swallowed somewhere, or logging level too high to show it | Ensure the global handler logs the **full stack trace** before responding; never silently catch `Exception` |
| Slow SQL / N+1 queries | Missing index, or lazy-loaded collections triggering per-row queries | `EXPLAIN ANALYZE` the query; enable SQL logging to count actual queries per request; add a fetch join |
| `OutOfMemoryError` in production | A memory leak (unbounded cache, unclosed resources) or heap sized too small for load | Heap dump + profiler diff between two points in time; check for ever-growing static collections |
| Docker container exits immediately | The main process crashed on startup — often a missing env var or bad config | `docker logs <id>` immediately after the exit; run the image interactively with `docker run -it --entrypoint sh` |
| Kafka consumer stuck / not receiving | Wrong topic name, consumer group already caught up, or a poison message blocking the partition | Check consumer lag with a Kafka admin tool; verify `group-id` and topic spelling; check for a dead-letter scenario |

## The general debugging method

1. **Reproduce reliably** — a bug you cannot reproduce, you cannot verify fixed
2. **Read the full stack trace** — bottom-to-top for the failure origin, top-to-bottom for the call chain
3. **Form one specific hypothesis at a time** — do not shotgun random changes
4. **Add the minimum logging or breakpoint** needed to confirm or reject it
5. **Fix the root cause, not the symptom** — then add a test that would have caught it

---
---

# Part 35 — Performance Optimization

**Measure first, optimize second.** Guessing at bottlenecks wastes effort on code that was never actually slow.

## 35.1 Database and Hibernate — before/after

```java
// BEFORE — N+1 queries (1 + 100 for 100 departments)
List<Department> depts = departmentRepository.findAll();
depts.forEach(d -> d.getEmployees().size());

// AFTER — 1 query total, via fetch join
@Query("SELECT DISTINCT d FROM Department d LEFT JOIN FETCH d.employees")
List<Department> findAllWithEmployees();
```

```java
// BEFORE — SELECT * pulls unused columns across the network
List<Employee> findByDepartment(String dept);

// AFTER — projection fetches only what the view needs
interface EmployeeNameOnly { String getName(); }
List<EmployeeNameOnly> findByDepartment(String dept);
```

```sql
-- BEFORE: Seq Scan on orders (cost=... rows=500000)
SELECT * FROM orders WHERE customer_id = 42;

-- AFTER: adding the missing index
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
-- now: Index Scan using idx_orders_customer_id (cost=... rows=12)
```

## 35.2 Collections and string handling — before/after

```java
// BEFORE — O(n²) string concatenation
String result = "";
for (String s : items) result += s + ",";

// AFTER — O(n)
StringBuilder sb = new StringBuilder();
for (String s : items) sb.append(s).append(",");
```

```java
// BEFORE — ArrayList.contains() is O(n) per call, O(n²) overall in a loop
List<String> blockList = loadBlockList();
for (String user : users) if (blockList.contains(user)) flag(user);

// AFTER — HashSet.contains() is O(1)
Set<String> blockList = new HashSet<>(loadBlockList());
```

## 35.3 API and caching optimizations

| Technique | Effect |
|---|---|
| Pagination on every list endpoint | Bounds response size and query cost regardless of table growth |
| Cache-aside with Redis on hot, rarely-changing reads | Removes repeated database round trips |
| Connection pool sizing (HikariCP) | Too small starves throughput; too large exhausts the database's own connection limit. Start from `(core_count × 2) + disk spindles`, then measure |
| Async processing for non-critical-path work | Keeps the request/response cycle fast by moving slow work off it (Kafka or `@Async`) |

## 35.4 JVM tuning basics

```bash
java -Xms1g -Xmx1g -XX:+UseG1GC -jar app.jar
# Set Xms == Xmx in production to avoid runtime heap resizing pauses.
# Monitor GC pause frequency/duration via Actuator + a GC log before changing flags further.
```

**Interview questions:** Walk through your process for diagnosing a slow API endpoint · Why measure before optimizing? · Give an example where adding a cache made things worse · How would you size a database connection pool? · Name three concrete fixes for an N+1 query problem.

---
---

# Part 36 — Clean Code & Professional Practice

## 36.1 The core principles

| Principle | Meaning |
|---|---|
| **DRY** | Don't Repeat Yourself — duplicated logic means duplicated bugs and duplicated future edits |
| **KISS** | Keep It Simple — the simplest design that solves the actual problem beats a clever one |
| **YAGNI** | You Aren't Gonna Need It — do not build flexibility for a requirement that does not exist yet |
| **SOLID** | Single responsibility · Open/closed · Liskov substitution · Interface segregation · Dependency inversion |

## 36.2 Bad code → improved code

```java
// BEFORE — unclear names, mixed responsibilities, magic numbers
public class Mgr {
    public double calc(double a, int t) {
        if (t == 1) return a * 0.9;
        if (t == 2) return a * 0.85;
        return a;
    }
}

// AFTER — intention-revealing names, extensible via polymorphism, no magic numbers
public interface DiscountPolicy { BigDecimal apply(BigDecimal price); }

public class LoyaltyDiscount implements DiscountPolicy {
    private static final BigDecimal LOYALTY_RATE = new BigDecimal("0.90");
    public BigDecimal apply(BigDecimal price) { return price.multiply(LOYALTY_RATE); }
}

public class BulkDiscount implements DiscountPolicy {
    private static final BigDecimal BULK_RATE = new BigDecimal("0.85");
    public BigDecimal apply(BigDecimal price) { return price.multiply(BULK_RATE); }
}
```

The "after" version names each concept explicitly, and adding a new discount type means **adding a class** — not editing a growing `if`-chain (the Open/Closed Principle).

## 36.3 Naming and method size

| Weak | Better | Why |
|---|---|---|
| `process(d)` | `calculateMonthlyInterest(deposit)` | The name states what, and on what |
| `List<String> list1` | `List<String> activeUserEmails` | Type-based names carry no domain meaning |
| A 200-line method doing five things | Five well-named private methods, one calling the others | Each piece is independently readable, testable and reusable |

## 36.4 Refactoring and code review

**Refactor in small, safe steps under an existing test suite** — never rewrite untested code from memory.

When reviewing a pull request, focus on **correctness, readability for the next reader, and adherence to the codebase's existing conventions** — not personal style preference. Leave specific, actionable comments: *"extract this into a named method"* beats *"this is messy"*.

**Habits that compound:** a clear README explaining setup and endpoints · meaningful commit messages · Javadoc on genuinely non-obvious public methods.

**Interview questions:** What is the practical difference between DRY and premature abstraction? · How would you refactor a long if/else chain based on a type field? · What makes a code review comment actionable vs just critical? · Give an example of YAGNI.

---
---

# Part 37 — Projects, Roadmaps and Job Preparation

## 37.1 Fifteen portfolio-ready project briefs

Every project follows the same production checklist: **Controller → Service → Repository → Entity/DTO** layering, request validation, centralized exception handling, JWT-secured endpoints where relevant, unit + integration tests, a Dockerfile, and a README documenting setup and API endpoints.

| # | Project | Core entities | Key concepts exercised |
|---|---|---|---|
| 1 | Employee Management System | Employee, Department, Role | One-to-many relationships, RBAC authorization |
| 2 | Expense Tracker | Expense, Category, Budget | Aggregation queries, monthly reporting, pagination |
| 3 | Banking Application | Account, Transaction, Customer | `@Transactional` transfers, optimistic locking, audit trail |
| 4 | E-commerce Backend | Product, Cart, Order, Payment | Many-to-many (cart items), inventory decrement, order state machine |
| 5 | Learning Management System | Course, Lesson, Enrollment, Progress | Nested relationships, role-based content access |
| 6 | Job Portal | JobPosting, Application, Candidate, Recruiter | Full-text search/filtering, file upload (resumes) to S3 |
| 7 | Food Delivery Backend | Restaurant, MenuItem, Order, Delivery | Geolocation queries, real-time status updates, Kafka events |
| 8 | Inventory Management System | Item, Warehouse, StockMovement | Concurrency control on stock updates, low-stock alerts |
| 9 | Payment Service | PaymentIntent, Refund, Ledger | Idempotency keys, webhook handling, reconciliation |
| 10 | Enterprise Microservices Platform | Spans projects 1–9 | API Gateway, service discovery, distributed tracing |
| 11 | Hotel Booking System | Hotel, Room, Booking, Guest | Availability-window queries, double-booking prevention via constraints/locking |
| 12 | Social Media Backend | Post, Comment, Like, Follow | Self-referencing many-to-many, feed pagination, fan-out on write vs read |
| 13 | Healthcare Appointment System | Patient, Doctor, Appointment, Slot | Time-slot conflict validation, role-based views |
| 14 | URL Shortener Service | ShortUrl, ClickEvent | Base62 encoding, Redis-backed redirect caching, click analytics via Kafka |
| 15 | Real-Time Chat Backend | Conversation, Message, Participant | WebSocket messaging, delivery status, Redis pub/sub for multi-instance fan-out |

**Build them roughly in order** — each reuses skills from the last while introducing one or two new concepts. Trying to combine everything in project 1 will slow you down.

**Worked example — Expense Tracker structure**
```
src/main/java/com/example/expensetracker/
├── entity/     Expense.java, Category.java, Budget.java, User.java
├── dto/        ExpenseRequest.java, ExpenseResponse.java, MonthlySummary.java
├── repository/ ExpenseRepository.java (with @Query for monthly aggregation)
├── service/    ExpenseService.java, BudgetAlertService.java
├── controller/ ExpenseController.java, ReportController.java
├── security/   SecurityConfig.java, JwtAuthFilter.java
└── exception/  GlobalExceptionHandler.java
```
```java
@Query("SELECT new com.example.dto.CategoryTotal(e.category.name, SUM(e.amount)) " +
       "FROM Expense e WHERE e.user.id = :userId AND e.date BETWEEN :start AND :end " +
       "GROUP BY e.category.name")
List<CategoryTotal> sumByCategory(Long userId, LocalDate start, LocalDate end);
```

## 37.2 The capstone — a multi-vendor marketplace

```
                    ┌── API Gateway ──┐
                    │ (routing, auth) │
                    └────────┬────────┘
      ┌───────────┬──────────┼──────────┬───────────┐
      ▼           ▼          ▼          ▼           ▼
auth-service catalog-svc order-service payment-svc inventory-svc
 (JWT issue)  (Postgres)   (Postgres)  (intents)  (Redis+Postgres)
      └──── Eureka (service discovery) ─── Config Server ────┘
                          │
             Kafka: order.placed, payment.completed,
                    inventory.reserved, order.shipped
```

| Concern | Component |
|---|---|
| Authentication | auth-service issues JWTs; every other service validates them via a shared filter |
| Data per service | Each service owns its own schema — order-service never queries catalog-service's database directly |
| Order → payment → inventory flow | order-service publishes `order.placed`; payment and inventory consume it independently and publish their own completion events |
| Resilience | Circuit breakers around any remaining synchronous calls |
| Caching | Product catalog reads cached in Redis; invalidated on vendor updates |
| Deployment | Each service containerized, Docker Compose locally / ECS in the cloud |
| CI/CD | Each service has its own pipeline: test → build image → push → deploy |
| Observability | Structured logs + Actuator metrics per service, correlated by a shared trace-id |
| Testing | Unit tests per service, integration tests with Testcontainers, an end-to-end smoke test hitting the gateway |

**Suggested build order:** auth-service (JWT standalone) → catalog-service (CRUD + search + Redis) → order-service (sync call to catalog, publishes events) → inventory & payment services (consume order events) → wire in Eureka + Config Server once 3+ services exist and coordination pain is real → **API Gateway last**, once you know what routes need exposing → layer in observability and CI/CD throughout, not as an afterthought.

**Be ready to explain honestly what you would change with more time** — that self-awareness reads better than pretending it is flawless.

## 37.3 The 90-day job-ready roadmap

**Days 1–30 — Java + DSA + SQL**

| Week | Theory | Daily practice | Outcome |
|---|---|---|---|
| 1 | Foundations, Java syntax, OOP basics | 10 beginner exercises/day | Comfortable writing basic Java programs |
| 2 | Collections, Exceptions, Java 8+ | 5 collections + 5 stream exercises/day | Fluent with Streams and core collections |
| 3 | Concurrency, Databases, SQL | 5 SQL queries/day against a practice schema | Joins, subqueries and window functions confidently |
| 4 | DSA — arrays, strings, two pointers, sliding window | 3 Easy DSA problems/day | 15–20 Easy problems solved independently |

**Days 31–60 — Spring + Spring Boot + JPA + REST + Security**

| Week | Theory | Daily practice | Outcome |
|---|---|---|---|
| 5 | Spring, Spring Boot | Build a "Hello API" from scratch each day, varying structure | Comfortable with DI, beans and app startup |
| 6 | REST APIs | Build the Student API and Employee API end to end | Two complete CRUD APIs with validation and error handling |
| 7 | JPA/Hibernate | Add relationships + fix an intentionally introduced N+1 each day | Confident diagnosing and fixing N+1 issues |
| 8 | Security, Testing | Add JWT auth to a prior project; write 5 tests/day | One fully secured, tested API project |

**Days 61–75 — Microservices + Kafka + Redis + Docker**

| Week | Theory | Daily practice | Outcome |
|---|---|---|---|
| 9 | Microservices, Spring Cloud | Split one prior monolith into two services | Two services communicating via OpenFeign + Eureka |
| 10 | Kafka | Add an event published on order creation, consumed by a second service | Working event-driven flow |
| 11 | Redis, Docker | Cache one endpoint; containerize the whole stack with Compose | `docker compose up` brings up the full working system |

**Days 76–90 — Projects + System Design + Interviews + Applications**

| Days | Focus | Outcome |
|---|---|---|
| 76–82 | Finish and polish the capstone; write its README and Dockerize it | One flagship portfolio project, fully documented |
| 83–85 | System design practice — 1 prompt/day, drawn and explained aloud | Comfortable structuring a 30–45 min design conversation |
| 86–87 | Mock interviews across all five tracks | Rehearsed answers to the highest-frequency questions |
| 88 | Resume, GitHub, LinkedIn | Application-ready profile |
| 89–90 | Begin applying — 10+ applications, prioritizing referrals | Applications in flight |

**Do not wait until day 90 to start applying.** Begin around day 75 once the capstone is functionally complete — interview loops take 2–4 weeks to progress, and you want that clock running in parallel with your final prep.

**The 100-day variant** covers identical ground at a gentler pace, adding two dedicated revision weeks. Pick the **90-day plan** if you can dedicate 4+ focused hours daily and have some prior programming exposure; pick the **100-day plan** if you are learning part-time (1–2 hrs/day), are a complete beginner, or retain material better with built-in review cycles.

**Use each revision week for active recall, not re-reading:** close the notes and rebuild a small project or re-solve a batch of DSA problems from scratch. Re-reading feels productive but builds far weaker retention.

## 37.4 Resume, portfolio and applications

**Resume & ATS**
- Lead each bullet with an action verb and a **measurable outcome**: *"Reduced API p95 latency by 40% by fixing an N+1 query and adding Redis caching"* beats *"Worked on backend performance"*
- **Mirror the exact technology names from the job posting** — "Spring Boot", not "Spring framework"; "PostgreSQL", not "SQL database". ATS keyword matching is literal
- List 2–3 real projects with a one-line description, tech stack, and a GitHub link each
- One page for under 5 years of experience; a clean **single-column** layout parses more reliably through ATS than multi-column designs

**GitHub portfolio.** Pin your 3–4 strongest projects. Each repo needs a clear README (what it does, tech stack, how to run it locally, a screenshot or API example), meaningful commit history (not one giant "final commit"), and a passing CI badge.

**LinkedIn & networking.** A headline stating the target role plainly — *"Backend Developer — Java, Spring Boot, PostgreSQL"* — reads better to a recruiter search than a vague tagline. Post about what you build. **A warm referral consistently outperforms a cold application.**

**Presenting a project in an interview:** the problem it solves (30 sec) → architecture at a high level, drawn if possible (1 min) → one technical decision worth defending, and why (1 min) → what you would improve with more time (30 sec). This shows judgment, not just output.

## 37.5 How interview loops differ by company type

| Company type | Typical rounds | What they weight most |
|---|---|---|
| **Product companies** | DSA coding, system design, Java/Spring depth, behavioral | Problem-solving depth and system design judgment |
| **Service/consulting** | Core Java/SQL fundamentals, a practical coding test, communication round | Breadth of practical knowledge, client-facing communication |
| **Startups** | A take-home or pairing exercise close to their actual stack, culture fit | Can you ship, and do you fit the team's pace and ownership style |
| **Enterprise** | Structured rounds: Java fundamentals, Spring/JEE ecosystem, SQL, sometimes a design document review | Process discipline, deep framework knowledge, stability |
| **FAANG-style** | 2–4 DSA coding rounds, 1 system design (for 3+ YOE), 1–2 behavioral | Algorithmic rigor and clear communication of tradeoffs under time pressure |

**Coding round expectations, regardless of company:** think aloud, clarify constraints and edge cases before coding, start with a working brute-force solution if the optimal approach is not immediately obvious, then optimize and **state the resulting time/space complexity unprompted**.

**Behavioral rounds:** use **STAR** (Situation, Task, Action, Result). Prepare concrete stories in advance for a conflict with a teammate, a mistake you made and how you recovered, a time you pushed back on a decision, and a project you are proud of — reuse and adapt these rather than improvising each time.

**Ask the recruiter directly what the loop structure looks like** before your interviews — most will tell you plainly, and tailoring prep to the actual format is a far better use of limited time than guessing.

## 37.6 Mock interview answers worth rehearsing

**Java — "Your service is throwing intermittent `ConcurrentModificationException`s. How would you find and fix it?"**
> "That points to a collection being structurally modified while it is being iterated — likely a shared List or Map being read in one thread while another mutates it, or a for-each loop calling `remove()` directly on the collection instead of the iterator. I would grep for iteration over that collection, check if it is ever accessed from more than one thread, and either switch to a concurrent collection like `CopyOnWriteArrayList`/`ConcurrentHashMap`, or use the iterator's own `remove()` and add synchronization if multiple threads are genuinely involved."

**Java — "Why composition over inheritance here?"**
> "Inheritance locks the subclass to one parent's implementation permanently and can violate Liskov Substitution if the subclass does not behave consistently with the parent's contract. Composition — giving the class a reference to a collaborator — keeps the relationship swappable and testable, which matters especially once the class needs to be unit tested in isolation."

**Spring Boot — "A developer added a bean with `@Autowired` on a field and it broke a unit test. Why?"**
> "Field injection means the class has no public constructor accepting its dependency, so a plain unit test that does not use Spring's context cannot supply a mock — the field stays null. I would refactor to constructor injection: the dependency becomes a required constructor parameter, trivially mockable with `new ServiceUnderTest(mockDependency)` and no Spring context at all."

**Spring Boot — "How would you add rate limiting to a public API?"**
> "At the gateway level ideally, using a token-bucket algorithm keyed by client id or IP — Resilience4j has a RateLimiter module, or Redis-backed counters work well across multiple instances since the limit state needs to be shared, not per-instance."

**Backend — "When is a synchronous REST call fine vs when do you need messaging?"**
> "If the caller genuinely needs the result immediately to proceed, and the two services' availability is already coupled anyway, REST is simpler and I would default to it. If the work can happen after the fact — a confirmation email, updating a search index, notifying another bounded context — messaging decouples the services' uptime and lets the receiver process at its own pace."

**SQL — "Find customers who placed orders in every month of Q1."**
```sql
SELECT customer_id FROM orders
WHERE order_date BETWEEN '2026-01-01' AND '2026-03-31'
GROUP BY customer_id
HAVING COUNT(DISTINCT DATE_TRUNC('month', order_date)) = 3;
```
Narrate the `HAVING` clause's role explicitly.

**System design — "Design a notification service for push, email and SMS."**
> Clarify scale and delivery guarantees first, then propose a `NotificationRequest` queue (Kafka), a router picking a channel-specific worker per message type, retry with exponential backoff and a dead-letter queue for permanent failures, and **idempotency keys** so a retried send does not double-notify a user — explicitly naming the tradeoff of at-least-once delivery.

**Debugging — "A bean fails with `BeanCreationException: Circular reference`."**
> "Two beans depend on each other via constructor injection, so neither can be fully constructed first. Fix by breaking the cycle — typically by extracting the shared responsibility into a third bean, or as a last resort using setter injection on one side to defer the dependency until after construction."

**Practice method:** record yourself answering each out loud in **under 90 seconds**, without reading — then compare. The gap between what you said and what is written is exactly what to drill next.

## 37.7 Additional high-frequency Q&A

**Why is Java platform-independent, and what actually crosses platforms?**
Source compiles to **bytecode**, not native machine code; any machine with a matching JVM runs that same bytecode. The JVM is platform-specific; the bytecode it consumes is not.

**Why does Java pass everything "by value", even objects?**
A reference variable holds a value — the memory address of an object. Passing it copies that **address**, not the object. The method can mutate the object through the copied reference, but reassigning the parameter never affects the caller's variable.

**Why can't static methods be overridden?**
Static methods are resolved at compile time based on the **reference type** (static/early binding), not the runtime object type. This is **method hiding**, not overriding — dynamic dispatch never enters the picture.

**`equals()` vs `hashCode()` — what is the contract?**
Equal objects (per `equals()`) must produce the same `hashCode()`; unequal objects may or may not. Breaking this corrupts hash-based collections.

**Why is `ArrayList.add()` amortized O(1) despite occasional O(n) resizing?**
Most adds just place an element in existing capacity — O(1). When capacity is exhausted, ArrayList allocates a larger array (typically 1.5×) and copies everything — O(n), but rarely enough that the average cost per add stays O(1).

**Why does modifying a List while iterating throw `ConcurrentModificationException`?**
The enhanced for-loop uses an `Iterator` internally, which tracks a modification count. Structurally changing the list outside the iterator's own `remove()` invalidates that count, and the next `next()` call detects the mismatch and **fails fast** — better than silent, undefined behaviour.

**What is type erasure's practical downside?**
You cannot create a generic array (`new T[10]`), use `instanceof` against a parameterized type, or overload methods differing only by generic type parameter — the compiler has already erased that information.

**Why is double-checked locking subtle to get right?**
Without the field being **`volatile`**, another thread can observe a partially-constructed object due to instruction reordering — the reference can appear non-null before the constructor has finished.
```java
private static volatile Singleton instance;
public static Singleton getInstance() {
    if (instance == null) {
        synchronized (Singleton.class) {
            if (instance == null) instance = new Singleton();
        }
    }
    return instance;
}
```

**Why is `ConcurrentHashMap` faster than a synchronized `HashMap` under contention?**
A synchronized HashMap locks the **entire map** for every operation. `ConcurrentHashMap` partitions its internal structure so different threads operate on different segments concurrently without blocking each other.

**Why can a stream only be consumed once?**
A stream is not a data structure — it is a **one-time pipeline** of operations over a source. Once a terminal operation runs the pipeline is consumed; reusing it throws `IllegalStateException` by design.

**When is a parallel stream actually worth using?**
Only for large datasets with **CPU-bound, independent** per-element work and no shared mutable state. For small collections or I/O-bound work the split/merge overhead outweighs any benefit.

**How does Hibernate manage entities across their lifecycle?**
An entity is **Transient** until `persist()`-ed, becoming **Managed** and tracked by the persistence context — changes are auto-detected ("dirty checking") and flushed on commit. It becomes **Detached** once the persistence context closes, at which point changes are no longer tracked; `remove()` transitions it to **Removed**.

**A production endpoint is suddenly slow only under load. How do you investigate?**
Check metrics for the time window (CPU, memory, DB connection pool saturation, GC pauses). Check for a newly introduced N+1. Check thread dumps for blocked threads (lock contention or a slow downstream). Check whether a circuit breaker or timeout is missing on a call to a degraded dependency, causing thread starvation upstream.

**How would you design a scalable REST API for 10x traffic growth?**
Stateless services behind a load balancer, a cache layer for hot reads, pagination on all list endpoints, async processing (Kafka) for non-critical-path work, database read replicas, and connection pooling sized to expected concurrency — **validated with load testing before the growth actually arrives**.

---
---

# Part 38 — Rapid Revision Cheat Sheets

## 38.1 Java syntax & OOP

| Need | Syntax |
|---|---|
| Class | `public class Foo { }` |
| Interface | `public interface Foo { void bar(); }` |
| Inheritance | `class Dog extends Animal { }` |
| Interface impl. | `class Foo implements Bar { }` |
| Record | `public record Point(int x, int y) {}` |
| Lambda | `(a, b) -> a + b` |
| Try-with-resources | `try (var r = open()) { }` |
| Modern switch | `switch(x) { case A -> ...; }` |

## 38.2 Collections & Streams

| Need | Use |
|---|---|
| Ordered, resizable list | `ArrayList` |
| Unique elements | `HashSet` |
| Key-value lookup | `HashMap` |
| Thread-safe map | `ConcurrentHashMap` |
| Filter + transform + collect | `list.stream().filter(...).map(...).collect(Collectors.toList())` |
| Group by a field | `Collectors.groupingBy(...)` |
| Safe "may be absent" | `Optional<T>` |

## 38.3 SQL

| Need | Syntax |
|---|---|
| Filter groups | `GROUP BY x HAVING COUNT(*) > 1` |
| Keep all left rows | `LEFT JOIN ... ON ...` |
| Named subquery | `WITH cte AS (SELECT ...) SELECT * FROM cte` |
| Rank within groups | `RANK() OVER (PARTITION BY x ORDER BY y)` |
| Check query plan | `EXPLAIN ANALYZE SELECT ...` |

## 38.4 Spring / Spring Boot / JPA

| Annotation | Purpose |
|---|---|
| `@SpringBootApplication` | Entry point: config + component scan + auto-config |
| `@RestController` / `@RequestMapping` | Declares a JSON-returning web controller and its base path |
| `@Service` / `@Repository` / `@Component` | Marks a class as a Spring-managed bean, by layer |
| `@Autowired` (constructor) | Injects a dependency — prefer constructor injection |
| `@Entity` / `@Id` / `@GeneratedValue` | Maps a class to a database table and its primary key |
| `@OneToMany` / `@ManyToOne` / `@ManyToMany` | Declares an entity relationship |
| `@Transactional` | Wraps a method in a database transaction |
| `@Valid` + `@RequestBody` | Validates an incoming JSON payload against a DTO's constraints |
| `@RestControllerAdvice` + `@ExceptionHandler` | Centralized error handling across all controllers |

## 38.5 Git, Docker, Linux

| Task | Command |
|---|---|
| Create + switch branch | `git checkout -b feature/x` |
| Replay commits cleanly | `git rebase main` |
| Build a Docker image | `docker build -t app:1.0 .` |
| Start a full local stack | `docker compose up -d` |
| Find what is using a port | `lsof -i :8080` |
| Tail logs live | `tail -f app.log` |

## 38.6 Big O

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | `HashMap.get()` |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Scanning an array once |
| O(n log n) | Linearithmic | Efficient sorting (merge sort) |
| O(n²) | Quadratic | Nested loop comparing every pair |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci, brute-force subsets |

## 38.7 Glossary

| Term | Definition |
|---|---|
| **ACID** | Atomicity, Consistency, Isolation, Durability — the guarantees a database transaction provides |
| **Bean** | An object managed by the Spring IoC container |
| **Circuit breaker** | A pattern that stops calling a repeatedly failing dependency, failing fast instead |
| **DTO** | Data Transfer Object — shapes data crossing an API boundary, separate from the internal entity |
| **Idempotent** | An operation producing the same result no matter how many times it is applied |
| **JWT** | JSON Web Token — a signed, self-contained token for stateless authentication |
| **N+1 problem** | One query for a list of parents plus one more query per parent for related data |
| **ORM** | Object-Relational Mapping — mapping Java objects to database rows (Hibernate implements this) |
| **Race condition** | An outcome depending on unpredictable thread timing due to unsynchronized shared state |
| **SOLID** | Single responsibility, Open/closed, Liskov substitution, Interface segregation, Dependency inversion |
| **TTL** | Time To Live — how long a cached value stays valid before automatic expiry |

## 38.8 The Java + Spring Boot job-ready master checklist

- [ ] Core Java syntax, OOP, generics
- [ ] Collections Framework, internal workings
- [ ] Exception handling, custom exceptions
- [ ] Java 8+ streams, lambdas, Optional
- [ ] Multithreading, concurrency primitives
- [ ] JVM internals, GC basics
- [ ] HTTP, REST principles, status codes
- [ ] SQL — joins, subqueries, window functions
- [ ] JDBC fundamentals
- [ ] Spring IoC/DI, bean lifecycle
- [ ] Spring Boot auto-configuration
- [ ] REST API design with Spring Boot
- [ ] Spring Data JPA / Hibernate, N+1 fixes
- [ ] Spring Security, JWT auth
- [ ] Unit + integration testing
- [ ] Microservices patterns & resilience
- [ ] Kafka fundamentals
- [ ] Redis caching
- [ ] Docker & Docker Compose
- [ ] CI/CD pipeline basics
- [ ] Cloud fundamentals (AWS)
- [ ] Observability: logs, metrics, tracing
- [ ] System design method + 3 case studies practiced
- [ ] Design patterns with real examples
- [ ] 100+ DSA problems solved across difficulties
- [ ] Mock interviews completed, all 5 tracks
- [ ] Resume, GitHub, LinkedIn ready
- [ ] 3+ portfolio projects + capstone complete

---

## Appendix — What was added in this revision

| Source | Added as |
|---|---|
| `java-springboot-complete-notes/springbootcompletenotesfromgumroad/Spring-Boot-Complete-Notes-Part-1..4.pdf` (36 pp, mellaithy) | **Part 29** — Spring Boot in Depth, including the corrections tables and defaults |
| `java-springboot-complete-notes/venu-uday-java-whatsapp.pdf` (167 pp, *Zero to Job Ready*, 45 parts) | **Parts 30–38** — JVM internals, toolchain, distributed systems, design patterns, debugging, performance, clean code, projects/roadmaps, cheat sheets |
| `java1.pdf` | **Nothing new** — byte-identical text to `1787731829904.pdf` (Spring Boot Field Notes), already covered in Part 26 |
| `java2.pdf` | **Nothing new** — byte-identical text to `1788540851430.pdf` / `backenddevelopementnotes.pdf` (Backend Development Beginner's Guide), already covered in Part 24 and Section D of the interview file |
| `java-springboot-complete-notes/jhu784-notes-javaspringbootnotes.pdf` | Already mapped in Part 26.28 (copy of the file in the parent folder) |
| `java-springboot-complete-notes/spring_boot_tutorial_tutorialspoint.pdf` | Already mapped in Part 26.28 (copy of the file in the parent folder) |

*End of notes. Interview questions continue in **JAVA-INTERVIEW-QUESTIONS.md**.*
