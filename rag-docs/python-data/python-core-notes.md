---
title: Python core concepts — study notes
topic: python-data
source_type: my-notes
note_kind: study-notes
---

# Python Core Concepts — Study Notes

## Comments and type conversion

- `#` for single-line comments; triple-quoted strings at the top of a function are **docstrings** (shown by `help()`).
- Conversion: `int("42")`, `float("3.5")`, `str(10)`, `list("abc")`, `bool(0)` → `False`.
- Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`. Everything else is truthy.

## Functions

```python
def greet(name, greeting="Hello", *args, **kwargs):
    return f"{greeting}, {name}!"
```

- **Default arguments** are evaluated once — never use a mutable default like `def f(items=[])`; use `None` and create the list inside.
- `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict.
- `lambda x: x * 2` is a small anonymous function, often used with `sorted(key=...)`, `map`, `filter`.

## Modules and packages

- A **module** is a `.py` file; a **package** is a folder of modules.
- `import math`, `from pathlib import Path`, `import pandas as pd`.
- `if __name__ == "__main__":` runs code only when the file is executed directly, not when imported.

## File handling

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")

with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

- Modes: `"r"` read, `"w"` write (overwrites), `"a"` append, `"b"` binary.
- `with` closes the file automatically, even on errors.
- CSV: the `csv` module (`csv.reader`, `csv.DictWriter`), or pandas for real analysis.

## Exceptions

```python
try:
    value = int(user_input)
except ValueError:
    print("Not a number")
else:
    print("Parsed fine")       # runs only if no exception
finally:
    print("Always runs")
```

Custom exceptions subclass `Exception`:

```python
class InvalidAgeError(Exception):
    pass

if age < 0:
    raise InvalidAgeError("age cannot be negative")
```

Catch specific exceptions; a bare `except:` hides bugs.

## Object-oriented Python

```python
class Account:
    bank_name = "Example Bank"          # class attribute (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner               # instance attribute
        self._balance = balance          # "internal" by convention

    def deposit(self, amount):           # instance method
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    @property
    def balance(self):                   # read-only access
        return self._balance

    @classmethod
    def from_dict(cls, data):            # alternative constructor
        return cls(data["owner"], data.get("balance", 0))

    @staticmethod
    def is_valid_amount(x):              # utility, no self/cls
        return x > 0
```

- **Encapsulation**: Python uses conventions — `_name` means internal, `__name` triggers name mangling.
- **Inheritance and overriding**: `class Savings(Account):` and redefine `deposit`; call the parent with `super().deposit(amount)`.
- **Abstraction**: `from abc import ABC, abstractmethod` defines methods subclasses must implement.
- **Dunder methods**: `__str__`, `__repr__`, `__len__`, `__eq__` customise built-in behaviour.

## Decorators

A decorator wraps a function to add behaviour without changing its code.

```python
import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
        return result
    return wrapper

@timed
def slow_sum(n):
    return sum(range(n))
```

Real-world uses: logging, timing, caching (`functools.lru_cache`), access checks, route registration in web frameworks.

## Closures

An inner function that remembers variables from the enclosing function, even after the outer function returns.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
double(5)   # 10
```

## Shallow vs deep copy

```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)     # new outer list, same inner lists
deep = copy.deepcopy(original)    # everything copied
original[0].append(99)
# shallow[0] is now [1, 2, 99]; deep[0] is still [1, 2]
```

Assignment (`b = a`) copies nothing — both names point to the same object.

## Memory management

- Every value is an object; variables are names pointing to objects.
- CPython uses **reference counting**: an object is freed when no references remain.
- A **cyclic garbage collector** cleans up reference cycles (objects pointing to each other).
- Mutable (list, dict, set) vs immutable (int, str, tuple) matters for copying and default arguments.

## Useful standard-library modules

| Module | Use |
| --- | --- |
| `os` | Environment variables (`os.environ`), file system operations |
| `sys` | Command-line args (`sys.argv`), interpreter info, `sys.path` |
| `time` / `datetime` | Timing, sleeping, dates |
| `pathlib` | Object-oriented file paths |
| `re` | Regular expressions |
| `json` | Read/write JSON |
| `collections` | `Counter`, `defaultdict`, `deque`, `namedtuple` |

## Regular expressions

```python
import re
re.search(r"\d+", "order 1043 shipped")     # first match anywhere → "1043"
re.match(r"\d+", "order 1043")              # only at the start → None
re.findall(r"#(\w+)", "#sql and #python")   # ["sql", "python"]
re.sub(r"\s+", " ", "too    many   spaces")  # collapse whitespace
```

Simple validation patterns:
- Email (basic): `r"^[\w.+-]+@[\w-]+\.[\w.]+$"`
- Strong password: at least 8 chars with a digit, lowercase and uppercase — lookaheads: `r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"`

Use raw strings (`r"..."`) so backslashes aren't interpreted by Python first.

## Talking to MySQL

```python
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="app", password=os.environ["DB_PASS"], database="shop")
cur = conn.cursor()
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Pen", 1.5))
conn.commit()
cur.execute("SELECT id, name FROM products WHERE price < %s", (5,))
for row in cur.fetchall():
    print(row)
conn.close()
```

Always use placeholders (`%s`) instead of string formatting to avoid SQL injection, and `commit()` after writes.
