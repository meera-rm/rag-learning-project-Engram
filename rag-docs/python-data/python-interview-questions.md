---
title: PYTHON-INTERVIEW-QUESTIONS
topic: python-data
source_type: interview-questions
source_file: STUDYNOTEs/PYTHON-INTERVIEW-QUESTIONS.md
---

# Python Interview Questions & Answers — Complete Compilation


This is the companion to `PYTHON-LEARNING-NOTES.md`. Learn the concepts there first; use this to test yourself and prepare for interviews.


### How to use this
Go through it once, marking the questions you could not answer yourself. On the second pass, review only those. After 2–3 passes you will be well prepared for a technical interview on Python.

---

## TABLE OF CONTENTS

- [Set A — 50 Questions (Illustrated Slides)](#set-a)
  - Slide 1: Python Basics (Q1–5)
  - Slide 2: Data Types (Q6–10)
  - Slide 3: Operators (Q11–15)
  - Slide 4: Control Flow (Q16–20)
  - Slide 5: Functions (Q21–25)
  - Slide 6: Object Oriented Programming (Q26–30)
  - Slide 7: Advanced Python (Q31–35)
  - Slide 8: Exception Handling (Q36–40)
  - Slide 9: Modules & Packages (Q41–45)
  - Slide 10: Built-in Functions & Best Practices (Q46–50)
- [Set B — 50 Questions (Fresher to Senior)](#set-b)
- [Set C — 200 Questions (Advanced & Core Concepts)](#set-c)
- [Set D — OOP Interview Preparation](#set-d)
- [Rapid-Fire Revision Sheet](#rapid-fire)

---

<a name="set-a"></a>
# SET A — 50 PYTHON INTERVIEW QUESTIONS & ANSWERS



## Slide 1: Python Basics

**Q1. What is Python?**
Python is a high-level, interpreted, object-oriented programming language known for its
simple and readable syntax.

**Q2. What are Python's key features?**
- Easy to learn and use
- Interpreted language
- Dynamically typed
- Object-oriented
- Large standard library
- Cross-platform support

*Why Python?* Beginner friendly · Versatile · Huge community support · Used in Web, AI,
Data Science, Automation, and more.

**Q3. What is the difference between interpreted and compiled languages?**
Interpreted languages execute code **line by line**, while compiled languages convert the
entire program into **machine code** before execution.

| Interpreted | Compiled |
|---|---|
| Executes line by line | Compiles entire program first |
| No separate compilation step | Faster execution |
| Examples: Python, JavaScript | Examples: C, C++, Java |

**Q4. What is PEP 8?**
PEP 8 is Python's **style guide** that provides conventions for writing clean, readable and
consistent code.

*PEP 8 helps in:* improving code readability · maintaining consistency · collaborating
better in teams.

**Q5. What are variables in Python?**
Variables are names used to store data values in memory.

```python
x = 10                  # x is integer
name = "Python"         # name is string
is_fun = True           # is_fun is boolean
print(x, name, is_fun)
```

## Slide 2: Data Types

**Q6. What are Python's built-in data types?**
`int`, `float`, `complex`, `str`, `list`, `tuple`, `set`, `dict`, `bool`, `NoneType`

**Q7. What is the difference between a list and a tuple?**
List is **mutable** (can be changed). Tuple is **immutable** (cannot be changed after
creation).

| List | Tuple |
|---|---|
| Uses `[ ]` | Uses `( )` |
| Mutable | Immutable |
| Slower | Faster |
| More methods | Fewer methods |
| `lst = [1, 2, 3]`; `lst[0] = 10` ✓ | `tup = (1, 2, 3)`; `tup[0] = 10` ✗ |

**Q8. What is a dictionary?**
A dictionary stores data in **key-value pairs**.

```python
student = {"name": "John", "age": 22}
print(student["name"])     # John
student["age"] = 23
print(student)             # {'name': 'John', 'age': 23}
```

**Q9. What is a set?**
A set is an **unordered collection of unique elements**.

```python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)         # {1, 2, 3, 4}
numbers.add(5)
numbers.remove(2)
print(numbers)         # {1, 3, 4, 5}
```

**Q10. What is type casting?**
Type casting is the process of **converting one data type into another**.

```python
x = "10"                    # string
y = int(x)                  # type casting to int
z = float(y)                # type casting to float
print(x, type(x))           # 10 <class 'str'>
print(y, type(y))           # 10 <class 'int'>
print(z, type(z))           # 10.0 <class 'float'>
```

Common conversions: `int()` → to integer · `float()` → to float · `str()` → to string ·
`list()` → to list · `tuple()` → to tuple · `set()` → to set

## Slide 3: Operators

**Q11. What are arithmetic operators?**
Used to perform mathematical operations.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | 8 |
| `-` | Subtraction | `5 - 3` | 2 |
| `*` | Multiplication | `5 * 3` | 15 |
| `/` | Division | `5 / 2` | 2.5 |
| `%` | Modulus | `5 % 2` | 1 |
| `**` | Exponent | `2 ** 3` | 8 |
| `//` | Floor Division | `5 // 2` | 2 |

**Q12. What is the difference between `=` and `==`?**
`=` is an **assignment** operator. `==` is a **comparison** operator.

```python
x = 10                # assignment (stores value)
y = 10                # assignment
print(x == y)         # True (comparison)
print(x = y)          # ✗ Syntax Error
```

**Q13. What are logical operators?**
They are used to combine conditional statements.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True if both are True | `True and False` | False |
| `or` | True if any one is True | `True or False` | True |
| `not` | Reverses the result | `not True` | False |

**Q14. What is the modulus operator?**
The `%` operator returns the **remainder after division**.

```python
print(10 % 3)     # 1
print(25 % 4)     # 1
print(-10 % 3)    # 2  (remainder is always non-negative)
```

**Q15. What is operator precedence?**
Operator precedence determines the order in which operations are evaluated. Higher
precedence operators are evaluated first.

**Precedence order (High → Low):**
1. `( )` Parentheses
2. `**` Exponent
3. `+x`, `-x`, `~x` Unary plus, minus, bitwise NOT
4. `*`, `/`, `//`, `%` Multiplication, Division, Floor Division, Modulus
5. `+`, `-` Addition, Subtraction
6. `<`, `<=`, `>`, `>=`, `!=`, `==` Comparison
7. `not` Logical NOT
8. `and` Logical AND
9. `or` Logical OR
10. `=`, `+=`, `-=`, `*=`, `/=` Assignment operators

**Sample expression**
```
x = 2 + 3 * 4 ** 2
  = 2 + 3 * 16     (Step 1: 4 ** 2 = 16)
  = 2 + 48         (Step 2: 3 * 16 = 48)
  = 50             (Step 3: 2 + 48 = 50)
```

## Slide 4: Control Flow

**Q16. What is an if statement?**
An if statement executes a block of code only when the condition is True.

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible.")
```

**Q17. What is the difference between for loop and while loop?**
`for` loop is used to iterate over a **sequence** (list, tuple, string, etc.).
`while` loop is used to repeat a block of code as long as a **condition** is True.

| for Loop | while Loop |
|---|---|
| Used with a sequence | Used with a condition |
| Number of iterations is known | Number of iterations is unknown |
| Example: iterate over list, string, range | Example: user input, condition-based tasks |

**Q18. What does break do?**
The `break` statement is used to **exit the loop immediately**.

```python
for i in range(1, 6):
    if i == 3:
        break          # loop terminates here
    print(i)
# Output: 1 2
```

**Q19. What does continue do?**
The `continue` statement **skips the current iteration** and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue       # skip the rest and go next
    print(i)
# Output: 1 2 4 5
```

**Q20. What is a nested loop?**
A loop inside another loop is called a nested loop. It is useful for working with
multi-dimensional data.

```python
for i in range(1, 4):          # Outer loop
    for j in range(1, 4):      # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=1, j=1 / i=1, j=2 / i=1, j=3
# i=2, j=1 / i=2, j=2 / i=2, j=3
# i=3, j=1 / i=3, j=2 / i=3, j=3
```

**Quick tips:** Use `if` to make decisions · Use `for` when you know how many times to loop
· Use `while` when the number of iterations is unknown · Use `break` to exit early · Use
`continue` to skip and move ahead · Nested loops are powerful — use them wisely.

## Slide 5: Functions

**Q21. What is a function?**
A function is a **reusable block of code** that performs a specific task.

```python
def greet():
    print("Hello, Python!")

greet()      # Function call
```

**Q22. What is the difference between parameters and arguments?**
**Parameters** are variables in the function **definition**. **Arguments** are the values
**passed** to the function when it is called.

```python
def add(a, b):          # a, b are parameters
    return a + b

result = add(5, 7)      # 5, 7 are arguments
print(result)           # Output: 12
```

**Q23. What is a return statement?**
A `return` statement sends a value back from the function to the caller.

```python
def square(x):
    return x * x

y = square(4)
print(y)     # Output: 16
```

**Q24. What are default arguments?**
Arguments with **predefined values** that are used if no value is passed.

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())              # Hello, Guest!
print(greet("Alice"))       # Hello, Alice!
```

**Q25. What is a lambda function?**
A lambda function is a small **anonymous** function defined using the `lambda` keyword.
Used for short, one-time functions.

```python
# Example 1
square = lambda x: x * x
print(square(5))     # Output: 25

# Example 2
add = lambda a, b: a + b
print(add(3, 7))     # Output: 10
```

*Why functions?* Makes code modular · Improves reusability · Easy to debug and maintain ·
Enhances readability.

## Slide 6: Object Oriented Programming

**Q26. What is OOP?**
Object Oriented Programming (OOP) is a programming paradigm that organizes code using
**objects and classes**.

*Key principles of OOP:* Encapsulation · Inheritance · Polymorphism · Abstraction

**Q27. What is a class?**
A class is a **blueprint or template** for creating objects.

```python
class Car:                                   # Class definition
    def __init__(self, brand, model):
        self.brand = brand                   # attribute
        self.model = model                   # attribute

    def info(self):
        return f"{self.brand} {self.model}"
```

**Q28. What is an object?**
An object is an **instance** of a class.

```python
c1 = Car("Toyota", "Innova")     # object 1
c2 = Car("Honda", "City")        # object 2

print(c1.info())                 # Toyota Innova
print(c2.info())                 # Honda City
```

**Q29. What is inheritance?**
Inheritance allows a new class (**child**) to inherit attributes and methods from an
existing class (**parent**).

```python
class Animal:                    # Parent class
    def speak(self):
        return "Some sound"

class Dog(Animal):               # Child class
    def speak(self):             # Method Overriding
        return "Bark"

d = Dog()
print(d.speak())     # Bark
```

**Q30. What is polymorphism?**
Polymorphism allows different classes to respond to the **same method call in different
ways**.

```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

for animal in [Cat(), Dog()]:
    print(animal.sound())    # Meow Bark
```

*Why OOP?* Makes code modular and easy to maintain · Reusability of code through
inheritance · Improves scalability for large projects · Enhances readability and
organization · Reduces complexity.

## Slide 7: Advanced Python

**Q31. What is a decorator?**
A decorator is a function that takes another function and **extends or modifies its
behavior without changing it**.

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before function call
# Hello!
# After function call
```

**Q32. What is a generator?**
A generator is a function that returns an iterator using the **`yield`** keyword.

```python
def count():
    yield 1
    yield 2
    yield 3

for num in count():
    print(num)

# Output: 1 2 3
```

**Q33. What is list comprehension?**
A **concise way to create lists in a single line** of code.

```python
squares = [x * x for x in range(6)]
print(squares)     # [0, 1, 4, 9, 16, 25]
```

**Q34. What is the difference between copy and deepcopy?**
`copy` creates a **shallow** copy, while `deepcopy` creates a **completely independent**
copy.

| copy (shallow) | deepcopy (deep) |
|---|---|
| Copies the outer object only | Copies the outer object and all nested objects |
| Nested objects are referenced | Fully independent copy |
| Changes in nested objects affect both | Changes in one do not affect the other |

**Q35. What is `*args` and `**kwargs`?**
`*args` allows a function to accept any number of **positional** arguments.
`**kwargs` allows a function to accept any number of **keyword** arguments.

```python
def demo(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

demo(1, 2, 3, name="John", age=25, city="Pune")

# Output:
# Positional args: (1, 2, 3)
# Keyword args: {'name': 'John', 'age': 25, 'city': 'Pune'}
```

*Why these concepts matter:* Decorators → for logging, authentication, timing.
Generators → for memory-efficient iteration. List comprehension → for cleaner and faster
code. Copy vs Deepcopy → to avoid unexpected side effects. `*args` & `**kwargs` → for
flexible and reusable functions.

## Slide 8: Exception Handling

**Q36. What is an exception?**
An exception is an **error that occurs during the execution of a program** and disrupts
the normal flow.

**Common built-in exceptions:**
| Exception | Meaning |
|---|---|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `FileNotFoundError` | File not found |
| `IndexError` | Index out of range |
| `KeyError` | Key not found in dict |

**Q37. What is a try-except block?**
The try-except block is used to **catch and handle exceptions** so that the program doesn't
crash.

```python
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Program continues...")

# Output:
# Cannot divide by zero!
# Program continues...
```

**Q38. What is the purpose of the finally block?**
The `finally` block contains code that executes **no matter what** — whether an exception
occurred or not.

```python
try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will always execute.")

# Output:
# File not found!
# This will always execute.
```

**Q39. What is the use of the raise keyword?**
The `raise` keyword is used to **manually throw an exception**.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    else:
        print("Access granted")

check_age(16)      # Raises ValueError
```

**Q40. What is the difference between Syntax Errors and Exceptions?**

| Syntax Errors | Exceptions |
|---|---|
| Occur when the code violates Python grammar rules | Occur during the execution of a valid program |
| Detected by the interpreter **before** execution | Caused by **runtime** conditions |
| Prevent the program from running | Can be handled using try-except |
| Example: missing colon, unmatched parentheses, indentation error | Example: division by zero, file not found, invalid input |
| `if True` ← missing colon | `x = 10 / 0` ← runtime exception |

*Quick tips:* Use try-except to handle errors gracefully · Always add `finally` to clean up
resources · **Never ignore exceptions — handle them!**

## Slide 9: Modules & Packages

**Q41. What is a module?**
A module is a file containing Python definitions and statements. It can include functions,
classes and variables.

```python
# mymodule.py
def add(a, b):
    return a + b

PI = 3.14159
```

We can import and use this module in another program.

**Q42. How do you import a module?**
We use the `import` keyword to import a module.

```python
import mymodule
result = mymodule.add(5, 7)
print(result)      # Output: 12
```

You can also import specific items from a module using the `from...import` statement.

**Q43. What is a package?**
A package is a **collection of modules in a directory**, with a special `__init__.py` file.

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpkg/
    ├── __init__.py
    └── module3.py
```

The `__init__.py` file tells Python that the directory is a package.

**Q44. How do you import from a package?**
We can import modules or specific items from a package.

```python
# Import entire module
from mypackage import module1
module1.some_function()

# Import specific item
from mypackage.module2 import some_variable
print(some_variable)

# Import with alias
import mypackage.module1 as m1
m1.some_function()
```

**Q45. What is the difference between module and package?**

| Module | Package |
|---|---|
| Single Python file (`.py`) | Collection of modules in a directory |
| Contains functions, classes, variables | Contains multiple modules and an `__init__.py` file |
| Imported using `import module_name` | Imported using `import package_name` or `from package import module` |
| Example: `math.py` | Example: `mypackage/` |

*Quick tips:* Use modules to organize code · Use packages for larger projects · Always use
meaningful names · Keep code reusable and maintainable · Follow PEP 8 naming conventions.

## Slide 10: Built-in Functions & Best Practices

**Q46. What are some commonly used built-in functions in Python?**

| Function | Description |
|---|---|
| `len()` | Returns length of an object |
| `type()` | Returns type of an object |
| `range()` | Returns a sequence of numbers |
| `max()` | Returns largest item |
| `min()` | Returns smallest item |
| `sum()` | Returns sum of items |
| `sorted()` | Returns sorted list |
| `enumerate()` | Returns index and value |

**Q47. Explain enumerate() with example.**
`enumerate()` adds a counter to an iterable and returns it as an (index, value) pair.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
```

**Q48. What is the difference between `list()` and `tuple()`?**

| `list()` | `tuple()` |
|---|---|
| Mutable (can be changed) | Immutable (cannot be changed) |
| Uses square brackets `[ ]` | Uses parentheses `( )` |
| Slower than tuples | Faster than lists |
| `a = [1, 2, 3]` | `b = (1, 2, 3)` |

**Q49. How do you use map(), filter(), reduce()?**
These are higher-order functions; `reduce` comes from the `functools` module.

```python
# map() - Applies a function to all items
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
print(squares)     # Output: [1, 4, 9]

# filter() - Filters items based on condition
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)       # Output: [2, 4]

# reduce() - Applies function cumulatively
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)     # Output: 24
```
*Note: Don't forget to import `reduce` from `functools`.*

**Q50. What are some Python best practices?**
Following best practices makes your code clean, efficient and professional.
- Follow **PEP 8** style guide
- Use **meaningful** variable and function names
- Write **modular** and **reusable** code
- Add comments and docstrings
- Handle exceptions properly
- Avoid global variables
- Keep functions small and focused
- Test your code regularly
- Use list comprehensions & built-in functions when possible

*Key takeaways:* Functions help in organizing and reusing code · OOP makes code scalable
and easier to maintain · Modules & Packages keep large projects well-structured · Built-in
functions & best practices improve code quality.

---

<a name="set-b"></a>
# SET B — 50 PYTHON INTERVIEW QUESTIONS (FRESHER TO SENIOR)

*Compiled after attending dozens of technical interviews at companies like Google,
Facebook, Netflix and Amazon. Difficulty ranges from fresher level to senior software
programmer.*

**B1. How will you improve the performance of a program in Python?**
1. **Data Structure:** select the right data structure for your purpose.
2. **Standard Library:** wherever possible use methods from the standard library — they
   have much better performance than user implementations.
3. **Abstraction:** too much abstraction and indirection can cause slow performance. Remove
   redundant abstraction.
4. **Algorithm:** the right algorithm makes a big difference. Find and select the suitable
   algorithm to solve your problem with high performance.

**B2. What are the benefits of using Python?**
Python is strong enough that even Google uses it.
1. **Efficient:** very efficient in memory management. For a large data set like Big Data,
   it is much easier to program in Python.
2. **Faster:** though Python code is interpreted, it still has very fast performance.
3. **Wide usage:** widely used among different organizations for different projects; due to
   this wide usage there are thousands of add-ons available.
4. **Easy to learn:** the biggest benefit. Complex tasks can be very easily implemented.

**B3. How will you specify source code encoding in a Python source file?**
By default, every source code file in Python is in **UTF-8** encoding. You can specify your
own encoding by adding this line after the `#!` line:
```python
# -*- coding: encoding -*-
```
Replace `encoding` with the encoding you want to use.

**B4. What is the use of PEP 8 in Python?**
PEP 8 is a **style guide** for Python code. It provides the coding conventions: indentation,
formatting, tabs, maximum line length, imports organization, line spacing, etc. We use
PEP 8 to bring consistency to our code — with consistency it is easier for other developers
to read the code.

**B5. What is Pickling in Python?**
Pickling is a process by which a Python object hierarchy can be converted into a **byte
stream**. The reverse operation is **Unpickling**. Python has a module named `pickle` which
implements a powerful algorithm for serialization and de-serialization of Python object
structures. Some people also call it Serialization or Marshalling. With serialization we
can transfer Python objects over the network. It is also used to persist the state of a
Python object — writing it to a file or a database.

**B6. How does memory management work in Python?**
There is a **private heap space** in Python that contains all the Python objects and data
structures. In CPython there is a **memory manager** responsible for managing the heap
space. There are different components in the Python memory manager that handle
segmentation, sharing, caching, memory pre-allocation, etc. The Python memory manager also
takes care of **garbage collection** by using a **reference counting** algorithm.

**B7. How will you perform Static Analysis on a Python Script?**
Use the static analysis tool **PyChecker**. PyChecker can detect errors in Python code and
also gives warnings for any style issues. Other tools to find bugs in Python code are
**pylint** and **pyflakes**.

**B8. What is the difference between a Tuple and List in Python?**
Both are built-in data structures.
1. **Syntax:** a Tuple is enclosed in parentheses — `myTuple = (10, 20, "apple")`. A List
   is enclosed in brackets — `myList = [10, 20, 30]`.
2. **Mutable:** Tuple is an immutable data structure; a List is mutable.
3. **Size:** a Tuple takes much less space than a List.
4. **Performance:** Tuple is faster than a List, so it gives good performance.
5. **Use case:** since Tuple is immutable, we can use it in cases like Dictionary creation.
   A List is preferred where data can alter.

**B9. What is a Python Decorator?**
A Python Decorator is a mechanism to **wrap a Python function and modify its behavior** by
adding more functionality to it. We use the `@` symbol to call a Python Decorator function.

**B10. How are arguments passed in a Python method? By value or by reference?**
Every argument in a Python method is an **Object**. All the variables in Python have a
reference to an Object. Therefore arguments in a Python method are **passed by Reference**.
Since some of the objects passed as reference are mutable, we can change those objects in a
method. But for an immutable object like a String, any change done within a method is not
reflected outside.

**B11. What is the difference between List and Dictionary data types in Python?**
1. **Syntax:** in a List we store objects in a sequence; in a Dictionary we store objects
   in key-value pairs.
2. **Reference:** in a List we access objects by index number, starting from 0; in a
   Dictionary we access objects by the key specified at the time of creation.
3. **Ordering:** in a List objects are stored in an ordered sequence; in a Dictionary
   objects are not stored in an ordered sequence *(historically — dicts preserve insertion
   order from Python 3.7)*.
4. **Hashing:** in a Dictionary, keys have to be **hashable**; in a List there is no need
   for hashing.

**B12. What are the different built-in data types available in Python?**

**Numeric types:**
- `int` — for Integers
- `long` — for very large integers of non-limited length *(Python 2 only)*
- `float` — for decimal numbers
- `complex` — for representing complex numbers

**Sequence types:**
- `str` — similar to String in Java; can represent a sequence of characters
- `bytes` — a sequence of integers in the range of 0–255
- `bytearray` — like bytes, but mutable; only available in Python 3.x
- `list` — a sequence of objects
- `tuple` — a sequence of immutable objects

**Sets** (unordered collections):
- `set` — a collection of unique objects
- `frozen set` — a collection of unique immutable objects

**Mappings** (similar to a Map in Java):
- `dict` — also called hashmap; has key-value pairs to store information using hashing

**B13. What is a Namespace in Python?**
A Namespace is a **mapping between a name and an object**. It is currently implemented as a
Python dictionary. Examples: the set of built-in exception names, the set of built-in
names, local names in a function.

At different moments in Python, different Namespaces are created, and each can have a
different lifetime:
- For the list of built-in names, the Namespace is created when the Python interpreter starts.
- When the interpreter reads the definition of a module, it creates a **global namespace**
  for that module.
- When the interpreter calls a function, it creates a **local namespace** for that function.

**B14. How will you concatenate multiple strings together in Python?**
1. **Use the `+` operator:**
   ```python
   >>> fname = "John"
   >>> lname = "Ray"
   >>> print(fname + lname)
   JohnRay
   ```
2. **Use the join function:**
   ```python
   >>> ''.join(['John', 'Ray'])
   'JohnRay'
   ```

**B15. What is the use of the Pass statement in Python?**
The use of the Pass statement is to **do nothing**. It is just a placeholder for a statement
that is required for syntax purposes. It does not execute any code or command.

Use cases:
1. **Syntax purpose:**
   ```python
   >>> while True:
   ...     pass    # Wait till user input is received
   ```
2. **Minimal Class:**
   ```python
   >>> class MyMinimalClass:
   ...     pass
   ```
3. **Placeholder for TODO work:**
   ```python
   >>> def initialization():
   ...     pass    # TODO
   ```

**B16. What is the use of Slicing in Python?**
We can use Slicing to get a substring from a String. The syntax is very convenient.
```python
>>> name = "John"
>>> name[1:3]
'oh'
```
In Slicing we give two indices in the String to create a Substring. If we do not give the
first index, it defaults to 0:
```python
>>> name[:2]
'Jo'
```
If we do not give the second index, it defaults to the size of the String:
```python
>>> name[3:]
'n'
```

**B17. What is the difference between Docstring in Python and Javadoc in Java?**
A Docstring in Python is a string used for adding comments or summarizing a piece of code.
The main difference is that a **docstring is available during runtime as well**, whereas
Javadoc is removed from the bytecode and is not present in the `.class` file. We can even
use Docstring comments at runtime as an interactive help manual.

In Python we have to specify the docstring as the **first statement** of a code object,
just after the `def` or `class` statement. The docstring for a code object can be accessed
from the **`__doc__`** attribute of that object.

**B18. How do you perform unit testing for Python code?**
We can use the unit testing modules **`unittest`** or `unittest2` to create and run unit
tests, and even automate tests. Main components:
1. **Test fixture:** creates preparation methods required to run a test; can even perform
   post-test cleanup.
2. **Test case:** the main unit test that we run on a piece of code. Use the `TestCase` base
   class to create new test cases.
3. **Test suite:** aggregates unit test cases.
4. **Test runner:** executes unit tests and produces reports of the test run.

**B19. What is the difference between an Iterator and Iterable in Python?**
An **Iterable** is an object that can be iterated by an Iterator. In Python, an Iterator
object provides `__iter__()` and `next()` methods. An Iterable object has an `__iter__`
function that returns an Iterator object. When we work on a map or a for loop, we can use
the `next()` method to get an Iterable item from the Iterator.

**B20. What is the use of Generator in Python?**
We can use a Generator to create Iterators. A Generator is written like a regular function
but can use the **`yield`** statement to return data during the function call. This way we
can write complex logic that works as an Iterator.

A Generator is more compact than an Iterator because `__iter__()` and `next()` functions
are automatically created in a Generator. Also, within Generator code, **local variables and
execution state are saved between multiple calls**, so there is no need to add extra
variables like `self.index` to track iteration. Generators also increase readability — they
are a very simple implementation of an Iterator.

**B21. What is the significance of functions that start and end with `_` symbol in Python?**
Python provides many built-in functions that are surrounded by the `_` symbol at the start
and end of the function name. As per Python documentation, the double `_` symbol is used
for **reserved names** of functions. These are also known as **System-defined names**.
Important ones: `object.__new__`, `object.__init__`, `object.__del__`.

**B22. What is the difference between xrange and range in Python?**
In Python we use `range(0,10)` to create a **list** in memory for 10 numbers. Python
provided another function `xrange()` that is similar to `range()` but returns a **sequence
object instead of a list object**. In `xrange()` all the values are not stored
simultaneously in memory — it is a lazy-loading based function. As per Python
documentation, the benefit of `xrange()` over `range()` is very minimal in regular
scenarios. **As of version 3.1, xrange is deprecated.**

**B23. What is a lambda expression in Python?**
A lambda expression is used for creating an **anonymous function**. Wherever we need a
function, we can also use a lambda expression. We use the `lambda` keyword.

**Syntax:** `lambda argumentList: expression`
**Example:** `lambda a,b: a+b` — takes two arguments and returns their sum.

We can use a lambda expression to return a function. A lambda expression can also be used
to pass a function as an argument to another function.

**B24. How will you copy an object in Python?**
We have two options, similar to cloning an object in Java:
1. **Shallow Copy:** call `copy.copy(x)`. Python creates a new compound object based on the
   original object, and tries to put **references** from the original object into the copy
   object.
2. **Deep Copy:** call `copy.deepcopy(x)`. Python creates a new object and **recursively**
   creates and inserts copies of the objects from the original into the copy. In a deep copy
   we may face the issue of a recursive loop due to infinite recursion.

**B25. What are the main benefits of using Python?**
1. **Easy to learn:** Python is a simple language, easy for a new programmer.
2. **Large library:** a large library for utilities that can be used for different kinds of
   applications.
3. **Readability:** a variety of statements and expressions that are quite readable and
   very explicit in their use, increasing the readability of the overall code.
4. **Memory management:** built into the interpreter, so a developer does not have to spend
   effort managing memory among objects.
5. **Complex built-in data types:** `list`, `set`, `dict` etc. give very good performance
   and save time coding new features.

**B26. What is a metaclass in Python?**
A metaclass is also known as the **class of a class**. A class defines the behavior of an
instance; a metaclass defines the behavior of a class. The most common metaclass in Python
is **`type`**. We can subclass `type` to create our own metaclass. We can use a metaclass as
a **class-factory** to create different types of classes.

**B27. What is the use of frozenset in Python?**
A frozenset is a **collection of unique values**. In addition to all the properties of a
set, a frozenset is **immutable and hashable**. Once we have set the values in a frozenset
we cannot change them, so we cannot use `add` and `update` methods from `set` on a
frozenset. Being hashable, we can use frozenset objects as **keys in a Dictionary**.

**B28. What is Python Flask?**
Python Flask is a **micro-framework** based on Python to develop a web application. It is a
very simple application framework that has many extensions to build an enterprise-level
application. Flask does not provide a data abstraction layer or form validation by default;
we can use external libraries on top of Flask to perform such tasks.

**B29. What is None in Python?**
`None` is a reserved keyword used for **null objects**. It is neither a null value nor a
null pointer — it is an **actual object**. But there is only **one instance** of None in a
Python environment. We can use None as a default argument in a function. During comparison
we have to use the **`is`** operator instead of `==` for None.

**B30. What is the use of the zip() function in Python?**
The built-in `zip()` function can be used to **aggregate all the Iterable objects of an
Iterator**. We can use it to aggregate Iterable objects from two iterators as well.

```python
list_1 = ['a', 'b', 'c']
list_2 = ['1', '2', '3']
for a, b in zip(list_1, list_2):
    print(a, b)

# Output:
# a 1
# b 2
# c 3
```
By using `zip()` we can divide our input data from different sources into a fixed number of
sets.

**B31. What is the use of the `//` operator in Python?**
Python provides `//` to perform **floor division** of a number by another. The result is a
whole number (without decimal part) quotient obtained by dividing the left number by the
right number. It can also be used via `floordiv(a,b)`.
```
10 // 4   =  2
-10 // 4  = -3
```

**B32. What is a Module in Python?**
A Module is a script written in Python with import statements, classes, functions etc. We
can use a module in another Python script by importing it or by giving the complete
namespace. With Modules, we can divide the functionality of our application into smaller
chunks that can be easily managed.

**B33. How can we create a dictionary with an ordered set of keys in Python?**
In a normal dictionary in Python there is no order maintained between keys. To solve this
problem we can use the **`OrderedDict`** class, available since version 2.7. It is similar
to a dictionary but it **maintains the insertion order of keys** in the dictionary
collection.

**B34. Python is an Object Oriented programming language or a functional programming
language?**
Python uses most of the Object Oriented programming concepts, but we can also do functional
programming in Python. As per experts, Python is a **multi-paradigm** programming language.
We can do functional, procedural, object-oriented and imperative programming with Python.

**B35. How can we retrieve data from a MySQL database in a Python script?**
To retrieve data from a database we make use of the module available for that database. For
MySQL we import the **`MySQLdb`** module in our Python script. We first connect to a specific
database by passing URL, username, password and the name of the database. Once we establish
the connection we can open a cursor with the `cursor()` function. On an open cursor we can
run the `fetch()` function to execute queries and retrieve data from the database tables.

**B36. What is the difference between append() and extend() functions of a list in Python?**
We call `append()` to add an item to the end of a list. We call `extend()` to add another
list to the end of a list. In `append()` we have to add items one by one, but in `extend()`
multiple items from another list can be added at the same time.

**B37. How will you handle an error condition in Python code?**
We can implement **exception handling**. If we are expecting an error condition that we
cannot handle, we can **raise** an error with an appropriate message:
```python
>>> if student_score < 0: raise ValueError("Score can not be negative")
```
If we do not want to stop the program, we can just catch the error condition, print a
message and continue:
```python
#!/usr/bin/python
try:
    age = 18 + 'duration'
except:
    print("duration has to be a number")
age = 18
print(age)
```

**B38. What is the difference between split() and slicing in Python?**
Both work on a String object. By using `split()` we can get the **list of words** from a
String:
```python
'a b c '.split()      # returns ['a', 'b', 'c']
```
Slicing is a way of getting a **substring** from a String — it returns another String:
```python
>>> 'a b c'[2:3]      # returns 'b'
```

**B39. How will you check in Python, if a class is a subclass of another class?**
Python provides a useful method **`issubclass(a,b)`** to check whether class `a` is a
subclass of `b`.
```python
>>> issubclass(int, long)     # int is not a subclass of long
False
>>> issubclass(bool, int)     # bool is a subclass of int
True
```

**B40. How will you debug a piece of code in Python?**
We can use the debugger **`pdb`**. To start debugging, enter these lines at the top of a
Python script:
```python
import pdb
pdb.set_trace()
```
After adding these lines our code runs in debug mode. Now we can use commands like
breakpoint, step through, step into, etc.

**B41. How do you profile a Python script?**
Python provides a profiler called **`cProfile`**. We can call it from our code as well as
from the interpreter. It gives us the number of function calls as well as the total time
taken to run the script. We can even write the profile results to a file instead of standard
out.

**B42. What is the difference between 'is' and '==' in Python?**
We use `is` to check an object against its **identity**. We use `==` to check the
**equality** of two objects.
```python
>>> lst = [10, 20, 20]
>>> lst == lst[:]
True
>>> lst is lst[:]
False
```

**B43. How will you share variables across modules in Python?**
We can create a **common module** with the variables that we want to share. This common
module can be imported in all the modules in which we want to share the variables. In this
way all the shared variables will be in one module and available for sharing with any new
module as well.

**B44. How can we do Functional programming in Python?**
In Functional Programming, we decompose a program into functions. These functions take input
and after processing give an output. The function does not maintain any state. Python
provides built-in functions for functional programming:
1. `map()`
2. `reduce()`
3. `filter()`

Iterators and generators can also be used for Functional programming in Python.

**B45. What is the improvement in the enumerate() function of Python?**
`enumerate()` is an improvement over regular iteration. It returns an iterator that gives
`(0, item[0])`, `(1, item[1])`, etc.
```python
>>> thelist = ['a','b']
>>> for i, j in enumerate(thelist):
...     print(i, j)
...
0 a
1 b
```

**B46. How will you execute a Python script in Unix?**
To execute a Python script in Unix we need to have a Python executor in the Unix
environment. In addition we have to add the following line as the first line in the Python
script file:
```python
#!/usr/local/bin/python
```
This will tell Unix to use the Python interpreter to execute the script.

**B47. What are the popular Python libraries used in Data analysis?**
1. **Pandas** — powerful Python Data Analysis Toolkit
2. **SciKit** — a machine learning library in Python
3. **Seaborn** — a statistical data visualization library
4. **SciPy** — an open source system for science, mathematics and engineering implemented
   in Python

**B48. What is the output of the following code in Python?**
```python
>>> thelist = ['a','b']
>>> print(thelist[3:])
```
**Answer:**
```
[]
```
Even though the list has only 2 elements, the call to `thelist` with index 3 does not give
any index error.

**B49. What is the output of the following code in Python?**
```python
>>> name = 'John Smith'
>>> print(name[:5] + name[5:])
```
**Answer:**
```
John Smith
```
This is an example of Slicing. Since we are slicing at the same index, `name[:5]` gives the
substring up to (but excluding) the 5th location, and `name[5:]` gives the rest of the
substring from the 5th location. So we get the full name as output.

**B50. If you have data with names of customers and their location, which data type will you
use to store it in Python?**
We can use the **`dict`** data type to store key-value pairs. In this example the customer
name can be the key and their location can be the value. A Dictionary is an efficient way to
store data that can be looked up based on a key.

---

<a name="set-c"></a>
# SET C — 200 PYTHON INTERVIEW QUESTIONS
## Advanced Topics & Core Concepts

### C001–C010: Modern syntax, concurrency & functional tooling

**C001. What is the walrus operator (`:=`)?**
The walrus operator, introduced in Python 3.8 (PEP 572), is the **assignment expression**
operator. It assigns a value to a variable as part of a larger expression. Example:
`while chunk := f.read(8192): process(chunk)`. It avoids redundant computation by assigning
and testing in the same expression.

**C002. What is the `dataclasses` module?**
The dataclasses module (Python 3.7+) provides a `@dataclass` decorator that auto-generates
`__init__`, `__repr__` and `__eq__` methods for classes based on annotated fields. It
reduces boilerplate for data-holding classes. Optional parameters include `frozen=True`
(immutable), `order=True` (comparison methods), and `field()` for default values.

**C003. What are Python type hints?**
Type hints (Python 3.5, PEP 484) allow you to annotate variables and function signatures
with expected types. Example: `def greet(name: str) -> str`. They are **not enforced at
runtime** but enable static analysis with tools like mypy, improve IDE support, and make
code more self-documenting.

**C004. What is async/await in Python?**
async/await is Python's syntax for writing asynchronous, non-blocking code using coroutines.
`async def` defines a coroutine function. `await` suspends the coroutine until the awaited
task completes, yielding control to the event loop. Used with asyncio for efficient I/O-bound
concurrency without threads.

**C005. What is the `asyncio` module?**
asyncio is Python's standard library for writing concurrent I/O-bound code using an event
loop and coroutines. Key functions: `asyncio.run()`, `asyncio.gather()` (run coroutines
concurrently), `asyncio.sleep()`, and `asyncio.create_task()`. It is the foundation for
async frameworks like FastAPI and aiohttp.

**C006. What is the `multiprocessing` module?**
The multiprocessing module enables **true parallelism** by spawning separate processes, each
with its own Python interpreter and memory space — bypassing the GIL. Ideal for CPU-bound
tasks. Key classes: `Process`, `Pool` (for parallel map/apply), `Queue`, and `Pipe` for
inter-process communication.

**C007. What is the `threading` module?**
The threading module enables concurrent execution using threads within the same process.
Threads share memory, requiring synchronization (`Lock`, `RLock`, `Semaphore`, `Event`) to
avoid race conditions. Due to the GIL, threads are best suited for **I/O-bound** tasks, not
CPU-bound parallel computation.

**C008. What is memoization and how is it implemented in Python?**
Memoization is an optimization technique that **caches the results of expensive function
calls** so they are not recomputed for the same inputs. In Python use
`@functools.lru_cache(maxsize=None)` or `@functools.cache` (Python 3.9+) as a decorator above
a recursive or expensive function.

**C009. What is the `functools` module?**
Provides higher-order functions. Key tools: `functools.reduce()` (applies a function
cumulatively), `@functools.lru_cache` (memoization), `functools.partial()` (partially applies
a function with preset arguments), and `functools.wraps()` (preserves metadata of wrapped
functions in decorators).

**C010. What is the `itertools` module?**
Provides fast, memory-efficient tools for iterators. Key functions: `chain()` (chains
iterables), `cycle()` (infinitely cycles), `combinations()` and `permutations()`
(combinatorics), `product()` (cartesian product), `groupby()` (groups consecutive elements),
and `islice()` (slices an iterator without materializing it).

### C011–C020: Data structures & object model internals

**C011. What is a namedtuple?**
A factory function from the `collections` module that creates tuple subclasses with named
fields. Example: `Point = namedtuple('Point', ['x', 'y']); p = Point(3, 4); p.x` gives 3.
Namedtuples are immutable, memory-efficient, and more readable than plain tuples.

**C012. What is the `collections` module?**
Provides specialized container data types: `Counter` (counts hashable objects), `defaultdict`
(dict with a default factory for missing keys), `OrderedDict` (remembers insertion order),
`deque` (double-ended queue with O(1) append/pop from both ends), and `namedtuple` (tuple
with named fields).

**C013. What is the `heapq` module?**
Implements a **min-heap** (priority queue) using a regular Python list. Key functions:
`heapq.heappush()`, `heapq.heappop()` (removes smallest), `heapq.heapify()` (converts list
in-place), `heapq.nlargest()`, and `heapq.nsmallest()`. Useful for efficiently finding top-K
elements.

**C014. What is multiple inheritance and MRO?**
Multiple inheritance allows a class to inherit from more than one parent. The **Method
Resolution Order (MRO)** defines the search order when looking up a method. Python uses the
**C3 linearization** algorithm. Inspect it using `ClassName.__mro__` or `ClassName.mro()`.
`super()` follows the MRO automatically.

**C015. What is a metaclass in Python?**
A metaclass is a class whose instances are **classes themselves**. It controls how a class is
created. The default metaclass is `type`. You define a custom metaclass by inheriting from
`type` and overriding `__new__` or `__init__`. Used in frameworks like Django ORM for
declarative class definitions.

**C016. What is `__new__` and how does it differ from `__init__`?**
`__new__` **creates and returns a new instance** of a class — called before `__init__`.
`__init__` then **initializes** the already-created instance. `__new__` is useful when
subclassing immutable types like `int` or `str`, or when implementing singleton patterns
where you control instance creation directly.

**C017. What is the difference between `__getattr__` and `__getattribute__`?**
`__getattribute__` is called on **every** attribute access. `__getattr__` is called **only
when the attribute was not found** through the normal mechanism — it is a fallback.
Overriding `__getattribute__` carelessly can cause infinite recursion; always call
`super().__getattribute__()` inside it.

**C018. What are property decorators?**
The `@property` decorator allows a method to be accessed like an attribute. It enables
getter, setter and deleter functionality with `@property`, `@name.setter` and
`@name.deleter`. This enforces encapsulation by validating or computing values on access
without exposing internal implementation details.

**C019. What is a descriptor in Python?**
A descriptor is any object that defines `__get__`, `__set__` or `__delete__` methods,
controlling attribute access on another class. They are the mechanism behind `@property`,
`@classmethod` and `@staticmethod`. **Data descriptors** define both `__get__` and `__set__`;
**non-data descriptors** define only `__get__`.

**C020. What is the purpose of `__slots__`?**
`__slots__` restricts instance attributes to a fixed set, replacing the default per-instance
`__dict__`. This **reduces memory usage significantly** for classes with many instances and
speeds up attribute access. Instances with `__slots__` cannot have arbitrary new attributes
added at runtime.

### C021–C030: Operators, scope, exceptions & binary data

**C021. What is operator overloading in Python?**
Allows custom classes to define behavior for built-in operators using dunder methods.
Examples: `__add__` for `+`, `__sub__` for `-`, `__mul__` for `*`, `__lt__` for `<`,
`__eq__` for `==`, `__len__` for `len()`, `__contains__` for `in`. This allows objects to
integrate naturally with Python syntax.

**C022. What is the difference between `global` and `nonlocal`?**
`global x` inside a function declares that `x` refers to the **module-level global** variable.
`nonlocal x` inside a nested function refers to the variable in the **nearest enclosing
(non-global)** scope. Neither keyword is needed just to read a variable — only to reassign it.

**C023. What is exception chaining in Python?**
Exception chaining links exceptions using `raise NewException from original`. The `from`
clause sets the `__cause__` attribute. When an exception occurs inside an except block
without `from`, Python sets `__context__` implicitly. Use `raise X from None` to suppress the
original exception context entirely.

**C024. What is the difference between `raise` and `raise from`?**
`raise ExceptionType(message)` raises a new exception. Bare `raise` re-raises the current
exception inside an except block. `raise NewException from original` explicitly chains
exceptions, setting `__cause__` on the new exception. Use `raise X from None` to hide the
original exception entirely.

**C025. What is string interning in Python?**
An optimization where Python **reuses the same object for identical string literals**, saving
memory. Short strings and identifiers are typically interned automatically. You can manually
intern strings using `sys.intern()`. **Never rely on `is` for string equality checks** —
always use `==`.

**C026. What are Python's bitwise operators?**
They work on integers at the binary level: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<`
(left shift), `>>` (right shift). Example: `5 & 3 = 1` (0101 & 0011 = 0001). Used in low-level
programming, flags, masking, and performance-critical bit manipulation.

**C027. What is the `contextlib` module?**
Provides utilities for context managers. Key tools: `@contextlib.contextmanager` (turns a
generator into a context manager), `contextlib.suppress(exceptions)` (suppresses specified
exceptions), `contextlib.nullcontext()` (a no-op context manager), and `ExitStack` (dynamic
stacking of context managers).

**C028. What is the difference between `bytes`, `bytearray` and `memoryview`?**
`bytes` is an **immutable** sequence of integers (0–255) for binary data. `bytearray` is its
**mutable** counterpart. `memoryview` exposes the buffer protocol of an object, allowing
slicing and working with binary data **without copying it** — critical for performance when
working with large binary buffers.

**C029. What is the `abc` module?**
The abc (Abstract Base Classes) module provides infrastructure for defining abstract base
classes. Using `@abc.abstractmethod` you declare methods subclasses must implement. A class
with unimplemented abstract methods **cannot be instantiated** — it raises `TypeError`. ABCs
enforce interface contracts throughout a class hierarchy.

**C030. What is the `struct` module?**
Converts between Python values and **C structs represented as bytes**. Used for binary data
parsing and packing — reading binary file formats or network protocols. `struct.pack(format,
values)` returns bytes; `struct.unpack(format, buffer)` returns a tuple. Format strings use
`'i'` (int), `'f'` (float), `'s'` (char[]).

### C031–C040: System modules, built-ins & text processing

**C031. What is the `os` module used for?**
Provides a portable interface to operating system functionality: `os.path` for path
manipulation (`join`, `exists`, `dirname`), `os.listdir()` to list directory contents,
`os.getcwd()` for current directory, `os.makedirs()` to create directories, `os.environ` for
environment variables, and `os.remove()` to delete files.

**C032. What is the `sys` module used for?**
Provides access to interpreter-specific variables and functions: `sys.argv` (command-line
arguments), `sys.path` (module search path), `sys.exit()`, `sys.stdin/stdout/stderr`,
`sys.version`, and `sys.getrecursionlimit()`.

**C033. What is the difference between Python 2 and Python 3?**
Python 3 introduced `print` as a function, true division by default, Unicode strings by
default, and removed `xrange()`. **Python 2 reached end-of-life in January 2020.** Python 3
also introduced f-strings, type hints, async/await, and many standard library improvements
not available in Python 2.

**C034. What is the difference between `any()` and `all()`?**
`any(iterable)` returns True if **at least one** element is truthy; False if the iterable is
empty. `all(iterable)` returns True if **all** elements are truthy; also **True if the
iterable is empty**. Both use **short-circuit evaluation** — they stop processing as soon as
the result is determined.

**C035. What is the `zip()` function?**
Takes multiple iterables and returns an iterator of tuples, pairing elements at the same
index. Example: `zip([1,2,3], ['a','b','c'])` gives `(1,'a'), (2,'b'), (3,'c')`. **It stops
at the shortest iterable.** Use `itertools.zip_longest()` to fill missing values with a
fillvalue.

**C036. What is the `enumerate()` function?**
`enumerate(iterable, start=0)` returns an iterator of `(index, value)` tuples, allowing you
to loop with both index and value simultaneously. Example: `for i, val in
enumerate(['a','b','c'])` gives `(0,'a'), (1,'b'), (2,'c')`. The `start` parameter sets the
initial counter value.

**C037. What is the `re` module in Python?**
Provides **regular expression** support. Key functions: `re.match()` (matches at start),
`re.search()` (searches anywhere), `re.findall()` (returns all matches as a list), `re.sub()`
(replaces matches), `re.compile()` (compiles a pattern for reuse). Use raw strings (`r'\d+'`)
to avoid backslash conflicts.

**C038. What is the difference between `re.match()` and `re.search()`?**
`re.match()` only matches **at the beginning** of the string — if the pattern is not at the
start, it returns None. `re.search()` **scans through the entire string** for any location
where the pattern matches. To match the full string, use `re.fullmatch()` or add `^` and `$`
anchors.

**C039. What is JSON and how does Python work with it?**
JSON is a lightweight data-interchange format. Python's `json` module handles serialization
and deserialization: `json.dumps(obj)` converts a Python object to a JSON string;
`json.loads(string)` parses JSON to a Python object. `json.dump()` and `json.load()` work with
file objects directly.

**C040. What is Python's logging best practice?**
Use the `logging` module instead of `print()` for production code. Create a logger with
`logging.getLogger(__name__)`. Use levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Configure
handlers and formatters to control output. Use **lazy formatting**: `logger.debug('%s',
value)` instead of `logger.debug(f'{value}')`.

### C041–C050: Comparisons, formatting & typing basics

**C041. What is chained comparison in Python?**
Python allows chaining comparisons: `1 < x < 10` is evaluated as `(1 < x) and (x < 10)`,
where `x` is **evaluated only once**. This is more readable and efficient than writing them
separately. Chaining works with all comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.

**C042. What is the difference between list, tuple and array?**
`list` is a dynamic, mutable sequence holding any type. `tuple` is immutable and slightly more
memory-efficient. `array.array` (from the `array` module) stores elements of a **single
C-type**, making it much more memory-efficient for large numeric data. For numerical
computing, **NumPy arrays** are preferred over all three.

**C043. What is the difference between `os.path.join` and string concatenation?**
`os.path.join()` correctly constructs file paths by inserting the **OS-appropriate
separator** (`/` on Unix, `\` on Windows) and handling edge cases like trailing slashes.
String concatenation is error-prone and platform-dependent. Python 3.4+ `pathlib.Path`
provides an even more readable object-oriented approach.

**C044. What is the difference between `str.format()` and f-strings?**
`str.format()` uses `{}` placeholders: `'{} {}'.format('hello', 'world')`. F-strings (Python
3.6+) embed expressions directly: `f'{name.upper()}'`. **F-strings are faster at runtime and
more readable.** For Python <3.6, `format()` is the preferred modern alternative to `%`-style
formatting.

**C045. What is Python's numeric precision issue with floats?**
Floating-point numbers follow the **IEEE 754** standard, which can cause precision issues
like `0.1 + 0.2 != 0.3`, because many decimal fractions cannot be represented exactly in
binary. For precise decimal arithmetic, use the `decimal.Decimal` class. **Always use
`Decimal` instead of `float` for financial calculations.**

**C046. What is a Python virtual environment?**
An isolated Python environment with its own interpreter and packages, separate from the
system Python. It **prevents dependency conflicts** between projects. Created using
`python -m venv env_name`, activated with `source env_name/bin/activate` (Linux/Mac) or
`env_name\Scripts\activate` (Windows).

**C047. What are Python's string methods `split()`, `join()`, `strip()`?**
`split(sep)` splits a string into a list by separator (default: whitespace).
`join(iterable)` joins strings with the calling string as separator: `', '.join(['a','b','c'])`
gives `'a, b, c'`. `strip()` removes leading and trailing whitespace (or specified
characters); `lstrip()` and `rstrip()` strip from one side only.

**C048. What is the difference between `input()` and `raw_input()`?**
In Python 3, `input()` reads a line from stdin and **always returns a string**. In Python 2,
`raw_input()` did the same, while `input()` **evaluated the expression** (a security risk).
Python 3 removed `raw_input()` entirely and made `input()` safe by always returning a string
that you explicitly convert.

**C049. What is pickling and unpickling?**
Pickling serializes a Python object into a byte stream using the `pickle` module, so it can be
saved to a file or transmitted. Unpickling is the reverse. Use `pickle.dump()` to pickle and
`pickle.load()` to unpickle. **Never unpickle data from untrusted sources.**

**C050. What is duck typing?**
A concept where the **type** of an object is less important than the **methods or attributes**
it has. If an object behaves like a duck (has the needed methods), Python treats it as one.
This allows flexible, dynamic code without strict type checking — enabling polymorphism
**without inheritance**.

### C051–C060: Copies, arguments, methods & mutability

**C051. What is the difference between a shallow copy and a deep copy?**
A **shallow copy** (`copy.copy()`) creates a new container but **shares references** to
nested objects. A **deep copy** (`copy.deepcopy()`) creates a fully independent object with
all nested objects also copied recursively. **Assignment (`b = a`) makes both variables point
to the same object — no copy at all.**

**C052. What is the difference between positional and keyword arguments?**
Positional arguments are passed in order and matched by position. Keyword arguments are
passed by explicitly naming the parameter (`key=value`), allowing them to be in any order.
Keyword arguments improve readability and allow skipping optional parameters that have
default values.

**C053. What is the difference between `assert` and raising an exception?**
`assert condition, message` raises `AssertionError` if False. **It can be disabled with the
`-O` flag** and should never be used for production validation. Raising exceptions
(`raise ValueError(...)`) is the correct approach for runtime error handling that must not be
silently bypassed in optimized builds.

**C054. What is the difference between `@staticmethod` and `@classmethod`?**
`@staticmethod` defines a method with **no implicit first argument** — a plain function
namespaced inside a class. `@classmethod` receives **`cls`** (the class itself) as the first
argument and can access or modify class-level state. `@classmethod` is commonly used as an
**alternative constructor** pattern.

**C055. What is the difference between mutable and immutable objects?**
**Mutable** objects can be changed after creation — lists, dictionaries and sets.
**Immutable** objects cannot be changed — integers, floats, strings, tuples and frozensets.
Immutable objects are **hashable** and can be used as dictionary keys or set elements;
mutable objects cannot.

**C056. What are Python modules and packages?**
A **module** is a single Python file (`.py`) containing functions, classes and variables. A
**package** is a directory containing multiple modules and an `__init__.py` file. Modules are
imported using `import module_name` or `from module import item`. Packages help organize large
codebases into namespaces.

**C057. What is the `with` statement used for?**
The `with` statement is used for **context management** — ensuring proper acquisition and
release of resources. It calls `__enter__` at the start and `__exit__` at the end, **even if
an exception occurs**. Most commonly used for file handling: `with open("file.txt") as f:`
automatically closes the file.

**C058. What is list comprehension?**
Provides a concise way to create lists. Syntax: `[expression for item in iterable if
condition]`. Example: `squares = [x**2 for x in range(10) if x % 2 == 0]` creates squares of
even numbers. Dictionary and set comprehensions follow the same pattern using `{}` instead.

**C059. What is a generator expression?**
Like a list comprehension but uses **parentheses**: `(x**2 for x in range(10))`. Unlike list
comprehensions, generator expressions produce items **lazily on demand**, using much less
memory. Ideal for large datasets where you don't need all items at once.

**C060. What is the difference between `/` and `//` in Python?**
`/` is **true division** and always returns a float (e.g. `7/2 = 3.5`). `//` is **floor
division** and returns the largest integer less than or equal to the result (e.g. `7//2 = 3`).
For negative numbers, floor division rounds toward negative infinity: `-7//2 = -4`.

### C061–C070: Sets, identity, MRO & list operations

**C061. What is the difference between a set and a frozenset?**
A `set` is a **mutable**, unordered collection of unique elements defined with `{}` or
`set()`. A `frozenset` is its **immutable** version created with `frozenset()`. Because
frozensets are immutable, they are **hashable** and can be used as dictionary keys or elements
of another set, unlike regular sets.

**C062. What is the difference between `is None` and `== None`?**
**Always use `is None` or `is not None`** rather than `== None`. Since None is a singleton in
Python, `is` checks identity and is guaranteed to work correctly. `== None` can be overridden
by a class's `__eq__` method, making it unreliable. **PEP 8 explicitly recommends using `is
None`.**

**C063. What is method resolution order (MRO) and how does `super()` use it?**
MRO is the order in which Python searches classes for a method. **`super()` doesn't just call
the parent class — it calls the next class in the MRO.** This ensures cooperative multiple
inheritance works correctly, with each class called exactly once in a predictable order
defined by C3 linearization.

**C064. What is the difference between `append()`, `extend()` and `insert()` in lists?**
`append(x)` adds a **single element** to the end. `extend(iterable)` adds **all elements** of
an iterable to the end. `insert(i, x)` inserts element x at position i, shifting subsequent
elements. `append` and `extend` are **O(1) amortized**; `insert` is **O(n)** because it shifts
elements to make room.

**C065. What is the difference between `map()` and a list comprehension?**
Both apply a function to each element of an iterable. `map(func, iterable)` returns a **lazy
iterator** and is slightly faster for simple built-in functions. List comprehensions are more
readable, support filtering (`if condition`), and are generally preferred in Python. Use
`map()` when passing an existing named function directly.

**C066. What is `*args` and `**kwargs` in function definitions?**
`*args` collects extra **positional** arguments into a **tuple**. `**kwargs` collects extra
**keyword** arguments into a **dictionary**. They allow functions to accept variable numbers
of arguments. Order must be: regular args, `*args`, keyword-only args, `**kwargs`. Used widely
in wrappers and decorators.

**C067. What is the difference between `del`, `remove()` and `pop()` for lists?**
`del list[index]` removes an element at a specific index. `list.remove(value)` removes the
**first occurrence** of a specific value — raises `ValueError` if not found. `list.pop(index)`
**removes and returns** the element at the given index (default: last). `pop()` from the end
is O(1); from the middle is O(n).

**C068. What is the difference between recursion and iteration?**
Recursion solves a problem by having a function call itself with a smaller sub-problem, using
the **call stack**. Iteration uses loops. Recursion is elegant for tree/graph traversal but
risks **stack overflow** for deep recursion. Iteration is generally more memory-efficient and
faster for simple repetition.

**C069. What are Python's built-in functions for sorting?**
`sorted(iterable, key=None, reverse=False)` returns a **new sorted list** without modifying
the original. `list.sort()` sorts **in-place and returns None**. Both use **Timsort**,
O(n log n). The `key` parameter accepts a function applied to each element for comparison:
`sorted(words, key=str.lower)`.

**C070. What is the purpose of `__repr__` vs `__str__`?**
`__str__` returns a **human-readable** string for end users, used by `print()` and `str()`.
`__repr__` returns an **unambiguous developer-facing** representation, used by the interpreter
and `repr()`. If only `__repr__` is defined, it serves as fallback for `__str__`. Best
practice: `__repr__` should return a string that could recreate the object.

### C071–C080: Coroutines, GIL, class variables & control keywords

**C071. What is the difference between a coroutine and a generator?**
**Generators** produce data for iteration using `yield`. **Coroutines** are designed for
concurrency and can both **receive and yield** values using `value = yield`. In modern Python,
`async def` coroutines (used with asyncio) are distinct from generator-based coroutines and
are the preferred approach for async programming.

**C072. What is the GIL and when does it matter?**
The **Global Interpreter Lock (GIL)** allows only one thread to execute Python bytecode at a
time. It matters for **CPU-bound** tasks — use multiprocessing to bypass it. For **I/O-bound**
tasks (network, file), threading is effective since threads release the GIL while waiting.
Python 3.13 introduces an experimental free-threaded build.

**C073. What is the difference between a class variable and an instance variable?**
A **class variable** is defined directly inside the class (outside methods) and is **shared
across all instances**. An **instance variable** is defined inside `__init__` using
`self.variable` and is **unique to each instance**. Modifying a class variable via an instance
creates a new instance variable that **shadows** the class variable for that instance only.

**C074. What is PEP 8 and why does it matter?**
PEP 8 is Python's official style guide. It covers naming conventions (`snake_case` for
variables/functions, `PascalCase` for classes), indentation (4 spaces), max line length (79
chars), blank lines, import ordering and commenting. Following PEP 8 ensures consistent,
readable and professionally written Python code.

**C075. What is the difference between `type()` and `isinstance()`?**
`type(obj)` returns the **exact class** of an object. `isinstance(obj, class)` checks whether
an object is an instance of a class **or any of its subclasses**. `isinstance` is preferred
for type checking because it properly handles inheritance, while `type()` does not consider
subclasses — making it too strict for most use cases.

**C076. What is monkey patching in Python?**
The **dynamic modification of a class or module at runtime**, replacing or extending its
attributes or methods without changing the original source code. Useful in testing (mocking)
and quick fixes, but should be used sparingly as it can make code unpredictable and difficult
to maintain.

**C077. What is the difference between `__iter__` and `__next__`?**
`__iter__` returns the **iterator object itself** (usually `self`) and is called when `iter()`
is invoked on an object. `__next__` returns the next value and raises **`StopIteration`** when
exhausted. A class implementing both is a full iterator. An **iterable** only needs `__iter__`,
which returns a separate iterator object.

**C078. What is the purpose of the `pass` statement?**
`pass` is a **no-operation placeholder** used when a statement is syntactically required but
no action is needed. Common uses: empty function or class bodies during development, empty
except blocks when intentionally ignoring an exception, and as a placeholder in abstract
method stubs before implementation.

**C079. What is the difference between `is` and `==` in Python?**
`==` checks for **value equality** — whether two objects have the same value. `is` checks for
**identity** — whether two variables point to the exact same object in memory. Example:
`a = [1,2]; b = [1,2]`; `a == b` is True but `a is b` is False. **Use `is` only for None, True
and False checks.**

**C080. What is the difference between `break`, `continue` and `pass` in loops?**
`break` **exits the current loop entirely**, skipping any remaining iterations and the `else`
clause. `continue` **skips the rest of the current iteration** and moves to the next one.
`pass` **does nothing** — it is a syntactic placeholder that allows an empty loop body without
causing a syntax error.

### C081–C090: Decorators, closures, scope & modern syntax

**C081. What is a decorator in Python?**
A function that takes another function (or class) and **extends its behavior without
modifying its source code**. Applied with `@decorator_name` syntax above a function
definition. Used for logging, timing, access control, caching and validation, and can be
stacked.

**C082. What is a closure in Python?**
A **nested function that captures and remembers variables from its enclosing scope**, even
after the outer function has returned. It requires a nested function referencing a variable
from the enclosing function, and the enclosing function returning that nested function.
Closures underpin decorators and factory functions.

**C083. What are lambda functions?**
A lambda is an **anonymous, single-expression** function defined with the `lambda` keyword:
`lambda x, y: x + y`. It cannot contain statements or multiple expressions, only one implicit
return. Commonly used as a short callback for `sorted()`, `map()` or `filter()` where defining
a full function would be overkill.

**C084. What does it mean that functions are "first-class objects" in Python?**
Functions being first-class means they can be **assigned to variables, stored in data
structures, passed as arguments, and returned from other functions**, just like any other
object. This enables higher-order functions, decorators, and functional programming patterns
such as passing callbacks.

**C085. What is the LEGB rule in Python?**
LEGB describes the order Python searches for a name: **L**ocal (current function),
**E**nclosing (any enclosing function), **G**lobal (module level), and **B**uilt-in (Python's
built-in namespace). The interpreter stops at the first scope where the name is found, raising
`NameError` if none match.

**C086. Why is using a mutable default argument dangerous in Python?**
Default argument values are evaluated **once, at function definition time**, not on every
call. If a default is a mutable object like a list or dict, that same object **persists across
calls and accumulates state**. The fix is to default to `None` and create the mutable object
inside the function body.

**C087. What are positional-only parameters in Python?**
Introduced in PEP 570 (Python 3.8), a forward slash (`/`) in a function signature marks all
parameters before it as **positional-only** — they cannot be passed by keyword. Example:
`def f(a, b, /): ...`. This lets library authors rename parameters later without breaking
callers.

**C088. What are keyword-only parameters in Python?**
An asterisk (`*`) in a function signature marks all parameters after it as **keyword-only** —
they must be passed by name, not position. Example: `def f(a, *, b): ...` requires calling
`f(1, b=2)`. This improves call-site clarity for functions with many optional flags.

**C089. What does the `=` specifier do in an f-string?**
Added in Python 3.8, writing `f'{expr=}'` prints **both the expression's source text and its
value**, e.g. `f'{x=}'` outputs `'x=5'`. This is a quick debugging aid that avoids manually
typing variable names in print statements while inspecting values.

**C090. What is dictionary comprehension?**
Builds a dict concisely using `{key_expr: value_expr for item in iterable if condition}`.
Example: `{x: x**2 for x in range(5)}` creates squares keyed by their base number. It is more
readable and often faster than building a dict with an explicit loop.

### C091–C100: Comprehensions, formatting, slicing & object identity

**C091. What is set comprehension?**
Builds a set using `{expression for item in iterable if condition}`, automatically
**discarding duplicates**. Example: `{x % 3 for x in range(10)}` produces the set of possible
remainders. It follows the same syntax pattern as list and dict comprehensions but with curly
braces and no colon.

**C092. What is Python's format specification mini-language?**
Controls how values are rendered inside `str.format()` or f-strings, using syntax like
`{value:width.precision type}`. Examples: `f'{3.14159:.2f}'` gives `'3.14'`, `f'{42:05d}'`
gives `'00042'`, and `f'{n:,}'` adds thousands separators. It also supports alignment
(`<`, `>`, `^`) and sign control.

**C093. How does slicing work in Python?**
Slicing extracts a sub-sequence using `sequence[start:stop:step]`. `start` is **inclusive**,
`stop` is **exclusive**, and `step` controls direction and stride. Example: `'hello'[1:4]`
gives `'ell'`, and `'hello'[::-1]` reverses the string. Omitted indices default to the
sequence's start or end.

**C094. How does negative indexing work in Python?**
Negative indices count **from the end** of a sequence, with `-1` referring to the last
element, `-2` the second-to-last, and so on. Example: `'python'[-1]` gives `'n'`. Negative
indices can be combined with slicing, e.g. `list[-3:]` returns the last three elements.

**C095. What does the `id()` function do?**
`id(obj)` returns a **unique integer identifier** for an object for the duration of its
lifetime, representing its memory address in CPython. It is used with `is` comparisons and to
check whether two variables reference the same object rather than equal but distinct objects.

**C096. What does the `hash()` function do, and how does it relate to `__eq__`?**
`hash(obj)` returns an integer hash value used by dicts and sets for fast lookups. **Objects
that compare equal (`__eq__` returns True) must have the same hash value**, or dict/set
behavior breaks. If you override `__eq__` on a class, you must also define a consistent
`__hash__`, or the class becomes unhashable.

**C097. What is the `weakref` module used for?**
Creates references to objects that **don't increase their reference count**, allowing the
object to be garbage collected even while the weak reference exists. Useful for caches and
observer patterns where you don't want to keep an object alive just because it's being
tracked.

**C098. How does garbage collection work in CPython?**
CPython primarily uses **reference counting**: each object tracks how many references point to
it, and is deallocated immediately when the count reaches zero. A supplementary **generational
garbage collector** (the `gc` module) periodically detects and cleans up **reference cycles**
that reference counting alone cannot resolve.

**C099. What is the `gc` module used for?**
Exposes Python's cyclic garbage collector. Key functions: `gc.collect()` forces a collection
cycle, `gc.disable()`/`gc.enable()` toggle automatic collection, and `gc.get_objects()` lists
tracked objects. Mainly used for diagnosing memory leaks or tuning performance in long-running
applications.

**C100. What is the Enum module used for?**
Lets you define a set of **named, related constants** as a class using `Enum`. Example:
`class Color(Enum): RED = 1; GREEN = 2`. Members are compared by identity, are iterable, and
print with a readable name instead of a bare value, improving code clarity over magic numbers.

### C101–C110: Enums, typing & dataclasses

**C101. What is the difference between IntEnum, StrEnum and IntFlag?**
`IntEnum` members behave like plain integers and can be compared to ints directly. `StrEnum`
(Python 3.11+) members behave like strings. `IntFlag` supports **bitwise combination** of
members (e.g. `Permissions.READ | Permissions.WRITE`) for representing flag-like sets, while
regular `Enum` members support none of these interoperations.

**C102. What does the `typing` module provide?**
Supplies generic type hint constructs: `List[int]`, `Dict[str, int]`, `Optional[str]`
(equivalent to `Union[str, None]`), and `Union[int, str]` for multiple possible types. Since
Python 3.9+, built-in generics like `list[int]` are often preferred over `typing.List`, though
`typing.Optional` and `typing.Union` are still common.

**C103. What is a TypeVar used for in typing?**
`TypeVar` defines a **generic placeholder type** so a function's input and output types stay
linked. Example: `T = TypeVar('T'); def first(items: list[T]) -> T`. Static type checkers like
mypy use this to verify that the returned value matches the type of the list's elements.

**C104. What is a Protocol in the typing module?**
`Protocol` (PEP 544) enables **structural subtyping** — a form of static duck typing. A class
satisfies a Protocol if it has the required methods and attributes, **without needing to
explicitly inherit from it**. This lets type checkers validate duck-typed code that relies on
an object's shape rather than its class hierarchy.

**C105. What does the `@overload` decorator do?**
`typing.overload` lets you declare **multiple type signatures for the same function name**,
each followed by `...` as a stub body, ending with one real implementation. Static type
checkers use the overloads to pick the correct return type based on argument types, useful
when behavior varies by input type.

**C106. What are Final and Literal in the typing module?**
`Final` marks a variable, attribute or method as **not meant to be reassigned or overridden**,
enforced by static type checkers, not at runtime. `Literal` restricts a value to a specific
set of literal values, e.g. `Literal['GET', 'POST']`, enabling precise validation of allowed
strings or constants.

**C107. What is a TypedDict?**
`TypedDict` (from typing) defines a dictionary type with a **fixed set of expected string keys
and value types**, without creating a full class. Example: `class Point(TypedDict): x: int;
y: int`. It's purely a static typing construct — at runtime, a TypedDict value is still a
plain dict.

**C108. What is the difference between `typing.NamedTuple` and `collections.namedtuple`?**
`collections.namedtuple()` is a **function** that creates a tuple subclass from a string of
field names. `typing.NamedTuple` is a **class-based syntax** that additionally supports type
annotations and default values, e.g. `class Point(NamedTuple): x: int; y: int = 0`. Both
produce equivalent, immutable, tuple-based objects.

**C109. What is `__post_init__` in a dataclass?**
A method automatically called by the generated `__init__` **right after all fields are set**,
letting you add custom validation or compute derived fields. Commonly used with
`dataclasses.field(init=False)` to compute a value from other fields once the object is
otherwise fully initialized.

**C110. What is `dataclasses.field()` used for?**
`field()` customizes an individual dataclass attribute beyond a simple default value.
**`default_factory=list` supplies a fresh mutable default per instance** (avoiding the
shared-default pitfall), while other options include `repr=False`, `compare=False` and
`init=False` to exclude a field from generated methods.

### C111–C120: functools, itertools & testing

**C111. What is `functools.singledispatch` used for?**
Turns a function into a **generic function that dispatches to different implementations based
on the type of its first argument**. Register type-specific implementations with
`@func.register(SomeType)`. It's a clean alternative to long `isinstance()` chains when
behavior needs to vary by argument type.

**C112. What is `functools.cached_property`?**
`@functools.cached_property` (Python 3.8+) computes an instance property **once and caches the
result** in the instance's `__dict__`, so subsequent accesses skip recomputation. Unlike
`@property`, the value is stored, not recalculated, making it suited for expensive derived
attributes.

**C113. What is the `operator` module used for?**
Exposes built-in operators as **regular functions**: `operator.add`, `operator.mul`,
`operator.itemgetter`, `operator.attrgetter`. These are useful as key functions for `sorted()`
or as callables passed to `functools.reduce()`, and are typically **faster than an equivalent
lambda**.

**C114. What does `itertools.accumulate()` do?**
`itertools.accumulate(iterable, func=operator.add)` returns an iterator of **running totals**
(or running results of any binary function) over the input. Example:
`list(accumulate([1,2,3,4]))` gives `[1,3,6,10]`. Passing `max` as func produces a running
maximum instead of a running sum.

**C115. What does `itertools.tee()` do?**
`itertools.tee(iterable, n)` splits a single iterable into **n independent iterators** that
can each be consumed separately at their own pace. Because the original iterator is consumed
as needed and buffered internally, **once `tee()` is called, the original iterable should not
be used directly**.

**C116. What does `itertools.starmap()` do?**
`itertools.starmap(func, iterable_of_tuples)` applies func to each tuple in the iterable by
**unpacking it as arguments**, equivalent to `[func(*args) for args in iterable]`. Useful when
your data is already stored as tuples of arguments, avoiding a lambda wrapper just to unpack
them.

**C117. What does `itertools.compress()` do?**
`itertools.compress(data, selectors)` filters elements from data, keeping only those where the
corresponding element in selectors is **truthy**. Example: `list(compress(['a','b','c'],
[1,0,1]))` gives `['a','c']`. A fast way to filter one sequence using a parallel boolean mask.

**C118. What does `itertools.filterfalse()` do?**
`itertools.filterfalse(predicate, iterable)` returns elements for which the predicate is
**False** — the logical opposite of the built-in `filter()`. Example:
`list(filterfalse(lambda x: x % 2 == 0, range(10)))` returns the odd numbers. It avoids
writing a negated lambda inside `filter()`.

**C119. What does `functools.total_ordering` do?**
`@functools.total_ordering` is a **class decorator** that fills in the remaining rich
comparison methods (`__le__`, `__gt__`, `__ge__`) automatically once you define `__eq__` and
just one of `__lt__`/`__le__`/`__gt__`/`__ge__`. It reduces boilerplate for classes that need
full ordering support.

**C120. What is the `unittest` module used for?**
Python's built-in testing framework, based on the **xUnit** style. Tests are written as methods
on a class inheriting from `unittest.TestCase`, using assertions like `assertEqual` and
`assertRaises`. Tests are grouped and run via `unittest.main()` or a test runner, with
`setUp`/`tearDown` for fixtures.

### C121–C130: Testing, profiling & the filesystem

**C121. What is pytest and how does it differ from unittest?**
pytest is a popular third-party testing framework that allows **plain functions** (not
classes) as test cases, uses the built-in `assert` statement instead of special assertion
methods, and provides powerful **fixtures** via the `@pytest.fixture` decorator. It can also
discover and run unittest-style tests, making migration easy.

**C122. What is `unittest.mock` used for?**
Provides `Mock` and `MagicMock` objects that simulate the behavior of real objects, plus the
`patch()` function/decorator to temporarily replace real objects with mocks during a test.
It's used to **isolate the code under test** from external dependencies like databases, APIs
or the filesystem.

**C123. What is the doctest module?**
`doctest` scans **docstrings** for text that looks like an interactive Python session (with
`>>>` prompts) and executes it, comparing the actual output to the expected output shown in
the docstring. It keeps small usage examples in sync with the code, doubling as both
documentation and a lightweight test.

**C124. What is the timeit module used for?**
Measures the execution time of **small code snippets** accurately by running them many times
and minimizing the effect of system noise. It can be used as a library (`timeit.timeit()`) or
from the command line (`python -m timeit`), and is the standard way to micro-benchmark
alternative implementations.

**C125. What is cProfile used for?**
Python's built-in **deterministic profiler**, reporting how much time is spent in each function
call across a program's execution. Run via `python -m cProfile script.py`, it outputs call
counts and cumulative time per function, helping identify real performance bottlenecks instead
of guessing.

**C126. What is code coverage and how is it measured in Python?**
Code coverage measures **what percentage of your source lines (or branches) were actually
executed** by your test suite. The `coverage.py` package (often used via `pytest-cov`)
instruments code during test runs and reports untested lines, helping identify gaps in test
suites — though 100% coverage doesn't guarantee correctness.

**C127. What is the subprocess module used for?**
Lets Python **spawn and interact with external processes** and shell commands.
`subprocess.run()` is the modern, recommended interface, returning a `CompletedProcess` with
stdout, stderr and return code. It replaces older, less safe alternatives like `os.system()`
and `os.popen()`.

**C128. What is the shutil module used for?**
Provides **high-level file operations** beyond what `os` offers: `shutil.copy()` and
`shutil.copytree()` copy files and directory trees, `shutil.move()` relocates files,
`shutil.rmtree()` recursively deletes a directory, and `shutil.disk_usage()` reports disk
space statistics.

**C129. What is the pathlib module?**
pathlib (Python 3.4+) provides an **object-oriented way to work with filesystem paths** via
the `Path` class, replacing much of `os.path`'s string-based API. Example: `Path('data') /
'file.txt'` joins paths with `/`, and methods like `.exists()`, `.read_text()` and `.glob()`
make common file operations more readable.

**C130. What is the glob module used for?**
`glob` finds filenames matching a **Unix shell-style wildcard pattern**, such as
`glob.glob('*.txt')` for all text files in the current directory. It supports `*` (any
characters), `?` (single character), and with `recursive=True` and `**` can search
directories recursively.

### C131–C140: Files, data formats, hashing & time

**C131. What is the tempfile module used for?**
Creates **temporary files and directories that are automatically cleaned up**.
`tempfile.NamedTemporaryFile()` creates a file with a real filesystem name, while
`TemporaryDirectory()` creates a self-deleting directory as a context manager — both useful
for scratch data that shouldn't persist after a script finishes.

**C132. What is the csv module used for?**
Reads and writes CSV (comma-separated values) files while correctly handling **quoting,
embedded commas and different delimiters**. `csv.reader()`/`csv.writer()` work with rows as
lists, while `csv.DictReader()`/`csv.DictWriter()` work with rows as dictionaries keyed by
column header.

**C133. What is the sqlite3 module used for?**
A built-in module providing a **lightweight, file-based SQL database with no separate server
process** required. `sqlite3.connect('file.db')` opens a connection, and `cursor.execute()`
runs SQL statements. Ideal for local storage, prototyping and small applications.

**C134. What is the hashlib module used for?**
Provides **cryptographic hash functions** like SHA-256 and MD5 for generating fixed-size
digests of data, commonly used for checksums, password hashing (with proper salting), and data
integrity verification. Example: `hashlib.sha256(data).hexdigest()` returns a hex string digest
of the input bytes.

**C135. What is the difference between the random and secrets modules?**
The `random` module generates **pseudo-random** numbers using a fast, deterministic algorithm
suitable for simulations and games, but it is **not cryptographically secure** and can be
predicted. The `secrets` module (Python 3.6+) generates cryptographically strong random values
and **should always be used for tokens, passwords and security-sensitive randomness**.

**C136. What is the uuid module used for?**
Generates **universally unique identifiers**. `uuid.uuid4()` creates a random 128-bit UUID with
a negligible chance of collision, while `uuid.uuid1()` incorporates the host's MAC address and
current time. UUIDs are commonly used as database primary keys or unique object identifiers
across distributed systems.

**C137. What is the datetime module used for?**
Provides classes for manipulating dates and times: `date`, `time`, `datetime` and `timedelta`.
`datetime.now()` gets the current local time, `strftime()`/`strptime()` format and parse date
strings, and `timedelta` objects support arithmetic like adding or subtracting durations from
a datetime.

**C138. What is the difference between the time and datetime modules?**
The `time` module works closer to the OS level with **Unix timestamps** (`time.time()`) and
simple sleep/measurement functions (`time.sleep()`, `time.perf_counter()`). The `datetime`
module offers **richer, higher-level** date and time objects with calendar-aware arithmetic,
formatting and time zone support, making it preferred for most application-level date logic.

**C139. What is the zoneinfo module?**
`zoneinfo` (Python 3.9+) provides **IANA time zone support built into the standard library**,
replacing the need for the third-party `pytz` package in most cases. Example:
`datetime.now(ZoneInfo('Asia/Kolkata'))` attaches a specific time zone to a datetime object,
correctly accounting for daylight saving rules.

**C140. What is the argparse module used for?**
Builds **command-line interfaces** by declaring expected arguments and options.
`parser.add_argument()` defines a flag or positional argument, and `parser.parse_args()` parses
`sys.argv` into a namespace object. It automatically generates `--help` text and handles type
conversion and error messages for invalid input.

### C141–C150: Config, packaging & the import system

**C141. What is the configparser module used for?**
Reads and writes **INI-style configuration files** with `[section]` headers and `key = value`
pairs. `config.read('file.ini')` loads a file, and `config['section']['key']` retrieves a
value. Commonly used for application settings that should be editable without touching source
code.

**C142. What is the difference between venv, virtualenv and conda?**
`venv` is Python's **built-in, lightweight** tool for creating isolated environments using the
same interpreter version as the system Python. `virtualenv` is a more feature-rich third-party
predecessor that also supports older Python versions. `conda` is a **separate package and
environment manager** that can install non-Python dependencies and different Python versions
entirely.

**C143. What is a requirements.txt file used for?**
Lists a project's Python package dependencies, typically with **pinned versions** (e.g.
`requests==2.31.0`), so they can be installed reproducibly with `pip install -r
requirements.txt`. A simple, widely supported way to share and lock down a project's dependency
set.

**C144. What is pyproject.toml used for?**
`pyproject.toml` (PEP 518/621) is the **modern, standardized configuration file** for Python
projects, specifying build system requirements and project metadata (name, version,
dependencies) in one place. It's replacing the older `setup.py`/`setup.cfg` approach and is used
by tools like Poetry, Hatch and pip itself.

**C145. What is the difference between a wheel and an sdist?**
An **sdist** (source distribution) packages a project's raw source code, requiring a build step
on install. A **wheel** (`.whl`) is a **pre-built, ready-to-install binary distribution** format
that installs faster and doesn't require a compiler on the user's machine, making it the
preferred distribution format for PyPI packages.

**C146. What is PYTHONPATH and how does Python find modules?**
`PYTHONPATH` is an environment variable listing **extra directories Python searches** when
importing modules, in addition to the standard library and installed site-packages. Python's
module search order is: built-in modules, then directories in `sys.path`, which is initialized
from the script's directory, PYTHONPATH, and installation-dependent defaults.

**C147. What does `if __name__ == "__main__":` do?**
When a Python file is run directly, its `__name__` variable is set to `'__main__'`. When the
same file is **imported as a module** elsewhere, `__name__` is set to the module's name
instead. This guard lets a file define reusable functions/classes while only running certain
code (like a demo or CLI) when executed directly.

**C148. What is the difference between absolute and relative imports?**
An **absolute** import specifies the full path from the project's root package, e.g.
`from mypackage.utils import helper`. A **relative** import uses dots to reference modules
relative to the current module's location, e.g. `from .utils import helper` (same package) or
`from ..utils import helper` (parent package). **Relative imports only work inside a proper
package.**

**C149. What causes a circular import in Python, and how do you fix it?**
A circular import happens when module A imports module B, and module B (directly or indirectly)
imports module A back, causing an **incomplete module** to be referenced during initialization.
Fixes: restructure code to remove the mutual dependency, move the import inside a function
(deferred import), or merge the modules.

**C150. What does the `__all__` variable do in a module?**
`__all__` is a list of strings defined in a module that specifies **which names are exported
when a client does `from module import *`**. Names not listed in `__all__` are still accessible
via explicit import but are excluded from wildcard imports, signaling the module's intended
public API.

### C151–C160: Namespace packages, importlib & async primitives

**C151. What are namespace packages in Python?**
Namespace packages (PEP 420) allow a package's contents to be **split across multiple
directories without requiring an `__init__.py`** file in each one. Python automatically treats
a directory as a namespace package if no `__init__.py` is present, which is useful for large
projects or plugin systems distributed across multiple locations.

**C152. What is the importlib module used for?**
Provides a **programmatic interface** to Python's import system.
`importlib.import_module('name')` imports a module dynamically using a string name, useful when
the module to load isn't known until runtime. `importlib.reload(module)` re-executes a
previously imported module, useful in interactive development.

**C153. How does Python's `sys.modules` cache affect imports?**
`sys.modules` is a dictionary **caching every module that has already been imported** in the
current process, keyed by module name. Subsequent `import` statements for the same module reuse
the cached object instead of re-executing the module's code — which is why
`importlib.reload()` is needed to force re-execution.

**C154. What is the contextvars module used for?**
Provides **Context Variables** that hold values which are local to the current execution
context, correctly isolated across concurrently running asyncio tasks or threads. Unlike a plain
global variable, a `ContextVar` set inside one async task won't leak its value into a
differently-scheduled concurrent task.

**C155. What are `asyncio.Lock` and `asyncio.Semaphore` used for?**
`asyncio.Lock` ensures **only one coroutine at a time** can enter a critical section, acquired
and released with `async with lock:`. `asyncio.Semaphore` generalizes this to allow **up to N
concurrent coroutines** into a section, commonly used to cap concurrent network requests or
resource usage in async code.

**C156. What is `asyncio.Queue` used for?**
An **async-aware FIFO queue** used to pass data between producer and consumer coroutines
safely. `put()` and `get()` are coroutines that can be awaited, allowing consumers to block
(without blocking the event loop) until an item becomes available — implementing the
producer-consumer pattern asynchronously.

**C157. What is an async generator in Python?**
Defined with `async def` containing a `yield` statement, combining asynchronous operations with
lazy iteration. It's consumed with **`async for`** instead of a regular for loop, and is useful
for streaming data (e.g. paginated API results) where each item may require an awaited I/O call
to produce.

**C158. What is an async context manager?**
Implements `__aenter__` and `__aexit__` as **coroutines** instead of `__enter__`/`__exit__`, and
is used with `async with`. Used when acquiring or releasing a resource involves an async
operation, such as opening a database connection pool or an async HTTP session.

**C159. What does `async for` do, and how does it differ from a regular for loop?**
`async for` iterates over an **async iterator** — one that implements `__aiter__` and an async
`__anext__` method — **awaiting each next value** instead of retrieving it synchronously. Used
with async generators and other asynchronous data sources so the event loop isn't blocked while
waiting for the next item.

**C160. What is the `concurrent.futures` module used for?**
Provides a **high-level interface for running callables asynchronously** using a pool of
workers, via `ThreadPoolExecutor` or `ProcessPoolExecutor`. `executor.submit()` returns a
`Future` object representing the eventual result, and `executor.map()` applies a function across
an iterable concurrently, abstracting away manual thread/process management.

### C161–C170: Parallelism, pattern matching & exceptions

**C161. What is the difference between ThreadPoolExecutor and ProcessPoolExecutor?**
`ThreadPoolExecutor` runs tasks in a pool of **threads within the same process**, sharing memory
but still subject to the GIL — best for **I/O-bound** work. `ProcessPoolExecutor` runs tasks in
**separate processes** with independent memory, bypassing the GIL for true parallelism — best
for **CPU-bound** work, at the cost of inter-process communication overhead.

**C162. What is `multiprocessing.Manager` used for?**
`multiprocessing.Manager()` creates a **manager process** that hosts shared Python objects (like
dict, list, or custom proxies) accessible by multiple worker processes. Because separate
processes don't share memory by default, a Manager provides a coordinated way to share and
mutate state across process boundaries safely.

**C163. What limitation does pickling place on multiprocessing?**
Data passed between processes (arguments, return values, and objects sent via Queue/Pipe) must
be **picklable**, since processes communicate by serializing objects. **Lambdas, local
functions, and objects holding unpicklable resources** (like open file handles or database
connections) generally can't be passed directly to worker processes.

**C164. What does `os.fork()` do?**
`os.fork()` (Unix-only) creates a new **child process that is a near-exact copy** of the calling
process, both continuing execution from the point of the `fork()` call. The return value
distinguishes the two: **0 in the child, and the child's PID in the parent**. It's a low-level
primitive; `multiprocessing` is generally preferred for portability.

**C165. What is structural pattern matching (match/case) in Python?**
Introduced in Python 3.10 (PEP 634), `match subject: case pattern:` provides structural pattern
matching similar to switch statements in other languages, but **far more powerful** — it can
match sequence structure, mapping keys, class attributes, and **bind variables** from the
matched shape, with a wildcard `_` as a catch-all.

**C166. What are exception groups and `except*` in Python?**
Python 3.11 introduced **`ExceptionGroup`**, which bundles multiple unrelated exceptions
together (common when multiple concurrent tasks fail), and the **`except*`** syntax to
selectively handle specific exception types within that group without accidentally swallowing
the others. Especially relevant for `asyncio.TaskGroup`.

**C167. What is the tomllib module?**
`tomllib` (Python 3.11+) is a built-in module for **parsing TOML files (read-only)**, used
heavily for configuration such as `pyproject.toml`. `tomllib.load(file)` reads a binary-mode
file object and returns a dict of the parsed data; **writing TOML still requires a third-party
library.**

**C168. What is a custom exception class and why define one?**
A class that inherits from `Exception` (or a more specific built-in exception), letting you
represent **domain-specific error conditions**, e.g. `class InsufficientFundsError(Exception):
pass`. This allows calling code to catch precisely the errors it expects using `except
InsufficientFundsError`, rather than overly broad or generic exception types.

**C169. What is the full try/except/else/finally flow in Python?**
The **try** block holds code that might raise an exception. **except** catches and handles
matching exceptions. **else** runs **only if no exception occurred** in try. **finally** always
runs, whether or not an exception occurred, and is used for cleanup like closing files or
releasing locks, **even if the function returns early**.

**C170. How should multiple except clauses be ordered?**
Except clauses are checked **top to bottom**, and the first matching one runs — so **more
specific exception types must be listed before more general ones** (e.g. `except ValueError`
before `except Exception`), or the specific handler will never be reached because the general
one catches it first.

### C171–C180: Context managers, file I/O, encoding & expressions

**C171. How do you write a custom context manager without a class?**
Using `@contextlib.contextmanager`, you write a **generator function** where code before
`yield` runs as `__enter__` and code after `yield` (typically in a try/finally) runs as
`__exit__`. Yield the resource, then clean it up after the yield statement, letting the
function be used directly in a `with` block.

**C172. What is the difference between `contextlib.suppress()` and a try/except pass?**
`contextlib.suppress(SomeError)` is a context manager that **silently ignores a specified
exception type** if raised inside the `with` block, functioning like a one-line equivalent of
`try/except SomeError: pass`. It's more concise and explicitly communicates intent, but should
still be scoped narrowly to avoid hiding unrelated bugs.

**C173. What are the common file open modes in Python?**
`'r'` opens for reading (default), `'w'` **truncates** and opens for writing, `'a'` opens for
appending, and `'x'` opens for **exclusive creation** (fails if the file exists). Appending
`'b'` (e.g. `'rb'`) opens in binary mode, and `'+'` (e.g. `'r+'`) allows both reading and
writing on the same file object.

**C174. What is buffering in Python file I/O?**
Buffering **batches small reads/writes into larger chunks** to reduce the number of costly
system calls. `open(file, buffering=...)` lets you control this: **0** disables buffering
(binary mode only), **1** enables line buffering (text mode), and any larger integer sets a
fixed buffer size in bytes; the default picks a sensible size automatically.

**C175. What is the difference between `encode()` and `decode()` for strings?**
`encode()` converts a Python `str` (Unicode text) **into bytes** using a specified encoding like
UTF-8: `'café'.encode('utf-8')`. `decode()` does the reverse, converting bytes back into a
`str`: `b'caf\xc3\xa9'.decode('utf-8')`. Mismatched encodings cause `UnicodeDecodeError` or
garbled text.

**C176. What is Unicode normalization and why does it matter in Python?**
Some characters can be represented **multiple equivalent ways** in Unicode, e.g. an accented
letter as one composed code point or as a base letter plus a combining accent.
`unicodedata.normalize()` converts strings to a consistent form (**NFC, NFD, NFKC or NFKD**) so
that visually identical strings compare equal with `==`.

**C177. What does the `ascii()` function do?**
`ascii(obj)` returns a string representation of an object, like `repr()`, but **escapes any
non-ASCII characters** using `\x`, `\u` or `\U` escapes instead of printing them directly.
Useful for producing output that's guaranteed to be safely displayable in environments that
don't support full Unicode.

**C178. What is operator precedence in Python and why does it matter?**
Determines the order operations are evaluated in an expression without explicit parentheses,
e.g. multiplication binds tighter than addition, so `2 + 3 * 4` evaluates to **14, not 20**.
Python follows a documented precedence table; **when in doubt, adding parentheses makes
evaluation order explicit and readable**.

**C179. What is a ternary (conditional) expression in Python?**
Python's conditional expression has the form `value_if_true if condition else value_if_false`,
evaluated inline. Example: `status = 'even' if n % 2 == 0 else 'odd'`. A concise alternative to
a full if/else block when assigning a value based on a condition.

**C180. What is extended iterable unpacking in Python?**
PEP 3132 allows a **starred name to capture multiple elements** during unpacking:
`first, *middle, last = [1,2,3,4,5]` assigns `first=1`, `last=5`, and `middle=[2,3,4]` as a
list. Useful for splitting off the head and/or tail of a sequence without slicing manually.

### C181–C190: Assignment, introspection & class design

**C181. What is chained assignment in Python?**
Chained assignment, `a = b = c`, assigns the same value to multiple variables in one statement,
**evaluating the right-hand side once** and binding all names to that same object. For mutable
objects, this means all variables reference the identical object, so mutating one is visible
through the others.

**C182. How does Python support returning multiple values from a function?**
Python functions can only return a **single object**, but that object is typically a **tuple**,
which can then be unpacked at the call site: `def divmod2(a, b): return a // b, a % b`, then
`q, r = divmod2(7, 2)`. The parentheses around a tuple are optional when returning multiple
comma-separated values.

**C183. What is the difference between a docstring and a regular comment?**
A **docstring** is a string literal placed as the first statement in a module, function, class
or method, stored in the object's `__doc__` attribute and **retrievable at runtime** via
`help()` or introspection tools. A regular `#` comment is discarded by the parser and has no
runtime representation. PEP 257 defines docstring conventions.

**C184. What do the `help()` and `dir()` functions do?**
`help(obj)` displays an object's **docstring and signature information** in an interactive,
readable format. `dir(obj)` returns a **list of the names** (attributes and methods) available
on an object, useful for exploring an unfamiliar object interactively without consulting
external documentation.

**C185. What do the `vars()` function and `__dict__` attribute show?**
Most Python objects store their instance attributes in a dictionary accessible via
`obj.__dict__`. `vars(obj)` is a convenient shortcut that returns this same dictionary. Called
with no arguments inside a function, `vars()` returns the **local namespace**, equivalent to
`locals()`.

**C186. What is name mangling in Python?**
When an attribute name inside a class body starts with **two leading underscores** (and at most
one trailing underscore), e.g. `__value`, Python automatically rewrites it internally to
**`_ClassName__value`**. This makes accidental overriding by subclasses less likely, though the
attribute remains accessible if you know the mangled name.

**C187. What is the convention for private vs protected attributes in Python?**
Python has **no true access control keywords**; conventions signal intent instead. A **single
leading underscore** (`_value`) signals "internal use, not part of the public API" by convention
only. A **double leading underscore** (`__value`) triggers name mangling, making accidental
access from subclasses harder, though not truly private.

**C188. What is an abstract property in Python?**
Combining `@property` with `@abstractmethod` (from the `abc` module) declares that subclasses
**must provide a concrete implementation of a particular property**, not just a regular method.
This enforces that any concrete subclass exposes a specific attribute-like interface, while the
abstract base class itself cannot be instantiated.

**C189. What is a mixin class in Python?**
A **mixin** is a class designed to be combined with others via multiple inheritance to add a
specific piece of **reusable behavior**, without being meant to stand alone or represent a
complete concept on its own. Example: a `JSONSerializableMixin` adding a `to_json()` method to
any class that includes it.

**C190. What is the difference between composition and inheritance?**
**Inheritance** models an **"is-a"** relationship, where a subclass extends and specializes a
parent class. **Composition** models a **"has-a"** relationship, where an object contains and
delegates to other objects to achieve behavior. **Composition is often preferred for
flexibility**, since it avoids tight coupling to a rigid class hierarchy.

### C191–C200: Protocols, typing internals & async mastery

**C191. When would you use a Protocol instead of an ABC?**
An **ABC** (`abc.ABC`) requires **explicit inheritance** and is best when you control the class
hierarchy and want to enforce a contract via subclassing. A **Protocol** enables **structural
typing** — any object with matching methods satisfies it without inheriting anything — useful
for typing third-party or unrelated classes that already have the right shape.
`@runtime_checkable` enables `isinstance()` checks against a Protocol.

**C192. What are ParamSpec and Concatenate used for in typing?**
**ParamSpec** (PEP 612) captures an **entire parameter signature** (both positional and keyword
parameters) as a single type variable, primarily to correctly type generic decorators that
preserve the wrapped function's signature. **Concatenate** lets you prepend additional
parameters to a captured ParamSpec, useful for decorators that inject an extra argument.

**C193. How does the GIL interact with asyncio's concurrency model?**
asyncio achieves concurrency through a **single-threaded event loop** that cooperatively
switches between coroutines at `await` points, so **the GIL is largely irrelevant** to asyncio's
own execution model — there's only ever one thread running Python bytecode at a time regardless.
This makes asyncio well-suited for I/O-bound concurrency without needing to bypass the GIL at
all.

**C194. How do you cancel a running asyncio task?**
Calling `task.cancel()` requests cancellation by raising **`asyncio.CancelledError`** inside the
coroutine at its next suspension point (an `await`). The coroutine can catch `CancelledError` to
perform cleanup, but **should generally re-raise it**, since swallowing it silently can leave
the task's cancellation state ambiguous to the caller.

**C195. What is the difference between `asyncio.wait()` and `asyncio.gather()`?**
`asyncio.gather(*coros)` runs coroutines concurrently and **returns their results in order**
once all complete, propagating the first exception raised (with an option to return exceptions
instead). `asyncio.wait(tasks)` instead returns **two sets — done and pending** tasks — offering
more control over partial completion, timeouts and cancellation, but does not directly return
ordered results.

**C196. How do you set a timeout on an asyncio operation?**
`asyncio.wait_for(coro, timeout=seconds)` wraps a coroutine and raises `asyncio.TimeoutError` if
it doesn't complete within the given time, cancelling the underlying task. Python 3.11
introduced **`async with asyncio.timeout(seconds):`** as a more composable context-manager-based
alternative for applying timeouts to a block of async code.

**C197. What is `threading.local` used for?**
`threading.local()` creates an object whose **attributes are stored separately per thread**,
even though all threads reference the same object. Setting `local_data.value` in one thread
doesn't affect the value seen in another thread, making it useful for per-thread state like
database connections without manual dictionary-based lookups keyed by thread ID.

**C198. What does `slots=True` do on a Python dataclass?**
Passing `slots=True` to `@dataclass` (Python 3.10+) automatically generates a **`__slots__`
definition matching the dataclass's fields**, removing the per-instance `__dict__` and reducing
memory usage — the same benefit as manually defining `__slots__` on a regular class, without
having to write it by hand.

**C199. What is Python's free-threaded (no-GIL) build?**
Introduced experimentally under **PEP 703** starting with Python 3.13, the free-threaded build
**removes the Global Interpreter Lock**, allowing true multi-threaded parallel execution of
Python bytecode. It requires a special build flag (or `python3.13t`), may have single-threaded
performance overhead, and third-party C extensions need updates to be compatible with it.

**C200. What is the difference between a coroutine object and an asyncio Task?**
Calling an `async def` function **just creates a coroutine object** — it does nothing until
awaited or scheduled. `asyncio.create_task(coro)` wraps that coroutine in a **Task**, scheduling
it to start running concurrently on the event loop **right away**, rather than waiting for an
explicit `await` to begin its execution.

---

<a name="set-d"></a>
# SET D — OOP INTERVIEW PREPARATION

*From the Python OOP Interview Series (Navya Sri Kurapati) — the framing, traps and design
scenarios interviewers actually use.*

## D1. Core conceptual questions

**What is OOP?**
A programming paradigm that organizes code around **Objects** instead of functions and logic.
An Object is a real-world entity that has **state (data)** and **behavior (methods)**.

*Interviewers are really asking:* What real-world problem does OOP solve? How does it make our
code better? Why is Python a great language for OOP?

*Strong answer:* It models real-world entities. It makes code reusable, modular and easy to
maintain. It helps manage complexity. Python supports OOP in a simple and powerful way.

> **Tip:** Always relate OOP concepts to real-life examples. Say: *"It helps organize code like
> real-world things."* Focus on Objects, their state and behavior.

**What is the difference between a class and an object?**

| Aspect | Class | Object |
|---|---|---|
| Definition | Blueprint or template | Real-world instance |
| Exists in Memory | Once | Many times |
| Created Using | `class` keyword | Constructor (`__init__()`) |
| Example | `Car` | `my_car`, `your_car` |
| Memory Allocation | No memory for data | Has memory for data |
| Purpose | Defines structure | Uses structure |

> **Tip:** Class is the plan. Object is the product built using the plan. Multiple objects can
> be created from one class.

**What are `self` and `__init__()`?**
`self` refers to the current object instance; it lets you access attributes and methods inside
the class. `__init__()` is a special method (**constructor**) that runs automatically when an
object is created, used to initialize attributes.

**Explain each of the four pillars.**

| Pillar | One line | Memory trick |
|---|---|---|
| **Encapsulation** | Hide data, control access | Think **"Capsule"** — data inside, protected |
| **Inheritance** | Reuse code, build hierarchy (DRY) | Think **"Family Tree"** — child gets nature from parent |
| **Polymorphism** | Same interface, different behavior | Think **"Many Shapes, One Name"** |
| **Abstraction** | Hide complexity, show what's important | Think **"Remote Control"** — buttons, not circuits |

Remember: Encapsulation – Secure · Inheritance – Reuse · Polymorphism – Flexibility ·
Abstraction – Simplicity.

**Encapsulation follow-up:** *Is encapsulation about hiding data?*
> **Interview tip:** Encapsulation is **not** about hiding data completely. It's about hiding
> the **implementation details** and showing only what is necessary.

**Inheritance follow-up:** *When should you use inheritance?*
> Use inheritance when classes share common behavior. **Prefer composition over inheritance when
> possible** (flexibility). Always ask: IS-A relationship or NOT?

**Polymorphism follow-up:** *How is polymorphism achieved in Python?*
> Through **method overriding**. Python also uses **Duck Typing**: *"If it walks like a duck and
> quacks like a duck, it's a duck."* Focus on behavior, not the actual type.
>
> *Why is polymorphism useful in real projects?* It allows different components to work together
> seamlessly through a common interface.

**Abstraction follow-up:** *How do you spot an abstraction question?*
> Look for keywords like *interface*, *abstract*, *hide*, *implementation*, *essential*,
> *contract*. Abstraction is about **managing complexity by showing only the important part**.

## D2. The four interview traps

*Small details, big impact in interviews.*

### Trap 1 — `self` vs `cls`
`self` → instance (object) · `cls` → class

```python
class Counter:
    count = 0

    def __init__(self):
        self.value = 1

    def inc_instance(self):
        self.value += 1

    def inc_class(cls):
        cls.count += 1

c1 = Counter()
c2 = Counter()
c1.inc_instance()
c1.inc_class()
c2.inc_class()

# Output:
# c1.value       → 2
# c2.value       → 1
# Counter.count  → 2
```
`self` works on object data (each object has its own copy). `cls` works on class data (shared by
all objects).

> **Tip:** Use `self` for instance data, `cls` for shared data or alternate constructors.

### Trap 2 — `__init__()`, the constructor trap
`__init__()` runs automatically when an object is created.

```python
class Book:
    def __init__(self, title):
        self.title = title
        print("Book created!")

b = Book("Python OOP")
# Output: Book created!
print(b.title)
# Python OOP
```
- If `__init__()` is **missing** → object is **still created**.
- If **parameters are wrong** → **`TypeError`**.

> **Tip:** `__init__` is for **initialization**, not for **creating** new objects.

### Trap 3 — Method overriding
Child class provides its own implementation.

```python
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()
a.speak()    # Animal makes sound
d.speak()    # Dog barks
```
Child method overrides parent method. Method name same, behavior different.

> **Tip:** Override only when behavior **needs to change**, not just to reuse.

### Trap 4 — `_x` vs `__x` (single vs double underscore)
**Both are not the same!**

| `_x` (single underscore) | `__x` (double underscore) |
|---|---|
| Just a convention (weak private) | Name mangling (stronger private) |
| Can be accessed outside | Not directly accessible |
| Meant for "internal use" only | Access via `_ClassName__x` |

```python
class Demo:
    def __init__(self):
        self._x = 10

obj = Demo()
print(obj._x)      # 10
```
```python
class Demo:
    def __init__(self):
        self.__x = 10

obj = Demo()
print(obj.__x)          # ✗ AttributeError
print(obj._Demo__x)     # 10
```

> **Tip:** Use `_x` for internal use, `__x` when you want stronger data hiding.

### Quick recap
| Trap | Rule |
|---|---|
| self vs cls | `self` → object level; `cls` → class level |
| `__init__()` | Runs automatically. Initialize, don't create. |
| Overriding | Same method name, different behavior. |
| `_x` vs `__x` | `_x` → weak convention; `__x` → name mangling |

### Common mistakes
| ✗ Mistake | ✓ Fix |
|---|---|
| Using `self` in class methods | Always use `cls` — `@classmethod def create(cls): pass` |
| Forgetting `__init__` params → mismatch → `TypeError` | Match the signature |
| Overriding by mistake — changing behavior unintentionally | Check before overriding |
| Accessing `__x` directly → `AttributeError` | Use `_ClassName__x` |

> **Interview tip:** Interviewers love to test edge cases. Small mistakes in OOP concepts signal
> lack of clarity. Be confident with these details — they are high scoring.

## D3. Predict-the-output challenge

**Scenario: Animal and Dog classes.** Dog overrides `+` operator and uses `super()`.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} yrs)"

    def __add__(self, other):
        return Animal(self.name + other.name,
                      self.age + other.age)      # Default behavior

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)              # call super()
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.age} yrs) - {self.breed}"

    def __add__(self, other):
        # Override + to keep breed of the first dog
        new = super().__add__(other)             # uses Animal.__add__
        return Dog(new.name, new.age, self.breed)

# Test case
d1 = Dog("Buddy", 3, "Labrador")
d2 = Dog("Max", 2, "Beagle")
d3 = d1 + d2
print(d3)
```

**What to find:** What is printed? Which method is called? How does overriding and `super()`
work here?

**Think step by step:**
1. `d1 + d2` calls `Dog.__add__()`
2. Inside `Dog.__add__()` it calls `super().__add__(other)` → `Animal.__add__`
3. `Animal.__add__()` adds names and ages → Name: "BuddyMax", Age: 3 + 2 = 5
4. Back in `Dog.__add__()`: creates a new Dog with Name "BuddyMax", Age 5, Breed from d1 →
   "Labrador"

**Expected output:**
```
BuddyMax (5 yrs) - Labrador
```

**Key concepts tested:** Method Overriding (`__add__`) · `super()` to call parent behavior ·
Operator Overloading (`+`) · Inheritance (Dog is-a Animal)

> **Interview tip:** Always check if a child class overrides a method. Look for `super()` usage
> and why it's used. Understand how special methods (`__add__`, `__str__`, etc.) behave.
>
> **Remember:** OOP is all about behavior + relationships + real-world modeling!

## D4. OOP design scenarios (whiteboard questions)

*Practise these. Nail the interview.*

### Scenario 1 — Vehicle
**Design a system for different vehicles.**
*Requirements:* Create a base class `Vehicle`. Child classes `Car` and `Bike`. Each vehicle
should have `start()` and `stop()`. Override `start()` in child classes.

```python
class Vehicle:
    def start(self):
        pass
    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
```
**Example output:** Car started / Vehicle stopped / Bike started / Vehicle stopped
**Tests:** Inheritance, Method Overriding, Polymorphism

### Scenario 2 — Shape
**Design a system to calculate the area of different shapes.**
*Requirements:* Create a base class `Shape` having method `area()`. Create `Circle` and
`Rectangle` classes. Override `area()` in each class.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l, self.b = l, b
    def area(self):
        return self.l * self.b
```
**Example output:** Circle Area: 78.5 / Rectangle Area: 50
**Tests:** Abstraction, Method Overriding, Polymorphism

### Scenario 3 — Payment
**Design a payment system.**
*Requirements:* Create a base class `Payment` with method `pay(amount)`. Create `CreditCard`,
`UPI` and `Wallet` classes. Each class implements payment in its own way.

```python
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Wallet(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Wallet")
```
**Example output:** Paid 500 using Credit Card / Paid 500 using UPI / Paid 500 using Wallet
**Tests:** Polymorphism, Abstraction

### Scenario 4 — Database
**Design a simple database connection system.**
*Requirements:* Create a base class `Database` with `connect()` and `close()`. Create `MySQL`
and `MongoDB` classes. Implement connection in child classes.

```python
class Database:
    def connect(self):
        pass
    def close(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connecting to MySQL")
    def close(self):
        print("MySQL connection closed")

class MongoDB(Database):
    def connect(self):
        print("Connecting to MongoDB")
    def close(self):
        print("MongoDB connection closed")
```
**Example output:** Connecting to MySQL / MySQL connection closed / Connecting to MongoDB /
MongoDB connection closed
**Tests:** Inheritance, Method Overriding

### What interviewers look for
| Signal | The question behind it |
|---|---|
| **Clear OOP concepts** | Do you really understand the pillars? |
| **Right design** | Can you break the problem into classes? |
| **Clean code** | Is your code readable and maintainable? |
| **Real-world thinking** | Can you apply OOP to real scenarios? |
| **Confidence** | Can you explain your design clearly? |

> **Interview tip:** Think before you code. **Design comes first!** Use all 4 pillars when
> possible. Keep your code simple, clean and well-structured.
>
> **Bonus advice:** Practise these patterns until they feel natural. Solve similar problems in
> your own way. Confidence comes from consistent practice!

## D5. Full-system design questions

Interviewers often ask you to design a complete system using all four pillars. Two worked
examples appear in `PYTHON-LEARNING-NOTES.md` §55:
1. **Online shopping system** — Customer → Browse & Add to Cart → Cart → Payment → Order
   Delivered
2. **Food delivery app** — Customer → Place Order → Order → Delivery Partner → Order Delivered

Both use: **Encapsulation** (private order/payment data with controlled access),
**Inheritance** (`User` → `Customer`, `DeliveryPartner`), **Polymorphism** (`Payment.pay()`
implemented by `CardPayment`, `UPIPayment`), and **Abstraction** (`PaymentGateway` ABC hiding
gateway details).

> **Interview tip:** Real projects use all 4 pillars together. Always think: *How can I make my
> system safe, reusable, flexible and easy to maintain?* Don't use inheritance or abstraction if
> not needed.

### Interview golden rules
- ✅ Always prefer **composition**, then inheritance.
- ✅ Use **abstraction** to reduce complexity.
- ✅ **Polymorphism** makes code flexible.
- ✅ **Encapsulation** protects your data.
- ⭐ Write clean code, think like a designer!

> **Quick tip:** Explain with examples. Draw diagrams if needed. Keep it simple and clear!

---

<a name="rapid-fire"></a>
# RAPID-FIRE REVISION SHEET

The questions that appear most often. If you can answer all of these cold, you are ready.

### Language fundamentals
| Question | One-line answer |
|---|---|
| Interpreted or compiled? | Interpreted — executes line by line, no separate compile step |
| Statically or dynamically typed? | Dynamically typed — no explicit type declarations |
| Who created it and when? | Guido van Rossum, released 1991, named after Monty Python |
| What is PEP 8? | Python's official style guide |
| Python 2 vs 3? | Py3: print function, true division, Unicode default, f-strings, type hints, async/await. Py2 EOL Jan 2020 |
| `is` vs `==`? | `is` = identity (same object); `==` = value equality |
| `=` vs `==`? | `=` assigns; `==` compares |
| `/` vs `//`? | `/` true division → float; `//` floor division → rounds toward −∞ |
| What is `None`? | A singleton object representing absence of value. Compare with `is None` |
| What does `if __name__ == "__main__"` do? | Runs code only when the file is executed directly, not imported |

### Data structures
| Question | One-line answer |
|---|---|
| List vs Tuple? | List mutable `[]` slower; Tuple immutable `()` faster, hashable |
| List vs Dictionary? | List = ordered sequence by index; Dict = key-value pairs by key, keys hashable |
| Set vs Frozenset? | Set mutable; frozenset immutable + hashable → usable as dict key |
| What makes an object hashable? | Immutability — int, float, str, tuple, frozenset |
| `append()` vs `extend()`? | `append` adds one item; `extend` adds all items of an iterable |
| `del` vs `remove()` vs `pop()`? | `del`/`pop` by index (`pop` returns it); `remove` by value |
| Shallow vs deep copy? | `copy.copy()` shares nested refs; `copy.deepcopy()` copies recursively |
| Are dicts ordered? | Yes, since Python 3.7 (insertion order) |

### Functions
| Question | One-line answer |
|---|---|
| Parameters vs arguments? | Parameters in the definition; arguments are the values passed |
| `*args` vs `**kwargs`? | `*args` → tuple of positional; `**kwargs` → dict of keyword |
| What is a lambda? | Anonymous single-expression function |
| What is a closure? | Nested function that remembers enclosing-scope variables |
| What is a decorator? | Function that wraps another to extend behavior, applied with `@` |
| What is a generator? | Function using `yield` that returns a lazy iterator |
| Generator vs list comprehension? | `()` lazy, memory-efficient; `[]` builds the whole list |
| LEGB rule? | Local → Enclosing → Global → Built-in name lookup order |
| Pass by value or reference? | Everything is an object reference; mutables can be changed in place |
| Why is a mutable default argument dangerous? | Evaluated once at definition; state persists across calls |
| Iterator vs Iterable? | Iterable has `__iter__`; Iterator has `__iter__` + `__next__` |

### OOP
| Question | One-line answer |
|---|---|
| Four pillars? | Encapsulation, Inheritance, Polymorphism, Abstraction |
| Class vs object? | Class = blueprint; object = instance |
| What is `self`? | Reference to the current instance |
| What is `__init__`? | Constructor — initializes an already-created instance |
| `__new__` vs `__init__`? | `__new__` creates the instance (runs first); `__init__` initializes it |
| `@staticmethod` vs `@classmethod`? | static: no implicit first arg; class: receives `cls` |
| `_x` vs `__x`? | `_x` convention only; `__x` triggers name mangling to `_Class__x` |
| Class vs instance variable? | Class var shared by all instances; instance var unique per object |
| What is MRO? | Method Resolution Order via C3 linearization; `super()` follows it |
| What is duck typing? | Type matters less than the methods an object has |
| `__str__` vs `__repr__`? | `__str__` for users (print); `__repr__` unambiguous, for developers |
| Composition vs inheritance? | "has-a" vs "is-a"; prefer composition for flexibility |
| What is a metaclass? | A class whose instances are classes; default is `type` |
| `type()` vs `isinstance()`? | `type()` exact class; `isinstance()` respects subclasses (preferred) |

### Errors & resources
| Question | One-line answer |
|---|---|
| try/except/else/finally? | try runs; except handles; else runs if no error; finally always runs |
| Ordering of except clauses? | Specific before general, or the general one swallows everything |
| Syntax error vs exception? | Syntax error before execution; exception at runtime, catchable |
| What does `with` do? | Context management — calls `__enter__`/`__exit__`, guarantees cleanup |
| `assert` vs `raise`? | `assert` disabled by `-O`; never use for production validation |

### Performance & internals
| Question | One-line answer |
|---|---|
| What is the GIL? | Only one thread runs Python bytecode at a time |
| Threading vs multiprocessing? | Threads for I/O-bound; processes for CPU-bound (bypass GIL) |
| How does memory management work? | Private heap + memory manager; reference counting + cyclic GC |
| How does garbage collection work? | Reference counting, plus a generational collector for cycles |
| What is memoization? | Caching results — `@functools.lru_cache` / `@functools.cache` |
| What sorting algorithm does Python use? | Timsort, O(n log n) |
| `sorted()` vs `.sort()`? | `sorted()` returns a new list; `.sort()` sorts in place, returns None |
| Why does `0.1 + 0.2 != 0.3`? | IEEE 754 binary floats; use `decimal.Decimal` for money |
| How do you improve performance? | Right data structure, standard library, remove abstraction, right algorithm |

### Modules & packaging
| Question | One-line answer |
|---|---|
| Module vs package? | Module = one `.py` file; package = directory with `__init__.py` |
| What is pip / PyPI? | pip installs packages from the Python Package Index |
| What is a virtual environment? | Isolated interpreter + packages; `python -m venv env` |
| Absolute vs relative import? | Absolute: full path from root; relative: dots, only inside a package |
| What causes a circular import? | A imports B and B imports A; fix by restructuring or deferring the import |
| What does `__all__` do? | Defines what `from module import *` exports |

---

*Compiled from all interview material in `pythonoopsfolder`. Source files were read only and
left unmodified. Concepts are explained in the companion file `PYTHON-LEARNING-NOTES.md`.*
