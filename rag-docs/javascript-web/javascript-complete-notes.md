---
title: JAVASCRIPT-COMPLETE-NOTES
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/JAVASCRIPT-COMPLETE-NOTES.md
---

# JavaScript — Complete Beginner-to-Advanced Notes


> Interview questions have been split into a separate file:
> **`JAVASCRIPT-INTERVIEW-QUESTIONS.md`**

---

## Table of Contents

**PART 1 — FOUNDATIONS**
1. [What JavaScript Is (and its History)](#1-what-javascript-is-and-its-history)
2. [How to Run JavaScript](#2-how-to-run-javascript)
3. [Output Statements & the Console](#3-output-statements--the-console)
4. [Comments](#4-comments)
5. [Variables: var, let, const](#5-variables-var-let-const)
6. [Identifiers & Keywords](#6-identifiers--keywords)
7. [Data Types](#7-data-types)
8. [Type Conversion & Coercion](#8-type-conversion--coercion)
9. [Truthy and Falsy Values](#9-truthy-and-falsy-values)
10. [Operators](#10-operators)

**PART 2 — CONTROLLING THE FLOW**
11. [Conditional Statements](#11-conditional-statements)
12. [The Ternary Operator](#12-the-ternary-operator)
13. [Loops](#13-loops)
14. [break, continue, and Labels](#14-break-continue-and-labels)

**PART 3 — THE BUILDING BLOCKS**
15. [Functions](#15-functions)
16. [Scope, Lexical Environment & the Scope Chain](#16-scope-lexical-environment--the-scope-chain)
17. [Hoisting](#17-hoisting)
18. [Execution Context & the Call Stack](#18-execution-context--the-call-stack)
19. [Closures](#19-closures)
20. [IIFE](#20-iife-immediately-invoked-function-expression)
21. [Higher-Order Functions & Callbacks](#21-higher-order-functions--callbacks)
22. [Recursion](#22-recursion)
23. [Strict Mode](#23-strict-mode)

**PART 4 — DATA STRUCTURES**
24. [Strings](#24-strings)
25. [Template Literals](#25-template-literals)
26. [Arrays](#26-arrays)
27. [Array Methods in Detail](#27-array-methods-in-detail)
28. [Objects](#28-objects)
29. [Object Methods](#29-object-methods)
30. [Destructuring](#30-destructuring)
31. [Spread & Rest Operators](#31-spread--rest-operators)
32. [Set & Map](#32-set--map)
33. [JSON](#33-json)
34. [Date Object](#34-date-object)
35. [Math & Number](#35-math--number)
36. [Regular Expressions](#36-regular-expressions)

**PART 5 — OBJECT-ORIENTED JAVASCRIPT**
37. [The `this` Keyword](#37-the-this-keyword)
38. [call, apply, bind](#38-call-apply-and-bind)
39. [Constructor Functions](#39-constructor-functions)
40. [Prototypes & Prototype Chaining](#40-prototypes--prototype-chaining)
41. [Classes](#41-classes)
42. [Inheritance, Encapsulation, Polymorphism, Abstraction](#42-the-four-oop-pillars-in-javascript)
43. [Static Methods](#43-static-methods)

**PART 6 — THE BROWSER**
44. [The Browser Structure & the Window Object](#44-the-browser-structure--the-window-object)
45. [BOM: Navigator, Screen, History, Location](#45-bom-navigator-screen-history-location)
46. [The DOM](#46-the-dom-document-object-model)
47. [Selecting Elements](#47-selecting-elements)
48. [Reading & Changing Elements](#48-reading--changing-elements)
49. [Creating, Inserting & Removing Elements](#49-creating-inserting--removing-elements)
50. [DOM Traversal](#50-dom-traversal-navigating-the-tree)
51. [Events & Event Handling](#51-events--event-handling)
52. [The Event Object](#52-the-event-object)
53. [Event Propagation: Bubbling & Capturing](#53-event-propagation-bubbling--capturing)
54. [Event Delegation](#54-event-delegation)
55. [Popup Methods: alert, prompt, confirm](#55-popup-methods-alert-prompt-confirm)
56. [Form Validation](#56-form-validation)
57. [Cookies](#57-cookies)
58. [Web Storage: localStorage & sessionStorage](#58-web-storage-localstorage--sessionstorage)

**PART 7 — ASYNCHRONOUS JAVASCRIPT**
59. [Synchronous vs Asynchronous](#59-synchronous-vs-asynchronous)
60. [The Event Loop](#60-the-event-loop)
61. [Callbacks & Callback Hell](#61-callbacks--callback-hell)
62. [Promises](#62-promises)
63. [Promise Combinators](#63-promise-combinators)
64. [async / await](#64-async--await)
65. [The Fetch API](#65-the-fetch-api)

**PART 8 — ERRORS, MODULES & ADVANCED**
66. [Error Handling](#66-error-handling)
67. [Debugging](#67-debugging)
68. [ES6 Modules](#68-es6-modules)
69. [Generators](#69-generators)
70. [Proxy & Reflect](#70-proxy--reflect)
71. [Web Workers](#71-web-workers)
72. [Design Patterns](#72-design-patterns)
73. [Other Web APIs](#73-other-web-apis)
74. [Modern Shortcuts You Should Know](#74-modern-shortcuts-you-should-know)
75. [ES6+ Feature Checklist](#75-es6-feature-checklist)

**PART 9 — PRACTICE**
76. [Full Project: To-Do List App](#76-full-project-a-to-do-list-app)
77. [Learning Roadmap](#77-learning-roadmap)

**PART 10 — PATTERNS & THE REACT BRIDGE**
78. [Async Concurrency Patterns](#78-async-concurrency-patterns)
79. [The JavaScript → React Bridge](#79-the-javascript--react-bridge)

---
---

# PART 1 — FOUNDATIONS

---

## 1. What JavaScript Is (and its History)

### What it is

**JavaScript is a high-level, interpreted, lightweight, dynamic programming language.**

Break that down:

| Term | Plain English |
|---|---|
| **High-level** | You don't manage memory or talk to hardware. You write human-readable instructions. |
| **Interpreted** | No separate "compile" step. The browser reads and runs your code line by line. |
| **Lightweight** | Small language, small runtime, loads fast in a browser. |
| **Dynamically typed** | A variable can hold *any* type of data, and can change type later. You never declare the type. |
| **Case-sensitive** | `myName`, `myname`, and `MyName` are three different things. |
| **Single-threaded** | It does one thing at a time (but has clever tricks for waiting — see the Event Loop). |
| **Not error-free** | It will often run "broken" code without complaining, producing weird results. This is why strict mode exists. |

**What it's for:** HTML gives a page *structure*, CSS gives it *style*, and JavaScript gives it
*behaviour*. It turns a static page into a dynamic one — reacting to clicks, fetching data,
animating, validating forms.

**Where it runs:**
1. Web applications (in every browser)
2. Web servers (via Node.js)
3. Mobile apps (React Native, Ionic)
4. Games
5. Desktop apps (Electron)

### Its history

| Year | Event |
|---|---|
| **1995** | **Brendan Eich**, a programmer at **Netscape**, creates the language in **just 10 days**. |
| 1995 | First name: **Mocha**. Then renamed **LiveScript**. |
| 1995 | Renamed again to **JavaScript** — purely for *marketing*, because Java was popular at the time. |
| 1996 | **Ecma International** (an industry standards association) is founded to standardise it. |
| 1997 | Microsoft copies the features into their own language, **JScript**, for Internet Explorer. The "browser wars" begin. |
| 1997 | To end the chaos, the language is standardised as **ECMAScript (ES1)** so it behaves the same in every browser. |
| 2009 | **ES5** — lots of new features. |
| **2015** | **ES6 (ES2015)** — the *biggest* update ever. This is what people mean by "Modern JavaScript". |
| 2015→ | Ecma's technical committee **TC39** decides to release a new version **every year**: ES2016, ES2017 … ES2024, ES2025. |

> ⚠️ **Very important:** **Java and JavaScript are completely different languages.**
> They have nothing in common except four letters in the name. This is like "car" and "carpet".

**ECMA** = *European Computer Manufacturers Association* (now "Ecma International").
**ECMAScript** = the official *specification* (the rulebook).
**JavaScript** = the *implementation* of that rulebook that you actually write.

> Formula to remember: **JavaScript + ECMA rules → ECMAScript**

### Feature list

1. Object-centred scripting language
2. Client-side technology (runs in the user's browser)
3. Validation of user input
4. `if` / `else` statements
5. Interpreter-centred
6. Ability to use built-in functions
7. Case-sensitive format
8. Lightweight and delicate
9. Looping statements
10. Event handling
11. Cross-platform
12. Backward compatible (old code keeps working in new browsers)

---

## 2. How to Run JavaScript

There are **two ways** to attach JavaScript to a web page.

### 1. Internal JavaScript

Write the code directly inside a `<script>` tag in your HTML, inside `<head>` or `<body>`.

```html
<body>
  <h1>My Page</h1>

  <script>
    console.log("Hello from internal JS!");
  </script>
</body>
```

### 2. External JavaScript

Put the code in a separate `.js` file and link it. **This is the professional way** — it keeps
your structure (HTML) and behaviour (JS) separate, and the file can be cached and reused
across pages.

```html
<!-- index.html -->
<body>
  <h1>My Page</h1>
  <script src="script.js"></script>
</body>
```

```javascript
// script.js
console.log("Hello from external JS!");
```

> 💡 **Place `<script>` just before `</body>`.** If it's in the `<head>`, the script runs
> *before* the HTML elements exist, so `document.getElementById(...)` will return `null`.

### Modules

If you're using `import` / `export` (see [ES6 Modules](#68-es6-modules)), you must add
`type="module"`:

```html
<script type="module" src="app.js"></script>
```

### Semicolons

It is considered mandatory to end every statement with a semicolon `;`.
JavaScript has "Automatic Semicolon Insertion" and will usually forgive you, but relying on
that causes rare, very confusing bugs. **Just use semicolons.**

### Where to see errors

Errors and `console.log` output appear in the browser's **Console**.
To open it: right-click the page → **Inspect** → **Console** tab.
(Or press `F12` / `Cmd+Option+I`.)

---

## 3. Output Statements & the Console

There are several ways to show output. Each behaves differently.

| Method | What it does |
|---|---|
| `console.log()` | Prints to the browser console. **This is what you'll use 99% of the time.** |
| `document.write()` | Writes directly onto the page, with **no space** between calls. |
| `document.writeln()` | Writes onto the page and adds a space/newline character at the end. |
| `alert()` | Shows a blocking popup box. |
| `innerHTML` | Puts HTML content inside an element. |

```javascript
document.write("Hello");
document.write("World");
// Page shows: HelloWorld     ← no space

document.writeln("Hello");
document.writeln("World");
// Page shows: Hello World    ← space added

console.log("Hello World");   // Console shows: Hello World
```

> ⚠️ **Never use `document.write()` in real projects.** If it runs after the page has loaded,
> it wipes the entire document. It appears in old tutorials only.

### The full console family

```javascript
console.log('message', obj);        // normal output
console.info('info message');       // informational
console.warn('warning message');    // yellow warning
console.error('error message');     // red error
console.clear();                    // wipes the console
```

---

## 4. Comments

Comments are notes for humans. JavaScript ignores them completely.

```javascript
// This is a single-line comment

/*
   This is a
   multi-line comment
*/

let x = 10; // comments can also go at the end of a line
```

---

## 5. Variables: var, let, const

A **variable** is a named container that stores a value.

Three vocabulary words you must not mix up:

| Term | Meaning | Example |
|---|---|---|
| **Declaration** | Creating the variable | `var a;` |
| **Initialization** | Giving it its *first* value | `a = 12;` |
| **Assignment** | Giving it a *new* value later | `a = "me";` |

There are **three keywords** to declare variables: `var`, `let`, and `const`.

### `var` — the old way (ES1)

- **Function-scoped** (or global if declared outside a function)
- Can be **re-declared** ✅
- Can be **re-initialized** (reassigned) ✅

```javascript
var greeting = "Hello";
var greeting = "Hi";       // Re-declaration allowed
greeting = "Hey";          // Re-assignment allowed
console.log(greeting);     // "Hey"
```

### `let` — the modern way (ES6)

- **Block-scoped** (only exists inside the `{ }` it was declared in)
- **Cannot** be re-declared in the same scope ❌
- Can be re-assigned ✅

```javascript
let name = "Alice";
// let name = "Bob";       // ❌ Error: Cannot re-declare block-scoped variable 'name'
name = "Charlie";          // ✅ Re-assignment allowed
console.log(name);         // "Charlie"

if (true) {
    let blockScoped = "I'm inside a block";
    console.log(blockScoped);   // ✅ "I'm inside a block"
}
// console.log(blockScoped);    // ❌ Error: blockScoped is not defined
```

### `const` — for values that never change (ES6)

- **Block-scoped**
- **Cannot** be re-declared ❌
- **Cannot** be re-assigned ❌
- **Must be initialized on the same line as its declaration** ❗

```javascript
const PI = 3.14159;
// PI = 3.14;              // ❌ Error: Assignment to constant variable.
// const GRAVITY;          // ❌ Error: Missing initializer in const declaration
```

### The `const` trap that confuses everyone

`const` means the **variable can't point to something new** — it does **not** mean the
*contents* are frozen.

```javascript
const person = { name: "David" };
person.name = "Eve";           // ✅ ALLOWED — we changed a property inside the object
console.log(person);           // { name: "Eve" }

// person = { name: "Frank" }; // ❌ NOT ALLOWED — we tried to point `person` at a new object
```

Same for arrays: `const arr = [1,2]; arr.push(3);` is fine. `arr = [9]` is not.

### The comparison table

| | Declaration | Initialization | Re-declaration | Re-initialization |
|---|:---:|:---:|:---:|:---:|
| **var** | ✅ | ✅ | ✅ | ✅ |
| **let** | ✅ | ✅ | ❌ | ✅ |
| **const** | ✅ (same line only) | ✅ (same line only) | ❌ | ❌ |

### Which should you use?

> **Rule of thumb: Use `const` by default. Use `let` only when you know the value must change.
> Never use `var` in new code.**

`var` causes bugs because it ignores blocks and gets hoisted in a confusing way (see
[Hoisting](#17-hoisting) and [Closures](#19-closures)).

---

## 6. Identifiers & Keywords

An **identifier** is the name you give to a variable, function, or class.

### Rules for identifiers

1. Cannot be a keyword (you can't name a variable `if` or `for`)
2. Cannot start with a number (`2names` ❌, `names2` ✅)
3. No special characters allowed **except** `$` and `_`
4. Cannot contain spaces (use `camelCase`: `firstName`, not `first name`)
5. Case-sensitive (`age` and `Age` are different)

### Keywords (reserved words)

Keywords are predefined words that are part of the language's vocabulary.
They are always **lowercase** and **cannot be used as identifiers**.

Examples: `var`, `let`, `const`, `if`, `else`, `for`, `while`, `function`, `return`,
`class`, `new`, `this`, `typeof`, `async`, `await`, `try`, `catch`, `throw`, `delete`,
`instanceof`, `switch`, `case`, `break`, `continue`, `do`, `extends`, `super`, `static`,
`import`, `export`, `yield`, `null`, `true`, `false`.

### Other vocabulary you'll hear

| Term | Meaning |
|---|---|
| **Statement** | A group of words, numbers and operators that performs a task. `var a = 7 + "2";` |
| **Expression** | A reference, value, or group of them combined with operators, which **results in a single value**. `7 + 2` |
| **Operator** | A reserved symbol that performs an action on values. `+ - = * === typeof` |
| **Code block** | Anything inside curly braces `{ ... }`. Used by functions, `if`, loops, etc. |
| **Parameter** | The placeholder name in a function definition. |
| **Argument** | The actual value you pass in when calling the function. |

---

## 7. Data Types

A data type tells you **what kind of data** is stored in a variable.
There are **two categories**: Primitive and Non-Primitive.

Use the **`typeof`** operator to check a type:

```javascript
console.log(typeof "Hello");   // "string"
```

### Primitive data types (7)

These hold a **single simple value**. They are stored **by value**.

#### 1. Number
Represents **all** numbers: integers, decimals, floats, negatives. JavaScript does not have
separate `int` / `float` / `double` types.

```javascript
let age = 30;
let price = 99.99;
console.log(typeof age);     // "number"
console.log(typeof price);   // "number"
```

#### 2. String
Text. Can be written with double quotes, single quotes, or backticks. Zero-based indexing.

```javascript
let a = "pro";
let b = 'pro';
let c = `pro`;
console.log(typeof a);       // "string"
```

#### 3. Boolean
Only two possible values: `true` or `false`.

```javascript
let isActive = true;
let hasPermission = false;
console.log(typeof isActive); // "boolean"
```

#### 4. Undefined
A variable that has been **declared but never assigned a value**. JavaScript assigns this
automatically. It also appears when you read a property that doesn't exist, or call a function
with no `return`.

```javascript
let undefinedVar;
console.log(undefinedVar);          // undefined
console.log(typeof undefinedVar);   // "undefined"
```

#### 5. Null
Represents the **intentional absence of a value**. *You* set this deliberately; JavaScript
never does it for you.

```javascript
let emptyValue = null;
console.log(emptyValue);            // null
console.log(typeof emptyValue);     // "object"  ← ⚠️ this is a famous, long-standing BUG
```

> ⚠️ **`typeof null` returns `"object"`.** This is a bug from 1995 that can never be fixed
> without breaking the web. Just memorise it.

#### 6. Symbol (ES6)
A guaranteed-unique, immutable value. Mostly used as a special object key that can never
accidentally collide with another key.

```javascript
const id1 = Symbol('id');
const id2 = Symbol('id');
console.log(id1 === id2);   // false — every Symbol is unique, even with the same description
console.log(typeof id1);    // "symbol"
```

#### 7. BigInt (ES2020)
For whole numbers larger than `2^53 - 1` (the biggest safe `Number`). Written with an `n` suffix.

```javascript
const bigNumber = 1234567890123456789012345678901234567890n;
console.log(typeof bigNumber);  // "bigint"
```

### Non-primitive (reference) data types

These hold **collections** of data. They are stored **by reference** (the variable holds a
pointer to the data, not the data itself).

#### Object
A collection of key–value pairs.

```javascript
let person = { firstName: "John", lastName: "Doe", age: 30 };
console.log(typeof person);  // "object"
```

#### Array
An ordered list. Technically a special kind of object.

```javascript
let colors = ["red", "green", "blue"];
console.log(typeof colors);        // "object"   ← arrays ARE objects in JS
console.log(Array.isArray(colors)); // true      ← use this to actually check for an array
```

#### Function
A reusable block of code. Also technically an object.

```javascript
function greet() { console.log("Hello!"); }
console.log(typeof greet);   // "function"
```

#### RegExp
A regular expression (search pattern). Also an object.

### Primitive vs Reference — the crucial difference

```javascript
// PRIMITIVES are copied by VALUE
let a = 10;
let b = a;      // b gets its own copy of 10
b = 20;
console.log(a); // 10 — unchanged ✅

// OBJECTS are copied by REFERENCE
let obj1 = { count: 10 };
let obj2 = obj1;      // obj2 points at the SAME object
obj2.count = 20;
console.log(obj1.count); // 20 — CHANGED! ⚠️ they are the same object
```

This is the single most common source of "why did my data change?!" bugs.

### Quick type-checking cheat sheet

```javascript
typeof "Hello"        // "string"
typeof 42             // "number"
typeof true           // "boolean"
typeof undefined      // "undefined"
typeof null           // "object"   ⚠️ bug
typeof Symbol()       // "symbol"
typeof 10n            // "bigint"
typeof {}             // "object"
typeof []             // "object"   ⚠️ use Array.isArray()
typeof function(){}   // "function"

Array.isArray([])     // true       ✅ correct way to detect an array
```

---

## 8. Type Conversion & Coercion

**Coercion** is when JavaScript automatically converts one type into another so it can
compare or combine two values.

### The coercion priority order

When mixing types, JavaScript converts toward:
1. **String**
2. **Number**
3. **Boolean**

```javascript
2 + "7"      // "27"   → the number 2 became the string "2"
true - 5     // -4     → true became the number 1, so 1 - 5
"5" * "2"    // 10     → both strings became numbers
```

> ⚠️ The `+` operator is special. If **either** side is a string, it does **concatenation**,
> not addition. Every other maths operator (`- * / %`) converts to numbers.

### Explicit conversion (do this deliberately)

```javascript
// To Number
Number("42")          // 42
parseInt("42px", 10)  // 42     (stops at the first non-digit)
parseFloat("42.5")    // 42.5
+"9"                  // 9      ← the unary plus "hack"

// To String
String(10)            // "10"
(10).toString()       // "10"
10 + ""               // "10"   ← the empty-string "hack"

// To Boolean
Boolean("")           // false
!!"hello"             // true   ← the double-bang "hack"
```

### Two handy "hacks" from the notes

```javascript
// 1. Convert a string to a number: put a + in front of it
let str = "9";
console.log(typeof (+str));      // "number"

// 2. Convert a number to a string: add an empty string
let num = 10;
console.log(typeof (num + ""));  // "string"
```

---

## 9. Truthy and Falsy Values

When a value is used where a boolean is expected (like inside an `if`), JavaScript coerces it.

**There are only 8 falsy values. Memorise this list — everything else is truthy.**

| Falsy (becomes `false`) | Truthy (becomes `true`) |
|---|---|
| `false` | `true` |
| `0` | any non-zero number, e.g. `72`, `-72` |
| `-0` | `Infinity`, `-Infinity` |
| `0n` (BigInt zero) | any non-empty string, e.g. `"text"`, `"0"`, `"false"` |
| `""` (empty string) | `{}` (empty object) ⚠️ |
| `null` | `[]` (empty array) ⚠️ |
| `undefined` | any function |
| `NaN` | |

> ⚠️ **`[]` and `{}` are TRUTHY**, even though they're empty. This surprises everyone.
> To check if an array is empty use `arr.length === 0`.

```javascript
if ("") console.log("won't run");
if ([]) console.log("WILL run");     // ← surprising!
if (0)  console.log("won't run");
if ("0") console.log("WILL run");    // ← a non-empty string
```

---

## 10. Operators

Operators are reserved symbols that perform an action on values and variables.

### Arithmetic

| Operator | Name | Example |
|---|---|---|
| `+` | Add | `10 + 3` → `13` |
| `-` | Subtract | `10 - 3` → `7` |
| `*` | Multiply | `10 * 3` → `30` |
| `/` | Divide | `10 / 3` → `3.333...` |
| `%` | Remainder (modulus) | `10 % 3` → `1` |
| `**` | Exponent (power) | `10 ** 3` → `1000` |
| `++` | Increment by 1 | `a++` |
| `--` | Decrement by 1 | `b--` |

```javascript
let a = 10, b = 3;
console.log(a + b);   // 13
console.log(a % b);   // 1
console.log(a ** b);  // 1000
a++; console.log(a);  // 11
b--; console.log(b);  // 2
```

**Prefix vs postfix:**
```javascript
let x = 5;
console.log(x++);  // prints 5, THEN x becomes 6   (postfix: use then increment)
let y = 5;
console.log(++y);  // y becomes 6, THEN prints 6   (prefix: increment then use)
```

### Assignment

| Operator | Means |
|---|---|
| `=` | Assign |
| `+=` | Add then assign — `x += 3` is `x = x + 3` |
| `-=` | Subtract then assign |
| `*=` | Multiply then assign |
| `/=` | Divide then assign |
| `%=` | Remainder then assign |
| `**=` | Power then assign |

```javascript
let x = 5;
x += 3;  // 8
x -= 5;  // 3
x *= 2;  // 6
```

### Comparison

| Operator | Name | Note |
|---|---|---|
| `==` | Loose equality | Compares **value only**, after coercion |
| `===` | **Strict equality** | Compares **value AND type**, no coercion |
| `!=` | Loose inequality | |
| `!==` | Strict inequality | |
| `>` `<` `>=` `<=` | Greater/less than | |

```javascript
console.log(5 == '5');    // true   ← "5" was converted to 5
console.log(5 === '5');   // false  ← different types
console.log(10 > 5);      // true
```

> ✅ **Always use `===` and `!==`.** Loose equality follows a long, confusing set of coercion
> rules and is a major source of bugs. (The full rules are in the interview questions file.)

### Logical

| Operator | Name | Result |
|---|---|---|
| `&&` | AND | `true` only if **both** sides are truthy |
| `\|\|` | OR | `true` if **either** side is truthy |
| `!` | NOT | Flips it |

```javascript
let isAdult = true;
let hasLicense = false;
console.log(isAdult && hasLicense);  // false
console.log(isAdult || hasLicense);  // true
console.log(!isAdult);               // false
```

### Bitwise

`&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift),
`>>>` (unsigned right shift). Rarely needed in everyday web work.

### Type operators

```javascript
typeof 42                 // "number"
[] instanceof Array       // true — checks if an object was built by a given constructor
```

### Conversion operators

| Operator | Effect |
|---|---|
| `+ ..` | Convert to number |
| `- ..` | Convert to number, then negate |
| `! ..` | Convert to boolean, then invert |

### Other operators

`( )` grouping · `.` property access · `[ ]` bracket access · `new` · `delete` ·
`...` spread/rest · `? :` ternary

### Operator precedence & associativity

- **Precedence** decides which operator runs first when several appear in one expression.
  The higher the precedence, the earlier it executes. (`*` runs before `+`, just like maths.)
- **Associativity** decides the direction of parsing when operators have *equal* precedence.

```javascript
console.log(2 + 3 * 4);     // 14  — * runs first
console.log((2 + 3) * 4);   // 20  — parentheses override precedence
```

> 💡 When in doubt, add parentheses. It costs nothing and makes intent obvious.
> Full table: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators>

---

# PART 2 — CONTROLLING THE FLOW

---

## 11. Conditional Statements

Conditional statements let your program run specific code **only if certain conditions are
met**. For instance, in a shopping app you can hide the "checkout" button if the cart is empty.

### `if`

```javascript
if (condition) {
  // this code runs only if condition is true
}
```

### `if` / `else`

If the condition is false, the `else` block runs instead.

```javascript
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}
```

### `if` / `else if` / `else` (the "ladder")

Checked top to bottom. **The first true condition wins**, and the rest are skipped.

```javascript
let temperature = 25;

if (temperature > 30) {
    console.log("It's hot outside!");
} else if (temperature > 20) {
    console.log("It's pleasant.");
} else {
    console.log("It's cold.");
}
// Output: It's pleasant.
```

### `switch`

Takes a **single expression**, and runs the code of the `case` that matches.
Use it when you're comparing one value against many fixed options — it reads better than a
long `if/else if` chain.

```javascript
let day = "Monday";

switch (day) {
    case "Monday":
        console.log("Start of the week.");
        break;
    case "Friday":
        console.log("End of the work week!");
        break;
    default:
        console.log("Just another day.");
}
// Output: Start of the week.
```

**Two things you must know about `switch`:**

1. **`break` is essential.** Without it, execution "falls through" and keeps running the
   next case's code too.
2. **`default`** is the catch-all, like `else`. It's optional and can go anywhere (but by
   convention goes last).

**The `switch(true)` trick** — for range checks:

```javascript
let num = 10;
switch (true) {
  case (num > 20):
    console.log("Greater than 20");
    break;
  case (num > 10):
    console.log("Greater than 10");
    break;
  default:
    console.log("10 or less");
}
// Output: 10 or less
```

---

## 12. The Ternary Operator

A one-line replacement for a simple `if/else`. It **returns** the first value if the
expression is truthy, otherwise the second.

```javascript
condition ? valueIfTrue : valueIfFalse
```

```javascript
let age = 18;
let status = (age >= 18) ? "Adult" : "Minor";
console.log(status);  // "Adult"
```

Because it's an *expression* (it produces a value), you can use it anywhere a value is
expected — inside template literals, as a function argument, etc.

```javascript
console.log(`You are ${age >= 18 ? "an adult" : "a minor"}`);
```

> 💡 Great for short either/or choices. **Don't nest them** — nested ternaries are unreadable.
> Use `if/else` for anything complex.

---

## 13. Loops

Loops repeat a block of code. Imagine you get 50 blog posts from a database and want to print
each title. Instead of writing the code 50 times, you loop.

### `for` loop

The workhorse. Use when you **know how many times** to repeat.

```javascript
for (initial-expression; condition; second-expression) {
    // code to run each time
}
```

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
// Output: 0 1 2 3 4
```

**How it runs, step by step:**
1. Run the **initial expression** (`let i = 0`) — once only.
2. Check the **condition** (`i < 5`). If true, continue; if false, end the loop.
3. Run the **code in the block**.
4. Run the **second expression** (`i++`).
5. Go back to Step 2.

### `while` loop

Use when you **don't know** how many repeats you need — you just loop until something changes.

```javascript
let count = 0;
while (count < 3) {
    console.log("Count: " + count);
    count++;         // ⚠️ don't forget this, or you get an infinite loop!
}
// Output: Count: 0, Count: 1, Count: 2
```

**How it runs:**
1. If the condition is true, continue; otherwise end.
2. Run the code block.
3. Go back to Step 1.

### `do...while` loop

Same as `while`, but the block runs **at least once** before the condition is ever checked.

```javascript
let i = 0;
do {
    console.log("Do-while iteration: " + i);
    i++;
} while (i < 0);      // condition is false, but it still ran once
// Output: Do-while iteration: 0
```

**How it runs:**
1. Run the code block.
2. If the condition is true, continue; otherwise end.
3. Go back to Step 1.

### `for...of` (ES6) — loop over **values**

Works on any *iterable*: arrays, strings, Maps, Sets, NodeLists.
**This is the cleanest way to loop over an array.**

```javascript
const colors = ["red", "green", "blue"];
for (let color of colors) {
    console.log(color);
}
// Output: red, green, blue

for (let char of "Hi") {
    console.log(char);   // H, i
}
```

### `for...in` — loop over **keys**

Iterates over the enumerable **property names** of an object.

```javascript
const car = { brand: "Toyota", model: "Camry", year: 2020 };
for (let key in car) {
    console.log(`${key}: ${car[key]}`);
}
// brand: Toyota
// model: Camry
// year: 2020
```

> ⚠️ **Don't use `for...in` on arrays.** It gives you the *index as a string* (`"0"`, `"1"`),
> may include inherited properties, and doesn't guarantee order. Use `for...of` or `forEach`.

### Choosing the right loop

| Situation | Use |
|---|---|
| You need the index, or want to skip/step | `for` |
| Loop over array values | `for...of` or `forEach()` |
| Loop over object keys | `for...in` or `Object.keys()` |
| Repeat until a condition changes | `while` |
| Must run at least once | `do...while` |
| Transform an array into a new array | `map()` |
| Keep only some items | `filter()` |
| Boil an array down to one value | `reduce()` |

---

## 14. break, continue, and Labels

### `break`

Immediately **exits the whole loop**.

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log(i);       // 0 1 2 3 4
}
```

### `continue`

**Skips the rest of the current iteration** and jumps to the next one.

```javascript
for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
  console.log(i);       // 0 1 3 4   ← 2 was skipped
}
```

### Labels

A label lets `break` or `continue` target an **outer** loop from inside a nested one.

```javascript
outerLoop:
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) continue outerLoop;   // skip to next i
    console.log(i, j);
  }
}
```

> 💡 Labels are rare. If you need one, a nested function with a `return` is often clearer.

---
---

# PART 3 — THE BUILDING BLOCKS

---

## 15. Functions

A function is simply a bunch of code bundled into a section. **This code only runs when the
function is called.** Functions let you organise code and reuse it.

Using a function has only two parts:
1. **Declaring / defining** the function
2. **Using / running (invoking / calling)** the function

### Anatomy of a function

```javascript
// (1) Function declaration
function someName(param1, param2) {
    //  ↑         ↑
    //  name      parameters (optional)

    // code block — anything inside { } is a "block"
    var a = param1 + " love " + param2;

    return a;        // return is optional
}

// (2) Invoke (run / call) the function
someName("Me", "You");   // arguments being passed in
```

- **Name** — just a name you give it. Make it *descriptive of what the function does*.
- **Parameters / arguments** — optional. Information the function can use inside its code.
- **Code block** — the `{ ... }`. Not exclusive to functions; `if` and `for` use blocks too.
- **`return`** — optional. Spits a value back out. **Once a function returns, no further
  lines inside it run.**
- **Invoking** — writing the name followed by `()` executes the code inside.

### The 6 types of function

#### 1. Function Declaration (function statement)
A regular named function. **Fully hoisted** — you can call it before it's defined.

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}
console.log(greet("Alice"));   // "Hello, Alice!"
```

#### 2. Function Expression
A function stored in a variable. **Not hoisted** — you must define it before calling it.

```javascript
const sayHi = function(name) {
    return "Hi, " + name + "!";
};
console.log(sayHi("Bob"));     // "Hi, Bob!"
```

#### 3. Arrow Function (ES6)
Shorter syntax. **Has no `this` binding of its own** (this is its most important trait — see
[the `this` keyword](#37-the-this-keyword)). Cannot be used as a constructor.

```javascript
// One expression → implicit return, no braces needed
const add = (a, b) => a + b;
console.log(add(5, 3));        // 8

// Multiple lines → braces AND an explicit return are required
const multiply = (a, b) => {
    return a * b;
};
console.log(multiply(4, 2));   // 8

// One parameter → parentheses optional
const square = n => n * n;

// No parameters → empty parentheses required
const hello = () => "Hi!";
```

#### 4. Anonymous Function
A function with no name, usually passed straight into another function as a callback.

```javascript
setTimeout(function() {
    console.log("Runs after 1 second");
}, 1000);
```

#### 5. IIFE — Immediately Invoked Function Expression
Defined and run instantly. See [section 20](#20-iife-immediately-invoked-function-expression).

```javascript
(function () {
    console.log("IIFE");
})();
```

#### 6. Callback Function
A function passed as an argument to another function, to be called later.

```javascript
arr.forEach(function(item) { console.log(item); });
```

### Parameters and arguments

```javascript
function calculateSum(num1, num2) {   // num1, num2 are PARAMETERS
    return num1 + num2;
}
console.log(calculateSum(10, 20));    // 10 and 20 are ARGUMENTS
```

### Default parameters (ES6)

Gives a parameter a fallback value if none is passed.

```javascript
function welcome(name = "Guest") {
    console.log(`Welcome, ${name}!`);
}
welcome("Charlie");   // Welcome, Charlie!
welcome();            // Welcome, Guest!
```

### Rest parameters (ES6)

Collects **any number** of remaining arguments into a real array.

```javascript
function sum(...nums) {
    return nums.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3, 4, 5));   // 15
```

### Why functions are "first-class objects"

In JavaScript, functions are treated like any other value. They can be:
- assigned to variables
- stored as object properties (then they're called **methods**)
- stored as items in an array
- passed as arguments to other functions
- returned as the result of another function

The only difference between a function and any other value is that a function can be **invoked**.

---

## 16. Scope, Lexical Environment & the Scope Chain

**Scope** = the limits within which a variable exists.

### The kinds of scope

| Scope | Meaning |
|---|---|
| **Global scope** | The outermost scope. Variables here are available everywhere. |
| **Function scope** | Any variable inside a function belongs to that function. `var` respects this. |
| **Block scope** | Any variable inside `{ }`. Only `let` and `const` respect this. |

```javascript
var globalVar = "I'm global";      // global scope

function myFunction() {
    var functionVar = "I'm function-scoped";

    if (true) {
        let blockVar = "I'm block-scoped";
        var notBlockVar = "var ignores blocks!";
        console.log(blockVar);      // ✅ works
    }

    console.log(notBlockVar);       // ✅ works — var leaked out of the block
    // console.log(blockVar);       // ❌ ReferenceError
}
// console.log(functionVar);        // ❌ ReferenceError
```

### Lexical Environment (lexical scope)

The **physical location in the code** where a variable or function is declared is its
**lexical environment**.

Two rules govern it:

> **Rule 1:** Variables in an outer scope **can** be accessed by a nested scope.
> But variables inside a nested scope **CANNOT** be accessed by the outer scope.
> (This is what makes "private variables" possible.)
>
> **Rule 2:** Variables are picked up from the lexical environment — i.e. from *where the
> code was written*, not from where it was called.

### The Scope Chain

The nested hierarchy of scopes is called the **scope chain**. When JavaScript looks for a
variable, it searches the current scope first, then the parent, then the grandparent, and so
on **upwards** until it reaches the global scope. If it never finds it → `ReferenceError`.

```javascript
var a = "global";

function first() {
    var a = "fresh";

    function second() {
        console.log(a);       // "fresh"
        // Scope chain: second's scope → first's scope → global scope
        // It found `a` in first's scope and stopped looking.
    }
    second();
}
first();
```

---

## 17. Hoisting

**Hoisting is the mechanism where JavaScript moves declarations of variables and functions to
the top of their scope before the code runs.** This means you can use them *before* you
declare them.

But **only the declaration is hoisted, never the value.**

### What gets hoisted, and how

| Thing | Hoisted? | Usable before declaration? |
|---|---|---|
| `function` declaration | ✅ Fully | ✅ Yes |
| `var` | ✅ Declaration only, initialised to `undefined` | ⚠️ Yes, but the value is `undefined` |
| `let` / `const` | ✅ (but in the "Temporal Dead Zone") | ❌ No — throws a `ReferenceError` |
| Function expressions | ❌ (follows its variable's rules) | ❌ No |
| Arrow functions | ❌ (follows its variable's rules) | ❌ No |

### Variable hoisting

```javascript
console.log(x);   // undefined  ← NOT an error!
var x = 10;
console.log(x);   // 10
```

JavaScript effectively rearranged this into:

```javascript
var x;            // declaration hoisted, value = undefined
console.log(x);   // undefined
x = 10;           // assignment stays where it was
console.log(x);   // 10
```

### Function hoisting

```javascript
console.log(sum(10, 20));    // 30 ✅ — works!

function sum(a, b) {
    return a + b;
}
```

The whole function body was hoisted, so it was ready to run.

### The `let` / `const` difference — the Temporal Dead Zone

```javascript
console.log(y);   // ❌ ReferenceError: Cannot access 'y' before initialization
let y = 10;
```

`let` and `const` *are* hoisted, but they sit in a "Temporal Dead Zone" (TDZ) from the start
of the block until their declaration line. Touching them in the TDZ throws an error.
**This is a good thing** — it catches mistakes that `var` silently hides.

### A worked example

```javascript
console.log(y);
y = 1;
console.log(y);
console.log(greet("Mark"));

function greet(name){
 return 'Hello ' + name + '!';
}

var y;
```
**Output:** `undefined`, `1`, `Hello Mark!`

**Why?** During the *compilation phase*, JavaScript hoists `greet` (fully) and `var y`
(as `undefined`). Then during the *execution phase* it runs the lines in order.

---

## 18. Execution Context & the Call Stack

An **Execution Context** is the environment in which JavaScript code is evaluated and executed.
Understanding it explains hoisting, scope, and `this` all at once.

### The three types of Execution Context

**1. Global Execution Context (GEC)**
- Created when your code first runs
- Stores global variables and functions
- Its `this` is attached to the `window` object in browsers
- There is only ever **one** GEC

**2. Function Execution Context (FEC)**
- Created **every single time a function is invoked**
- Has its own variable environment
- Has access to the outer/global scope via the scope chain

```javascript
function add(x, y) {
  let sum = x + y;
  return sum;
}
add(5, 10);
// When add(5, 10) is called, a NEW FEC is created with its own x, y, and sum.
```

**3. Eval Execution Context (rare)**
- `eval()` executes a *string* of code as if it were real JavaScript
- **Not recommended** — it breaks scope and can be unsafe

### What's inside every Execution Context

Each context contains four key components:

**1. Lexical Environment (LE)**
- Stores `let` and `const` declarations
- Maintains a reference to the outer scope — **this is what enables closures**
- Supports block-level scoping

**2. Variable Environment (VE)**
- A sub-part of the Lexical Environment
- Holds variables declared with `var`, plus functions and the `arguments` object
- **Handles hoisting** by setting up declarations during the creation phase

**3. Scope Chain**
- When looking up a variable, JavaScript checks the current scope → parent scope → global
- Built using Lexical Environments

**4. `this` Binding**
- Sets what `this` refers to for that context
- Depends entirely on *how the function was called*

### The Execution Context lifecycle — two phases

**Phase 1 — Creation Phase (a.k.a. Compilation)**
- **Hoisting happens here**
- JavaScript scans the code for declarations
- Memory is allocated: `var` → `undefined`; function declarations → the full function
- The scope chain and `this` are determined

**Phase 2 — Execution Phase**
- Assignments are made (values get put into the variables)
- Code is executed line by line
- Functions are invoked

### The Call Stack

The **Call Stack** is a **Last-In, First-Out (LIFO)** structure that tracks execution contexts.

- When a function is called, a new execution context is **pushed** onto the stack.
- When a function finishes, its context is **popped** off.
- This is how nested functions and async callbacks are managed under the hood.

```javascript
function first()  { console.log("first start");  second(); console.log("first end"); }
function second() { console.log("second start"); third();  console.log("second end"); }
function third()  { console.log("third"); }
first();
```
```
Output:              Stack over time:
first start          [ GEC, first ]
second start         [ GEC, first, second ]
third                [ GEC, first, second, third ]
second end           [ GEC, first, second ]   ← third popped
first end            [ GEC, first ]           ← second popped
                     [ GEC ]                  ← first popped
```

> If you recurse forever, the stack fills up and you get the famous
> **"Maximum call stack size exceeded"** error.

### Why you should care

Understanding execution context helps you:
- Debug hoisting and scope issues
- Avoid common reference errors
- Write better closures and callbacks
- **Predict how code behaves before running it**

---

## 19. Closures

> **A closure is a function that remembers the variables from the place where it was
> *declared*, even after that outer function has finished running.**

More formally: a closure is the combination of a function and the lexical environment within
which that function was declared. At the moment of declaration, the function captures the
references to variables in its own scope, its parent's scope, its grandparent's scope, and so
on up to global — via the scope chain.

### The simplest example

```javascript
function outerFunction() {
  let outerVar = "I'm outer!";      // outer function's variable

  function innerFunction() {
    console.log(outerVar);          // accessing the outer function's variable
  }

  return innerFunction;             // return the inner function (don't call it)
}

const closureExample = outerFunction();  // outerFunction RUNS and RETURNS innerFunction
closureExample();                        // "I'm outer!"
```

**How it works:** `outerFunction()` has completely finished by the time we call
`closureExample()`. Normally `outerVar` would be garbage-collected. But because
`innerFunction` still holds a reference to it, JavaScript keeps it alive. That preserved
bundle is the **closure**.

### The practical use: private state

This is the real reason closures matter. `count` below cannot be touched from outside.

```javascript
function createCounter() {
      let count = 0;    // "closed over" by the returned functions — nobody outside can reach it

      return {
           increment: function() { count++; console.log(count); },
           decrement: function() { count--; console.log(count); },
           getCount:  function() { return count; }
      };
}

const counter1 = createCounter();
counter1.increment();               // 1
counter1.increment();               // 2
console.log(counter1.getCount());   // 2

const counter2 = createCounter();   // a brand-new, completely independent counter
counter2.increment();               // 1
```

### Closures keep REFERENCES, not copies

This is the subtle part that trips people up.

```javascript
var globalVar = "global";
var outerVar  = "outer";

function outerFunc(outerParam) {
  function innerFunc(innerParam) {
    console.log(globalVar, outerParam, innerParam);
  }
  return innerFunc;
}

const x = outerFunc(outerVar);   // outerParam is set to "outer" RIGHT NOW
outerVar  = "outer-2";           // changed AFTER the call — too late
globalVar = "guess";             // changed BEFORE x is invoked
x("inner");
```

**Output: `guess outer inner`**

- `outerParam` = `"outer"` — because the value was passed *at invocation time*, before the
  reassignment happened.
- `globalVar` = `"guess"` — because the closure holds a **reference** to the variable, and
  we look up its *current* value at the moment `x("inner")` runs.
- `innerParam` = `"inner"` — passed in directly.

### The classic closure bug (and how to fix it)

```javascript
const arrFuncs = [];
for (var i = 0; i < 5; i++) {
    arrFuncs.push(function () { return i; });
}
console.log(i);                       // 5

for (let j = 0; j < arrFuncs.length; j++) {
    console.log(arrFuncs[j]());       // logs 5, 5, 5, 5, 5  ← NOT 0,1,2,3,4!
}
```

**Why?** `var i` is a *single* function-scoped variable. All five functions close over the
**same** `i`. By the time we call them, the loop has finished and `i` is `5`.

**Fix 1 — use `let` (best):** `let` creates a **new binding for each iteration**.
```javascript
for (let i = 0; i < 5; i++) {
    arrFuncs.push(function () { return i; });
}
// now logs 0, 1, 2, 3, 4 ✅
```

**Fix 2 — use an IIFE (the old ES5 way):**
```javascript
for (var i = 0; i < 5; i++) {
    (function(captured) {
        arrFuncs.push(function () { return captured; });
    })(i);
}
```

---

## 20. IIFE (Immediately Invoked Function Expression)

An IIFE is **self-invoking** — it is defined and executed immediately, without needing to be
called separately.

```javascript
(function () {
  console.log("IIFE");
})();
```

**The two sets of parentheses:**
- The **outer** `( ... )` turn the function declaration into an *expression*.
- The **trailing** `()` immediately invoke it.

**Arrow-function version:**
```javascript
(() => {
  console.log("Arrow IIFE");
})();
```

**Async version:**
```javascript
(async () => {
  const data = await fetch(url);
})();
```

### Why use one?

Before ES6 modules and `let`, an IIFE was the only way to create a private scope and avoid
polluting the global namespace. Variables inside it are invisible to the outside world.

```javascript
(function() {
  var secret = "you can't see me";
})();
// console.log(secret);  // ❌ ReferenceError — perfect encapsulation
```

> ⚠️ In an IIFE, `this` points to the **`window`** object (in non-strict mode), not to any
> enclosing object.

---

## 21. Higher-Order Functions & Callbacks

These two concepts always appear together.

### Higher-Order Function

> **A higher-order function is a function that takes another function as an argument,
> returns a function, or both.**

```javascript
function higherOrderFunction(param, callback) {
    return callback(param);
}
```

**Taking a function as an argument:**
```javascript
function operateOnNumbers(a, b, operation) {
     return operation(a, b);
}
function add(x, y)      { return x + y; }
function subtract(x, y) { return x - y; }

console.log(operateOnNumbers(10, 5, add));       // 15
console.log(operateOnNumbers(10, 5, subtract));  // 5
```

**Returning a function:**
```javascript
function multiplier(factor) {
     return function(number) {
           return number * factor;
     };
}
const multiplyBy5 = multiplier(5);
console.log(multiplyBy5(10));  // 50
```

### Callback Function

> **A callback is a function passed as an argument to another function, to be executed later
> — after some operation completes.**

**A good analogy:** you call someone, they don't answer, so you leave a message and expect
them to *call back*. Leaving the message is the event; the call back is the action you expect
to happen later.

```javascript
const btnAdd = document.getElementById('btnAdd');

btnAdd.addEventListener('click', function clickCallback(e) {
  // this runs LATER, only when the button is actually clicked
});
```

### Array higher-order functions

Several array methods — `map()`, `filter()`, `forEach()`, `reduce()` — are higher-order
functions that expect a callback. Together they allow flexible, powerful patterns, especially
in array manipulation and async code.

| Method | What it returns |
|---|---|
| `arr.forEach(cb)` | `undefined` — just performs an action for each item |
| `arr.map(cb)` | A **new array** with modified values |
| `arr.filter(cb)` | A **new array** with only the items that passed the test |
| `arr.reduce(cb, init)` | A **single value** (not an array) |

```javascript
let numbers = [1, 2, 3, 4];

numbers.forEach(n => console.log(n));           // 1 2 3 4 (returns undefined)
let doubled = numbers.map(n => n * 2);          // [2, 4, 6, 8]
let evens   = numbers.filter(n => n % 2 === 0); // [2, 4]
let total   = numbers.reduce((acc, n) => acc + n, 0);  // 10
```

---

## 22. Recursion

**Recursion is the process of a function calling itself.** A function that calls itself is a
*recursive function*.

Every recursive function needs **two parts**:
1. A **base case** — the condition that stops the recursion
2. A **recursive case** — where it calls itself with a smaller problem

```javascript
function factorial(n) {
  if (n <= 1) return 1;          // BASE CASE — stop here
  return n * factorial(n - 1);   // RECURSIVE CASE
}
console.log(factorial(5));       // 120  (5 × 4 × 3 × 2 × 1)
```

**Tracing it:**
```
factorial(5) → 5 * factorial(4)
             → 5 * (4 * factorial(3))
             → 5 * (4 * (3 * factorial(2)))
             → 5 * (4 * (3 * (2 * factorial(1))))
             → 5 * (4 * (3 * (2 * 1)))  = 120
```

> ⚠️ **Forget the base case and you get infinite recursion**, which fills the call stack and
> throws "Maximum call stack size exceeded".

---

## 23. Strict Mode

Strict mode makes JavaScript behave more **strictly and securely**. Being a scripting
language, JavaScript sometimes displays a "correct" result even when the code has errors.
Strict mode catches those silent errors early and prevents bad practices.

### What it does

- Declaring variables without `let` / `const` / `var` throws an error
- Prevents using reserved keywords (like `private`, `interface`) as variable names
- Makes it harder to accidentally create global variables
- Stops you deleting important objects or properties (like `delete Object.prototype`)
- Disallows duplicate parameter names in functions
- In a plain function call, `this` is `undefined` instead of `window`

### How to enable it

Write `"use strict";` at the very top of your file, or inside a function.

```javascript
"use strict";
x = 10;         // ❌ ReferenceError: x is not defined
```

```javascript
function test() {
  "use strict";
  y = 20;       // ❌ ReferenceError: y is not defined
}
```

> 💡 **ES6 modules and classes are always in strict mode automatically.** You don't need the
> directive when using `import`/`export` or `class`.

---
---

# PART 4 — DATA STRUCTURES

---

## 24. Strings

A **string** is a sequence of characters used for storing and managing text data.
Strings follow **zero-based indexing** — the first character is at position `0`.

### Creating strings

Three ways, all valid:

```javascript
let str1 = "pro";     // double quotes
let str2 = 'pro';     // single quotes
let str3 = `pro`;     // backticks (template literal — see next section)
```

### Basic access

```javascript
let name = "Tony";
console.log(name.length);   // 4   ← number of characters
console.log(name[0]);       // "T" ← first character
console.log(name[3]);       // "y"
```

> ⚠️ **Strings are immutable.** `name[0] = "P"` does nothing. Every string method returns a
> **new** string; it never changes the original.

### String methods — complete reference

| Method | What it does | Example |
|---|---|---|
| `.length` | Get the length (a property, not a method) | `text.length` |
| `.toUpperCase()` | Convert to uppercase | `"hi".toUpperCase()` → `"HI"` |
| `.toLowerCase()` | Convert to lowercase | `"HI".toLowerCase()` → `"hi"` |
| `.trim()` | Remove whitespace from **both** ends | `"  hi  ".trim()` → `"hi"` |
| `.slice(start, end)` | Extract part of the string (supports negatives) | `"hello".slice(1, 4)` → `"ell"` |
| `.substring(start, end)` | Extract between two indexes (no negatives) | `"hello".substring(1, 4)` → `"ell"` |
| `.concat(str)` | Join strings together | `"a".concat("b")` → `"ab"` |
| `.replace(old, new)` | Replace the **first** match | `"aa".replace("a","b")` → `"ba"` |
| `.replaceAll(old, new)` | Replace **all** matches | `"aa".replaceAll("a","b")` → `"bb"` |
| `.charAt(i)` | Get the character at a position | `"hello".charAt(1)` → `"e"` |
| `.includes(sub)` | Does it contain this? → boolean | `"hello".includes("ell")` → `true` |
| `.indexOf(sub)` | **First** index of a substring (`-1` if absent) | `"hello".indexOf("l")` → `2` |
| `.lastIndexOf(sub)` | **Last** index of a substring | `"hello".lastIndexOf("l")` → `3` |
| `.startsWith(sub)` | Does it start with this? | `"hello".startsWith("he")` → `true` |
| `.endsWith(sub)` | Does it end with this? | `"hello".endsWith("lo")` → `true` |
| `.split(sep)` | Split into an **array** | `"a,b".split(",")` → `["a","b"]` |
| `.repeat(n)` | Repeat the string n times | `"ab".repeat(2)` → `"abab"` |
| `.match(regex)` | Match a regex pattern | `"hi".match(/h/)` |
| `.search(value)` | Search against a value, returns index | `"hello".search(/l/)` → `2` |
| `.padStart(len, ch)` | Pad the front to a length | `"5".padStart(3,"0")` → `"005"` |
| `.padEnd(len, ch)` | Pad the end to a length | `"5".padEnd(3,"0")` → `"500"` |
| `.at(i)` | Character at index (supports negatives) | `"hello".at(-1)` → `"o"` |

### Worked examples

```javascript
let text = "  Hello World  ";

console.log(text.trim());                  // "Hello World"
console.log(text.trim().toUpperCase());    // "HELLO WORLD"   ← methods chain!
console.log(text.trim().split(" "));       // ["Hello", "World"]
console.log(text.includes("World"));       // true
console.log(text.trim().slice(0, 5));      // "Hello"
console.log(text.trim().slice(-5));        // "World"   ← negative counts from the end
console.log("ha".repeat(3));               // "hahaha"
console.log(String.fromCharCode(65));      // "A"
```

### `slice()` vs `substring()`

| | `slice(start, end)` | `substring(start, end)` |
|---|---|---|
| Negative numbers | ✅ Counts from the end | ❌ Treated as `0` |
| If `start > end` | Returns `""` | **Swaps them** |

> 💡 **Just use `slice()`.** It's more predictable and works the same on arrays.

---

## 25. Template Literals

Introduced in ES6. Written with **backticks** `` ` `` instead of quotes. They give you two
superpowers:

**1. Embedded expressions** with `${ ... }` — no more `+` concatenation

```javascript
let name = "World";
console.log(`Hello, ${name}!`);          // "Hello, World!"
console.log(`2 + 3 = ${2 + 3}`);         // "2 + 3 = 5"  ← any expression works
console.log(`You are ${age >= 18 ? "an adult" : "a minor"}`);
```

**2. Multi-line strings** — press Enter, it just works

```javascript
const greeting = `Hello, ${name}!
This is a multi-line string.
No \n needed.`;
```

**The old painful way vs the new way:**
```javascript
// Old
let msg = "Hello, " + firstName + " " + lastName + "! You are " + age + " years old.";
// New
let msg = `Hello, ${firstName} ${lastName}! You are ${age} years old.`;
```

---

## 26. Arrays

An array is a **collection of data items** stored in a **single variable**, in order.

**Key facts:**
- In JavaScript arrays are **heterogeneous** — one array can hold mixed types (numbers,
  strings, booleans, objects, even functions).
- Arrays are **not fixed in length** — they are growable.
- The `length` property tells you how many elements there are.
- To access elements you use **index positions, which start from 0**.
- **The data type of an array is `object`.** Use `Array.isArray()` to check properly.

### Creating arrays

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
let emptyArray = [];
let mixedArray = [1, "hello", true, { key: "value" }, () => "I'm a function"];
let numbers = new Array(1, 2, 3);      // constructor form (rarely used)
```

### Accessing and modifying

```javascript
let fruits = ["Apple", "Banana", "Cherry"];

console.log(fruits[0]);                     // "Apple"   ← first item
console.log(fruits[fruits.length - 1]);     // "Cherry"  ← last item
console.log(fruits.at(-1));                 // "Cherry"  ← modern way
console.log(fruits.length);                 // 3
console.log(typeof fruits);                 // "object"
console.log(Array.isArray(fruits));         // true

fruits[1] = "Blueberry";                    // modify in place
console.log(fruits);                        // ["Apple", "Blueberry", "Cherry"]
```

### Looping over arrays

```javascript
let heroes = ["Ironman", "Hulk", "Thor"];

// Best for simple iteration
for (let hero of heroes) {
  console.log(hero);
}

// When you need the index
for (let i = 0; i < heroes.length; i++) {
  console.log(i, heroes[i]);
}

// forEach — gives you value, index, and the whole array
heroes.forEach((hero, index) => console.log(index, hero));
```

---

## 27. Array Methods in Detail

There are 29 core array methods. They fall into two vital categories:

> **MUTATING methods change the original array.**
> **NON-MUTATING methods return a new array and leave the original alone.**
>
> Getting this wrong is the #1 array bug.

| Mutates the original ⚠️ | Returns a new value ✅ |
|---|---|
| `push`, `pop`, `shift`, `unshift` | `slice`, `concat`, `join`, `toString` |
| `splice`, `sort`, `reverse`, `fill`, `copyWithin` | `map`, `filter`, `reduce`, `find`, `findIndex` |
| | `includes`, `indexOf`, `some`, `every`, `entries` |

### PART 1 — Adding and removing at the ends

#### 1. `toString()`
Returns a string with array values separated by commas. **Does not change the original.**
```javascript
let bikes = ["yamaha", "Bajaj", "Honda", "TVS"];
console.log(bikes.toString());   // "yamaha,Bajaj,Honda,TVS"
```

#### 2. `join(separator)`
Returns a new string by concatenating all elements, separated by commas **or a separator you
specify**. Non-mutating.
```javascript
let bikes = ["yamaha", "Bajaj", "Honda", "TVS"];
console.log(bikes.join());      // "yamaha,Bajaj,Honda,TVS"
console.log(bikes.join(""));    // "yamahaBajajHondaTVS"
console.log(bikes.join("-"));   // "yamaha-Bajaj-Honda-TVS"
```

#### 3. `pop()`
Removes the **last** element and **returns the removed element**. ⚠️ Mutates.
```javascript
let bikes = ["yamaha", "Bajaj", "Honda", "TVS"];
console.log(bikes.pop());   // "TVS"
console.log(bikes);         // ["yamaha", "Bajaj", "Honda"]
```

#### 4. `push(item1, item2, ...)`
Adds new items to the **end** and **returns the new length**. Accepts n arguments. ⚠️ Mutates.
```javascript
let bikes = ["yamaha", "Bajaj", "Honda", "TVS"];
console.log(bikes.push("Ducatti", "Royal Enfield"));   // 6  ← the NEW LENGTH
console.log(bikes);  // ['yamaha','Bajaj','Honda','TVS','Ducatti','Royal Enfield']
```

#### 5. `shift()`
Removes the **first** element and **returns it**. ⚠️ Mutates.
```javascript
let bikes = ["yamaha", "Bajaj", "Honda", "TVS"];
console.log(bikes.shift());   // "yamaha"
console.log(bikes);           // ["Bajaj", "Honda", "TVS"]
```

#### 6. `unshift(item1, ...)`
Adds elements to the **beginning** and **returns the new length**. ⚠️ Mutates.
```javascript
let bikes = ["Bajaj", "Honda"];
console.log(bikes.unshift("BMW", "Kawasaki"));  // 4
console.log(bikes);   // ['BMW', 'Kawasaki', 'Bajaj', 'Honda']
```

> **Memory aid:**
> `push`/`pop` work at the **end**. `unshift`/`shift` work at the **start**.
> `push`/`unshift` **add**. `pop`/`shift` **remove**.

### PART 2 — Reordering and slicing

#### 7. `delete`
The `delete` operator removes a value but **leaves a hole** — the length stays the same and
you get `undefined` in the gap.
```javascript
let arr = [1, 2, 3];
delete arr[1];
console.log(arr);          // [1, empty, 3]
console.log(arr.length);   // 3   ⚠️ still 3!
```
> ⚠️ **Never use `delete` on arrays.** Use `splice()` instead.

#### 8. `concat(arr2)`
Joins two or more arrays into a **new** array. Non-mutating.
```javascript
let a = [1, 2], b = [3, 4];
console.log(a.concat(b));       // [1, 2, 3, 4]
console.log(a);                 // [1, 2] — unchanged ✅
```

#### 9. `sort()`
Sorts the array. ⚠️ Mutates.

> ⚠️ **The big gotcha:** by default `sort()` converts everything to **strings** and sorts
> alphabetically. So `[10, 9, 1]` sorts to `[1, 10, 9]`.

```javascript
let nums = [10, 9, 1, 100];
console.log(nums.sort());                 // [1, 10, 100, 9]  ⚠️ WRONG for numbers

// Correct — provide a compare function
console.log(nums.sort((a, b) => a - b));  // [1, 9, 10, 100]  ascending ✅
console.log(nums.sort((a, b) => b - a));  // [100, 10, 9, 1]  descending ✅

// Sorting strings
let names = ["Zoe", "adam", "Bob"];
names.sort((a, b) => a.localeCompare(b)); // handles case + accents properly
```

#### 10. `splice(startIndex, deleteCount, ...itemsToAdd)`
The Swiss army knife: **remove elements from the middle of an array and/or add elements into
the middle**. Accepts up to 3+ arguments. ⚠️ Mutates. Returns the removed items.

```javascript
let arr = [10, 20, 30, 40, 50];

arr.splice(1, 2);            // from index 1, delete 2 items
console.log(arr);            // [10, 40, 50]

arr.splice(1, 0, 99, 98);    // delete 0 items, INSERT 99 and 98 at index 1
console.log(arr);            // [10, 99, 98, 40, 50]

arr.splice(1, 1, "replaced");// delete 1, insert 1 → replacement
console.log(arr);            // [10, "replaced", 98, 40, 50]
```

#### 11. `slice(startIndex, endIndex)`
Returns a **shallow copy of a portion** of the array. The end index is **not included**.
**Does not affect the original.** ✅ Non-mutating.
```javascript
let arr = [10, 20, 30, 40, 50];
console.log(arr.slice(1, 3));   // [20, 30]     ← index 3 excluded
console.log(arr.slice(2));      // [30, 40, 50] ← to the end
console.log(arr.slice(-2));     // [40, 50]     ← last two
console.log(arr.slice());       // full shallow copy
console.log(arr);               // unchanged ✅
```

#### 12. `reverse()`
Reverses the order of elements in place. ⚠️ Mutates.
```javascript
let arr = [1, 2, 3];
arr.reverse();
console.log(arr);   // [3, 2, 1]

// To reverse WITHOUT mutating:
let reversed = [...arr].reverse();
```

### PART 3 — Searching

#### 13. `Array.isArray(value)`
The only reliable way to check if something is an array.
```javascript
Array.isArray([]);   // true
Array.isArray({});   // false
typeof [];           // "object"  ⚠️ unhelpful
```

#### 14. `indexOf(item)`
Returns the index of the given element. If the element appears multiple times, it gives the
index of the **first occurrence**. Returns `-1` if not found.
```javascript
let arr = [10, 20, 10, 30];
console.log(arr.indexOf(10));    // 0
console.log(arr.indexOf(100));   // -1
```

#### 15. `lastIndexOf(item)`
Same, but gives the index of the **last occurrence**.
```javascript
console.log([10, 20, 10, 30].lastIndexOf(10));   // 2
```

#### 16. `find(callback)`
Returns the **first element** that passes the test, or `undefined`.
```javascript
const found = [5, 12, 8, 130].find(x => x > 10);
console.log(found);   // 12  ← the VALUE
```

#### 17. `findIndex(callback)`
Returns the **index** of the first element that passes, or `-1`.
```javascript
const idx = [5, 12, 8, 130].findIndex(x => x > 10);
console.log(idx);     // 1   ← the INDEX
```

#### 18. `includes(item)`
Checks if a value exists. Returns a boolean. **Cleaner than `indexOf(x) !== -1`.**
```javascript
console.log(["apple", "banana"].includes("banana"));   // true
```

### PART 4 — Testing and filling

#### 19. `entries()`
Returns an iterator of `[index, value]` pairs.
```javascript
for (const [i, val] of ["a", "b"].entries()) {
  console.log(i, val);   // 0 "a" / 1 "b"
}
```

#### 20. `every(callback)`
Returns `true` only if **ALL** elements pass the test.
```javascript
console.log([2, 4, 6].every(x => x % 2 === 0));   // true
console.log([2, 5, 6].every(x => x % 2 === 0));   // false
```

#### 21. `some(callback)`
Returns `true` if **AT LEAST ONE** element passes.
```javascript
console.log([1, -2, 3].some(x => x < 0));   // true
```

#### 22. `fill(value, start, end)`
Fills the array with a static value. ⚠️ Mutates.
```javascript
console.log([1, 2, 3, 4].fill(0, 1, 3));   // [1, 0, 0, 4]
console.log(new Array(5).fill(0));         // [0, 0, 0, 0, 0]  ← handy!
```

#### 23. `copyWithin(target, start, end)`
Copies part of the array to another position within itself. ⚠️ Mutates. Rare.
```javascript
console.log([1,2,3,4,5].copyWithin(0, 3));   // [4, 5, 3, 4, 5]
```

#### 24. `valueOf()`
Returns the array itself (the primitive value). Rarely used directly.

### PART 5 — The iteration methods (the important ones)

These four are what you'll reach for every day.

#### 25. `forEach(callback)`
Runs a function **once for each element**. **Returns `undefined`** — you can't chain it.
Use it for side effects (logging, DOM updates).
```javascript
[1, 2, 3].forEach((value, index, array) => {
  console.log(index, value);
});
```
> ⚠️ You **cannot** `break` out of a `forEach`. Use a `for...of` loop if you need to stop early.

#### 26. `map(callback)`
Creates a **new array** with the results of calling a function on **every** element.
**Same length as the original.** ✅ Non-mutating.
```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(n => n * 2);
console.log(doubled);   // [2, 4, 6, 8]
console.log(numbers);   // [1, 2, 3, 4] — unchanged ✅

// Very common: extracting a field from objects
const users = [{name: "Ann", age: 30}, {name: "Bob", age: 25}];
const names = users.map(u => u.name);   // ["Ann", "Bob"]
```

#### 27. `filter(callback)`
Creates a **new array** with **all elements that pass the test**. Can be shorter than the
original. ✅ Non-mutating.
```javascript
const numbers = [1, 2, 3, 4, 5];
const evens = numbers.filter(n => n % 2 === 0);
console.log(evens);   // [2, 4]

const adults = users.filter(u => u.age >= 18);
```

#### 28. `reduce(callback, initialValue)`
Executes a "reducer" function on each element, **resulting in a single output value**.
The most powerful — and most confusing — array method.

```javascript
array.reduce((accumulator, currentValue, index, array) => {
  return newAccumulator;
}, initialValue);
```

- **accumulator** — the running total, carried from one iteration to the next
- **currentValue** — the current element
- **initialValue** — the accumulator's starting value (⚠️ always provide this)

```javascript
// Sum
const sum = [1, 2, 3, 4].reduce((acc, curr) => acc + curr, 0);
console.log(sum);   // 10

// Max
const max = [3, 7, 2].reduce((a, b) => a > b ? a : b);

// Count occurrences → build an object
const fruits = ["apple", "banana", "apple"];
const counts = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});
console.log(counts);   // { apple: 2, banana: 1 }

// Flatten
const flat = [[1,2],[3,4]].reduce((acc, arr) => acc.concat(arr), []);
console.log(flat);     // [1, 2, 3, 4]
```

#### 29. `reduceRight(callback, init)`
Same as `reduce`, but processes the array **right to left**.

#### 30. `Array.from(iterable, mapFn)`
Creates a real array from anything array-**like** or iterable — strings, NodeLists,
`arguments`, Sets.
```javascript
Array.from("hello");                       // ["h","e","l","l","o"]
Array.from({length: 5}, (_, i) => i);      // [0, 1, 2, 3, 4]
Array.from(document.querySelectorAll("p")); // NodeList → real Array
```

### Chaining methods together

Because `map` and `filter` return arrays, you can chain them. This is where the style shines.

```javascript
const products = [
  { name: "Laptop", price: 1000, inStock: true },
  { name: "Mouse",  price: 25,   inStock: true },
  { name: "Screen", price: 300,  inStock: false }
];

const total = products
  .filter(p => p.inStock)          // only in-stock items
  .map(p => p.price)               // grab the prices
  .reduce((sum, p) => sum + p, 0); // add them up

console.log(total);   // 1025
```

---

## 28. Objects

> **An object is a collection of properties, where each property is defined by a key
> (a property name) and a corresponding value.**

- The **key** is always a string (or a Symbol).
- The **value** can be any data type — including other objects and functions.
- If a key's value is a **function**, it's called a **method**.

JavaScript is an **object-based**, **prototype-based** language. It is *template-based*, not
strictly class-based — you don't need to create a class to get an object; you can create
objects directly.

### The three ways to create an object

#### 1. Object literal (by far the most common)

```javascript
let person = {
  name: 'John',                  // property: key 'name', value 'John'
  age: 30,                       // property
  greet: function() {            // METHOD (a function as a value)
    console.log('Hello!');
  },
  sayHi() {                      // ES6 shorthand for a method — same thing
    console.log('Hi!');
  }
};
```

#### 2. By creating an instance of Object directly

```javascript
let emp = new Object();
emp.id = 101;
emp.name = "Ravi Malik";
emp.salary = 50000;
console.log(emp.id + " " + emp.name + " " + emp.salary);
// 101 Ravi Malik 50000
```

#### 3. By using an object constructor

Create a function with arguments. Each argument value is assigned onto the current object
using the `this` keyword.

```javascript
function emp(id, name, salary) {
  this.id = id;
  this.name = name;
  this.salary = salary;
}
let e = new emp(103, "Vimal Jaiswal", 30000);
console.log(e.id + " " + e.name + " " + e.salary);
// 103 Vimal Jaiswal 30000
```

### Accessing properties

**Dot notation** — clean, use it by default:
```javascript
console.log(person.name);      // "John"
person.greet();                // calls the method
```

**Bracket notation** — needed when the key is dynamic or has special characters:
```javascript
console.log(person['age']);              // 30
let key = "name";
console.log(person[key]);                // "John"   ← dynamic key
console.log(person['my-weird-key']);     // dot notation would break here
```

### Nested objects

```javascript
let user = {
  name: "Jane Doe",
  address: { street: "123 Main St", city: "Anytown" }
};
console.log(user.address.city);      // "Anytown"
console.log(user.address?.zip);      // undefined — optional chaining, no crash
```

> ⚠️ `user.someProp.x` throws an error if `someProp` doesn't exist, because `someProp` is
> `undefined` and `undefined` has no property `x`. Use **optional chaining** `?.` to be safe.

### Adding, modifying, deleting

```javascript
person.name = 'Jane';           // modify an existing property
person.city = 'New York';       // add a new property
delete person.age;              // remove a property
```

### Checking for a property

```javascript
console.log('name' in person);                 // true
console.log(person.hasOwnProperty('name'));    // true (ignores inherited)
console.log(person.name !== undefined);        // true
```

---

## 29. Object Methods

`Object` is a built-in with static helper methods. These are the ones you'll actually use.

### The essential trio

```javascript
const obj = { name: "John", age: 30 };

Object.keys(obj);     // ["name", "age"]           ← array of KEYS
Object.values(obj);   // ["John", 30]              ← array of VALUES
Object.entries(obj);  // [["name","John"],["age",30]]  ← array of [key,value] pairs
```

These make objects loopable with array methods:
```javascript
Object.entries(obj).forEach(([key, value]) => {
  console.log(`${key}: ${value}`);
});
```

### Full reference

| Method | What it does |
|---|---|
| `Object.assign(target, ...sources)` | Copies enumerable own properties from source objects to a target object |
| `Object.create(proto)` | Creates a new object with the specified prototype object |
| `Object.defineProperty(obj, key, descriptor)` | Adds/modifies a **single** property with specific behavioural attributes |
| `Object.defineProperties(obj, descriptors)` | Adds/modifies **multiple** properties |
| `Object.entries(obj)` | Array of `[key, value]` pairs |
| `Object.keys(obj)` | Array of an object's own enumerable property **names** |
| `Object.values(obj)` | Array of **values** |
| `Object.freeze(obj)` | **Freezes** it — no modifying, adding, or deleting |
| `Object.isFrozen(obj)` | Checks whether an object was frozen |
| `Object.seal(obj)` | **Seals** it — no adding or deleting, but **modifying is allowed** |
| `Object.isSealed(obj)` | Checks whether an object is sealed |
| `Object.preventExtensions(obj)` | Prevents any new properties being added |
| `Object.isExtensible(obj)` | Checks if an object is extensible |
| `Object.getOwnPropertyNames(obj)` | Array of **all** property names, including non-enumerable |
| `Object.getOwnPropertyDescriptor(obj, key)` | Returns the descriptor for one property |
| `Object.getOwnPropertyDescriptors(obj)` | Returns all own property descriptors |
| `Object.getOwnPropertySymbols(obj)` | Array of all own Symbol-keyed properties |
| `Object.getPrototypeOf(obj)` | Returns the prototype (internal `[[Prototype]]`) |
| `Object.setPrototypeOf(obj, proto)` | Sets the prototype to another object |
| `Object.is(a, b)` | Determines whether two values are the same value |
| `obj.hasOwnProperty(key)` | Does the object have this as its *own* property? |

### freeze vs seal — the difference

| | Modify existing | Add new | Delete |
|---|:---:|:---:|:---:|
| **`Object.seal()`** | ✅ Yes | ❌ No | ❌ No |
| **`Object.freeze()`** | ❌ No | ❌ No | ❌ No |

```javascript
const car = { color: "red", mileage: 100 };

Object.seal(car);
car.color = "blue";       // ✅ modifying keys IS possible
car.price = 20000;        // ❌ adding is silently ignored
delete car.color;         // ❌ deleting is silently ignored
console.log(Object.isSealed(car));   // true

const pen = { color: "blue" };
Object.freeze(pen);
pen.color = "red";        // ❌ modify, add, and delete are ALL blocked
console.log(Object.isFrozen(pen));   // true
```

> 💡 In strict mode these silent failures become thrown errors.

### Copying objects

```javascript
const obj1 = { a: 1 }, obj2 = { b: 2 };

// Shallow copy / merge
const merged  = Object.assign({}, obj1, obj2);   // { a: 1, b: 2 }
const merged2 = { ...obj1, ...obj2 };            // same, but nicer (spread)

// Deep copy (nested objects too)
const deep = structuredClone(original);          // modern, best
const deep2 = JSON.parse(JSON.stringify(original)); // old trick, loses functions/dates
```

> ⚠️ **Shallow copy** only copies the top level. Nested objects are still shared by reference.

---

## 30. Destructuring

Destructuring extracts values from arrays or properties from objects into **distinct
variables**, in one line.

### Array destructuring

```javascript
// Basic
let [a, b] = [1, 2];                     // a = 1, b = 2

// Skipping values — leave a gap
let [x, , z] = [1, 2, 3];                // x = 1, z = 3

// Default values (used if the element is undefined)
let [p = 5, q = 10] = [1];               // p = 1, q = 10

// Rest — collect the remaining items into a new array
let [first, ...rest] = [1, 2, 3, 4];     // first = 1, rest = [2, 3, 4]

// Nested arrays
let [m, [n, o]] = [1, [2, 3]];           // m = 1, n = 2, o = 3

// Swapping variables — no temp variable needed!
let i = 1, j = 2;
[i, j] = [j, i];                         // i = 2, j = 1
```

### Object destructuring

```javascript
const person = { name: "John", age: 30, address: { city: "NY", country: "USA" } };

// Basic — the variable name must MATCH the key
const { name, age } = person;            // name = "John", age = 30

// Renaming — key: newVariableName
const { name: fullName, age: yearsOld } = person;   // fullName, yearsOld

// Default values
const { name = "Guest", nickname = "none" } = person;  // nickname = "none"

// Rest — collect the remaining properties into a new object
const { name: n2, ...others } = person;  // others = { age: 30, address: {...} }

// Nested destructuring
const { address: { city, country } } = person;   // city = "NY", country = "USA"
```

### Destructuring in function parameters

Extremely common in modern JavaScript — especially in React.

```javascript
function greet({ name, age }) {
  console.log(name, age);
}
greet({ name: "John", age: 30 });   // "John 30"

// With defaults, so calling it with no argument doesn't crash
function config({ width = 100, height = 50 } = {}) {
  console.log(width, height);
}
config();                  // 100 50
config({ width: 200 });    // 200 50
```

---

## 31. Spread & Rest Operators

Both are written `...`. **The position tells you which one it is.**

> **Spread** = *unpacking* — it takes a collection apart into individual pieces.
> **Rest** = *packing* — it gathers individual pieces into a collection.

### Spread — expands an iterable into individual elements

**In arrays:**
```javascript
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];              // [1, 2, 3, 4, 5]
let copy = [...arr1];                    // a real copy, not a reference ✅
let merged = [...[1,2], ...[3,4]];       // [1, 2, 3, 4]
```

**In objects (ES2018):**
```javascript
let obj1 = { name: "John", age: 30 };
let obj2 = { ...obj1, city: "New York" };
// { name: "John", age: 30, city: "New York" }

// Later properties WIN — great for overriding defaults
const defaults  = { color: "red", size: "M" };
const userPrefs = { size: "L", theme: "dark" };
const combined  = { ...defaults, ...userPrefs };
// { color: "red", size: "L", theme: "dark" }
```

**In function calls:**
```javascript
function sum(x, y, z) { return x + y + z; }
const numbers = [1, 2, 3];
console.log(sum(...numbers));            // 6

console.log(Math.max(...[3, 7, 2]));     // 7
```

**On strings:**
```javascript
console.log([..."hello"]);               // ["h","e","l","l","o"]
```

### Rest — collects remaining items into a collection

**In function parameters:**
```javascript
function collectArgs(first, ...rest) {
     console.log(first);   // 1
     console.log(rest);    // [2, 3, 4, 5]   ← a REAL array
}
collectArgs(1, 2, 3, 4, 5);
```
> ⚠️ The rest parameter must be the **last** parameter.

**In array destructuring:**
```javascript
let [a, ...rest] = [1, 2, 3, 4];         // a = 1, rest = [2, 3, 4]
```

**In object destructuring:**
```javascript
let { name, ...rest } = { name: "John", age: 30, city: "New York" };
// name = "John", rest = { age: 30, city: "New York" }
```

---

## 32. Set & Map

Two ES6 data structures that solve problems plain objects and arrays handle badly.

### Set — a collection of **unique** values

```javascript
let set = new Set([1, 2, 2, 3]);     // duplicates are automatically dropped
console.log(set);                    // Set(3) {1, 2, 3}

set.add(4);                          // add a value
set.has(2);                          // true — check if a value exists
set.delete(1);                       // remove a value
console.log(set.size);               // number of elements (NOT .length)
set.clear();                         // remove everything
```

**Killer use case — removing duplicates from an array:**
```javascript
const nums = [1, 2, 2, 3, 3, 3];
const unique = [...new Set(nums)];   // [1, 2, 3]
```

### Map — key-value pairs where **the key can be anything**

Unlike objects (whose keys must be strings/Symbols), a Map's key can be a number, an object,
even a function. Maps also remember **insertion order**.

```javascript
let map = new Map();

map.set("name", "Jaid");             // add a key-value pair
map.set(1, "number key");            // ← a number as a key!
map.set({id: 1}, "object key");      // ← an object as a key!

console.log(map.get("name"));        // "Jaid"
console.log(map.has("name"));        // true
map.delete("name");                  // remove
console.log(map.size);               // number of entries
map.clear();

// Iterating
for (const [key, value] of map) {
  console.log(key, value);
}
```

### Object vs Map — when to use which

| | Object | Map |
|---|---|---|
| Key types | Strings & Symbols only | **Anything** |
| Order | Not guaranteed | **Insertion order preserved** |
| Size | `Object.keys(o).length` | `map.size` |
| Iterating | Needs `Object.entries()` | Directly iterable |
| Best for | Records with known fields | Dynamic key-value lookups, caches |

---

## 33. JSON

**JSON** = JavaScript Object Notation. A **text format** for sending data between a server and
a browser. It looks like a JavaScript object, but it's actually a **string**.

Two methods, and that's it:

| Method | Direction |
|---|---|
| `JSON.stringify(obj)` | **Object ➔ String** |
| `JSON.parse(str)` | **String ➔ Object** |

```javascript
let user = { name: "Jaid", age: 22 };

let jsonStr = JSON.stringify(user);
console.log(jsonStr);              // '{"name":"Jaid","age":22}'   ← a STRING
console.log(typeof jsonStr);       // "string"

let backToObj = JSON.parse(jsonStr);
console.log(backToObj.name);       // "Jaid"                        ← an OBJECT again
console.log(typeof backToObj);     // "object"
```

**Pretty-printing** (add indentation for readability):
```javascript
console.log(JSON.stringify(user, null, 2));
/*
{
  "name": "Jaid",
  "age": 22
}
*/
```

### JSON rules you must follow

- Keys **must** be in double quotes: `{"name": "x"}` ✅, `{name: "x"}` ❌
- Only double quotes for strings — no single quotes
- No trailing commas
- No comments
- **Functions, `undefined`, and Symbols are silently dropped** by `stringify`
- Dates become strings (you must convert them back yourself)

> ⚠️ `JSON.parse()` throws a `SyntaxError` on malformed JSON. Always wrap it in `try...catch`
> when parsing data you didn't create.

---

## 34. Date Object

The Date object is used to work with dates and times. It has methods to get and set the day,
month, year, hour, minute, and seconds.

### Creating dates

```javascript
let now = new Date();                       // current date and time
let birthday = new Date("2000-01-01");      // from a string (YYYY-MM-DD)
let specific = new Date(2024, 0, 15);       // year, month(0-11!), day
let fromMs = new Date(1700000000000);       // from a timestamp
console.log(Date.now());                    // milliseconds since 1 Jan 1970
```

> ⚠️ **Months are 0-indexed!** January is `0`, December is `11`. Days of the week are also
> 0-indexed (Sunday = 0).

### Getting parts of a date

```javascript
let d = new Date();

d.getFullYear();      // 2026   — the year (4 digits)
d.getMonth();         // 0-11   — the month ⚠️ zero-based
d.getDate();          // 1-31   — the day of the month
d.getDay();           // 0-6    — the day of the week (0 = Sunday)
d.getHours();         // 0-23
d.getMinutes();       // 0-59
d.getSeconds();       // 0-59
d.getMilliseconds();  // 0-999
d.getTime();          // milliseconds since 1 Jan 1970 (the "epoch")
```

### Setting parts of a date

```javascript
d.setFullYear(2030);
d.setMonth(11);        // December
d.setDate(25);
d.setHours(12);
```

### Formatting

```javascript
d.toString();          // "Mon Sep 08 2026 ..."
d.toDateString();      // "Mon Sep 08 2026"
d.toISOString();       // "2026-09-08T10:30:00.000Z"  ← best for storing/sending
d.toLocaleDateString();// "9/8/2026" (depends on the user's locale)
d.toLocaleTimeString();// "10:30:00 AM"
d.toLocaleDateString('en-GB');  // "08/09/2026"
```

### Comparing dates

Because dates convert to numbers (milliseconds), you can compare them directly:

```javascript
const d1 = new Date("2024-01-01");
const d2 = new Date("2024-06-01");

console.log(d1 < d2);                   // true
console.log(d1.getTime() === d2.getTime());  // ⚠️ use getTime() for EQUALITY

// Difference in days
const diffMs = d2 - d1;
const diffDays = diffMs / (1000 * 60 * 60 * 24);
console.log(diffDays);                  // 152
```

> ⚠️ `d1 === d2` is **always false** for two separate Date objects, even with identical
> values — because objects are compared by reference. Use `.getTime()`.

### Formatting with Intl (modern, locale-aware)

```javascript
const formatter = new Intl.DateTimeFormat('en-US');
console.log(formatter.format(new Date()));

const numberFormatter = new Intl.NumberFormat('en-US');
console.log(numberFormatter.format(1234567.89));   // "1,234,567.89"
```

---

## 35. Math & Number

### The Math object

`Math` is a built-in object with constants and methods for mathematical operations.
You never create a `new Math()` — you just call its methods directly.

```javascript
Math.PI                 // 3.141592653589793

Math.round(4.7)         // 5    — round to the NEAREST integer
Math.round(4.4)         // 4
Math.floor(4.9)         // 4    — round DOWN always
Math.ceil(4.1)          // 5    — round UP always
Math.trunc(4.9)         // 4    — just chop off the decimal
Math.abs(-5)            // 5    — absolute value

Math.max(3, 7, 2)       // 7
Math.min(3, 7, 2)       // 2
Math.max(...[3, 7, 2])  // 7    — with an array, use spread

Math.sqrt(16)           // 4    — square root
Math.pow(2, 3)          // 8    — 2 to the power of 3 (same as 2 ** 3)
Math.exp(1)             // 2.718... — E^x
Math.log(10)            // natural logarithm

Math.random()           // a random decimal between 0 (inclusive) and 1 (exclusive)
```

**Random number recipes:**
```javascript
// Random integer from 0 to 9
Math.floor(Math.random() * 10);

// Random integer between min and max (inclusive)
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
randomInt(1, 6);        // a dice roll

// Random item from an array
const arr = ["a", "b", "c"];
arr[Math.floor(Math.random() * arr.length)];
```

### Number methods

```javascript
// Parsing strings into numbers
Number.parseInt("42px", 10);     // 42     (radix 10 = decimal)
Number.parseFloat("42.5kg");     // 42.5
parseInt("42");                  // 42     (the global version works too)
parseFloat("42.5");              // 42.5

// Checking
Number.isNaN(NaN);               // true
Number.isFinite(42);             // true
Number.isInteger(42.0);          // true
Number.isInteger(42.5);          // false

// Formatting
(3.14159).toFixed(2);            // "3.14"   ⚠️ returns a STRING
(1234.5678).toFixed(0);          // "1235"
(0.000123).toExponential(2);     // "1.23e-4"  — exponential form
(123.456).toPrecision(4);        // "123.5"    — format to a total length
(255).toString(2);               // "11111111" — binary
(255).toString(16);              // "ff"       — hexadecimal
(42).valueOf();                  // 42         — the primitive value
```

**Global functions:**
```javascript
isNaN("hello");        // true   (coerces first — less strict)
isFinite("42");        // true   (coerces first)
encodeURIComponent("a b");   // "a%20b"
decodeURIComponent("a%20b"); // "a b"
```

> ⚠️ **The floating-point trap:** `0.1 + 0.2 === 0.3` is **`false`** (it's
> `0.30000000000000004`). This affects every language that uses IEEE-754 floats.
> Fix: `Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON`, or work in integers (cents, not dollars).

---

## 36. Regular Expressions

Regular expressions (regex) are **search patterns** used to match combinations of characters
in a string. Useful for both text search and text replacement.

### Creating and using

```javascript
const regex1 = /hello/gi;                    // literal notation (preferred)
const regex2 = new RegExp("hello", "gi");    // constructor notation

// The two RegExp methods
regex1.test("say hello");        // true  — does it match? returns a boolean
regex1.exec("say hello");        // returns match details, or null

// The String methods that take a regex
"say hello".match(/hello/);      // returns the match
"say hello".search(/hello/);     // returns the index (4)
"say hello".replace(/hello/, "hi");   // "say hi"
"a1b2".split(/\d/);              // ["a", "b", ""]
```

### Pattern modifiers (flags)

Put these after the closing `/`.

| Flag | Meaning |
|---|---|
| `g` | **Global** matching — find all matches, not just the first |
| `i` | Case-**insensitive** matching |
| `m` | **Multi-line** matching |
| `s` | Treat the string as a **single** line (`.` matches newlines too) |
| `U` | Ungreedy pattern |
| `x` | Allow comments and whitespace in the pattern |
| `e` | Evaluate replacement |

### Metacharacters

| Pattern | Finds |
|---|---|
| `.` | Any single character **except** a newline or line terminator |
| `\w` | Word characters (letters, digits, underscore) |
| `\W` | **Non**-word characters |
| `\s` | Whitespace characters |
| `\S` | **Non**-whitespace characters |
| `\b` | A match at the **beginning or end of a word** |
| `\B` | A match **not** at the beginning or end of a word |
| `\d` | Digits (0–9) |
| `\D` | **Non**-digit characters |
| `\0` | NULL character |
| `\n` | A newline character |
| `\f` | A form-feed character |
| `\r` | A carriage-return character |
| `\t` | A tab character |
| `\v` | A vertical-tab character |
| `\xxx` | Character given by the octal number xxx |
| `\xdd` | Character given by the hexadecimal number dd |
| `\uxxxx` | The Unicode character given by hex number XXXX |

### Brackets

Group parts of a regex together by putting them inside round brackets (parentheses).

| Pattern | Finds |
|---|---|
| `[abc]` | Any one of the characters between the brackets |
| `[^abc]` | Every character **NOT** in the brackets |
| `(a\|b\|c)` | Any of the alternatives separated by `\|` |
| `[0-9]` | Each digit from 0 to 9 |
| `[A-z]` | Each character from uppercase A to lowercase z |

### Quantifiers

Quantifiers give the minimum number of instances of a character, group, or character class
required for a match.

| Pattern | Matches |
|---|---|
| `n+` | A string having **one or more** `n` |
| `n*` | A string having **zero or more** occurrences of `n` |
| `n?` | A string having **zero or one** occurrence of `n` |
| `^n` | A string with `n` in the **first** place |
| `n$` | A string with `n` at the **end** |
| `?=n` | Strings **followed by** a particular string |
| `?!n` | Strings **not followed by** a particular string |
| `n{X}` | A sequence of exactly **X** `n`s |
| `n{X,Y}` | A sequence of **X to Y** `n`s |
| `n{X,}` | A sequence of **X or more** `n`s |

### Practical patterns

```javascript
// Email (basic)
const email = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
email.test("user@example.com");     // true

// Phone (10 digits)
const phone = /^\d{10}$/;

// Password: min 8 chars, 1 uppercase, 1 lowercase, 1 digit
const pwd = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;

// Extract all numbers from a string
"a1b22c333".match(/\d+/g);          // ["1", "22", "333"]

// Remove all whitespace
"a b  c".replace(/\s+/g, "");       // "abc"
```

---
---

# PART 5 — OBJECT-ORIENTED JAVASCRIPT

---

## 37. The `this` Keyword

> **`this` is a reference variable that points to the object that is currently executing
> the function.**

The value of `this` is **not** decided by where the function is written. It is decided by
**HOW the function is called**. This is the single most confusing thing in JavaScript, so
learn the rules one by one.

### Rule 1 — `this` inside a plain function → the global object

```javascript
var name = "Fatema";      // declaring with `var` in global scope attaches it to `window`

function fun() {
  console.log(this.name);
}
fun();                    // "Fatema" — `this` is the window object
```

In a browser the global object is **`window`**. In Node.js it's **`global`**.

> ⚠️ In **strict mode**, `this` is `undefined` here instead of `window`.

### Rule 2 — `this` inside a method → the object that owns the method

The rule of thumb: **`this` refers to whatever is to the left of the dot.**

```javascript
var address = {
  company: "Javatpoint",
  city: "Noida",
  state: "UP",
  fullAddress: function() {
     return this.company + " " + this.city + " " + this.state;
  }
};

console.log(address.fullAddress());   // "Javatpoint Noida UP"
//          ^^^^^^^ this = address
```

Another example:
```javascript
const carDetails = {
  name: "Ford Mustang",
  getName() { return this.name; }
};
console.log(carDetails.getName());   // "Ford Mustang" ✅
```

### Rule 3 — losing `this` (the classic bug)

```javascript
var name = "Ford Ranger";                  // becomes window.name
var getCarName = carDetails.getName;       // we detached the method from its object!

console.log(getCarName());   // "Ford Ranger"  ⚠️ NOT "Ford Mustang"
```

**Why?** When you assign the method to a variable and call it standalone, there's no longer
an object to the left of the dot. It falls back to Rule 1, so `this` becomes `window`. And
because `var name` in global scope creates `window.name`, `this.name` finds `"Ford Ranger"`.

```javascript
console.log(getCarName === window.getCarName);   // true
```

### Rule 4 — inner functions also lose `this`

IIFEs, functions declared in the global scope, anonymous functions, and **inner functions
inside a method** all default to `this === window`.

```javascript
const myObj = {
  name: 'Marko Polo',
  guessThis() {
    function getThis() {
      console.log(this);      // ⚠️ the WINDOW object, not myObj!
    }
    getThis();
  },
  thisIsAnnoying(callback) {
    callback();
  }
};

myObj.guessThis();                              // logs window
myObj.thisIsAnnoying(function(){ console.log(this); });  // logs window
```

**Fix 1 — save `this` in a variable (the old `self`/`that` pattern):**
```javascript
const myObj = {
  name: 'Marko Polo',
  guessThis() {
    const self = this;          // save the correct `this`
    function getName() {
      console.log(self.name);   // "Marko Polo" ✅
    }
    getName();
  }
};
```

**Fix 2 — use an arrow function (the modern way):**
```javascript
const myObj = {
  name: 'Marko Polo',
  guessThis() {
    const getName = () => {
      console.log(this.name);   // "Marko Polo" ✅
    };
    getName();
  }
};
```

### Rule 5 — arrow functions have NO `this` of their own

> **Arrow functions do not bind their own `this`. They inherit it lexically — from the
> enclosing scope where they were written.**

This is their most important property, and why they fixed a decade of `this` bugs.

```javascript
const arrowObject = {
    name: "Arrow Guy",
    sayName: function() {
        // here `this` = arrowObject
        const innerArrow = () => {
            console.log(this.name);   // also arrowObject — inherited lexically ✅
        };
        innerArrow();
    }
};
arrowObject.sayName();   // "Arrow Guy"
```

> ⚠️ **But never use an arrow function as an object method:**
> ```javascript
> const obj = {
>   name: "Test",
>   greet: () => console.log(this.name)   // ❌ `this` is window, NOT obj
> };
> ```
> There's no enclosing function, so it inherits from global scope.

### Rule 6 — `this` in a constructor → the newly created object

When a function is called with the `new` keyword, `this` points to the brand-new object.

```javascript
function Person(name) {
  this.name = name;      // `this` = the new object being built
}
const p = new Person("Ann");
console.log(p.name);     // "Ann"
```

### Rule 7 — explicit binding with call/apply/bind

`this` is explicitly set to whatever you pass in. (See the next section.)

### Rule 8 — `this` in event handlers → the element that received the event

```javascript
button.addEventListener('click', function() {
  console.log(this);     // the <button> element
});

button.addEventListener('click', () => {
  console.log(this);     // ⚠️ window — arrow functions don't rebind
});
```

### The complete `this` summary table

| How the function is called | What `this` is |
|---|---|
| Plain function call | `window` (or `undefined` in strict mode) |
| Method call `obj.method()` | `obj` — whatever is left of the dot |
| Constructor `new Fn()` | The newly created object |
| Arrow function | Inherited from the enclosing lexical scope |
| `fn.call(x)` / `fn.apply(x)` | `x` |
| `fn.bind(x)()` | `x` |
| DOM event handler | The element that received the event |
| Class method | The instance |

---

## 38. call, apply, and bind

These three methods let you **explicitly set what `this` will be**. They allow you to write a
method once and use it on many different objects.

### `call(thisArg, arg1, arg2, ...)`

Calls the function **immediately**, with arguments passed **individually**.

```javascript
var emp_address = {
   fullAddress: function() {
       return this.company + " " + this.city + " " + this.state;
   }
};

var address = { company: "Javatpoint", city: "Noida", state: "UP" };

console.log(emp_address.fullAddress.call(address));   // "Javatpoint Noida UP"
```

### `apply(thisArg, [argsArray])`

Identical to `call`, but arguments are passed as **an array**.

```javascript
console.log(emp_address.fullAddress.apply(address));

function introduce(greeting, punctuation) {
  return `${greeting}, I'm ${this.name}${punctuation}`;
}
const person = { name: "Ann" };

introduce.call(person, "Hi", "!");      // "Hi, I'm Ann!"     — individual args
introduce.apply(person, ["Hi", "!"]);   // "Hi, I'm Ann!"     — array of args
```

> **Memory aid:** **A**pply takes an **A**rray. **C**all takes a **C**omma-separated list.

### `bind(thisArg, ...args)`

Introduced in ECMAScript 5. **Does NOT call the function.** Instead it **creates and returns
a NEW function** whose `this` is permanently locked to the provided value.

```javascript
var lang = "Java";

function lang_name(call) {
  call();
}

var obj = {
  lang: "JavaScript",
  language: function() {
    console.log(this.lang + " is a popular programming language");
  }
};

lang_name(obj.language);              // "undefined is a popular..." ⚠️ `this` was lost
lang_name(obj.language.bind(obj));    // "JavaScript is a popular..." ✅ `this` locked
```

**The most common real-world use — preserving `this` in a callback:**
```javascript
class Timer {
  constructor() { this.seconds = 0; }
  start() {
    setInterval(this.tick.bind(this), 1000);   // without .bind, `this` would be window
  }
  tick() { this.seconds++; console.log(this.seconds); }
}
```

**Partial application** — pre-filling some arguments:
```javascript
function multiply(a, b) { return a * b; }
const double = multiply.bind(null, 2);   // lock a = 2
console.log(double(5));                  // 10
```

### The three compared

| | Calls immediately? | Arguments | Returns |
|---|:---:|---|---|
| `call` | ✅ Yes | Comma-separated | The function's result |
| `apply` | ✅ Yes | An array | The function's result |
| `bind` | ❌ No | Comma-separated | **A new bound function** |

---

## 39. Constructor Functions

> **A constructor is a special function that acts as a mould to create new objects.**

JavaScript has many built-in constructors: `String`, `Number`, `Boolean`, `Promise`, `Date`,
`Array`, `Object`, `RegExp` and more. You can also create your own.

**A great place to use a constructor is when you're creating multiple objects of the same
kind.**

There are two parts to working with a constructor:
1. **Defining** a constructor
2. **Using** it with the `new` keyword

```javascript
// (1) Defining a constructor — name it with a Capital Letter by convention
function Car(make, model, year) {
    this.make  = make;
    this.model = model;
    this.year  = year;

    this.setMiles = function(miles) {
        this.miles = miles;
        return miles;
    };
}

// (2) Using a constructor — the `new` keyword creates a new instance
const car1 = new Car('Toyota', 'Prius',  2016);
const car2 = new Car('Hyundai', 'Sonata', 2018);

console.log(car1.make);   // "Toyota"
```

### What `new` actually does — four steps

1. Creates a brand-new empty object `{}`
2. Sets that object's prototype to `Car.prototype`
3. Binds `this` inside the function to the new object
4. Returns the new object automatically (you don't write `return`)

> ⚠️ **Forget `new` and everything breaks:** `const c = Car('Toyota', ...)` would set
> properties on `window` and return `undefined`. This is why classes (which throw an error
> if you forget `new`) are safer.

### Adding methods to the prototype

> **Rule of thumb:**
> **A) Set properties inside the constructor.**
> **B) Set methods inside the `prototype` property.**

```javascript
Car.prototype.age = function() {
    return (new Date()).getFullYear() - this.year;
};

console.log(car1.age());   // 10 (in 2026)
```

**Why?** If you define methods inside the constructor, **every single instance gets its own
separate copy** of that function — wasting memory. Methods on the prototype are stored
**once** and shared by all instances.

---

## 40. Prototypes & Prototype Chaining

> **JavaScript is a prototype-based language.** Objects acquire properties and features from
> one another. **Each object contains a prototype object.**

### Auto-inherited properties

When you create a value in JavaScript, certain properties are **automatically inherited** by
it. This works because every type has a constructor with a special property called
**`prototype`**. All methods on that prototype get automatically inherited by every new value
created for that type.

```javascript
const thing = "some text";
thing.toUpperCase();     // where did this method come from? String.prototype
thing.split(" ");        // String.prototype
thing.indexOf("t");      // String.prototype

const num = 123.45;
num.toFixed(2);          // Number.prototype

const arr = [1, 2, 3];
arr.map(x => x);         // Array.prototype
```

That's why `.filter()`, `.map()`, `.find()`, `.every()`, `.some()`, `.sort()`, `.slice()`,
`.splice()`, `.reduce()`, `.forEach()` exist on **every** array you create — they live on
`Array.prototype`.

### Prototype chaining

> **Each object contains a prototype object that acquires properties and methods from it.
> Again, that prototype object may itself contain a prototype object, and so on. This is
> prototype chaining.**

When you access a property, JavaScript:
1. Looks on the object itself.
2. If not found, looks on its prototype.
3. If not found, looks on the prototype's prototype…
4. …until it reaches `Object.prototype`, whose prototype is `null`.
5. If still not found → `undefined`.

```javascript
const animal = {
     eats: true,
     walk() { console.log("Animal walks."); }
};

const rabbit = {
     jumps: true,
     __proto__: animal      // rabbit inherits from animal
};

console.log(rabbit.jumps);   // true  — its own property
console.log(rabbit.eats);    // true  — inherited from animal ✅
rabbit.walk();               // "Animal walks." — inherited ✅
```

**Using `Object.create()` (the cleaner way):**
```javascript
const dog = Object.create(animal);
dog.barks = true;
console.log(dog.eats);   // true
```

### Prototype example with a constructor

```javascript
function Employee(firstName, lastName) {
  this.firstName = firstName;
  this.lastName  = lastName;
}

Employee.prototype.fullName = function() {
  return this.firstName + " " + this.lastName;
};

var employee1 = new Employee("Martin", "Roy");
var employee2 = new Employee("Duke", "William");

console.log(employee1.fullName());   // "Martin Roy"
console.log(employee2.fullName());   // "Duke William"
```

Both instances share **one** `fullName` function stored on `Employee.prototype`.

### Inspecting the chain

```javascript
Object.getPrototypeOf(rabbit);          // the animal object
Object.setPrototypeOf(rabbit, animal);  // set it (slow — avoid at runtime)
rabbit.__proto__;                       // same thing (legacy syntax)
```

---

## 41. Classes

> **Classes are the new (ES6) way of writing constructor functions. It is syntactic sugar —
> under the hood it still uses prototypes and prototype-based inheritance.**

Classes are a special type of function. **The class body is always executed in strict mode**,
so silent errors throw.

**Class syntax has two forms:**
- Class declaration
- Class expression

### Class Declaration

The `class` keyword declares a class with a name. **By naming convention, class names always
start with an uppercase letter.**

```javascript
class Employee {
  // Initializing an object
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }

  // Declaring a method
  detail() {
    console.log(this.id + " " + this.name);
  }
}

// Passing an object to a variable
var e1 = new Employee(101, "Martin Roy");
var e2 = new Employee(102, "Duke William");
e1.detail();   // 101 Martin Roy
e2.detail();   // 102 Duke William
```

### Class Expression

Another way to define a class. Here it is **not mandatory to assign a name**, so the class
expression can be **named or unnamed**. A class expression lets you fetch the class name —
which is not possible with a class declaration.

**Unnamed class expression:**
```javascript
var emp = class {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }
};
console.log(emp.name);   // "emp"
```

**Named class expression:**
```javascript
var emp = class Employee2 {
  constructor(id) { this.id = id; }
};
console.log(emp.name);   // "Employee2"
```

### The constructor method

> **A constructor method is a special method used to initialize and create an object. It is
> called when memory is allocated for an object.**

**Points to remember:**
- The `constructor` keyword is used to declare a constructor method.
- **A class can contain ONE constructor method only.**
- JavaScript allows us to use the parent class constructor through the **`super`** keyword.

```javascript
class Employee {
  constructor() {
    this.id = 101;
    this.name = "Martin Roy";
  }
}
var emp = new Employee();
console.log(emp.id + " " + emp.name);   // 101 Martin Roy
```

**With `super`:**
```javascript
class CompanyName {
  constructor() {
    this.company = "Javatpoint";
  }
}

class Employee extends CompanyName {
  constructor(id, name) {
    super();              // ⚠️ MUST be called before using `this`
    this.id = id;
    this.name = name;
  }
}

var emp = new Employee(1, "John");
console.log(emp.id + " " + emp.name + " " + emp.company);
// 1 John Javatpoint
```

### Getters and setters

```javascript
class Student {
  constructor() {
    var name;
    var marks;
  }
  get name()       { return this.name;  }
  set name(name)   { this.name = name;  }
  get marks()      { return this.marks; }
  set marks(marks) { this.marks = marks;}
}
```

### ES5 vs ES6 — the same thing, two ways

```javascript
// ES5 Version — constructor function
function Person(firstName, lastName, age, address){
    this.firstName = firstName;
    this.lastName  = lastName;
    this.age       = age;
    this.address   = address;
}
Person.self = function(){ return this; };                      // "static"
Person.prototype.toString = function(){ return "[object Person]"; };
Person.prototype.getFullName = function(){
  return this.firstName + " " + this.lastName;
};

// ES6 Version — class
class Person {
    constructor(firstName, lastName, age, address){
      this.firstName = firstName;
      this.lastName  = lastName;
      this.age       = age;
      this.address   = address;
    }
    static self() { return this; }
    toString(){ return "[object Person]"; }
    getFullName(){ return `${this.firstName} ${this.lastName}`; }
}
```

### Proof that classes still use prototypes

```javascript
class Something {}
function AnotherSomething(){}

const as = new AnotherSomething();
const s  = new Something();

console.log(typeof Something);         // "function"  ← a class IS a function!
console.log(typeof AnotherSomething);  // "function"
console.log(as.toString === Object.prototype.toString);  // true
console.log(s.toString  === Object.prototype.toString);  // true
// Both return true, showing we're still using prototypes under the hood, because
// Object.prototype is the last link in the prototype chain.
```

---

## 42. The Four OOP Pillars in JavaScript

### 1. Inheritance

> **Inheritance is a mechanism that allows us to create new classes on the basis of already
> existing classes. It gives the child class flexibility to reuse the methods and variables
> of a parent class.**

The **`extends`** keyword creates a child class based on a parent class. It lets the child
acquire all the properties and behaviour of its parent.

**Points to remember:**
- It maintains an **IS-A relationship** (a Dog *is an* Animal).
- `extends` is used in class expressions or class declarations.
- Using `extends`, we can acquire all the properties and behaviour of **built-in objects** as
  well as custom classes.
- We can also use a **prototype-based approach** to achieve inheritance.

```javascript
class Animal {
     constructor(name) { this.name = name; }
     speak() { console.log(`${this.name} makes a sound.`); }
}

class Dog extends Animal {
     constructor(name, breed) {
          super(name);            // call the parent constructor FIRST
          this.breed = breed;
     }
     speak() {                    // OVERRIDING the parent method
          console.log(`${this.name} (${this.breed}) barks.`);
     }
}

const myDog = new Dog("Buddy", "Golden Retriever");
myDog.speak();   // "Buddy (Golden Retriever) barks."
```

**Extending a built-in object:**
```javascript
class Moment extends Date {
  constructor() { super(); }
}
var m = new Moment();
console.log(m.getDate() + "-" + (m.getMonth() + 1) + "-" + m.getFullYear());
```

**The ES5 prototype-based equivalent:**
```javascript
function Employee(firstName, lastName, jobTitle) {
  Person.call(this, firstName, lastName);   // call the parent constructor
  this.jobTitle = jobTitle;
}
Employee.prototype = Object.create(Person.prototype);   // link the prototypes
Employee.prototype.describe = function () {
  return `I am ${this.getFullName()} and I have a position of ${this.jobTitle}`;
};
```

### 2. Encapsulation

> **Encapsulation is the process of binding data with the functions acting on that data.
> It allows us to control the data and validate it.**

To achieve encapsulation in JavaScript:
- Use the `var` keyword (or `#` private fields) to make data members **private**
- Use **setter** methods to set the data and **getter** methods to get the data

Encapsulation lets you handle an object with these properties:

| Property | How |
|---|---|
| **Read/Write** | Use setter methods to write the data and getter methods to read it |
| **Read Only** | Use getter methods **only** |
| **Write Only** | Use setter methods **only** |

```javascript
class Student {
  constructor() {
    var name;
    var marks;
  }
  get name()        { return this.name; }
  setName(name)     { this.name = name; }
  get Marks()       { return this.marks; }
  setMarks(marks)   { this.marks = marks; }
}

var stud = new Student();
stud.setName("John");
stud.setMarks(80);
console.log(stud.getName() + " " + stud.getMarks());   // John 80
```

**Modern private fields (ES2022) — genuinely private:**
```javascript
class BankAccount {
  #balance = 0;                        // # means truly private

  deposit(amount) {
    if (amount <= 0) throw new Error("Invalid amount");   // validation!
    this.#balance += amount;
  }
  get balance() { return this.#balance; }
}

const acc = new BankAccount();
acc.deposit(100);
console.log(acc.balance);     // 100
// console.log(acc.#balance); // ❌ SyntaxError — genuinely inaccessible
```

### 3. Polymorphism

> **Polymorphism is a core concept of object-oriented programming that provides a way to
> perform a single action in different forms. It provides the ability to call the same method
> on different JavaScript objects.**

Because JavaScript is **not a type-safe language**, we can pass any type of data members with
the methods.

```javascript
class A {
  display() { console.log("A is invoked"); }
}
class B extends A { }        // B inherits display() from A

var b = new B();
b.display();                 // "A is invoked"
```

**Method overriding — same name, different behaviour:**
```javascript
class Shape { area() { return 0; } }
class Circle extends Shape {
  constructor(r) { super(); this.r = r; }
  area() { return Math.PI * this.r ** 2; }
}
class Square extends Shape {
  constructor(s) { super(); this.s = s; }
  area() { return this.s ** 2; }
}

// The SAME method call produces DIFFERENT results
[new Circle(2), new Square(3)].forEach(s => console.log(s.area()));
// 12.566...
// 9
```

### 4. Abstraction

> **Abstraction is a way of hiding the implementation details and showing only the
> functionality to the users. In other words, it ignores the irrelevant details and shows
> only the required one.**

**Points to remember:**
- **We cannot create an instance of an abstract class.**
- It reduces the duplication of code.

```javascript
// Creating a constructor function that acts as an abstract class
function Vehicle() {
  this.vehicleName = "Vehicle Name";
  throw new Error("You cannot create an instance of Abstract class");
}

Vehicle.prototype.display = function() {
  return "Vehicle is: " + this.vehicleName;
};

// Creating a concrete constructor function
function Bike(vehicleName) {
  this.vehicleName = vehicleName;
}

// Creating the object WITHOUT using the function constructor
Bike.prototype = Object.create(Vehicle.prototype);
var bike = new Bike("Honda");
console.log(bike.display());     // "Vehicle is: Honda"

// var v = new Vehicle();        // ❌ Error: You cannot create an instance of Abstract class
```

---

## 43. Static Methods

> **Static methods belong to the class itself, not to an instance of that class. So an
> instance is NOT required to call a static method. These methods are called directly on the
> class itself.**

**Points to remember:**
- The `static` keyword declares a static method.
- The static method can be of any name.
- **A class can contain more than one static method.**
- If we declare more than one static method with a similar name, **JavaScript always invokes
  the last one**.
- Static methods are used to create **utility functions**.
- We **can** use the `this` keyword to call a static method within another static method.
- We **cannot** use `this` directly to call a static method within a **non-static** method.
  In that case we call it either using the class name or as a property of the constructor.

```javascript
class Test {
  static display() {
    return "static method is invoked";
  }
}
console.log(Test.display());   // "static method is invoked"
//          ^^^^ called on the CLASS, not on an instance
```

**Utility function example:**
```javascript
class MathHelper {
  static add(a, b) { return a + b; }
  static PI = 3.14159;              // static property
}
console.log(MathHelper.add(2, 3));  // 5
console.log(MathHelper.PI);         // 3.14159

// const m = new MathHelper();
// m.add(2, 3);                     // ❌ TypeError — not on the instance
```

You already use static methods every day: `Object.keys()`, `Array.isArray()`,
`Math.max()`, `Promise.all()`, `JSON.parse()` are all static.

---
---

# PART 6 — THE BROWSER

---

## 44. The Browser Structure & the Window Object

A web browser is a fairly advanced piece of software containing many components. Many of these
are **accessible to a web developer**, so we can create complex web apps. At the same time,
many components are **kept out of reach for security reasons**. For instance, we can get
access to the user's location, but we **cannot** access their saved passwords or browsing
history.

### How a browser is structured

```
┌──────────────────────────────────────────────────────┐
│ WINDOW  — each browser TAB is a window.               │
│           The outermost container a web app can       │
│           access.                                     │
│  ┌────────────────────────────────┐   Components:     │
│  │ DOCUMENT                       │   • Navigator     │
│  │  The viewport — the section    │   • HTML/CSS      │
│  │  where the website is          │     Processor     │
│  │  displayed.                    │   • JavaScript    │
│  │                                │     Engine        │
│  └────────────────────────────────┘   • Dev Tools     │
└──────────────────────────────────────────────────────┘
```

> 🔒 **Notice:** A website opened in one tab **CANNOT** access the `window` object of another
> tab. This is a core security guarantee.

### The Window object

`window` is the **global object in the browser**. Every global variable and function you
create is actually a property of `window`. Because it's global, you can omit the word
`window` — `alert()` and `window.alert()` are identical.

### Window methods & properties

| Member | What it does |
|---|---|
| `window.alert(msg)` | Show an alert box |
| `window.prompt(msg, default)` | Ask the user for input |
| `window.confirm(msg)` | Show a confirm box (OK / Cancel) |
| `window.open(url)` | Open a new browser window/tab |
| `window.close()` | Close the current window/tab |
| `window.setTimeout(fn, ms)` | Run code once, after a delay |
| `window.setInterval(fn, ms)` | Run code repeatedly, every `ms` |
| `window.clearTimeout(id)` | Cancel a `setTimeout` |
| `window.clearInterval(id)` | Cancel a `setInterval` |
| `window.scrollTo(x, y)` | Scroll the document to specific coordinates |
| `window.scrollBy(x, y)` | Scroll by a relative amount |
| `window.blur()` | Remove focus from the current window |
| `window.focus()` | Give focus to the window |
| `window.stop()` | Stop further resource loading |
| `window.moveTo(x, y)` | Move the window |
| `window.resizeTo(w, h)` | Resize the window |
| `window.location` | The current page URL object |
| `window.location.href` | Get or set the URL (setting it navigates) |
| `window.innerWidth` | Width of the browser viewport |
| `window.innerHeight` | Height of the browser viewport |

```javascript
window.alert('Hello!');
let name = window.prompt('Enter your name:');
let ok = window.confirm('Are you sure?');
window.open('https://example.com');

console.log(window.location.href);
window.location.href = 'https://example.com';    // redirect

console.log(window.innerWidth, window.innerHeight);
```

### Timers in detail

```javascript
// Run ONCE after a delay
const timeoutId = setTimeout(() => {
  console.log("Runs after 2 seconds");
}, 2000);
clearTimeout(timeoutId);        // cancel it before it fires

// Run REPEATEDLY every interval
const intervalId = setInterval(() => {
  console.log("Every 1 second");
}, 1000);
clearInterval(intervalId);      // ⚠️ ALWAYS clear intervals, or they run forever
```

> ⚠️ `setTimeout(fn, 1000)` does **not** guarantee it runs in exactly 1000ms. It means
> "run this **no sooner than** 1000ms from now" — it waits for the call stack to be empty.
> See [the Event Loop](#60-the-event-loop).

---

## 45. BOM: Navigator, Screen, History, Location

**BOM** = Browser Object Model — objects for interacting with the browser itself (as opposed
to the page's content, which is the DOM).

### Navigator object — information about the browser

| Property | Returns |
|---|---|
| `navigator.appName` | The name of the browser |
| `navigator.appVersion` | The version |
| `navigator.appCodeName` | The code name |
| `navigator.userAgent` | The full user-agent header string |
| `navigator.language` | The browser's language |
| `navigator.cookieEnabled` | `true` if cookies are enabled |
| `navigator.onLine` | `true` if the browser is online |
| `navigator.platform` | The platform, e.g. `"Win32"` |
| `navigator.product` | The engine name |
| `navigator.mimeTypes[]` | Array of MIME types (Netscape/Firefox only) |

| Method | Does |
|---|---|
| `navigator.javaEnabled()` | Checks if Java is enabled |
| `navigator.taintEnabled()` | Checks if taint is enabled (deprecated since JS 1.2) |

```javascript
console.log(navigator.userAgent);
console.log(navigator.onLine);       // true/false
```

### Screen object — information about the user's display

Accessed as `window.screen` or just `screen`.

| Property | Returns |
|---|---|
| `screen.width` | The width of the screen |
| `screen.height` | The height of the screen |
| `screen.availWidth` | The available width (minus OS taskbars) |
| `screen.availHeight` | The available height |
| `screen.colorDepth` | The colour depth |
| `screen.pixelDepth` | The pixel depth |

```javascript
console.log("Screen Width: "  + screen.width);
console.log("Screen Height: " + screen.height);
console.log("Available Width: "  + screen.availWidth);
console.log("Available Height: " + screen.availHeight);
console.log("Colour Depth: " + screen.colorDepth);
console.log("Pixel Depth: "  + screen.pixelDepth);
```

### History object

```javascript
history.back();       // go back one page (like the back button)
history.forward();    // go forward one page
history.go(-2);       // go back two pages
history.length;       // number of entries in the session history

// The History API — change the URL without reloading (used by all SPAs)
history.pushState(stateObj, 'title', 'page2.html');
history.replaceState(stateObj, 'title', 'page3.html');
```

### Location object

```javascript
location.href;         // the full URL
location.protocol;     // "https:"
location.hostname;     // "example.com"
location.pathname;     // "/about"
location.search;       // "?id=1"       (the query string)
location.hash;         // "#section2"

location.href = "https://example.com";   // navigate
location.reload();                       // refresh the page
location.assign(url);                    // navigate (keeps history)
location.replace(url);                   // navigate (REPLACES history entry)
```

---

## 46. The DOM (Document Object Model)

> **DOM stands for Document Object Model. It is an interface (an API) for HTML and XML
> documents. When the browser first reads (parses) your HTML document, it creates a big
> object based on that document — this is the DOM.**

It is a **tree-like structure** modelled from the HTML document. The DOM is used for
interacting with and modifying the structure, or specific elements and nodes.

**In short:** `HTML → becomes DOM → JavaScript can manipulate it!`

The `document` object in JavaScript **represents the whole HTML document**. It is the root
element. Note that `window.document` and `document` are the same thing.

### From HTML to DOM tree

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document Object Model</title>
</head>
<body>
  <div>
    <p><span></span></p>
    <label></label>
    <input>
  </div>
</body>
</html>
```

Becomes this tree:

```
document
  └── html
       ├── head
       │    └── title
       └── body
            └── div
                 ├── p
                 │    └── span
                 ├── label
                 └── input
```

### What is a "Node"?

**Node:** Every item in the DOM tree is called a node. There are two types:

- **Text Node** — a node that has text
- **Element Node** — a node that has an element

Relationships between nodes:

| Term | Meaning |
|---|---|
| **Child Node** | A node which is a child of another node |
| **Parent Node** | A node which has one or more children |
| **Descendant Node** | A node nested deep in the tree |
| **Sibling Node** | Nodes that share the same parent node |

---

## 47. Selecting Elements

Before you can change something, you have to find it.

### The modern way (preferred)

```javascript
// Returns the FIRST matching element (or null)
document.querySelector('css-selector');

// Returns ALL matching elements as a static NodeList
document.querySelectorAll('css-selector');
```

Because these take **any CSS selector**, they can do everything the old methods can:

```javascript
document.querySelector('#myId');            // by id
document.querySelector('.myClass');         // by class
document.querySelector('p');                // by tag
document.querySelector('div.note');         // combined
document.querySelector('input[type="text"]');  // by attribute
document.querySelector('ul > li:first-child'); // complex selectors

document.querySelectorAll('div.note');      // all of them
```

### The old ways (still work, still common)

| Method | Returns |
|---|---|
| `document.getElementById('id')` | A single element by its ID |
| `document.getElementsByClassName('class')` | A **live HTMLCollection** of all elements with that class |
| `document.getElementsByTagName('tag')` | A live HTMLCollection of all elements with that tag |
| `document.getElementsByName('name')` | All elements with that `name` attribute |

```javascript
// getElementById — the most direct
var number = document.getElementById("number").value;
alert(number * number * number);       // cube it

// getElementsByClassName — returns an array-LIKE object
var x = document.getElementsByClassName('class');
console.log(x);   // [object HTMLCollection]

// getElementsByTagName — count all paragraphs
var totalPara = document.getElementsByTagName("p");
alert("total p tags are: " + totalPara.length);

// getElementsByName — count radio buttons
var allgenders = document.getElementsByName("gender");
alert("Total Genders: " + allgenders.length);
```

### ⚠️ Live vs Static collections — a real gotcha

| Method | Returns | Live? |
|---|---|---|
| `getElementsByClassName` / `getElementsByTagName` | HTMLCollection | **✅ LIVE** — updates automatically when the DOM changes |
| `querySelectorAll` | NodeList | **❌ STATIC** — a frozen snapshot |

Neither is a real array. To use array methods:
```javascript
const els = [...document.querySelectorAll('p')];   // now a real Array
els.forEach(...); els.map(...); els.filter(...);
// NodeList does have .forEach built in, but HTMLCollection does not.
```

---

## 48. Reading & Changing Elements

### Content properties

| Property | What it does |
|---|---|
| `element.innerText` | Get/set the **visible** text (respects CSS — hidden text excluded) |
| `element.textContent` | Get/set **all** text, including hidden |
| `element.innerHTML` | Get/set the **HTML** content inside the element |
| `element.outerHTML` | Get/set the element **including** its own tag |
| `element.value` | Get/set the value of an `<input>` / `<textarea>` / `<select>` |
| `element.tagName` | Get the tag name |

```javascript
element.innerText   = 'Hello';
element.textContent = 'Hello';
element.innerHTML   = '<b>Hello</b>';     // renders the bold tag
let tag = element.tagName;                // "DIV"
```

> ⚠️ **Security warning:** Never put user input into `innerHTML`. A malicious user could
> inject `<script>` or `<img onerror=...>` — this is an **XSS attack**. Use `textContent`
> for anything a user typed.

**The `innerHTML` use case from the notes** — generating dynamic HTML such as registration
forms, comment forms, links:

```javascript
function showcommentform() {
  var data = "Name: <input type='text' name='name'><br>Comment:" +
             "<br><textarea rows='5' cols='80'></textarea>" +
             "<br><input type='submit' value='Post Comment'>";
  document.getElementById('mylocation').innerHTML = data;
}
```

### Attributes

| Method | Does |
|---|---|
| `element.getAttribute('name')` | Get the value of an attribute |
| `element.setAttribute('name', 'value')` | Set or update an attribute |
| `element.removeAttribute('name')` | Remove an attribute |
| `element.hasAttribute('name')` | Check if it exists |

```javascript
element.getAttribute('href');
element.setAttribute('class', 'highlight');
element.setAttribute('data-custom', 'value');
element.removeAttribute('data-custom');
```

### Classes — the `classList` API

**Much better than setting `className` directly**, because it doesn't wipe existing classes.

```javascript
node.classList                             // the list of classes
node.classList.add('class-name', ...)      // add one or more
node.classList.remove('class-name', ...)   // remove one or more
node.classList.toggle('class-name')        // add if absent, remove if present
node.classList.contains('class-name')      // → boolean
node.classList.replace('old', 'new')       // swap one for another
```

> 💡 **Best practice:** define your styles in CSS classes, then use `classList.toggle()`
> from JavaScript. Don't set dozens of inline styles.

### Inline styles

```javascript
element.style.color            = 'blue';
element.style.backgroundColor  = 'yellow';   // ⚠️ camelCase, not background-color
element.style.fontSize         = '20px';     // ⚠️ units are required
element.style.display          = 'none';     // hide the element
element.style.border           = '1px solid black';
element.style.padding          = '10px';
```

> ⚠️ CSS `background-color` becomes JavaScript `backgroundColor`. Every hyphenated CSS
> property becomes camelCase.

**Reading computed styles** (`element.style` only reads *inline* styles):
```javascript
const styles = getComputedStyle(element);
console.log(styles.color);
```

---

## 49. Creating, Inserting & Removing Elements

### Creating

```javascript
const el   = document.createElement('p');           // create a new element
const div  = document.createElement("div");
const text = document.createTextNode('some text');  // create a text node
const copy = node.cloneNode(true);                  // clone (true = deep, with children)
node.textContent = 'some text here';
```

### Inserting

**Modern methods (recommended):**
```javascript
parent.append(child);       // add child at the END of parent (accepts text too)
parent.prepend(child);      // add child at the START of parent
element.before(newEl);      // insert BEFORE the target element
element.after(newEl);       // insert AFTER the target element
```

**Older methods (still everywhere):**
```javascript
parentNode.appendChild(nodeToAdd);                 // add as the last child
parentNode.insertBefore(nodeToAdd, childNode);     // insert before a specific child
element.insertAdjacentHTML(position, html);        // insert an HTML string
```

`insertAdjacentHTML` positions:
```
<!-- beforebegin -->
<div>
  <!-- afterbegin -->
  content
  <!-- beforeend -->
</div>
<!-- afterend -->
```

### Removing

```javascript
element.remove();                        // remove the element itself (modern, easy)
parentNode.removeChild(nodeToRemove);    // remove a specific child from its parent

// The old "remove self" hack, before .remove() existed:
nodeToRemove.parentNode.removeChild(nodeToRemove);
```

### A complete worked example

```javascript
const button = document.createElement('button');
button.textContent = "Click Me";
button.classList.add('my-btn');
document.body.appendChild(button);

button.addEventListener('click', () => {
  console.log('Button Clicked!');
});
```

> ⚠️ **Performance tip:** adding many elements one at a time forces the browser to
> re-render each time. Build them in a `DocumentFragment` first, then append once:
> ```javascript
> const frag = document.createDocumentFragment();
> items.forEach(i => { const li = document.createElement('li'); li.textContent = i; frag.append(li); });
> list.append(frag);   // a single DOM update
> ```

---

## 50. DOM Traversal (Navigating the Tree)

Once you have one element, you can move to its relatives.

| Property | Returns |
|---|---|
| `node.parentNode` | The parent **node** of the specified node, as a Node object |
| `node.parentElement` | The parent **element** |
| `node.childNodes` | A NodeList collection of **all** child nodes (⚠️ includes text nodes) |
| `node.children` | Only the child **elements** (usually what you want) |
| `node.firstChild` | The first child **node** (may be whitespace text!) |
| `node.firstElementChild` | The first child **element** |
| `node.lastChild` | The last child node |
| `node.lastElementChild` | The last child element |
| `node.nextSibling` | The next node at the same tree level |
| `node.nextElementSibling` | The first following sibling that is an **element**, otherwise `null` |
| `node.previousSibling` | The previous node at the same level |
| `node.previousElementSibling` | The first preceding sibling that is an element, otherwise `null` |
| `element.closest(selector)` | The nearest **ancestor** (or self) matching a CSS selector |
| `element.matches(selector)` | Does this element match the selector? → boolean |

```html
<body>
  <div id="div1">
    <h1></h1>
    <div>
      <h1></h1>
      <p></p>
      <div><a href="#">click</a></div>
    </div>
  </div>
</body>
```

```javascript
let div1 = document.getElementById("div1");

console.log(div1.firstChild);              // may be a TEXT node (whitespace)
console.log(div1.firstElementChild);       // the <h1> ✅
console.log(div1.lastChild);
console.log(div1.lastElementChild);
console.log(div1.previousSibling);
console.log(div1.previousElementSibling);
console.log(div1.nextSibling);
console.log(div1.nextElementSibling);
console.log(div1.parentElement);
console.log(div1.children);                // HTMLCollection of elements
console.log(div1.childNodes);              // NodeList including text nodes
```

> ⚠️ **Always prefer the `Element` versions** (`firstElementChild`, `nextElementSibling`,
> `children`). The plain versions include whitespace text nodes and will confuse you.

**`closest()` is extremely useful** — it walks *up* the tree:
```javascript
// From a clicked delete button, find the whole row it belongs to
const row = event.target.closest('.task-item');
```

---

## 51. Events & Event Handling

> **The change in the state of an object is known as an Event.**

In HTML there are various events which represent that some activity is performed by the user
or by the browser. When JavaScript code is included in HTML, JS reacts to these events and
allows execution. **This process of reacting over events is called Event Handling.** Thus, JS
handles HTML events via **Event Handlers**.

For example, when a user clicks on the browser, you add JS code which will execute the task to
be performed on that event.

### Mouse events

| Event Performed | Event Handler | Description |
|---|---|---|
| `click` | `onclick` | When the mouse clicks on an element |
| `dblclick` | `ondblclick` | When an element is double-clicked |
| `contextmenu` | `oncontextmenu` | When an element is right-clicked |
| `mouseover` | `onmouseover` | When the cursor of the mouse comes over the element |
| `mouseout` | `onmouseout` | When the cursor of the mouse leaves an element |
| `mouseenter` | `onmouseenter` | When an element is entered by the mouse arrow (doesn't bubble) |
| `mouseleave` | `onmouseleave` | When an element is exited by the mouse arrow |
| `mousedown` | `onmousedown` | When the mouse button is pressed down over the element |
| `mouseup` | `onmouseup` | When the mouse button is released over the element |
| `mousemove` | `onmousemove` | When the mouse movement takes place |

### Keyboard events

| Event Performed | Event Handler | Description |
|---|---|---|
| `keydown` | `onkeydown` | When the user is pressing a key down |
| `keyup` | `onkeyup` | When the user releases a key |
| `keypress` | `onkeypress` | When the user presses a key ⚠️ **deprecated** |

### Form events

| Event Performed | Event Handler | Description |
|---|---|---|
| `focus` | `onfocus` | When the user focuses on an element |
| `blur` | `onblur` | When the focus moves away from a form element |
| `submit` | `onsubmit` | When the user submits the form |
| `change` | `onchange` | When the user modifies or changes the value of a form element |
| `input` | `oninput` | Fires on **every keystroke** in an input field |

### Window / Document events

| Event Performed | Event Handler | Description |
|---|---|---|
| `load` | `onload` | When the browser finishes loading the page |
| `unload` | `onunload` | When the visitor leaves the current webpage |
| `resize` | `onresize` | When the visitor resizes the browser window |
| `DOMContentLoaded` | — | When the HTML is parsed (doesn't wait for images) — **use this** |

### The three ways to attach an event

#### Way 1 — as an HTML attribute (oldest, avoid)

Writing the event name as an attribute directly in the HTML.

```html
<button onclick="demo()">click</button>
<script>
  function demo() {
    console.log("button is clicked");
  }
</script>
```

> ❌ **Avoid this.** It mixes HTML and JavaScript, and you can only attach one handler.

#### Way 2 — `addEventListener()` (best practice ✅)

```javascript
element.addEventListener(event, function, useCapture);
```

**Parameter values:**

- **`event`** — Required. A string that specifies the event's name (`"click"`, not `"onclick"`).
- **`function`** — Required. The JavaScript function which responds to the event occurring.
- **`useCapture`** — Optional. A Boolean specifying whether the event executes in the
  **bubbling** or **capturing** phase. When `true`, the handler executes in the **capturing**
  phase. When `false`, it executes in the **bubbling** phase. **Its default value is `false`.**

**The addEventListener() method is used to attach an event handler to a particular element.
It does NOT override existing event handlers** — you can attach as many as you like.

```html
<button id="btn">click me</button>
<p id="para"></p>
<script>
  document.getElementById("btn").addEventListener("click", fun);
  function fun() {
    document.getElementById("para").innerHTML = "Hello, World!";
  }
</script>
```

```javascript
// With an arrow function
let btn1 = document.getElementById("btn1");
btn1.addEventListener("click", () => {
  console.log("button is clicked");
});
```

**Removing a listener** — you must pass the *same function reference*:
```javascript
function handleClick() { console.log("clicked"); }
element.addEventListener("click", handleClick);
element.removeEventListener("click", handleClick);   // ✅ works

element.addEventListener("click", () => {});
element.removeEventListener("click", () => {});      // ❌ different function, won't remove
```

#### Way 3 — the `onclick` property

```javascript
let btn1 = document.getElementById("btn1");
btn1.onclick = () => {
  console.log("button is clicked");
};
```

```javascript
element.onclick = function () {
  console.log("Clicked");
};
```

> ⚠️ **Only one handler at a time.** Assigning a second `onclick` overwrites the first.

### Worked event examples

**Click event:**
```html
<script>
  function clickevent() {
    document.write("This is JavaTpoint");
  }
</script>
<form>
  <input type="button" onclick="clickevent()" value="Who's this?"/>
</form>
```

**MouseOver event:**
```html
<script>
  function mouseoverevent() {
    alert("This is JavaTpoint");
  }
</script>
<p onmouseover="mouseoverevent()">Keep cursor over me</p>
```

**Focus event:**
```html
<h2>Enter something here</h2>
<input type="text" id="input1" onfocus="focusevent()"/>
<script>
  function focusevent() {
    document.getElementById("input1").style.background = "aqua";
  }
</script>
```

**Keydown event:**
```html
<h2>Enter something here</h2>
<input type="text" id="input1" onkeydown="keydownevent()"/>
<script>
  function keydownevent() {
    document.getElementById("input1");
    alert("Pressed a key");
  }
</script>
```

---

## 52. The Event Object

Every event handler automatically receives an **event object** as its first argument. It
carries all the details about what happened.

```javascript
element.onclick = function (event) {
  console.log(event);          // the whole event object
  console.log(event.type);     // "click" — the type of event that occurred
  console.log(event.target);   // the element that triggered the event
};
```

### Key properties and methods

| Member | What it gives you |
|---|---|
| `event` | The event object passed to the handler |
| `event.type` | The type of event, e.g. `"click"` |
| **`event.target`** | **The element on which the event actually occurred** |
| `event.currentTarget` | The element the *listener* is attached to |
| `event.preventDefault()` | Prevent the default browser behaviour |
| `event.stopPropagation()` | Stop the event from bubbling further up |
| `event.stopImmediatePropagation()` | Stop bubbling **and** other handlers on the same element |
| `event.key` | Which key was pressed (keyboard events) |
| `event.clientX` / `clientY` | Mouse coordinates relative to the viewport |

### `event.target` explained

> **In simplest terms, `event.target` is the element on which the event occurred — the element
> that triggered the event.**

```html
<div onclick="clickFunc(event)" style="border:1px solid red">
  <div style="border:1px solid royalblue">
    <div style="border:1px solid skyblue">
      <button>Button</button>
    </div>
  </div>
</div>
```
```javascript
function clickFunc(event) {
  console.log(event.target);
}
```

If you click the button, it logs the **button** markup — even though the handler is attached
to the outermost `div`. So we can conclude that **`event.target` is always the element that
triggered the event**.

**`target` vs `currentTarget`:**
- `event.target` = what was actually clicked (the deepest element)
- `event.currentTarget` = the element the listener is attached to

### `preventDefault()` vs `stopPropagation()`

These two get confused constantly. **They do completely different things.**

**`event.preventDefault()`** — prevents the **default behaviour** of an element:
- In a **form** element → prevents it from submitting
- In an **anchor** element → prevents it from navigating
- In a **contextmenu** → prevents the right-click menu from showing

```javascript
form.onsubmit = function(event) {
  event.preventDefault();       // stop the page reloading
  // ... validate and send with fetch instead
};

link.addEventListener('click', e => e.preventDefault());   // don't follow the link
```

**`event.stopPropagation()`** — stops the **propagation** of the event; it stops the event
from continuing in the bubbling or capturing phase.

```javascript
child.addEventListener('click', e => {
  e.stopPropagation();          // the parent's handler will NOT fire
  console.log("child only");
});
```

---

## 53. Event Propagation: Bubbling & Capturing

> **When an event occurs on a DOM element, that event does not occur entirely on just that
> one element.** It travels through the DOM tree. Event propagation describes how an event
> should flow in the DOM tree.

### The three phases

**1. Capturing Phase (a.k.a. trickling)**
The event starts from the `window` and goes **down** through every ancestor element until it
reaches the target element.

**2. Target Phase**
The event has reached the target element — the element where the event was triggered. Any
event handlers associated with the target element for that event execute in this phase.

**3. Bubbling Phase**
The event **bubbles up** from the target element and goes up through every ancestor element
until it reaches the `window` again.

```
                    CAPTURING ↓            BUBBLING ↑
        window            1                     6
          │               ↓                     ↑
        <div>             2                     5
          │               ↓                     ↑
        <div>             3                     4
          │               ↓                     ↑
       <button>  ←──── 3.5 TARGET PHASE ────→
```

### Controlling the phase

**The 3rd argument of `addEventListener()` controls this:**
- `false` (the **default**) → the handler runs in the **BUBBLING** phase
- `true` → the handler runs in the **CAPTURING** phase

```javascript
element.addEventListener("click", handler);          // bubbling (default)
element.addEventListener("click", handler, false);   // bubbling (explicit)
element.addEventListener("click", handler, true);    // capturing
```

### A demonstration

```html
<style>
  #div1 { height: 200px; width: 200px; border: 2px solid; }
  #div2 { margin: 15px; border: 2px solid red; height: 40px; width: 160px;
          text-align: center; }
</style>

<div id="div1">Div1
  <div id="div2">Div2
    <button id="btn1">click1</button>
    <button id="btn2">click2</button>
  </div>
</div>

<script>
  let div1 = document.getElementById("div1");
  let div2 = document.getElementById("div2");
  let btn1 = document.getElementById("btn1");
  let btn2 = document.getElementById("btn2");

  div1.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("Div1 is clicked");
  });
  div2.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("Div2 is clicked");
  });
  btn1.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("btn1 is clicked");
  });
  btn2.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("btn2 is clicked");
  });
</script>
```

> **NOTE:** We use the **`stopPropagation()`** or **`stopImmediatePropagation()`** methods to
> stop bubbling or capturing.

Without `stopPropagation()`, clicking `btn1` would log:
```
btn1 is clicked
Div2 is clicked
Div1 is clicked
```
Because the event bubbles up through each ancestor.

---

## 54. Event Delegation

> **Event delegation is a technique in JavaScript where a SINGLE event listener is attached to
> a PARENT element instead of attaching event listeners to multiple child elements.**

The event object has a special property called **`.target`** which helps us get access to the
individual child elements.

### Why it matters

Imagine a list with 1,000 items. Without delegation you'd attach 1,000 listeners — slow and
memory-hungry. And if you add a new item later, it would have **no listener at all**.

With delegation, you attach **one** listener to the parent. It catches every click that
bubbles up, and `event.target` tells you which child was actually clicked. **New children
work automatically**, because the parent listener was always there.

### The pattern

```html
<ul id="taskList">
  <li>Task 1 <button class="delete">X</button></li>
  <li>Task 2 <button class="delete">X</button></li>
  <!-- more items added dynamically later -->
</ul>
```

```javascript
document.getElementById('taskList').addEventListener('click', function(e) {
  // Check whether the thing that was actually clicked is a delete button
  if (e.target.classList.contains('delete')) {
    e.target.closest('li').remove();
  }
});
```

**One listener. Works for existing items AND every item you add in the future.**

Using `closest()` makes it robust even when you click a nested element inside the button:
```javascript
const btn = e.target.closest('.delete');
if (!btn) return;      // the click wasn't on a delete button — ignore it
btn.closest('li').remove();
```

---

## 55. Popup Methods: alert, prompt, confirm

In JavaScript there are 3 popup methods: `alert()`, `prompt()` and `confirm()`.
**These methods are present in the `window` object**, and they can be accessed **without
referring to the window object name**.

### `alert()`

Used to display a warning message to the user, like a popup. Returns nothing.

```javascript
let btn1 = document.getElementById("btn1");
btn1.addEventListener("click", () => {
  alert("Warning...!");
});
```

### `prompt()`

Used to **collect input from the user**.
- It shows an input box, an **OK** button, and a **Cancel** button.
- If the user clicks **OK**, it returns the value present in the input.
- If the user clicks **Cancel**, it returns **`null`**.
- ⚠️ **`prompt()` always returns the value as a STRING.**

```javascript
let btn4 = document.getElementById("btn4");
btn4.addEventListener("click", () => {
  let a = prompt("Enter first number");
  let b = prompt("Enter second number");
  console.log(a + b);            // ⚠️ "510" — string concatenation, not addition!
  console.log(Number(a) + Number(b));   // ✅ 15 — convert first
});

// With a default value (second argument)
const userInput = prompt('Enter your name:', 'Default Name');
```

### `confirm()`

Instructs the browser to display a dialog with an optional message, and to **wait until the
user either confirms or cancels**.
- Returns **`true`** if the user clicks OK
- Returns **`false`** if the user clicks Cancel

```javascript
const result = confirm('Are you sure?');
if (result) {
  console.log("User clicked OK");
} else {
  console.log("User clicked Cancel");
}
```

> ⚠️ **All three are BLOCKING** — they freeze the entire page until dismissed, and they can't
> be styled. Real applications use custom modal dialogs instead. Use these for learning and
> quick debugging only.

---

## 56. Form Validation

> **It is important to validate the form submitted by the user, because it can have
> inappropriate values. So validation is a must to authenticate the user.**

JavaScript provides the facility to validate the form on the **client side**, so data
processing will be **faster than server-side validation**. Most web developers prefer
JavaScript form validation.

Through JavaScript we can validate name, password, email, date, mobile numbers and more.

> ⚠️ **Client-side validation is for user experience only.** It makes the form feel fast and
> friendly. **You must ALWAYS validate on the server too**, because a malicious user can
> disable JavaScript entirely.

### Basic validation — name and password

```html
<script>
function validateform() {
  var name     = document.myform.name.value;
  var password = document.myform.password.value;

  if (name == null || name == "") {
    alert("Name can't be blank");
    return false;                      // returning false STOPS the submission
  } else if (password.length < 6) {
    alert("Password must be at least 6 characters long.");
    return false;
  }
}
</script>

<body>
<form name="myform" method="post" action="abc.jsp" onsubmit="return validateform()">
  Name:     <input type="text" name="name"><br/>
  Password: <input type="password" name="password"><br/>
  <input type="submit" value="register">
</form>
</body>
```

> 💡 The key trick is `onsubmit="return validateform()"`. If the function returns `false`,
> the form does **not** submit.

### Email validation

We can validate the email with the help of JavaScript. There are many criteria that need to
be followed to validate an email ID:

- The email ID must contain the **`@`** and **`.`** characters
- There must be **at least one character before and after the `@`**
- There must be **at least two characters after the `.` (dot)**

```html
<script>
function validateemail() {
  var x = document.myform.email.value;
  var atposition  = x.indexOf("@");
  var dotposition = x.lastIndexOf(".");

  if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
    alert("Please enter a valid email address\nat position: " + atposition +
          "\ndot position: " + dotposition);
    return false;
  }
}
</script>

<body>
<form name="myform" method="post" action="#" onsubmit="return validateemail();">
  Email: <input type="text" name="email"><br/>
  <input type="submit" value="register">
</form>
</body>
```

**Breaking down that condition:**
- `atposition < 1` → the `@` is missing, or there's no character before it
- `dotposition < atposition + 2` → the dot comes too early (no character between `@` and `.`)
- `dotposition + 2 >= x.length` → fewer than two characters after the dot

### The modern approach

```javascript
form.addEventListener('submit', function(e) {
  e.preventDefault();                 // ✅ better than returning false

  const email = document.getElementById('email').value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  if (!emailRegex.test(email)) {
    showError('Please enter a valid email address');
    return;
  }
  // ... all good, submit with fetch()
});
```

You can also lean on **built-in HTML5 validation** and just style it:
```html
<input type="email" required minlength="6" pattern="[a-z]+">
```
```javascript
if (!input.checkValidity()) { console.log(input.validationMessage); }
```

---

## 57. Cookies

> **A cookie is an amount of information that persists between a server-side and a
> client-side. A web browser stores this information at the time of browsing.**

A cookie contains the information as a **string**, generally in the form of a **name-value
pair separated by semicolons**. It maintains the state of a user and remembers the user's
information among all the web pages.

### How cookies work

- When a user sends a request to the server, each of those requests is treated as a **new
  request sent by a different user** (HTTP is stateless).
- So, to recognise the old user, we need to **add the cookie with the response from the
  server**, which is stored in the browser at the client side.
- Now, whenever a user sends a request to the server, **the cookie is added with that request
  automatically**. Due to the cookie, the server recognises the user.

### Creating a cookie

In JavaScript, we can create, read, update and delete a cookie by using the
**`document.cookie`** property.

```javascript
document.cookie = "name=value";
```

```html
<!DOCTYPE html>
<html>
<head></head>
<body>
<input type="button" value="set Cookie" onclick="setCookie()">
<input type="button" value="get Cookie" onclick="getCookie()">

<script>
function setCookie() {
  document.cookie = "username=Duke Martin";
}

function getCookie() {
  if (document.cookie.length != 0) {
    alert(document.cookie);
  } else {
    alert("Cookie not available");
  }
}
</script>
</body>
</html>
```

### Cookie attributes

JavaScript provides some optional attributes that enhance the functionality of cookies.

| Attribute | Description |
|---|---|
| **`expires`** | Maintains the state of a cookie up to the specified date and time |
| **`max-age`** | Maintains the state of a cookie up to the specified time, **in seconds** |
| **`path`** | Expands the scope of the cookie to all pages of a website |
| **`domain`** | Specifies the domain for which the cookie is valid |
| `secure` | Only send over HTTPS |
| `SameSite` | Controls cross-site sending (`Strict` / `Lax` / `None`) |

### The `expires` attribute

The `expires` attribute provides one of the ways to create a **persistent cookie**. Here, a
date and time are declared that represent the active period of a cookie. **Once the declared
time is passed, the cookie is deleted automatically.**

```javascript
function setCookie() {
  document.cookie = "username=Duke Martin; expires=Sun, 20 Aug 2030 12:00:00 UTC";
}

function getCookie() {
  if (document.cookie.length != 0) {
    var array = document.cookie.split("=");
    alert("Name=" + array[0] + " Value=" + array[1]);
  } else {
    alert("Cookie not available");
  }
}
```

### Cookies with multiple name-value pairs

**In JavaScript, a cookie can contain only a single name-value pair.** However, to store more
than one name-value pair, we can use the following approaches:

- **Serialize the custom object into a JSON string**, then store it in a cookie
- **For each name-value pair, use a separate cookie**

```html
Name:   <input type="text" id="name"><br>
Email:  <input type="email" id="email"><br>
Course: <input type="text" id="course"><br>
<input type="button" value="Set Cookie" onclick="setCookie()">
<input type="button" value="Get Cookie" onclick="getCookie()">

<script>
function setCookie() {
  // Declaring 3 key-value pairs
  var info = "Name=" + document.getElementById("name").value +
             "; Email=" + document.getElementById("email").value +
             "; Course=" + document.getElementById("course").value;

  // Providing all 3 key-value pairs to a single cookie
  document.cookie = info;
}

function getCookie() {
  if (document.cookie.length != 0) {
    alert(document.cookie);       // invoking the key-value pairs stored in the cookie
  } else {
    alert("Cookie not available");
  }
}
</script>
```

### Deleting a cookie

There are the following ways to delete a cookie:

1. A cookie can be deleted by using the **`expires`** attribute (set it to a **past** date)
2. A cookie can also be deleted by using the **`max-age`** attribute (set it to `0` or negative)
3. We can delete a cookie **explicitly, by using a web browser**

```javascript
function setCookie() {
  // Set the expiry date to a date in the PAST → the cookie is deleted immediately
  document.cookie = "name=Martin Roy; expires=Sun, 20 Aug 2000 12:00:00 UTC";
}

function getCookie() {
  if (document.cookie.length != 0) {
    alert(document.cookie);
  } else {
    alert("Cookie not available");
  }
}
```

### Helper functions worth having

```javascript
function setCookie(name, value, days) {
  const d = new Date();
  d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
  document.cookie = `${name}=${value}; expires=${d.toUTCString()}; path=/`;
}

function getCookie(name) {
  return document.cookie
    .split('; ')
    .find(row => row.startsWith(name + '='))
    ?.split('=')[1];
}

function deleteCookie(name) {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
}
```

---

## 58. Web Storage: localStorage & sessionStorage

A modern, far easier alternative to cookies for storing data **in the browser**.

| | `localStorage` | `sessionStorage` |
|---|---|---|
| Lifetime | **Persists even after the browser closes** | **Cleared when the tab/window is closed** |
| Scope | Shared across all tabs of the same origin | That one tab only |
| Capacity | ~5–10 MB | ~5–10 MB |
| Sent to server? | ❌ Never | ❌ Never |

Compare with cookies: ~4KB max, and **sent with every HTTP request**.

### The API (identical for both)

```javascript
// Local Storage — persistent storage in browser memory
localStorage.setItem('username', 'Alice');
const username = localStorage.getItem('username');
console.log(username);                    // "Alice"
localStorage.removeItem('username');
localStorage.clear();                     // clears ALL items
localStorage.length;                      // how many items

// Session Storage — session-specific storage
sessionStorage.setItem('tempData', JSON.stringify({ id: 1, value: 'temporary' }));
const tempData = JSON.parse(sessionStorage.getItem('tempData'));
console.log(tempData);                    // { id: 1, value: 'temporary' }
```

> ⚠️ **Storage can only hold STRINGS.** Storing an object directly gives you the useless
> string `"[object Object]"`. Always use `JSON.stringify()` to save and `JSON.parse()` to
> read back.

```javascript
// ❌ Wrong
localStorage.setItem('user', { name: 'Ann' });
localStorage.getItem('user');       // "[object Object]"

// ✅ Right
localStorage.setItem('user', JSON.stringify({ name: 'Ann' }));
const user = JSON.parse(localStorage.getItem('user'));
```

**Safe read with a fallback:**
```javascript
function load(key, fallback = null) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch {
    return fallback;      // corrupted data, or storage blocked in private mode
  }
}
```

> 🔒 **Never store passwords, tokens, or sensitive data in localStorage.** Any JavaScript on
> the page — including injected malicious scripts — can read it.

---
---

# PART 7 — ASYNCHRONOUS JAVASCRIPT

---

## 59. Synchronous vs Asynchronous

**JavaScript is single-threaded** — it has one call stack and can do only one thing at a time.

**Synchronous** code runs line by line. Each line waits for the one before it to finish.

```javascript
console.log("First");
console.log("Second");
console.log("Third");
// First → Second → Third   (always, in order)
```

The problem: if one line takes 5 seconds, **the entire page freezes** for 5 seconds. No
clicks, no scrolling, nothing.

### What is an async task?

> **An async task is one in which a THIRD-PARTY PROCESS is doing the task.**

Examples:
- Requesting / sending data to a **database**
- Requesting / sending data via the **HTTP protocol**
- Working with the **file system** of the computer
- **Timers** (`setTimeout`, `setInterval`)
- **DOM events** (waiting for a click)

JavaScript hands these tasks off to the browser (or Node), carries on with the rest of your
code, and picks up the result later.

```javascript
console.log("Start");

setTimeout(function() {
      console.log("Inside setTimeout (after 2 seconds)");
}, 2000);

console.log("End");

// Output: Start → End → Inside setTimeout (after 2 seconds)
//         ↑ "End" prints BEFORE the timeout, even though it's written after
```

---

## 60. The Event Loop

The Event Loop is the mechanism that makes single-threaded JavaScript feel multi-tasking.

### The pieces

```
    ┌─────────────────── JavaScript Engine ────────────────────┐
    │                                                           │
    │   ┌────────────────┐        ┌──────────────────┐         │
    │   │  Call Stack    │        │  Message Queue   │         │
    │   │ Last-in        │        │ (Task Queue)     │         │
    │   │ First-out      │        │ [Task][Task][..] │         │
    │   │                │        └──────────────────┘         │
    │   │ Execution Ctx  │              ↑                       │
    │   │ Execution Ctx  │              │                       │
    │   │ Global Ex.Ctx  │              │                       │
    │   └────────────────┘              │                       │
    │           ↑                        │                      │
    │           └──── EVENT LOOP ────────┘                      │
    └───────────────────────────────────────────────────────────┘
                                    ↑
                        ┌───────────┴─────────────┐
                        │   Third-Party Processes │
                        │   • HTTP Process        │
                        │   • Timer Process       │
                        │   • DOM Events          │
                        └─────────────────────────┘
```

| Piece | Job |
|---|---|
| **Call Stack** | Where functions actually execute. Last-in, first-out. |
| **Web APIs / third-party processes** | The browser handles timers, HTTP requests, DOM events — **outside** the JS thread. |
| **Message Queue (Task Queue)** | Finished callbacks wait here (`setTimeout`, DOM events). |
| **Microtask Queue** | Higher priority queue for **Promise** callbacks. |
| **Event Loop** | Constantly checks: *"Is the call stack empty? If so, move the next queued task onto it."* |

### The golden rule

> **The Event Loop only moves a queued callback onto the call stack when the call stack is
> COMPLETELY EMPTY.**

That's why `setTimeout(fn, 0)` doesn't run immediately — it has to wait for all your
synchronous code to finish first.

### Microtasks beat macrotasks

**Promises** go into the **microtask queue**, which is drained **before** the task queue.

```javascript
console.log('1');

setTimeout(() => console.log('2'), 0);       // macrotask

Promise.resolve().then(() => console.log('3'));  // microtask

console.log('4');

// Output: 1, 4, 3, 2
```

**Why?**
1. `1` — synchronous
2. `setTimeout` callback → task queue
3. `.then` callback → **microtask** queue
4. `4` — synchronous
5. Stack empty → drain **microtasks first** → `3`
6. Then the task queue → `2`

Understanding this one example means you understand the event loop.

---

## 61. Callbacks & Callback Hell

### Callbacks

> **A callback is a function passed into another function to be called once an operation is
> complete.** This was the original way to handle async work.

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback('Data received');
  }, 1000);
}

fetchData((data) => {
  console.log(data);      // logs after 1 second
});
```

### The Node.js "error-first" convention

```javascript
fs.readFile('file.txt', (err, data) => {
  if (err) { console.error(err); return; }   // always check the error FIRST
  console.log(data);
});
```

### ❌ Callback Hell

When one async task depends on another, callbacks nest. Deeply. This is called the
**"pyramid of doom"** and it is **hard to manage**.

```javascript
getUser(userId, (user) => {
  getOrders(user.id, (orders) => {
    getOrderDetails(orders[0].id, (details) => {
      getShipping(details.shippingId, (shipping) => {
        console.log(shipping);
        // ...and error handling has to be duplicated at every level 😱
      }, handleError);
    }, handleError);
  }, handleError);
}, handleError);
```

**Problems:** unreadable, hard to debug, error handling is repeated everywhere, and you
cannot easily run tasks in parallel.

**This is exactly the problem Promises were invented to solve.**

---

## 62. Promises

> **A Promise is an object that provides a useful construct when dealing with asynchronous
> tasks. It is called a "Promise" because it guarantees it will run upon success or failure
> of that task.**

Or in the words of the handwritten notes:

> *Promises in real life express a trust between two or more people and an assurance that a
> particular thing will surely happen. In JavaScript, a Promise is an object which ensures to
> produce a single value in the future. Promises in JavaScript are used for managing and
> tackling asynchronous operations.*

**A Promise represents a value that will be available now, later, or never.**

### The four states of a Promise

| State | Meaning |
|---|---|
| **pending** | The initial state — neither rejected nor fulfilled yet |
| **fulfilled** | The related promise action was **fulfilled successfully** |
| **rejected** | The related promise action **failed** to be fulfilled |
| **settled** | Either the action is fulfilled **or** rejected — i.e. it's done |

Thus a promise represents the completion of an asynchronous operation with its result. It can
be either successful completion, or its failure, but eventually completed. A Promise uses
`.then()`, which is executed only after the promise resolves.

### The three guarantees a Promise makes

1. Unless the current execution of the JS event loop is completed (success or failure),
   callbacks will **never** be called before it.
2. Even if the callbacks with `.then()` are present, they will be called **only after the
   asynchronous operation completes**.
3. When multiple callbacks are included by invoking `.then()` many times, **each of them will
   be executed in a chain** — one after the other, following the sequence in which they were
   inserted.

### Working with a Promise — two parts

**(A) Creating a promise:**
```javascript
const p = new Promise((resolve, reject) => {
     // Do some async task
     setTimeout(() => {
       if (condition) {
           resolve('Successful login');    // ✅ success
       } else {
           reject('Login failed');         // ❌ failure
       }
     }, 2000);
});
```

**(B) Using a promise:**
```javascript
p.then((res) => {
      console.log(res);          // runs if resolved
  })
  .catch((err) => {
      console.log(err);          // runs if rejected
  })
  .finally(() => {
      console.log("Promise finished");  // runs either way
  });
```

> **Note:** 90% of the time you will be working with **pre-existing** promises. The step of
> "creating a promise" will be done for you by a library, framework or environment. The most
> common example of a built-in promise is **`fetch`**.

### The method summary

| Method | What it does |
|---|---|
| `resolve(value)` | Mark the promise as successful and pass a result |
| `reject(error)` | Mark the promise as failed and pass an error message |
| `.then(cb)` | Handle the successful result of a resolved promise |
| `.catch(cb)` | Handle the error if the promise gets rejected |
| `.finally(cb)` | Run code after the promise is settled — no matter success or failure |
| `Promise.resolve(v)` | Create an already-resolved promise |
| `Promise.reject(e)` | Create an already-rejected promise |

### A full example

```javascript
const fetchData = new Promise((resolve, reject) => {
     setTimeout(() => {
         const success = true;
         if (success) {
            resolve("Data fetched successfully!");
        } else {
            reject("Failed to fetch data.");
        }
    }, 1500);
});

fetchData
    .then(data  => console.log(data))       // "Data fetched successfully!"
    .catch(error => console.error(error))
    .finally(() => console.log("Promise finished."));
```

### Chaining — the cure for callback hell

**Each `.then()` returns a new Promise**, so you can chain them into a flat sequence.
One `.catch()` at the end handles errors from **any** step.

```javascript
getUser(userId)
  .then(user    => getOrders(user.id))
  .then(orders  => getOrderDetails(orders[0].id))
  .then(details => getShipping(details.shippingId))
  .then(shipping => console.log(shipping))
  .catch(error   => console.error("Something failed:", error));  // ONE handler for all
```

Compare that to the pyramid of doom above. Flat, readable, one error path.

> ⚠️ **You must `return` inside `.then()`**, otherwise the next `.then()` receives `undefined`.

---

## 63. Promise Combinators

Used for handling **multiple asynchronous operations in parallel**.

### `Promise.all([...])` — wait for ALL

Resolves when **every** promise resolves. **Rejects immediately if ANY one rejects.**

```javascript
Promise.all([fetchData1(), fetchData2()])
  .then(([res1, res2]) => {
    console.log(res1, res2);
  })
  .catch(err => console.error("At least one failed:", err));
```

**Use when:** you need all the results and can't proceed without any of them.

### `Promise.allSettled([...])` — wait for all, never reject

Returns the results of **all** promises, regardless of success or failure.

```javascript
const results = await Promise.allSettled([p1, p2, p3]);
results.forEach(r => {
  if (r.status === 'fulfilled') console.log('✅', r.value);
  else                          console.log('❌', r.reason);
});
```

**Use when:** you want every result and a failure shouldn't kill the batch.

### `Promise.race([...])` — first one to settle wins

Resolves or rejects as soon as the **first** promise settles — success **or** failure.

```javascript
Promise.race([fetchData(), timeout(5000)])
  .then(value => console.log(value));
```

**Use when:** implementing timeouts.
```javascript
const timeout = ms => new Promise((_, rej) =>
  setTimeout(() => rej(new Error('Timed out')), ms));

const data = await Promise.race([fetch(url), timeout(5000)]);
```

### `Promise.any([...])` — first SUCCESS wins

Ignores rejections. Only rejects if **every** promise rejects.

```javascript
const fastest = await Promise.any([mirror1(), mirror2(), mirror3()]);
```

### Quick comparison

| Method | Resolves when | Rejects when |
|---|---|---|
| `all` | **All** succeed | **Any** one fails |
| `allSettled` | All settle | **Never** |
| `race` | **First** settles | First settles as a rejection |
| `any` | **First** succeeds | **All** fail |

### Observables (advanced, bonus)

Used in **RxJS** (Reactive Programming) for handling complex async data streams — common in
Angular apps.

```javascript
import { of } from 'rxjs';
of('Hello').subscribe((data) => {
  console.log(data);
});
```
✅ Powerful for real-time data streams · ❌ Requires learning RxJS

---

## 64. async / await

Introduced in **ES2017**. It's **syntactic sugar built on Promises** that makes asynchronous
code **look and read like synchronous code**. It's the modern default.

### The two keywords

- **`async`** — put it before a function. That function now **always returns a Promise**.
- **`await`** — put it before a Promise. It **pauses the async function** until that Promise
  settles, then gives you the value.

```javascript
async function myFunc() {
  return "Hello";              // automatically wrapped: Promise.resolve("Hello")
}
myFunc().then(v => console.log(v));   // "Hello"
```

```javascript
async function myFunc() {
  let result = await Promise.resolve("Done");
  console.log(result);        // "Done"
}
myFunc();
```

### Rewriting a promise chain

```javascript
// Promise chain
function getUserData() {
  return getUser(1)
    .then(user => getOrders(user.id))
    .then(orders => console.log(orders));
}

// async/await — same thing, reads top to bottom
async function getUserData() {
  const user   = await getUser(1);
  const orders = await getOrders(user.id);
  console.log(orders);
}
```

### Error handling — use try/catch

With `async/await` you use ordinary `try...catch`, exactly like synchronous code.

```javascript
async function getUserData() {
      try {
           console.log("Fetching user data...");
           const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
           const data = await response.json();
           console.log("User data:", data);
      } catch (error) {
           console.error("Error fetching user:", error);
      } finally {
           console.log("Done.");
      }
}
getUserData();
```

### Running things in PARALLEL

> ⚠️ **The most common `async/await` performance mistake:** awaiting things one after
> another when they don't depend on each other.

```javascript
// ❌ SLOW — sequential. Total time = 1s + 1s = 2 seconds
const a = await fetchA();     // waits 1s
const b = await fetchB();     // then waits another 1s

// ✅ FAST — parallel. Total time = 1 second
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```

Only await sequentially when step 2 genuinely needs step 1's result.

### Rules and gotchas

- `await` only works **inside an `async` function** (or at the top level of an ES module).
- An `async` function **always** returns a Promise, even if you return a plain value.
- Forgetting `await` gives you the Promise object itself, not the value:
  ```javascript
  const data = fetch(url);          // ❌ a Promise object
  const data = await fetch(url);    // ✅ the actual Response
  ```
- Unhandled rejections in async functions produce warnings. Always `try/catch` or `.catch()`.

### The three async styles compared

| Style | Pros | Cons |
|---|---|---|
| **Callbacks** | Simple for one level | ❌ Callback hell; error handling repeated |
| **Promises** | ✅ Cleaner than callbacks; chainable | ❌ Can still get messy with many `.then()` |
| **async/await** | ✅ Very clean and readable; normal try/catch | ❌ Must be used inside an `async` function |

---

## 65. The Fetch API

`fetch()` makes HTTP requests and **returns a Promise**.
> **Note:** `fetch` is a **Web API**, not part of core JavaScript. But it's used with
> Promises and async/await constantly.

### Three ways to write the same request

**1. With `.then()` chains:**
```javascript
fetch("url")
  .then(res => res.json())
  .then(data => console.log(data));
```

**2. With async/await (cleaner):**
```javascript
async function getData() {
  let res  = await fetch("url");
  let data = await res.json();
  console.log(data);
}
getData();
```

**3. With async/await and try-catch (handles errors gracefully — do this):**
```javascript
async function getData() {
  try {
    let res  = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    let data = await res.json();
    console.log(data);
  } catch (error) {
    console.log("Error:", error);
  }
}
getData();
```

### ⚠️ The huge fetch gotcha

> **`fetch()` does NOT reject on HTTP error statuses.** A 404 or a 500 still **resolves**.
> It only rejects on a *network* failure (no connection, DNS failure, CORS block).

You **must** check `response.ok` yourself:

```javascript
async function getData(url) {
  try {
    const res = await fetch(url);

    if (!res.ok) {                                  // ✅ ESSENTIAL check
      throw new Error(`HTTP error! Status: ${res.status}`);
    }

    return await res.json();
  } catch (err) {
    console.error('Fetch failed:', err.message);
    throw err;
  }
}
```

### Sending data (POST)

```javascript
const response = await fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  },
  body: JSON.stringify({ name: 'Ann', email: 'ann@example.com' })
});
const result = await response.json();
```

### Response methods

```javascript
await response.json();       // parse the body as JSON      (most common)
await response.text();       // as plain text
await response.blob();       // as binary (images, files)
await response.formData();   // as form data

response.ok;                 // true if status is 200–299
response.status;             // 200, 404, 500 ...
response.headers.get('Content-Type');
```

> ⚠️ You can only read the body **once**. Calling `.json()` twice throws.

### Cancelling a request

```javascript
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);   // give up after 5s

try {
  const res = await fetch(url, { signal: controller.signal });
} catch (err) {
  if (err.name === 'AbortError') console.log('Request cancelled');
}
```

### The older XMLHttpRequest

You'll still see this in legacy code:
```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', url);
xhr.send();
```
`fetch` replaced it. Use `fetch`.

---
---

# PART 8 — ERRORS, MODULES & ADVANCED

---

## 66. Error Handling

> **In programming, exception handling is a process or method used for handling the abnormal
> statements in the code and executing them. It also enables you to handle the flow control
> of the code/program.**

In exception handling:
- A **`throw`** statement is used to raise an exception. When an abnormal condition occurs, an
  exception is thrown using `throw`.
- The thrown exception is handled by wrapping the code into the **`try`** block.

### The three types of errors

While coding, there can be three types of errors in the code:

**1. Syntax Error**
When a user makes a mistake in the predefined syntax of a programming language, a syntax error
may appear. The code won't even run.
```javascript
let x = ;          // SyntaxError
```

**2. Runtime Error**
When an error occurs **during the execution** of the program, such an error is known as a
runtime error. The codes which create runtime errors are known as **Exceptions**. Thus,
exception handlers are used for handling runtime errors.
```javascript
undefinedFunction();     // ReferenceError at runtime
```

**3. Logical Error**
An error which occurs when there is a **logical mistake** in the program, that may not produce
the desired output, and may terminate abnormally. **The hardest to find** — the code runs
perfectly, it just gives the wrong answer.
```javascript
function average(a, b) { return a + b / 2; }   // ⚠️ missing parentheses — wrong maths
```

### The Error object

When a runtime error occurs, it creates and throws an **Error object**. Such an object can be
used as a base for user-defined exceptions too. An error object has **two properties**:

1. **`name`** — an object property that sets or returns an error name
2. **`message`** — returns an error message in string form

```javascript
try {
  null.foo;
} catch (e) {
  console.log(e.name);     // "TypeError"
  console.log(e.message);  // "Cannot read properties of null..."
  console.log(e.stack);    // the full stack trace
}
```

### The 7 built-in error types

Although `Error` is a generic constructor, there are the following standard built-in error
types (error constructors) beside it:

| Error type | When it happens |
|---|---|
| **EvalError** | An error that occurred in the `eval()` global function, used for evaluating JS string code |
| **InternalError** | Created when the JS engine throws an internal error |
| **RangeError** | A numeric variable or parameter is **out of its valid range** |
| **ReferenceError** | An **invalid reference** is de-referenced (using an undeclared variable) |
| **SyntaxError** | A syntax error that may occur while parsing |
| **TypeError** | A variable is **not a valid type** |
| **URIError** | Invalid parameters passed in `encodeURI()` or `decodeURI()` |

```javascript
new Array(-1);          // RangeError: Invalid array length
undefinedVariable;      // ReferenceError: undefinedVariable is not defined
null.property;          // TypeError: Cannot read properties of null
decodeURI('%');         // URIError: URI malformed
```

### `try...catch`

**`try { }` statement:** here the code which needs possible error testing is kept within the
try block. In case any error occurs, it passes to the `catch { }` block for taking suitable
actions and handling the error. Otherwise, it executes the code written within.

**`catch { }` statement:** this block handles the error of the code by executing the set of
statements written within the block. This block contains either the user-defined exception
handler or the built-in handler. **This block executes only when any error-prone code needs to
be handled in the try block. Otherwise, the catch block is skipped.**

```javascript
try {
  var a = ["34", "32", "5", "31", "24", "44", "67"];   // a is an array
  document.write(a);      // displays elements of a
  document.write(b);      // b is undefined but still trying to fetch its value
                          // → the catch block will be invoked
} catch (e) {
  alert("There is an error which shows " + e.message);  // handling the error
}
```

**A simpler example:**
```javascript
try {
  let x = y + 1;              // y is not defined (error)
} catch (error) {
  console.log(error.message); // "y is not defined"
}
```

### The `throw` statement

Throw statements are used for throwing **user-defined errors**. A user can define and throw
their own custom errors. **When a throw statement is executed, the statements present after it
will not execute. The control will directly pass to the catch block.**

```javascript
try {
    throw new Error('This is the throw keyword');   // user-defined throw statement
} catch (e) {
    document.write(e.message);    // "This is the throw keyword"
}
```

```javascript
let age = 15;
if (age < 18) {
  throw new Error("You must be 18+");
}
```

### `try...catch...finally`

**`finally`** is an optional block of statements which is executed after the execution of the
try and catch statements. **The finally block does not hold for the exception to be thrown.
Whether any exception is thrown or not, the finally block code, if present, executes. It does
not care for the output either.**

```javascript
try {
  var a = 2;
  if (a == 2)
    document.write("Ok");
} catch (e) {
  document.write("Error found " + e.message);
} finally {
  document.write("Value of a is 2");
}
```

```javascript
try {
  console.log("Trying...");
  throw new Error("Something went wrong!");
} catch (error) {
  console.log(error.message);      // "Something went wrong!"
} finally {
  console.log("Always runs!");     // ALWAYS executes
}
```

**A practical example with a return value:**
```javascript
function divide(a, b) {
     try {
            if (b === 0) {
                  throw new Error("Cannot divide by zero!");
            }
            return a / b;
     } catch (error) {
            console.error("An error occurred:", error.message);
            return null;                 // or re-throw, or return a default
     } finally {
            console.log("Division attempt finished.");
     }
}

console.log(divide(10, 2));
// "Division attempt finished."  then  5

console.log(divide(10, 0));
// "An error occurred: Cannot divide by zero!"
// "Division attempt finished."
// null
```

### Custom error classes

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

try {
  throw new ValidationError('Email is required', 'email');
} catch (e) {
  if (e instanceof ValidationError) {
    console.log(`${e.name} on ${e.field}: ${e.message}`);
  } else {
    throw e;                    // not ours — re-throw it
  }
}
```

### Async error handling

```javascript
// With async/await — normal try/catch
async function load() {
  try {
    const data = await fetch(url).then(r => r.json());
  } catch (e) {
    console.error(e);
  }
}

// With promise chains — .catch()
fetch(url).then(r => r.json()).catch(e => console.error(e));

// ⚠️ try/catch does NOT catch errors inside a callback that runs later
try {
  setTimeout(() => { throw new Error("boom"); }, 100);
} catch (e) {
  // ❌ never reached — the stack is long gone by the time it throws
}
```

### Good practice

```javascript
// ❌ Don't swallow errors silently
try { risky(); } catch (e) { }

// ❌ Don't catch what you can't handle
try { everything(); } catch (e) { console.log("something broke"); }

// ✅ Catch specific things, handle or re-throw
try {
  const data = JSON.parse(input);
} catch (e) {
  if (e instanceof SyntaxError) {
    showUserMessage("That file isn't valid JSON.");
  } else {
    throw e;
  }
}
```

---

## 67. Debugging

> **Sometimes a code may contain mistakes. Being a scripting language, JavaScript doesn't
> show any error message in a browser. But these mistakes can affect the output.**

### Method 1 — using `console.log()`

The `console.log()` method displays the result in the console of the browser. If there is any
mistake in the code, it generates the error message.

```javascript
x = 10;
y = 15;
z = x + y;
console.log(z);     // 25
console.log(a);     // ⚠️ ReferenceError — 'a' is not initialised
```

**Better console methods for debugging:**
```javascript
console.table([{a:1,b:2}, {a:3,b:4}]);   // pretty table — great for arrays of objects
console.group('Label'); console.log('nested'); console.groupEnd();
console.time('op'); /* ...work... */ console.timeEnd('op');   // measure duration
console.count('clicked');                 // how many times did this run?
console.trace();                          // where was this called from?
console.assert(x > 0, 'x should be positive');
```

### Method 2 — using the `debugger` keyword

In debugging, we generally set **breakpoints** to examine each line of code step by step.
**There is no requirement to perform this task manually in JavaScript** — just write
`debugger;` and the browser pauses there (as long as DevTools is open).

```javascript
x = 10;
y = 15;
z = x + y;
debugger;              // ← execution pauses here
document.write(z);
document.write(a);
```

While paused you can inspect every variable, and step through with:
- **Step over** — run the next line
- **Step into** — go inside the function being called
- **Step out** — finish the current function and come back
- **Resume** — continue until the next breakpoint

### Method 3 — DevTools breakpoints

Open DevTools → **Sources** tab → click a line number to set a breakpoint. No code change
needed. This is what professionals use.

### A debugging strategy

1. **Read the actual error message.** It tells you the type, the message, the file and the line.
2. **Check the line above** the reported one — errors often surface one line late.
3. **`console.log` the variables** just before the failure. Is the value what you expected?
4. **Check the type**, not just the value: `console.log(typeof x, x)`.
5. **Comment out half** the code. Does the bug persist? Now you know which half to search.
6. **Use `debugger`** to freeze time and look around.

**The most common beginner errors:**

| Error | Usual cause |
|---|---|
| `Cannot read properties of null` | `getElementById` found nothing — check the ID, or move the `<script>` to the bottom |
| `Cannot read properties of undefined` | You accessed a property on something that doesn't exist |
| `x is not a function` | Typo, or `x` isn't what you think it is |
| `x is not defined` | Typo in the variable name, or it's out of scope |
| `Unexpected token` | A missing bracket, brace or comma |
| `Maximum call stack size exceeded` | Infinite recursion — you forgot the base case |

---

## 68. ES6 Modules

Modules let you **organise code into separate files** for better maintainability and
reusability. Each file gets its own scope — nothing leaks into global.

### Exporting

**Named exports** — export multiple things from one module:
```javascript
// math.js
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export class Calculator { }

// or export them all at the bottom
const E = 2.718;
function subtract(a, b) { return a - b; }
export { E, subtract };
```

**Default export** — export a single main thing. **One per file maximum.**
```javascript
export default function subtract(a, b) { return a - b; }
```

### Importing

```javascript
// app.js

// Named import — the names must MATCH, and need curly braces
import { PI, add } from './math.js';

// Default import — you can call it ANYTHING, no braces
import subtractNumbers from './math.js';

// Renaming a named import
import { PI as CIRCLE_PI } from './math.js';

// Combining default and named in a single statement
import subtract, { PI, add } from './math.js';

// Import everything as a namespace object
import * as MathUtils from './math.js';
console.log(MathUtils.PI, MathUtils.add(2, 3));

console.log(PI);                 // 3.14159
console.log(add(2, 3));          // 5
console.log(subtractNumbers(5, 2)); // 3
```

### Named vs default — the difference

| | Named export | Default export |
|---|---|---|
| How many per file | Many | **One** |
| Import syntax | `import { x } from` | `import x from` |
| Name must match? | ✅ Yes (unless renamed with `as`) | ❌ No — call it anything |

### Requirements

> **Note:** Modules require a server environment or specific browser configuration.

```html
<script type="module" src="app.js"></script>
```

- You **must** use `type="module"`
- File extensions are required in the browser: `'./math.js'` not `'./math'`
- Modules are **always in strict mode** automatically
- Modules are **deferred** by default (they wait for the HTML to parse)
- Because of CORS, you need to serve over `http://`, not open the file directly with `file://`
  (use VS Code's Live Server, or `npx serve`)

### Dynamic imports

Load a module **on demand**, at runtime. Returns a Promise.
```javascript
button.addEventListener('click', async () => {
  const { heavyFunction } = await import('./heavy-module.js');
  heavyFunction();
});
```
Great for reducing the initial bundle size.

---

## 69. Generators

> **Generators are a new way to work with functions and iterators. Using a generator, you can
> STOP the execution of a function from anywhere inside the function, and continue executing
> code from the halted position.**

They are defined with **`function*`** and use the **`yield`** keyword.

```javascript
function* idGenerator() {
     let id = 1;
     while (true) {
           yield id++;      // PAUSE execution and return id, resume on the next .next()
     }
}

const gen = idGenerator();
console.log(gen.next().value);   // 1
console.log(gen.next().value);   // 2
console.log(gen.next().value);   // 3
```

Each call to `.next()` returns `{ value: ..., done: false }` and runs until the next `yield`.

```javascript
function* simple() {
  yield 1;
  yield 2;
  return 3;
}
const g = simple();
console.log(g.next());   // { value: 1, done: false }
console.log(g.next());   // { value: 2, done: false }
console.log(g.next());   // { value: 3, done: true }
console.log(g.next());   // { value: undefined, done: true }
```

Generators are iterable, so `for...of` and spread work:
```javascript
function* colors() { yield "red"; yield "green"; }
for (const c of colors()) console.log(c);
console.log([...colors()]);      // ["red", "green"]
```

**Why they matter:** infinite sequences without infinite memory, lazy evaluation, and custom
iterators. They're also the machinery that async/await was originally built on.

---

## 70. Proxy & Reflect

Both ES6. Advanced, but worth knowing they exist.

### Proxy

> **Proxies are objects that wrap another object or function and can intercept fundamental
> operations** — e.g. property lookup, assignment, function invocation.

```javascript
const target = {
     message1: "hello",
     message2: "world"
};

const handler = {
     get: function(target, property, receiver) {
          if (property === 'message2') {
                 return 'Intercepted message2!';
          }
          return Reflect.get(target, property, receiver);
     },
     set: function(target, property, value, receiver) {
          if (property === 'message1' && typeof value !== 'string') {
                 throw new TypeError('message1 must be a string');
          }
          return Reflect.set(target, property, value, receiver);
     }
};

const proxy = new Proxy(target, handler);

console.log(proxy.message1);   // "hello"
console.log(proxy.message2);   // "Intercepted message2!"  ← intercepted!

proxy.message1 = "new hello";
console.log(proxy.message1);   // "new hello"

// proxy.message1 = 123;       // ❌ Throws TypeError
```

**Common "traps"** you can define in the handler: `get`, `set`, `has`, `deleteProperty`,
`apply`, `construct`, `ownKeys`.

**Where it's used in the real world:** Vue 3's reactivity system, validation layers,
logging/instrumentation, and mock objects in tests.

### Reflect

> **A built-in object that provides methods for interceptable JavaScript operations.
> Often used with Proxies.**

`Reflect` gives you the *default* behaviour of an operation, so inside a Proxy trap you can
do your custom bit and then say "…and now do what you'd normally do".

```javascript
Reflect.get(obj, 'key');
Reflect.set(obj, 'key', value);
Reflect.has(obj, 'key');           // like the `in` operator
Reflect.deleteProperty(obj, 'key');
Reflect.ownKeys(obj);
```

---

## 71. Web Workers

Web Workers allow running JavaScript in a **background thread**, separate from the main
execution thread — **preventing UI blocking**. Use them for heavy computation.

```javascript
// main.js
if (window.Worker) {
     const myWorker = new Worker('worker.js');

     myWorker.postMessage({ command: 'startCalculation', data: 1000000000 });

     myWorker.onmessage = function(e) {
          console.log('Message received from worker:', e.data);
     };

     myWorker.onerror = function(error) {
          console.error('Worker error:', error);
     };

     console.log('Main thread continues...');   // this runs immediately — no blocking!
} else {
     console.log('Web Workers are not supported in this browser.');
}
```

```javascript
// worker.js — a SEPARATE file
onmessage = function(e) {
    if (e.data.command === 'startCalculation') {
        let sum = 0;
        for (let i = 0; i < e.data.data; i++) {
            sum += i;
        }
        postMessage(sum);      // send the result back to the main thread
    }
};
```

> ⚠️ **Web Workers cannot directly access the DOM.** They have no `document`, no `window`.
> They communicate only via `postMessage`. They must live in **separate files**.

`myWorker.terminate()` stops a worker.

---

## 72. Design Patterns

Common, proven solutions to recurring problems in software design.

### Module Pattern

Encapsulates **private state** and exposes only **public methods**. Built on an IIFE + closure.

```javascript
const ShoppingCart = (function() {
    let items = [];                       // PRIVATE — unreachable from outside

    function addItem(item) {
          items.push(item);
          console.log(`${item} added.`);
    }
    function removeItem(item) {
          const index = items.indexOf(item);
          if (index > -1) {
                items.splice(index, 1);
                console.log(`${item} removed.`);
          }
    }
    function getItems() {
          return [...items];              // return a COPY to prevent external modification
    }

    return {                              // the PUBLIC interface
          add:    addItem,
          remove: removeItem,
          list:   getItems
    };
})();

ShoppingCart.add("Laptop");
ShoppingCart.add("Mouse");
console.log(ShoppingCart.list());    // ["Laptop", "Mouse"]
console.log(ShoppingCart.items);     // undefined — genuinely private ✅
```

### Revealing Module Pattern

A variation where you explicitly return an object with pointers to the private functions you
want to expose.

```javascript
const Calculator = (function() {
     let result = 0;

     function add(num)      { result += num; }
     function subtract(num) { result -= num; }
     function getResult()   { return result; }

     return {                     // "reveal" the private functions
           add: add,
           subtract: subtract,
           getResult: getResult
     };
})();

Calculator.add(10);
Calculator.subtract(3);
console.log(Calculator.getResult());   // 7
```

### Singleton Pattern

Ensures a class has **only one instance**, and provides a global point of access to it.

```javascript
const Logger = (function() {
     let instance;

     function init() {
           let logs = [];
           function addLog(message) {
               const timestamp = new Date().toISOString();
               logs.push(`[${timestamp}] ${message}`);
           }
           function getLogs() { return logs; }
           return { addLog, getLogs };
     }

    return {
        getInstance: function() {
            if (!instance) {
                instance = init();      // create it only ONCE
            }
            return instance;
        }
    };
})();

const logger1 = Logger.getInstance();
logger1.addLog("First message.");

const logger2 = Logger.getInstance();
logger2.addLog("Second message.");

console.log(logger1.getLogs());   // BOTH messages — it's the same instance
console.log(logger2.getLogs());   // identical output
```

**Use for:** a single config object, a single database connection, one app-wide logger.

### Observer Pattern (Publish/Subscribe)

Defines a **one-to-many** dependency between objects, so that when one object changes state,
all its dependents are notified and updated automatically.

```javascript
class Subject {
     constructor() {
           this.observers = [];
     }
     addObserver(observer) {
           this.observers.push(observer);
     }
     removeObserver(observer) {
           this.observers = this.observers.filter(obs => obs !== observer);
     }
     notify(data) {
           this.observers.forEach(observer => observer.update(data));
     }
}

class Observer {
     constructor(name) { this.name = name; }
     update(data) {
         console.log(`${this.name} received update: ${data}`);
     }
}

const newsFeed    = new Subject();
const subscriber1 = new Observer("Subscriber A");
const subscriber2 = new Observer("Subscriber B");

newsFeed.addObserver(subscriber1);
newsFeed.addObserver(subscriber2);

newsFeed.notify("Breaking News: JavaScript is awesome!");
// Subscriber A received update: Breaking News: JavaScript is awesome!
// Subscriber B received update: Breaking News: JavaScript is awesome!

newsFeed.removeObserver(subscriber1);
newsFeed.notify("Another update!");
// Subscriber B received update: Another update!
```

**You already use this pattern:** `addEventListener` is the Observer pattern.
It also underpins Redux, RxJS, and Vue's reactivity.

---

## 73. Other Web APIs

Web APIs are features provided **by the browser**, not by the JavaScript language itself.

| API | What it does | Example |
|---|---|---|
| **Web Storage** | Persistent (`localStorage`) and session (`sessionStorage`) storage in browser memory | `localStorage.setItem('k','v')` |
| **Fetch** | Make HTTP calls | `fetch(url).then(r => r.json())` |
| **Geolocation** | Get the user's location | `navigator.geolocation.getCurrentPosition(p => console.log(p))` |
| **Canvas** | Draw 2D/3D graphics | `const ctx = canvas.getContext('2d')` |
| **Web Audio** | Create and play sound — e.g. an oscillator playing a tone | `new AudioContext()` |
| **Web Speech** | Text-to-speech and speech recognition | `speechSynthesis.speak(new SpeechSynthesisUtterance("Hello There"))` |
| **WebSockets** | Real-time, bidirectional communication protocol | `new WebSocket('ws://example.com')` |
| **IndexedDB** | Structured client-side data storage (much bigger than localStorage) | `indexedDB.open('db', 1)` |
| **File / FileReader** | Manipulate files, access metadata | `reader.readAsDataURL(file)` |
| **Notification** | Display system notifications | `new Notification("Hi!")` |
| **Web Workers** | Execute background scripts off the main thread | `new Worker('worker.js')` |
| **Intersection Observer** | Efficiently observe element visibility changes | Lazy-loading images, infinite scroll |
| **Mutation Observer** | Observe DOM changes asynchronously | `new MutationObserver(cb)` |
| **Pointer Lock** | Capture mouse movements precisely in-browser | Used by browser games |
| **Battery Status** | Monitor device battery information asynchronously | `navigator.getBattery()` |
| **Gamepad** | Interact with game controller devices | `navigator.getGamepads()` |
| **DeviceOrientation / Motion** | Track device orientation and motion data | `window.ondeviceorientation` |
| **Push** | Enable push notifications in browsers | Service Workers + Push |
| **Payment Request** | Streamlined online payment processing | `new PaymentRequest(...)` |
| **Performance** | Measure timings precisely | `performance.now()` |
| **requestAnimationFrame** | Schedule smooth animations | `requestAnimationFrame(step)` |
| **Screen** | Screen dimensions | `screen.width`, `screen.height` |
| **Navigator** | Browser and connection info | `navigator.userAgent`, `navigator.onLine` |
| **History** | Manipulate session history | `history.pushState(...)` |
| **Drag and Drop** | Native drag/drop | `element.ondragstart`, `dropArea.ondrop` |
| **Intl** | Locale-aware formatting | `new Intl.NumberFormat('en-US')` |

### A few in code

```javascript
// Geolocation
navigator.geolocation.getCurrentPosition(position => console.log(position));
const watchID = navigator.geolocation.watchPosition(p => console.log(p));

// Canvas — draw a filled blue rectangle
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';
ctx.fillRect(10, 10, 100, 50);

// FileReader
const reader = new FileReader();
reader.readAsDataURL(file);
reader.onload = function() { console.log(reader.result); };

// Mutation Observer
const observer = new MutationObserver(callback);
observer.observe(targetNode, config);

// Performance timing
const start = performance.now();
doWork();
console.log(`Took ${performance.now() - start}ms`);

// Smooth animation
function step(timestamp) {
  // ...update positions...
  requestAnimationFrame(step);
}
requestAnimationFrame(step);
```

---

## 74. Modern Shortcuts You Should Know

These four make modern JavaScript dramatically shorter and safer.

### Optional chaining `?.`

Safely access deeply nested properties. Returns `undefined` instead of throwing.

```javascript
// Old, painful way
let val = obj && obj.key && obj.key.deep;

// New way
let val = obj?.key?.deep;

// Works on methods and arrays too
obj.method?.();          // only calls if the method exists
arr?.[0];                // only indexes if arr exists
user?.address?.city;     // undefined instead of a crash
```

### Nullish coalescing `??`

Returns the right-hand side **only if** the left is `null` or `undefined`.

```javascript
let val = obj?.key ?? "Default";
```

**Crucially different from `||`:**
```javascript
0        || "default"    // "default"  ⚠️ 0 is falsy
0        ?? "default"    // 0          ✅ 0 is a real value
""       || "default"    // "default"  ⚠️
""       ?? "default"    // ""         ✅
null     ?? "default"    // "default"  ✅
```

> ✅ **Use `??` for defaults when `0`, `""` or `false` are legitimate values.**

### Logical assignment operators

```javascript
x ||= y;    // assign y if x is falsy
x &&= y;    // assign y if x is truthy
x ??= y;    // assign y only if x is null/undefined
```

### Object property shorthand

```javascript
const name = "Ann", age = 30;

// Old
const user = { name: name, age: age };
// New
const user = { name, age };

// Computed keys
const key = "dynamic";
const obj = { [key]: "value" };   // { dynamic: "value" }

// Method shorthand
const o = {
  greet() { }        // instead of greet: function() { }
};
```

---

## 75. ES6+ Feature Checklist

The full list of what "modern JavaScript" means.

### ES6 (2015) — the big one

1. **`let`, `const`** (instead of only `var`)
2. **Arrow Functions** `() => {}`
3. **Template Literals** `` `Hello, ${name}` ``
4. **Default Parameters** — used inside functions
5. **Destructuring**
   - Array Destructuring — `let [a, b] = [1, 2];`
   - Object Destructuring — `let { name, age } = person;`
6. **Spread Operator** — `...arr`, `...obj`
7. **Rest Operator** — `...rest`
8. **`for...of` Loop** — new in ES6 for iterating arrays
9. **Set and Map** data structures
10. **Promises** — `.then()`, `.catch()`, `.finally()`
11. **Classes** — `class`, `extends`, `super`, `static`
12. **ES6 Modules** — `export`, `import`
13. **Generators** — `function*`, `yield`
14. **Symbols**
15. **Proxy & Reflect**

### ES2017+
- **`async` / `await`** (ES2017)
- **Object spread in objects** (ES2018)
- **`Array.flat()` / `flatMap()`** (ES2019)
- **`Object.fromEntries()`** (ES2019)
- **`String.trimStart()` / `trimEnd()`** (ES2019)
- **Optional chaining `?.`** (ES2020)
- **Nullish coalescing `??`** (ES2020)
- **BigInt** (ES2020)
- **`Promise.allSettled()`** (ES2020)
- **Dynamic `import()`** (ES2020)
- **Logical assignment `||=` `&&=` `??=`** (ES2021)
- **`String.replaceAll()`** (ES2021)
- **`Promise.any()`** (ES2021)
- **Class private fields `#`** (ES2022)
- **Top-level `await`** (ES2022)
- **`Array.at()`** (ES2022)
- **`Object.hasOwn()`** (ES2022)
- **`Array.toSorted()` / `toReversed()` / `with()`** — non-mutating (ES2023)
- **`Array.findLast()` / `findLastIndex()`** (ES2023)

**And the Web API you must know:** `fetch` — modern HTTP requests, built on Promises.

### The one-line summary

> `let`, `const`, arrow functions, template literals, destructuring, spread/rest operators,
> `for...of`, Set, Map, Promises, `async`/`await`, the fetch API, and ES6 modules.

---
---

# PART 9 — PRACTICE

---

## 76. Full Project: A To-Do List Application

This project pulls together everything you've learned:

- **DOM Manipulation**
- **Event Handling**
- **Local Storage for persistence**
- **Basic Array methods** (`map`, `filter`, `push`, `forEach`)
- **Functions**

The application lets users **add, delete, and mark tasks as complete**, with tasks
**persisting across browser sessions**.

Save this as a single `.html` file and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple To-Do List</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
          rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }
        .container {
            background-color: #ffffff;
            border-radius: 1rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            width: 100%;
            max-width: 500px;
            margin-top: 2rem;
        }
        .task-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0;
            border-bottom: 1px solid #e5e7eb;
        }
        .task-item:last-child { border-bottom: none; }
        .task-text {
            flex-grow: 1;
            margin-right: 1rem;
            word-break: break-word;
        }
        .task-text.completed {
            text-decoration: line-through;
            color: #6b7280;
        }
        .action-buttons button {
            padding: 0.4rem 0.8rem;
            border-radius: 0.5rem;
            font-size: 0.875rem;
            font-weight: 600;
            transition: background-color 0.2s ease-in-out;
        }
        .action-buttons .complete-btn { background-color: #d1fae5; color: #065f46; }
        .action-buttons .complete-btn:hover { background-color: #a7f3d0; }
        .action-buttons .delete-btn {
            background-color: #fee2e2; color: #991b1b; margin-left: 0.5rem;
        }
        .action-buttons .delete-btn:hover { background-color: #fecaca; }
        .input-group { display: flex; gap: 0.5rem; margin-bottom: 1.5rem; }
        .input-group input {
            flex-grow: 1;
            padding: 0.75rem 1rem;
            border: 1px solid #d1d5db;
            border-radius: 0.75rem;
            outline: none;
            transition: border-color 0.2s;
        }
        .input-group input:focus { border-color: #3b82f6; }
        .input-group button {
            background-color: #3b82f6;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 0.75rem;
            font-weight: 600;
            transition: background-color 0.2s ease-in-out;
            cursor: pointer;
        }
        .input-group button:hover { background-color: #2563eb; }
        .message-box {
            background-color: #fff;
            border-radius: 0.75rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 1rem;
            margin-top: 1rem;
            text-align: center;
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 1000;
            display: none;
            max-width: 300px;
        }
        .message-box button {
            background-color: #3b82f6; color: white;
            padding: 0.5rem 1rem; border-radius: 0.5rem;
            margin-top: 0.75rem; cursor: pointer;
        }
        .message-box.show { display: block; }
    </style>
</head>
<body class="antialiased">
    <div class="container">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">My To-Do List</h1>

        <div class="input-group">
            <input type="text" id="taskInput" placeholder="Add a new task..."
                   class="focus:ring-2 focus:ring-blue-500">
            <button id="addTaskBtn">Add Task</button>
        </div>

        <ul id="taskList" class="divide-y divide-gray-200">
            <!-- Tasks will be dynamically added here -->
        </ul>
    </div>

    <!-- Custom Message Box (better than alert()) -->
    <div id="messageBox" class="message-box">
        <p id="messageBoxText"></p>
        <button id="messageBoxCloseBtn">OK</button>
    </div>

    <script>
        // ---- Get DOM elements ----
        const taskInput          = document.getElementById('taskInput');
        const addTaskBtn         = document.getElementById('addTaskBtn');
        const taskList           = document.getElementById('taskList');
        const messageBox         = document.getElementById('messageBox');
        const messageBoxText     = document.getElementById('messageBoxText');
        const messageBoxCloseBtn = document.getElementById('messageBoxCloseBtn');

        // ---- Array to store tasks ----
        // Each task object: { id: string, text: string, completed: boolean }
        let tasks = [];

        /**
         * Displays a custom message box instead of alert().
         * @param {string} message - The message to display.
         */
        function showMessageBox(message) {
            messageBoxText.textContent = message;
            messageBox.classList.add('show');
        }

        /** Hides the custom message box. */
        function hideMessageBox() {
            messageBox.classList.remove('show');
        }

        messageBoxCloseBtn.addEventListener('click', hideMessageBox);

        /** Loads tasks from local storage when the page loads. */
        function loadTasks() {
            const storedTasks = localStorage.getItem('tasks');
            if (storedTasks) {
                tasks = JSON.parse(storedTasks);   // STRING → array of objects
                renderTasks();
            }
        }

        /** Saves the current tasks array to local storage. */
        function saveTasks() {
            localStorage.setItem('tasks', JSON.stringify(tasks));  // array → STRING
        }

        /** Renders all tasks from the `tasks` array to the DOM. */
        function renderTasks() {
            taskList.innerHTML = '';   // clear existing list items

            if (tasks.length === 0) {
                taskList.innerHTML =
                  '<li class="text-center text-gray-500 py-4">No tasks yet. Add one!</li>';
                return;
            }

            tasks.forEach(task => {
                const listItem = document.createElement('li');
                listItem.classList.add('task-item');
                listItem.setAttribute('data-id', task.id);   // store the ID on the element

                // Task text span
                const taskTextSpan = document.createElement('span');
                taskTextSpan.classList.add('task-text', 'text-gray-700', 'text-lg');
                taskTextSpan.textContent = task.text;        // textContent = XSS-safe ✅
                if (task.completed) {
                    taskTextSpan.classList.add('completed');
                }

                // Action buttons container
                const actionButtonsDiv = document.createElement('div');
                actionButtonsDiv.classList.add('action-buttons');

                // Complete button
                const completeBtn = document.createElement('button');
                completeBtn.classList.add('complete-btn');
                completeBtn.textContent = task.completed ? 'Undo' : 'Complete';
                completeBtn.addEventListener('click', () => toggleComplete(task.id));

                // Delete button
                const deleteBtn = document.createElement('button');
                deleteBtn.classList.add('delete-btn');
                deleteBtn.textContent = 'Delete';
                deleteBtn.addEventListener('click', () => deleteTask(task.id));

                // Append everything
                actionButtonsDiv.appendChild(completeBtn);
                actionButtonsDiv.appendChild(deleteBtn);
                listItem.appendChild(taskTextSpan);
                listItem.appendChild(actionButtonsDiv);
                taskList.appendChild(listItem);
            });
        }

        /** Adds a new task to the list. */
        function addTask() {
            const taskText = taskInput.value.trim();   // get text and remove whitespace

            if (taskText === '') {
                showMessageBox('Task cannot be empty!');
                return;
            }

            const newTask = {
                id: crypto.randomUUID(),   // generate a unique ID
                text: taskText,
                completed: false
            };

            tasks.push(newTask);      // ARRAY METHOD: push
            saveTasks();              // save to local storage
            renderTasks();            // re-render the list
            taskInput.value = '';     // clear the input field
        }

        /**
         * Toggles the 'completed' status of a task.
         * @param {string} id - The ID of the task to toggle.
         */
        function toggleComplete(id) {
            tasks = tasks.map(task =>                       // ARRAY METHOD: map
                task.id === id ? { ...task, completed: !task.completed } : task
            );                                              // SPREAD to copy + override
            saveTasks();
            renderTasks();
        }

        /**
         * Deletes a task from the list.
         * @param {string} id - The ID of the task to delete.
         */
        function deleteTask(id) {
            tasks = tasks.filter(task => task.id !== id);   // ARRAY METHOD: filter
            saveTasks();
            renderTasks();
        }

        // ---- Event listeners ----
        addTaskBtn.addEventListener('click', addTask);

        // Enter key in the input field
        taskInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                addTask();
            }
        });

        // Load tasks when the page first loads
        document.addEventListener('DOMContentLoaded', loadTasks);
    </script>
</body>
</html>
```

### What to notice in this code

| Concept | Where it appears |
|---|---|
| **Selecting elements** | `document.getElementById(...)` at the top |
| **Arrays as state** | `let tasks = []` — the single source of truth |
| **Array methods** | `push` (add), `map` (toggle), `filter` (delete), `forEach` (render) |
| **Spread operator** | `{ ...task, completed: !task.completed }` — copy then override |
| **JSON** | `stringify` to save, `parse` to load |
| **localStorage** | Persistence across browser sessions |
| **Creating elements** | `createElement` + `appendChild` |
| **Event listeners** | `addEventListener` on buttons and the input |
| **Arrow functions + closures** | `() => toggleComplete(task.id)` captures `task.id` |
| **XSS safety** | `textContent` rather than `innerHTML` for user input |
| **`DOMContentLoaded`** | Wait for the HTML before touching the DOM |

### Ideas to extend it

1. Add an **Edit** button (double-click to edit in place)
2. Add **filters**: All / Active / Completed (`filter` again)
3. Add a **"Clear completed"** button
4. Add **due dates** using the Date object
5. Refactor to **event delegation** — one listener on `taskList` instead of two per item
6. Add **drag-and-drop** reordering
7. Replace `localStorage` with a real API using `fetch`

---

## 77. Learning Roadmap

### The five levels

**Level 1 — Beginner (Weeks 1–2)**
Variables · data types · operators · `if`/`else` · loops · functions · basic arrays and
objects · `console.log`
> ✅ **Milestone:** write a program that takes numbers and prints the largest one.

**Level 2 — DOM & Events (Weeks 3–4)**
Selecting elements · changing text and styles · `addEventListener` · form validation ·
creating and removing elements
> ✅ **Milestone:** build a working to-do list (section 76).

**Level 3 — Intermediate (Weeks 5–7)**
`map`/`filter`/`reduce` · destructuring · spread/rest · template literals · arrow functions ·
scope · hoisting · **closures** · `this`
> ✅ **Milestone:** explain closures and `this` to someone else without notes.

**Level 4 — Asynchronous (Weeks 8–10)**
Callbacks · Promises · `async`/`await` · `fetch` · the event loop · error handling
> ✅ **Milestone:** build an app that fetches data from a public API and displays it,
> with loading and error states.

**Level 5 — Advanced (Weeks 11+)**
Prototypes · classes and OOP · modules · generators · Proxy · design patterns ·
performance · testing
> ✅ **Milestone:** you can read any JavaScript codebase and understand what it does.

### The 20-hour Pareto plan (10 × 2-hour sessions)

The 20% of JavaScript that generates 80% of the results:

| # | Focus | Ends with |
|---|---|---|
| 1 | Variables, data types, operators, truthy/falsy | Type quiz — predict `typeof` for 15 values |
| 2 | Conditionals, loops, `break`/`continue` | FizzBuzz; multiplication table |
| 3 | Functions, parameters, arrow functions, scope | Write 5 reusable utility functions |
| 4 | Arrays + `map`/`filter`/`reduce` | Transform an array of user objects 5 ways |
| 5 | Objects, destructuring, spread/rest | Model a shopping cart with objects |
| 6 | DOM selection and manipulation | Build a colour-changing page |
| 7 | Events, forms, validation | Build a validated sign-up form |
| 8 | Closures, `this`, hoisting, execution context | Explain the classic `var` loop bug |
| 9 | Promises, `async`/`await`, `fetch` | Fetch and render data from a public API |
| 10 | Classes, modules, error handling | Refactor session 9 into modules + classes |

**End every session with a 15-minute review** of what you built and what confused you.

### The 5-minute cheat sheet

```javascript
// DECLARE
const x = 1;  let y = 2;                  // never var

// TYPES: string number boolean undefined null symbol bigint | object array function

// FUNCTIONS
const add = (a, b) => a + b;
function greet(name = "Guest") { return `Hi ${name}`; }

// ARRAYS
arr.push(x)  arr.pop()  arr.shift()  arr.unshift(x)
arr.map(f)  arr.filter(f)  arr.reduce(f, init)  arr.find(f)  arr.includes(x)
arr.slice(a,b)      // copy, non-mutating
arr.splice(i,n,...) // cut/insert, MUTATES

// OBJECTS
Object.keys(o)  Object.values(o)  Object.entries(o)
const { a, b } = obj;        const [x, y] = arr;
const copy = { ...obj };     const merged = { ...a, ...b };

// STRINGS
`Hello ${name}`  s.trim()  s.split(",")  s.includes(x)  s.slice(a,b)  s.replace(a,b)

// DOM
document.querySelector('.x')       document.querySelectorAll('.x')
el.textContent   el.innerHTML      el.classList.add/remove/toggle('c')
el.addEventListener('click', fn)   e.preventDefault()   e.target

// ASYNC
async function f() {
  try { const r = await fetch(url); if(!r.ok) throw Error(r.status); return r.json(); }
  catch (e) { console.error(e); }
}
await Promise.all([a(), b()]);     // parallel, not sequential

// MODERN
obj?.deep?.key ?? "default"        // optional chaining + nullish coalescing
[...new Set(arr)]                  // deduplicate an array
JSON.stringify(o) / JSON.parse(s)  // object ↔ string
```

### The 10 mistakes beginners make

1. Using `var` instead of `let`/`const`
2. Using `==` instead of `===`
3. Forgetting `return` inside a function or a `.then()`
4. Mutating an array or object you meant to copy (`=` doesn't copy objects)
5. Forgetting `await`, then wondering why you got a `Promise`
6. Putting `<script>` in `<head>` and getting `null` from `getElementById`
7. Not knowing `sort()` sorts numbers as strings
8. Not checking `response.ok` after `fetch`
9. Using `innerHTML` with user input (XSS risk)
10. Assuming `this` means what it does in other languages

### The 5 best resources

| Resource | Why it's worth your time |
|---|---|
| **MDN Web Docs** (`developer.mozilla.org`) | The official reference. Accurate, exhaustive, has runnable examples. When in doubt, Google "mdn <topic>". |
| **javascript.info** | The best free structured tutorial. Explains *why*, not just *how*, with exercises and solutions. |
| **"You Don't Know JS Yet"** by Kyle Simpson (free on GitHub) | Goes deep on scope, closures, `this` and types — the exact things that confuse people. |
| **freeCodeCamp** | Free, hands-on, in-browser. Best for building muscle memory through repetition. |
| **The browser DevTools console** | Not a course — a laboratory. Every idea in these notes can be tested in 10 seconds. Use it constantly. |

Useful reference repos:
- `github.com/jlevy/the-art-of-command-line` — terminal usage and real workflows
- `github.com/kilimchoi/engineering-blogs` — architecture and scaling from real companies
- `github.com/RefactoringGuru/design-patterns-typescript` — design patterns with clear examples
- `github.com/abhivaikar/howtheytest` — real company testing strategies

### Final advice

> **Reading about JavaScript will not teach you JavaScript.**
>
> After each section here, open DevTools and type the examples yourself. Change them. Break
> them. Read the error. That loop — write, run, break, fix — is the only thing that actually
> works.
>
> Build something small and useless every week. A tip calculator, a quiz, a colour picker, a
> stopwatch. Volume of finished tiny projects beats one perfect big one.

---

# PART 10 — PATTERNS & THE REACT BRIDGE

---

## 78. Async Concurrency Patterns

Sections 59–65 cover the *mechanics* of async. This section covers the *patterns* — the handful of
shapes that almost every real async problem turns out to be. Compiled from two async cheatsheets that
live outside this folder (see Source Files).

### Sharing a promise — the key insight

A promise is just an object. Multiple callers can `.then()` the same one, and the work happens once.

```javascript
const shared = fetch('/api/data');       // ONE network call

shared.then(r => console.log('Caller A:', r));
shared.then(r => console.log('Caller B:', r));
shared.then(r => console.log('Caller C:', r));
// All three get the same result. One request was made.
```

Everything below builds on this.

### Pattern 1 — Deduplication: share in-flight promises

*Trigger: multiple callers want the same async result at the same time.*

```javascript
const cache = new Map();                 // MUST live outside the function

function deduped(id, apiCall) {
  if (cache.has(id)) return cache.get(id);      // return the SAME promise

  const promise = apiCall(id)
    .then(result => { cache.delete(id); return result; })
    .catch(err   => { cache.delete(id); throw err;    });

  cache.set(id, promise);
  return promise;
}
```

**Why clean up in both paths.** Only cleaning up on success means a failed request stays cached
forever and callers can never retry. Only cleaning up on failure means a successful request stays
cached and callers get stale data forever. Always both.

**Why `.then(fn, fn)` and not `.finally()`.** `.finally()` runs a microtask tick later. When the
cleanup is exact — deleting from a cache another caller is about to read — that tick matters. The
two-argument form runs both handlers in the same tick.

### Pattern 2 — Retry with exponential backoff

*Trigger: a call may fail temporarily and succeed on retry.*

```javascript
async function withRetry(fn, retries = 3, delayMs = 100) {
  try {
    return await fn();
  } catch (err) {
    if (retries === 0) throw err;
    await new Promise(r => setTimeout(r, delayMs));
    return withRetry(fn, retries - 1, delayMs * 2);      // double each time
  }
}
```

Only retry what is retryable — a 429 or a 5xx, never a 400 or a 401. Retrying a validation failure
just fails three times more slowly.

### Pattern 3 — Timeout

*Trigger: fail fast if something takes too long.*

```javascript
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Timed out')), ms)
  );
  return Promise.race([promise, timeout]);       // first to settle wins
}
```

Note this doesn't *cancel* the underlying work — it just stops waiting. To actually cancel a fetch,
use `AbortController` (§65).

### Pattern 4 — Async recursion: follow a chain

*Trigger: the response tells you to fetch again — redirects, pagination, tree walks.*

```javascript
async function fetchWithRedirect(id, fetcher, depth = 0, maxDepth = 5) {
  if (depth > maxDepth) throw new Error('Max redirect depth exceeded');

  const response = await fetcher(id);
  if (response.redirectId) {
    return fetchWithRedirect(response.redirectId, fetcher, depth + 1, maxDepth);
  }
  return response;                       // base case — no redirect, done
}
```

The depth counter is not optional. Without it, a cycle in the data is an infinite loop.

### Pattern 5 — Parallel + redirect: combining patterns

*Trigger: a set of IDs, each of which may redirect, all of which should run at once.*

```javascript
async function fetchDeep(ids, fetcher, maxDepth = 5) {
  async function fetchOne(id, depth) {
    if (depth > maxDepth) throw new Error('Max redirect depth exceeded');
    const res = await fetcher(id);
    if (res.redirectId) return fetchOne(res.redirectId, depth + 1);
    return res;
  }

  const keys = Object.keys(ids);
  const results = await Promise.all(keys.map(k => fetchOne(ids[k], 0)));
  return Object.fromEntries(keys.map((k, i) => [k, results[i]]));
}
```

### The six questions to ask on any async problem

| Question | If yes, reach for |
|---|---|
| Multiple callers want the same thing at the same time? | Deduplication — `Map` + shared promise |
| Does each step depend on the previous result? | Async recursion, or sequential `await` |
| Can things run independently at the same time? | `Promise.all(items.map(...))` |
| Can it loop back on itself forever? | Depth counter, or a visited `Set` |
| Must it fail fast if too slow? | `Promise.race([work, timeout])` |
| Can it fail temporarily but succeed on retry? | Retry with exponential backoff |

### Data structure quick pick

| Structure | Use for |
|---|---|
| `Map` | Cache of key → in-flight promise. Dedup, memoisation. `.has()` `.get()` `.set()` `.delete()` |
| `Set` | Visited IDs, loop detection. O(1) `.has()` |
| `Array` | Collecting promises for `Promise.all` via `.map()` |
| Object | Structured output — `Object.keys()` + `Object.fromEntries()` |

### The eight async mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| `await` inside a plain `for` loop | Everything runs sequentially, slowly | `Promise.all` + `.map()` |
| Forgetting the argument — `apiCall()` | Returns `data-undefined` | `apiCall(id)` |
| Cache declared **inside** the function | Cache resets every call; dedup never works | Move it outside |
| Storing the *result* instead of the *promise* | Duplicate calls fire before the first resolves | Store the promise object |
| `.finally()` for cache cleanup | Timing issues — cache not cleared in time | Use `.then(fn, fn)` |
| Unhandled promise rejection | Node crashes | `.catch()` on every chain |
| No base case in recursion | Stack overflow, infinite loop | Check the exit condition first |
| Forgetting to re-throw in `.catch()` | Error swallowed; caller thinks it succeeded | `catch(err => { cleanup(); throw err; })` |

### Unhandled rejections crash Node

A rejected promise with no `.catch()` terminates a Node process. When you keep a side reference to a
promise, suppress the crash on the side chain while letting the returned promise carry the real error:

```javascript
const promise = apiCall(id);
promise.catch(() => {});      // suppress the unhandled-rejection crash
return promise;               // the caller still receives the real rejection
```

---

## 79. The JavaScript → React Bridge

Everything in this file is prerequisite to `REACT-COMPLETE-NOTES.md`. This table says which section
explains which React idiom — use it when something in React looks like magic.

| React thing | The JavaScript underneath | Section |
|---|---|---|
| `const [count, setCount] = useState(0)` | Array destructuring | §30 |
| `<Profile {...props} />` | Spread operator | §31 |
| `setUser({ ...user, name })` | Immutable update via spread | §31 |
| `{items.map(i => <li key={i.id}>{i.name}</li>)}` | `Array.map` returning values | §27 |
| `{isOpen && <Modal />}` | `&&` returns an operand, not a boolean | §10 |
| `{count ?? 0}` vs `{count \|\| 0}` | Nullish vs falsy — **`0` is falsy** | §9, §74 |
| `user?.address?.city` | Optional chaining | §74 |
| `onClick={() => handle(id)}` | Arrow function closing over `id` | §15, §19 |
| A stale value inside `useEffect` | The closure captured an earlier render's variable | §19 |
| `this.handleClick = this.handleClick.bind(this)` | A detached method loses `this` | §37, §38 |
| `function Component({ name, age = 0 })` | Parameter destructuring with defaults | §30 |
| `` className={`btn ${variant}`} `` | Template literals | §25 |
| `useEffect(() => { fetch… }, [])` | Promises, `async`/`await`, `AbortController` | §62, §64, §65 |
| Why lists need a `key` | Reference vs value identity | §7 |
| `dangerouslySetInnerHTML` | The `innerHTML` XSS risk | §48 |
| Why a new object always re-renders | `{} !== {}` — objects compare by reference | §7 |
| Custom hooks | Closures + higher-order functions | §19, §21 |
| React's synthetic events | One delegated listener at the root | §54 |
| `useMemo` / `useCallback` | Memoisation via closure | §19 |

**The five to be fluent in before opening the React notes:** destructuring (§30), spread (§31),
`map`/`filter`/`reduce` (§27), arrow functions and closures (§15, §19), and `async`/`await` (§64).
Everything else you can look up as you go.

---

## Source Files

These notes were compiled from every JavaScript file in this folder:

| File | Contributed |
|---|---|
| `1745769452351.pdf` | "JavaScript Notes for Freshers" — 48-topic structured syllabus |
| `1753509885185.pdf` | "Comprehensive JavaScript Notes: Basics to Advanced" + the To-Do project |
| `1755149071517.pdf` | Beginner cheat sheet (`coding_dev_` / Tilak) — regex tables, error types |
| `1755868507406.pdf` | 73-page handwritten course — DOM traversal, event propagation, delegation, popups |
| `1766400622505.pdf` | 50-page handwritten notes (`@programmer-girl`) — history, ECMAScript timeline, hacks |
| `JS Web API.pdf` | 22 browser Web APIs |
| `execution context in js.pdf` | Execution context, lexical/variable environment, call stack (`@MohitDecodes`) |
| `javascript-notes.pdf` | iLoveCoding visual cheat sheet — vocabulary, browser structure, event loop diagram |
| `js Array methods.pdf` | All 29 array methods in detail (`@MohitDecodes`) |
| `js fundamental questions.pdf` | 20 interview questions → **moved to the interview file** |
| `js-handwritten-notes.pdf` / `jsnotes1.pdf` | 159-page handwritten notebook (identical files) — the backbone of Parts 5 & 6 |
| `js-notes.pdf` | Handwritten notes (Ajeet Yadav) |
| `jscheatsheet.pdf` | "JavaScript Full Cheatsheet (2025 Edition)" — modern shortcuts |
| `jscheathseet.pdf` | 30 categories of built-in methods (`@MohitDecodes`) |

**Added later, from two async cheatsheets outside this folder** (`~/Documents/linkedinpdfs/` and
`~/Documents/MyVault/raw_sources/`):

| File | Contributed |
|---|---|
| `asyncjavascript.pdf` | "Async JavaScript — async/await" deep dive (Neeraj Kumar) → §78 |
| `javascriptconcepts async.pdf` | "Async JavaScript Master Cheatsheet" (Neeraj Kumar) — the five concurrency patterns, the six questions, the eight mistakes → §78 |

**Two files were excluded from these notes because they are not JavaScript:**
- `JAVABASICSPringBootstructureproject.pdf` — a one-page Java/Spring Boot prompt
- `jobsearchquestions.pdf` — 5 questions to ask an interviewer (career advice, not JS)

*No source files were modified. This is a new file compiled from reading them all.*
