---
title: PYTHON-LEARNING-NOTES
topic: python-data
source_type: my-notes
source_file: STUDYNOTEs/PYTHON-LEARNING-NOTES.md
---

# Python — Complete Beginner-to-Confident Notes

**A single, step-by-step study guide compiled from every file in `pythonoopsfolder`.**

Read this top to bottom. Each part builds on the one before it. Nothing here assumes you have programmed before. Code you can type and run is in `code blocks`; the `#` comments show what each line produces.

**Companion file:** interview questions live separately in `PYTHON-INTERVIEW-QUESTIONS.md`.

---

# TABLE OF CONTENTS

**PART 1 — GETTING STARTED**
1. What Python Is
2. History of Python
3. Features of Python
4. Where Python Is Used
5. Installing Python & VS Code
6. Your First Program
7. Comments
8. Indentation

**PART 2 — THE BASICS**
9. Variables
10. Identifiers & Naming Rules
11. Keywords
12. Data Types
13. Type Casting
14. Operators
15. Input & Output
16. String Formatting

**PART 3 — CONTROL FLOW**
17. if / elif / else
18. while Loop
19. range()
20. for Loop
21. break, continue, pass
22. Nested Loops

**PART 4 — DATA STRUCTURES**
23. Strings
24. String Methods
25. Lists
26. List Methods & Comprehension
27. Tuples
28. Sets
29. Dictionaries
30. Collections Compared
31. Nested Collections

**PART 5 — FUNCTIONS**
32. Defining Functions
33. Arguments
34. return
35. Docstrings
36. Scope
37. Lambda, map, filter, reduce
38. Pass by Reference

**PART 6 — ORGANIZING CODE**
39. Modules
40. Packages
41. pip & PyPI
42. Standard Library Tour

**PART 7 — FILES & ERRORS**
43. File Handling
44. Exception Handling

**PART 8 — OBJECT-ORIENTED PROGRAMMING**
45. Why OOP
46. Class vs Object
47. self and `__init__`
48. Encapsulation
49. Inheritance
50. Polymorphism
51. Abstraction
52. Operator Overloading
53. Class vs Instance Variables
54. Common OOP Traps
55. All Four Pillars in One System

**PART 9 — REFERENCE**
56. Command Reference Tables
57. 40 Essential One-Liners
58. Practice Exercises
59. Suggested Learning Path

---

# PART 1 — GETTING STARTED

## 1. What Python Is

Python is a **general-purpose, dynamic, high-level, interpreted** programming language.

Break that down, because each word matters:

- **General-purpose** — not limited to one job. Websites, data analysis, AI, automation,
  games, desktop apps all get built in Python.
- **High-level** — you write instructions close to English. You never manage memory
  addresses or CPU registers yourself.
- **Interpreted** — the Python interpreter reads your code **line by line and runs it
  immediately**. There is no separate "compile" step producing a machine-code file first.
  That is why development feels fast: edit, save, run.
- **Dynamically typed** — you never declare that a variable is an integer. Python works
  out the type from the value you assign.

It is designed to be simple and readable, which makes it an ideal first language, and it
supports **object-oriented programming**, which lets you build organized, reusable code.

### Interpreted vs Compiled

| Interpreted | Compiled |
|---|---|
| Executes line by line | Compiles the whole program first |
| No separate compilation step | Faster execution once built |
| Examples: Python, JavaScript | Examples: C, C++, Java |

## 2. History of Python

- **Created by:** Guido van Rossum
- **First released:** 1991
- **Named after:** *Monty Python's Flying Circus*, a British comedy show — Guido was a fan.
  It has nothing to do with snakes.
- **Designed to be:** simple, readable, easy to learn
- **Open source** and free to use
- Supports multiple programming paradigms

### Version timeline
| Version | Released |
|---|---|
| Python 1.0 | 1991 |
| Python 2.0 | 2000 |
| Python 3.0 | 2008 (major update, not backward compatible) |
| Python 3.x | Latest line, many features and improvements |
| Python 3.12 | One of the latest stable versions |

**Python 2 reached end-of-life in January 2020.** Always learn and write Python 3.

Used today by Google, YouTube, Instagram, Spotify, Netflix, and many more.

## 3. Features of Python

1. **Easy to learn and use** — simple syntax similar to English; perfect for beginners.
2. **Readable and clean syntax** — uses indentation (spaces) to define blocks of code
   instead of curly braces.
3. **Interpreted language** — executes code line by line at runtime.
4. **High-level language** — no worrying about complex details like memory management.
5. **Portable / cross-platform** — the same code runs on Windows, macOS and Linux.
6. **Extensive standard library** — a huge collection of built-in modules and functions;
   you can do a lot without installing anything extra.
7. **Open source** — anyone can use, modify and distribute it freely.
8. **Dynamic typing** — no explicit type declarations needed.
9. **Object-oriented support** — classes, objects and inheritance.
10. **Extensive third-party libraries** — a vast ecosystem (NumPy, Pandas, Django, …).
11. **Integration capabilities** — integrates with C, C++ and Java, so you can reuse
    existing codebases.
12. **Automatic memory management** — garbage collection is built in.
13. **Extensible and embeddable** — can be extended with other languages.
14. **Huge community support** — answers to almost any question already exist.

## 4. Where Python Is Used

| Domain | Detail |
|---|---|
| **Web development** | Frameworks like **Django** and **Flask** provide efficient tools and libraries to build dynamic websites and web applications. |
| **Data analysis & visualization** | **NumPy**, **Pandas**, **Matplotlib** let professionals process, manipulate and visualize data precisely. |
| **Machine learning & AI** | Python is the go-to language. **TensorFlow**, **Keras**, **scikit-learn** provide tools for implementing complex algorithms and training models. |
| **Automation & scripting** | Easy-to-read syntax and rapid development cycle make it ideal for automating repetitive tasks and scraping. |
| **Cybersecurity** | Tooling and scripting. |
| **Desktop GUI applications** | Tkinter, PyQt and others. |
| **Game development** | Pygame and similar. |

## 5. Installing Python & Setting Up VS Code

### A. Installing Python

**Windows**
1. Go to the official website: **www.python.org/downloads**
2. Click the **Download** button; choose the latest version for Windows.
   (On the "Python Releases for Windows" page, pick the *Windows x86-64 executable
   installer* for 64-bit, or *Windows x86 executable installer* for 32-bit.)
3. Run the installer file.
4. **IMPORTANT:** tick the box **"Add Python to PATH"** *before* clicking **Install Now**.
   Skipping this is the single most common beginner setup problem — without it your
   terminal will not find the `python` command.
5. After installation, click **Close**.

**Linux (Ubuntu)**
1. Open the **Ubuntu Software Center**.
2. From the *All Software* dropdown, locate the entry for **Python 3.x** and double-click it.
3. Click **Install** to begin the installation.
4. Once complete, close the Software Center.

### B. Installing VS Code
1. Go to **code.visualstudio.com**
2. Click **Download for Windows**
3. Run the installer and follow the steps
4. Open VS Code when done

### C. Verify the installation
Open Command Prompt / Terminal and type:

```bash
python --version
```

You should see something like `Python 3.12.2`. On macOS/Linux you may need `python3 --version`.

### D. Run Python inside VS Code
1. Open VS Code
2. Click **Extensions** (Ctrl + Shift + X)
3. Search for **"Python"** and install the extension by Microsoft
4. You are ready to write and run Python programs

> **Note:** keep Python and VS Code updated for new features and better performance.

### Other ways to run Python code
- **Python IDLE** — the editor that ships with Python
- **Terminal / Command Prompt (REPL)** — type `python` and get an interactive prompt
- **Code editors** — VS Code, PyCharm
- **Jupyter Notebook / Google Colab** — great for data work

## 6. Your First Python Program

Every journey has a starting point. In programming that point is "Hello, World!".

### 1. Writing the program
Open VS Code and create a new file called `hello.py`:

```python
# This is our first Python program
print("Hello, World!")
```

### 2. Running the program
1. Save the file (Ctrl + S)
2. Click the **Run** ▶ button, or press **F5**
3. The output appears in the terminal:

```
PS C:\> python hello.py
Hello, World!
```

### 3. Explanation
- `print()` is a **built-in function** in Python.
- It is used to display output on the screen.
- `"Hello, World!"` is the **string** (text) we want to print. Strings are enclosed in
  quotes — single `' '` or double `" "` both work.
- The `#` symbol marks a **comment**. Comments are ignored by the interpreter and are
  used to explain the code to humans.

### 4. Key points
- Python is **case-sensitive** (`Print` is not `print`).
- Each statement is written on a new line.
- **No semicolon (`;`) is required** at the end of a line.
- **Indentation (spaces) is very important** in Python.
- Always save your file with a **`.py`** extension.

## 7. Comments

Comments provide explanatory notes inside code that are **not executed**. They improve
readability and leave reminders or explanations for other developers (including
future you). They have zero impact on the program's functionality or performance.

### Single-line comments
Start with a hash symbol `#` and continue until the end of the line. Anything written
after `#` is ignored by the interpreter.

```python
# This is a single-line comment
x = 5   # Assigning a value to the variable x
```

### Multi-line comments (block comments)
Python has **no built-in syntax specifically for multi-line comments**. You achieve the
effect with **triple quotes** (single or double) creating a string that is not assigned
to any variable — since it is not used elsewhere, it acts as a comment.

```python
"""
This is a multi-line comment.
It can span across multiple lines.
"""
print("Comments make code readable")
```

Good comments explain the **hows and whys**, not the *what* — the code itself should
already say what it does.

## 8. Indentation Rules

This is the feature that surprises people coming from other languages.

- Python uses **indentation (spaces)** instead of `{ }` to define blocks of code.
- **Standard indentation = 4 spaces.**
- Incorrect indentation raises an **`IndentationError`**.

```python
if True:
    print("Correctly indented")   # works fine
print("This runs after the if block")
```

All statements indented by the same number of spaces after a construct are considered
part of a **single block of code**. Indentation is not a style choice here — **it is
syntax**.

---

# PART 2 — THE BASICS

## 9. Variables

A variable is a **container that stores a data value**. Think of it as a labelled box:
the label is the name, the contents are the value.

What makes Python distinctive is that you **do not need to explicitly declare the type**.
You simply assign a value using the `=` operator, and Python works out the type.

```python
name = "Yaanyesh"
```

Here `name` is the variable name and `"Yaanyesh"` is the value. Python automatically
determines that the type is a string.

Variables can hold different kinds of data — numbers, strings, lists, or more complex
objects — and you can change the value at any time:

```python
age = 25
age = 26        # updating the value of 'age'
```

You can perform operations on variables:

```python
x = 5
y = 3
z = x + y                     # z is 8

greeting = "Hello"
name = "John"
message = greeting + " " + name   # "Hello John"
```

Example set covering several types:

```python
name = "Abhi"          # String
age = 22               # Integer
height = 5.9           # Float
is_student = True      # Boolean
marks = None           # NoneType
```

Giving variables **meaningful names** makes code readable and understandable.

## 10. Identifiers & Naming Rules

An **identifier** is a name used to identify a variable, function, class, module, or any
other user-defined object.

**Rules:**
- **Valid characters:** letters (`a–z`, `A–Z`), digits (`0–9`) and underscores (`_`).
  Cannot contain spaces or special characters like `!`, `#`, `$`.
- **Must start with** a letter or an underscore — **not a digit**.
- **Case-sensitive:** `myvar`, `MyVar` and `MYVAR` are three different identifiers.
- **Reserved words (keywords)** cannot be used as identifiers — e.g. `if`, `while`, `def`.
- **Length:** any length, but use meaningful, descriptive names that are not excessively long.
- **Readability:** choose names that convey purpose or meaning.

**Valid identifiers**
```
my_variable
count
total_sum
PI
MyClass
```

**Invalid identifiers**
```
123abc         # starts with a digit
my-variable    # contains a hyphen
if             # reserved word
my var         # contains a space
```

## 11. Keywords

Keywords are **special reserved words** with predefined meanings in the language. They
cannot be used as variable names or identifiers.

Keywords are the building blocks that let you create conditional statements, loops,
functions and classes, handle errors, and control the flow of a program. For example
`if` checks a condition, `for` and `while` create loops, and `def` defines a function.

**The full list of Python keywords:**

```
False     await     else      import    pass
None      break     except    in        raise
True      class     finally   is        return
and       continue  for       lambda    try
as        def       from      nonlocal  while
assert    del       global    not       with
async     elif      if        or        yield
```

## 12. Data Types

Data types determine the nature of the data and the operations that can be performed on it.

### Built-in types at a glance

| Data Type | Description | Example | `type()` Output |
|---|---|---|---|
| `int` | Integer numbers | `10`, `-25`, `1000` | `<class 'int'>` |
| `float` | Decimal numbers | `10.5`, `-3.14`, `0.001` | `<class 'float'>` |
| `str` | Text / String | `"Hello"`, `'Python'` | `<class 'str'>` |
| `bool` | Boolean (True/False) | `True`, `False` | `<class 'bool'>` |
| `NoneType` | Special type (no value) | `None` | `<class 'NoneType'>` |
| `list` | Ordered, mutable sequence | `[1, 2, 3]` | `<class 'list'>` |
| `tuple` | Ordered, immutable sequence | `(1, 2, 3)` | `<class 'tuple'>` |
| `set` | Unordered unique collection | `{1, 2, 3}` | `<class 'set'>` |
| `dict` | Key-value pairs | `{"a": 1}` | `<class 'dict'>` |
| `complex` | Complex numbers | `3 + 4j` | `<class 'complex'>` |

### 1. Numeric types
- **Integers (`int`)** — whole numbers without a fractional part. `age = 25`
- **Floating-point numbers (`float`)** — numbers with decimal parts or fractions. `pi = 3.14`
- **Complex numbers (`complex`)** — have a real and an imaginary part, denoted with a
  `j` suffix on the imaginary part. `c = 3 + 4j`
- *(Python 2 also had `long` for very large integers; in Python 3, `int` handles
  arbitrarily large numbers.)*

### 2. Boolean
`bool` represents the truth values **`True`** or **`False`**. Used for logical
operations and conditions. `is_valid = True`

### 3. Sequence types
Sequences represent an ordered collection of elements.
- **Strings (`str`)** — sequences of characters enclosed in single or double quotes.
  `name = "John"`
- **Lists (`list`)** — ordered sequences of elements enclosed in square brackets. Each
  element can be any data type. `numbers = [1, 2, 3, 4]`
- **Tuples (`tuple`)** — similar to lists but **immutable**: elements cannot be changed
  once defined. Enclosed in parentheses. `coordinates = (3, 4)`
- **bytes** — an immutable sequence of integers in the range 0–255.
- **bytearray** — like bytes, but mutable.

### 4. Sets
`set` is an **unordered collection of unique elements** enclosed in curly braces. Useful
for mathematical operations such as union, intersection and difference.

```python
fruits = {"apple", "banana", "orange"}
```

`frozenset` is the immutable version of a set.

### 5. Mappings
`dict` (dictionary) stores **key-value pairs** enclosed in curly braces. Each value is
associated with a unique key, allowing efficient lookup and retrieval.

```python
person = {"name": "John", "age": 25, "city": "New York"}
```

### Checking a type
```python
type(name)          # <class 'str'>
type(age)           # <class 'int'>
type(height)        # <class 'float'>
type(is_student)    # <class 'bool'>
type(marks)         # <class 'NoneType'>
```

## 13. Type Casting

Type casting means **converting one data type into another**, either automatically
(implicit) or manually (explicit).

### Implicit type conversion
Done automatically by Python, when there is no risk of losing data:

```python
a = 5          # int
b = 2.5        # float
c = a + b      # Python converts 'a' to float automatically
print(c)         # 7.5
print(type(c))   # <class 'float'>
```

### Explicit type conversion
Done manually using built-in functions:

| Function | Converts To | Example |
|---|---|---|
| `int()` | Integer | `int("10")` → `10` |
| `float()` | Float | `float("3.5")` → `3.5` |
| `str()` | String | `str(25)` → `'25'` |
| `bool()` | Boolean | `bool(0)` → `False` |
| `list()` | List | `list((1,2,3))` → `[1, 2, 3]` |
| `tuple()` | Tuple | `tuple([1,2,3])` → `(1, 2, 3)` |
| `set()` | Set | `set([1,1,2])` → `{1, 2}` |
| `dict()` | Dictionary | `dict([("a",1)])` → `{'a': 1}` |

```python
num_str = "100"
num_int = int(num_str)          # 100    (str -> int)
num_float = float(num_int)      # 100.0  (int -> float)
back_str = str(num_float)       # '100.0' (float -> str)
```

Worked example:
```python
x = "10"
y = int(x)
z = float(y)
print(x, type(x))   # 10 <class 'str'>
print(y, type(y))   # 10 <class 'int'>
print(z, type(z))   # 10.0 <class 'float'>
```

> **Watch out!** `int("abc")` raises a **`ValueError`** — only numeric strings can be
> converted to `int` or `float`.

## 14. Operators

### Arithmetic operators

| Operator | Meaning | Example (a=10, b=3) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | Division (always returns a **float**) | `a / b` | `3.333…` |
| `//` | Floor division (returns whole number) | `a // b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `1` |
| `**` | Exponent (power) | `a ** b` | `1000` |

More on `//` — floor division rounds **down**, toward negative infinity:
```python
10 // 4     #  2
-10 // 4    # -3   (not -2!)
```

More on `%` — the modulus returns the remainder after division:
```python
print(10 % 3)    # 1
print(25 % 4)    # 1
print(-10 % 3)   # 2  (in Python the remainder is always non-negative here)
```

### Comparison operators
| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### `=` vs `==` — a classic confusion
- `=` is the **assignment** operator (stores a value)
- `==` is the **comparison** operator (asks "are these equal?")

```python
x = 10              # assignment (stores value)
y = 10              # assignment
print(x == y)       # True   (comparison)
print(x = y)        # ✗ SyntaxError
```

### Logical operators
| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True if **both** are True | `True and False` | `False` |
| `or` | True if **any one** is True | `True or False` | `True` |
| `not` | Reverses the result | `not True` | `False` |

```python
if has_high_income and has_good_credit:
    ...
if has_high_income or has_good_credit:
    ...
is_day = True
is_night = not is_day
```

### Assignment operators
Augmented assignment is shorthand: `x = x + 10` becomes `x += 10`.

```python
x = 5
x += 3    # x = x + 3  ->  8
x -= 2    # x = x - 2  ->  6
x *= 4    # x = x * 4  -> 24
x //= 5   # x = x // 5 ->  4
```

### Membership & identity operators
| Operator | Checks | Example |
|---|---|---|
| `in` | Value exists in sequence | `'a' in 'apple'` → `True` |
| `not in` | Value doesn't exist | `5 not in [1,2,3]` → `True` |
| `is` | Same object in memory | `a is b` |
| `is not` | Different objects | `a is not b` |

```python
contains = 'Python' in course
```

### Bitwise operators
These work on integers at the binary level:

| Operator | Meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `^` | XOR |
| `~` | NOT (invert) |
| `<<` | Left shift |
| `>>` | Right shift |

```python
5 & 3      # 1     (0101 & 0011 = 0001)
```

### Operator precedence

Precedence determines the order operations are evaluated in without explicit parentheses.
Higher precedence is evaluated first.

**Order (high → low):**
1. `()` — Parentheses
2. `**` — Exponent
3. `+x`, `-x`, `~x` — Unary plus, minus, bitwise NOT
4. `*`, `/`, `//`, `%` — Multiplication, Division, Floor Division, Modulus
5. `+`, `-` — Addition, Subtraction
6. `<`, `<=`, `>`, `>=`, `!=`, `==` — Comparison
7. `not` — Logical NOT
8. `and` — Logical AND
9. `or` — Logical OR
10. `=`, `+=`, `-=`, `*=`, `/=` — Assignment operators

**Worked example:**
```
x = 2 + 3 * 4 ** 2
    Step 1: 4 ** 2  = 16
    Step 2: 3 * 16  = 48
    Step 3: 2 + 48  = 50
x = 50
```

Note `2 + 3 * 4` is `14`, not `20`. **When in doubt, add parentheses** — explicit
evaluation order is more readable anyway.

## 15. Input & Output

### The `print()` function
`print()` displays output to the console. It can take multiple values, separated by `sep`
and ended with `end`.

```python
print("Hello", "World")               # Hello World
print("A", "B", "C", sep="-")         # A-B-C
print("Loading", end="...")           # no newline after this
```

### The `input()` function
- Used to take input from the user.
- **`input()` always returns a string**, even when the user types numbers. This trips up
  everyone once. Convert explicitly.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))     # cast to int
print("Hello", name, "- you are", age, "years old")
```

```python
birth_year = int(input('Birth year: '))
```

## 16. String Formatting

| Method | Example |
|---|---|
| **f-string (best)** | `f"My name is {name}"` |
| `.format()` | `"My name is {}".format(name)` |
| `%` operator (old) | `"My name is %s" % name` |

```python
name = "Abhi"
age = 22
print(f"Hi, I am {name} and I am {age} years old")
# Output: Hi, I am Abhi and I am 22 years old
```

**Pro tip:** f-strings can do maths inline: `f"Total = {5 + 3}"` → `'Total = 8'`

---

# PART 3 — CONTROL FLOW

## 17. Conditional Statements: if / elif / else

Conditional statements let a program **make decisions** and run different blocks of code
based on whether a condition is `True` or `False`.

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: B
```

**Remember:** Python checks conditions **top to bottom and stops at the first `True`
block** — the remaining `elif`/`else` branches are skipped.

Simple example:
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible.")
```

Another form:
```python
if is_hot:
    print("hot day")
elif is_cold:
    print("cold day")
else:
    print("beautiful day")
```

### Nested if statements
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry denied")
```

### Shorthand / ternary if
```python
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)   # Odd
```

Form: `value_if_true if condition else value_if_false`

## 18. The while Loop

A **loop** repeats a block of code multiple times, instead of writing it again and again.

`while` executes a block of statements repeatedly **until a given condition is no longer
satisfied**. When the condition becomes false, the line immediately after the loop is
executed.

**Syntax**
```
while expression:
    statement(s)
```

**Flowchart**
```
        Enter while loop
               ↓
      ┌─────────────────┐  False
      │ Test expression │────────→ Exits while loop
      └─────────────────┘
               ↓ True
        ┌────────────┐
        │ Statements │
        └────────────┘
               ↑___________|
```

`while` falls under the category of **indefinite iteration** — the number of times the
loop executes isn't specified explicitly in advance. Use it when you don't know the exact
number of iterations ahead of time.

**Example 1**
```python
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

# Output:
# Hello Geek
# Hello Geek
# Hello Geek
```

**Example 2 — looping over a list until it is empty**
```python
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# Output: 4 3 2 1
```

**Example 3 — single-statement while block**
Just like the `if` block, if the `while` block consists of a single statement you can
declare the entire loop on a single line. Multiple statements in the body can be
separated by semicolons (`;`).

```python
count = 0
while (count < 5): count += 1; print("Hello Geek")
```

**Standard counting example**
```python
count = 1
while count <= 5:
    print(count)
    count += 1        # important! avoids infinite loop
```

> **⚠ Danger!** Forgetting to update the loop variable creates an **INFINITE LOOP**.
> Always make sure the condition eventually becomes `False`.

## 19. range()

The `range()` function returns a **sequence of numbers** in a given range. Its most
common use is to iterate over a sequence of numbers using Python loops.

**Syntax:** `range(start, stop, step)`

| Syntax | Meaning | Example |
|---|---|---|
| `range(stop)` | 0 to stop−1 | `range(5)` → 0,1,2,3,4 |
| `range(start, stop)` | start to stop−1 | `range(2,6)` → 2,3,4,5 |
| `range(start, stop, step)` | with step size | `range(0,10,2)` → 0,2,4,6,8 |

`range()` can be initialised in **3 ways**:

**a) `range(stop)`** — one argument. You get a series of numbers that starts at 0 and
includes every whole number up to, **but not including**, the stop number.

```python
for i in range(6):
    print(i, end=" ")
# Output: 0 1 2 3 4 5
```

```
| 0 | 1 | 2 | 3 | 4 | 5 |   | 6 |
 ←────── Output ──────→     ↑ Stop (excluded)
```

**b) `range(start, stop)`** — two arguments. You decide not only where the series stops
but also where it starts, so you don't have to start at 0 every time.

```python
# printing natural numbers from 5 to 19
for i in range(5, 20):
    print(i, end=" ")
# Output: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

**c) `range(start, stop, step)`** — three arguments. You choose where the series starts
and stops, and **how big the difference is between one number and the next**. If you
don't provide the step, `range()` behaves as if the step is 1.

```python
for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8
```

```
Start                          stop
  ↓                              ↓
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  └2 step┘         ↓
            | 0 | 2 | 4 | 6 | 8 |
             ←─── Output ────→
```

Standard usage:
```python
for i in range(1, 6):
    print(i, end=" ")
# Output: 1 2 3 4 5
```

## 20. The for Loop

`for` is used for **sequential traversal** — iterating over an *iterable* like a String,
Tuple, List, Set or Dictionary.

In Python there is **no C-style for loop** (`for (i=0; i<n; i++)`). There is a `for` loop
which is similar to the *for-each* loop in other languages.

> **NOTE:** In Python, `for` loops only implement **collection-based iteration**.

**Syntax**
```
for var in iterable:
    # statements
```

**Flowchart**
```
      For each item in sequence
                ↓
      ┌──────────────────┐  True
      │ Last item        │────────→ Exit For loop
      │ reached?         │
      └──────────────────┘
                ↓ False
         ┌────────────┐
         │ Statements │
         └────────────┘
                ↑__________|
```

Here the iterable is a collection of objects like lists or tuples. The indented statements
inside the for loop are executed **once for each item** in an iterable. The variable `var`
takes the value of the next item of the iterable each time through the loop.

**Iterating over a list**
```python
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Output:
# geeks
# for
# geeks
```

```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# mango
```

**Iterating over a string**
```python
for ch in "Python":
    print(ch)
```

**Iterating over a dictionary**
```python
# iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

# Output:
# Dictionary Iteration
# xyz 123
# abc 345
```

Cleaner, modern style using `.items()`:
```python
student = {"name": "Abhi", "age": 22}
for key, value in student.items():
    print(key, "->", value)
```

### for vs while — when to use which

| for Loop | while Loop |
|---|---|
| Used with a **sequence** | Used with a **condition** |
| Number of iterations is **known** | Number of iterations is **unknown** |
| Example: iterate over list, string, range | Example: user input, condition-based tasks |

## 21. break, continue, and pass

### break
`break` brings the control **out of the loop** when some external condition is triggered.
The break statement is put inside the loop body (generally after an `if` condition). It
terminates the current loop — the loop in which it appears — and resumes execution at the
next statement immediately after the end of that loop.

**If the break statement is inside a nested loop, break terminates the innermost loop.**

```
              ↓
      ┌──────────────────┐ False
      │ Loop test        │────────────┐
      │ expression       │            │
      └──────────────────┘            │
              ↓ True                  │
      ┌──────────────┐  Yes           │
      │    Break     │────────────────┤
      └──────────────┘                ↓
              ↓ No                Exit loop
    ┌────────────────────────┐        ↑
    │ Remaining body of loop │────────┘
    └────────────────────────┘
```

**Example 1**
```python
for i in range(10):
    print(i)
    if i == 2:
        break

# Output:
# 0
# 1
# 2
```

**Example 2 — break in both loop types**
```python
s = 'geeksforgeeks'

# Using for loop
for letter in s:
    print(letter)
    # break the loop as soon as it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break
print("Out of for loop")
print()

i = 0
# Using while loop
while True:
    print(s[i])
    # break the loop as soon as it sees 'e' or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1
print("Out of while loop")

# Output:
# g
# e
# Out of for loop
#
# g
# e
# Out of while loop
```

Standard example:
```python
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# Output: 1 2 3 4
```

### continue
`continue` is a **loop control statement** that forces the loop to execute the next
iteration while **skipping the rest of the code inside the loop for the current iteration
only**.

When `continue` is executed, the code inside the loop following the continue statement is
skipped for the current iteration and the next iteration of the loop begins.

**Syntax**
```
while True:
    .....
    if x == 10:
        continue
    print(x)
```

**Flowchart**
```
      ┌──────────────────┐
      │ Loop test        │←────────────┐
      │ expression       │             │
      └──────────────────┘             │
              ↓                        │
      ┌──────────────────┐  True       │
      │ Condition to     │──→ Continue─┤
      │ continue next    │             │
      │ iteration        │             │
      └──────────────────┘             │
              ↓ False                  │
   ┌──────────────────────────────┐    │
   │ Execute the remaining        │────┘
   │ part of loop                 │
   └──────────────────────────────┘
```

**Example 1**
```python
for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)

# Output: G k s f o r g k s  (each on its own line — all 'e's skipped)
```
*Explanation: we are skipping the print of character 'e' using if-condition checking and
the continue statement.*

**Example 2** — print numbers 1 to 10, but not 6.
```python
# loop from 1 to 10
for i in range(1, 11):
    # if i is equal to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value of i
        print(i, end=" ")

# Output: 1 2 3 4 5 7 8 9 10
```

> **NOTE:** The continue statement can be used with any other loop as well, like the
> "while loop", similarly as it is used with the "for loop" above.

Standard example:
```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5
```

### pass
`pass` is a **null operation** — it does nothing. It is a placeholder used when a
statement is syntactically required but no action is needed.

**Use cases:**
1. **Syntax purpose**
   ```python
   while True:
       pass    # Wait till user input is received
   ```
2. **Minimal class**
   ```python
   class MyMinimalClass:
       pass
   ```
3. **Placeholder for TODO work**
   ```python
   def initialization():
       pass    # TODO
   ```

```python
for num in range(5):
    if num == 2:
        pass   # TODO: handle this later
    print(num)
```

### break vs continue vs pass — summary
- **`break`** exits the current loop entirely, skipping remaining iterations.
- **`continue`** skips the rest of the current iteration and moves to the next one.
- **`pass`** does nothing — a syntactic placeholder that allows an empty body without a
  syntax error.

## 22. Nested Loops

With `for` and `while` loops you can create **nested loops** — loops inside a loop. For
example a while loop inside a for loop, or a for loop inside a for loop.

**Syntax**
```
Outer-loop Expression:
    Inner-loop Expression:
        Statement inside inner-loop
    Statement inside Outer-loop
```

**Example 1**
```python
x = [1, 2]
y = [4, 5]
for i in x:
    for j in y:
        print(i, j)

# Output:
# 1 4
# 1 5
# 2 4
# 2 5
```

**Example 2 — multiplication table**
```python
# Multiplication Table
# Running outer loop from 2 to 3
for i in range(2, 4):
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
        # Printing inside the inner loop
        print(i, "*", j, "=", i * j)
    # Printing inside the outer loop
    print()

# Output:
# 2 * 1 = 2 ......... 2 * 10 = 20
# 3 * 1 = 3 ......... 3 * 10 = 30
```

**Example 3 — for loop with a nested while loop**
```python
# Initialize list1 and list2 with some strings
list1 = ['I am', 'You are']
list2 = ['healthy', 'fine', 'geek']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to iterate through list1
for item in list1:
    # Printing outside inner loop
    print("start outer for loop")
    # initialize counter i with 0
    i = 0
    # Running inner while loop to iterate through list2
    while (i < list2_size):
        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i + 1
    # printing outside inner loop
    print("end for loop")

# Output:
# start outer for loop
# I am healthy
# I am fine
# I am geek
# end for loop
# start outer for loop
# You are healthy
# You are fine
# You are geek
# end for loop
```
*Explanation: we initialise two lists with some strings, store the size of list2 in
`list2_size` using `len()` and use it in the while loop as a counter. Then we run an outer
for loop to iterate over list1, and inside that an inner while loop to iterate over list2
using list indexing, printing each value of list2 for every value of list1.*

Simple nested for:
```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
# (1,1) (1,2) (2,1) (2,2)
```

Nested loops are useful for working with **multi-dimensional data**.

---

# PART 4 — DATA STRUCTURES

## 23. Strings

A string is a **sequence of characters** enclosed in single, double or triple quotes.
Strings are **arrays of bytes representing Unicode characters**.

**Strings are immutable in Python** — this is important and comes up constantly.

```python
s1 = 'Hello'
s2 = "World"
s3 = """Multi-line
string"""
```

### String indexing
Each character has a position (index), starting from **0**. **Negative indexes count from
the end**, with `-1` being the last character.

```python
s = "PYTHON"
#     P Y T H O N
#     0 1 2 3 4 5
#    -6 -5 -4 -3 -2 -1

s[0]        # "P"
s[-1]       # "N"
```

```python
String1 = "GeeksForGeeks"
print("First character of String is:")
print(String1[0])          # G

print("\nLast character of String is:")
print(String1[-1])         # s
```

### Reversing a string
```python
gfg = "geeksforgeeks"
print(gfg[::-1])
# Output: skeegrofskeeg
```

### String slicing
To access a **range of characters** in a string, use slicing with the slicing operator
(colon).

```python
s = "PYTHON"
s[1:4]     # 'YTH'    (index 1 to 3)
s[:3]      # 'PYT'    (start to index 2)
s[3:]      # 'HON'    (index 3 to end)
s[::-1]    # 'NOHTYP' (reversed!)
```

```python
String1 = "GeeksForGeeks"
print("Initial String:")
print(String1)

print("\nSlicing characters for 3-12:")
print(String1[3:12])           # ksForGeek

print("\nSlicing characters between 3rd and 2nd last character:")
print(String1[3:-2])           # ksForGee
```

Rules:
- If you leave out the start index, **0** is assumed.
- If you leave out the end index, the **length of the string** is assumed.
- `start` is inclusive, `stop` is exclusive.

```python
name = "John"
name[1:3]    # 'oh'
name[:2]     # 'Jo'
name[3:]     # 'n'
```

### The chr() function
Returns a string from a Unicode code integer.
```python
print(chr(97))
# Output: a
```

### Escape sequencing
Printing a string with both single and double quotes in it causes a `SyntaxError`,
because the string already contains single and double quotes and hence cannot be printed
with either of these. To print such a string either **triple quotes** are used, or
**escape sequences** are used.

Common escape sequences: `\n` (newline), `\t` (tab), `\\` (backslash), `\'`, `\"`.

### String concatenation
The `+` operator can be used to add multiple strings together. However, the arguments
**must be strings**. Here the `+` operator combines the strings stored in `var1` and
`var2` and stores the result in `var3`.

> **NOTE: STRINGS ARE IMMUTABLE, THEREFORE, WHENEVER A STRING IS CONCATENATED, IT IS
> ASSIGNED TO A NEW VARIABLE.**

```python
first = "Py"
second = "thon"
full = first + second          # 'Python'
echo = "Ha" * 3                # 'HaHaHa'   (repetition)
```

> **Remember:** Strings are immutable — `s[0] = 'X'` raises a **`TypeError`**. You must
> create a new string instead.

### String length
```python
len("Python")       # 6
```

## 24. String Methods

There are 40+ string methods; these are the ones you will use daily.

### Case conversion
| Method | Example | Result |
|---|---|---|
| `.upper()` | `"abhi".upper()` | `'ABHI'` |
| `.lower()` | `"ABHI".lower()` | `'abhi'` |
| `.title()` | `"hello world".title()` | `'Hello World'` |
| `.capitalize()` | `"python".capitalize()` | `'Python'` |

From the handwritten notes:
- **`lower()`** — convert all uppercase characters in a string into lowercase.
- **`upper()`** — convert all lowercase characters in a string into uppercase.
- **`title()`** — convert string to title case.

### Searching & checking
| Method | Example | Result |
|---|---|---|
| `.find(x)` | `"hello".find("l")` | `2` (index) |
| `.count(x)` | `"hello".count("l")` | `2` |
| `.startswith(x)` | `"python".startswith("py")` | `True` |
| `.endswith(x)` | `"python".endswith("on")` | `True` |
| `.isdigit()` | `"123".isdigit()` | `True` |
| `.isalpha()` | `"abc".isalpha()` | `True` |

### index() method
Allows a user to find the index of the **first occurrence** of an existing substring
inside a given string.

**Syntax:** `string_obj.index(substring, begp, endp)`

**Parameters:**
- `substring` — the string to be searched for.
- `begp` (default: 0) — specifies the position from where the search has to be started.
- `endp` (default: length of string) — specifies the position where the search has to end.

**Return:** returns the 1st position of the substring found.
**Exception:** raises `ValueError` if the argument string is not found or the index is out
of range.

### rindex() method
Returns the **highest index** of the substring inside the string if the substring is
found. Otherwise it raises `ValueError`.

### find() method
Returns the **lowest index** or first occurrence of the substring if it is found in a
given string. **If it is not found, then it returns −1.**

**Syntax:** `str_obj.find(sub, start, end)` — where `sub` is the substring that needs to
be searched.

### startswith() and endswith()
```
startswith()  →  str.startswith(search_string, start, end)
endswith()    →  str.endswith(search_string, start, end)
```

### Cleaning & splitting
```python
s = "   Hello Python   "
s.strip()                       # 'Hello Python'  (removes outer spaces)
s.replace('Python', 'World')    # '   Hello World   '

names = "Amit,Bhavya,Chirag"
names.split(",")                # ["Amit", "Bhavya", "Chirag"]
",".join(["a", "b", "c"])       # "a,b,c"
```

- `split(sep)` splits a string into a list by separator (default: whitespace).
- `join(iterable)` joins strings with the calling string as separator.
- `strip()` removes leading and trailing whitespace (or specified characters);
  `lstrip()` and `rstrip()` strip from one side only.

### split() vs slicing
Both work on a String object.
- `split()` gives you the **list of words** from a String: `'a b c '.split()` → `['a','b','c']`
- **Slicing** gives you a **substring** — it returns another String: `'a b c'[2:3]` → `'b'`

### Concatenating strings — two ways
```python
# 1. the + operator
fname = "John"
lname = "Ray"
print(fname + lname)         # JohnRay

# 2. the join function
''.join(['John', 'Ray'])     # 'JohnRay'
```

## 25. Lists

Python lists are just like **dynamically sized arrays** declared in other languages
(C++'s vector, Java's ArrayList). In simple language, it is a **collection of things,
enclosed with `[ ]` and separated by commas**.

The list is a **sequence data type** used to store a collection of data. Tuples and
Strings are other types of sequence data types.

```python
Var = ["Geeks", "For", "Geeks"]
print(Var)
# Output: ['Geeks', 'For', 'Geeks']
```

Key characteristics:
- Lists need **not be homogeneous** always, which makes it the most powerful tool in
  Python. A single list may contain data types like Int, Str, as well as objects.
- Lists are **mutable**, and hence they can be altered even after their creation.
- Lists are **ordered** and **allow duplicate values**.

```python
fruits = ["apple", "banana", "mango"]
mixed = [1, "two", 3.0, True]
empty = []
```

### Creating a list
A list can be created by just placing the sequence inside square braces `[]`. Unlike
Sets, a list doesn't need a built-in function for its creation.

```python
List = []
print("Blank list:")
print(List)

List = [10, 20, 30]
print("\nList of numbers:")
print(List)

# Output:
# Blank list:
# []
# List of numbers:
# [10, 20, 30]
```

### Accessing elements
```python
List = ["Geeks", "For", "Geeks"]
print("Accessing a element:")
print(List[0])       # Geeks
print(List[2])       # Geeks
```

```python
fruits[0]              # 'apple'
fruits[-1]             # 'mango'   (negative indexing)
fruits[0:2]            # ['apple', 'banana']  (slicing)
```

### Getting the size of the list
```python
List1 = []
print(len(List1))          # 0
List2 = [1, 2, 3]
print(len(List2))          # 3
```

### Adding elements to a list

**Using `append()`**
- **Only 1 element can be added at a time**; for the addition of multiple elements with
  the `append()` method, loops are used.
- **Tuples can be added to the list** with the use of the append method because tuples are
  immutable.

```python
List = []
print("Initial blank List:")
print(List)

List.append(1)
List.append(2)
List.append(4)
print("\nList After Addition of three elements:")
print(List)

for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3:")
print(List)

List.append((5, 6))
print("\nList after Addition of a Tuple:")
print(List)

List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List:")
print(List)

# Output:
# Initial blank List:
# []
# List After Addition of Three elements:
# [1, 2, 4]
# List after Addition of elements from 1-3:
# [1, 2, 4, 1, 2, 3]
# List after Addition of a Tuple:
# [1, 2, 4, 1, 2, 3, (5, 6)]
# List after Addition of a List:
# [1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
```

**Using `insert()`** — inserts a given element at a given index in a List.

**Syntax:** `list_name.insert(index, element)`
- `index` — at which the element has to be inserted.
- `element` — to be inserted in the list.
- **Returns:** does not return any value.

```python
lis = ['Geeks', 'Geeks']
lis.insert(1, "For")
print(lis)
# Output: ['Geeks', 'For', 'Geeks']
```

### count() method
Returns the count of how many times a given object occurs in a List.

**Syntax:** `list_name.count(object)`

**Parameters:** `object` — is the item whose count is to be returned.
**Exception:** `TypeError` — raised if more than 1 parameter is passed in `count()`.

```python
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
print(list2.count('b'))
# Output: 3
```

### Removing elements — del, remove(), pop()
`del` is a **keyword**; `remove()` and `pop()` are **in-built methods**.

- **`remove()`** deletes values or objects from the list **using the value**.
- **`del` and `pop()`** delete values or objects from the list **using an index**.
- The `del` keyword deletes any variable, or a list of values from a list.

**Syntax**
```python
del list_name[index]     # To delete a single value
del list_name            # To delete the whole list
```

- The `remove()` method removes the **first matching value** from the list.
  **Syntax:** `list_name.remove(value)`
- The `pop()` method, like the `del` keyword, deletes a value at a particular index. **But
  the `pop()` method returns the deleted value from the list.**
  **Syntax:** `list_name.pop(index)`

```python
number = [1, 2, 3, 2, 3, 4, 5]
number.pop(3)
print(number)        # [1, 2, 3, 3, 4, 5]
number.pop(-1)
print(number)        # [1, 2, 3, 3, 4]
number.pop(0)
print(number)        # [2, 3, 3, 4]
```

### max() and min()
- **`max()`** is used to compute the maximum of the values passed in its argument, and the
  **lexicographically largest value** if strings are passed as arguments.
- **`min()`** is used to compute the minimum of the values passed in its arguments.

```python
print("Maximum of 4, 12, 43.3, 19 and 100 is:", end=" ")
print(max(4, 12, 43.3, 19, 100))
# Output: Maximum of 4, 12, 43.3, 19, 100 is = 100
```

### sort() function
Can be used to sort a List in **ascending, descending, or user-defined order**.

**Syntax:** `list_name.sort(reverse=True/False, key=myFunc)`

### reverse() method
An inbuilt method in Python that **reverses objects of the List in place** — i.e. it
doesn't use any extra space but just modifies the original list.

**Syntax:** `list_name.reverse()`

### Modifying a list — summary
```python
fruits[1] = "kiwi"                      # update
fruits.append("grape")                  # add at end
fruits.insert(1, "papaya")              # add at index
fruits.remove("apple")                  # remove by value
fruits.pop()                            # remove last item
```

### Common list operations
| Operation | Example | Result |
|---|---|---|
| Length | `len(fruits)` | no. of items |
| Sort | `fruits.sort()` | sorts in place |
| Reverse | `fruits.reverse()` | reverses order |
| Membership | `'mango' in fruits` | `True` / `False` |
| Combine | `list1 + list2` | concatenated list |

### Full list method reference
| Method | Description |
|---|---|
| `append(x)` | Add item at the end |
| `insert(i, x)` | Insert at index `i` |
| `extend(iterable)` | Add multiple items |
| `remove(x)` | Remove first occurrence of `x` |
| `pop(i)` | Remove and return item at index `i` |
| `index(x)` | Return index of first occurrence |
| `count(x)` | Count occurrences of `x` |
| `sort()` | Sort the list |
| `reverse()` | Reverse the list |
| `clear()` | Remove all items |
| `copy()` | Return a shallow copy |

### List methods with worked examples
Starting from `my_list = [10, 20, 30, 40]`:

| Method | Example | Output |
|---|---|---|
| `append(x)` | `my_list.append(50)` | `[10, 20, 30, 40, 50]` |
| `insert(i, x)` | `my_list.insert(1, 15)` | `[10, 15, 20, 30, 40]` |
| `extend([60,70])` | `my_list.extend([60,70])` | `[10, 20, 30, 40, 60, 70]` |
| `remove(30)` | `my_list.remove(30)` | `[10, 20, 40]` |
| `pop()` | `my_list.pop()` | `40` (returned) |
| `index(20)` | `my_list.index(20)` | `1` |
| `count(20)` | `my_list.count(20)` | `1` |
| `sort()` | `my_list.sort()` | `[10, 20, 30, 40]` |
| `reverse()` | `my_list.reverse()` | `[40, 30, 20, 10]` |
| `clear()` | `my_list.clear()` | `[]` |

Mosh's quick reference:
```python
numbers = [1, 2, 3, 4, 5]
numbers[0]           # returns the first item
numbers[-1]          # returns the first item from the end

numbers.append(6)    # adds 6 to the end
numbers.insert(0, 6) # adds 6 at index position 0
numbers.remove(6)    # removes 6
numbers.pop()        # removes the last item
numbers.clear()      # removes all the items
numbers.index(8)     # returns the index of first occurrence of 8
numbers.sort()       # sorts the list
numbers.reverse()    # reverses the list
numbers.copy()       # returns a copy of the list
```

## 26. List Comprehension

A short, elegant way to create lists in a single line, instead of using a for-loop with
`append()`.

**Syntax**
```
[ expression for item in iterable if condition ]
```

```python
# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension way
squares = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```

**With a condition**
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in nums if n % 2 == 0]
# [2, 4, 6, 8]
```

```python
even = [x for x in range(1, 11) if x % 2 == 0]
print(even)
# Output: [2, 4, 6, 8, 10]
```

### Nested lists (2D lists)
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2]     # 6  (row 1, col 2)
```

## 27. Tuples

A Python Tuple is a **collection of objects separated by commas**. In some ways a tuple is
similar to a list in terms of indexing, nested objects and repetition, **but a tuple is
immutable, unlike lists which are mutable**.

An ordered, immutable collection — once created, it cannot be changed. Defined using round
brackets `( )`.

To create a Tuple we use `()` operators:
```python
var = ("Geeks", "for", "Geeks")
print(var)
```

```python
point = (10, 20)
colors = ("red", "green", "blue")
single = (5,)      # comma needed for a single-item tuple!

point[0]                    # 10
colors.count('red')         # 1
colors.index('blue')        # 2
```

### Accessing values in tuples
- **Method 1:** using positive index
- **Method 2:** using negative index

### Unpacking
You can unpack a list or a tuple into separate variables:
```python
coordinates = (1, 2, 3)
x, y, z = coordinates
```

> **Why tuples?** They are **faster than lists** and **protect data from accidental
> changes** — great for fixed values like coordinates. Because they are immutable they are
> also hashable, so they can be used as dictionary keys.

### Tuple vs List
| | List | Tuple |
|---|---|---|
| **Syntax** | `[10, 20, 30]` | `(10, 20, "apple")` |
| **Mutable** | Mutable | Immutable |
| **Size** | Takes more space | Takes much less space |
| **Performance** | Slower | Faster |
| **Methods** | More methods | Fewer methods |
| **Use case** | Data that can alter | Fixed data; dictionary keys |

## 28. Sets

A set is an **unordered collection data type that is iterable, mutable and has no
duplicate elements**. Sets are represented by `{ }`.

**Since sets are unordered, we can't access items using indexes like we do in lists.**

```python
var = {"Geeks", "for", "Geeks"}
print(type(var))
# Output: <class 'set'>
```

Duplicates are removed automatically:
```python
nums = {1, 2, 3, 3, 2, 1}
print(nums)     # {1, 2, 3}     duplicates removed!

nums.add(4)
nums.remove(1)
```

### Frozen set
Frozen sets are **immutable objects** that only support methods and operators that produce
a result without affecting the frozen set or sets to which they are applied. It can be
done with the `frozenset()` method.

Because frozensets are immutable, they are **hashable** and can be used as dictionary keys
or as elements of another set, unlike regular sets.

### Methods for sets
| Operation | Method / Operator |
|---|---|
| Adding elements to sets | `set.add()` function |
| Union operation on sets | `union()` function or `\|` operator |
| Intersection operation | `intersection()` or `&` operator |
| Difference | `difference()` or `-` operator |
| Symmetric difference | `symmetric_difference()` or `^` operator |
| Clearing sets | `clear()` method |
| Remove element | `remove(x)` (error if not found) / `discard(x)` (no error) |
| Remove arbitrary | `pop()` |
| Add from iterable | `update(iterable)` |

### Set operations
| Operation | Symbol | Example |
|---|---|---|
| Union | `\|` | `a \| b` |
| Intersection | `&` | `a & b` |
| Difference | `-` | `a - b` |
| Symmetric Diff. | `^` | `a ^ b` |

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # {1, 2, 3, 4}
a & b   # {2, 3}
a - b   # {1}
a ^ b   # {1, 4}
```

## 29. Dictionaries

A dictionary is a **collection of key-value pairs**, used to store data values like a
map, which — unlike other data types that hold only a single value as an element — holds
`key: value` pairs.

```python
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
```

### Creating a dictionary
A dictionary can be created by placing a sequence of elements within curly `{}` braces,
separated by 'comma'. Dictionary holds pairs of values, one being the **key** and the
other the corresponding pair element being its **value**.

- **Values** in a dictionary can be of any data type and **can be duplicated**.
- **Keys** can't be repeated and **must be immutable**.

> **NOTE:** Dictionary keys are **case sensitive** — the same name but different cases of
> key will be treated distinctly.

```python
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer keys:")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed keys:")
print(Dict)
```

```python
student = {
    "name": "Abhi",
    "age": 22,
    "course": "Python"
}
```

```python
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
```

You can use strings or numbers to define keys. They should be unique. You can use any
types for the values.

### Accessing & updating values
```python
student["name"]                  # "Abhi"
student.get("age")               # 22
student["age"] = 23              # update value
student["grade"] = "A"           # add new key
```

```python
customer["name"]                 # returns "John Smith"
customer["type"]                 # throws a KeyError
customer.get("type", "silver")   # returns "silver" (a safe default)
```

**Use `.get()` when a key might be missing** — it returns `None` (or your default)
instead of raising `KeyError`.

### Removing items
```python
student.pop("grade")             # removes key "grade"
del student["course"]            # removes key 'course'
student.clear()                  # removes everything
```

### Dictionary methods
| Method | Description |
|---|---|
| `get(key, default)` | Returns value for key, else default |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `update(dict2)` | Update dictionary with items / merges another dict |
| `pop(key)` | Remove and return value for key |
| `popitem()` | Remove and return last inserted pair |
| `clear()` | Remove all items from dictionary |

### Worked example
```python
d = {'name': 'Aman', 'age': 22, 'city': 'Delhi'}

d.get('name')      # Output: Aman
d.keys()           # Output: dict_keys(['name', 'age', 'city'])
d.values()         # Output: dict_values(['Aman', 22, 'Delhi'])
d.items()          # Output: dict_items([('name','Aman'), ('age',22), ('city','Delhi')])

d.update({'age': 23, 'gender': 'M'})
d.pop('city')      # Removes city
d.clear()          # Removes all items
```

### Looping through a dictionary
```python
for key, value in student.items():
    print(key, ":", value)
```

> **Key point:** Dictionaries are **ordered (Python 3.7+)** and very **fast for lookups
> by key**.

### Ordered dictionaries
In older Python versions no order was maintained between keys. To solve this you can use
the **`OrderedDict`** class (available since 2.7), which maintains the insertion order of
keys. Since Python 3.7 regular dicts preserve insertion order too.

### List vs Dictionary
| | List | Dictionary |
|---|---|---|
| **Syntax** | Objects stored in a sequence | Objects stored in key-value pairs |
| **Reference** | Access by index number (starts at 0) | Access by key |
| **Ordering** | Stored in an ordered sequence | (Historically unordered; ordered since 3.7) |
| **Hashing** | No hashing needed | Keys have to be hashable |

## 30. Collections Compared

**Collections** are used to store multiple items in a single variable. Python has **four
built-in collection datatypes**. They are all **mutable (changeable) except Tuple, which
is immutable**. Choosing the right collection type makes the program efficient.

```
                    Python Collections
                            │
    ┌───────────┬───────────┼───────────┬────────────┐
    ↓           ↓                       ↓            ↓
  List        Tuple                    Set       Dictionary
(Mutable)   (Immutable)              (Mutable)   (Mutable)
```

**Why collections?**
- Store multiple values together
- Easy to access and manage
- Built-in functions & methods
- Improve code readability

### The master comparison table

| Collection | Ordered | Mutable | Allows Duplicates | Access | Syntax | Best Used For |
|---|---|---|---|---|---|---|
| **List** | Yes | Yes | Yes | Index / Slice | `[ ]` | Dynamic data, ordered items, frequent changes |
| **Tuple** | Yes | No | Yes | Index / Slice | `( )` | Fixed data, read-only access |
| **Set** | No | Yes | No | No index | `{ }` | Unique items, membership testing, mathematical ops |
| **Dictionary** | Yes (3.7+) | Yes | No (keys) | Key | `{key: value}` | Key-value data, lookups, mapping |

### Examples of each
```python
List        :  my_list  = [10, 20, 30, 40]
Tuple       :  my_tuple = (1, 2, 3, 4)
Set         :  my_set   = {10, 20, 30}
Dictionary  :  my_dict  = {"name": "Aman", "age": 22}
```

### Quick side-by-side

| LIST | TUPLE | SET | DICTIONARY |
|---|---|---|---|
| Ordered | Ordered | Unordered | Ordered (3.7+) |
| Mutable | Immutable | Mutable | Mutable |
| Allows Duplicates | Allows Duplicates | No Duplicates | No duplicate keys |
| Access by index/slice | Access by index/slice | No index access | Access by keys |
| Syntax: `[ ]` | Syntax: `( )` | Syntax: `{ }` | Syntax: `{key: value}` |
| Methods: `append()`, `remove()`, `pop()`, `sort()`, `reverse()` | Methods: `count()`, `index()`, `len()` | Methods: `add()`, `remove()`, `discard()`, `union()`, `intersection()` | Methods: `get()`, `keys()`, `values()`, `items()`, `update()` |

### Key takeaways — choosing the right one
- **Choose List** when you need an **ordered, changeable sequence**.
- **Choose Tuple** when data **should not change**.
- **Choose Set** when you need **unique items and fast membership testing**.
- **Choose Dictionary** when you need **key-value mapping and fast lookups**.

**Decision flow — "What do you need?"**
```
                    What do you need?
        ┌───────────────┬────────────┬──────────────┬──────────────┐
        ↓               ↓            ↓              ↓
   Ordered &       Ordered &     Unique Items    Key-Value
   Changeable      Unchangeable  (No Duplicates)  Mapping
        ↓               ↓            ↓              ↓
      LIST            TUPLE         SET         DICTIONARY
```

### Comprehensions across all three
Comprehensions provide a concise way to create lists, sets and dictionaries. They improve
readability and are generally faster.

**List comprehension**
```
[expression for item in iterable if condition]
```
```python
squares = [x * x for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]
```

**Set comprehension**
```
{expression for item in iterable if condition}
```
```python
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)
# Output: {2, 4, 6, 8, 10}
```

**Dictionary comprehension**
```
{key_expr: value_expr for item in iterable if condition}
```
```python
cube_dict = {x: x ** 3 for x in range(1, 5)}
print(cube_dict)
# Output: {1: 1, 2: 8, 3: 27, 4: 64}
```

## 31. Nested Collections

Collections can hold other collections. This is how you model real structured data.

**List of Lists (a matrix)**
```python
matrix = [[1, 2, 3],
          [4, 5, 6]]
```
```
⎡ 1  2  3 ⎤
⎣ 4  5  6 ⎦
```

**List of Dictionaries**
```python
students = [
    {'name': 'Aman', 'age': 22},
    {'name': 'Riya', 'age': 21}
]
# students[0] -> {'name': 'Aman', 'age': 22}
# students[1] -> {'name': 'Riya', 'age': 21}
```

**Dictionary of Lists**
```python
marks = {
    'Aman': [80, 90, 85],
    'Riya': [88, 92, 79]
}
# Aman -> [80, 90, 85]
# Riya -> [88, 92, 79]
```

**Set of Tuples**
```python
points = {(1, 2), (3, 4), (1, 2)}
# Duplicates removed
# {(1, 2), (3, 4)}
```

---

# PART 5 — FUNCTIONS

## 32. Defining Functions

Python Functions are a **block of statements that return a specific task**.

The idea is to put some commonly or repeatedly done tasks together and make a function, so
that instead of writing the same code again and again for different inputs, we can do the
function calls to reuse code contained in it over and over again.

Functions break up code into small chunks that are easier to read, understand and
maintain. If there are bugs, it's easier to find bugs in a small chunk than the entire
program. And you can re-use these chunks.

**Syntax**
```
 keyword   function name    parameters
    ↓            ↓              ↓
   def   function_name(parameters):

           # statement    ]────→ Body of Statement

           return expression
                  ↑
            function return
```

**Simplest example**
```python
def fun():
    print("Welcome to GFG")

# Driver code to call a function
fun()

# Output: Welcome to GFG.
```

```python
def greet():
    print("Hello, welcome!")

greet()            # calling the function
```

### Defining and calling a function with parameters

**Syntax**
```
def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
```

**Example**
```python
# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

print(is_prime(78), is_prime(79))
# Output: False True
```

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Abhi")          # Hello, Abhi!
```

```python
def greet_user(name):
    print(f"Hi {name}")

greet_user("John")
```

## 33. Arguments of a Python Function

**Arguments** are the values passed inside the parenthesis of the function. A function can
have any number of arguments separated by a comma.

**Parameters** are placeholders for the data we can pass to functions. **Arguments** are
the actual values we pass.

```python
# A simple Python Function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call the function
evenOdd(2)
evenOdd(3)

# Output:
# even
# odd
```

### Types of arguments

**1. Default argument**
A parameter that assumes a default value if a value is not provided in the function call
for that argument.

```python
def myFun(x, y=50):
    print("x:", x)
    print("y:", y)

# Driver code (We call myFun() with only argument)
myFun(10)

# Output:
# x: 10
# y: 50
```

```python
def greet(name, msg="Good Morning"):
    print(f"{msg}, {name}!")

greet("Abhi")                             # Good Morning, Abhi!
greet("Abhi", msg="Good Night")           # Good Night, Abhi!
```

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())              # Hello, Guest!
print(greet("Alice"))       # Hello, Alice!
```

**2. Keyword arguments**
The idea is to allow the caller to specify the argument name with values so that the
caller does not need to remember the order of parameters.

```python
def student(firstname, lastname):
    print(firstname, lastname)

# Keyword arguments
student(firstname='Geeks', lastname='for')
student(lastname='for', firstname='Geeks')

# Output:
# Geeks for
# Geeks for
```

We have two types of arguments:
- **Positional arguments:** their position (order) matters
- **Keyword arguments:** position doesn't matter — we prefix them with the parameter name

```python
# Two positional arguments
greet_user("John", "Smith")

# Keyword arguments
calculate_total(order=50, shipping=5, tax=0.1)
```

**3. Variable-length arguments**
We can pass a variable number of arguments to a function using special symbols. There are
two special symbols:
- `*args` (**Non-keyword Arguments**)
- `**kwargs` (**Keyword Arguments**)

```python
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Output:
# Hello
# Welcome
# to
# GeeksforGeeks
```

**`*args` — Variable Positional Args**
```python
def total(*args):
    return sum(args)

total(1, 2, 3)           # 6
total(5, 10, 15, 20)     # 50
```

**`**kwargs` — Variable Keyword Args**
```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)

show_info(name="Abhi", age=22)
```

Both together:
```python
def demo(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

demo(1, 2, 3, name="John", age=25, city="Pune")

# Output:
# Positional args: (1, 2, 3)
# Keyword args: {'name': 'John', 'age': 25, 'city': 'Pune'}
```

> `args` = tuple of extra values, `kwargs` = dict of extra key=value pairs.

## 34. The return Statement

The function `return` statement is used to **exit from a function and go back to the
function caller**, and return the specified value or data item to the caller.

**Syntax:** `return [expression_list]`

The return statement can consist of a variable, an expression, or a constant which is
returned to the end of the function execution. **If none of the above is present with the
return statement, a `None` object is returned.**

```python
def square_value(num):
    """This function returns the square value of the entered number"""
    return num ** 2

print(square_value(2))
print(square_value(4))

# Output:
# 4
# 16
```

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8
```

```python
def square(number):
    return number * number

result = square(2)
print(result)     # prints 4
```

> **Remember:** A function without a `return` statement returns **`None`** by default.
> `None` is an object that represents the absence of a value.

## 35. Docstrings

The **first string after the function** is called the Document string or **Docstring** in
short. This is used to describe the functionality of the function. The use of a docstring
in a function is **optional but it is considered a good practice**.

**Syntax:** `print(function_name.__doc__)`

```python
def evenOdd(x):
    """Function to check whether x is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call the function
print(evenOdd.__doc__)

# Output: Function to check whether x is even or odd.
```

**Docstring vs a regular comment:** a docstring is a string literal placed as the first
statement in a module, function, class or method, stored in the object's `__doc__`
attribute and retrievable at runtime via `help()` or introspection tools. A regular `#`
comment is discarded by the parser and has no runtime representation.

*(Compared with Java: the main difference between Javadoc and Docstring is that a docstring
is available during runtime as well, whereas Javadoc is removed from the bytecode and is
not present in the `.class` file. You can even use Docstring comments at runtime as an
interactive help manual.)*

## 36. Variable Scope

| Scope | Meaning |
|---|---|
| **Local** | Defined inside a function; accessible only there |
| **Global** | Defined outside; accessible everywhere |

Python resolves names using the **LEGB rule**: **L**ocal (current function) → **E**nclosing
(any enclosing function) → **G**lobal (module level) → **B**uilt-in (Python's built-in
namespace). The interpreter stops at the first scope where the name is found, raising
`NameError` if none match.

- `global x` inside a function declares that `x` refers to the module-level global variable.
- `nonlocal x` inside a nested function refers to the variable in the nearest enclosing
  (non-global) scope.
- Neither keyword is needed just to **read** a variable — only to **reassign** it.

### Namespaces
A **Namespace** is a mapping between a name and an object; it is currently implemented as
a Python dictionary. Examples: the set of built-in exception names, the set of built-in
names, local names in a function.

Different namespaces are created at different moments and have different lifetimes:
- For the list of built-in names, the namespace is created when the interpreter starts.
- When the interpreter reads the definition of a module, it creates a **global namespace**
  for that module.
- When the interpreter calls a function, it creates a **local namespace** for that function.

## 37. Lambda, map, filter, reduce

### Lambda functions
A **lambda** is a small, **anonymous**, one-line function — useful for short throwaway
operations. Wherever you need a function, you can also use a lambda expression.

**Syntax:** `lambda arguments : expression`

```python
square = lambda x: x ** 2
print(square(5))     # 25

add = lambda a, b: a + b
print(add(3, 4))     # 7
```

A lambda cannot contain statements or multiple expressions, only one implicit return. It
is commonly used as a short callback for `sorted()`, `map()` or `filter()` where defining
a full function would be overkill. A lambda expression can also be used to return a
function, or to pass a function as an argument to another function.

### map()
Applies a function to all items in an iterable.
```python
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
print(squares)     # [1, 4, 9]
```

### filter()
Filters items based on a condition.
```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)       # [2, 4]
```

### reduce()
Applies a function cumulatively. **Note: don't forget to import `reduce` from `functools`.**
```python
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)     # 24
```

These three are the foundation of **functional programming** in Python, where you
decompose a program into functions that take input and produce output without maintaining
state. Iterators and generators can be used for functional programming too.

## 38. Pass by Reference or Pass by Value

One important thing to note is that **in Python every variable name is a reference**. When
we pass a variable to a function, a **new reference to the object** is created.

Every argument in a Python method is an Object. All the variables in Python have a
reference to an Object. Therefore arguments in a Python method are **passed by reference**.

Since some of the objects passed as reference are **mutable**, we can change those objects
in a method. But for an **immutable** object like a String, any change done within a method
is not reflected outside.

```python
def myFun(x):
    x[0] = 20

# Driver Code (Note the lst is modified after function call)
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# Output: [20, 11, 12, 13, 14, 15]
```

---

# PART 6 — ORGANIZING CODE

## 39. Modules

Modules provide a way to **organize your code logically**. Instead of having all your code
in a single file, you can split it into multiple modules based on their purpose.

For example, you might have one module for handling input/output operations, another for
mathematical calculations, and another for data manipulation.

When you want to use the functionality from a module, you import it into your current
program or another module. This allows you to access and use the functions, classes and
variables defined within that module. By importing a module you can **avoid writing the
same code repeatedly** and instead reuse the code defined in the module.

A module is simply a **Python file (`.py`)** containing functions, classes or variables
that can be reused in other programs.

```python
# math_utils.py
def add(a, b):
    return a + b

# main.py
import math_utils
print(math_utils.add(2, 3))         # 5
```

```python
# mymodule.py
def add(a, b):
    return a + b

PI = 3.14159
```

```python
import mymodule
result = mymodule.add(5, 7)
print(result)      # Output: 12
```

### Three main types of modules

```
                     Modules
                        │
     ┌──────────────────┼──────────────────┐
     ↓                  ↓                  ↓
 Built-in           External           User-defined
 modules            Modules            Modules
```

**1. Built-in modules**
- Modules that come **pre-installed with Python**. They are part of the standard library
  and provide a wide range of functionalities.
- Examples: `math` for mathematical operations, `random` for generating random numbers,
  `datetime` for working with date and time, and `os` for interacting with the operating
  system.
- Built-in modules are readily available for use **without the need for additional
  installation**.

**2. External modules**
- Modules created by **third-party developers** that are not part of the standard library.
- They extend Python's capabilities by providing additional functionalities for specific
  purposes.
- External modules can be downloaded and installed using package managers like **pip**
  (Python Package Index).
- Popular external modules include **numpy** for numerical computations, **pandas** for
  data manipulation and analysis, **matplotlib** for data visualization, and **requests**
  for making HTTP requests.

**3. User-defined modules**
- Modules created by the Python programmers themselves.
- They allow users to organize their code into separate files and reuse functionality
  across multiple programs.
- User-defined modules can contain functions, classes, variables and other code that can
  be imported and used in other Python scripts or modules.

### Different import styles
```python
import math
from math import sqrt
from math import pi as PI
from math import *      # imports everything (avoid this!)
```

```python
# importing the entire converters module
import converters
converters.kg_to_lbs(5)

# importing one function in the converters module
from converters import kg_to_lbs
kg_to_lbs(5)
```

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

### Sharing variables across modules
Create a **common module** with the variables you want to share, then import that common
module in all the modules where you need them. This way all shared variables live in one
place and are available to any new module too.

## 40. Packages

A **package** is a folder of related modules — a **directory with `__init__.py` in it**.
It can contain one or more modules. The `__init__.py` file tells Python that the directory
is a package.

**Example structure**
```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpkg/
    ├── __init__.py
    └── module3.py
```

```python
# importing the entire sales module
from ecommerce import sales
sales.calc_shipping()

# importing one function in the sales module
from ecommerce.sales import calc_shipping
calc_shipping()
```

### Module vs Package
| | Module | Package |
|---|---|---|
| **What** | Single Python file (`.py`) | Collection of modules in a directory |
| **Contains** | Functions, classes, variables | Multiple modules and an `__init__.py` file |
| **Imported using** | `import module_name` | `import package_name` or `from package import module` |
| **Example** | `math.py` | `mypackage/` |

**Quick tips**
- Use **modules** to organize code.
- Use **packages** for larger projects.
- Always use **meaningful names**.
- Keep code **reusable and maintainable**.
- Follow **PEP 8** naming conventions.

## 41. pip & PyPI

In simple terms, **pip is a package manager for Python**. It stands for "Pip Installs
Packages" or "Pip Installs Python Packages".

When working with Python you may need to use external libraries or modules that provide
additional functionality beyond what the standard library offers. These libraries are
often developed by the Python community and are available for anyone to use.

Pip makes it easy to **install, manage and uninstall** these external libraries. It helps
you find and download the libraries you need from the **Python Package Index (PyPI)**,
which is a repository of Python packages maintained by the community.

With pip you can install a package by running a simple command in your terminal or command
prompt.

```bash
pip install requests
pip install numpy pandas
pip install openpyxl
pip uninstall openpyxl
pip list           # show installed packages
```

## 42. Standard Library Tour

Python comes with a huge library of modules for performing common tasks such as sending
emails, working with date/time, generating random values, etc.

### Commonly used built-in modules
| Module | Used For |
|---|---|
| `math` | Mathematical operations |
| `random` | Generating random numbers |
| `datetime` | Working with dates & times |
| `os` | Interacting with the operating system |
| `sys` | System-specific parameters & functions |

### The random module
```python
import random

random.random()            # returns a float between 0 to 1
random.randint(1, 6)       # returns an int between 1 to 6

members = ['John', 'Bob', 'Mary']
leader = random.choice(members)   # randomly picks an item

print(random.randint(1, 100))     # random number 1-100
```

### Popular libraries for data analysis
- **Pandas** — powerful Python data analysis toolkit
- **SciKit (scikit-learn)** — machine learning library
- **Seaborn** — statistical data visualization
- **SciPy** — open source system for science, mathematics and engineering
- **NumPy** — numerical computation
- **Matplotlib** — plotting and visualization

### Useful tooling
- **Debugging** — use `pdb`:
  ```python
  import pdb
  pdb.set_trace()
  ```
  After adding these lines your code runs in debug mode, where you can use commands like
  breakpoint, step through, step into.
- **Profiling** — use `cProfile`. It can be called from your code as well as from the
  interpreter. It gives you the number of function calls and the total time taken to run
  the script; results can be written to a file instead of stdout.
- **Static analysis** — `PyChecker` detects errors and gives warnings for style issues.
  Other tools to find bugs: `pylint` and `pyflakes`.
- **Unit testing** — `unittest` (see Part 7 note below).

### Running a Python script in Unix
Add this as the first line in the script file:
```python
#!/usr/local/bin/python
```
This tells Unix to use the Python interpreter to execute the script.

### Specifying source code encoding
By default every source file in Python is in **UTF-8** encoding. You can specify your own
encoding by adding this line after the `#!` line:
```python
# -*- coding: encoding -*-
```

---

# PART 7 — FILES & ERRORS

## 43. File Handling

### Opening & closing files

| Mode | Meaning |
|---|---|
| `'r'` | Read (default) |
| `'w'` | Write (overwrites file) |
| `'a'` | Append (adds to end) |
| `'r+'` | Read and Write |
| `'x'` | Exclusive creation (fails if file exists) |
| `'b'` | Binary mode (append to another mode, e.g. `'rb'`) |

```python
file = open("data.txt", "r")
content = file.read()
file.close()

# Better way - auto closes the file
with open("data.txt", "r") as file:
    content = file.read()
```

**Always prefer the `with` statement.** It is used for **context management** — ensuring
proper acquisition and release of resources. It calls `__enter__` at the start and
`__exit__` at the end, **even if an exception occurs**, so the file is always closed.

### Writing to a file
```python
with open("data.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning file handling.")
```

## 44. Exception Handling

Errors that occur during execution (runtime) are called **exceptions**. If not handled,
they crash the program. An exception is an error that occurs during the execution of a
program and **disrupts the normal flow**.

### Common built-in exceptions
| Exception | Meaning |
|---|---|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `FileNotFoundError` | File not found |
| `IndexError` | Index out of range |
| `KeyError` | Key not found in dict |
| `AttributeError` | Attribute does not exist |
| `IndentationError` | Bad indentation |

### try / except
The **try-except block** is used to catch and handle exceptions so that the program
doesn't crash.

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

### try / except / finally
The **`finally` block** contains code that executes **no matter what** — whether an
exception occurred or not. It is great for cleanup code.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")
finally:
    print("Execution complete.")
```

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

Mosh's version:
```python
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Age cannot be 0')
```

### The full flow: try / except / else / finally
- **`try`** — holds code that might raise an exception.
- **`except`** — catches and handles matching exceptions.
- **`else`** — runs **only if no exception occurred** in try.
- **`finally`** — **always runs**, whether or not an exception occurred; used for cleanup
  like closing files or releasing locks, even if the function returns early.

**Ordering matters:** except clauses are checked top to bottom, and the first matching one
runs — so **more specific exception types must be listed before more general ones** (e.g.
`except ValueError` before `except Exception`), or the specific handler will never be
reached.

### The raise keyword
`raise` is used to **manually throw an exception**.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    else:
        print("Access granted")

check_age(16)      # Raises ValueError
```

```python
if student_score < 0:
    raise ValueError("Score can not be negative")
```

If you don't want to stop the program, you can just catch the error condition, print a
message and continue:

```python
try:
    age = 18 + 'duration'
except:
    print("duration has to be a number")
age = 18
print(age)
```

### Syntax Errors vs Exceptions

| Syntax Errors | Exceptions |
|---|---|
| Occur when the code violates Python grammar rules | Occur during the execution of a valid program |
| Detected by the interpreter **before** execution | Caused by **runtime** conditions |
| Prevent the program from running at all | Can be handled using try-except |
| Example: missing colon, unmatched parentheses, indentation error | Example: division by zero, file not found, invalid input |
| `if True` ← missing colon | `x = 10 / 0` ← runtime exception |

**Quick tips**
- Use `try-except` to handle errors gracefully.
- Always add `finally` to clean up resources.
- **Never ignore exceptions — handle them!**
- Exceptions are not failures, they are opportunities to make your code stronger.

### Unit testing (related)
You can use `unittest` (or `unittest2`) to create and run unit tests, and even automate
them. Main components:
1. **Test fixture** — preparation methods required to run a test; can also perform
   post-test cleanup.
2. **Test case** — the main unit test run on a piece of code. Use the `TestCase` base
   class to create new test cases.
3. **Test suite** — aggregate your unit test cases.
4. **Test runner** — executes unit tests and produces reports of the test run.

---

# PART 8 — OBJECT-ORIENTED PROGRAMMING

## 45. Why OOP

**Object-Oriented Programming (OOP)** is a programming paradigm that **organizes code
around Objects instead of functions and logic**.

An **Object** is a real-world entity that has **state (data)** and **behavior (methods)**.

**In simple words:** OOP helps us model real-world things in a program.

### Think like an interviewer
- What real-world problem does OOP solve?
- How does it make our code better?
- Why is Python a great language for OOP?

→ It models real-world entities.
→ It makes code reusable, modular and easy to maintain.
→ It helps in managing complexity.
→ Python supports OOP in a simple and powerful way.

### Real-world analogy: a BANK
Think of a **BANK**. A bank has **customers**. Each customer has an **account**. An account
has a **balance**. We can **deposit**, **withdraw** and **check balance**. These are the
**data (state)** and **actions (behavior)** of the account object.

```
 Customer  →  BANK  →  Balance
              Account
                ↓
   ┌────────────┼────────────┐
   ↓            ↓            ↓
Deposit    Withdraw    Check Balance
```

### Key benefits of OOP
| Benefit | Meaning |
|---|---|
| **Reusability** | Reuse classes and objects in different parts of the program |
| **Modularity** | Break large problems into smaller, manageable objects |
| **Maintainability** | Easy to update and maintain code in the long run |
| **Scalability** | Easy to extend functionality without breaking existing code |
| **Reduces complexity** | Better organization makes complex systems easier to handle |

### Python example: bank account
```python
class BankAccount:
    def __init__(self, customer, balance):
        self.customer = customer      # state
        self.balance = balance        # state

    def deposit(self, amount):
        self.balance += amount        # behavior

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount    # behavior
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.balance           # behavior
```

### How this maps to the real world
| OOP Term | Meaning | Bank Example |
|---|---|---|
| **Class** | Blueprint / Template | `BankAccount` (a blueprint) |
| **Object** | Real-world instance | My Account, Your Account |
| **Attribute (Data)** | State of the object | `customer`, `balance` |
| **Method (Function)** | Behavior / Actions | `deposit()`, `withdraw()`, `get_balance()` |

> **Interview tip:** Always relate OOP concepts to real-life examples. Say: *"It helps
> organize code like real-world things."* Focus on Objects, their state and behavior.

**Is Python OOP or functional?** Python uses most of the Object Oriented programming
concepts, but you can also do functional programming in Python. Experts call Python a
**multi-paradigm** programming language — you can do functional, procedural,
object-oriented and imperative programming with it.

## 46. Class vs Object

**Blueprint vs Real-world Instance.**

### CLASS
- A class is a **blueprint or template** for creating objects.
- It defines the **attributes (data)** and **methods (behavior)** that the objects will have.

### OBJECT
- An object is a **real-world instance** of a class.
- It has its own **identity**, **state (data)** and **behavior**.

### Real-world analogy
Think of a class as the **design of a CAR**. It describes what a car can do and what
features it has. Objects are the **actual cars** built using that design.

```
CLASS (BLUEPRINT)        OBJECTS (REAL CARS)
   Car Class        →    My Car (Object)  |  Your Car (Object)
   [blueprint]           KA01AB1234       |  KA05CD5678
```

### Python example
```python
# 1. Class (Blueprint)
class Car:
    def __init__(self, brand, color, model):
        self.brand = brand          # attribute
        self.color = color          # attribute
        self.model = model          # attribute

    def start(self):
        return f"{self.brand} {self.model} started!"

# 2. Objects (Real-world cars)
my_car = Car("Toyota", "Red", "Glanza")
your_car = Car("Honda", "Blue", "City")

print(my_car.start())      # Toyota Glanza started!
print(your_car.start())    # Honda City started!
```

### Key differences
| Aspect | Class | Object |
|---|---|---|
| **Definition** | Blueprint or template | Real-world instance |
| **Exists in Memory** | Once | Many times |
| **Created Using** | `class` keyword | Constructor (`__init__()`) |
| **Example** | `Car` | `my_car`, `your_car` |
| **Memory Allocation** | No memory for data | Has memory for data |
| **Purpose** | Defines structure | Uses structure |

### What a Car class defines
- **ATTRIBUTES (DATA):** `brand`, `color`, `model`
- **METHODS (BEHAVIOR):** `start()`, `stop()`, `drive()`
- **OBJECTS (INSTANCES):** `my_car`, `your_car`, many more…

Mosh's version:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

point1 = Point(10, 5)
point2 = Point(2, 4)
```

When a function is part of a class, we refer to it as a **method**.

> **Interview tip:** Class is the plan. Object is the product built using the plan.
> Multiple objects can be created from one class.
>
> **Key point:** Classes help in code reuse. Objects make the code real and useful. OOP is
> all about modeling real-world things!
>
> **Memory tip:** Class = Blueprint (e.g. house design). Object = Actual thing built from
> it (e.g. real house).

## 47. self and `__init__()`

**Every object needs an identity and a start.**

### self
- `self` refers to the **current object instance**.
- It lets us access attributes and methods inside the class.

### `__init__()`
- A special method (**constructor**).
- **Runs automatically when an object is created.**
- Used to **initialize attributes**.

### Example: game character
Every game character has a name, health and level. We'll create a class to represent our
character.

```python
class GameCharacter:
    def __init__(self, name, health, level):
        # self refers to the current object
        self.name = name        # attribute
        self.health = health    # attribute
        self.level = level      # attribute

    def introduce(self):
        print(f"{self.name} | Level {self.level} | "
              f"Health: {self.health}")

# Creating an object (instance)
hero = GameCharacter("Arjun", 100, 1)
hero.introduce()
# Output: Arjun | Level 1 | Health: 100
```

### How it works
1. **Object is created** — `hero = GameCharacter("Arjun", 100, 1)`
2. **`__init__()` runs automatically** —
   `self.name = "Arjun"`, `self.health = 100`, `self.level = 1`
3. **Object is ready to use** — `hero.introduce()`

### Visual memory
```
Class Blueprint              Object (hero)
GameCharacter      Creates
  name         ───────────→   name   : Arjun
  health                      health : 100
  level                       level  : 1
  introduce()
```

### Key takeaway
- `self` is the reference to the current object.
- `__init__()` initializes the object's state.
- **Attributes** hold the data.
- **Methods** define the behavior.

> **Remember:** `self` is like "me" inside the class. `__init__()` is like "setting things
> up" when a new object is born.

### The dunder convention
Python provides many built-in functions surrounded by double underscore `__` at the start
and end of the function name. Per Python documentation, the double `__` symbol is used for
**reserved names** of functions — also known as **system-defined names**. Important ones
include `object.__new__`, `object.__init__`, `object.__del__`.

## 48. Encapsulation

**Hide the Data, Expose the Behavior.**

### Concept
Encapsulation means **wrapping data (attributes) and methods (behavior) together in a
class and restricting direct access to some of the data**.

> Protect the data. Provide **controlled** access.

### Real-world analogy: a BANK ACCOUNT
A user **requests through methods**; the BankAccount holds the **internal balance**
(locked); the result is **safe and controlled access** to the money.

```
        BANK
User → BankAccount (Internal Balance 🔒) → Money
            ↓
  ┌─────────┼─────────┐
  ↓         ↓         ↓
deposit() withdraw() get_balance()
Add Money Remove Money Check Money
```

### Python example
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private (encapsulated)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount(1000)
acc.deposit(500)          # Deposited: 500
acc.withdraw(200)         # Withdrew: 200
print(acc.get_balance())  # 1300
```

### Access restriction
Direct access to `__balance` is **not allowed**:
```python
print(acc.__balance)
# AttributeError: 'BankAccount' object has no attribute '__balance'
```

**Why?** Because `__balance` is internal data. We can only interact with it using public
methods.

### How it works
```
User → deposit(500) → Validation (inside class) → __balance Updated Safely
```
*Data stays private. Access is controlled.*

### Key benefits
| Benefit | Meaning |
|---|---|
| **Data protection** | Prevents direct modification of important data |
| **Data validation** | We can validate data before updating it |
| **Easy to maintain** | Internal changes do not affect outside code |
| **Reduce complexity** | Users only interact with what is necessary |
| **Less error prone** | Controlled access leads to fewer bugs |

### Quick summary
- Wrap data and methods in a class.
- Make sensitive data private (`__`).
- Provide public methods to access or modify data.
- Control and validate all access through methods.

> **Interview tip:** Encapsulation is **not** about hiding data completely. It's about
> hiding the **implementation details** and showing only what is necessary.

### `_x` vs `__x` — single vs double underscore
Python has **no true access-control keywords**; conventions signal intent instead.

| `_x` (single underscore) | `__x` (double underscore) |
|---|---|
| Just a **convention** (weak private) | **Name mangling** (stronger private) |
| Can be accessed outside | Not directly accessible |
| Meant for "internal use" only | Access via `_ClassName__x` |

```python
class Demo:
    def __init__(self):
        self._x = 10

obj = Demo()
print(obj._x)     # 10  — works fine
```

```python
class Demo:
    def __init__(self):
        self.__x = 10

obj = Demo()
print(obj.__x)          # ✗ AttributeError
print(obj._Demo__x)     # 10
```

**Name mangling:** when an attribute name inside a class body starts with two leading
underscores (and at most one trailing underscore), e.g. `__value`, Python automatically
rewrites it internally to `_ClassName__value`. This makes accidental overriding by
subclasses less likely, though the attribute remains accessible if you know the mangled
name.

> **Tip:** Use `_x` for internal use, `__x` when you want stronger data hiding.

## 49. Inheritance

**Reusing Code. Extending Behavior.**

### Concept
Inheritance allows a new class (**child / subclass**) to acquire the properties and
behavior of an existing class (**parent / superclass**).

- ✅ Reusability
- ✅ Extensibility
- ✅ Establishes an **IS-A** relationship

> Dog **IS-A** Animal
> Cat **IS-A** Animal

### Real-world analogy: ANIMALS
```
              Animal
        (Parent / Superclass)
     Animal provides common features.
     Specific animals add their own.
                 │
        ┌────────┴────────┐
        ↓                 ↓
       Dog               Cat
  (Child Class)     (Child Class)
   • barks           • meows
   • wags tail       • purrs
```

### Python example
```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child Class: Dog
class Dog(Animal):              # Inherits from Animal
    def bark(self):
        print(f"{self.name} says Woof! 🐶")

# Child Class: Cat
class Cat(Animal):              # Inherits from Animal
    def meow(self):
        print(f"{self.name} says Meow! 🐱")

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()       # Inherited method
dog.sleep()     # Inherited method
dog.bark()      # Dog specific

cat.eat()       # Inherited method
cat.sleep()     # Inherited method
cat.meow()      # Cat specific
```

**Sample output**
```
Buddy is eating.
Buddy is sleeping.
Buddy says Woof! 🐶
Whiskers is eating.
Whiskers is sleeping.
Whiskers says Meow! 🐱
```

### How inheritance works
1. `Animal` defines common attributes and methods (`name`, `eat()`, `sleep()`).
2. `Dog` and `Cat` inherit from `Animal`.
3. They reuse what `Animal` provides and add their own unique behavior
   (Dog adds `bark()`, Cat adds `meow()`).

> Avoids code duplication and promotes reusability.

### Key points
| Concept | Meaning |
|---|---|
| **IS-A Relationship** | Dog IS-A Animal; Cat IS-A Animal |
| **Code Reusability** | Reuse methods like `eat()`, `sleep()` |
| **Extensibility** | Add new methods without modifying the parent class |
| **Hierarchy** | Build a natural hierarchy of classes |

### Mosh's minimal example
Inheritance is a technique to remove code duplication. We create a base class to define
the common methods and then have other classes inherit these methods.

```python
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

dog = Dog()
dog.walk()      # inherited from Mammal
dog.bark()      # defined in Dog
```

### Method overriding
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):              # inherits from Animal
    def speak(self):            # overrides parent method
        print("Woof!")

Dog().speak()             # Woof!
```

The child class provides its own implementation. The method name is the same, but the
behavior is different.

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

> **Tip:** Override only when behavior **needs to change**, not just to reuse.

### super() and multiple inheritance
- `super()` calls the **next class in the Method Resolution Order (MRO)**, not simply "the
  parent". This makes cooperative multiple inheritance work correctly.
- Inspect the order with `ClassName.__mro__` or `ClassName.mro()`. Python uses the **C3
  linearization** algorithm.
- A **mixin** is a class designed to be combined with others via multiple inheritance to
  add a specific piece of reusable behavior, without being meant to stand alone.

### Checking subclass relationships
```python
issubclass(bool, int)     # True
```

### Composition vs Inheritance
- **Inheritance** models an **"is-a"** relationship, where a subclass extends and
  specializes a parent class.
- **Composition** models a **"has-a"** relationship, where an object contains and
  delegates to other objects.
- **Composition is often preferred** for flexibility, since it avoids tight coupling to a
  rigid class hierarchy.

> **Interview tip:** Use inheritance when classes share common behavior. **Prefer
> composition over inheritance when possible** (flexibility). Always ask: IS-A
> relationship or NOT?

## 50. Polymorphism

**One Interface, Many Forms.**

### Concept
Polymorphism (many forms) allows objects of **different classes** to be treated as objects
of a **common type** through a **common method**.

> Same method name, different behavior.

### Real-world analogy: NOTIFICATION SYSTEM
Different channels, same action: `send()`.

```
   Email          SMS           Push
   send()        send()        send()
```

### Python example
```python
# Base Class (Interface)
class Notification:
    def send(self):
        pass

# Different implementations
class Email(Notification):
    def send(self):
        print("Sending Email")

class SMS(Notification):
    def send(self):
        print("Sending SMS")

class Push(Notification):
    def send(self):
        print("Sending Push Notification")

# Using polymorphism
notifications = [Email(), SMS(), Push()]

for notification in notifications:
    notification.send()
```

**Sample output**
```
Sending Email
Sending SMS
Sending Push Notification
```

### How polymorphism works
```
Client Code  →  Notification Interface  →  Different Objects
Calls send()        send()                 Email | SMS | Push
                                     Different behavior, same method name!
```

> The client doesn't care what type it is. It only cares that it can `send()`.

### Another example
```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

for animal in [Cat(), Dog()]:
    print(animal.sound())     # Meow Bark
```

### Key benefits
| Benefit | Meaning |
|---|---|
| **Flexibility** | Add new notification types easily |
| **Extensibility** | Open for extension, closed for modification |
| **Clean code** | Works with interface, not implementation |
| **Loose coupling** | Client is independent of concrete classes |

> **Interview tip:** Polymorphism is achieved through **method overriding**. Python uses
> **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Focus
> on behavior, not the actual type.

**Duck typing** is a concept where the type of an object is less important than the
methods or attributes it has. If an object behaves like a duck (has the needed methods),
Python treats it as one. This allows flexible, dynamic code without strict type checking —
enabling polymorphism **without inheritance**.

**Quick check:** *Why is polymorphism useful in real projects?*
→ It allows different components to work together seamlessly through a common interface.

## 51. Abstraction

**Focus on What, Not How.**

### Concept
Abstraction means **showing only the essential part to the user and hiding the internal
implementation details**.

> The user uses the feature, but doesn't need to know how it works inside.

### Real-world analogy: a PAYMENT SYSTEM
The user says "I just want to pay." The `Payment process()` hides the implementation.
Different payment methods (Stripe / UPI / Card) are hidden from the user.

> The user only sees `process()`, not the complex steps inside.

### Python example
```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

# Different implementations (hidden from user)
class StripePayment(Payment):
    def process(self, amount):
        print(f"Processing ₹{amount} via Stripe")

class UPIPayment(Payment):
    def process(self, amount):
        print(f"Processing ₹{amount} via UPI")

class CardPayment(Payment):
    def process(self, amount):
        print(f"Processing ₹{amount} via Card")

# Client code (user)
def make_payment(payment: Payment, amount):
    payment.process(amount)
```

### How abstraction works
```
USER CODE                          BEHIND THE SCENES
payment = UPIPayment()             UPIPayment.process(500)
make_payment(payment, 500)                  ↓
# User only calls process()        Connect to UPI gateway
                                            ↓
                                     Verify & Process
                                            ↓
                                     Complete Payment ✅
```

> The user doesn't need to know these steps. They only care that the payment is successful!

### The abc module
The `abc` (Abstract Base Classes) module provides infrastructure for defining abstract
base classes. Using `@abc.abstractmethod` you declare methods subclasses **must**
implement. A class with unimplemented abstract methods **cannot be instantiated** — it
raises `TypeError`. ABCs enforce interface contracts throughout a class hierarchy.

Combining `@property` with `@abstractmethod` declares an **abstract property**, requiring
subclasses to provide a concrete implementation.

### Benefits of abstraction
| Benefit | Meaning |
|---|---|
| **Reduces complexity** | Shows only what is necessary, hides the unnecessary details |
| **Improves security** | Hides sensitive implementation details |
| **Easy to extend** | New payment methods can be added without changing user code |
| **Maintainable code** | Internal changes don't affect the user or other parts of the system |

### Summary
- Abstraction hides the **"how"** and shows the **"what"**.
- User interacts with high-level code.
- Implementation can change without affecting the user.
- It helps in building clean, secure and maintainable code.

> **Interview tip:** Look for keywords like *interface*, *abstract*, *hide*,
> *implementation*, *essential*, *contract*. Abstraction is about **managing complexity by
> showing only the important part**.

## 52. Operator Overloading

Operator overloading allows custom classes to define behavior for **built-in operators**
using **dunder (double-underscore) methods**.

| Dunder | Operator |
|---|---|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__and__` | `&` |
| `__or__` | `\|` |
| `__xor__` | `^` |
| `__lshift__` | `<<` |
| `__rshift__` | `>>` |
| `__invert__` | `~` |
| `__lt__` | `<` |
| `__eq__` | `==` |
| `__len__` | `len()` |
| `__contains__` | `in` |

This allows objects to integrate naturally with Python syntax.

### Worked example from the handwritten notes
```python
class Geek:
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("XOR operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value

# Driver's code
if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)

# Output:
# And operator overloaded
# 8
# Or operator overloaded
# 14
# Xor operator overloaded
# 8
# lshift operator overloaded
# 40960
# rshift operator overloaded
# 8
# Invert operator overloaded
# -11
```

### `__str__` vs `__repr__`
- **`__str__`** returns a human-readable string for end users, used by `print()` and `str()`.
- **`__repr__`** returns an unambiguous developer-facing representation, used by the
  interpreter and `repr()`.
- If only `__repr__` is defined, it serves as the fallback for `__str__`.
- Best practice: `__repr__` should return a string that could recreate the object.

## 53. Class Variables vs Instance Variables

- A **class variable** is defined directly inside the class (outside methods) and is
  **shared across all instances**.
- An **instance variable** is defined inside `__init__` using `self.variable` and is
  **unique to each instance**.
- Modifying a class variable via an instance creates a new instance variable that
  **shadows** the class variable for that instance only.

### self vs cls
- `self` → **instance (object)** — works on object data (each object has its own copy)
- `cls` → **class** — works on class data (shared by all objects)

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
# c1.value  → 2
# c2.value  → 1
# Counter.count → 2
```

> **Tip:** Use `self` for instance data, `cls` for shared data or alternate constructors.

### @staticmethod vs @classmethod
- **`@staticmethod`** defines a method with **no implicit first argument** — a plain
  function namespaced inside a class.
- **`@classmethod`** receives **`cls`** (the class itself) as the first argument and can
  access or modify class-level state. Commonly used as an **alternative constructor**.

### @property
The `@property` decorator allows a method to be **accessed like an attribute**. It enables
getter, setter and deleter functionality with `@property`, `@name.setter` and
`@name.deleter`. This enforces encapsulation by validating or computing values on access
without exposing internal implementation details.

## 54. Common OOP Traps

Small details, big impact in interviews.

### 1. self vs cls
Covered above — `self` → object level; `cls` → class level.

### 2. `__init__()` — the constructor trap
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

- If `__init__()` is **missing** → the object is **still created**.
- If **parameters are wrong** → **`TypeError`**.

> **Tip:** `__init__` is for **initialization**, not for **creating** new objects.
> (`__new__` creates and returns a new instance, called *before* `__init__`. `__init__`
> then initializes the already-created instance.)

### 3. Method overriding
Covered above — child method overrides parent method; method name same, behavior different.

> **Tip:** Override only when behavior needs to change, not just to reuse.

### 4. `_x` vs `__x`
Covered in Encapsulation above.

### Quick recap table
| Trap | Rule |
|---|---|
| **self vs cls** | `self` → object level; `cls` → class level |
| **`__init__()`** | Runs automatically. Initialize, don't create. |
| **Overriding** | Same method name, different behavior. |
| **`_x` vs `__x`** | `_x` → weak convention; `__x` → name mangling |

### Common mistakes
| ✗ Mistake | ✓ Fix |
|---|---|
| Using `self` in class methods | Always use `cls` — `@classmethod def create(cls): pass` |
| Forgetting `__init__` params → Mismatch → `TypeError` | `__init__(self, name)` then `obj = Class()` ✗ |
| Overriding by mistake — changing behavior unintentionally | Check before overriding |
| Accessing `__x` directly → leads to `AttributeError` | Use `_ClassName__x` |

> **Interview tip:** Interviewers love to test edge cases. Small mistakes in OOP concepts
> signal lack of clarity. Be confident with these details — they are high scoring.

### Mini challenge — predict the output
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

**Think step-by-step:**
1. `d1 + d2` calls `Dog.__add__()`
2. Inside `Dog.__add__()` it calls `super().__add__(other)` (i.e. `Animal.__add__`)
3. `Animal.__add__()` adds names and ages: Name = "BuddyMax", Age = 3 + 2 = 5
4. Back in `Dog.__add__()`, creates a new Dog with Name "BuddyMax", Age 5, Breed from
   `d1` → "Labrador"

**Expected output:**
```
BuddyMax (5 yrs) - Labrador
```

**Key concepts tested:** Method Overriding (`__add__`), `super()` to call parent behavior,
Operator Overloading (`+`), Inheritance (Dog is-a Animal).

> **Interview tip:** Always check if a child class overrides a method. Look for `super()`
> usage and why it's used. Understand how special methods (`__add__`, `__str__`, etc.)
> behave.
>
> **Remember:** OOP is all about behavior + relationships + real-world modeling!

## 55. All Four Pillars in One System

### The 4 pillars at a glance

| Pillar | One line | Memory trick |
|---|---|---|
| **1. Encapsulation** | Hide data, control access. Keep data safe. | Think **"Capsule"** — data is inside, protected like a capsule. |
| **2. Inheritance** | Reuse code, build hierarchy. DRY Principle. | Think **"Family Tree"** — child gets nature from parent. |
| **3. Polymorphism** | Same interface, different behavior. One interface, many forms. | Think **"Many Shapes, One Name"** — same name, different behavior. |
| **4. Abstraction** | Hide complexity, show what's important. Focus on essentials. | Think **"Remote Control"** — you only see buttons, not the complex circuits inside. |

**Remember:** Encapsulation – Secure · Inheritance – Reuse · Polymorphism – Flexibility ·
Abstraction – Simplicity

### Syntax quick reference
```python
# 1. ENCAPSULATION
class Account:
    def __init__(self):
        self.__balance = 0        # private

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt

    def get_balance(self):
        return self.__balance
# Access via methods only
# acc._Account__balance  ✗

# 2. INHERITANCE
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Bark"

d = Dog()
d.speak()      # Bark

# 3. POLYMORPHISM
class Notification:
    def send(self):
        pass

class Email(Notification):
    def send(self):
        return "Email sent"

n = Email()
n.send()       # Email sent

# 4. ABSTRACTION
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class UPI(Payment):
    def process(self, amount):
        return "Paid via UPI"
```

### One-liner recap
| Pillar | Recap | Syntax cue |
|---|---|---|
| **Encapsulation** | Hide data, expose behavior | `self.__x = 10` |
| **Inheritance** | Child class inherits parent | `class B(A): pass` |
| **Polymorphism** | Same method, different forms | `obj.method()` |
| **Abstraction** | Hide details, show essentials | `@abstractmethod` |

### Interview golden rules
- ✅ Always prefer **composition**, then inheritance.
- ✅ Use **abstraction** to reduce complexity.
- ✅ **Polymorphism** makes code flexible.
- ✅ **Encapsulation** protects your data.
- ⭐ Write clean code, think like a designer!

> **Quick tip:** Explain with examples. Draw diagrams if needed. Keep it simple and clear!

---

### Worked system 1 — Online shopping system

A complete system that uses all 4 OOP pillars together.

```
Customer → Browse & Add to Cart → Cart → Payment → Order Delivered
```

**1. ENCAPSULATION** — keep data safe inside classes and control access.
```python
class Order:
    def __init__(self, id):
        self.__order_id = id
        self.__amount = 0

    def add_item(self, item):
        self.__amount += item.price

    def get_total(self):
        return self.__amount
```
*Internal data (`__amount`) is hidden and protected. Access only via methods.*

**2. INHERITANCE** — create specific types of users from a common base.
```python
class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def place_order(self):
        pass

class DeliveryPartner(User):
    def deliver_order(self):
        pass
```
*Customer and DeliveryPartner inherit from User.*

**3. POLYMORPHISM** — same action, different payment methods.
```python
class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("Paying by Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paying by UPI")
```
*Different payment types use the same `pay()` method.*

**4. ABSTRACTION** — hide complex steps, show only what's important.
```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Client uses only this interface
```
*Client calls `process_payment()` without knowing the details.*

**Class overview**
```
User (Base Class)          Order                    Payment (Parent Class)
 - name          ←-------  - order_id      ◇------  + pay(amount)
 - email                   - items                         ↑
 + login()                 - __amount              ┌───────┴───────┐
      ↑                    + add_item()        CardPayment    UPIPayment
 ┌────┴────┐               + get_total()       + pay(amount)  + pay(amount)
Customer  DeliveryPartner        ◇
- address - vehicle          PaymentGateway
- cart    - location         (Interface)
+ browse()+ accept_order()   + process_payment()
+ place_order() + deliver_order()  (abstract)

---→ is-a       ──── uses/has
```

**Example flow**
1. Customer adds item → 2. Places order → 3. `Payment.pay()` (Polymorphism) →
4. `PaymentGateway.process_payment()` (Abstraction) → 5. Order stored safely
(Encapsulation) → 6. DeliveryPartner delivers (Inheritance)

**Key benefits:** Maintainable, Reusable, Flexible, Scalable, Less Error Prone.

> **Interview tip:** Real projects use all 4 pillars together. Always think: How can I make
> my system safe, reusable, flexible and easy to maintain? Don't use inheritance or
> abstraction if not needed.

---

### Worked system 2 — Food delivery app

```
Customer → Place Order → Order (Items, Address, Payment) → Delivery Partner → Order Delivered
```

**Core classes:** Customer · Order · DeliveryPartner · Payment (Abstraction)

**1. ENCAPSULATION** — keep order and payment data safe and controlled.
```python
class Order:
    def __init__(self, items, total):
        self.__items = items
        self.__total = total          # private data

    def get_total(self):
        return self.__total

    def add_item(self, item):
        self.__items.append(item)
```
*Data is hidden. Access only through methods.*

**2. INHERITANCE** — different user types share common features.
```python
class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in")

class Customer(User):
    def place_order(self):
        print("Placing order...")

class DeliveryPartner(User):
    def deliver_order(self):
        print("Delivering order...")
```

**3. POLYMORPHISM** — same method name, different payment behavior.
```python
class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")
```

**4. ABSTRACTION** — hide complex payment steps, expose a simple interface.
```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing {amount} with Stripe")
```

**Mini code flow**
```python
customer = Customer("Riya")                    # Create customer
order = Order(items, address, total)           # Create order
order.add_item("Burger")                       # Add items
order.add_item("Fries")

pay = UPIPayment()   # or CardPayment/StripePayment — Polymorphism in action
pay.process_payment(order.get_total())         # Process payment (Abstraction)

partner = DeliveryPartner("Rahul")             # Assign delivery
partner.deliver_order(order)
```
*All four pillars working together in a real system.*

**Key benefits:** Secure & Safe (protects important data) · Reusable Code (shared code
through inheritance) · Flexible System (change payment method easily) · Easy to Maintain
(hide complexity, show simplicity).

> **Interview tip:** Think in terms of real-world systems. Identify objects, their data and
> behavior. Apply all 4 pillars wherever possible. Always prefer SOLID and clean design.

---

### OOP design practice scenarios

**1. Vehicle scenario** — design a system for different vehicles.
*Requirements:* create a base class `Vehicle`; child classes `Car` and `Bike`; each vehicle
should have `start()` and `stop()`; override `start()` in child classes.
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

# Example Output:
# Car started
# Vehicle stopped
# Bike started
# Vehicle stopped
```
*Tests: Inheritance, Method Overriding, Polymorphism*

**2. Shape scenario** — design a system to calculate the area of different shapes.
*Requirements:* base class `Shape` having method `area()`; create `Circle` and `Rectangle`
classes; override `area()` in each class.
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

# Example Output:
# Circle Area: 78.5
# Rectangle Area: 50
```
*Tests: Abstraction, Method Overriding, Polymorphism*

**3. Payment scenario** — design a payment system.
*Requirements:* base class `Payment` with method `pay(amount)`; create `CreditCard`, `UPI`
and `Wallet` classes; each class implements payment in its own way.
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

# Example Output:
# Paid 500 using Credit Card
# Paid 500 using UPI
# Paid 500 using Wallet
```
*Tests: Polymorphism, Abstraction*

**4. Database scenario** — design a simple database connection system.
*Requirements:* base class `Database` with `connect()` and `close()`; create `MySQL` and
`MongoDB` classes; implement connection in child classes.
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
*Tests: Inheritance, Method Overriding*

**What interviewers look for:**
- **Clear OOP concepts** — do you really understand the pillars?
- **Right design** — can you break the problem into classes?
- **Clean code** — is your code readable and maintainable?
- **Real-world thinking** — can you apply OOP to real scenarios?
- **Confidence** — can you explain your design clearly?

> **Interview tip:** Think before you code. Design comes first! Use all 4 pillars when
> possible. Keep your code simple, clean and well-structured.
>
> **Bonus advice:** Practise these patterns until they feel natural. Solve similar problems
> in your own way. Confidence comes from consistent practice!

---

# PART 9 — REFERENCE

## 56. Command Reference Tables

*(From the "Important Python Commands" sheet — Python is simple, powerful and beginner friendly.)*

### 1. Basic / general commands
| Command | Use |
|---|---|
| `print()` | Prints the output |
| `input()` | Takes input from the user |
| `type()` | Returns the data type |
| `len()` | Returns the length of an object |
| `id()` | Returns the identity of an object |
| `help()` | Shows the help documentation |
| `dir()` | Returns the list of attributes and methods |

### 2. Data type related
| Command | Use |
|---|---|
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `list()` | Converts to list |
| `tuple()` | Converts to tuple |
| `set()` | Converts to set |
| `dict()` | Converts to dictionary |
| `bool()` | Converts to boolean |

### 3. Math & numeric commands
| Command | Use |
|---|---|
| `abs(x)` | Absolute value of x |
| `round(x, n)` | Rounds x to n decimal places |
| `pow(x, y)` | Returns x**y |
| `max(iterable)` | Returns the maximum value |
| `min(iterable)` | Returns the minimum value |
| `sum(iterable)` | Returns the sum of all values |
| `sorted(iterable)` | Returns a sorted list |
| `divmod(x, y)` | Returns quotient and remainder |

### 4. String commands
| Command | Use |
|---|---|
| `s.upper()` | Converts to upper case |
| `s.lower()` | Converts to lower case |
| `s.title()` | Converts first letter of each word to capital |
| `s.strip()` | Removes leading and trailing spaces |
| `s.replace(old, new)` | Replaces old with new |
| `s.split(sep)` | Splits string by separator (default is space) |
| `"sep".join(iterable)` | Joins elements with separator |
| `s.find(sub)` | Returns first index of sub (or −1 if not found) |
| `s.count(sub)` | Counts occurrences of sub |
| `s.startswith(sub)` | Checks if string starts with sub (True/False) |
| `s.endswith(sub)` | Checks if string ends with sub (True/False) |

### 5. List commands
| Command | Use |
|---|---|
| `lst.append(x)` | Adds x at the end |
| `lst.insert(i, x)` | Inserts x at index i |
| `lst.extend(iterable)` | Extends list by adding elements from iterable |
| `lst.remove(x)` | Removes element x |
| `lst.pop(i)` | Removes and returns element at index i (default last) |
| `lst.clear()` | Removes all elements |
| `lst.index(x)` | Returns index of first occurrence of x |
| `lst.count(x)` | Counts occurrences of x |
| `lst.sort()` | Sorts the list in place |
| `lst.reverse()` | Reverses the list |

### 6. Dictionary commands
| Command | Use |
|---|---|
| `d.keys()` | Returns all keys |
| `d.values()` | Returns all values |
| `d.items()` | Returns key-value pairs |
| `d.get(key)` | Returns value for key (None if not found) |
| `d.update(d2)` | Updates dictionary with d2 key-value pairs |
| `d.pop(key)` | Removes key and returns its value |
| `d.popitem()` | Removes and returns last inserted key-value pair |
| `d.clear()` | Removes all items |

### 7. Set commands
| Command | Use |
|---|---|
| `s.add(x)` | Adds element x |
| `s.update(iterable)` | Adds elements from iterable |
| `s.remove(x)` | Removes element x (raises error if not found) |
| `s.discard(x)` | Removes element x (no error if not found) |
| `s.pop()` | Removes an arbitrary element |
| `s.clear()` | Removes all elements |
| `s.union(s2)` | Returns union of two sets |
| `s.intersection(s2)` | Returns intersection |
| `s.difference(s2)` | Returns difference (s − s2) |

### 8. Comparison operators
| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

> **Tips:** Practise these commands daily. The more you practise, the better you'll become!
> *"Code is like humor. When you have to explain it, it's bad."* — Cory House
> **Remember:** Understanding commands is the first step to becoming a Python Pro!

## 57. 40 Essential Python One-Liners

*(From "40 Essential Python Techniques Every Developer Needs" — AI without the PhD series
by Robbert van Vlijmen.)*

### Functional
| # | Technique | One-liner |
|---|---|---|
| 1 | **Range Sum** — calculate totals fast | `sum(range(1,101))` |
| 2 | **Swap** — swap variables instantly | `a, b = b, a` |
| 3 | **All** — verify every element | `all(x > 0 for x in lst)` |
| 4 | **Any** — check at least one | `any(x > 0 for x in lst)` |
| 5 | **Reduce** — sum iterable data | `reduce(lambda a, b: a + b, lst)` |
| 6 | **Filter** — filter unwanted items | `list(filter(None, lst))` |
| 7 | **Map** — transform each element | `list(map(str, lst))` |
| 8 | **Lambda** — define inline function | `f = lambda x: x * 2` |

### Files
| # | Technique | One-liner |
|---|---|---|
| 9 | **Read CSV** — read CSV faster | `pd.read_csv(f)` |
| 10 | **File Exists** — find file quickly | `os.path.exists(f)` |
| 11 | **List Files** — directory contents | `os.listdir(".")` |
| 12 | **Write JSON** — save data easily | `json.dump(data, open(f, "w"))` |
| 13 | **Read JSON** — load JSON easily | `json.load(open(f))` |
| 14 | **Line Count** — count file lines | `sum(1 for _ in open(f))` |
| 15 | **Write File** — write text quickly | `open(f, "w").write(text)` |
| 16 | **Read File** — read entire file | `open(f).read()` |

### Dicts
| # | Technique | One-liner |
|---|---|---|
| 17 | **Max by Value** — find highest value | `max(d, key=d.get)` |
| 18 | **Filter** — filter dictionary entries | `{k: v for k, v in d.items() if v > 0}` |
| 19 | **Values** — get all values | `list(d.values())` |
| 20 | **Keys** — get all keys | `list(d.keys())` |
| 21 | **Get Default** — retrieve safely | `d.get(k, 0)` |
| 22 | **Invert** — swap keys and values | `{v: k for k, v in d.items()}` |
| 23 | **Merge** — merge dictionaries | `{**d1, **d2}` |
| 24 | **Comprehension** — build collections | `{k: v for k, v in pairs}` |

### Lists
| # | Technique | One-liner |
|---|---|---|
| 25 | **Zip** — combine iterables together | `list(zip(a, b))` |
| 26 | **Enumerate** — iterate with index | `[(i, v) for i, v in enumerate(lst)]` |
| 27 | **Reverse** — reverse efficiently | `lst[::-1]` |
| 28 | **Sort** — return sorted list | `sorted(lst)` |
| 29 | **Unique** — remove duplicates | `list(set(lst))` |
| 30 | **Max/Min** — find extremes | `max(lst), min(lst)` |
| 31 | **Flatten** — flatten nested lists | `[x for sub in lst for x in sub]` |
| 32 | **Comprehension** — create using comprehension | `[x**x for x in range(5)]` |

### Strings
| # | Technique | One-liner |
|---|---|---|
| 33 | **f-string** — format readable text | `f"{name} is {age}"` |
| 34 | **Title Case** — capitalize each word | `s.title()` |
| 35 | **Is Palindrome** — check palindrome | `s == s[::-1]` |
| 36 | **Count Char** — count character frequency | `s.count("a")` |
| 37 | **Replace** — replace text easily | `s.replace("a", "b")` |
| 38 | **Strip Spaces** — remove extra spaces | `s.strip()` |
| 39 | **Join** — concatenate strings | `",".join(lst)` |
| 40 | **Uppercase** — convert to uppercase | `s.upper()` |

## 58. Practice Exercises

Work through these in order. Do not look at solutions until you've tried.

**Level 1 — Basics**
1. Print "Hello, World!"
2. Ask the user for their name and greet them.
3. Ask for two numbers and print their sum, difference, product and quotient.
4. Convert a temperature from Celsius to Fahrenheit.
5. Given a number, print whether it is even or odd.

**Level 2 — Control flow**
6. Print the numbers 1 to 10 using a `for` loop, then again using a `while` loop.
7. Print the multiplication table of a number the user enters.
8. Print numbers 1 to 20, skipping multiples of 3 (use `continue`).
9. Find the first number greater than 100 that is divisible by 7 (use `break`).
10. Grade calculator: `>=90` A, `>=75` B, `>=50` C, else F.
11. Print a right triangle of stars using nested loops.

**Level 3 — Data structures**
12. Reverse a string without using a loop.
13. Check whether a string is a palindrome.
14. Count how many times each character appears in a string.
15. Given a list of numbers, find the max, min and sum without built-ins, then with them.
16. Remove duplicates from a list.
17. Given two lists, produce a list of items in both (try it with sets too).
18. Build a dictionary of student names → marks; print the top scorer.
19. Flatten a nested list `[[1,2],[3,4],[5]]` into `[1,2,3,4,5]`.
20. Rewrite exercises 15–19 using comprehensions where possible.

**Level 4 — Functions**
21. Write `is_prime(n)`.
22. Write `factorial(n)` both iteratively and recursively.
23. Write a function with a default argument and call it both ways.
24. Write a function accepting `*args` that returns the average.
25. Write a function accepting `**kwargs` that prints a formatted profile.
26. Rewrite `is_even` as a lambda, then use it with `filter()`.

**Level 5 — Files & errors**
27. Write a list of names to a file, one per line; read it back.
28. Write a program that asks for a number and handles both `ValueError` and
    `ZeroDivisionError`.
29. Write a function that reads a file and returns `"File not found"` instead of crashing.

**Level 6 — OOP**
30. Create a `Student` class with name, roll number and marks, and a method to print details.
31. Add encapsulation: make `marks` private with a getter and a validating setter.
32. Create `Shape` with `area()`; subclass into `Circle` and `Rectangle`.
33. Create `Vehicle` → `Car`, `Bike` with overridden `start()`.
34. Create a `Payment` abstract base class with `CreditCard`, `UPI`, `Wallet`.
35. Build a mini library system: `Book`, `Member`, `Library` — borrow and return books,
    using all four pillars.

## 59. Suggested Learning Path

**Week 1 — Foundations**
Parts 1 & 2. Install Python and VS Code. Write and run 20 small scripts. Get comfortable
with `print()`, `input()`, variables, types and operators. Exercises 1–5.

**Week 2 — Control flow**
Part 3. `if/elif/else`, `while`, `for`, `range()`, `break`/`continue`/`pass`, nested loops.
Exercises 6–11. Do not move on until loops feel automatic.

**Week 3 — Data structures**
Part 4. Strings and their methods first, then lists, tuples, sets, dictionaries. Learn the
comparison table by heart — it is asked in nearly every interview. Exercises 12–20.

**Week 4 — Functions**
Part 5. Parameters vs arguments, default/keyword/variable-length arguments, `return`,
scope, lambda + map/filter/reduce. Exercises 21–26.

**Week 5 — Organizing code, files, errors**
Parts 6 & 7. Write your own module and import it. Build a small package. Practise
`try/except/else/finally`. Exercises 27–29.

**Week 6 — OOP**
Part 8. Class vs object first, then `self`/`__init__`, then the four pillars one at a time.
Finish with the two worked systems and the four design scenarios. Exercises 30–35.

**Week 7+ — Consolidate**
- Work through `PYTHON-INTERVIEW-QUESTIONS.md`.
- Re-implement one of the worked systems from scratch without looking.
- Pick a small real project: a CLI to-do app, a file organizer, a CSV report generator.

**Habits that make the difference**
- Type code out by hand rather than copy-pasting it.
- Read the error message before doing anything else — Python's errors are informative.
- Follow **PEP 8**: `snake_case` for variables and functions, `PascalCase` for classes,
  4-space indentation, meaningful names.
- Use `print()` and `type()` liberally while learning; move to a debugger later.
- Explain a concept out loud as if teaching someone. Gaps surface immediately.

---

*Compiled from all 27 files in `pythonoopsfolder`. Source files were read only and left
unmodified.*
