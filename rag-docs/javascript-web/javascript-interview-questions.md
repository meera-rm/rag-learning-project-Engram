---
title: JAVASCRIPT-INTERVIEW-QUESTIONS
topic: javascript-web
source_type: interview-questions
source_file: STUDYNOTEs/JAVASCRIPT-INTERVIEW-QUESTIONS.md
---

# JavaScript Interview Questions & Answers


---

## Contents

**SECTION A — Core Fundamentals (Q1–Q20)** — the classic question set
**SECTION B — Rapid-Fire Questions** — quick answers for a phone screen
**SECTION C — Output-Prediction Puzzles** — "what does this log?"
**SECTION D — Coding Challenges** — implement it by hand
**SECTION E — Questions to Ask the Interviewer**

---
---

# SECTION A — Core Fundamentals

---

## Q1. What's the difference between `undefined` and `null`?

**`undefined`** is the **default value** of:
- a variable that has not been assigned a specific value
- a function that has no explicit return value (e.g. `console.log(1)`)
- a property that does not exist in an object

**The JavaScript engine does this for us** — it assigns the `undefined` value automatically.

**`null`** is **"a value that represents no value"**. It is a value that has been **explicitly
defined** by *you*. For example, you get `null` when `fs.readFile` does not throw an error.

```javascript
let a;
console.log(a);              // undefined — JS assigned it

let b = null;
console.log(b);              // null — I assigned it

console.log(typeof undefined);   // "undefined"
console.log(typeof null);        // "object"  ⚠️ a famous historical bug

console.log(null == undefined);  // true  — loose equality says they're alike
console.log(null === undefined); // false — different types
```

> **One-line answer:** `undefined` means "JavaScript hasn't given this a value yet".
> `null` means "I deliberately set this to nothing".

---

## Q2. What is the DOM?

**DOM stands for Document Object Model.** It is an **interface (an API)** for HTML and XML
documents.

When the browser first reads (parses) our HTML document, it creates a big object — a really
big object — based on the HTML document. **This is the DOM.** It is a **tree-like structure**
that is modelled from the HTML document. The DOM is used for interacting with and modifying
the DOM structure, or specific Elements or Nodes.

The **`document`** object in JavaScript represents the DOM. It provides many methods we can
use to select elements, update element contents, and much more.

```html
<html>
<head><title>DOM</title></head>
<body>
  <div>
    <p><span></span></p>
    <label></label>
    <input>
  </div>
</body>
</html>
```

Becomes:
```
document
  └── html
       ├── head → title
       └── body → div → p → span
                      → label
                      → input
```

### DOM Methods Cheat Sheet

**🔍 Selecting Elements**

| Method | Description |
|---|---|
| `document.getElementById('id')` | Selects an element by its ID |
| `document.getElementsByClassName('class')` | Returns a **live** HTMLCollection of all elements with that class |
| `document.getElementsByTagName('tag')` | Returns all elements with the specified tag name |
| `document.querySelector('selector')` | Returns the **first** element matching the CSS selector |
| `document.querySelectorAll('selector')` | Returns a NodeList of **all** elements matching the CSS selector |

**🧱 Creating and Inserting Elements**

| Method | Description |
|---|---|
| `document.createElement('tag')` | Creates a new HTML element |
| `element.appendChild(newElement)` | Appends a child to an element (at the end) |
| `element.insertBefore(newNode, referenceNode)` | Inserts a node before another inside a parent |
| `element.insertAdjacentHTML(position, html)` | Inserts HTML at `'beforebegin'`, `'afterbegin'`, `'beforeend'`, `'afterend'` |

**🛠️ Modifying Elements**

| Method | Description |
|---|---|
| `element.setAttribute('name', 'value')` | Sets an attribute on an element |
| `element.getAttribute('name')` | Gets the value of an attribute |
| `element.removeAttribute('name')` | Removes an attribute |
| `element.classList.add('class')` | Adds a class |
| `element.classList.remove('class')` | Removes a class |
| `element.classList.toggle('class')` | Toggles a class on/off |
| `element.classList.contains('class')` | Checks if a class exists |
| `element.style.property = 'value'` | Changes inline styles, e.g. `style.color = 'blue'` |

**🧹 Removing Elements**

| Method | Description |
|---|---|
| `element.remove()` | Removes the element from the DOM |
| `parent.removeChild(child)` | Removes a specified child from its parent |

**💬 Working with Content**

| Method | Description |
|---|---|
| `element.innerHTML` | Gets/sets HTML content inside the element |
| `element.textContent` | Gets/sets plain text inside the element |
| `element.innerText` | Similar to `textContent`, but **respects CSS styling** |
| `element.value` | Used with input/textarea to get/set user input |

**🎯 Event Handling**

| Method | Description |
|---|---|
| `element.addEventListener('event', callback)` | Adds an event listener |
| `element.removeEventListener('event', callback)` | Removes an event listener |
| `event.preventDefault()` | Prevents default browser behaviour (e.g. stop form submission) |
| `event.stopPropagation()` | Stops the event from bubbling up the DOM |

**✅ Example**
```javascript
const button = document.createElement('button');
button.textContent = "Click Me";
button.classList.add('my-btn');
document.body.appendChild(button);

button.addEventListener('click', () => {
  alert('Button Clicked!');
});
```

---

## Q3. What is Event Propagation?

**When an event occurs on a DOM element, that event does not entirely occur on that just one
element.**

- In the **Bubbling Phase**, the event bubbles up: it goes to its parent, to its grandparent,
  to its grandparent's parent, until it reaches all the way to the `window`.
- In the **Capturing Phase**, the event starts from the `window` and goes down to the element
  that triggered the event — the `event.target`.

**Event Propagation has three phases:**

1. **Capturing Phase** — the event starts from `window`, then goes down through every element
   until it reaches the target element.
2. **Target Phase** — the event has reached the target element.
3. **Bubbling Phase** — the event bubbles up from the target element, then goes up through
   every element until it reaches the `window`.

```
CAPTURING ↓                              BUBBLING ↑
window  →  html  →  body  →  div  →  [TARGET]  →  div  →  body  →  html  →  window
```

**Controlling it:** the third argument of `addEventListener()` decides the phase.
```javascript
el.addEventListener('click', fn);          // false (default) = BUBBLING
el.addEventListener('click', fn, true);    // true            = CAPTURING
```

Use `e.stopPropagation()` or `e.stopImmediatePropagation()` to stop it.

---

## Q4. What's the difference between `event.preventDefault()` and `event.stopPropagation()`?

**They solve completely different problems.**

**`event.preventDefault()`** prevents the **default behaviour** of an element:
- If used in a **form** element, it prevents it from **submitting**
- If used in an **anchor** element, it prevents it from **navigating**
- If used in a **contextmenu**, it prevents it from **showing/displaying**

**`event.stopPropagation()`** stops the **propagation of an event** — it stops the event from
occurring in the bubbling or capturing phase.

```javascript
// preventDefault — the click still bubbles, but the link doesn't navigate
link.addEventListener('click', e => e.preventDefault());

// stopPropagation — the link still navigates, but the parent's handler won't fire
child.addEventListener('click', e => e.stopPropagation());

// You can use both together
form.addEventListener('submit', e => {
  e.preventDefault();      // don't reload the page
  e.stopPropagation();     // don't let ancestors hear about it
});
```

> **Memory aid:** `preventDefault` stops **what the browser would do**.
> `stopPropagation` stops **where the event goes**.

---

## Q5. Why does this code `obj.someprop.x` throw an error?

```javascript
const obj = {};
console.log(obj.someprop.x);
```

**This throws an error** because we are trying to access an **`x` property inside the
`someprop` property**, which has an `undefined` value.

Remember: **properties in an object which do not exist in itself and in its prototype have a
default value of `undefined`** — and **`undefined` has no property `x`**.

```
obj.someprop        → undefined
undefined.x         → ❌ TypeError: Cannot read properties of undefined (reading 'x')
```

**The fixes:**
```javascript
// 1. Optional chaining (modern, best)
console.log(obj.someprop?.x);            // undefined — no crash

// 2. Guard clause
if (obj.someprop) console.log(obj.someprop.x);

// 3. Default value
console.log(obj.someprop?.x ?? "not found");
```

---

## Q6. What is `event.target`?

**In simplest terms, `event.target` is the element on which the event occurred — the element
that triggered the event.**

**Sample HTML:**
```html
<div onclick="clickFunc(event)" style="text-align:center; margin:15px;
     border:1px solid red; border-radius:3px;">
  <div style="margin:25px; border:1px solid royalblue; border-radius:3px;">
    <div style="margin:25px; border:1px solid skyblue; border-radius:3px;">
      <button style="margin:10px">Button</button>
    </div>
  </div>
</div>
```

**Sample JavaScript:**
```javascript
function clickFunc(event) {
  console.log(event.target);
}
```

**If you click the button it will log the BUTTON markup**, even though we attached the event
on the outermost `div`. It will always log the button. So we can conclude that **`event.target`
is the element that triggered the event**.

**Bonus — `target` vs `currentTarget`:**

| | Refers to |
|---|---|
| `event.target` | The element that was **actually** clicked (the deepest one) |
| `event.currentTarget` | The element the **listener is attached to** |

---

## Q7. What's the difference between `==` and `===`?

**The difference between `==` (abstract equality) and `===` (strict equality) is that `==`
compares by value AFTER COERCION, and `===` compares by value AND TYPE WITHOUT COERCION.**

**Coercion** is the process of converting a value to another type. The `==` operator does
**implicit coercion**.

### The `==` algorithm

Suppose we compare `x == y`:

1. If `x` and `y` have the **same type**, compare them with the `===` operator.
2. If `x` is `null` and `y` is `undefined`, return **`true`**.
3. If `x` is `undefined` and `y` is `null`, return **`true`**.
4. If `x` is type **number** and `y` is type **string**, return `x == toNumber(y)`.
5. If `x` is type **string** and `y` is type **number**, return `toNumber(x) == y`.
6. If `x` is type **boolean**, return `toNumber(x) == y`.
7. If `y` is type **boolean**, return `x == toNumber(y)`.
8. If `x` is `string`/`symbol`/`number` and `y` is type **object**, return `x == toPrimitive(y)`.
9. If `x` is **object** and `y` is `string`/`symbol`, return `toPrimitive(x) == y`.
10. Otherwise return **`false`**.

> **Note:** `toPrimitive` uses first the `valueOf` method, then the `toString` method, to get
> the primitive value of that object.

### Examples with `==` — these all return `true`

| x | y | `x == y` | Why |
|---|---|---|---|
| `5` | `5` | `true` | Condition 1 — same type and value |
| `1` | `'1'` | `true` | Condition 4 — `y` converted to a number |
| `null` | `undefined` | `true` | Condition 2 |
| `0` | `false` | `true` | Condition 7 — `y` is boolean, becomes `0` |
| `'1,2'` | `[1,2]` | `true` | Condition 8 — the array became `"1,2"` via `toString()` |
| `'[object Object]'` | `{}` | `true` | Condition 10 path — the object became `"[object Object]"` |

### The same examples with `===`

| x | y | `x === y` |
|---|---|---|
| `5` | `5` | **`true`** |
| `1` | `'1'` | `false` |
| `null` | `undefined` | `false` |
| `0` | `false` | `false` |
| `'1,2'` | `[1,2]` | `false` |
| `'[object Object]'` | `{}` | `false` |

**If we use the `===` operator, all the comparisons except for the first example return
`false`**, because they don't have the same type. The first returns `true` because the two
have the same type and value.

> ✅ **Always use `===`.** The only common exception is `x == null`, which conveniently checks
> for both `null` and `undefined` at once.

---

## Q8. What is Hoisting?

**Hoisting is the term used to describe the moving of variables and functions to the top of
their (global or function) scope, where we define that variable or function.**

To understand hoisting, you have to understand the **execution context**.

**The Execution Context is the "environment of code" that is currently executing.** It has
**two phases: compilation and execution.**

**Compilation phase** — it gets all the **function declarations** and hoists them up to the
top of their scope, so we can reference them later. It also gets all **variables declared with
the `var` keyword**, hoists them up, and gives them a default value of **`undefined`**.

**Execution phase** — it assigns values to the variables hoisted earlier, and it executes or
invokes functions (methods in objects).

> **⚠️ Note: ONLY function declarations and variables declared with the `var` keyword are
> hoisted — NOT function expressions, arrow functions, `let`, or `const`.**

### Worked example

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

**This code logs `undefined`, `1`, `Hello Mark!` respectively.**

**The compilation phase would look like this:**
```javascript
function greet(name) {
    return 'Hello ' + name + '!';
}

var y;   // implicit "undefined" assignment

// waiting for the "compilation" phase to finish
// then start the "execution" phase
/*
console.log(y);
y = 1;
console.log(y);
console.log(greet("Mark"));
*/
```

**After the compilation phase finishes, it starts the execution phase** — invoking methods and
assigning values to variables:
```javascript
function greet(name) {
    return 'Hello ' + name + '!';
}
var y;

// start "execution" phase
console.log(y);            // undefined
y = 1;
console.log(y);            // 1
console.log(greet("Mark")); // Hello Mark!
```

### What about `let` and `const`?

They **are** hoisted, but placed in the **Temporal Dead Zone (TDZ)** — accessing them before
their declaration throws a `ReferenceError` rather than giving `undefined`.

```javascript
console.log(a);   // undefined ✅
var a = 1;

console.log(b);   // ❌ ReferenceError: Cannot access 'b' before initialization
let b = 1;
```

---

## Q9. What are Closures?

**Closures is simply the ability of a function at the time of DECLARATION to remember the
references of variables and parameters on its current scope, on its parent function scope, on
its parent's parent function scope, until it reaches the global scope — with the help of the
Scope Chain. Basically it is the Scope created when the function was declared.**

### Simple example

```javascript
// Global's Scope
var globalVar = "abc";

function a(){
    // a's Scope
    console.log(globalVar);
}

a();   // logs "abc"

/* Scope Chain from inside function a:
     a's scope → global's scope
*/
```

In this example, when we declare the `a` function, the **Global Scope is part of `a`'s
closure**.

The variable `globalVar` doesn't have a fixed value in the closure diagram, because **the
value of that variable can change based on where and when we invoke the `a` function.** In our
example it will have the value `"abc"`.

### Complex example

```javascript
var globalVar = "global";
var outerVar  = "outer";

function outerFunc(outerParam) {
   function innerFunc(innerParam) {
       console.log(globalVar, outerParam, innerParam);
   }
   return innerFunc;
}

const x = outerFunc(outerVar);
outerVar  = "outer-2";
globalVar = "guess";
x("inner");
```

**This will print `"guess outer inner"`.**

**The explanation:**
- When we invoke `outerFunc` and assign the returned `innerFunc` to the variable `x`, the
  `outerParam` will have a value of **`"outer"`** — even though we assign a new value
  `"outer-2"` to `outerVar` — because **the reassignment happened AFTER the invocation** of
  the outer function. At the time we invoked `outerFunc`, it looked up the value of `outerVar`
  in the Scope Chain, and `outerVar` had the value `"outer"`.
- When we invoke the `x` variable (which holds a reference to `innerFunc`), `innerParam` has
  the value **`"inner"`** because that's the value we passed in at invocation.
- The `globalVar` variable has the value **`"guess"`** because **before** the invocation of
  `x`, we assigned a new value to `globalVar`, and at the time of invoking `x`, the value of
  `globalVar` in the Scope Chain is `"guess"`.

### The problem example

We have an example that demonstrates a problem of not understanding closures correctly:

```javascript
const arrFuncs = [];
for(var i = 0; i < 5; i++){
    arrFuncs.push(function (){
       return i;
    });
}
console.log(i); // i is 5

for (let i = 0; i < arrFuncs.length; i++) {
    console.log(arrFuncs[i]()); // all log "5"
}
```

**This code is not working as we expected because of Closures.**

The `var` keyword makes a **global variable**, and when we push a function we return the
global variable `i`. So when we call one of those functions in that array after the loop, it
logs `5` — because we get the **current** value of `i`, which is `5`, and we can access it
because it's a global variable.

**Because Closures keep the REFERENCES of that variable, not its VALUES at the time of its
creation.**

**We can solve this using IIFEs or by changing the `var` keyword to `let` for block-scoping.**

```javascript
// Fix 1 — let creates a new binding per iteration
for (let i = 0; i < 5; i++) {
    arrFuncs.push(function () { return i; });
}   // now logs 0, 1, 2, 3, 4 ✅

// Fix 2 — IIFE captures the value
for (var i = 0; i < 5; i++) {
    (function(captured) {
        arrFuncs.push(function () { return captured; });
    })(i);
}
```

### The practical use — private state

```javascript
function createCounter() {
  let count = 0;                    // private
  return {
    increment: () => ++count,
    getCount:  () => count
  };
}
const c = createCounter();
c.increment();
console.log(c.getCount());   // 1
console.log(c.count);        // undefined — genuinely private ✅
```

---

## Q10. What's the value of `this` in JavaScript?

**Basically, `this` refers to the value of the object that is currently executing or invoking
the function.** We say "currently" because **the value of `this` changes depending on the
context in which we use it, and where we use it.**

### The normal case

```javascript
const carDetails = {
  name: "Ford Mustang",
  yearBought: 2005,
  getName(){
       return this.name;
  },
  isRegistered: true
};

console.log(carDetails.getName());   // logs "Ford Mustang"
```

This is what we would normally expect, because in the `getName` method we return `this.name`.
`this` in this context refers to the object which is the `carDetails` object — currently the
**"owner" object** of the function executing.

### Now let's make it weird

Add these three lines below the `console.log` statement:

```javascript
var name = "Ford Ranger";
var getCarName = carDetails.getName;

console.log(getCarName());   // logs "Ford Ranger"
```

**The second `console.log` prints `"Ford Ranger"`, which is weird**, because the first
printed `"Ford Mustang"`.

**The reason:** the `getCarName` method has a **different "owner" object — the `window`
object**. Declaring variables with the `var` keyword in the global scope attaches properties
to the `window` object with the same name as the variables. **Remember, `this` in the global
scope refers to the `window` object when `"use strict"` is not used.**

```javascript
console.log(getCarName === window.getCarName);   // logs true
console.log(getCarName === this.getCarName);     // logs true
```
`this` and `window` in this example refer to the same object.

### Solving it with `apply` and `call`

```javascript
console.log(getCarName.apply(carDetails));   // logs "Ford Mustang"
console.log(getCarName.call(carDetails));    // logs "Ford Mustang"
```

**The `apply` and `call` methods expect the first parameter to be an object, which becomes the
value of `this` inside that function.**

### Things that default `this` to `window`

**IIFEs, functions declared in the global scope, anonymous functions, and inner functions in
methods inside an object** all have a default `this` which points to the `window` object.

```javascript
(function (){
  console.log(this);       // logs the "window" object
})();

function iHateThis(){
  console.log(this);
}
iHateThis();               // logs the "window" object

const myFavoriteObj = {
 guessThis(){
   function getThis(){
     console.log(this);    // logs the "window" object
   }
   getThis();
 },
 name: 'Marko Polo',
 thisIsAnnoying(callback){
   callback();
 }
};

myFavoriteObj.guessThis();                        // logs "window"
myFavoriteObj.thisIsAnnoying(function (){
  console.log(this);                              // logs "window"
});
```

### Two ways to fix it

**First — save the value of `this` in a variable:**
```javascript
const myFavoriteObj = {
 guessThis(){
   const self = this;          // saves the this value to the "self" variable
   function getName(){
     console.log(self.name);   // "Marko Polo" ✅
   }
   getName();
 },
 name: 'Marko Polo',
 thisIsAnnoying(callback){ callback(); }
};
```
In this case we save the value of `this` (which would be the `myFavoriteObj` object), so we
can access it inside the `getName` inner function.

**Second — use ES6 Arrow Functions:**
```javascript
const myFavoriteObj = {
 guessThis(){
   const getName = () => {
     // copies the value of "this" outside of this arrow function
     console.log(this.name);   // "Marko Polo" ✅
   };
   getName();
 },
 name: 'Marko Polo',
 thisIsAnnoying(callback){ callback(); }
};
```

**Arrow Functions do not have their own `this`. They copy the value of `this` of the enclosing
lexical scope** — in this example the value of `this` outside the `getName` inner function,
which would be the `myFavoriteObj` object.

**We can also determine the value of `this` by how the function is invoked.**

### Summary table

| How it's called | `this` is |
|---|---|
| Plain function | `window` (or `undefined` in strict mode) |
| Method `obj.fn()` | `obj` |
| `new Fn()` | The new instance |
| Arrow function | Inherited from the enclosing lexical scope |
| `fn.call/apply/bind(x)` | `x` |
| Event handler | The element that received the event |

---

## Q11 & Q18. What are Higher Order Functions?

**Higher-Order Functions are functions that can RETURN a function, or RECEIVE an argument or
arguments which have a value of a function.**

```javascript
function higherOrderFunction(param, callback){
    return callback(param);
}
```

**Taking a function:**
```javascript
function operate(a, b, operation) { return operation(a, b); }
operate(10, 5, (x, y) => x + y);   // 15
```

**Returning a function:**
```javascript
function multiplier(factor) {
  return (n) => n * factor;
}
const double = multiplier(2);
console.log(double(5));   // 10
```

**Built-in examples:** `map`, `filter`, `reduce`, `forEach`, `sort`, `setTimeout`,
`addEventListener`.

---

## Q12. Why are functions called First-class Objects?

**Functions in JavaScript are First-class Objects because they are treated as any other value
in the language.** They can be:

- **assigned to variables**
- **properties of an object** — which are then called **methods**
- **an item in an array**
- **passed as arguments** to a function
- **returned as values** of a function

**The ONLY difference between a function and any other value in JavaScript is that functions
can be INVOKED or CALLED.**

```javascript
const fn = function() {};              // assigned to a variable
const obj = { method: function() {} }; // a property → a method
const arr = [function() {}];           // an item in an array
[1,2].map(function(x) { return x; });  // passed as an argument
function outer() { return function() {}; }  // returned as a value
```

---

## Q13. Implement the `Array.prototype.map` method by hand.

**MDN description:** *The `map()` method creates a new array with the results of calling a
provided function on every element in the calling array.*

### Version 1 — as a standalone function

```javascript
function map(arr, mapCallback) {
  // First, we check if the parameters passed are right.
  if (!Array.isArray(arr) || !arr.length || typeof mapCallback !== 'function') {
    return [];
  } else {
    let result = [];
    // We're making a results array every time we call this function
    // because we don't want to mutate the original array.
    for (let i = 0, len = arr.length; i < len; i++) {
      result.push(mapCallback(arr[i], i, arr));
      // push the result of the mapCallback into the 'result' array
    }
    return result;   // return the result array
  }
}

const numbers = [1, 2, 3, 4];
const doubled = map(numbers, function(num) {
  return num * 2;
});
console.log(doubled);   // [2, 4, 6, 8]
```

### Version 2 — as a real prototype method

```javascript
Array.prototype.myMap = function(callback) {
  // Ensure 'this' is an array
  if (!Array.isArray(this)) {
      throw new TypeError('Called on non-array');
  }

  // Ensure callback is a function
  if (typeof callback !== 'function') {
    throw new TypeError(callback + ' is not a function');
  }

  const result = [];

  for (let i = 0; i < this.length; i++) {
    // Check if the index exists (to skip holes in sparse arrays)
    if (i in this) {
      result.push(callback(this[i], i, this));
    }
  }

  return result;
};

const numbers = [1, 2, 3, 4];
const doubled = numbers.myMap(function(num) {
  return num * 2;
});
console.log(doubled);   // [2, 4, 6, 8]
```

---

## Q14. Implement the `Array.prototype.filter` method by hand.

**MDN description:** *The `filter()` method creates a new array with all elements that pass
the test implemented by the provided function.*

```javascript
function filter(arr, filterCallback) {
  // First, we check if the parameters passed are right.
  if (!Array.isArray(arr) || !arr.length || typeof filterCallback !== 'function') {
    return [];
  } else {
    let result = [];
    // We're making a results array every time we call this function
    // because we don't want to mutate the original array.
    for (let i = 0, len = arr.length; i < len; i++) {
      // check if the return value of the filterCallback is true or "truthy"
      if (filterCallback(arr[i], i, arr)) {
        // push the current item into the 'result' array if the condition is true
        result.push(arr[i]);
      }
    }
    return result;   // return the result array
  }
}

const numbers = [1, 2, 3, 4, 5];
const evens = filter(numbers, function(num) {
  return num % 2 === 0;
});
console.log(evens);   // [2, 4]
```

---

## Q15. Implement the `Array.prototype.reduce` method by hand.

**MDN description:** *The `reduce()` method executes a reducer function (that you provide) on
each element of the array, resulting in a single output value.*

```javascript
function reduce(arr, reduceCallback, initialValue) {
  // First, we check if the parameters passed are right.
  if (!Array.isArray(arr) || !arr.length || typeof reduceCallback !== 'function') {
    return [];
  } else {
    // If no initialValue has been passed to the function we're gonna use the
    // first array item as the initialValue
    let hasInitialValue = initialValue !== undefined;
    let value = hasInitialValue ? initialValue : arr[0];

    // Then we're gonna start looping at index 1 if there is no
    // initialValue passed to the function, else we start at 0 if
    // there is an initialValue.
    for (let i = hasInitialValue ? 0 : 1, len = arr.length; i < len; i++) {
        // Then for every iteration we assign the result of the
        // reduceCallback to the variable value.
        value = reduceCallback(value, arr[i], i, arr);
    }
    return value;
  }
}

const numbers = [1, 2, 3, 4];
const sum = reduce(numbers, function(acc, curr) {
  return acc + curr;
}, 0);
console.log(sum);   // 10
```

---

## Q16. What are Classes?

**Classes are the new way of writing constructor functions in JavaScript. It is SYNTACTIC
SUGAR for using constructor functions — it still uses prototypes and Prototype-Based
Inheritance under the hood.**

### ES5 vs ES6

```javascript
// ES5 Version
function Person(firstName, lastName, age, address){
    this.firstName = firstName;
    this.lastName  = lastName;
    this.age       = age;
    this.address   = address;
}

Person.self = function(){
  return this;
};

Person.prototype.toString = function(){
  return "[object Person]";
};

Person.prototype.getFullName = function (){
  return this.firstName + " " + this.lastName;
};


// ES6 Version
class Person {
     constructor(firstName, lastName, age, address){
       this.lastName  = lastName;
       this.firstName = firstName;
       this.age       = age;
       this.address   = address;
     }

     static self() {
         return this;
     }

     toString(){
         return "[object Person]";
     }

     getFullName(){
       return `${this.firstName} ${this.lastName}`;
     }
}
```

### Overriding methods and inheriting from another class

```javascript
// ES5 Version
Employee.prototype = Object.create(Person.prototype);

function Employee(firstName, lastName, age, address, jobTitle, yearStarted) {
  Person.call(this, firstName, lastName, age, address);
  this.jobTitle    = jobTitle;
  this.yearStarted = yearStarted;
}

Employee.prototype.describe = function () {
  return `I am ${this.getFullName()} and I have a position of ${this.jobTitle} ` +
         `and I started at ${this.yearStarted}`;
};

Employee.prototype.toString = function () {
  return "[object Employee]";
};


// ES6 Version
class Employee extends Person {          // Inherits from the "Person" class
  constructor(firstName, lastName, age, address, jobTitle, yearStarted) {
    super(firstName, lastName, age, address);
    this.jobTitle    = jobTitle;
    this.yearStarted = yearStarted;
  }

  describe() {
    return `I am ${this.getFullName()} and I have a position of ${this.jobTitle} ` +
           `and I started at ${this.yearStarted}`;
  }

  toString() {    // Overriding the "toString" method of "Person"
    return "[object Employee]";
  }
}
```

### So how do we know it uses prototypes under the hood?

```javascript
class Something { }
function AnotherSomething(){ }

const as = new AnotherSomething();
const s  = new Something();

console.log(typeof Something);          // logs "function"
console.log(typeof AnotherSomething);   // logs "function"
console.log(as.toString());             // logs "[object Object]"
console.log(s.toString());              // logs "[object Object]"
console.log(as.toString === Object.prototype.toString);   // true
console.log(s.toString  === Object.prototype.toString);   // true
```

**Both logs return `true`, indicating that we are still using prototypes under the hood** —
because `Object.prototype` is the last part of the Prototype Chain, and both `Something` and
`AnotherSomething` inherit from `Object.prototype`.

---

## Q17 & Q19. What is a Callback function?

**A Callback function is a function that is going to get called at a later point in time.**

```javascript
const btnAdd = document.getElementById('btnAdd');

btnAdd.addEventListener('click', function clickCallback(e) {
  // do something useless
});
```

In this example, we wait for the `click` event on the element with an id of `btnAdd`. **If it
is clicked, the `clickCallback` function is executed.**

**A Callback function adds some functionality to some data or event.** The `reduce`, `filter`
and `map` methods in Array expect a callback as a parameter.

> **A good analogy for a callback:** when you call someone and they don't answer, you leave a
> message and you expect them to **call back**. The act of calling someone or leaving a
> message is the **event or data**, and the **callback is the action that you expect to occur
> later**.

---

## Q20. What are the ways of handling asynchronous operations in JavaScript?

In JavaScript, handling asynchronous operations is essential when working with tasks like API
calls, file reading, timers, or any operations that take time to complete. JavaScript provides
several ways to manage async code efficiently:

### 1. Callbacks

A callback is a function passed into another function to be called once an operation is
complete.

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback('Data received');
  }, 1000);
}

fetchData((data) => {
  console.log(data);   // Logs after 1 second
});
```

❌ **Can lead to callback hell** (deeply nested callbacks), which is hard to manage.

### 2. Promises

A Promise represents a value that will be available now, later, or never.

```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received');
    }, 1000);
  });
};

fetchData().then(data => console.log(data));
```

✅ Cleaner than callbacks
❌ Can still get messy with multiple `.then()` calls

### 3. Async/Await

Introduced in **ES2017**, `async/await` makes asynchronous code look synchronous.

```javascript
const fetchData = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Data received');
    }, 1000);
  });
};

async function getData() {
  const result = await fetchData();
  console.log(result);
}

getData();
```

✅ Very clean and readable
❌ Must be used inside an `async` function

### 4. Promise.all / Promise.allSettled / Promise.race

Used for handling multiple asynchronous operations in parallel.

**`Promise.all`** (waits for **all** promises):
```javascript
Promise.all([fetchData1(), fetchData2()])
 .then(([res1, res2]) => {
   console.log(res1, res2);
 });
```

**`Promise.race`** — resolves/rejects as soon as the **first** promise settles
**`Promise.allSettled`** — returns the results of **all**, regardless of success/failure

### 5. Observable (Advanced)

Used in **RxJS** (Reactive Programming) for handling complex async data streams (e.g. Angular
apps).

```javascript
import { of } from 'rxjs';

of('Hello').subscribe((data) => {
  console.log(data);
});
```

✅ Powerful for real-time data streams
❌ Requires learning RxJS

---
---

# SECTION B — Rapid-Fire Questions

Short, common questions with short answers.

### Q. What is JavaScript?
A high-level, interpreted, lightweight, dynamically-typed, single-threaded, case-sensitive
programming language used to add interactivity and logic to web pages. Runs in browsers and,
via Node.js, on servers.

### Q. Who created JavaScript and what was it first called?
**Brendan Eich**, a Netscape programmer, created it in **just 10 days in September 1995**. It
was first called **Mocha**, then **LiveScript**, then **JavaScript** (a marketing decision
because Java was popular).

### Q. Is JavaScript the same as Java?
**No.** They are completely different languages with nothing in common but four letters in the
name.

### Q. What is ECMAScript?
The **official specification** that JavaScript implements, maintained by **Ecma
International** (founded 1996). ES1 was released in 1997. **ES6 (2015)** was the biggest
update. Since 2015, TC39 releases a new version **annually**.

### Q. What are the data types in JavaScript?
**Primitive (7):** String, Number, Boolean, Undefined, Null, Symbol, BigInt.
**Non-primitive:** Object (and its subtypes Array, Function, RegExp, Date).

### Q. What does `typeof null` return, and why?
`"object"`. It's a **bug** from the original 1995 implementation that can never be fixed
without breaking existing websites.

### Q. Difference between `var`, `let` and `const`?

| | Scope | Re-declare | Re-assign | Hoisted as |
|---|---|:---:|:---:|---|
| `var` | Function | ✅ | ✅ | `undefined` |
| `let` | Block | ❌ | ✅ | TDZ (error) |
| `const` | Block | ❌ | ❌ | TDZ (error) |

`const` prevents **reassignment**, not **mutation** — you can still change an object's
properties.

### Q. What is the Temporal Dead Zone?
The period between entering a block and the `let`/`const` declaration being executed.
Accessing the variable in this window throws a `ReferenceError`.

### Q. What are the falsy values?
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. **Everything else is truthy** —
including `[]` and `{}`.

### Q. What is coercion?
The automatic conversion of one type to another. Priority order: **String → Number →
Boolean**. `2 + "7"` gives `"27"`; `true - 5` gives `-4`.

### Q. `slice()` vs `splice()`?
`slice(start, end)` returns a copy, **doesn't mutate**.
`splice(start, deleteCount, ...items)` removes/inserts, **mutates**, returns what it removed.

### Q. `map()` vs `forEach()`?
`map` returns a **new array** of the same length and is chainable.
`forEach` returns `undefined` and is used for side effects only.

### Q. `find()` vs `filter()`?
`find` returns the **first matching element** (or `undefined`).
`filter` returns a **new array of all matches** (possibly empty).

### Q. `some()` vs `every()`?
`some` → `true` if **at least one** passes. `every` → `true` only if **all** pass.

### Q. Why does `[10, 9, 1].sort()` give `[1, 10, 9]`?
By default `sort()` converts elements to **strings** and sorts lexicographically.
Fix: `sort((a, b) => a - b)`.

### Q. Shallow copy vs deep copy?
**Shallow** copies only the top level; nested objects are still shared by reference
(`{...obj}`, `Object.assign`, `slice`).
**Deep** copies everything (`structuredClone(obj)`, or `JSON.parse(JSON.stringify(obj))` —
which loses functions, dates and `undefined`).

### Q. `null` vs `undefined` vs `NaN`?
`undefined` = not assigned. `null` = deliberately empty. `NaN` = "Not a Number", the result of
an invalid maths operation. `typeof NaN` is `"number"`, and `NaN !== NaN`.

### Q. How do you check for `NaN`?
`Number.isNaN(x)` — the strict version. Avoid the global `isNaN()`, which coerces first
(`isNaN("hello")` is `true`).

### Q. Arrow function vs regular function?

| | Regular | Arrow |
|---|---|---|
| `this` | Own binding, depends on call site | **Lexical** — inherited |
| `arguments` object | ✅ Yes | ❌ No |
| Usable as constructor (`new`) | ✅ Yes | ❌ No |
| Hoisted (declaration form) | ✅ Yes | ❌ No |
| Good as an object method | ✅ Yes | ❌ **No** |

### Q. What is an IIFE and why use one?
An **Immediately Invoked Function Expression** — `(function(){ })();`. It runs instantly and
creates a **private scope**, avoiding global namespace pollution. Before ES6 modules and
`let`, this was the main encapsulation tool.

### Q. What is `use strict`?
A directive that makes JavaScript stricter: undeclared variables throw, reserved words are
blocked, duplicate parameters are illegal, `this` is `undefined` in plain functions, and some
silent failures become errors. **Modules and classes are strict automatically.**

### Q. What is the Event Loop?
The mechanism that lets single-threaded JavaScript handle async work. Long tasks are handed to
browser Web APIs; their callbacks queue up; the **Event Loop moves a queued callback onto the
call stack only when the stack is empty**. **Microtasks (Promises) are drained before
macrotasks (`setTimeout`).**

### Q. `setTimeout(fn, 0)` — does it run immediately?
**No.** It runs after all synchronous code finishes and the call stack is empty. It's the
*minimum* delay, not a guarantee.

### Q. What are the states of a Promise?
**pending**, **fulfilled**, **rejected** — and **settled** (meaning either fulfilled or
rejected).

### Q. `Promise.all` vs `allSettled` vs `race` vs `any`?

| | Resolves when | Rejects when |
|---|---|---|
| `all` | All succeed | Any one fails |
| `allSettled` | All settle | **Never** |
| `race` | First settles | First settles as a rejection |
| `any` | First succeeds | All fail |

### Q. Does `fetch()` reject on a 404?
**No.** It only rejects on network failure. A 404 or 500 still resolves. You must check
`response.ok` yourself.

### Q. What is a prototype?
An object that other objects inherit properties and methods from. Every object has an internal
`[[Prototype]]` link. Looking up a property walks this **prototype chain** until it finds the
property or reaches `null`.

### Q. `call` vs `apply` vs `bind`?
`call(thisArg, a, b)` — invokes now, comma-separated args.
`apply(thisArg, [a, b])` — invokes now, **array** of args.
`bind(thisArg)` — **returns a new function** with `this` locked; doesn't invoke.

### Q. What is event delegation and why is it useful?
Attaching **one** listener to a parent instead of many to children, then using `event.target`
to identify what was clicked. **Better performance**, and it **automatically works for
elements added later**.

### Q. `innerHTML` vs `textContent` vs `innerText`?
`innerHTML` parses HTML — **XSS risk with user input**.
`textContent` gets/sets all text including hidden — **safe and fast**.
`innerText` respects CSS, so it excludes hidden text and triggers a reflow — slower.

### Q. localStorage vs sessionStorage vs cookies?

| | Lifetime | Size | Sent to server |
|---|---|---|---|
| `localStorage` | Until manually cleared | ~5–10MB | ❌ |
| `sessionStorage` | Until the tab closes | ~5–10MB | ❌ |
| Cookies | Until `expires`/`max-age` | ~4KB | ✅ Every request |

### Q. `==` vs `===` in one line?
`==` compares after **type coercion**; `===` compares **value and type** with no coercion.
Always use `===`.

### Q. What is a pure function?
A function that (1) always returns the same output for the same input, and (2) has **no side
effects** — it doesn't modify anything outside itself.

### Q. What's the difference between an HTMLCollection and a NodeList?
`getElementsByClassName`/`TagName` return a **live** HTMLCollection (updates with the DOM).
`querySelectorAll` returns a **static** NodeList (a snapshot). Neither is a real array —
`NodeList` has `forEach`, `HTMLCollection` doesn't. Use `[...collection]` to convert.

### Q. What is currying?
Transforming a function of many arguments into a chain of single-argument functions:
`f(a, b, c)` → `f(a)(b)(c)`. Useful for partial application.
```javascript
const add = a => b => a + b;
add(2)(3);   // 5
```

### Q. What is debouncing vs throttling?
**Debounce** — wait until the user *stops* firing events, then run once (search-as-you-type).
**Throttle** — run at most once every N milliseconds (scroll, resize handlers).

---
---

# SECTION C — Output-Prediction Puzzles

These test whether you truly understand the mechanics. Predict before revealing.

### Puzzle 1 — Hoisting
```javascript
console.log(a);
var a = 1;
console.log(b);
let b = 2;
```
<details><summary>Answer</summary>

`undefined`, then a **ReferenceError**. `var a` is hoisted and initialised to `undefined`;
`let b` is in the Temporal Dead Zone.
</details>

### Puzzle 2 — The event loop
```javascript
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
```
<details><summary>Answer</summary>

**`1, 4, 3, 2`.** Synchronous code first (`1`, `4`), then the **microtask** queue (`3`, the
Promise), then the **macrotask** queue (`2`, the timeout).
</details>

### Puzzle 3 — The classic loop
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```
<details><summary>Answer</summary>

**`3, 3, 3`.** `var` is function-scoped, so all three callbacks close over the *same* `i`,
which is `3` by the time they run. Change `var` to `let` to get `0, 1, 2`.
</details>

### Puzzle 4 — `this` in a method vs a callback
```javascript
const obj = {
  name: "Ann",
  regular() { console.log(this.name); },
  arrow: () => console.log(this.name)
};
obj.regular();
obj.arrow();
```
<details><summary>Answer</summary>

`"Ann"`, then `undefined`. The arrow function has no `this` of its own and inherits from the
enclosing (global) scope — **never use an arrow function as an object method**.
</details>

### Puzzle 5 — Coercion
```javascript
console.log(1 + "1");
console.log(1 - "1");
console.log([] + []);
console.log([] + {});
console.log(0.1 + 0.2 === 0.3);
```
<details><summary>Answer</summary>

`"11"` (`+` concatenates with a string), `0` (`-` coerces to numbers), `""` (both arrays
stringify to `""`), `"[object Object]"`, and `false` (floating-point precision — it's
`0.30000000000000004`).
</details>

### Puzzle 6 — Reference vs value
```javascript
let a = { x: 1 };
let b = a;
b.x = 2;
console.log(a.x);

let c = 1;
let d = c;
d = 2;
console.log(c);
```
<details><summary>Answer</summary>

`2`, then `1`. Objects are copied **by reference**; primitives **by value**.
</details>

### Puzzle 7 — const with objects
```javascript
const arr = [1, 2, 3];
arr.push(4);
console.log(arr);
arr = [5];
```
<details><summary>Answer</summary>

`[1, 2, 3, 4]`, then a **TypeError: Assignment to constant variable**. `const` blocks
reassignment, not mutation.
</details>

### Puzzle 8 — Sorting
```javascript
console.log([1, 10, 2, 21].sort());
```
<details><summary>Answer</summary>

`[1, 10, 2, 21]`. `sort()` converts to strings, so `"10"` comes before `"2"`.
</details>

### Puzzle 9 — Async ordering
```javascript
async function f() {
  console.log('A');
  await null;
  console.log('B');
}
f();
console.log('C');
```
<details><summary>Answer</summary>

`A, C, B`. Everything before the first `await` runs synchronously. The `await` yields control,
so `C` runs, then `B` runs as a microtask.
</details>

### Puzzle 10 — Truthiness
```javascript
if ([]) console.log("array");
if ({}) console.log("object");
if ("0") console.log("string zero");
if (0)  console.log("number zero");
```
<details><summary>Answer</summary>

`"array"`, `"object"`, `"string zero"` all log. `0` does not. **Empty arrays and objects are
truthy**; only `0` is falsy here.
</details>

---
---

# SECTION D — Coding Challenges

Common "implement this on a whiteboard" tasks.

### 1. Reverse a string
```javascript
const reverse = s => s.split("").reverse().join("");
// Without built-ins:
function reverse(s) {
  let out = "";
  for (let i = s.length - 1; i >= 0; i--) out += s[i];
  return out;
}
```

### 2. Check if a string is a palindrome
```javascript
function isPalindrome(s) {
  const clean = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  return clean === [...clean].reverse().join("");
}
```

### 3. Find the largest number in an array
```javascript
const max = arr => Math.max(...arr);
const max2 = arr => arr.reduce((a, b) => a > b ? a : b);
```

### 4. Remove duplicates
```javascript
const unique = arr => [...new Set(arr)];
const unique2 = arr => arr.filter((v, i) => arr.indexOf(v) === i);
```

### 5. Count character occurrences
```javascript
function countChars(str) {
  return [...str].reduce((acc, ch) => {
    acc[ch] = (acc[ch] || 0) + 1;
    return acc;
  }, {});
}
```

### 6. FizzBuzz
```javascript
for (let i = 1; i <= 100; i++) {
  let out = "";
  if (i % 3 === 0) out += "Fizz";
  if (i % 5 === 0) out += "Buzz";
  console.log(out || i);
}
```

### 7. Flatten a nested array
```javascript
const flat = arr => arr.flat(Infinity);
// By hand:
function flatten(arr) {
  return arr.reduce((acc, v) =>
    acc.concat(Array.isArray(v) ? flatten(v) : v), []);
}
```

### 8. Factorial (recursion)
```javascript
const factorial = n => n <= 1 ? 1 : n * factorial(n - 1);
```

### 9. Fibonacci with memoisation (closures)
```javascript
const fib = (() => {
  const cache = {};
  return function f(n) {
    if (n <= 1) return n;
    if (cache[n]) return cache[n];
    return cache[n] = f(n - 1) + f(n - 2);
  };
})();
```

### 10. Debounce
```javascript
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

### 11. Throttle
```javascript
function throttle(fn, limit) {
  let waiting = false;
  return function (...args) {
    if (waiting) return;
    fn.apply(this, args);
    waiting = true;
    setTimeout(() => waiting = false, limit);
  };
}
```

### 12. Deep clone
```javascript
function deepClone(obj) {
  if (obj === null || typeof obj !== "object") return obj;
  if (Array.isArray(obj)) return obj.map(deepClone);
  return Object.fromEntries(
    Object.entries(obj).map(([k, v]) => [k, deepClone(v)])
  );
}
// Modern built-in:
const copy = structuredClone(obj);
```

### 13. Group an array of objects by a key
```javascript
function groupBy(arr, key) {
  return arr.reduce((acc, item) => {
    (acc[item[key]] ||= []).push(item);
    return acc;
  }, {});
}
```

### 14. Implement `bind` by hand
```javascript
Function.prototype.myBind = function (context, ...boundArgs) {
  const fn = this;
  return function (...callArgs) {
    return fn.apply(context, [...boundArgs, ...callArgs]);
  };
};
```

### 15. Promisify a callback function
```javascript
function promisify(fn) {
  return (...args) => new Promise((resolve, reject) => {
    fn(...args, (err, result) => err ? reject(err) : resolve(result));
  });
}
```

---
---

# SECTION E — Questions to Ask the Interviewer

When you're asked *"Do you have any questions for me?"*, having good questions is part of the
evaluation. **Thoughtful questions help leave a strong impression and help you decide whether
the opportunity is right for you.**

### 1. "Can you describe an average day in this role?"

**You'll learn:**
- What your day-to-day work might look like
- How the team collaborates
- Whether the role matches your expectations

### 2. "What does success look like in the first 90 days?"

**You'll discover:**
- The team's priorities
- How success is measured
- What your manager values most

### 3. "What are the biggest challenges someone in this role will face?"

**You'll discover:**
- The team's biggest priorities
- Challenges you may be expected to solve
- Where your skills can make an impact

### 4. "What information can I offer that can address any concerns about my fit for this role?"

**This gives you one last chance to:**
- Clarify your experience
- Address any concerns
- End the interview on a strong note

### 5. "What's the next step in the hiring process?"

**Before you leave, make sure you know:**
- What happens next
- When to expect an update
- When it's appropriate to follow up

---

## Source Files

| File | Contributed |
|---|---|
| `js fundamental questions.pdf` | Section A — the 20 core questions (Q1–Q20), verbatim explanations and code |
| `jobsearchquestions.pdf` | Section E — the 5 questions to ask an interviewer |
| All other JS files in this folder | Sections B, C and D — rapid-fire, puzzles and challenges, derived from the concepts covered across the notes |

Sections B, C and D were written to test the material in
**`JAVASCRIPT-COMPLETE-NOTES.md`**.

*No source files were modified.*
