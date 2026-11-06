---
title: python-syntax-reference
topic: python-data
source_type: my-notes
source_file: python-syntax-reference.md
---

# Complete Python Notes
---

# Chapter 1: Introduction to Python

## What is Python?
Python is a popular, high-level, interpreted programming language known for its simplicity and readability. It is used for web development, data science, AI, automation, and more.

## History
| Year | Event |
|---|---|
| 1989 | Created by Guido van Rossum at CWI, Netherlands |
| 1991 | Python 0.9.0 released, with classes and functions |
| 2000 | Python 2.0 released, added list comprehensions and garbage collection |
| 2008 | Python 3.0 released, improved language constructs and better Unicode support |

## Features
- **Easy to learn:** simple, easy-to-understand syntax.
- **Readable:** code is clear and reads like English.
- **Interpreted:** executes code line by line, with no separate compile step.
- **Cross-platform:** runs on Windows, Mac and Linux.
- **Large standard library:** a rich set of modules and functions for many tasks.
- **Dynamically typed:** you don't declare variable types explicitly.
- **Open source:** free, with a large community.

## Advantages and disadvantages
| Advantages | Disadvantages |
|---|---|
| Simple and easy to learn: reads like English | Slower execution: interpretation is slower than compiled languages |
| Extensive libraries for many tasks | Memory consumption: high usage due to dynamic nature |
| Versatile: web, data science, AI | Not ideal for mobile apps |
| Great community support | GIL (Global Interpreter Lock) limits performance in multi-threaded environments |
| Cross-platform | |
| High-level: easy to write and understand | |

## Python vs other languages
Python has simpler, easy-to-learn syntax, is interpreted with dynamic typing, has a large standard library, and has great libraries for AI, data science and web. Other languages (C, C++, Java) offer faster execution, static typing, better mobile development, and more control over memory.

## Applications
- **Web development:** websites and web apps with Django and Flask.
- **Data science:** analysis and visualization with Pandas, NumPy, Matplotlib.
- **AI and ML:** models and algorithms with TensorFlow, Keras, Scikit-learn.
- **Automation:** repetitive tasks, scripting, task scheduling.
- **Game development:** games and graphical apps with Pygame and Panda3D.

---

# Chapter 2: Installation and Setup

## Installing Python
**Windows:**
1. Download the installer from python.org (latest version).
2. Run the downloaded file and follow the setup wizard.
3. Tick **"Add Python to PATH"** during installation.

**Linux:** use the package manager.
```bash
sudo apt-get update            # Debian/Ubuntu
sudo apt-get install python
sudo dnf install python3       # Red Hat/Fedora
```

## Python interpreter
The interpreter is a program that executes Python code. It converts Python scripts into machine-readable code. Running `python` opens an interactive shell with the `>>>` prompt:
```
>>> print("Hello, Python!")
```

## Running Python programs
Programs are run by an interpreter that reads and executes the code. An IDE (Integrated Development Environment) is software that provides tools to write, edit and run Python code. Three popular ones:
- **IDLE:** basic and simple, comes with Python by default.
- **VS Code:** lightweight and customizable, with many extensions for Python.
- **PyCharm:** professional IDE by JetBrains, feature-rich with code suggestions, debugging and more.

## First program
```python
# First Python Program
print("Hello, World!")        # Output: Hello, World!
```
`print()` displays text in the output.

## Comments
Comments are lines that are not executed. They explain the code and make it more readable.
```python
# This is a single-line comment

"""
Triple-quoted strings can be used for
multi-line comments.
"""
```

---

# Chapter 3: Python Basics

## Keywords and identifiers
- **Keywords** are reserved words that cannot be used as identifiers: `if, else, for, while, def, import, class, None ...`. They cover conditionals, loops, function definitions and more.
- **Identifiers** are user-defined names for variables, functions, classes and more.

Naming rules:
- Start with a letter (a-z, A-Z) or an underscore `_`.
- No spaces.
- No special characters (`$ @ % &`).
- Identifiers are case-sensitive.

```python
# Valid
my_variable, count123, data, sum_total
# Invalid
2nd_name, my-var, for*count
```

## Variables
Variables store data values (numbers, strings, lists, etc.) in memory. You don't declare the type, because Python is dynamically typed.
```python
name = "Alice"
age = 25
height = 5.7
```

## Data types overview
A data type classifies the kind of value a variable holds.
```python
x = 10                       # int
y = 3.14                     # float
name = "Alice"               # str
numbers = [1, 2, 3]          # list
point = (3, 4)               # tuple
person = {"name": "Bob", "age": 30}   # dict
```
**[Fix]** The original labels the dict example as a tuple.

## Type casting
Type casting converts a value from one data type to another with built-in functions `int()`, `float()`, `str()`. It is useful when you need to operate between different data types.
```python
original_str = "123"
number = int(original_str)    # 123

age = 25
age_str = str(age)            # "25"

float("3.14")                 # 3.14
```

## Input and output
**`print()`** outputs data to the screen. It can print strings, numbers and more.
```python
print("Hello, Python!")           # Hello, Python!
print("The answer is", 42)        # The answer is 42   (commas separate items)
name = "Alice"
print(f"Hello, {name}!")          # f-string formatting
```

## Indentation
Indentation defines the structure of code. Python uses four spaces to indicate code blocks. It is essential for loops, conditionals and function definitions. Incorrect indentation causes errors.
```python
# Correct
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Incorrect
if age >= 18:
print("Adult")      # IndentationError: expected an indented block
```

---

# Chapter 4: Python Data Types

## Built-in data types
The main numeric types are `int`, `float` and `complex`. There is also a Boolean type.

| Type | Meaning | Example |
|---|---|---|
| `int` | integer values | `a = 10`, `b = -25` |
| `float` | floating-point numbers (decimals) | `c = 3.14`, `d = 0.5` |
| `complex` | complex numbers with a real and imaginary part | `z = 2+3j`, `w = -0.5-1.5j` |
| `bool` | true or false values | `p = True`, `q = False` |
| `str` | a sequence of characters in quotes, stores text | `"Alice"`, `"Hello, World!"` |
| `NoneType` | absence of a value, single value `None` | `x = None` |

---

# Chapter 5: Operators

## Arithmetic operators
They perform basic mathematical operations.

| Operator | Description | Example (x=7, y=5) | Result |
|---|---|---|---|
| `+` | Addition | `x + y` | 12 |
| `-` | Subtraction | `x - y` | 2 |
| `*` | Multiplication | `x * y` | 35 |
| `/` | Division | `x / y` | 1.4 |
| `%` | Modulus (remainder) | `x % y` | 2 |
| `**` | Exponentiation | `x ** y` | 16807 |
| `//` | Floor division | `x // y` | 1 |

## Relational (comparison) operators
They compare two values and return a Boolean (`True` or `False`).

| Operator | Description | Example (x=7, y=5) | Result |
|---|---|---|---|
| `==` | Equal to | `x == y` | False |
| `!=` | Not equal to | `x != y` | True |
| `>` | Greater than | `x > y` | True |
| `<` | Less than | `x < y` | False |
| `>=` | Greater than or equal | `x >= y` | True |
| `<=` | Less than or equal | `x <= y` | False |

**[Fix]** The original prints `False` for `x >= y`, but with x=7, y=5 it is `True`.

## Logical operators
They combine conditional statements.

| Operator | Example (a=5, b=10) | Result |
|---|---|---|
| `and` | `a < 5 and b > 10` | False |
| `or` | `a < 5 or b > 10` | False |
| `not` | `not a == 5` | False |

## Assignment operators
They assign values to variables.

| Operator | Meaning | Example |
|---|---|---|
| `=` | assign | `x = 5` |
| `+=` | add | `x += 3` is `x = x + 3` |
| `-=` | subtract | `x -= 2` |
| `*=` | multiply | `x *= 4` |
| `/=` | divide | `x /= 5` |
| `%=` | modulus | `x %= 2` |
| `**=` | exponent | `x **= 3` |
| `//=` | floor divide | `x //= 3` |

## Bitwise operators
They operate on the bits of integers, bit by bit.

| Operator | Meaning | Example |
|---|---|---|
| `&` | AND | `5 & 3 = 1` |
| `\|` | OR | `5 \| 3 = 7` |
| `^` | XOR | `5 ^ 3 = 6` |
| `~` | NOT | `~5 = -6` |
| `<<` | Left shift | `5 << 1 = 10` |
| `>>` | Right shift | `5 >> 1 = 2` |

## Membership operators
They test whether a value is present in a sequence (list, string, etc.).
- `in`: True if the value is found. `'a' in "apple"` gives True.
- `not in`: True if the value is not found. `'x' not in [1, 2, 3]` gives True.

## Identity operators
They compare the memory location of two objects.
- `is`: True if both variables refer to the same object.
- `is not`: True if they do not refer to the same object.
```python
x = [1, 2, 3]
y = x
x is y            # True
a = [1, 2, 3]
b = [1, 2, 3]
a is not b        # True (equal values, different objects)
```
**[Fix]** The original's identity table has copy-pasted arithmetic rows.

## Operator precedence
Precedence determines the order of operations. Higher precedence is evaluated first. From high to low:
1. `**` exponentiation
2. `* / // %` multiplication, division, floor division, modulus
3. `+ -` addition, subtraction
4. Comparisons and identity (`== != < > <= >= is`), then assignment

Example: `10 - 3*2 // 5` is evaluated as `10 - ((3*2) // 5) = 10 - (6//5) = 10 - 1 = 9`.

---

# Chapter 6: Control Flow

## Conditional statements
They let you make decisions based on conditions.

**`if`** runs a block only when the condition is True.
```python
age = 18
if age >= 18:
    print("You are an adult.")
```

**`if-else`** runs one block if the condition is True and another if it is False.
```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Nested `if`** is an `if` inside another `if`, to check multiple conditions.
```python
num = 15
if num > 10:
    print("Value is greater than 10.")
    if num > 5:
        print("Value is also greater than 5.")
else:
    print("Value is 5 or less.")
```
(`elif` is standard Python for chaining conditions: `if ... elif ... else`.)

## Loops
**`for` loop** iterates over a sequence (list, tuple, string).
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)
```

**`while` loop** executes a block while the condition remains True.
```python
count = 0
while count < 3:
    print(count)          # 0 1 2
    count += 1
```

**Nested loops** are a loop inside another loop.

## Loop control statements
- **`break`** terminates the loop early.
- **`continue`** skips the rest of the current iteration and goes to the next.
- **`pass`** is a placeholder for code to be added later. It does nothing.

```python
for i in range(5):
    if i == 3:
        break
    print(i)              # 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)              # 0 1 2 4

for i in range(5):
    if i == 3:
        pass              # does nothing, loop carries on
    print(i)              # 0 1 2 3 4
```

---

# Chapter 7: Strings

## Creation
A string is a sequence of characters enclosed in quotes. Single, double or triple quotes work. Triple quotes allow multi-line strings.
```python
name = "Alice"
greeting = 'Hello, World!'
text = """This is
multi-line"""
```

## Indexing and slicing
Strings are indexed from 0. Negative indices count from the end.
```python
text = "Python"
text[0]       # 'P'       first character
text[-1]      # 'n'       last character
text[0:2]     # 'Py'      index 0 up to 2 (exclusive)
text[1:]      # 'ython'   from index 1 to the end
text[-3:]     # 'hon'     last three characters
text[::2]     # 'Pto'     whole string with step 2
```
**[Fix]** The original's `text[:2]` row describes "step 2". That is `text[::2]`.

## String methods
Built-in functions that manipulate string data: change case, remove whitespace, replace parts.
```python
"hello world".upper()            # "HELLO WORLD"
"Hello World".lower()            # "hello world"
"  python  ".strip()             # "python"
"bananas".replace("ban", "man")  # "mananas"
```

## String formatting
Formatting builds strings by inserting variables into templates.
```python
name = "Alice"; age = 25

# format() method
"My name is {} and I am {} years old.".format(name, age)

# f-string
f"My name is {name} and I am {age} years old."
# Output: My name is Alice and I am 25 years old.
```

## Escape characters
Special characters that start with a backslash `\`.

| Character | Description |
|---|---|
| `\n` | new line |
| `\t` | tab |
| `\'` | single quote |
| `\"` | double quote |

```python
text = "Hello,\nThis is a new line."
print(text)
# Hello,
# This is a new line.
```

## String functions
Built-in functions that operate on string data.
```python
amt = "Simple123"
length = len(amt)       # 9
```

## Immutability
Strings are immutable: they cannot be changed after creation. To modify one, create a new string.
```python
greeting = "Hello"
greeting[0] = "J"       # TypeError
greeting = "J" + greeting[1:]   # "Jello" (new string)
```
**[Fix]** The original shows "Jello" as the output of the failing line. The assignment raises an error.

---

# Chapter 8: Lists

## Creating lists
Lists are created with square brackets `[]` and can store items of any data type.
```python
numbers = [1, 2, 3, 4, 5]
mixed_list = ["Python", 42, 3.14, True]     # str, int, float, bool
fruits = ["apple", "banana", "cherry"]
```

## Indexing and slicing
Lists use zero-based indexing. Slicing accesses a range. Negative indices start at -1 for the last element. `list[start:stop]` stops at the index before `stop`.
```python
colors = ["red", "green", "blue", "yellow", "purple"]
colors[0]       # "red"
colors[1:4]     # ["green", "blue", "yellow"]
colors[-1]      # "purple"
```

## List methods
```python
fruits = ["apple", "banana"]
fruits.append("cherry")     # add to end -> ["apple", "banana", "cherry"]

fruits = ["apple", "orange", "banana", "cherry"]
fruits.remove("orange")     # remove by value -> ["apple", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]
fruits.index("banana")      # 1  (position of a value)
```

## Nested lists
Lists can contain other lists (lists within lists).
```python
matrix = [[1, 2, 3], [4, 5, 6]]
matrix[1]       # [4, 5, 6]
matrix[1][2]    # 6
```

## List comprehension
A concise way to create lists, useful for transforming or filtering elements.
```python
squares = [x**2 for x in range(5)]                 # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]       # [0, 2, 4, 6, 8]
```

## List vs array
| Aspect | List | Array (NumPy) |
|---|---|---|
| Availability | Implemented in Python natively | Requires the NumPy package |
| Data types | Flexible, can store different types | Fixed data type for all elements |
| Use | General-purpose | Efficient for numerical operations |

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)       # [1 2 3 4 5]
```

---

# Chapter 9: Tuples

## Creating tuples
Tuples are ordered, **immutable** collections, created with parentheses.
```python
numbers = (1, 2, 3, 4, 5)
single_element = (42,)       # a comma is required for a single-element tuple
```
**[Fix]** The original's first tuple example is an invalid list comprehension.

## Tuple operations
Tuples support indexing and slicing like lists, and can be combined. They are immutable, so they cannot be changed after creation. They can be used as dictionary keys (lists can't).

## Tuple methods
Tuples have only two methods, used to gather information.

| Method | Description |
|---|---|
| `count()` | returns the number of occurrences of a value |
| `index()` | returns the index of the first occurrence of a value |

```python
numbers = (1, 2, 3, 3, 2, 4, 2)
numbers.count(2)         # 3

numbers = (10, 20, 30, 40, 50)
numbers.index(40)        # 3
```

## Packing and unpacking
```python
packed = 1, 2, 3, 4, 5          # packing -> (1, 2, 3, 4, 5)
a, b, c, d, e = packed          # unpacking
first, *rest = (1, 2, 3, 4, 5)  # first = 1, rest = [2, 3, 4, 5]  (*rest collects the remainder)
```

## Tuple vs list
| Feature | Tuple | List |
|---|---|---|
| Definition | `tuple1 = (1, 2, 3)` | `list1 = [1, 2, 3]` |
| Mutability | Immutable | Mutable |
| Methods | `count()`, `index()` | `append()`, `extend()`, `pop()` |
| Usage | Generally for fixed or read-only collections | Dynamic collections |

```python
tuple1 = (1, 2, 3)
tuple1.append(4)      # AttributeError: 'tuple' object has no attribute 'append'

list1 = [1, 2, 3]
list1.append(4)       # [1, 2, 3, 4]
```

---

# Chapter 10: Sets

## Creating sets
A set is a collection of **unique, unordered** elements. Create with `set()` or curly braces `{}`.
```python
set1 = set([1, 2, 3, 4])    # using set()
set2 = {5, 6, 7, 8}         # using braces
```

## Properties
- Elements are unordered. Duplicates are not allowed.
- Sets are mutable: you can add or remove elements.
- `len()` gives the number of elements: `len(set2)` is 4.

## Methods
- `add(x)` adds element `x`.
- `remove(x)` removes `x`. Raises `KeyError` if not found.
- `union(set2)` returns a new set with elements from both.
- `intersection(set2)` returns a new set with elements common to both.

## Set operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 | set2      # union: all unique elements       -> {1, 2, 3, 4, 5, 6}
set1 & set2      # intersection: common elements    -> {3, 4}
set1 - set2      # difference: in set1, not set2    -> {1, 2}
```

## Frozenset
An immutable version of a set. It acts like a set but cannot be modified.
```python
fs = frozenset([1, 2, 3, 4])
```

---

# Chapter 11: Dictionaries

## What is a dictionary?
A collection of **key-value pairs** that is mutable. It is defined with curly braces `{}`, with keys and values separated by colons and pairs separated by commas.

## Creating and accessing
```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
student_scores = {"Math": 85, "English": 92, "History": 78}

print(my_dict["name"])              # Alice
print(student_scores["Math"])       # 85
```

## Methods: keys, values, items
```python
student = {"name": "Alice", "age": 25, "city": "New York"}

student.keys()     # dict_keys(['name', 'age', 'city'])        all keys
student.values()   # dict_values(['Alice', 25, 'New York'])    all values
student.items()    # dict_items([('name','Alice'), ('age',25), ('city','New York')])   key-value tuples
```

## Nested dictionaries
Dictionaries within dictionaries, useful for complex data hierarchies.
```python
classrooms = {
    "class1": {
        "teacher": "Mr. Smith",
        "students": ["Alice", "Bob", "Charlie"]
    },
    "class2": {
        "teacher": "Ms. Johnson",
        "students": ["David", "Eva", "Frank"]
    }
}
print(classrooms["class1"]["teacher"])               # Mr. Smith
classrooms["class2"]["students"].append("Grace")     # update nested list
```

## Dictionary comprehension
Creates dictionaries concisely by iterating over an iterable and applying an expression.
```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional dictionary comprehension
evens = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

# Chapter 12: Functions

## What is a function?
A reusable block of code that performs a specific task. Functions break a program into smaller, manageable, reusable parts.

## Defining and calling
Use `def`, the function name, parentheses, and a colon.
```python
def greet():
    print("Hello, world!")

greet()                   # Hello, world!

def add(a, b):
    return a + b

result = add(5, 7)
print(result)             # 12
```

## Function arguments
**Positional:** arguments are matched by their position in the call.
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Alice", 25)        # Hello Alice, you are 25 years old.
```

**Keyword:** arguments are passed by name, in any order.
```python
greet(age=30, name="Bob")  # Hello Bob, you are 30 years old.
```

**Default:** a parameter has a fallback value if none is passed.
```python
def greet(name, age=20):
    print(f"Hello {name}, you are {age} years old.")
greet("Charlie")           # Hello Charlie, you are 20 years old.
greet("Dana", 35)          # Hello Dana, you are 35 years old.
```

**Variable-length:**
- `*args`: lets a function accept an arbitrary number of non-keyword (positional) arguments.
- `**kwargs`: lets a function accept an arbitrary number of keyword arguments.
```python
def greet(*names):
    for name in names:
        print(f"Hello {name}")
greet("Alice", "Bob", "Charlie")

def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
describe(name="Alice", age=25, city="New York")
# name: Alice / age: 25 / city: New York
```

## Return statement
`return` exits the function and sends a value back to the caller. A function can return multiple values, packed as a tuple.
```python
def add(a, b):
    return a + b
result = add(3, 5)         # 8

def get_stats(numbers):
    return len(numbers), sum(numbers), min(numbers)

length, total, minimum = get_stats([4, 8, 6, 2])
# length: 4, total: 20, minimum: 2
```

## Lambda functions
Small, anonymous, single-line functions defined with the `lambda` keyword. They have no name and are used for short, simple operations.
```python
add = lambda a, b: a + b
add(3, 5)                  # 8

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))   # [1, 4, 9, 16, 25]
```

## Recursion
A function calling itself to solve a problem. Each call addresses a smaller subproblem, converging on a **base case**, the condition that stops the recursion.
```python
def factorial(n):
    if n == 0:             # base case
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)               # 120
```

## Docstrings
Triple-quoted strings that document a function, method or class. They explain what it does. Use triple double quotes for multi-line docstrings.
```python
def greet(name):
    """This function greets a person by name."""
    return f"Hello {name}!"

print(greet.__doc__)       # This function greets a person by name.
```

---

# Chapter 13: Modules and Packages

## What is a module?
A file containing Python code (functions, variables, classes). Modules organize code and allow reuse.

## Importing
```python
import math                     # import the entire module
from math import sqrt, pi       # import only specific names
import random as rnd            # import with an alias

print(math.sqrt(16))            # 4.0
print(sqrt(25))                 # 5.0
print(rnd.randint(1, 10))       # random integer between 1 and 10
```

## Built-in modules
Python ships with many modules that extend its functionality (`math`, `random`, `os`, `sys`, `datetime`, `re`, etc.).

## User-defined modules
Write Python code and save it as a `.py` file.
```python
# greetings.py
def hello(name):
    print(f"Hello, {name}!")
```
```python
import greetings
greetings.hello("Alice")        # Hello, Alice!
```

## Packages
A package is a collection of modules in a directory that includes a special `__init__.py` file.
```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```
```python
import mypackage.module1
mypackage.module1.hello()
```

## `__name__ == "__main__"`
`__name__` is set to `"__main__"` when the file is executed directly, not imported. This lets a module run code only when run as a script.
```python
# mymodule.py
def main():
    print("This is the main function.")

if __name__ == "__main__":
    main()
```

---

# Chapter 14: File Handling

## Overview
Reading from and writing to files. File types:

| Type | Description |
|---|---|
| Text files (`.txt`) | plain text data |
| Binary files (`.bin`, `.dat`) | binary data (images, videos, executables) |

## Opening and closing
```python
file = open("example.txt", "r")    # open in read mode
content = file.read()              # read the content
file.close()                       # close the file
```

## File modes
| Mode | Meaning |
|---|---|
| `r` | Read (default) |
| `w` | Write. Creates the file if missing, **truncates** it if it exists |
| `a` | Append, writes at the end |
| `x` | Create new file, fails if it exists |
| `r+` | Read and write |
| `w+` | Write and read (truncates) |
| `b` | Binary mode (combine, e.g. `rb`) |

## Reading and writing
```python
# Reading
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Writing
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
```

## The `with` statement
Used for resource management. It ensures a resource (like a file) is properly closed after its block, even if an error occurs.
```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

## CSV and text files
```python
# Reading a CSV (csv module)
import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)            # each row as a list

# Writing a text file line by line
lines = ["First line", "Second line", "Third line"]
with open("file.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
```

---

# Chapter 15: Exception Handling

## Errors vs exceptions
- **Errors** are problems that make a program stop unexpectedly.
- **Exceptions** are events that can be detected and handled by the program.

## Types of errors
- **Syntax errors:** mistakes in the code itself, found before it runs.
- **Runtime errors:** occur during execution.
```python
x = 5
y = 0
print(x / y)          # ZeroDivisionError (runtime error)
```

## try-except
Catches and handles exceptions.
```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Handling a specific exception type
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a number.")
```

## else
Runs if **no exception** was raised in the `try` block.
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful:", result)     # 5.0
```

## finally
Runs **regardless** of whether an exception occurred. Typically used for cleanup.
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("File closed")
```

## Custom exceptions
Define your own by creating a class that inherits from `Exception`.
```python
class MyCustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise MyCustomError("Value cannot be negative")

try:
    check_value(-5)
except MyCustomError as e:
    print(e)            # Value cannot be negative
```

---

# Chapter 16: Object-Oriented Programming

## Class and object
OOP is a paradigm based on **objects** that contain data and functions. A **class** is the blueprint. An **object** is an instance of a class.
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")     # creating an object
```
- A class is defined with the `class` keyword.
- `__init__` is the constructor and initializes the object's attributes.
- An object is created by calling the class name with arguments.

## Constructor (`__init__`)
A special method that is called automatically when a new object is created. It initializes the object's attributes. `self` refers to the instance being created and is used to access its attributes and methods.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
```

## Instance variables and methods
Tied to a specific instance. They operate on the instance and access its unique data.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy", 3)
my_dog.bark()            # Buddy barks!
```

## Static and class methods
Bound to the class, not the instance.
```python
# Static method: no self or cls, a utility function
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

MathUtils.add(5, 7)      # 12

# Class method: receives the class (cls), can modify class variables
class Dog:
    species = "Canine"

    @classmethod
    def set_species(cls, species):
        cls.species = species

Dog.set_species("Wolf")
print(Dog.species)       # Wolf
```

## Encapsulation
Restricts direct access to an object's data, promoting controlled access and data hiding. A double underscore marks an attribute as private.
```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())     # 1500
```

## Inheritance
A child class inherits attributes and methods from a parent class. It allows code reuse and extension.
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy")
my_dog.make_sound()      # Buddy barks!
```

## Abstraction
Hides details and shows only essential features. It provides a template for other classes.
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")
```
`@abstractmethod` marks a method that child classes must implement.

## Method overriding
A child class provides its own implementation of a method already defined in the parent.
```python
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")

Dog().make_sound()       # Dog barks.
```

---

# Chapter 17: Advanced Python Concepts

## Iterators
Objects that let you traverse all elements in a collection. An iterator implements two special methods:
- `__iter__()` returns the iterator object itself.
- `__next__()` returns the next value, or raises `StopIteration` when none are left.
```python
numbers = [1, 2, 3]
my_iter = iter(numbers)      # create an iterator
print(next(my_iter))         # 1
print(next(my_iter))         # 2
print(next(my_iter))         # 3
```
`iter()` creates an iterator from a collection. `next()` retrieves the next item or raises `StopIteration`.

## Generators
A simple way to create iterators using functions. They generate values on the fly without storing them in memory. They use `yield`.
```python
def square_numbers(n):
    for i in range(n):
        yield i * i

gen = square_numbers(3)
print(next(gen))     # 0
print(next(gen))     # 1
print(next(gen))     # 4
```
- `yield` is used instead of `return` to produce values over time.
- When `yield` runs, the function's state is saved and the value returned.
- The next value is produced when `next()` is called.
- Generators are memory efficient for large data sets.

## Decorators
Functions that modify the behavior of another function, often to add functionality to existing functions. The `@` syntax applies one.
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

## Closures
An inner function that remembers and can access variables from an enclosing function, even after the outer function has finished.
```python
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

greet = outer_func("Hello!")
greet()                      # Hello!
```

## Shallow copy vs deep copy
- A **shallow copy** creates a new object but inserts references to the objects found in the original.
- A **deep copy** creates a new object and recursively copies nested objects.
```python
import copy
original = [1, [2, 3], 4]
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)

original[1][0] = "changed"
# shallow_copied[1][0] is also "changed" (shares nested objects)
# deep_copied stays [1, [2, 3], 4]
```

## Memory management
Python allocates and deallocates memory efficiently so programs run smoothly. It uses **reference counting**: memory isn't freed until all references are deleted.
```python
data = [1, 2, 3]
ref = data           # ref points to the same list
del data
print(ref)           # [1, 2, 3], still works
```

## Garbage collection
Python automatically reclaims memory by disposing of objects no longer in use.
```python
import gc

class MyClass:
    def __del__(self):
        print("Object deleted")

obj = MyClass()
del obj              # Object deleted
gc.collect()         # force garbage collection
```

---

# Chapter 18: Core Libraries

## math
Mathematical functions.
```python
import math
math.sqrt(16)                      # 4.0     square root
math.factorial(5)                  # 120     factorial
math.pi                            # 3.14159265358979...
math.sin(math.radians(90))         # 1.0     sine takes radians; radians() converts from degrees
```

## random
Random numbers and selections.
```python
import random
random.randint(1, 10)                  # random integer 1..10 inclusive
random.choice(["red", "blue", "green"])  # random item from a list
random.random()                        # random float between 0 and 1
random.sample(range(1, 50), 5)         # 5 unique random numbers between 1 and 49
```

## datetime
Dates and times.
```python
from datetime import datetime, timedelta
now = datetime.now()                          # current date and time
now.strftime("%Y-%m-%d %H:%M:%S")             # formatted string
future_date = now + timedelta(days=5)         # date 5 days from now
```
`strftime()` formats a date as a string. `timedelta` is a duration that can be added to or subtracted from a date.

## os
Interacts with the operating system.
```python
import os
print(os.getcwd())        # current working directory
os.chdir("..")            # change to parent directory
os.mkdir("new_folder")    # create a folder
```

## sys
Access to variables and functions related to the Python interpreter.
```python
import sys
print(sys.version)        # Python version
print(sys.argv)           # command-line arguments, e.g. ['script.py']
```

## time
Time-related functions.
```python
import time
print(time.time())        # current time in seconds since the epoch
time.sleep(2)             # pause for 2 seconds
```

## re
Support for regular expressions (see Chapter 19).
```python
import re
pattern = r"\bhello\b"                  # match "hello" as a whole word
text = "hello world, hello python"
re.findall(pattern, text)               # ['hello', 'hello']
```

---

# Chapter 19: Regular Expressions

## Pattern matching
The `re` module works with regular expressions.
```python
import re
text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())      # Found: rain
```
- `re.search(pattern, string)` finds the first occurrence anywhere. Returns a match object or `None`.
- `re.match(pattern, string)` matches only at the **start** of the string.
- `re.findall(pattern, string)` returns a list of all non-overlapping matches.
- `re.sub(pattern, repl, string)` replaces matches with `repl`.

## Meta characters
Special characters with a unique meaning in regex.

| Character | Description | Example |
|---|---|---|
| `.` | any character except newline | `r"a.c"` matches "abc", "a1c" |
| `^` | start of a string | `r"^hello"` matches "hello world" |
| `$` | end of a string | `r"world$"` matches "hello world" |
| `[ ]` | character class, any one enclosed character | `r"[A-Za-z]"` matches "c" or "D" |
| `\|` | OR | `r"cat\|dog"` matches "I have a cat" or "I have a dog" |
| `*` | zero or more of the preceding | `r"cat*"` matches "ca", "cat", "catt" |
| `+` | one or more of the preceding | `r"cat+"` matches "cat", "catt" |
| `?` | zero or one of the preceding | `r"colou?r"` matches "color" and "colour" |
| `{n}` | exactly n repetitions | `r"\d{3}"` matches "123" |

**[Fix]** The original describes `*` as "zero or more" and `?` as "one or more". The correct meaning of `?` is zero or one.

## Regex functions: search, match, findall
```python
import re
re.search(r"\d+", "123abc456").group()    # '123'   first match anywhere
re.match(r"\d+", "123abc").group()        # '123'   must match at the start
re.findall(r"\d+", "123abc456")           # ['123', '456']
```

## Email and password validation
Regex can validate email addresses and passwords against defined rules.
```python
import re
def validate_email(email):
    pattern = r"^\S+@\S+\.\S+$"
    return re.match(pattern, email) is not None
```
(The notes mention a `validate_password` for password complexity but the code is not legible in the scan.)

---

# Chapter 20: Python with Databases

## Introduction
Databases manage and organize large amounts of data efficiently. They let you store, retrieve and manipulate data.
- **Table:** stores data in rows and columns, like a spreadsheet.
- **Query:** a request to retrieve specific data.
- **CRUD:** Create, Read, Update, Delete, the basic data operations.

## SQLite with Python
SQLite is a lightweight, embedded database library included with Python, ideal for small to medium applications.
```python
import sqlite3
conn = sqlite3.connect("example.db")    # creates example.db if it doesn't exist
cursor = conn.cursor()                  # cursor object executes SQL commands

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")
```
- `id INTEGER PRIMARY KEY`: integer column that uniquely identifies each row.
- `name TEXT`: text column.
- `age INTEGER`: integer column.

## MySQL with Python
MySQL is a popular relational database.
```python
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)
if conn.is_connected():
    print("Connected to MySQL")
```

## CRUD operations
```python
cursor = conn.cursor()

# Create
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 25))
conn.commit()                       # commit saves the transaction

# Read
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()            # fetch all result rows

# Update
cursor.execute("UPDATE users SET age = %s WHERE name = %s", (26, "John"))
conn.commit()

# Delete
cursor.execute("DELETE FROM users WHERE name = %s", ("John",))
conn.commit()
```
Always use `%s` placeholders with a values tuple, not string concatenation. `commit()` is needed after changes to save them.

---

# Chapter 21: Python for Automation

Automation means using Python to perform repetitive tasks automatically, saving time and reducing effort.

## File automation
Manage files and folders without manual work. Use cases: organizing downloads, creating backups, cleaning unused files.
```python
import shutil, os
source_file = "example.txt"
destination_folder = "/path/to/destination/"
shutil.move(source_file, os.path.join(destination_folder, "example.txt"))
```

## Web automation (Selenium basics)
Interacting with websites automatically through code. Selenium can open a browser, visit sites, click buttons and links, fill forms, and scrape basic information.

Workflow: open the browser with WebDriver, load a URL, locate elements (buttons, inputs), then perform actions like click or type.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")
button = driver.find_element(By.ID, "submit-button")
button.click()
```

## Email automation
Send reports, newsletters and updates, or notify when tasks finish.
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "Test Email"
msg["From"] = "myemail@example.com"
msg["To"] = "recipient@example.com"

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login("myemail@example.com", "password")
server.send_message(msg)
```

## Task scheduling
Run scripts automatically at scheduled times, using the `schedule` library.
```python
import schedule, time

def my_task():
    print("Task is running...")

schedule.every().day.at("08:00").do(my_task)   # every day at 8:00 AM

while True:
    schedule.run_pending()
    time.sleep(60)                              # wait one minute
```

---

# Chapter 22: Python for Data Science (Basics)

Python is popular for data science because its libraries make analysis and manipulation easy.

## NumPy
Numerical Python: a library for numerical computation, supporting large multi-dimensional arrays and matrices. Uses: efficient array operations, mathematical functions, random number generation.
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
```

## Pandas
A library for data manipulation and analysis, built on NumPy. It works with structured data such as tables (**DataFrames**).
```python
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Carol"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 65000]
}
df = pd.DataFrame(data)
print(df)
```
Common manipulations: sorting and filtering (e.g. Age > 25).

## Matplotlib
Creates static graphs and visualizations: line plots, scatter plots, histograms.
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
```

## Seaborn
Built on Matplotlib, for more attractive and informative statistical visualizations. It makes beautiful charts easily.
```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
sns.barplot(x="species", y="sepal_length", hue="species", data=df)
plt.show()
```

## Data analysis basics
1. **Collect data:** gather relevant data.
2. **Clean data:** handle missing values, remove duplicates.
3. **Analyze data:** calculate statistics, identify trends.

---

# Chapter 23: Python for Web Development

## Flask (basics)
A lightweight web framework, easy to learn, for creating simple web applications.
- Uses: simple websites, building APIs, prototyping ideas quickly.
- Features: simple and easy setup, built-in development server, extensive documentation.
- Flow: the user requests a page, the Flask server handles it and returns a web page to the browser.

## Django (introduction)
A high-level web framework for building robust, scalable web applications.

| | Flask | Django |
|---|---|---|
| Type | Lightweight | Full framework |
| Use case | Small, simple web apps | Large, robust apps |
| Features | Quick setup, flexible | Built-in admin panel, ORM, URL handling, authentication |

- Django uses an **ORM** for database operations.
- It includes a built-in admin panel and handles URLs and authentication.
```bash
pip install django
django-admin startproject mywebsite
```

## REST APIs
Representational State Transfer APIs let client applications and servers communicate using HTTP methods.
- Use requests and responses over HTTP.
- Support CRUD operations (GET, POST, PUT, DELETE).
- The common data format is **JSON**.
```python
import requests
response = requests.get("https://api.example.com/users/1")
data = response.json()
print(data)
```

## JSON handling
JSON (JavaScript Object Notation) is a lightweight data format for exchanging data between client and server, commonly used with REST APIs.
```python
import json

json_str = '{"name": "Alice", "age": 25, "email": "alice@example.com"}'
data = json.loads(json_str)          # JSON string -> dictionary
print(data["email"])                 # access a value
json.dumps(data)                     # dictionary -> JSON string
```
- `json.loads()` parses a JSON string to a dictionary.
- `json.dumps()` converts a dictionary to a JSON string.

---

# Chapter 24: Python Testing

## Unit testing
Testing individual units of code (like functions) to check they work as expected. It catches errors early and maintains code quality.

## unittest module
A built-in module for creating and running unit tests. Key features: basic testing framework, built-in assertion methods, generates test reports.
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)      # checks 2+3 equals 5

if __name__ == "__main__":
    unittest.main()
```
Run the tests:
```bash
python -m unittest
```
Output: `Ran 1 test in 0.001s ... OK`

## Assertion methods
| Method | Asserts |
|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` is True |
| `assertFalse(x)` | `x` is False |

## Assertions (`assert`)
A built-in check that a condition is True during execution. If False, `AssertionError` is raised and the program stops. Used for debugging and verifying assumptions, and helps catch bugs early.
```python
x = 5
assert x % 2 == 0, "x should be even"
# AssertionError: x should be even
print("x is even")          # not reached
```

## Test cases
Sets of conditions used to check whether a program works correctly. Automated tests in Python often use `unittest`: write a test class, call the function, assert the result, run the tests.

---

# Chapter 25: Interview Preparation

## Time complexity
Measures how long an algorithm takes to run as a function of input size.

| Class | Name | Example |
|---|---|---|
| O(1) | Constant | `arr[0]` |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Finding the max element in an array |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Naive Fibonacci |

## Space complexity
Measures how much memory an algorithm uses as a function of input size. It shows how much extra space a program needs.

## OOP interview questions
- What is Object-Oriented Programming?
- Explain the four pillars of OOP: encapsulation, inheritance, polymorphism, abstraction.
- What is a class? What is an object? What is a constructor?
- What is inheritance? How does polymorphism work?
- What is method overloading and method overriding?
- What is the difference between an abstract class and an interface?

## Common Python interview questions
- What are Python's built-in data types?
- What is a list? Explain list comprehension.
- What is a tuple? How is it different from a list?
- What are dictionaries? How do they work?
- What are `*args` and `**kwargs`?
- What is a lambda function?
- How does exception handling work in Python?
- What are decorators? How are they used?
- How do you manage memory in Python?
- What is the Global Interpreter Lock (GIL)?

---

# Exercises

The original notes have **no practice exercises**. The only question material is the interview list above, which has no answers.

# Gaps in the original notes

Not covered: list methods beyond `append`/`remove`/`index` (e.g. `extend`, `insert`, `pop`, `sort`, `reverse`), dict methods like `get`/`update`/`pop`, `elif` explicitly, `range()` arguments, `enumerate`, `zip`, `filter`, Flask code, and the `validate_password` function.
