---
title: JAVA-INTERVIEW-QUESTIONS
topic: java-spring
source_type: interview-questions
source_file: STUDYNOTEs/JAVA-INTERVIEW-QUESTIONS.md
---

# Java & Backend — Complete Interview Question Bank

> Every interview question found across the files in the `javanotes` folder, organised by topic.
> Concepts and explanations live in **JAVA-COMPLETE-NOTES.md** — read that first, then use this to test yourself.

## Contents

| Section | Topic | Questions |
|---|---|---|
| **A** | Core Java | 94 |
| **B** | Spring Boot & Backend (Top 50) | 50 |
| **C** | API & REST | 100 |
| **D** | Backend Development Fundamentals | 30 |
| **E** | Multithreading & Concurrency Scenarios | 70 |
| **F** | System Design | 10 + 40 tips |

**How to practise:** cover the answer, say yours out loud, then compare. If you cannot explain it in under a minute in plain words, you do not know it yet.

---
---

# SECTION A — Core Java (94 Questions)

## A1–A10: Basics and OOP intro

**1. What is Java?**
A high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible. It is general-purpose and follows "write once, run anywhere" — compiled Java code runs on all platforms that support Java without recompiling. Used for web, mobile, desktop, enterprise, scientific and embedded applications.

**2. Explain the difference between JDK, JRE and JVM.**
- **JDK (Java Development Kit)** — a development environment that includes the JRE plus development tools (compiler, debugger, documentation generator). Used to **create** Java applications.
- **JRE (Java Runtime Environment)** — a set of tools providing the runtime environment for running Java software. Contains class libraries, supporting files and the JVM.
- **JVM (Java Virtual Machine)** — the foundation that makes Java source platform-agnostic. It runs the bytecode. It is included in both the JDK and JRE, and Java programs will not run without it.

**3. What are the main features of Java?**
Simple and easy to learn; object-oriented; platform independent; automatic memory management; secure; rich API; multithreading; high performance; scalable. Also robust, portable, architecture neutral, distributed and dynamic.

**4. What is the difference between Java and JavaScript?**
Java is an OOP programming language; JavaScript is an OOP scripting language. Java creates applications that run in a virtual machine or browser; JavaScript runs in a browser only. Java code must be compiled; JavaScript code is all text.

**5. What is an object-oriented programming language?**
A language that uses objects to bind data and the functions that operate on it together. The goal is to implement real-world entities like inheritance, hiding and polymorphism. Its concepts are class, object, inheritance, polymorphism, encapsulation and abstraction.

**6. What are the pillars of OOP?**
Four: **Inheritance, Polymorphism, Encapsulation, Data Abstraction.**

**7. What is a class in Java?**
A set of objects that share common characteristics/behaviour and common properties/attributes. It is a user-defined blueprint or prototype from which objects are created. `Student` is a class; a particular student named Ravi is an object.

**8. What is an object in Java?**
The basic unit of OOP, representing a real-life entity. Objects are instances of a class, created to use the class's attributes and methods. A cat, a lighter, a pen or a car are all objects.

**9. How do you create an object in Java?**
With the `new` keyword: `MyClass myObject = new MyClass();`
Other ways: using `newInstance()` (of `Class` or of `Constructor`), the `clone()` method, and deserialization.

**10. What is the difference between a class and an object?**

| Class | Object |
|---|---|
| A user-defined datatype with its own data members and member functions | An instance of a class |
| A blueprint or prototype | A real-world entity such as a book or car |
| A logical entity | A physical entity |
| Occupies no memory space | Occupies memory space |
| Declared with the `class` keyword | Created with the `new` keyword |

## A11–A20: Inheritance, polymorphism, encapsulation, constructors

**11. Explain the concept of inheritance.**
A mechanism that lets a class inherit the properties and behaviours of another class, using the `extends` keyword. The inheriting class is the subclass/child; the inherited one is the superclass/parent. The subclass inherits all `public` and `protected` members — fields, methods and constructors.
```java
class Animal { String name; void eat() { System.out.println("Animal is eating"); } }
class Dog extends Animal { String breed; void bark() { System.out.println("Dog is barking"); } }
```

**12. What is the purpose of the `super` keyword?**
To call the superclass constructor from the subclass constructor with `super(args)`, and to access parent fields and methods (`super.field`, `super.method()`).
```java
class Subclass extends Superclass {
    public Subclass(int x, int y) { super(x); /* ... */ }
}
```

**13. What is polymorphism in Java?**
From the Greek *poly* (many) and *morph* (forms) — the ability of objects to take on many forms, letting different objects respond to the same method call in multiple ways. Achieved through overloading (compile-time) and overriding (runtime).

**14. Explain the difference between method overloading and method overriding.**
Overloading is two or more methods in a class with the same name but different parameters, so the same name performs different tasks. Overriding is a subclass providing its own implementation of a method already defined in the superclass, customising behaviour without breaking code that relies on the superclass.

| Feature | Overloading | Overriding |
|---|---|---|
| Number of methods | Two or more with the same name | One in the subclass, one in the superclass |
| Parameters | Different | Same |
| Return type | Same or different | Same (or covariant) |
| Inheritance | Not required | Required |
| Purpose | Multiple methods with one name doing different tasks | Customise behaviour in a subclass |

**15. What is encapsulation in Java?**
The process by which data (variables) and the code that acts on them (methods) are integrated as a single unit. By making a class's variables private, other classes cannot access them — only the class's own methods can. Access is then provided through public getters and setters, so the internal implementation stays hidden.

**16. What is the purpose of access modifiers in Java?**
To control the access level of classes, methods, variables and constructors — restricting access to certain parts of a program, which improves security and makes the code more maintainable.

**17. What is the difference between public, private, protected and default?**
- **public** — accessible from anywhere in the program
- **private** — accessible only within the class where it is declared
- **protected** — accessible within the declaring class and from any subclass of it
- **default** (no keyword) — accessible only within the package where it is declared

**18. What is an abstract class in Java?**
A restricted class that cannot be used to create objects — to access it, it must be inherited from another class. An abstract method can only appear in an abstract class and has no body; the body is provided by the subclass.
```java
abstract class Shape { abstract void draw(); }
class Circle extends Shape { @Override void draw() { System.out.println("Drawing a circle"); } }
```

**19. How do you achieve abstraction in Java?**
Through interfaces and abstract classes. **100% abstraction is achieved with interfaces.** Data abstraction is the process of identifying only the required characteristics of an object, ignoring the irrelevant details.

**20. What is a constructor in Java?**
A special method used to **initialize objects**. It is called when an object of the class is created, and it can set initial values for object attributes.
Differences from a method: a constructor has the same name as the class, has **no return type**, and is called automatically on object creation.

## A21–A30: Constructors, static, final, packages

**21. What is the difference between a default and a parameterized constructor?**
- **Default constructor** — no parameters; implicitly provided by the compiler if no constructor is explicitly defined; initialises instance variables to their default values.
- **Parameterized constructor** — has one or more parameters; explicitly written by the programmer; lets you initialise instance variables to specific values at creation time.

**22. What is the purpose of the `static` keyword?**
Mainly memory management. It shares the same variable or method across all instances of a class. It can be applied to variables, methods, blocks and nested classes. A static member belongs to the **class** rather than to an instance.

**23. What is a static method in Java?**
A method that belongs to the class rather than an instance. It is used to access and change static variables and call other static methods.
Features: called using the class name, not an instance name; can only access static variables and static methods; cannot access non-static members; typically used for utility functions such as mathematical or string manipulation helpers.

**24. What is the purpose of the `final` keyword?**
A non-access modifier used on classes, attributes and methods to make them non-changeable — impossible to inherit or override. It is useful when you want a variable to always store the same value, like PI.

**25. Explain the difference between `final`, `finally` and `finalize`.**
1. **`final`** — a keyword that restricts modification of a variable, method or class
2. **`finally`** — a block that ensures a section of code always executes, even if an exception is thrown
3. **`finalize`** — a method used to perform cleanup processing on an object before it is garbage collected

**26. What is method overriding in Java?**
When a subclass has the same method as the parent class — providing a particular implementation of a method declared by one of its parent classes. The subclass must use the same method name, return type and parameter list. The overriding method may return a **subtype** of the overridden method's return type (covariant return).

**27. What is method overloading in Java?**
Having two or more methods in a class with the same name and different arguments — a different number of arguments, or different data types.
```java
class Adder {
    static int add(int a, int b) { return a + b; }
    static double add(double a, double b) { return a + b; }
}
```

**28. What is a package in Java?**
A group of similar types of classes, interfaces and sub-packages. Packages can be built-in or user-defined. Built-in packages include `java`, `lang`, `awt`, `javax`, `swing`, `net`, `io`, `util` and `sql`.

**29. How do you import packages in Java?**
Packages avoid naming conflicts and control access to classes. They are declared with the `package` keyword (`package mypackage;`), and nested packages use dots (`package mypackage.subpackage;`). You import with `import java.lang.String;`.

**30. What is the purpose of the import statement?**
It tells Java which class you mean when you use a short name like `List`, and where to find that class's definition. You can import just the classes you need, one statement per class, or a whole package.
```java
import java.util.List;
import java.util.*;
import static java.lang.Math.PI;
```

## A31–A40: Interfaces, variables, keywords, arrays

**31. What is a Java interface?**
An abstract type used to declare behaviour that classes must implement — similar to protocols in other languages.
Key features: interfaces can contain only abstract methods; they cannot contain concrete methods or instance variables; they can be used to achieve multiple inheritance; they can be extended by other interfaces; and they are implemented by classes.

**32. Explain the difference between abstract classes and interfaces.**

| Feature | Abstract Class | Interface |
|---|---|---|
| Definition | A class declared abstract cannot be instantiated, but it can be subclassed | A reference type used to declare a set of abstract methods |
| Methods | Both abstract and non-abstract methods | Only abstract methods |
| Variables | Can have variables | Cannot have (instance) variables |
| Inheritance | Can only be extended by one class | Can be implemented by multiple classes |
| Implementation | Can provide default implementations | Cannot provide implementations for abstract methods |

**33. Can you implement multiple interfaces in Java?**
Yes. A class can implement more than one interface — the `implements` keyword is followed by a comma-separated list. By convention, the `implements` clause follows the `extends` clause if there is one.

**34. What is a Java abstract class?**
A restricted class that cannot be used to create objects; to access it, it must be inherited from another class. An abstract method can only be used in an abstract class and has no body.

**35. What is the purpose of the `instanceof` operator?**
It checks whether an object is an instance of a particular class. `objectName instanceof ClassName` returns `true` if it is, `false` otherwise.
```java
if (myObject instanceof Dog) { ... } else if (myObject instanceof Animal) { ... }
```

**36. What are the different types of variables in Java?**
Three:
- **Local** — declared inside a method, constructor or block; only accessible in that scope; created on entry and destroyed on exit
- **Instance** — declared outside any method but inside a class; accessible to all methods in the class; created with the object and destroyed with it
- **Static** — declared with `static`; shared among all instances; created when the class is loaded and destroyed when it is unloaded

**37. How do you declare and initialise a variable in Java?**
```java
int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
```

**38. What is the purpose of the `volatile` keyword?**
It indicates that a variable's value can be modified by different threads. It ensures that changes made to a volatile variable by one thread are **immediately visible** to other threads.
```java
private volatile boolean running = true;
```

**39. What is the purpose of the `transient` keyword?**
A variable modifier used in the context of **serialization**. Applying it instructs the JVM to **exclude that variable from serialization** — transient variables are not saved in the serialized form of the object. After deserialization the field comes back as `null` (or its default value).

**40. What is a Java array?**
A data structure that stores a fixed-size sequence of elements of the same data type. An array is an **object** in Java, so it can be assigned to a variable, passed as a method parameter, and returned from a method.

## A41–A50: Arrays, Object methods, exceptions

**41. How do you declare and initialise an array?**
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
int[] myNum = {10, 20, 30, 40};
for (int i = 0; i < myArray.length; i++) System.out.println(myArray[i]);
```

**42. What is the length of an array in Java?**
The theoretical maximum Java array size is 2,147,483,647 elements. To find the size, query the array's `length` **property**. The size is set permanently when the array is initialised, and the count includes both null and non-null entries.
```java
int[] arr = new int[5];
System.out.println(arr.length);   // 5
```

**43. What is the difference between an Array and an ArrayList?**
An array has a fixed size that cannot change after creation, can store both primitives and objects, is accessed by index, is sorted with `Arrays.sort()`, can be multidimensional, cannot store nulls (for primitives), and is generally faster but less flexible.
An ArrayList is a resizable array, can only store object types, is accessed through methods (`get()`, `add()`, `remove()`), supports efficient insertion and deletion, is sorted with `Collections.sort()`, is single-dimensional only, can store null values, and is slower but more flexible.

**44. What is the purpose of the `clone()` method?**
`clone()` is Java's method for object duplication. Objects are manipulated through reference variables and there is no operator for copying an object — the assignment operator duplicates the *reference*, not the object. `clone()` provides that missing functionality.

**45. What is the purpose of the `toString()` method?**
A pre-existing method in the `Object` class that returns a string representation of an object. By default it produces the class name, an `@` symbol and the hash code. Overriding it lets you return meaningful content.
```java
@Override public String toString() { return "Person{name='" + name + "', age=" + age + "}"; }
```

**46. What is the purpose of the `equals()` method?**
It compares the **value** of two objects. It is an instance method of the `Object` class — the parent of all classes — so it can compare any two objects in Java.

**47. What is the purpose of the `hashCode()` method?**
A built-in method that returns an integer hash code representing the value of the object. It plays a crucial role in data retrieval, especially with hash-based collections like `HashMap` and `HashSet`.

**48. What is the purpose of the `getClass()` method?**
A method of `Object` in `java.lang` that returns the **runtime class** of `this`. The returned class object is locked by the static synchronized method of the represented class.
```java
Object obj = new String("Hello, world!");
System.out.println(obj.getClass().getName());
```

**49. What is exception handling in Java?**
Java uses exceptions to handle errors and other exceptional events — the process of responding to unwanted or unexpected events when a program runs. There are five keywords: **try, catch, throw, throws, finally.**

**50. Explain try, catch and finally blocks.**
- **try** — encloses code that might throw an exception. If one occurs, it is handled by an associated exception handler. A try block must contain at least one catch block or a finally block.
- **catch** — handles the exception. It must be used after the try block only, and you can have multiple catch blocks with a single try.
- **finally** — executes important code such as closing a connection or a stream. It is **always executed** whether an exception was handled or not, and follows a try or catch. Each try can have zero or more catch blocks but only one finally. It will **not** run if the program exits via `System.exit()` or a fatal error aborts the process.

## A51–A60: Exceptions, Strings, ArrayList

**51. What is the purpose of the `throw` and `throws` keywords?**
- **`throw`** explicitly throws an exception from a method or block. It can throw checked or unchecked exceptions and is followed by an *instance* of an exception.
- **`throws`** declares exceptions. It does not throw one — it specifies that a method **might** throw, typically to inform callers of what they may encounter.

**52. What is the difference between checked and unchecked exceptions?**

| Checked | Unchecked |
|---|---|
| Occur at compile time | Occur at runtime |
| The compiler checks for them | The compiler does not check |
| Can be handled at compilation time | Cannot be caught or handled at compile time |
| A subclass of the Exception class | Not part of the Exception class — they are runtime exceptions |
| The JVM requires them to be caught and handled | The JVM does not require handling |
| Example: `FileNotFoundException` | Example: `NoSuchElementException` |
| Usually external causes | Usually mistakes in the program |

**53. What is the purpose of the try-with-resources statement?**
A try statement that declares one or more resources. A resource is an object that must be closed after the program finishes with it. try-with-resources ensures each resource is closed at the end of the statement's execution.
```java
try (BufferedReader br = new BufferedReader(new FileReader("myfile.txt"))) {
    String line;
    while ((line = br.readLine()) != null) System.out.println(line);
}
```

**54. What is a Java String?**
A sequence of characters that exists as an object of the class `java.lang.String`. Strings are created and manipulated through the String class, and once created a String is **immutable** — its value cannot be changed.

**55. How do you create and manipulate Strings?**
Strings are immutable. You can create one with `new String("Hello World")` or with a string literal `"Hello World"`.
Common methods: `length()`, `charAt()`, `substring()`, `indexOf()`, `lastIndexOf()`, `replace()`, `toUpperCase()`, `toLowerCase()`.

**56. What is the difference between String, StringBuilder and StringBuffer?**
- **String** — immutable; cannot be changed after creation. String objects are stored in the **String pool**, a shared area of memory used for all String objects in a program.
- **StringBuilder** — mutable; can be changed after creation, and is not stored in the String pool.
- **StringBuffer** — also mutable and not stored in the String pool; it is **thread-safe** because its methods are **synchronized**, which makes it slower than StringBuilder.

**57. What is a Java ArrayList?**
A resizable array class in the `java.util` package. Built-in arrays have a fixed size, but ArrayLists change size dynamically — elements can be added and removed whenever needed, which helps with memory management.

**58. How do you create and manipulate ArrayLists?**
Import `java.util.ArrayList`, then create one: `ArrayList<String> languages = new ArrayList<>();`
Methods: `get()` returns an element; `set()` changes one; `remove()` removes one; `size()` returns the number of elements; `isEmpty()` checks whether it is empty; `contains()` checks for a specific element; `clear()` removes everything.

**59. What is the purpose of the Iterator interface?**
The Iterator interface lets you access the elements of a collection (Map, List or Set) and iterate over them, retrieving elements easily and performing operations on each.
Three methods: `hasNext()` returns true if there are more elements; `next()` returns the next element; `remove()` removes the last element returned by `next()`.

**60. What is a Java HashMap?**
`HashMap` stores data in (key, value) pairs, accessed by a key of another type. One object is the key (index) to another object (the value). Inserting a duplicate key replaces the value of the corresponding key.
Key features: stores elements in key-value pairs; is **unsorted** so insertion order is not preserved; allows **one null key** and **multiple null values**; provides efficient access and manipulation based on unique keys.

## A61–A70: HashMap, HashSet, LinkedList

**61. How do you create and manipulate HashMaps?**
```java
Map<String, Integer> numberMapping = new HashMap<>();
numberMapping.put("One", 1);
numberMapping.put("Two", 2);
System.out.println(hashMap.get("John"));
hashMap.remove("Jim");
System.out.println(hashMap.containsKey("Jim"));
```

**62. What is the purpose of the `entrySet()` method in HashMap?**
It converts the elements within a HashMap into a **Set**, giving a convenient way to access and manipulate the stored elements. It is the standard way to iterate over map entries, and can also remove entries.
```java
for (Map.Entry<String, Integer> entry : map.entrySet())
    System.out.println(entry.getKey() + " : " + entry.getValue());

map.entrySet().removeIf(entry -> entry.getKey().equals("one"));
```

**63. What is the purpose of `put()` and `get()` in HashMap?**
`put()` adds a new key-value pair; `get()` retrieves the value associated with a given key. `put()` returns the previous value for that key, or null if there was none. `get()` returns the value, or null if the key is absent.

**64. What is the purpose of `remove()` in HashMap?**
It removes the mapping and returns the previous value associated with the specified key (or true if the mapping is removed). Useful to remove an item that is no longer needed, is causing problems, or is outdated.

**65. What is a Java HashSet?**
A class from the Collections Framework that lets you store multiple values in a collection using a **hash table**. The hash table stores values in an unordered way using a hashing mechanism.
Methods: `add(E e)`, `contains(Object o)`, `remove(Object o)`, `size()`, `isEmpty()`, `clear()`.

**66. How do you create and manipulate HashSets?**
Add elements with `add()`, print with `println()`, check existence with `contains()`, and remove with `remove()`.
```java
HashSet<String> names = new HashSet<>();
names.add("John"); names.add("Alice"); names.add("Bob");
names.contains("Alice");   // true
names.remove("Bob");
```

**67. What is the purpose of `add()` in HashSet?**
It adds a specific element to a HashSet — but **only if the element is not already present**. If it is already there, the method returns `false`.

**68. What is the purpose of `remove()` in HashSet?**
`remove()` is in the HashSet class inside `java.util`. It removes only the specified element from the HashSet.

**69. What is a Java LinkedList?**
A dynamic data structure whose size increases as you add elements and decreases as you remove them. Elements are stored in containers, and the list holds the link to the first container.

**70. How do you create and manipulate a LinkedList?**
Import `LinkedList` from `java.util`; create with `new`; add with `add()`; remove with `remove()`; get the size with `size()`; check emptiness with `isEmpty()`; iterate with a for-each loop.

## A71–A84: Collections methods, Comparator, Object methods

**71. What is the purpose of `add()` and `remove()` in LinkedList?**
`add()` takes an element and adds it to the **end** of the list. `remove()` takes an element and removes the **first occurrence** of it.

**72. What is a Java TreeSet?**
An implementation of a **red-black tree** in Java. `TreeSet` maintains a **sorted order** for storing unique elements.

**73. What is the purpose of `add()` and `remove()` in TreeSet?**
`add()` adds a new element to the set. If it is already present, `add()` does nothing and returns `false`; otherwise it adds it and returns `true`.
`remove()` removes an element. If it is absent, it does nothing and returns `false`; otherwise it removes it and returns `true`.

**74. What is the purpose of `contains()` in Java Collections?**
`contains()` of `AbstractCollection` checks whether an element is present in a collection. It takes the element as a parameter and returns `true` if it is present.

**75. What is the purpose of `isEmpty()`?**
A convenient way to check whether a collection is empty. It is available in all collection interfaces, so it works with any collection type.

**76. What is the purpose of `size()`?**
It returns the number of elements in a collection — useful for determining the length and for iterating. Internally it simply reads the variable tracking the element count, which is updated on every add and remove. Available in `List`, `Set` and `Map`.

**77. What is the purpose of `clear()`?**
`clear()` of the Collection interface removes **all** the elements from the collection. It returns `true` if it successfully empties it.

**78. What is the purpose of `toArray()`?**
It converts an ArrayList into an array. It either takes no parameter, or takes an array of type `T[]` into which the list's elements will be stored. With no argument it returns an `Object` array.
```java
String[] array = list.toArray(new String[0]);
```

**79. What is the purpose of the `iterator()` method?**
It returns an Iterator that lets you access and iterate over the elements of a collection (Map, List or Set), so you can easily retrieve elements and perform operations on each. The Iterator provides `hasNext()`, `next()` and `remove()`.

**80. What is the Java Comparator?**
An interface used to order the objects of user-defined classes. A Comparator object can compare two objects of the same class. It provides a single method, `compare(T o1, T o2)`, returning an integer indicating whether the first object is less than, equal to, or greater than the second. It can be used with `Collections.sort()` and `Arrays.sort()`, and to create sorted sets and maps.

**81. How do you implement custom sorting using a Comparator?**
Define the class representing your objects, then create a comparator class implementing `Comparator`. Override `compare()` to define how objects are compared, including multiple criteria.
```java
public class StudentComparator implements Comparator<Student> {
    @Override public int compare(Student s1, Student s2) {
        int nameComparison = s1.getName().compareTo(s2.getName());
        return nameComparison == 0 ? s1.getAge() - s2.getAge() : nameComparison;
    }
}
students.sort(new StudentComparator());
```

**82. What is the purpose of `compareTo()`?**
It returns an integer representing the comparison result. If the result is less than 0, `str1` comes before `str2` in lexicographical order; greater than 0 means it comes after; 0 means both are equal.

**83. What is the purpose of `equals()`?** (repeat of Q46)
It compares the value of two objects. As an instance method of `Object` — the parent class of all classes — it can compare any two objects in Java.

**84. What is the purpose of `hashCode()`?** (repeat of Q47)
It returns an integer hash code representing the object's value. It plays a crucial role in data retrieval, especially with collections like `HashMap` and `HashSet`.

## A85–A94: Threads, synchronization, deadlock

**85. What is a Java thread?**
The direction or path taken while a program is executed. Generally all programs have at least one thread — the **main thread** — provided by the JVM at the start of execution.

**86. How do you create and start a thread in Java?**
Two ways:
1. By extending the `Thread` class and overriding `run()`
2. By implementing the `Runnable` interface and passing an instance to the `Thread` constructor

Once created, start it by calling `start()`. The thread then runs concurrently with the main thread until `run()` finishes.
```java
public class MyThread extends Thread {
    @Override public void run() { System.out.println("Hello from MyThread!"); }
}
new MyThread().start();

public class MyRunnable implements Runnable {
    @Override public void run() { System.out.println("Hello from MyRunnable!"); }
}
new Thread(new MyRunnable()).start();
```

**87. What is the difference between a thread and a process?**

| Feature | Thread | Process |
|---|---|---|
| Memory space | Shares the process's memory space | Has its own memory space |
| Stack | Has its own stack | Has its own stack |
| Creation | Created and destroyed by the JVM | Created and destroyed by the OS |
| Communication | Through shared memory | Through IPC (pipes, sockets, shared memory) |
| Weight | Lightweight unit of execution within a process | Independent unit of execution; can have multiple threads |

**88. What is synchronization in Java?**
The capability to control the access of multiple threads to any shared resource. In multithreading, multiple threads trying to access a shared resource at once produce inconsistent results. Synchronization is necessary for reliable communication between threads.

**89. How do you achieve synchronization in Java?**
With the `synchronized` keyword and the `volatile` modifier. `synchronized` defines critical sections of code that only one thread may access at a time. It can be applied to methods or code blocks.
```java
public synchronized void increment() { }
synchronized (obj) { }
```

**90. What is the purpose of the `synchronized` keyword?**
It is the tool for achieving thread safety and synchronization in multithreaded applications. Synchronized blocks or methods control concurrent access to shared resources, prevent data inconsistencies and ensure proper thread synchronization.

**91. What are the states of a thread in Java?**
Six:
1. **New** — the thread object has been created but is not yet runnable
2. **Runnable** — ready to run, waiting to be scheduled by the operating system
3. **Running** — currently executing
4. **Blocked** — waiting for an event, such as a lock becoming available
5. **Waiting** — waiting for another thread to finish executing
6. **Terminated** — finished executing

**92. What is deadlock in Java?**
A condition where two or more threads are blocked forever, waiting for each other. It usually happens when multiple threads need the same locks but obtain them **in different orders**. Multithreaded Java programs can suffer deadlock because of the `synchronized` keyword.

**93. How do you prevent deadlock in Java?**
- **Avoid unnecessary locking** — lock only when absolutely necessary and release as soon as possible
- **Acquire locks in a consistent order** — all threads should acquire locks in the same order
- **Avoid nested locks** — do not acquire a second lock while holding another
- **Use timeouts when acquiring locks** — prevents waiting indefinitely
- **Use lock-free data structures** designed for use by multiple threads without locks
- **Use a deadlock detection and avoidance algorithm** — complex, but effective when other methods are not feasible

Additional tips: use proper synchronization techniques when threads access the same data; be aware of the potential for deadlocks when designing; test your code thoroughly.

**94. What is the purpose of `wait()`, `notify()` and `notifyAll()`?**
They coordinate the actions of multiple threads and are part of the `Object` class, used to implement inter-thread communication.
- **`wait()`** — causes the current thread to wait indefinitely until another thread invokes `notify()` or `notifyAll()` on the same object
- **`notify()`** — wakes up a single thread waiting on that object's monitor
- **`notifyAll()`** — wakes up all threads waiting on that object's monitor

They are typically used with `synchronized` blocks to ensure only one thread accesses a shared resource at a time — for example, solving the producer-consumer problem. They must be used carefully to avoid race conditions and deadlocks.

---
---

# SECTION B — Spring Boot & Backend (Top 50)

## B1–B10: Spring Boot fundamentals

**1. What is Spring Boot?**
A Java-based framework built on top of the Spring Framework that simplifies the development of stand-alone, production-ready applications. It minimizes configuration through auto-configuration, starter dependencies and embedded servers, and is widely used for REST APIs, microservices and enterprise Java applications. Remember: **Spring Boot = convention over configuration.**

**2. What are the features of Spring Boot?**
Auto Configuration (configures beans based on the classpath); Starter Dependencies (predefined bundles simplifying Maven/Gradle); Embedded Servers (Tomcat, Jetty, Undertow — no external deployment); Spring Boot Actuator (health checks, metrics, monitoring); Spring Boot CLI (create and run applications from the command line); Externalized Configuration (properties, YAML, environment variables, command-line arguments); DevTools (automatic restart, LiveReload, developer productivity).

**3. What are the advantages of using Spring Boot?**
Embedded web servers; simplified dependency management; rapid development with auto-configuration; production-ready monitoring with Actuator; easy integration with Spring projects and third-party libraries; less boilerplate code and more productivity.
**Interview tip:** always mention "auto-configuration + starter dependencies + embedded servers" — these are the key differentiators.

**4. Define the key components of Spring Boot.**
Starter Dependencies; Auto Configuration; Spring Boot CLI; Actuator; Embedded Servers; Spring Boot Annotations (`@SpringBootApplication`, `@RestController`, `@Autowired`, etc.). They work together to make Spring Boot powerful, simple and production-ready.

**5. Why do we prefer Spring Boot over Spring?**

| Feature | Spring Framework | Spring Boot |
|---|---|---|
| Configuration | Mostly manual | Auto configuration |
| Dependency management | Manual | Starter dependencies |
| Embedded server | Not provided | Tomcat, Jetty, Undertow |
| Deployment | WAR on an external server | Executable JAR/WAR |
| Boilerplate | More | Less |
| Development speed | Slower | Faster |
| Production features | Requires additional setup | Built-in Actuator |
| Microservices support | Possible | Excellent |

Spring Boot reduces manual configuration, speeds up development and provides production-ready features out of the box.
*Common follow-ups:* Is Spring Boot a replacement for Spring? (No.) Can we use Spring Boot without the Spring Framework? (No — it is built on it.)

**6. Explain the internal working of Spring Boot.**
1. The client sends an HTTP request (GET, POST, PUT, DELETE)
2. The request is received and mapped to the appropriate controller method (`@RestController`)
3. The controller forwards it to the service layer (`@Service`)
4. The service layer executes business logic
5. The service interacts with the repository (`@Repository`, JPA/Hibernate) for database operations
6. The repository communicates with the database and returns the result
7. The response (JSON/XML/View) goes back to the client

Always mention the flow **in layers** (Controller -> Service -> Repository -> Database) and highlight separation of concerns. Understanding the flow helps in debugging, performance tuning and designing scalable applications. Spring Boot follows a layered architecture based on the **Inversion of Control (IoC)** principle.

**7. What are Spring Boot starter dependencies?**
Preconfigured dependency descriptors that include commonly used libraries for a specific functionality.

| Starter | Purpose |
|---|---|
| `spring-boot-starter-web` | Web and REST applications |
| `spring-boot-starter-data-jpa` | Database access using JPA |
| `spring-boot-starter-security` | Authentication and authorization |
| `spring-boot-starter-test` | Unit and integration testing |
| `spring-boot-starter-thymeleaf` | Thymeleaf template engine |
| `spring-boot-starter-validation` | Bean validation |
| `spring-boot-starter-actuator` | Monitoring and health checks |

Starters save time, reduce boilerplate and ensure compatibility. But more starters means more dependencies, higher memory use and slower startup.

**8. How does a Spring application get started?**
The `main()` method is the entry point. It calls `SpringApplication.run()`, which bootstraps the application. Spring Boot starts the embedded server (Tomcat/Jetty/Undertow). The application context is created and all beans are initialised. Dependency injection is performed and the application is wired. The application is then ready to handle incoming requests.
Remember: `@SpringBootApplication` -> `SpringApplication.run()` -> `ApplicationContext`.

**9. What is `@SpringBootApplication`?**
A single annotation combining three:
- `@Configuration` — indicates a configuration class
- `@EnableAutoConfiguration` — enables Spring Boot auto-configuration
- `@ComponentScan` — scans the current package for components

It makes the main class powerful by enabling auto-configuration, scanning components and registering bean definitions.

**10. What is the use of `application.properties` (or `application.yml`)?**
It holds externalized configuration for the application, stores environment-specific settings, supports easy configuration without code changes, and supports placeholders, profiles and command-line overrides.
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.jpa.hibernate.ddl-auto=update
```
Use `application.yml` for hierarchical and complex configurations.

## B11–B20: Annotations and configuration

**11. What is the difference between `@Component`, `@Service`, `@Repository` and `@Controller`?**

| Annotation | Purpose | Used in |
|---|---|---|
| `@Component` | Generic Spring-managed bean | Any layer |
| `@Service` | A service-layer class containing business logic | Service layer |
| `@Repository` | Data access. Also provides **exception translation** | Persistence layer |
| `@Controller` | Handles web requests and returns views | Web layer |
| `@RestController` | Combination of `@Controller` and `@ResponseBody` | REST APIs |

`@Service`, `@Repository` and `@Controller` are specializations of `@Component` with clearer intent and better readability. Use the right annotation at the right layer for a clean architecture.

**12. What is auto-configuration in Spring Boot?**
Auto-configuration automatically configures Spring beans based on the libraries on the classpath and the configuration you have defined.
How it works: Spring Boot scans the classpath; if the required libraries are present it applies suitable configuration; bean definitions are created automatically; and you can override it by providing your own configuration. It reduces manual configuration and speeds up development.

**13. What is Spring Boot Actuator?**
It provides production-ready features to monitor and manage your application: health checks, metrics (JVM, HTTP requests, DB), application info, beans list, environment properties and loggers. Endpoints include `/actuator/health`, `/actuator/metrics`, `/actuator/info`, `/actuator/beans`, `/actuator/env`, `/actuator/loggers`. Expose only required endpoints in production for security.

**14. What is the use of `@SpringBootApplication`?** (see Q9)
It is placed on the main class and triggers component scanning, auto-configuration and Spring Boot features. It is a combination of `@Configuration`, `@EnableAutoConfiguration` and `@ComponentScan`.

**15. What is `@RestController`?**
A stereotype annotation used to create RESTful web services — a combination of `@Controller` and `@ResponseBody`. It handles HTTP requests, returns data (JSON/XML) directly in the response body, performs no view resolution, and is widely used for building REST APIs.

**16. What is `@RequestMapping`?**
It maps web requests to handler methods or controller classes. It can be used at class or method level, supports GET, POST, PUT, DELETE and others, and lets you define a base path at class level and specific paths at method level.

**17. What is `@PathVariable`?**
It extracts values from the URI template. The value inside `{ }` in the URL is mapped to the method parameter, and the parameter name must match the variable name (or use `@PathVariable("name")`).
```java
@GetMapping("/users/{id}")
public ResponseEntity<User> getUser(@PathVariable Long id) { ... }
// GET /users/101 -> id = 101
```

**18. What is `@RequestParam`?**
It extracts query parameters from the URL. Use `required = false` or `defaultValue` for optional parameters, and it supports default values.
```java
@GetMapping("/search")
public List<Product> search(@RequestParam String name,
                            @RequestParam(defaultValue = "0") int page) { ... }
// GET /search?name=mobile&page=1
```

**19. What is `@RequestBody`?**
It accepts JSON (or XML) data in the request body and binds it to a Java object. The body is converted using an `HttpMessageConverter`, and it is commonly used in POST, PUT and PATCH requests. The `Content-Type` should be `application/json`.

**20. What are `@GetMapping`, `@PostMapping`, `@PutMapping` and `@DeleteMapping`?**
Composed annotations that map HTTP requests to specific handler methods: `@GetMapping` handles GET (fetch data), `@PostMapping` handles POST (create data), `@PutMapping` handles PUT (update data), and `@DeleteMapping` handles DELETE. Use the correct method to follow REST principles.

## B21–B30: Injection, annotations, scopes

**21. What is the difference between `@Autowired` and `@Resource`?**

| | `@Autowired` | `@Resource` |
|---|---|---|
| Package | `org.springframework.beans.factory.annotation` | `jakarta.annotation` |
| Injection | By type (default) | By name (default) |
| If multiple beans | Must use `@Qualifier` | Matches by name |
| Required | `required = true` (default) | `required = true` (default) |
| Used on | Fields, setters, constructors | Fields, setters |

Use `@Autowired` in Spring applications unless you specifically need name-based injection.

**22. What is the difference between `@Controller` and `@RestController`?**
`@Controller` handles web requests and returns **views** (HTML/JSP/Thymeleaf). `@RestController` is a combination of `@Controller` and `@ResponseBody` — it builds REST APIs and returns JSON/XML directly in the response body. Use `@Controller` for traditional web apps and `@RestController` for REST APIs.

**23. What is the use of the `@Repository` annotation?**
It marks a class as a data-access-layer component. It indicates that the class provides database access, **automatically translates database exceptions into Spring's `DataAccessException`**, enables exception consistency, and is usually used with Spring Data JPA. It acts as the bridge between the application and the database. All repository interfaces extend `JpaRepository` or `CrudRepository`.

**24. What is `@Autowired`?**
It performs automatic dependency injection, injecting the required bean **by type**. If multiple beans of the same type exist, use `@Qualifier`. It can be used on fields, constructors or setter methods. The Spring container looks for a bean of the required type and injects it automatically — no need to create the object manually. It reduces boilerplate and improves readability.

**25. What is the difference between constructor injection and setter injection?**

| Constructor injection | Setter injection |
|---|---|
| Dependencies are passed through the constructor | Dependencies are injected using setter methods |
| Ensures immutability | Allows optional dependencies |
| Mandatory dependencies are injected at object creation | Can be changed after object creation |
| Preferred for required dependencies | Less preferred for mandatory dependencies |
| Cannot be changed after object creation | |

**Prefer constructor injection for mandatory dependencies and setter injection for optional ones.**

**26. What is the use of the `@Service` annotation?**
A stereotype annotation indicating that a class belongs to the **service layer**. It marks the class as a Spring service component, contains the application's business logic, is detected automatically by component scanning, and promotes loose coupling and separation of concerns. It keeps business logic separate from the controller and repository layers. Service classes are autowired into controllers and other services.

**27. What is the use of the `@Component` annotation?**
A stereotype annotation marking a class as a Spring-managed component (bean). It marks the class as a Spring bean, is detected during component scanning, and is used for general-purpose components that do not fit a specific category. Prefer the specific annotations (`@Service`, `@Repository`, `@Controller`) for better readability and role clarity.

**28. What is the use of the `@Value` annotation?**
It injects values from properties files, environment variables or SpEL expressions into fields, constructors or methods. It supports default values.
```java
@Value("${server.port}")           private int port;
@Value("${app.name:MyApp}")        private String appName;   // with default
@Value("#{10 * 5}")                private int result;       // SpEL
```
Use `@Value` for simple values; use `@ConfigurationProperties` for complex configuration.

**29. What is the `@Qualifier` annotation?**
Used with `@Autowired` to resolve ambiguity when multiple beans of the same type exist. It specifies which bean to inject by name, works with field, constructor, setter and method injection, and reduces confusion when multiple beans of the same type are present. It works only with `@Autowired`, not with `@Resource`.

**30. What is the use of the `@Configuration` annotation?**
It indicates that a class contains one or more `@Bean` methods and can be used by the Spring IoC container as a source of bean definitions. It marks the class as a source of bean definitions, replaces XML-based configuration, allows defining `@Bean` methods, and the class is enhanced with a CGLIB proxy to manage those methods. It provides a central place to configure beans using Java code instead of XML.

## B31–B40: Scopes, lifecycle, configuration

**31. What are the bean scopes supported in Spring Boot?**
A bean scope defines the lifecycle and visibility of a bean within the container.

| Scope | Meaning | Use case |
|---|---|---|
| **singleton** | **Default** — a single instance per Spring IoC container | Most common |
| **prototype** | A new instance every time the bean is requested | When a fresh instance is required |
| **request** | A new instance per HTTP request | Web applications |
| **session** | A new instance per HTTP session | User-specific data in session |
| **application** | A single instance per ServletContext | Application-wide objects |
| **websocket** | A new instance per WebSocket connection | WebSocket-specific data |

Singleton is the default; the others are web-aware scopes.

**32. What are the lifecycle phases of a Spring bean?**
1. **Instantiation** — the bean is created using the constructor
2. **Populate properties** — dependencies are injected
3. **Initialization** — `@PostConstruct` or `afterPropertiesSet()` is called
4. **Bean in use** — ready and available
5. **Destruction** — `@PreDestroy` or `destroy()` is called

The Spring IoC container manages the entire lifecycle. Initialization and destruction callbacks are optional, and the scope affects the lifecycle (singleton vs prototype).

**33. What is the difference between `@Bean` and `@Component`?**

| Feature | `@Bean` | `@Component` |
|---|---|---|
| Definition | Method-level annotation used inside a `@Configuration` class | Class-level annotation on regular classes |
| Purpose | Tells Spring to create a bean using the method's return value | Tells Spring to create a bean by scanning the class |
| Where used | Inside a `@Configuration` class only | On any Spring-managed class |
| Flexibility | More flexible — you control bean creation manually | Less flexible — Spring controls creation |
| Dependencies | Passed as method parameters | Injected with `@Autowired` or a constructor |
| Use case | Fine-grained control over bean creation | When you want Spring to manage the component automatically |

Use `@Bean` when you need custom logic while creating the bean; use `@Component` for automatic component scanning.

**34. What is the difference between `@Primary` and `@Qualifier`?**

| Feature | `@Primary` | `@Qualifier` |
|---|---|---|
| Purpose | Resolves which bean to inject when multiple of the same type exist by marking one as primary | Specifies exactly which bean to inject, by name |
| How it works | Used implicitly | Used at the injection point to choose a specific bean |
| Scope | Class level, on the bean definition | Field, parameter or method level, at the injection point |
| When used | When only one clearly preferred bean exists | When you need a specific bean out of multiple options |

Use `@Primary` for the default preference and `@Qualifier` for explicit selection.

**35. What is the use of the `@Bean` annotation?**
It declares a method that produces a bean to be managed by the Spring container. It is used in a `@Configuration` class, the returned object is registered as a bean, it allows custom bean creation, and it gives more control over initialization. Use `@Bean` when you do not own the class or need to register a third-party object.

**36. What is Spring Boot auto-configuration?** (see Q12)
It automatically configures Spring beans based on the libraries present on the classpath and the configuration you have defined. Spring Boot scans the classpath, checks available libraries, applies auto-configuration rules and creates beans. It uses the spring.factories / AutoConfiguration import mechanism. Examples: if `spring-boot-starter-web` is on the classpath, Tomcat and Spring MVC are auto-configured; if `spring-boot-starter-data-jpa` is present, `DataSource`, `EntityManagerFactory` and JPA are auto-configured. **Convention over configuration is the heart of auto-configuration.**

**37. How can we disable auto-configuration?**
Three ways:
1. `@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})`
2. Add class names in `application.properties`: `spring.autoconfigure.exclude=...`
3. Use `@EnableAutoConfiguration(exclude = ...)` on a `@Configuration` class

Disable only when you need full control or want to replace default behaviour. Avoid disabling auto-configuration unless absolutely necessary.

**38. How does Spring Boot handle externalized configuration?**
Spring Boot supports external configuration from multiple sources, making applications flexible across environments.
**Priority, high to low:**
1. Command-line arguments
2. Environment variables
3. `application-{profile}.yml` / `.properties`
4. `application.yml` / `.properties`
5. `@PropertySource` and `RandomValuePropertySource`
6. Default properties

It supports `.properties`, `.yml`, environment variables and CLI arguments, and profile-based configuration for switching between dev, test and prod.

**39. What is the difference between `application.properties` and `application.yml`?**

| Feature | `application.properties` | `application.yml` |
|---|---|---|
| Format | Key-value pairs | YAML (hierarchical) |
| Readability | Less readable for complex data | More readable for nested data |
| Data types | Only String | String, List, Map, etc. |
| Structure | Flat | Hierarchical |
| Comments | `#` | `#` |
| Use case | Simple configurations | Complex configurations |

Both are supported; YAML is more powerful for complex structured data.

**40. What is Spring Boot DevTools?**
A module that improves developer productivity: automatic restart on code changes, LiveReload for the browser, disabled caching, and global settings. Add the `spring-boot-devtools` dependency in `pom.xml`. It is enabled by default in development but **not in production**.

## B41–B50: Actuator, CLI, IoC and DI, microservices

**41. What is Spring Boot Actuator?** (see Q13)
It provides production-ready features to monitor and manage your application. It helps with monitoring, managing and troubleshooting, provides built-in endpoints, can be secured for sensitive information, and is extensible with custom endpoints. Endpoints feed monitoring tools like Prometheus and Grafana.

**42. How can we secure Actuator endpoints?**
Using Spring Security, restricting access to authenticated users or specific roles.
```properties
management.endpoints.web.exposure.include=health,info
management.endpoints.web.base-path=/actuator
```
Use Spring Security to restrict access, expose only necessary endpoints, use roles/authorities for sensitive endpoints, and use HTTPS in production. **Never expose all endpoints in production without security.**

**43. What is the use of the Spring Boot CLI?**
A command-line tool that helps develop and test Spring Boot applications quickly. You can run Spring applications without packaging, quickly test snippets of code, create projects from templates, use Groovy for scripting, and learn and prototype rapidly.

| Command | Purpose |
|---|---|
| `spring --version` | Check the CLI version |
| `spring init <project>` | Create a project from a template |
| `spring run <file>` | Run an application |
| `spring shell` | Open an interactive shell |

**44. What are the advantages of using Actuator?**
Health monitoring (check the health of the application and its components); metrics collection (JVM, HTTP, DB performance); application information (environment, components, configuration); easier troubleshooting in production; and friendly integration with monitoring tools like Prometheus and Grafana.
Best practices: expose only required endpoints, secure them with authentication, and combine with monitoring tools.

**45. What are the key annotations in Spring Boot?**

| Annotation | Purpose |
|---|---|
| `@SpringBootApplication` | The main annotation, combining `@Configuration`, `@EnableAutoConfiguration` and `@ComponentScan` |
| `@RestController` | Marks a class as a REST controller (`@Controller` + `@ResponseBody`) |
| `@RequestMapping` | Maps HTTP requests to handler methods at class or method level |
| `@PathVariable` | Extracts a value from the URI path |
| `@RequestParam` | Extracts query parameters from the URL |
| `@Service` | Marks a class as a service component |
| `@Repository` | Marks the data access / repository layer (with exception translation) |
| `@Autowired` | Automatically injects a dependency (constructor, field or setter) |

They reduce boilerplate code and configuration, improve readability and maintainability, follow Spring best practices, and enable auto-configuration and dependency injection.

**46. What is IoC (Inversion of Control) in Spring?**
A design principle where the control of object creation, configuration and lifecycle management is **transferred from the application code to the Spring container**. The Spring container creates objects, manages dependencies and lifecycle, promotes loose coupling and makes testing easier.
Think of Spring as a factory that builds and manages objects for you.

**47. What is Dependency Injection (DI) in Spring?**
A technique where the dependencies (required objects) are **provided to a class by the Spring container** instead of the class creating them itself.
Three types:
1. **Constructor injection** — dependencies are provided via the constructor
2. **Setter injection** — dependencies are provided via a setter method
3. **Field injection** — dependencies are injected directly into fields

It removes hard-coded dependencies and makes the application loosely coupled. **Prefer constructor injection for mandatory dependencies.**

**48. What is the difference between IoC and DI?**

| | IoC (Inversion of Control) | DI (Dependency Injection) |
|---|---|---|
| Definition | A design principle that transfers control to the container | An implementation technique to provide dependencies to a bean |
| Scope | The broader concept | A subset of IoC |
| Focus | Manages object creation and lifecycle | Provides objects to a bean |
| Who does it | The Spring container | The Spring container |
| Example | Spring creates and manages beans | Spring injects `UserRepository` into `UserService` |

**All DI is IoC, but not all IoC is DI.** Analogy: IoC is the factory; DI is the delivery of parts to the car.

**49. What are the benefits of IoC and DI?**
*IoC:* centralized control over configuration and lifecycle, encourages loose coupling, makes unit testing easy (mock dependencies), supports AOP, transactions and caching, enhances application modularity.
*DI:* reduces tight coupling, easier testing and maintenance, improves code reusability, easy to replace dependencies, improves scalability and flexibility.
Whenever you see `@Autowired`, constructor injection or setter injection, you are using DI — a part of IoC.

**50. How does Spring Boot support microservices?**
- **Lightweight and fast** — minimal dependencies and quick startup, perfect for small services
- **Embedded servers** — comes with embedded Tomcat/Jetty
- **Auto-configuration** — reduces boilerplate so you focus on business logic
- **Actuator** — health, metrics and info endpoints per service
- **Easy integration** — seamless with databases, Redis, Kafka, RabbitMQ
- **Cloud ready** — works with Spring Cloud for discovery (Eureka), config server, API gateway, routing and scaling

*Benefits:* independent deployment, fault isolation, scalability, technology flexibility, easier maintenance, high availability.
*Best practices:* keep services small and single-purpose, use meaningful service names, monitor each service, use centralized config management, and secure services (SSL, OAuth2, roles).

**The formula to remember:** Spring Boot + IoC + DI + Actuator = fast, scalable, maintainable backend applications.

## B51+ Bonus: Spring "senior-level" trade-off questions

**B51. What is the difference between IoC and DI (senior answer)?**
"IoC is the principle — the framework controls object creation instead of my code. DI is how Spring implements it: it injects the dependencies a class declares, usually through the constructor. So IoC is the idea, DI is the mechanism."
*Gotcha:* field injection compiles fine but hides dependencies and blocks `final` fields — say **constructor injection** in the interview.

**B52. How does Spring Boot auto-configuration work (senior answer)?**
"At startup Boot reads a list of auto-configuration classes shipped in the starters, then evaluates conditions on each one. If the class is on the classpath and I haven't defined that bean myself, it creates it. That's why adding `spring-boot-starter-web` gives me an embedded Tomcat with no config."
*Gotcha:* run with `--debug` to print the condition evaluation report — it shows exactly what matched and why.

**B53. Is there any real difference between `@Component` and `@Service`?**
"Functionally almost none — both register a bean. The difference is intent, which matters for readability and for AOP targeting. The one real exception is `@Repository`, which adds automatic translation of persistence exceptions into Spring's `DataAccessException` hierarchy."
*Gotcha:* `@Configuration` is proxied with CGLIB, plain `@Component` is not — calling one `@Bean` method from another only stays a singleton inside `@Configuration`.

**B54. Walk me through what happens when a request hits your Spring Boot app.**
"The request goes through the filter chain, then `DispatcherServlet`. It asks `HandlerMapping` which controller method matches, invokes it through a handler adapter, and the controller delegates to the service and repository. On the way back, an `HttpMessageConverter` serialises the returned object into JSON and writes the response."
*Gotcha:* returning your JPA entity straight from the controller leaks the schema and triggers lazy-loading errors — map to a DTO.

**B55. What makes an API RESTful, and when would you not use REST?**
"Resource-based URLs, standard HTTP verbs, stateless requests, and meaningful status codes. I'd move away from REST when the call is fire-and-forget or fans out to many consumers — that's a Kafka event. And when clients need very different shapes of the same data, GraphQL fits better."
*Gotcha:* PUT must be idempotent — sending it twice should leave the same state. If your PUT creates a second row, it is really a POST.

**B56. What is the N+1 problem and how do you fix it?**
"You load a list of parents, then every access to a lazy child fires its own query — one query becomes N plus one. I fix it with a `JOIN FETCH` query or an `@EntityGraph` so the children come back in the same round trip, and I check the generated SQL rather than assuming."
*Gotcha:* `FetchType.EAGER` looks like the fix and is the trap — it drags the whole object graph on every single read.

**B57. Why did your `@Transactional` method not roll back?**
"Usually one of three things: the exception was checked and I didn't set `rollbackFor`, the method was called from inside the same class so the proxy was bypassed, or the method wasn't public. **Self-invocation** is the one that catches people most often."
*Gotcha:* across microservices there is no distributed rollback — you need a Saga with compensating actions, not `@Transactional`.

**B58. What is the downside of JWT, and how do you handle logout?**
"A JWT is valid until it expires — you can't un-issue it. So I keep access tokens short-lived, a few minutes, and pair them with a refresh token I can revoke server-side. For immediate logout you need a deny-list, which quietly reintroduces state."
*Gotcha:* never put anything sensitive in the payload — it's base64, not encryption. Anyone can read it.

**B59. When would you tell a client NOT to go microservices?**
"Small team, single product, no scaling pain — then a well-modularised monolith wins. Microservices trade code complexity for operational complexity, and you need the CI/CD, monitoring and tracing to pay for it. I'd start modular and split along the seams that actually hurt."
*Gotcha:* a shared database between services is a distributed monolith — you get the latency without the independence.

**B60. How do you keep the cache from going stale?**
"Every entry gets a TTL so the worst case is bounded. On writes I evict or update the key in the same flow as the database write. For data where a few seconds of staleness is fine, I lean on a short TTL rather than complex invalidation — it's far easier to reason about."
*Gotcha:* `@Cacheable` on a method called from inside the same class does nothing — the proxy is bypassed, same trap as `@Transactional`.

**B61. How do you guarantee a Kafka message isn't lost or processed twice?**
"Producer side: `acks=all` with retries so the write is on every replica. Consumer side: commit the offset only after the work succeeds, and make the handler idempotent — usually by storing the event id and skipping duplicates. Delivery is at-least-once, so **idempotency** is what actually saves you."
*Gotcha:* ordering is only guaranteed within a partition. No key means round-robin, and your events arrive out of order.

**B62. What's the difference between liveness and readiness?**
"Liveness answers *should this pod be restarted* — the process is wedged. Readiness answers *can it take traffic right now*, which may be false while warming caches or when a downstream is down. Getting them backwards means Kubernetes restarts a perfectly healthy pod that was just busy."
*Gotcha:* only expose what you need. Leaving `/env` or `/heapdump` open in production is a real data leak.

**B63. How do you test code that talks to a database?**
"Repository logic against a real database in **Testcontainers**, so I'm testing the SQL that actually runs in production rather than H2's dialect. Service logic gets unit tested with the repository mocked. I keep full `@SpringBootTest` for a handful of critical paths because it's slow."
*Gotcha:* `@DataJpaTest` swaps in an embedded DB by default — add `@AutoConfigureTestDatabase(replace=NONE)` or Testcontainers is silently ignored.

---
---

# SECTION C — API & REST (100 Questions)

## C1–C30: API Basics

**1. What is an API?**
A set of rules and protocols that allows different software applications to communicate with each other.
*Real-time:* a weather app has no weather data built in — it calls a weather service API (like OpenWeatherMap), sends your location, and receives the current weather to display.

**2. What is a REST API?**
REST (Representational State Transfer) is an architectural style for designing networked applications that use HTTP methods to perform operations on resources.
*Real-time:* a food delivery app uses `GET /restaurants`, `POST /orders`, `GET /orders/{id}`, `DELETE /orders/{id}`.

**3. What are HTTP methods?**
Standard operations defined by the HTTP protocol for web communication.
```
GET    /api/products    # Get all products
POST   /api/cart        # Add item to cart
PUT    /api/users/123   # Update user profile
DELETE /api/comments/5  # Remove comment
PATCH  /api/orders/10   # Partially update order status
```

**4. Difference between GET and POST?**
GET retrieves data, has parameters visible in the URL, is bookmarkable, and has limited data capacity (e.g. `amazon.com/search?q=laptop`). POST submits data, keeps data in the request body (hidden), is not bookmarkable, and has larger data capacity (e.g. submitting a login form).

**5. What is an endpoint?**
A specific URL where an API can be accessed to perform operations.
```
GET  /api/accounts       -> List all accounts
GET  /api/accounts/{id}  -> Get a specific account
POST /api/transfers      -> Initiate a money transfer
GET  /api/transactions   -> View transaction history
```

**6. What is request and response?**
The **request** is what the client sends to the server; the **response** is what the server returns.
```
POST /api/login HTTP/1.1
Content-Type: application/json
{"username": "john", "password": "pass123"}

HTTP/1.1 200 OK
{"token": "abc123", "user": {"id": 1, "name": "John"}}
```

**7. What is JSON?**
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse. When you submit a registration form, your data is converted to JSON.

**8. What is an HTTP status code?**
A 3-digit code indicating the result of an HTTP request. 200 OK — the request succeeded; 404 Not Found — the page does not exist; 500 Internal Server Error — the website is down; 403 Forbidden — you are not allowed to access it.

**9. Common HTTP status codes?**
*Success:* 200 OK (successful), 201 Created (resource created — a new user registered), 204 No Content (success but nothing to return).
*Client errors:* 400 Bad Request (invalid input), 401 Unauthorized (not authenticated, missing token), 403 Forbidden (authenticated but not authorized), 404 Not Found, 429 Too Many Requests (rate limit exceeded).
*Server errors:* 500 Internal Server Error, 502 Bad Gateway (upstream server issue), 503 Service Unavailable (overloaded or in maintenance).

**10. What is a RESTful API?**
An API that follows REST architectural principles including statelessness, cacheability and proper use of HTTP methods.
```
GET    /products        -> list of products
POST   /products        -> create a new product (admin)
GET    /products/{id}   -> specific product details
PUT    /products/{id}   -> update the entire product
PATCH  /products/{id}   -> update the price only
DELETE /products/{id}   -> remove the product
```

**11. What is statelessness?**
Each request from client to server must contain all the information needed to understand and process it. The server does not store any client context between requests — which is why every authenticated request must carry its token.

**12. What is CRUD?**
Create, Read, Update, Delete.
```
Create: POST   /articles
Read:   GET    /articles/{id}
Update: PUT    /articles/{id}
Delete: DELETE /articles/{id}
```

**13. What is API testing?**
Verifying API functionality, performance, security and reliability — for example testing payment APIs for success, failure, load and edge cases.

**14. Tools for API testing?**
Postman, Swagger/OpenAPI, SoapUI. Also curl, Insomnia, Thunder Client, Newman, RestAssured.

**15. What is a payload?**
The data sent in the request or response body.
```json
{ "content": "Just launched my new app!", "privacy": "public" }
```

**16. What are headers?**
Key-value pairs sent with an HTTP request or response containing **metadata** about it. They do not contain the actual data, but tell the server how to process it. Headers are mainly used for authentication, content type, caching and client information.
```
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
Content-Type: application/json
Accept: application/json
```

**17. What is Content-Type?**
A header specifying the **format of the data being sent** in the request or response body — `application/json`, `multipart/form-data` for file upload. If the server receives JSON but Content-Type is missing or wrong, the request may fail. Always set it correctly for POST, PUT and PATCH.

**18. What is the Accept header?**
It tells the server which **response format** the client expects. A mobile app sending `Accept: application/json` gets JSON; a browser sending `Accept: text/html` gets an HTML page.
Remember: **Accept = response format, Content-Type = request format.**

**19. What is a query parameter?**
Key-value pairs appended to the URL after `?`, used for filtering, sorting, searching and pagination.
`GET /api/products?category=mobile&price=low&page=2` — category filters, price sorts, page paginates. Query parameters are optional.

**20. What is a path parameter?**
Variables embedded in the URL path that identify a specific resource. `GET /api/users/25` fetches user 25; `DELETE /api/orders/789` deletes order 789. Path parameters are **mandatory** and represent unique resource identifiers.

**21. Difference between query and path parameter?**

| Feature | Path Parameter | Query Parameter |
|---|---|---|
| Purpose | Identify a resource | Filter or modify the response |
| Mandatory | Yes | No |
| Position | Part of the URL path | After `?` |
| Example | `/users/10` | `/users?role=admin` |

In `GET /api/users/10?active=true`, `10` is a path param (a specific user) and `active=true` is a query param (a filter condition).

**22. What is API documentation?**
It explains how to use an API — endpoints, request formats, response formats and error messages. Examples: Stripe API docs (payments), Google Maps API docs (location), Twitter API docs. Good documentation reduces developer confusion and speeds up integration.

**23. What is Swagger / OpenAPI?**
A standard specification used to document REST APIs in a readable, interactive format. A frontend developer opens Swagger UI and sees all endpoints, tests APIs without Postman, and understands request/response formats. Benefits: interactive testing, auto-generated docs, client SDK generation.

**24. What is versioning in an API?**
Maintaining multiple versions of an API to support changes without breaking existing clients: `/api/v1/users` for old mobile apps, `/api/v2/users` for new ones. Versioning enables smooth upgrades and backward compatibility.

**25. Why is versioning important?**
It ensures existing applications keep working when APIs are updated. If a company changes a response from `{"name": "John"}` to `{"fullName": "John Doe"}`, old apps break without versioning but upgrade safely with it.

**26. What is a REST constraint?**
Rules that define how a REST API should behave. The key constraints are: Client-Server, Stateless, Cacheable, Uniform Interface, Layered System (plus optional Code on Demand). Example: a React frontend, a Node API backend and a database — each layer works independently.

**27. What is cache?**
Temporary storage of frequently accessed data to improve performance and reduce server load. In a weather app the first request is a slow API call; subsequent ones are served fast from the cache. Cache improves speed, scalability and user experience.

**28. What is CORS?**
CORS (Cross-Origin Resource Sharing) allows a server to specify which domains may access its resources. If the frontend is `https://myapp.com` and the backend is `https://api.myapp.com`, the server sends `Access-Control-Allow-Origin: https://myapp.com`. **CORS is a browser-side security feature, not backend logic.**

**29. What is the same-origin policy?**
A browser security rule preventing a webpage from accessing data from another origin. An origin is **protocol + domain + port**. `https://siteA.com -> https://siteB.com` is blocked; `https://siteA.com -> https://siteA.com/api` is allowed.

**30. What is API authentication?**
Verifying who is making the request before allowing access. Methods: **API keys** (`GET /api/data?api_key=abc123`, used in public APIs like maps and weather), **JWT tokens** (`Authorization: Bearer ...`, used in login-based systems), **OAuth** (login with Google/Facebook), and **Basic authentication** (`Authorization: Basic base64(username:password)`, used in internal or legacy systems).
Authentication = identity; authorization = permissions.

## C31–C60: Intermediate API concepts

**31. What is authentication vs authorization?**
Authentication answers "who are you?" — verifying identity. Authorization answers "what are you allowed to do?" — determining permissions after authentication.
*Real-time:* an employee logs into the HR system (authentication succeeds), then tries to access payroll data — an HR manager is allowed, an intern gets 403 Forbidden.

**32. What is JWT (JSON Web Token)?**
A compact, URL-safe token used to securely transmit information between client and server. It enables stateless authentication with no server-side session storage, and scales easily in microservices. A user logs into an e-commerce site, receives a JWT, and uses it to access orders, cart and profile.

**33. What is the structure of a JWT?**
Three parts separated by dots: `Header.Payload.Signature`.
- **Header** — token type and algorithm
- **Payload** — user data (claims), e.g. `{"userId": 123, "role": "admin", "exp": 1700000000}`
- **Signature** — verifies token integrity

**34. What is a Bearer token?**
An access token sent in HTTP headers to authenticate API requests: `Authorization: Bearer eyJhbGciOiJIUzI1NiIs...`. It is called "Bearer" because **whoever holds the token can access the resource** — so it must be protected.

**35. How does JWT work in real time?**
1. The user sends credentials (`POST /login`)
2. The server validates them
3. The server generates a JWT
4. The JWT is sent to the frontend
5. The frontend stores the token (localStorage or cookies)
6. The token is sent with every API request
7. The server verifies the token

**36. What is OAuth?**
An authorization framework that lets third-party apps access user data **without exposing passwords**. With "Login with Google", the app never sees your Google password — Google issues an access token, and the app accesses your profile and email with permission.

**37. What is a refresh token?**
A token used to obtain a **new access token** without requiring the user to log in again. The access token might expire in 15 minutes while the refresh token is valid for 7 days, giving a seamless experience without frequent logins.

**38. What is API rate limiting?**
Restricting the number of API requests a client can make within a time window, for example 100 requests per minute per user. It prevents abuse, protects server resources and ensures fair usage.

**39. Why is rate limiting important?**
A public API without limits attracts bot attacks, DDoS attempts and server crashes. The solution is to return `429 Too Many Requests`.

**40. What is idempotency?**
An operation is idempotent if performing it multiple times produces the same result. With `POST /payments` plus an idempotency key, a request retried after a network failure processes the payment **only once**.

**41. Which HTTP methods are idempotent?**
Idempotent: **GET, PUT, DELETE** (also HEAD and OPTIONS). Not idempotent: **POST** — it creates a new resource each time.

**42. What is pagination?**
Dividing large datasets into smaller chunks to improve performance. An Instagram feed loads 10 posts at a time and loads the next page as you scroll.

**43. Pagination example?**
`GET /api/posts?page=2&limit=20`. Two approaches: **offset-based** pagination, and **cursor-based** pagination (better for large datasets).

**44. What is filtering?**
Restricting API responses based on conditions: `GET /orders?status=delivered&payment=completed`.

**45. What is sorting?**
Arranging response data in a specific order: `GET /products?sort=price&order=asc`.

**46. What is HATEOAS?**
Hypermedia As The Engine Of Application State — API responses include links to related actions.
```json
{ "orderId": 123, "status": "shipped",
  "links": { "track": "/orders/123/track", "cancel": "/orders/123/cancel" } }
```

**47. What is an API Gateway?**
A single entry point that manages requests to multiple backend services. Responsibilities: authentication, rate limiting, routing and logging.

**48. What is microservices architecture?**
An architecture where an application is split into small, independent services. An e-commerce example: User Service, Order Service, Payment Service, Inventory Service — each with its own API.

**49. API Gateway — real-time use case?**
Flow: Client -> API Gateway -> the appropriate microservice. Benefits: simplifies frontend logic, centralizes security, and makes monitoring easier.

**50. Difference between REST and SOAP?**

| Feature | REST | SOAP |
|---|---|---|
| Protocol | HTTP | XML-based |
| Format | JSON | XML |
| Speed | Fast | Slower |
| Complexity | Simple | Complex |
| Usage | Modern web apps | Legacy systems |

**51. What is SOAP?**
Simple Object Access Protocol — a messaging protocol using XML. Used in banking systems and enterprise legacy systems.

**52. What is WSDL?**
WSDL describes a SOAP service's structure, operations and endpoints. Analogy: **WSDL = the contract, API = the implementation.**

**53. What is GraphQL?**
A query language that allows clients to request **exactly the data they need**.
```graphql
{ user(id: 1) { name email } }
```

**54. REST vs GraphQL?**
REST's issue is over-fetching and under-fetching; GraphQL's solution is precise data fetching.

**55. What is API throttling?**
Temporary control over request rates when server load is high — for example throttling traffic during a peak Amazon sale to avoid a crash.

**56. What is load balancing?**
Distributing incoming requests across multiple servers — for example Netflix traffic spread across servers worldwide.

**57. What is API mocking?**
Simulating API responses without an actual backend, so the frontend team can work before the backend is ready.

**58. What is contract testing?**
Ensuring the API provider and consumer follow the same contract. If the frontend expects an `email` field, the backend must not remove it.

**59. What is API latency?**
The time from a request being sent to the response being received. High latency means poor user experience.

**60. How do you reduce API latency?**
Caching, database indexing, a CDN, and asynchronous processing.

## C61–C100: Advanced and real-time scenarios

**61. How do you secure an API?**
HTTPS (SSL/TLS encryption), authentication (JWT, OAuth, API keys), authorization (role-based access), input validation, rate limiting, firewall and WAF.
*Banking app:* HTTPS encrypts transactions, JWT validates users, rate limiting prevents brute force, and validation prevents SQL injection.

**62. Explain the real-time login API flow.**
1. The user enters their username/password
2. The client sends `POST /login`
3. The server validates the credentials
4. The server generates a JWT
5. The token is returned to the client
6. The client sends the token in future requests
7. The server verifies the token
This is how Amazon, Netflix and Gmail logins work.

**63. How do you handle API errors?**
Return meaningful responses when something fails: proper HTTP status codes, clear error messages, logged errors, and **never expose internal stack traces**.
```json
{ "error": "Invalid credentials", "code": 401 }
```

**64. What is centralized error handling?**
Handling all application errors in one place (middleware or a global handler). Benefits: cleaner code, consistent error responses, easier debugging. Examples: Express.js error middleware, Spring Boot's global exception handler (`@RestControllerAdvice`).

**65. How do you design a REST API?**
Use nouns not verbs; use the correct HTTP methods; version it; use proper status codes; keep naming consistent; support pagination and filtering; secure it.
Good: `GET /users`, `POST /users`, `GET /users/{id}`. Bad: `/getUsers`, `/createUser`.

**66. What is API schema validation?**
Ensuring incoming requests match the expected structure. It prevents invalid data, improves security and avoids crashes. Tools: Joi, Zod, JSON Schema, OpenAPI validation.

**67. What is the OpenAPI Specification?**
A standard format to define REST APIs. Uses: auto-generating documentation, generating client SDKs, and validating requests. Swagger UI is used by Stripe, GitHub and PayPal.

**68. What is middleware?**
Code executed between the request and the response. Uses: authentication, logging, validation, error handling and rate limiting.
Flow: `Request -> Middleware -> Controller -> Response`.

**69. Middleware — real-time example?**
Every request to `/api/orders`: 1. Verify the JWT, 2. Log the request, 3. Validate input, 4. Process the request.

**70. How do you upload files via an API?**
File uploads use `multipart/form-data` — for example uploading a profile picture to Facebook or Instagram.
```
Content-Type: multipart/form-data
```

**71. How do you handle large API responses?**
Pagination, streaming, compression (gzip), caching and lazy loading — for example downloading a full transaction history from a bank.

**72. What is API monitoring?**
Tracking API performance, uptime and failures. Metrics: response time, error rate, traffic volume, availability.

**73. Tools for API monitoring?**
New Relic, Datadog, Prometheus, Grafana, the ELK Stack.

**74. What is a webhook?**
A way for a server to send real-time data to another system automatically when an event occurs.
**API — the client requests data. Webhook — the server pushes data.**

**75. Webhook — real-time example?**
A payment gateway sends webhooks on payment success, payment failure and refund processed. Stripe sends a webhook and your server updates the order status.

**76. What is an event-driven API?**
API communication triggered by events rather than direct requests — order placed, user registered, payment completed. Used in microservices.

**77. What is a message queue?**
A queue that stores messages for asynchronous processing. It improves scalability, prevents blocking and handles traffic spikes.

**78. Message queue tools?**
RabbitMQ, Kafka, AWS SQS, Redis Queue — for example order processing in Amazon.

**79. Difference between sync and async APIs?**

| Synchronous | Asynchronous |
|---|---|
| The client waits | The client continues |
| Blocking | Non-blocking |
| Slower for heavy tasks | Better for scalability |

Sync: fetch a user profile. Async: send an email, generate a report.

**80. What is a retry mechanism?**
Retrying failed API requests automatically — for example a network failure while placing an order, where the system retries safely.

**81. What is a circuit breaker?**
It stops sending requests to a failing service to prevent system collapse. If the payment gateway fails, calls are temporarily stopped and a fallback is used.

**82. How do you prevent duplicate API requests?**
Idempotency keys, request hashing, unique transaction IDs — for example preventing a double payment when a user clicks "Pay" twice.

**83. What is API schema evolution?**
Managing changes to an API without breaking clients: versioning, backward compatibility and optional fields.

**84. How do you log API calls?**
Log the timestamp, endpoint, status code, response time, user ID and errors. Important for debugging, auditing and monitoring.

**85. What is API abuse?**
Misuse of an API, intentional or not: brute force attacks, scraping, DDoS, excessive requests. Prevention: rate limiting, captcha, authentication.

**86. How do you prevent SQL injection via an API?**
Input validation, prepared statements, an ORM, and escaping inputs.
Bad: `"SELECT * FROM users WHERE id=" + userInput`.

**87. What is an API timeout?**
The maximum time a client waits for a response — for example a payment API timing out after 30 seconds.

**88. How do you handle concurrent API requests?**
Async processing, thread pools, queues, locks and optimistic concurrency control — for example multiple users booking the same train seat.

**89. What is blue-green deployment?**
Deploying a new version without downtime. Blue is the old version, green is the new one; traffic switches after testing.

**90. What is a canary release?**
Gradually releasing a new API version to a small percentage of users, to detect bugs before full rollout.

**91. How do you test APIs automatically?**
Tools: Postman automation, Jest, Mocha, Newman, RestAssured. Types: unit tests, integration tests, load tests.

**92. What is a schema registry?**
A central repository for API schemas, used in microservices and event-driven systems to ensure a consistent data structure.

**93. How do you document APIs for the frontend team?**
Swagger/OpenAPI, examples, sample requests and responses, error scenarios and an authentication guide.

**94. How do you handle backward compatibility?**
Do not remove existing fields; add optional fields; use versioning; publish a deprecation policy.

**95. What is an API sandbox?**
A test environment where developers can experiment safely — PayPal Sandbox, Stripe Test Mode.

**96. What is a rate limit exceeded error?**
It occurs when a user exceeds the allowed request limit. HTTP code: **429 Too Many Requests**.

**97. How do you debug API issues in production?**
Logs, monitoring, distributed tracing, alerts and error tracking (Sentry).

**98. What is distributed tracing?**
Tracking a request across multiple services: Client -> API Gateway -> Auth Service -> Order Service -> Payment Service. Essential for microservices debugging.

**99. What is the API-first approach?**
Designing the API before building the frontend or backend. Benefits: better collaboration, clear contracts, parallel development, better scalability.

**100. Real-time interview question: "Design a Login API".**
1. Endpoint: `POST /login`
2. Input validation
3. Authenticate the user
4. Generate a JWT
5. Return the token
6. Secure storage
7. Error handling
8. Logging
9. Rate limiting

```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "expiresIn": 900,
  "user": { "id": 101, "name": "Mounika" }
}
```

---
---

# SECTION D — Backend Development Fundamentals (30 Questions)

**1. What is the difference between frontend and backend development?**
Frontend is everything the user sees and interacts with directly — buttons, forms, layout. Backend is the part that runs on the server, handling data, logic and security behind the scenes. The frontend talks to the backend through APIs.

**2. What is an API?**
A set of rules that allows two programs to communicate. A frontend app calls an API to request data from a backend, and the backend responds with the requested information.

**3. What is the difference between a GET and a POST request?**
GET retrieves data from the server without changing anything — like loading a webpage. POST sends new data to the server, such as submitting a form or creating a new record.

**4. What is a database and why is it needed?**
A database stores data permanently so it can be retrieved later, even after the server restarts. Without one, all information — user accounts, orders — would disappear immediately.

**5. What is the difference between authentication and authorization?**
Authentication checks **who you are**, usually through a username and password. Authorization checks **what you are allowed to do** once you are logged in, such as whether you can access admin features.

**6. What is a status code, and what does 404 mean?**
A number the server sends back to indicate the result of a request. 404 means "Not Found" — the requested resource does not exist. 200 means success and 500 means a server error occurred.

**7. What is caching and why does it improve performance?**
Caching stores frequently requested data temporarily so it can be returned quickly without recalculating or re-fetching it every time. This reduces load on the database and makes responses much faster.

**8. What is the difference between SQL and NoSQL databases?**
SQL databases (PostgreSQL, MySQL) store data in structured tables with fixed relationships. NoSQL databases (MongoDB) store data in flexible formats, useful when the structure of data changes often.

**9. What is middleware in a backend application?**
Code that runs between receiving a request and sending a response. It is commonly used for checking authentication, logging requests, or validating input before the main logic runs.

**10. What is the request-response cycle?**
The full process of a client sending a request to a server and receiving a response back. The client sends a request, the server processes it (often involving a database), and then sends a response with the result.

**11. What is the difference between synchronous and asynchronous programming?**
Synchronous code runs one task at a time, waiting for each to finish before starting the next. Asynchronous code can start a task and move on to other work while waiting — useful for slow operations like network calls.

**12. What is a token, and why is it used instead of a password for every request?**
A token is a piece of data generated after a successful login that proves a user is authenticated. Instead of sending a password with every request, the client sends the token, which is faster and safer.

**13. What does it mean for a backend system to be "scalable"?**
A scalable system continues to perform well as the number of users or amount of data grows. This is achieved through techniques like caching, load balancing and efficient database design.

**14. What is a server, in simple terms?**
A computer that is always running and listening for requests. When a client sends a request, the server processes it and sends back a response — like a waiter taking and delivering orders in a restaurant.

**15. What is REST, and why is it commonly used for APIs?**
REST is a set of conventions for designing APIs using standard HTTP methods like GET, POST, PUT and DELETE. It is widely used because it is simple, predictable and works well over the web.

**16. What is SQL injection, and why is it dangerous?**
An attack where a malicious user inserts harmful SQL code into an input field to manipulate or steal data from a database. It is dangerous because it can expose or destroy sensitive information. **Always use parameterized queries to prevent it.**

**17. What is the difference between PUT and PATCH requests?**
PUT replaces an entire resource with new data. PATCH updates only specific fields, leaving the rest unchanged. PATCH is more efficient when only small changes are needed.

**18. Why is error handling important in backend development?**
Good error handling prevents the application from crashing and gives clear, useful feedback when something goes wrong — such as returning a helpful message instead of a confusing technical error.

**19. What is the role of environment variables in a backend project?**
They store configuration values like database passwords or API keys **outside the actual code**. This keeps sensitive information secure and makes it easy to use different settings for development and production.

**20. What is the difference between a monolith and microservices?**
A monolith is a single application containing all features in one codebase. Microservices break the application into many small, independent services, each handling one specific feature, which can be deployed and scaled separately.

**21. What is load balancing, and why is it used?**
Load balancing distributes incoming requests across multiple servers so no single server becomes overwhelmed. It improves reliability and keeps the application fast even with many users.

**22. What is the most important skill for a backend developer to have?**
Clear logical thinking and the ability to break a big problem into small, manageable steps. Tools and languages can be learned over time, but methodical reasoning is the foundation.

**23. What is database indexing?**
An index is a special data structure that makes searching a database table much faster, similar to an index at the back of a book. Without one, the database must check every row to find a match.

**24. Why should passwords never be stored as plain text?**
If a database is ever compromised, plain text passwords are immediately exposed and reusable by attackers. Passwords are hashed using a one-way function so even if the data leaks, the originals cannot be recovered.

**25. What is rate limiting and why is it useful?**
Rate limiting restricts how many requests a user or system can make within a certain time period. It protects the backend from abuse, prevents overload, and reduces the risk of certain attacks.

**26. What is the difference between vertical and horizontal scaling?**
Vertical scaling means making a single server more powerful by adding memory or processing power. Horizontal scaling means adding more servers to share the load, working together as a group.

**27. What is JSON, and why is it commonly used in APIs?**
JSON (JavaScript Object Notation) is a lightweight format for structuring data using key-value pairs. It is widely used because it is easy for both humans to read and machines to parse.

**28. What happens if a backend server goes down?**
Users cannot access the application or receive an error response. Well-designed systems use multiple servers and load balancers so that if one fails, others continue handling traffic without the application going fully offline.

**29. What is the purpose of logging in a backend application?**
Logging records what happens inside an application over time — requests received, errors that occurred, actions taken. It is essential for debugging problems and understanding system behaviour in production.

**30. Why is it important to validate user input on the backend, not just the frontend?**
Frontend validation can be bypassed by a user calling the API directly. Backend validation is the final, trusted checkpoint that ensures no invalid or harmful data is processed or stored, regardless of how the request was made.

> **Closing thought:** backend development is built on a small set of core ideas — servers, APIs, databases, authentication and communication — repeated and combined in different ways. Master these fundamentals deeply, explain them simply, and you are well prepared.

---
---

# SECTION E — Multithreading & Concurrency Scenarios (70)

These are scenario-style questions. For each one, state the problem, name the tool, and explain the trade-off. Detailed code for the key patterns is in Part 17 of the notes.

## E1–E10: Basics, synchronization, async aggregation

**1. Thread lifecycle in action.** Explain all six states (New, Runnable, Running, Blocked, Waiting, Terminated) and what moves a thread between them.

**2. Runnable vs Thread in a web application.** Which do you choose and why? *Answer:* `Runnable`, because Java only allows single inheritance, so extending `Thread` uses up your one `extends`. It also separates the task from the thread that runs it, which is what executors and lambdas need. Future scope: switch to `Callable` for return values, use `ExecutorService` to manage threads at scale, and with virtual threads (Loom) `Runnable` becomes even more important for lightweight concurrency.

**3. Synchronization for a shared resource.** In an online ticket booking system, two users update the seat count at the same time and cause overbooking. *Answer:* a classic race condition — use a `synchronized` method so only one thread modifies the shared resource at a time. For counters, `AtomicInteger` is lighter. For read-heavy cases use `ReadWriteLock`. In distributed systems combine with database-level locking or optimistic concurrency.

**4. Aggregate multiple API calls asynchronously.** An e-commerce dashboard pulls product info, pricing and inventory from three services in parallel and renders only when all are ready. *Answer:* `CompletableFuture.supplyAsync` on a custom I/O executor, combined with `allOf` (or `thenCombine` for pairwise merges), plus `exceptionally`/`handle` and a timeout.

**5. Correctly updating a shared counter under contention.** A rate-limiter counter shows inconsistent and occasionally negative values. *Answer:* `AtomicInteger` for simple increments, `LongAdder` under very high contention, and `synchronized`/`ReentrantLock` when the update has rules (like a cap). Never do a naive read-then-write.

**6. Exclusive DB update without collisions.** Two threads update the same customer row. *Answer:* guard the critical section with a `ReentrantLock`, use `tryLock` with a timeout to avoid indefinite blocking, and always unlock in `finally`. Keep the lock private, and establish a global lock ordering if multiple rows are touched.

**7. Producer makes parts, assembler must wait.** *Answer:* the intrinsic monitor with `wait`/`notifyAll`. Always check in a **while** loop to handle spurious wakeups, and use `notifyAll` when there may be multiple waiters. In production prefer a `BlockingQueue` or `ReentrantLock` + `Condition`.

**8. Gracefully shutting down an ExecutorService.** *Answer:* `shutdown()` -> `awaitTermination()` -> if needed `shutdownNow()` -> await again. Restore the interrupt status when catching `InterruptedException`, and log the dropped queue for visibility.

**9. Dependent asynchronous tasks.** Task B (dispatch) must only run if Task A (payment) succeeds. *Answer:* `thenCompose`. `thenCombine` is for two *independent* tasks whose results you merge. This avoids nested blocking `Future.get()` calls.

**10. Retrying flaky API calls with timeout.** Retry up to three times with a 2-second timeout per attempt. *Answer:* wrap the call in a `CompletableFuture` and use `get(timeout)`; catch `TimeoutException`/`ExecutionException` and retry, breaking on success. Restore interrupts and shut down the executor.

## E11–E30

**11. Phase-by-phase coordination across threads** — `CyclicBarrier`
**12. Enforce per-task time limits with clean cancellation** — `Future.cancel()` with a timeout
**13. Chain dependent async steps without blocking** — `CompletableFuture` chaining
**14. Limit concurrent access with permits** — `Semaphore`
**15. Heavy computations in parallel with limited threads** — a fixed thread pool sized to the cores
**16. Many readers, few writers** — `ReadWriteLock`
**17. Graceful cancellation of long-running tasks** — cooperative interruption
**18. Orchestrating interdependent tasks (DAG style)** — a `CompletableFuture` graph
**19. Strict task order A -> B -> C without thread juggling** — chained futures
**20. Keep the pipeline running when some tasks fail** — `exceptionally` / `handle` per stage
**21. Fire many independent tasks and resume only when all finish** — `allOf` / `invokeAll`
**22. Prevent starvation when many threads compete** — a **fair** `ReentrantLock(true)`; fairness trades throughput for predictability. Also reduce lock hold time and remove unbounded retries. Do not rely on thread priorities — Java scheduling is not guaranteed across operating systems
**23. Threads keep dodging each other and never make progress** — this is **livelock**: threads are active and responsive but make zero forward progress. Fix with randomness or **backoff with jitter**, or a protocol where one side eventually wins
**24. Enforce a hard deadline for work** — timeouts
**25. Handling InterruptedException the right way** — restore the interrupt status, never swallow it
**26. Multi-phase work where everyone must rendezvous** — `CyclicBarrier`
**27. Many CPU-heavy tasks without melting the machine** — a bounded pool sized to available processors
**28. Server handling many requests without one-thread-per-request** — a thread pool (or virtual threads)
**29. Separate pipelines for high and low priority, served in order** — priority queues
**30. Two-way money transfers sometimes freeze the system** — **deadlock** from inconsistent lock ordering; fix with a global lock order

## E31–E50

**31. Mixed-duration jobs with limited workers** — pool tuning and task segregation
**32. Cap concurrent client connections** — `Semaphore`
**33. Start many tasks, handle results the moment they are ready** — `ExecutorCompletionService`
**34. Producer hands off data; consumer waits until it is ready** — `BlockingQueue`
**35. Threads grab different locks and end up waiting forever** — deadlock analysis, consistent ordering
**36. Many quick tasks — do not spawn a thread per task** — thread pooling
**37. Do not start the app until all subsystems are ready** — `CountDownLatch`
**38. Multi-phase workers that must rendezvous at each step** — `CyclicBarrier`
**39. Speed up independent element processing over a big list** — parallel streams
**40. Ensure the JVM waits for critical work before exit** — `join()` and non-daemon threads
**41. The class already extends a base type but must run concurrently** — implement `Runnable`
**42. Prevent an inconsistent balance** — synchronization on the shared account
**43. Consumer sometimes waits forever despite data being present** — a missed notify; wait in a `while` loop and use `notifyAll`
**44. Avoid deadlock in a two-account transfer** — consistent lock ordering (e.g. by account id)
**45. Prevent starvation under heavy contention** — a fair lock
**46. Run recurring tasks reliably** — `ScheduledExecutorService`
**47. Fan out to multiple services and aggregate safely** — `CompletableFuture.allOf`
**48. Producer-consumer with backpressure and multiple consumers** — a **bounded** `BlockingQueue`
**49. Dynamic team size across phases (CyclicBarrier will not fit)** — `Phaser`
**50. Time-box and cancel an async pipeline** — `CompletableFuture` with a timeout

## E51–E70

**51. Parallel streams corrupt output due to shared mutable state** — use collectors and reductions, never a shared accumulator
**52. Threads must finish initialization before main continues** — `CountDownLatch` or `join`
**53. Need both parallel and sequential phases in a pipeline** — ForkJoin with a custom executor
**54. Cancel long-running tasks if they exceed a deadline** — `Future.cancel` with a timeout
**55. Parallel stream runs slower than sequential on small data** — coordination overhead dominates; use sequential
**56. Multiple readers, single writer with high read frequency** — `ReadWriteLock` (or `StampedLock` for optimistic reads)
**57. Coordinating different tasks that must run in order** — chained futures
**58. Detect and recover from livelock** — backoff with jitter, tie-breakers, and monitoring
**59. Cancel tasks cleanly in an ExecutorService** — graceful shutdown sequence
**60. Parallel aggregation of large datasets** — `ForkJoinPool`
**61. Throttling API calls with limited concurrency** — `Semaphore` as a rate limiter
**62. Coordinating variable participants across phases** — `Phaser`
**63. Task dependencies with CompletableFuture** — `thenCompose` chains
**64. Handling starvation in a lock-heavy system** — lock tuning and fairness
**65. Run thousands of tasks efficiently** — `ThreadPoolExecutor` tuning (core size, max size, queue, rejection policy)
**66. Divide-and-conquer over a big array** — the ForkJoin framework
**67. Process results as soon as they finish** — `ExecutorCompletionService`
**68. Robust async pipeline with fallbacks** — `CompletableFuture` with `exceptionally` fallbacks
**69. Double-buffer handoff between two threads** — `Exchanger`; the swap is atomic, with no copying and minimal GC
**70. Graceful shutdown of a multi-consumer pipeline** — a **poison pill** per consumer on a bounded `BlockingQueue`; no fragile shared flags or timing assumptions

---
---

# SECTION F — System Design

## F1 — The seven-step answer template

Use this structure for **every** system design question.

1. **Clarify requirements** — functional (core features, users, interaction channels, data types, integrations) and non-functional (read-heavy or write-heavy, availability, latency, consistency, rate limiting)
2. **Capacity estimation** — daily/monthly users, peak concurrency, read/write RPS, storage, cache memory, bandwidth
3. **High-level design** — clients, application servers, load balancers, services, databases, storage, caching, message queues, external services
4. **Database design** — data modelling, entities and relationships, choosing the right storage, schema and access patterns
5. **API design** — which endpoints to expose, which style (REST, GraphQL, RPC), which protocols (HTTPS, WebSockets, gRPC, AMQP/MQTT)
6. **Dive deep into key components** — whatever the interviewer focuses on (short-URL generation, real-time message delivery, sharding, replication, cache invalidation)
7. **Address key concerns** — scalability and performance (scale up/out, caching, indexing, denormalization, sharding, async), and reliability (identify single points of failure, redundancy, geographic redundancy, replication, circuit breakers, retries with exponential backoff, monitoring and alerting)

## F2 — The ten most common questions

**1. Design a URL Shortener (TinyURL).**
*Functional:* generate a unique short URL; redirect to the original; optional custom short URLs; link expiration; optional usage analytics.
*Non-functional:* 99.9% availability; millisecond latency for shortening and redirects; millions of requests per day; durability for years; security against phishing.

**2. Design a Chat Application (WhatsApp).**
*Functional:* one-on-one and group conversations; online/offline status; delivery statuses (sent, delivered, read); multimedia messages; push notifications.
*Non-functional:* real-time delivery with minimal latency; millions of concurrent users; high availability (may be compromised in favour of consistency); durability — messages must not be lost.

**3. Design a Social Media Platform (Instagram).**
*Functional:* upload and share images and videos; like, comment and share; follow and unfollow; generate a news feed; tagging in posts and comments.
*Non-functional:* 99.9% availability; low latency for feed generation; millions of concurrent users; high durability for uploads; eventual consistency is acceptable.

**4. Design a Video Streaming Service (YouTube).**
*Functional:* upload videos with titles, descriptions, tags and thumbnails; on-demand streaming; search for videos, channels and playlists; like, dislike, comment and share; record view counts.
*Non-functional:* 99.99% uptime; real-time, lag-free streaming; horizontal scalability; high durability.

**5. Design an E-commerce Platform (Amazon).**
*Functional:* sellers list products with details; cart and wishlist; search by product, category and brand; place orders for one or many products; rate and review purchased products.
*Non-functional:* millions of users, products and transactions simultaneously; 99.9% availability; low latency for page loads, search and checkout; high durability for user data, listings and orders.

**6. Design a Ride-Sharing Service (Uber).**
*Functional:* see nearby available drivers; book a ride with pickup and drop-off; real-time matching; real-time cost and ETA estimation from distance, traffic and demand; real-time tracking for rider and driver.
*Non-functional:* millions of users and rides; low latency for matching, GPS tracking and requests; 99.9% uptime; a consistent view of the system for riders and drivers.

**7. Design a File Storage Service (Google Drive).**
*Functional:* upload files of various types and sizes; download on demand; share files and folders via links or email invitations; search by name, type, content or metadata; synchronize across devices.
*Non-functional:* millions of users and billions of files; low-latency uploads, downloads and search; high availability; consistency across devices during sync; durability.

**8. Design a Web Crawler.**
*Functional:* fetch URLs efficiently; handle different content types (text, images, multimedia); prioritise URLs by criteria such as importance and freshness; store crawled data efficiently.
*Non-functional:* scale to millions or billions of pages; minimal fetch and processing latency; maximise pages crawled per unit of time.

**9. Design a Notification System.**
*Functional:* support email, SMS, push (mobile/web) and in-app channels; support transactional, promotional and informational types; schedule notifications; send in bulk for campaigns; automatically retry failed deliveries.
*Non-functional:* millions of notifications per minute at peak; 99.99% uptime; low latency for real-time and high-priority notifications; reliable delivery across all channels.

**10. Design a Logging and Monitoring System.**
*Functional:* collect logs from applications, servers, databases and microservices; support multiple formats (JSON, plaintext, XML); archive old logs to cold storage; powerful querying by time range, log level, source and other attributes; alerts on patterns, thresholds or anomalies.
*Non-functional:* horizontal scalability for growing log volume; low-latency ingestion and processing for real-time monitoring; 99.99% uptime; durability with replication across nodes or data centres.

## F3 — Forty system design interview tips

1. Understand the functional and non-functional requirements before designing
2. Clearly define the use cases and constraints of the system
3. There is no perfect solution — it is all about trade-offs
4. Assume everything can and will fail; make it fault tolerant
5. Keep it simple; avoid over-engineering
6. Design for scalability from the ground up
7. Prefer horizontal scaling over vertical scaling
8. Use load balancers to ensure high availability and distribute traffic
9. Consider SQL databases for structured data and ACID transactions
10. Opt for NoSQL databases when dealing with unstructured data
11. Consider a graph database for highly connected data
12. Use database sharding to scale SQL databases horizontally
13. Use database indexing to optimise read queries
14. Assume everything can and will fail; make it fault tolerant
15. Use rate limiting to prevent overload and DoS attacks
16. Consider WebSockets for real-time communication
17. Use heartbeat mechanisms to detect failures
18. Consider a message queue for asynchronous communication
19. Implement data partitioning and sharding for large datasets
20. Consider denormalizing databases for read-heavy workloads
21. Use bloom filters to check for an item in a large dataset quickly
22. Use CDNs to reduce latency for a global user base
23. Use caching to reduce database load and improve response times
24. Use a write-through cache for write-heavy applications
25. Use a read-through cache for read-heavy applications
26. Use object storage like S3 for large datasets and media files
27. Implement data replication and redundancy to avoid single points of failure
28. Implement autoscaling to handle traffic spikes smoothly
29. Use asynchronous processing for background tasks
30. Use batch processing for non-urgent tasks to optimise resources
31. Make operations idempotent to simplify retry logic and error handling
32. Consider a data lake or data warehouse for analytics and reporting
33. Implement comprehensive logging and monitoring
34. Implement circuit breakers to prevent one failing service bringing down the system
35. Implement chaos engineering practices to test resilience
36. Design for statelessness where possible
37. Use failover mechanisms to switch to a redundant system automatically
38. Distribute your system across different data centres to prevent localized failures
39. Use Time-To-Live (TTL) values to expire cached data and reduce staleness
40. Pre-populate critical data in the cache to avoid cold starts

## F4 — Fundamentals you must be able to define in one sentence

Scalability, availability (uptime / (uptime + downtime)), latency vs throughput, the CAP theorem, load balancers and their algorithms, database types, CDN, message queues, rate limiting and its algorithms, database indexes, caching strategies and eviction policies, consistent hashing, database sharding, consensus algorithms (Paxos, Raft), proxy servers (forward vs reverse), heartbeats, checksums, service discovery, bloom filters, and the gossip protocol.

## F5 — The trade-offs you will be asked to compare

Vertical vs horizontal scaling; strong vs eventual consistency; stateful vs stateless design; read-through vs write-through cache; SQL vs NoSQL; REST vs RPC; synchronous vs asynchronous; batch vs stream processing; long polling vs WebSockets; normalization vs denormalization; TCP vs UDP.

All of these are explained in Part 27 of **JAVA-COMPLETE-NOTES.md**.

---

*End of the question bank. Concepts and code are in **JAVA-COMPLETE-NOTES.md**.*
