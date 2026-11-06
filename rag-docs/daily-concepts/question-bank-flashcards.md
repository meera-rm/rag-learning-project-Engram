---
title: question-bank-flashcards
topic: interview-prep
source_type: my-notes
source_file: STUDYNOTEs/question-bank-flashcards.html
---

# Question Bank Flashcards

## A1 — Data types, conversion, truthiness

### Q: List every JavaScript primitive type. Which one is `typeof null`, and why is that wrong?

**A:** string, number, bigint, boolean, undefined, null, symbol. `typeof null` returns `"object"` — a long-standing language bug; null was originally represented internally as a pointer-like value, so its typeof tag was wrong from the start and can't be fixed without breaking the web.

### Q: Name Python's four sequence types and its two mapping/set types.

**A:** Sequence types: list, tuple, str, range. Mapping/set types: dict, set (and frozenset).

### Q: Java has 8 primitives. Name them with their sizes. Which are the non-primitive (reference) types?

**A:** byte(8), short(16), int(32), long(64), float(32), double(64), char(16), boolean(JVM-dependent, effectively 1 bit of info). Everything else — String, arrays, classes, interfaces, wrapper types — is a reference type.

### Q: `"5" + 3` in JS, Python, Java, TS — give all four results.

**A:** JS: `"53"` (string concatenation). Python: `TypeError` (can't add str + int). Java: `"53"` (string concatenation, same rule as JS). TS: `"53"` (compiles to the same JS behavior).

### Q: Why does `1 + "2" + 3` give `"123"` in Java but `1 + 2 + "3"` gives `"33"`?

**A:** Evaluation is left to right. Once a string appears, everything after becomes concatenation: `1 + "2"` → `"12"`, then `+ 3` → `"123"`. In the second case, `1 + 2` are both numbers and add first to `3`, then `3 + "3"` concatenates to `"33"`.

### Q: List JavaScript's 8 falsy values. What is Python's rule instead? What does Java have?

**A:** JS falsy: `false, 0, -0, 0n, "", null, undefined, NaN`. Python: only "empty-like" values are falsy — `0, 0.0, "", [], {}, (), set(), None, False` — no separate NaN rule. Java: no truthy/falsy coercion at all — only an actual `boolean` works in a condition.

### Q: `if (flag)` where `Boolean flag = null` — what happens in Java, and at which moment?

**A:** It throws a `NullPointerException` at the point Java tries to auto-unbox the `Boolean` object into the primitive `boolean` the `if` needs.

### Q: String → int in all four languages. Which throw, which return NaN, which need a check afterwards?

**A:** JS: `Number("abc")` returns `NaN` (no throw) — needs an `isNaN` check afterward. Python: `int("abc")` raises `ValueError`. Java: `Integer.parseInt("abc")` throws `NumberFormatException`. TS: same runtime behavior as JS — returns `NaN`, needs a check.

### Q: Float → int: does Python's `int()` round or truncate? Java's `(int)` cast? JS's options?

**A:** Python `int()` truncates toward zero. Java `(int)` cast truncates toward zero. JS: `Math.trunc()` truncates, `Math.floor()` rounds down, `Math.round()` rounds to nearest.

### Q: `??` vs `||` in TS/JS — give a value where they differ and say which is the bug.

**A:** With `x = 0`: `0 || "default"` → `"default"` (0 is falsy, so this is usually the bug — you wanted to keep 0). `0 ?? "default"` → `0` (only null/undefined trigger the fallback, so this is correct).

### Q: Why does `int("9.99")` raise, and what's the two-step fix?

**A:** `int()` can't parse a decimal point directly. Fix: convert to float first, then to int — `int(float("9.99"))`.

### Q: How do you deep-compare two objects in JS? Why doesn't `===` work?

**A:** Use `JSON.stringify(a) === JSON.stringify(b)` for simple cases, or a proper deep-equal utility (lodash `isEqual`, structuredClone comparison, etc). `===` compares object references, not contents — two structurally identical objects are still different references.

## A2 — Operators and conditionals

### Q: `==` vs `===` vs `.equals()` vs `is` — one sentence each, one language each.

**A:** `==` (JS): loose equality, coerces types before comparing. `===` (JS): strict equality, no coercion. `.equals()` (Java): logical/content equality, overridable per class. `is` (Python): identity equality — same object in memory.

### Q: `10 / 4` and `10 // 4` in Python, JS, Java. Which language has no `//` and what replaces it?

**A:** Python: `10/4 = 2.5` (true division), `10//4 = 2` (floor division). JS: `10/4 = 2.5`, no `//` operator — use `Math.floor(10/4)` or `Math.trunc(10/4)`. Java: `10/4 = 2` (int/int truncates automatically).

### Q: `-10 % 3` — Python says one thing, Java and JS say another. Which, and why?

**A:** Python: `-10 % 3 = 2` — the result takes the sign of the divisor (true modulo). Java/JS: `-10 % 3 = -1` — the result takes the sign of the dividend (remainder, not modulo).

### Q: Operator precedence, high → low. Where do `not`/`and`/`or` sit relative to comparisons?

**A:** Roughly: unary operators → arithmetic → comparisons → `not` → `and` → `or`. Comparisons bind tighter than the boolean logical operators, so `a < b and c < d` evaluates both comparisons first, then combines with `and`.

### Q: Python has no `switch`. Name the three replacements.

**A:** An `if/elif/elif/...` chain, a dict-of-functions dispatch table, or `match`/`case` structural pattern matching (Python 3.10+).

### Q: What goes wrong in a JS `switch` with no `break`? When is that deliberate?

**A:** Execution "falls through" into the next case's body regardless of whether its condition matched, continuing until a `break` or the switch ends. Deliberate when several case labels should share identical handling (grouped fallthrough).

### Q: Rest vs spread in JS — same `...`, opposite jobs. One example each.

**A:** Rest gathers multiple values into one array/object: `function f(...args) {}`. Spread expands an array/object into individual elements: `f(...arr)` or `[...arr1, ...arr2]`.

### Q: Java's `strictfp`, `volatile`, `transient` — one line each.

**A:** `strictfp`: forces consistent IEEE 754 floating-point results across all platforms. `volatile`: guarantees a field's writes are immediately visible to other threads (no thread-local caching). `transient`: excludes a field from default object serialization. Note: since Java 17 all floating-point math is strict by default, so the keyword no longer changes anything.

## A3 — Loops

### Q: Loop over array **values** in JS, Python, Java. Which JS loop gives you indexes instead, and what's the trap?

**A:** JS: `for (const x of arr)` or `arr.forEach(x => ...)`. Python: `for x in list`. Java: enhanced for, `for (Type x : arr)`. `for...in` gives you indexes (as strings) — the trap is it also walks enumerable inherited/prototype properties, not just the array's own indexes.

### Q: `range(start, stop, step)` — is stop included? What's the JS and Java equivalent?

**A:** `stop` is excluded (exclusive upper bound). JS/Java equivalent: a classic counted loop, `for (let i = start; i < stop; i += step) {}`.

### Q: What is Python's `pass`, and how does it differ from `continue`?

**A:** `pass` is a no-op placeholder that does nothing but keeps a block syntactically valid (e.g. an empty function body). `continue` actively skips the rest of the current loop iteration and jumps to the next one.

### Q: Python has `for…else`. When does the `else` run?

**A:** The `else` block runs only if the loop completes normally, without ever hitting a `break`.

### Q: JS labelled loops — write one that breaks out of two levels.

**A:** `outer: for (let i=0;i<n;i++){ for (let j=0;j<m;j++){ if (cond) break outer; } }`

## A4 — Functions

### Q: Name the 6 JavaScript function forms.

**A:** Your notes (§15) list six: 1. function declaration, 2. function expression, 3. arrow function, 4. anonymous function (no name, usually passed straight in), 5. IIFE (immediately invoked function expression: defined and called at once), 6. callback function (a function passed to another function to be called later). A declaration is hoisted, so you can call it before its line. An expression or an arrow function is not.

### Q: Write a Python signature using positional, keyword, default, `*args` and `**kwargs` in the correct order.

**A:** `def f(a, b, c=1, *args, d, **kwargs):` — positional, then defaulted, then `*args`, then keyword-only, then `**kwargs`.

### Q: Java varargs: write the signature. Two rules about where it can sit. Is it `null` or empty when called with nothing?

**A:** `void printAll(String... items) {}`. Rules: varargs must be the last parameter, and a method can have only one varargs parameter. Called with nothing, `items` is an empty array (length 0), not `null`.

### Q: `add(int a, int b)` and `add(int... nums)` both exist. Which does `add(1,2)` call?

**A:** The exact-match `add(int, int)` overload — Java always prefers the most specific applicable signature over a varargs match.

### Q: Java has overloading; JS, Python and TS don't. What does each use instead?

**A:** Default parameters, rest parameters (`...args`), or runtime type/arity checks inside a single function body. TS supports overload *signatures* for documentation/type-checking, but still only one actual implementation.

### Q: TS optional param `level?: "warn" | "error"` — what is its actual type inside the function?

**A:** `"warn" | "error" | undefined` — the `?` adds `undefined` to the declared union.

### Q: `typeof (() => {})` returns what? Why can you store a function in a `const` and call it?

**A:** Returns `"function"`. Functions are first-class values in JS, so they can be assigned to variables (including `const`) like any other value, then invoked with `()`.

### Q: Python: mutating a list argument vs rebinding the parameter name. Which is visible to the caller, and why?

**A:** Mutating (`list.append(x)`) is visible to the caller because both names reference the same underlying object. Rebinding (`x = []`) only changes what the local variable points to — the caller's original reference is untouched.

### Q: What is the mutable-default-argument trap in Python, and what's the fix?

**A:** `def f(x=[])` creates the default list *once*, at function definition time, and it's shared/mutated across every call that doesn't pass its own `x`. Fix: default to `None` and create the list fresh inside the function body.

## A5 — Scope, hoisting, closures

### Q: `var` vs `let`/`const` scope, in one sentence each.

**A:** `var` is function-scoped (or global if declared outside any function). `let`/`const` are block-scoped, confined to the nearest enclosing `{}`.

### Q: What is hoisted for `var`, for function declarations, for `let`?

**A:** `var`: the declaration is hoisted and pre-initialized to `undefined`. Function declarations: fully hoisted, both name and body. `let`: hoisted but left uninitialized — inaccessible until its line executes (temporal dead zone).

### Q: Define the temporal dead zone. What error does touching a TDZ variable throw?

**A:** The TDZ is the span from the start of a block to the `let`/`const` declaration's line, during which the variable exists but can't be read or written. Touching it throws a `ReferenceError`.

### Q: Define a closure in one sentence. Write the smallest counter factory.

**A:** A closure is a function that retains access to the variables of its defining scope even after that scope has finished executing. `function makeCounter(){ let c = 0; return () => ++c; }`

### Q: The `var`-in-a-loop bug: write it, explain why all three print the same number, give both fixes.

**A:** `for (var i=0;i<3;i++){ setTimeout(()=>console.log(i)); }` prints `3,3,3` because `var i` is one shared binding across all iterations, and by the time the callbacks run the loop has already finished with `i=3`. Fix 1: use `let i` (creates a fresh binding per iteration). Fix 2: wrap the body in an IIFE that captures `i`'s current value as a parameter.

### Q: Python's LEGB — expand it. Which keyword reaches the enclosing scope, which reaches module scope?

**A:** Local, Enclosing, Global, Built-in — the order Python searches for a name. `nonlocal` reaches the nearest enclosing function scope; `global` reaches module scope.

### Q: Describe the two phases of an execution context. Where does hoisting happen?

**A:** Creation phase: scope and `this` are set up, memory is allocated, `var`s are set to `undefined`, function declarations are fully hoisted. Execution phase: code runs line by line, assigning real values. Hoisting happens during the creation phase.

### Q: Why does Java only capture *effectively final* variables in a lambda?

**A:** Because the lambda may execute later or on another thread, it needs a stable snapshot of the variable rather than a live mutable reference — restricting captures to values that never change after initialization avoids race conditions and confusing semantics.

### Q: What is an IIFE, and what problem did it solve before `let` existed?

**A:** An Immediately Invoked Function Expression — a function defined and called in the same expression: `(function(){ ... })();`. Before `let`, it was used to create a fresh private scope per loop iteration, fixing the classic `var`-in-a-loop closure bug.

### Q: What does `"use strict"` change? Name three things.

**A:** Your notes (§23) list: declaring a variable without `let`, `const` or `var` throws an error; reserved keywords (like `private`, `interface`) can't be used as variable names; accidental global variables are harder to create; you can't delete important objects or properties; duplicate parameter names are not allowed; and in a plain function call `this` is `undefined` instead of `window`. Enable it with `"use strict";` at the very top of a file or inside a function. ES6 modules and classes are always strict.

## A6 — Java arrays and strings

### Q: Declare and initialise an `int[]` two ways. Can its length change?

**A:** `int[] a = new int[5];` and `int[] a = {1, 2, 3};` (or `new int[]{1,2,3}`). No — once created, an array's length is fixed.

### Q: `Arrays.sort` / `fill` / `equals` / `toString` — one line each. What is `deepEquals` for?

**A:** `sort`: sorts the array in place. `fill`: fills every slot with a given value. `equals`: compares two arrays element-by-element for content equality. `toString`: returns a readable string like `"[1, 2, 3]"`. `deepEquals` compares nested arrays (arrays of arrays) recursively.

### Q: Why is `arr1.equals(arr2)` false when `Arrays.equals(arr1, arr2)` is true?

**A:** Arrays don't override `equals()`, so `arr1.equals(arr2)` falls back to `Object`'s default reference equality (effectively `==`). `Arrays.equals` explicitly compares contents element by element.

### Q: Array vs ArrayList: what are the differences? (your notes list eight)

**A:** Array: fixed size that can't change after creation, stores primitives and objects, accessed by index, sorted with `Arrays.sort()`, can be multidimensional, can't hold nulls for primitives, generally faster but less flexible. ArrayList: resizable, stores only objects, accessed through methods (`get()`, `add()`, `remove()`), efficient insertion and deletion, sorted with `Collections.sort()`, single-dimensional only, can store null values, slower but more flexible.

### Q: Why is `String` immutable? Give the three reasons (hashing, interning, threads).

**A:** (1) Safe to cache its hashcode and use as a HashMap key since it can never change underneath. (2) Enables the string pool/interning — identical literals can safely share one object. (3) Thread safety — a shared String needs no synchronization since it can't be mutated.

### Q: `StringBuilder` — append, insert, replace, delete, reverse. Why is `toString()` needed at the end?

**A:** `append` adds to the end, `insert` adds at a position, `replace` overwrites a range, `delete` removes a range, `reverse` flips the whole sequence. `toString()` is needed because `StringBuilder` is a separate mutable buffer class, not itself a `String`.

### Q: What is the growth rule when a `StringBuilder`'s buffer fills?

**A:** It typically grows to roughly `oldCapacity * 2 + 2`, allocating a new backing array and copying the existing characters over.

### Q: `StringBuilder` vs `StringBuffer` — the one-word difference. Why is it rarely needed?

**A:** Synchronization — `StringBuffer` is the thread-safe twin of `StringBuilder`. Rarely needed because most `StringBuilder` use is confined to a single method/thread, where the synchronization overhead buys nothing.

### Q: Does synchronising each method make a *sequence* of calls atomic?

**A:** No. Synchronizing individual methods only protects each call in isolation — another thread can still interleave between two calls on the same object, so compound operations still need external synchronization (or a lock held across the whole sequence).

### Q: Big-O: `a + b`, n appends with `+`, n appends with `StringBuilder`, `substring(i,j)`, `charAt(i)`.

**A:** `a + b` (two values): O(1). n appends with `+`: O(n²) (each `+=` allocates and copies a new string). n appends with `StringBuilder`: O(n) amortized. `substring(i,j)`: O(j−i) in modern Java (copies a new char array). `charAt(i)`: O(1).

## A7 — TypeScript

### Q: What does "annotate" mean? Where does an annotation go for a variable, a parameter, a return type?

**A:** Annotating means explicitly writing out a type instead of relying on inference. Variable: `let x: number`. Parameter: `function f(x: number)`. Return type: `function f(): number`.

### Q: Give one case where inference beats an annotation, and one where the annotation is required.

**A:** Inference wins for a simple literal initializer: `let x = 5` (TS already knows it's `number`). Annotation is required when there's no initializer to infer from, e.g. a bare function parameter: `function f(x: number)`.

### Q: `any` vs `unknown` vs `never` — one example each, and what each one *permits*.

**A:** `any`: opts out of type checking entirely — `let x: any = 5; x.foo()` compiles even though unsafe. `unknown`: the safe top type — `let x: unknown = 5;` must be narrowed (e.g. `typeof` check) before use. `never`: values that never occur — the return type of a function that always throws, or an exhausted union case.

### Q: Why is `string | unknown` just `unknown`?

**A:** `unknown` already represents "any possible type," so unioning it with anything — even a narrower type like `string` — collapses back to `unknown`; it absorbs everything.

### Q: How is `never` used for exhaustiveness checking in a `switch`?

**A:** After handling every member of a union in a `switch`, the value in the `default` branch should have narrowed to `never`. Assigning it to a variable typed `never` makes the compiler error if a new union member is ever added and left unhandled.

### Q: `interface` vs `type` alias — when does each win?

**A:** `interface` wins for object shapes meant to be extended or declaration-merged — good for public API contracts. `type` wins for everything an interface can't express: unions, intersections, primitives, tuples, mapped types.

### Q: What do `strict`, `noUncheckedIndexedAccess`, `noUnusedLocals` and `resolveJsonModule` each turn on?

**A:** `strict`: the full bundle of strict type-checking flags (`noImplicitAny`, `strictNullChecks`, etc). `noUncheckedIndexedAccess`: adds `undefined` to the type of any array/object index access. `noUnusedLocals`: errors on declared-but-unused local variables. `resolveJsonModule`: allows importing `.json` files with an inferred type.

### Q: Why must a file containing JSX be `.tsx`?

**A:** The compiler only enables JSX-markup parsing in `.tsx` files; in a plain `.ts` file, `<` is parsed as a comparison operator or generic-type syntax instead of markup.

### Q: With `noUncheckedIndexedAccess` on, what is the type of `arr[0]`, and what are the two ways to handle it?

**A:** `T | undefined`. Handle it either with an explicit guard/check for `undefined`, or with the non-null assertion operator `arr[0]!` when you're certain the element exists.

## A8 — Python strings and I/O

### Q: What type does `input()` always return? Give the two ways that bites you.

**A:** Always a `str`. Bites you when: (1) you forget to convert before doing arithmetic, causing a `TypeError` or accidental string concatenation; (2) there's leftover whitespace/newline you didn't strip before comparing or converting.

### Q: Convert input to int, to float. Which inputs make `int()` raise?

**A:** `int(input())`, `float(input())`. `int()` raises `ValueError` on anything non-integer, including strings with a decimal point like `"9.99"` or non-numeric text.

### Q: Read two numbers from one line, into two ints, in one expression.

**A:** `a, b = map(int, input().split())`

### Q: Write the same formatted line three ways: f-string, `.format()`, `%`.

**A:** `f"{price:.2f} {name}"` · `"{:.2f} {}".format(price, name)` · `"%.2f %s" % (price, name)`

### Q: What does `:>10,.2f` mean, piece by piece?

**A:** `>`: right-align. `10`: field width 10. `,`: use a thousands separator. `.2`: 2 decimal places. `f`: fixed-point notation.

### Q: When is `.format()` genuinely better than an f-string?

**A:** When the same template string is reused across multiple calls with different args passed in dynamically, or when the format string itself comes from a variable/config file — f-strings must be literal source at the call site, `.format()` doesn't.

### Q: Why does `logging.info("user %s", name)` beat an f-string in a log call?

**A:** It defers the actual string interpolation until (and unless) the log record is emitted — if that log level is disabled, the formatting work never happens. An f-string always formats immediately regardless of whether the result is ever used.

### Q: `s[1:4]` — is stop included? What does `s[::-1]` do and why?

**A:** Stop is excluded — `s[1:4]` gives indices 1, 2, 3. `s[::-1]` reverses the string by taking the full range with a step of −1.

### Q: Why does `s[99]` raise but `s[99:200]` not?

**A:** A single out-of-range index has no valid value to return, so it raises `IndexError`. A slice clamps its bounds silently and just returns whatever fits — an empty string if nothing is in range — instead of erroring.

### Q: `s[0] = 'X'` — what happens in Python, JS, Java? Which one fails silently?

**A:** Python: raises `TypeError` (strings don't support item assignment). JS: silently does nothing — strings are immutable but no error is thrown, so this is the one that fails silently. Java: strings are also immutable, and index-assignment syntax on a String doesn't even exist — it's a compile error, not a runtime failure.

### Q: `s += "d"` vs `a += [3]` — why does one leave the original untouched and the other not?

**A:** `s += "d"` creates a brand-new string and rebinds `s` to it (strings are immutable), so any other reference to the old string is unaffected. `a += [3]` on a list calls `__iadd__`, which mutates the list in place — any other reference to that same list sees the change.

### Q: `strip`, `split`, `join`, `replace`, `find` — one line each. Which object is `join` called on?

**A:** `strip()`: removes leading/trailing whitespace (or given chars). `split()`: breaks a string into a list on a delimiter. `join()`: concatenates an iterable of strings — called on the *separator* string, e.g. `",".join(parts)`. `replace()`: substitutes occurrences of a substring. `find()`: returns the index of the first match, or −1.

### Q: `strip("xy")` — does it remove the substring `"xy"` or the characters `x` and `y`?

**A:** It removes any of the individual characters `x` or `y` from both ends — not the two-character substring `"xy"` as a unit.

### Q: `find` vs `index` on a missing value. When do you pick each?

**A:** `find()` returns −1 on no match — good when absence is an expected case handled numerically. `index()` raises `ValueError` on no match — good when absence should be treated as an error.

### Q: Why is `if s.find("h"):` a bug?

**A:** Because `find()` returns `0` when the match is at position 0, and `0` is falsy — the condition incorrectly treats a match at the very start of the string as "not found."

### Q: Why is string concatenation in a loop O(n²)? Trace the character copies for 4 pieces.

**A:** Each `+=` allocates a brand-new string and copies every previous character plus the new piece. For 4 pieces the copies are roughly 1+2+3+4 characters — over n pieces the total grows like n²/2, i.e. O(n²).

### Q: Give the O(n) fix in Python, JS and Java.

**A:** Python: `"".join(list_of_pieces)`. JS: push pieces into an array and `arr.join("")`. Java: `StringBuilder`, appending each piece then calling `toString()` once at the end.

## A9 — SQL

### Q: Data vs database vs DBMS vs RDBMS. SQL vs MySQL.

**A:** Data: raw facts. Database: an organized collection of data. DBMS: software that manages databases (storage, queries, security). RDBMS: a DBMS built on the relational (table-based) model with constraints like keys. SQL is the language used to talk to a relational database; MySQL is one specific RDBMS product that implements SQL.

### Q: The five command families — name them and two commands each.

**A:** DDL (structure): `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. DML (data): `INSERT`, `UPDATE`, `DELETE`. DQL (retrieve): `SELECT`. DCL (access): `GRANT`, `REVOKE`. TCL (transactions): `COMMIT`, `ROLLBACK`, `SAVEPOINT`. `SELECT` is sometimes grouped under DML, so say DQL and mention it.

### Q: The four steps a query goes through.

**A:** Your notes (§3) show the query going through the query language processor (the parser breaks it into tokens and checks the syntax, then the optimizer picks the best way to run it), then the DBMS engine (the file manager finds the data on disk, the transaction manager keeps the operation safe and consistent), then the physical database (the actual bytes on disk). You say what you want and the optimizer decides how, which is why SQL is called declarative.

### Q: `INT` vs `DECIMAL` vs `FLOAT` — which for money, and why not the other two?

**A:** `DECIMAL` — it's an exact, fixed-point representation with no rounding error. `INT` can't hold fractional cents. `FLOAT` is binary floating point and introduces rounding error that's unacceptable for currency.

### Q: `CHAR` vs `VARCHAR`.

**A:** `CHAR` is fixed-length, padded with spaces up to its declared size. `VARCHAR` is variable-length, storing only the characters used (plus a small length prefix).

### Q: Write INSERT for one row and for several rows.

**A:** `INSERT INTO t (a,b) VALUES (1,2);` and `INSERT INTO t (a,b) VALUES (1,2),(3,4),(5,6);`

### Q: Why avoid `SELECT *` in production code? Three reasons.

**A:** Pulls unnecessary columns, wasting bandwidth/memory. Breaks silently if the schema changes (columns reordered or added). Prevents certain index-only query optimizations that need an explicit column list.

### Q: What happens to UPDATE or DELETE with no WHERE? What's the habit that prevents it?

**A:** It applies to every row in the table. Habit: write and run the equivalent `SELECT` with the same `WHERE` clause first, to confirm the exact target rows, before switching the statement to `UPDATE`/`DELETE`.

### Q: What does NULL mean, and how does it differ from `0` and `''`?

**A:** NULL means "unknown or absent value" — it's not a real value at all, unlike `0` (a real number) and `''` (a real, empty-but-present string).

### Q: Why does `= NULL` return no rows? What do you use instead?

**A:** Because under three-valued logic, `NULL` is never equal (or unequal) to anything, including itself — any `= NULL` comparison evaluates to unknown, not true. Use `IS NULL` instead.

### Q: `COALESCE` vs `IFNULL` vs `NVL` vs `ISNULL` — which is standard, which belongs to which vendor?

**A:** `COALESCE` is the ANSI SQL standard, works across vendors, and accepts multiple arguments. `IFNULL` is MySQL-specific, `NVL` is Oracle-specific, `ISNULL` is SQL Server-specific — all are vendor two-argument equivalents.

### Q: `NULLIF` — write the divide-by-zero guard.

**A:** `total / NULLIF(headcount, 0)` — returns NULL instead of erroring when `headcount` is 0.

### Q: `COUNT(*)` vs `COUNT(column)` — on a table of 6 rows with 1 NULL salary, give both numbers.

**A:** `COUNT(*)` = 6 (counts every row regardless of NULLs). `COUNT(salary)` = 5 (skips the one NULL salary).

### Q: Do `SUM`, `AVG`, `MAX` skip NULLs? What does `AVG` do about the denominator?

**A:** Yes, all three skip NULLs. `AVG` divides by the count of non-NULL values only, not the total row count.

### Q: `!=` vs `<>` — any difference?

**A:** No — they're equivalent in standard SQL. `<>` is the ANSI-standard spelling; `!=` is a widely supported alias most engines also accept.

## A10 — DSA — 11→16 Sep

### Q: Group Anagrams — what is the dict key, and what are the two choices for it?

**A:** The dict key must be some canonical form shared by all anagrams of a word: either the sorted string/tuple of its characters, or a fixed-length character-count signature. Sorted string is simpler; count-signature is faster for long strings (avoids an O(k log k) sort per word).

### Q: Top K Frequent — why is bucket sort O(n) where a heap is O(n log k)?

**A:** Bucket sort creates buckets indexed 0..n by frequency and places each element directly, so building and reading buckets is O(n) total with no comparisons. A heap of size k needs O(log k) per push/pop, done up to n times, giving O(n log k).

### Q: Product of Array Except Self — why is division banned, and what replaces it?

**A:** Division breaks when the array contains a zero (or handles multiple zeros awkwardly). It's replaced by two passes: running prefix products from the left, then multiplying in running suffix products from the right.

### Q: Two Sum — why must you store the complement *after* the check, not before?

**A:** If you insert the current number into the map before checking, a number could incorrectly "pair with itself" — e.g. if `target` is exactly double the current number, you'd match it against its own not-yet-processed index.

### Q: Valid Anagram — the single-pass increment/decrement form. What must you check first?

**A:** Increment a count for each character in the first string, decrement for each character in the second, in one combined pass; at the end all counts should be zero. You must first check the two strings are the same length — otherwise the counts can't reliably confirm an anagram.

## A11 — JS strings, template literals, arrays

### Q: Why is a string immutable in JS — what does `s[0] = "X"` actually do?

**A:** Strings are a primitive type in JS with no writable index access; `s[0] = "X"` is simply a silent no-op — it neither throws nor changes `s`, since primitives can't be mutated.

### Q: Template literal — write one that spans two lines and interpolates an expression, not just a variable.

**A:** `const html = @@BT@@Hello ${name},
Your total is ${price * qty}@@BT@@;` — it spans two lines directly in the source, and the second interpolation runs an actual expression (a multiplication), not just a bare variable.

### Q: What is a tagged template, and name one built-in that uses the pattern.

**A:** A template literal preceded by a function name — the function receives the literal string pieces and the interpolated values separately, so it can process or escape them before combining. `styled-components`'s `css\`\`` is a well-known example of the pattern (built on the same mechanism as the built-in `String.raw`).

### Q: Three ways to create an array. What does `Array.from({ length: 5 }, (_, i) => i)` produce?

**A:** Array literal `[]`, `new Array(n)`, or `Array.from(...)`. `Array.from({ length: 5 }, (_, i) => i)` produces `[0, 1, 2, 3, 4]`.

### Q: Can you set `arr.length` directly? What happens if you shrink it?

**A:** Yes, `arr.length` can be assigned directly. Shrinking it truncates the array, permanently deleting every element beyond the new length.

### Q: What is an array "hole" — what does `[1, , 3]` actually contain, and how does it differ from `[1, undefined, 3]`?

**A:** A hole is an empty slot with no value stored at all — not even `undefined`. Methods like `forEach`/`map` skip holes entirely. `[1, undefined, 3]` instead has an actual `undefined` value at index 1, which IS visited by those methods.

## A12 — JS array methods ⭐

### Q: List the 9 mutating array methods and the 14 non-mutating ones from memory.

**A:** Mutating (9): `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`, `fill`, `copyWithin`. Non-mutating (14, they return a new value): `slice`, `concat`, `join`, `toString`, `map`, `filter`, `reduce`, `find`, `findIndex`, `includes`, `indexOf`, `some`, `every`, `entries`. Your notes (§27) count 29 core array methods in all, and call mixing these up the #1 array bug.

### Q: `sort()` with no comparator — sorts by what, and what's the classic numeric bug?

**A:** Sorts by converting elements to strings and comparing UTF-16 code units. Numeric bug: `[10, 2, 1].sort()` gives `[1, 10, 2]` instead of numeric order. Fix: pass a comparator, `(a,b) => a - b`.

### Q: Write a `sort` call that mutates an array you didn't mean to touch, then the `[...arr].sort()` fix.

**A:** `arr.sort((a,b) => a-b)` mutates `arr` in place, silently changing any other reference to it too. Fix: `[...arr].sort((a,b) => a-b)` sorts a shallow copy, leaving the original untouched.

### Q: `map` vs `forEach` — what does each return, and which one do you chain?

**A:** `map` returns a new array of the same length, built from the callback's return values — this is the one you chain (e.g. `.map(...).filter(...)`). `forEach` returns `undefined` — it's for side effects only and can't be chained.

### Q: `reduce` — write the signature. What happens if you omit the initial value on an empty array?

**A:** `arr.reduce((accumulator, current) => ..., initialValue)`. Omitting the initial value on an empty array throws `TypeError: Reduce of empty array with no initial value`.

### Q: `find` vs `filter` — what does each return when nothing matches?

**A:** `find` returns `undefined` when nothing matches. `filter` always returns an array — an empty array `[]` when nothing matches, never `undefined`.

### Q: `some` vs `every` — what do each return on an empty array, and why?

**A:** `some` returns `false` on an empty array — vacuously, nothing satisfies the condition since there's nothing to check. `every` returns `true` on an empty array — vacuously, all (zero) elements satisfy it, since none exist to violate it.

### Q: `splice` vs `slice` — one mutates, one doesn't. Write one call of each that returns the same elements.

**A:** `arr.splice(1, 2)` removes and returns 2 elements starting at index 1, mutating `arr` in place. `arr.slice(1, 3)` returns the same two elements as a brand-new array, leaving `arr` untouched.

### Q: Write one chained `filter` → `map` → `reduce` over an array of product objects (e.g. total price of in-stock items).

**A:** `const total = products.filter(p => p.inStock).map(p => p.price).reduce((sum, price) => sum + price, 0);`

## A13 — React — setup, JSX

### Q: What is React, in one line? What problem does the virtual DOM solve?

**A:** React is a JS library for building UI out of composable, reusable components. The virtual DOM is an in-memory representation of the UI that React diffs against the previous version to compute the minimal set of real-DOM changes, avoiding slow full-page re-renders.

### Q: What is a component? What does "declarative" mean, contrasted with "imperative"?

**A:** A component is a reusable, self-contained function (or class) that returns UI markup for a given input. Declarative means describing *what* the UI should look like for a given state; imperative means writing the step-by-step instructions for *how* to mutate the DOM yourself.

### Q: What does "one-way data flow" mean in React?

**A:** Data flows in a single direction — from parent to child, via props. A child component never directly mutates its parent's state; it can only request a change by calling a callback function the parent passed down.

### Q: Name one concrete difference between React and Angular or Vue.

**A:** React is just a rendering library using a virtual DOM and JSX embedded in plain JS, with routing/state management left to separate libraries. Angular is a full opinionated framework bundling two-way data binding, dependency injection, and routing out of the box.

### Q: Give three ways JSX is not HTML.

**A:** JSX compiles to nested JS function calls rather than literal markup; it uses camelCase attribute names (`onClick`, not `onclick`); and only expressions (not statements like `if`) are allowed inside `{}`.

### Q: Why `className` instead of `class`, and `htmlFor` instead of `for`?

**A:** `class` and `for` are both reserved words in JavaScript (`class` for class declarations, `for` for loops), so JSX uses `className` and `htmlFor` instead to avoid colliding with the language's own syntax.

### Q: What's allowed inside `{}` in JSX? What is *not* allowed (e.g. why doesn't a bare `if` work inline)?

**A:** Any valid JS expression is allowed — variables, function calls, ternaries, arithmetic, arrow functions. Statements are not allowed, because `{}` expects a value to render, and `if`/`for`/`while` don't evaluate to a value — use a ternary or `&&` short-circuit instead.

### Q: Why must a JSX expression have one root element? What are the two ways around it?

**A:** JSX compiles down to a single nested function-call tree, so `return` can only hand back one top-level node. Wrap siblings in a container `<div>`, or use an empty fragment `<>...</>` to group them without adding an extra DOM element.

### Q: How do you self-close a tag with no children in JSX, and why does it matter?

**A:** Add a trailing slash, e.g. `<img />` or `<br />`. It matters because JSX is stricter than HTML — every non-container element must be explicitly closed or self-closed, or the compiler throws a syntax error.

## A14 — DSA — Valid Palindrome

### Q: What's the two-pointer approach, in one line?

**A:** Move a left pointer from the start and a right pointer from the end inward, skipping non-alphanumeric characters, comparing lowercased characters as you go until the pointers cross or a mismatch is found.

### Q: Why is this the O(1)-space version — what would building a cleaned string first cost?

**A:** It scans the original string in place using only two index variables — no extra storage proportional to input size. Building a cleaned string first (filtering + lowercasing into a new string) would cost O(n) extra space.

### Q: Which function decides "alphanumeric," and how do you normalize case before comparing?

**A:** `isalnum()` (Python) or an equivalent regex/char-code check decides alphanumeric. Case is normalized with `.lower()` (or a case-insensitive character comparison) before comparing the two characters.

### Q: What are the loop's two advance conditions besides the pointers meeting?

**A:** Advance the left pointer forward while its current character isn't alphanumeric, and advance the right pointer backward while its current character isn't alphanumeric — in addition to moving both pointers inward together after a successful character match.

## B17 — Array methods drill (24 Sep)

### Q: Given `products: Product[]` with `{ name, price, inStock, qty }` — write `filter` → `map` → `reduce` for the total price of all in-stock items.

**A:** `const total = products
  .filter(p => p.inStock)
  .map(p => p.price)
  .reduce((sum, price) => sum + price, 0);`

### Q: Sort a copy of `products` by price descending without mutating the original. How do you prove the original is untouched?

**A:** `const sorted = [...products].sort((a, b) => b.price - a.price);` — spread makes a shallow copy first, so `sort` mutates the copy, not `products`. Prove it by logging `products[0]` before and after: it's unchanged, only `sorted[0]` reflects the new order.

### Q: Find the first out-of-stock item with `find`, and its index with `findIndex`. How do you handle "not found" for both?

**A:** `const firstOut = products.find(p => !p.inStock);   // undefined if none
const idx = products.findIndex(p => !p.inStock);  // -1 if none` — guard with `if (!firstOut) {...}` and `if (idx === -1) {...}` respectively; never assume a match exists.

### Q: Check with `some`/`every`: is anything out of stock? is everything in stock?

**A:** `const anyOutOfStock = products.some(p => !p.inStock);
const allInStock = products.every(p => p.inStock);`

### Q: Reduce the array into a `{ name: price }` lookup object.

**A:** `const byName = products.reduce((acc, p) => {
  acc[p.name] = p.price;
  return acc;
}, {});`

## B18 — Valid Palindrome (24 Sep)

### Q: Write it in Python — two-pointer, O(1) space, using `isalnum()` and `.lower()`.

**A:** `def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l].lower() != s[r].lower(): return False
        l += 1; r -= 1
    return True`

### Q: Write it in JavaScript — two-pointer, O(1) space, regex or char-code check.

**A:** `function isPalindrome(s) {
  const alnum = c => /[a-z0-9]/i.test(c);
  let l = 0, r = s.length - 1;
  while (l < r) {
    while (l < r && !alnum(s[l])) l++;
    while (l < r && !alnum(s[r])) r--;
    if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    l++; r--;
  }
  return true;
}`

## B19 — Plain JS → JSX substitution (24 Sep)

### Q: Take a plain-JS object → HTML-string-via-template-literal drill and rewrite it as a JSX-returning function, same data and visual output. What specifically changes in the substitution?

**A:** Plain JS: `const html = @@BT@@<div class="card">${p.name} — $${p.price}</div>@@BT@@;`
JSX: `function Card({ p }) { return <div className="card">{p.name} — ${p.price}</div>; }`
What changes: `${}` string interpolation becomes `{}` JSX expressions; the string attribute `class` becomes the JSX prop `className`; and every tag needs a real closing tag (or self-close) since JSX is parsed as markup, not just text.

## A15 — JS Set & Map (2 Oct)

### Q: What does a `Set` guarantee that an array doesn't, and how do you dedupe an array with it?

**A:** Every value is unique. Dedupe with `[...new Set(arr)]` (or `Array.from(new Set(arr))`). The first occurrence wins and order is preserved.

### Q: Name the core `Set` methods. Is `size` a property or a method?

**A:** `add`, `delete`, `has`, `clear`. `size` is a property: `set.size` works, `set.size()` throws a `TypeError`.

### Q: How does a `Set` decide two values are the same? What about `NaN` and objects?

**A:** It uses SameValueZero. `NaN` equals `NaN` (unlike `===`) and `+0` equals `-0`, so a Set keeps one `NaN`. Objects compare by reference, so two separate `{a: 1}` literals are both kept.

### Q: `Map` vs plain object — key types, ordering, size.

**A:** Map keys can be any type (objects, functions, `NaN`); a plain object turns keys into strings or symbols. Map iterates in insertion order for every key, while an object lists integer-like keys first. Map has `.size`; an object needs `Object.keys(o).length`. A plain object also inherits keys such as `toString`, so `"toString" in {}` is `true`.

### Q: Count word frequency with a `Map`.

**A:** `const freq = new Map();
for (const w of words) freq.set(w, (freq.get(w) ?? 0) + 1);`
`get` returns `undefined` for a missing key, so `?? 0` supplies the starting count.

### Q: What order do `Set` and `Map` iterate in, and what are the ways to loop over a `Map`?

**A:** Insertion order. Loop with `for (const [k, v] of map)`, `map.entries()`, `map.keys()`, `map.values()`, or `map.forEach((value, key) => ...)`. Note `forEach` passes the value first, then the key.

### Q: Which Python types correspond to JS `Set` and `Map`? How do you dedupe a list and keep the original order?

**A:** `set` and `dict`. `list(set(x))` loses the order because sets are unordered. `list(dict.fromkeys(x))` keeps first-seen order, since dicts preserve insertion order (Python 3.7+).

### Q: Why is `has` on a Set O(1) on average while `includes` on an array is O(n)? Where did that matter in Two Sum and Group Anagrams?

**A:** A Set hashes the value and jumps straight to it; `includes` scans every element. In Two Sum, looking up each complement in a Map or Set makes the whole pass O(n) instead of O(n²). In Group Anagrams, a Map keyed by the sorted-letters or letter-count signature collects each group in one pass.

## A16 — JS JSON (2 Oct)

### Q: What do `JSON.stringify` and `JSON.parse` do, and what are the 2nd and 3rd arguments of `stringify` for?

**A:** `stringify` turns a value into a JSON string; `parse` turns a JSON string back into a value. In `JSON.stringify(obj, null, 2)` the 2nd argument is a replacer (a function, or an array of allowed keys) and the 3rd is the indent (a number of spaces or a string) for pretty-printing.

### Q: Which values does `JSON.stringify` drop or change?

**A:** Object properties holding `undefined`, functions or symbols are omitted; in arrays they become `null`. `NaN` and `Infinity` become `null`. A `Date` becomes an ISO string and parses back as a string, not a Date. `Map` and `Set` become `{}`. `BigInt` and circular references throw a `TypeError`.

### Q: What is the `JSON.parse(JSON.stringify(obj))` deep-copy trick, and where does it fail?

**A:** It serializes then re-parses, so nested objects are fully copied. It loses functions, `undefined`, `Date` objects (they become strings), `Map`/`Set` and class prototypes, and it throws on circular references and `BigInt`. `structuredClone(obj)` keeps `Date`, `Map`, `Set` and circular references, but throws on functions.

### Q: Why does `JSON.parse("{'a': 1}")` throw? What are JSON's syntax rules?

**A:** JSON requires double-quoted strings and keys. No single quotes, no trailing commas, no comments, no `undefined`, no unquoted keys. `{"a": 1}` parses; `{'a': 1}` does not.

### Q: Python equivalents: `json.dumps` vs `json.dump`, `loads` vs `load`. How do `None`, `True` and tuples map?

**A:** `dumps`/`loads` work on strings (the `s` is for string); `dump`/`load` work on file objects. `None` → `null`, `True` → `true`, tuples → arrays, and `loads` returns a `dict` or `list`. Unserializable types such as sets and datetimes raise `TypeError` unless you pass `default=`.

### Q: How do you handle bad input to `JSON.parse`, and what does `JSON.parse("undefined")` do?

**A:** Wrap it in `try/catch`; it throws a `SyntaxError`. `"undefined"` is not valid JSON, so it throws too. `JSON.parse("null")` is valid and returns `null`.

## A17 — JS Date, Math, Number (2 Oct)

### Q: In a JS `Date`, which things are 0-indexed? What date is `new Date(2026, 0, 31)`?

**A:** Months are 0-indexed (0 = January, 11 = December); the day of the month starts at 1. `new Date(2026, 0, 31)` is 31 January 2026. `getDay()` is 0-indexed too (0 = Sunday).

### Q: `new Date("2026-10-02")` vs `new Date(2026, 9, 2)` — what is the time zone trap?

**A:** A date-only ISO string is parsed as UTC midnight; the component constructor uses local time. In a time zone behind UTC, the first can print as 1 October when formatted locally.

### Q: What do `Math.round`, `floor`, `ceil` and `trunc` return for `-2.5`?

**A:** `Math.round(-2.5)` is `-2` (halves round toward +∞), `Math.floor(-2.5)` is `-3`, `Math.ceil(-2.5)` is `-2`, `Math.trunc(-2.5)` is `-2`.

### Q: Why is `0.1 + 0.2 !== 0.3`, and what do you do about it?

**A:** Numbers are IEEE 754 binary floats. 0.1 and 0.2 can't be stored exactly, so the sum is `0.30000000000000004`. Compare with a tolerance (`Math.abs(a - b) < Number.EPSILON`), do money math in integer cents, and use `toFixed` only for display.

### Q: `Number.isNaN` vs `isNaN` — what is the difference?

**A:** `isNaN` coerces its argument first, so `isNaN("abc")` is `true`. `Number.isNaN` is `true` only for the actual value `NaN`, so `Number.isNaN("abc")` is `false`.

### Q: What is `Number.MAX_SAFE_INTEGER`, and what happens past it?

**A:** 2^53 − 1, which is `9007199254740991`. Beyond it integers lose precision (`9007199254740992 === 9007199254740993` is `true`). Use `BigInt` (`123n`) for larger integers; you can't mix `BigInt` and `Number` in one expression.

### Q: What type does `toFixed` return? What does `(1.005).toFixed(2)` give?

**A:** A string. `(1.005).toFixed(2)` is `"1.00"`, not `"1.01"`, because 1.005 is stored as 1.00499999999999989… Wrap it in `Number()` if you need a number back.

## A18 — JS Regular expressions (2 Oct)

### Q: What do the `g`, `i` and `m` flags do?

**A:** `g` finds every match instead of just the first; `i` ignores case; `m` makes `^` and `$` match at each line boundary instead of only at the start and end of the whole string.

### Q: `test` vs `match` vs `replace` — what does each return?

**A:** `re.test(str)` returns a boolean. `str.match(re)` returns an array describing the match, or `null`; with the `g` flag it returns every matched string and drops capture groups. `str.replace(re, repl)` returns a new string and leaves the original unchanged.

### Q: Name the common regex tokens `\d \w \s ^ $ + * ? .`

**A:** `\d` a digit, `\w` a word character (letter, digit, underscore), `\s` whitespace, `^` start, `$` end, `+` one or more, `*` zero or more, `?` zero or one, `.` any character except a newline.

### Q: What does `"a-b-c".replace("-", "+")` return? How do you replace every occurrence?

**A:** `"a+b-c"`. A string pattern replaces only the first match. Use a global regex, `"a-b-c".replace(/-/g, "+")`, or `"a-b-c".replaceAll("-", "+")`.

### Q: What is the trap with calling `.test()` repeatedly on a regex with the `g` flag?

**A:** A global regex keeps `lastIndex` between calls, so `const re = /a/g; re.test("a"); re.test("a");` returns `true` and then `false`. Don't reuse a `g` regex for `test`, or reset `re.lastIndex = 0` first.

### Q: How do capture groups work with `match` and `replace`?

**A:** Parentheses capture: `"2026-10".match(/(\d+)-(\d+)/)` gives `["2026-10", "2026", "10"]`. In `replace`, refer to them as `$1` and `$2`, or pass a callback `(m, a, b) => ...`. Named groups, `(?<year>\d{4})`, are read from `match.groups.year`.

### Q: Greedy vs lazy: what do `/<.+>/` and `/<.+?>/` match in `<a><b>`?

**A:** Greedy `.+` takes as much as it can, so `/<.+>/` matches the whole `<a><b>`. Lazy `.+?` stops at the first possible end, so `/<.+?>/` matches just `<a>`.

### Q: What are Python's equivalents: `re.search`, `re.match`, `re.findall`, `re.sub`? Why raw strings?

**A:** `re.search` finds the first match anywhere (a match object or `None`); `re.match` matches only at the start; `re.findall` returns a list of matched strings; `re.sub(pattern, repl, s)` replaces every occurrence by default, unlike JS string `replace`. Use raw strings, `r"\d+"`, so backslashes aren't eaten. In pandas the same jobs are `.str.contains` and `.str.replace(regex=True)`.

## A19 — Python lists & comprehensions (2 Oct)

### Q: Python list indexing and slicing: what do `lst[-1]`, `lst[1:4]` and `lst[::-1]` give? How does that differ from JS?

**A:** `lst[-1]` is the last item, `lst[1:4]` is items 1 to 3, `lst[::-1]` is a reversed copy. In JS `arr[-1]` is `undefined`; use `arr.at(-1)`. JS `slice(1, 4)` matches Python's start/stop but has no step.

### Q: Which Python list methods mutate and which don't? Compare with the JS array table.

**A:** Mutating: `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`. Non-mutating: `sorted(lst)`, `lst[:]`, `lst + other`, `lst.copy()`, `index`, `count`. Same split as JS, where `sort` and `reverse` also mutate, so copy first with `[...arr].sort()`.

### Q: `append` vs `extend` vs `+=` on a list.

**A:** `append(x)` adds `x` as one element: `[1, 2].append([3])` gives `[1, 2, [3]]`. `extend(iterable)` adds each element: `[1, 2, 3]`. `lst += other` behaves like `extend` and mutates in place. `lst + other` builds a new list.

### Q: `lst.sort()` vs `sorted(lst)` — what does each return?

**A:** `sort()` sorts in place and returns `None`, so `x = lst.sort()` leaves `x` as `None`. `sorted(lst)` returns a new sorted list from any iterable and leaves the original untouched.

### Q: Rewrite `nums.filter(x => x % 2 === 0).map(x => x * x)` as a list comprehension.

**A:** `[x * x for x in nums if x % 2 == 0]`. The transform goes at the front, the filter `if` at the end.

### Q: In a comprehension, where does an `if`/`else` go versus a plain filtering `if`?

**A:** A conditional expression (with `else`) goes at the front: `[x if x > 0 else 0 for x in nums]`. A filtering `if` (no `else`) goes at the end: `[x for x in nums if x > 0]`.

### Q: In what order do you read a nested comprehension like `[x for row in matrix for x in row]`?

**A:** Left to right, in the same order as the equivalent nested loops: the outer `for row in matrix` comes first, the inner `for x in row` second. It flattens the matrix.

### Q: What are dict and set comprehensions? Why is `{w: words.count(w) for w in set(words)}` a poor word-frequency counter?

**A:** `{k: v for k, v in pairs}` builds a dict and `{x for x in lst}` builds a set. `words.count(w)` rescans the whole list for every word, so it is O(n²). Use `collections.Counter(words)`, which is O(n).

### Q: What is the aliasing trap with `b = a`, `a[:]` and `[[0] * 3] * 3`?

**A:** `b = a` makes two names for one list. `a[:]` or `a.copy()` makes a shallow copy; nested lists are still shared. `[[0] * 3] * 3` repeats a reference to the same inner list three times, so changing one row changes all. Build rows separately: `[[0] * 3 for _ in range(3)]`.

## B20 — Set / Map drill (2 Oct)

### Q: Dedupe an array with `Set`, count word frequency with `Map`, and print the top 3 words (JavaScript).

**A:** `const nums = [3, 1, 3, 2, 1];
const unique = [...new Set(nums)];          // [3, 1, 2]

const words = "the cat and the hat and the bat".split(" ");
const freq = new Map();
for (const w of words) freq.set(w, (freq.get(w) ?? 0) + 1);

const top3 = [...freq].sort((a, b) => b[1] - a[1]).slice(0, 3);
console.log(unique, top3);   // [["the",3],["and",2],["cat",1]]`

### Q: The same dedupe and top-3 word count in Python.

**A:** `from collections import Counter

nums = [3, 1, 3, 2, 1]
unique = list(dict.fromkeys(nums))      # [3, 1, 2], keeps first-seen order

words = "the cat and the hat and the bat".split()
freq = Counter(words)
print(unique, freq.most_common(3))      # [('the', 3), ('and', 2), ('cat', 1)]`

## B21 — JSON round-trip drill (2 Oct)

### Q: Round-trip an object through `JSON.stringify` / `JSON.parse` and say exactly what was lost.

**A:** `const original = { name: "Ana", age: undefined, greet() {}, joined: new Date("2026-10-02"), tags: new Set(["a"]), n: NaN };
const copy = JSON.parse(JSON.stringify(original));
console.log(copy);
// { name: "Ana", joined: "2026-10-02T00:00:00.000Z", tags: {}, n: null }`
Lost: `age` (undefined) and `greet` (function) are dropped; `joined` is now a string, not a Date; `tags` (a Set) became `{}`; `NaN` became `null`.

### Q: Redo the deep copy of that object so the `Date` and `Set` survive. What still breaks?

**A:** `structuredClone` keeps the `Date` and the `Set`: `const copy = structuredClone({ name: "Ana", joined: new Date("2026-10-02"), tags: new Set(["a"]) });`. It throws a `DataCloneError` if the object holds a function, so remove methods like `greet` first. It also drops the prototype, so a class instance comes back as a plain object.

## B22 — Comprehension drill (2 Oct)

### Q: Rewrite last Thursday's `filter` → `map` as one Python list comprehension, then as the JS chain.

**A:** `nums = [1, 2, 3, 4, 5, 6]
squares_of_evens = [x * x for x in nums if x % 2 == 0]   # [4, 16, 36]`
JS: `nums.filter(x => x % 2 === 0).map(x => x * x)`  // [4, 16, 36]

### Q: Write a comprehension that replaces negatives with 0, and another that flattens a 2D list.

**A:** `nums = [3, -1, 4, -5]
clamped = [x if x > 0 else 0 for x in nums]      # [3, 0, 4, 0]

matrix = [[1, 2], [3, 4], [5]]
flat = [x for row in matrix for x in row]         # [1, 2, 3, 4, 5]`

## B23 — Trap probe: Date / Math / Number / regex (2 Oct)

### Q: Predict each result before running it: `new Date(2026, 0, 31).getMonth()`, `0.1 + 0.2 === 0.3`, `Math.round(-2.5)`, `Math.round(2.5)`, `isNaN("abc")`, `Number.isNaN("abc")`, `"a-b-c".replace("-", "+")`, `(1.005).toFixed(2)`, and `re.test` twice on `const re = /a/g`.

**A:** `new Date(2026, 0, 31).getMonth()` → `0`
`0.1 + 0.2 === 0.3` → `false` (it is 0.30000000000000004)
`Math.round(-2.5)` → `-2`; `Math.round(2.5)` → `3`
`isNaN("abc")` → `true`; `Number.isNaN("abc")` → `false`
`"a-b-c".replace("-", "+")` → `"a+b-c"`
`(1.005).toFixed(2)` → `"1.00"` (a string)
`const re = /a/g; re.test("a"); re.test("a");` → `true`, then `false`

## D1 — Week 0 basics (11 and 14 Sep)

### Q: Contains Duplicate: what are the three ways to solve it, and what does each cost?

**A:** Brute force compares every pair: O(n²) time, O(1) space. Sorting puts duplicates side by side, so one pass finds them: O(n log n) time, O(n) space for the sorted copy. A set remembers what it has seen: O(n) time, O(n) space. The set version is the one to give.

### Q: Python: what is its version of null, how do you make a constant, and which names can't you use as a variable?

**A:** `None` (its type is `NoneType`). Python has no real constants, so `MAX = 100` is a naming convention and nothing stops you reassigning it. An identifier can't start with a digit, can't contain `-`, and can't be a keyword such as `class`. Names are case-sensitive, so `Class` is fine.

### Q: Java: what happens at `Integer.MAX_VALUE + 1`? What does `(int) 9.99` give? Why does `if (1)` not compile?

**A:** `int` is 32 bits, so `Integer.MAX_VALUE + 1` wraps around to `-2147483648` with no error. `(int) 9.99` truncates to `9`; it doesn't round. Java has no truthiness: a condition must be a `boolean`, so write `x != 0` instead of `if (x)`. Primitives such as `int` can't be `null`; only reference types like `String` and `Integer` can.

### Q: Compare Python, Java, JavaScript and TypeScript on null, constants, truthiness, integer division, `"5" + 3` and `-7 % 2`.

**A:** null: `None` / `null` (reference types only) / `null` and `undefined` / same as JS, checked by `strictNullChecks`. Constant: `MAX = 100` by convention / `final int MAX = 100` / `const` / `const`. Truthiness: empty and zero are falsy / none, needs a `boolean` / 8 falsy values / same as JS. Integer division: `//` / `/` on two ints / none, use `Math.trunc(7 / 2)` / same as JS. `"5" + 3`: `TypeError` / `"53"` / `"53"` / `"53"`. `-7 % 2`: `1` / `-1` / `-1` / `-1`.

### Q: What three rules does JavaScript's `==` follow when the two sides are different types?

**A:** 1. Same type: it behaves like `===`. 2. `null` and `undefined` are equal to each other and to nothing else. 3. Otherwise both sides are converted to numbers (objects are turned into a primitive first). So `"1" == 1` is true, `[1] == 1` is true, `[] == false` is true, `null == 0` is false, and `NaN == NaN` is false. This is why most code uses `===`.

### Q: Why must the `% 15` check come first in FizzBuzz?

**A:** A multiple of 15 is also a multiple of 3 and of 5. If `% 3` came first it would print `Fizz` and never reach `FizzBuzz`.

### Q: Why does TypeScript reject `const questions: Question[] = data` when `data` comes from a JSON file, and what is the cost of `as Question[]`?

**A:** TypeScript reads the JSON as `{ difficulty: string }`, and `string` is wider than `"easy" | "medium" | "hard"`. `as Question[]` tells the compiler to trust you and checks nothing at runtime, so a typo like `"midium"` in the JSON won't be caught. That is fine for local mock data. Real data from a server needs a guard or validation.

## D2 — Functions and recursion (15 and 16 Sep)

### Q: JavaScript: what does a default parameter do, and where must `...rest` go?

**A:** A default is used when the argument is missing or `undefined`. `...rest` collects all the remaining arguments into a real array, and it must be the last parameter. It is the opposite job of spread (`...arr` in a call), which expands an array into arguments. `function greet(name = "friend", ...rest)` called as `greet("Ana", 1, 2, 3)` gives `rest = [1, 2, 3]`.

### Q: TypeScript: how do you annotate a function that returns a function, and what does the compiler do if you use the result as the wrong type?

**A:** Write the returned function's type after the parameters: `function makeCounter(start: number): () => number`. The compiler then knows that calling the result gives a `number`, so `const bad: string = next()` is an error.

### Q: What makes a function higher-order, and what must a recursive function have?

**A:** A higher-order function takes a function as an argument, returns a function, or both. A callback is a function you pass in to be called later. A recursive function needs a base case that stops it, and each call must move toward that base case. Without one it recurses until the stack runs out.

## D3 — SQL: NULL and commands (16 Sep)

### Q: What are the five ways to handle NULLs in SQL?

**A:** `IS NULL`, `IS NOT NULL`, `COALESCE()` (the first non-NULL value in a list), `IFNULL()` / `NVL()` / `ISNULL()` (the MySQL / Oracle / SQL Server versions of replacing NULL with a value), and `NULLIF()` (returns NULL when two values are equal, handy to avoid dividing by zero: `total / NULLIF(count_value, 0)`). Remember that NULL is not 0, not an empty string and not FALSE.

### Q: How is `ALTER` different from `UPDATE`?

**A:** `ALTER` is DDL: it changes the table's structure, such as adding, dropping or modifying a column, and a new column starts as NULL in every row. `UPDATE` is DML: it changes the values in existing rows.

### Q: Why does `WHERE v != 1` not return rows where `v` is NULL, and how do you include them?

**A:** Comparing anything to NULL gives unknown, and `WHERE` keeps only rows where the test is true, so the NULL row is dropped. Add `OR v IS NULL` to include it.

### Q: How do `SUM`, `AVG`, `COUNT(*)` and `COUNT(col)` treat NULLs, and does `salary < 50000` match a NULL salary?

**A:** `SUM`, `AVG`, `MAX` and `MIN` ignore NULLs, and `AVG` divides by the number of non-NULL values only. If every value is NULL, `SUM` and `AVG` return NULL, not 0. `COUNT(*)` counts all rows and `COUNT(col)` skips NULLs. `salary < 50000` doesn't match a NULL, so add `OR salary IS NULL` to include it.

## D4 — Objects, destructuring, spread and rest (1 Oct)

### Q: What is the difference between `obj.key` and `obj["key"]`, and what does a computed key do? What do `Object.keys`, `Object.values` and `Object.entries` return?

**A:** Dot access needs a fixed name. Brackets accept any expression, such as a variable. A computed key `[key]: value` uses the value of `key` as the property name. `Object.keys` returns the names, `Object.values` the values, and `Object.entries` an array of `[key, value]` pairs: `Object.entries({ a: 1, b: 2 })` is `[["a", 1], ["b", 2]]`.

### Q: Object destructuring: how do you rename a property, give a default, and reach a nested value?

**A:** It matches by property name. `const { id: userId } = user` renames. `const { role = "guest" } = user` sets a default, used when the value is `undefined`. `const { address: { city } } = user` goes into a nested object. Example: `const { name, role = "guest", address: { city } } = { name: "Ana", address: { city: "Pune" } }` gives `Ana`, `guest`, `Pune`.

### Q: Array destructuring: how do you skip an item, give a default and collect the rest?

**A:** It matches by position. A skipped item is an empty slot between commas, a default applies when the value is `undefined`, and `...rest` collects the remainder: `const [first, , third = 9, ...rest] = [1, 2, undefined, 4, 5]` gives `first = 1`, `third = 9`, `rest = [4, 5]`.

### Q: Spread and rest both use `...`: how do you tell them apart, and which value wins in an object spread?

**A:** Spread expands a collection into separate items and goes on the right of `=` or inside a call: `[...a, ...b]`, `{ ...obj }`, `sum(...nums)`. Rest collects separate items into one array and goes on the left (a destructuring pattern) or in a parameter list. In an object spread the later key wins: `{ ...{ x: 1, y: 2 }, y: 9 }` is `{ x: 1, y: 9 }`.

## D5 — this, call, apply and bind (1 and 8 Oct)

### Q: What decides the value of `this` in a regular function, and what does an arrow function do about `this`?

**A:** The call site decides. `obj.method()` gives `this = obj`, but a plain `f()` call gives `undefined` in strict mode (the global object otherwise). An arrow function has no `this` of its own: it uses the `this` of the place where it was written. So an arrow function used as an object's method does not get the object.

### Q: Why does `const c = counter.inc; c()` lose `this`, and what are the two fixes?

**A:** Copying the method into a variable removes the `counter.` in front of the call, so nothing supplies `this`. In strict mode it is `undefined` and `this.count` throws a `TypeError`. Fix 1: `counter.inc.bind(counter)`, which returns a new function with `this` fixed. Fix 2: wrap the call in an arrow function: `() => counter.inc()`.

### Q: How do `call`, `apply` and `bind` differ, and when can you pass `null` as `this`?

**A:** All three set `this` explicitly. `call(thisArg, a, b)` runs the function now with the arguments listed one by one. `apply(thisArg, [a, b])` runs it now with the arguments in an array. `bind(thisArg, a)` doesn't run it: it returns a new function with `this` (and optionally some arguments) fixed. Pass `null` as `this` only when the function doesn't use `this`, like `Math.max.apply(null, [1, 5, 3])`.

### Q: TypeScript: how do you tell the compiler what `this` is inside a function, and what happens on a plain call?

**A:** Add a fake first parameter named `this`: `function greet(this: { name: string }, g: string)`. It is erased at compile time. `greet.call({ name: "Ana" }, "Hi")` is fine, but a plain `greet("Hi")` is an error because the call supplies no `this`.

## D6 — Two pointers (1, 8 and 9 Oct)

### Q: Two Sum II: why can two pointers replace the hash map, which pointer moves, and why is the answer 1-based?

**A:** The array is sorted, so the sum tells you which way to move. Too small: move `l` right to get a bigger number. Too big: move `r` left. Each step discards one number that can't be part of the answer, so it is O(n) time and O(1) space with no map. The problem asks for 1-based indexes, so return `l + 1` and `r + 1`.

### Q: 3Sum: why sort first, and where are duplicates skipped?

**A:** Sorting lets you fix one number `i` and then run Two Sum II (two pointers) on the rest. Duplicates are skipped at two levels: the outer one (`i > 0 and nums[i] == nums[i - 1]`) so the same first number isn't used twice, and the inner one after a hit so the same pair isn't added twice. Push `[a, b, c]` into the result, not their sum.

### Q: Container With Most Water: what is the area formula, which pointer moves, and why can't that move miss the best answer?

**A:** Area is `min(height[l], height[r]) * (r - l)`: the shorter line sets the water level and the gap sets the width. Start at both ends for the widest container, then move the pointer at the shorter line inward. The width only shrinks from here, so a taller line is the only way to get a bigger area, and keeping the shorter line can never beat the best already recorded. O(n) time, O(1) space.

### Q: How is Container With Most Water different from 3Sum?

**A:** 3Sum fixes one number and then moves two pointers based on a sum. In Container With Most Water the move depends on the heights, and you keep a running maximum instead of looking for a target.

## D7 — TypeScript: functions, strict, interfaces (8 and 9 Oct)

### Q: What do `?` and a default value mean on a parameter, and what type does each have inside the function?

**A:** A `?` parameter may be left out, so inside the function it is `T | undefined`. A default parameter (`greeting = "Hello"`) always has a value inside, and callers may leave it out.

### Q: TypeScript overloads: what do overload signatures give you, and how are they different from Java's overloading?

**A:** Overload signatures list the exact call shapes that are allowed, and the implementation signature underneath is not visible to callers: `pad(x: string): string;` and `pad(x: number): string;` over a body that takes `string | number`, so `pad(true)` is an error. TypeScript has one implementation body per function. In Java each overload has its own body, and the compiler picks one at compile time from the number and types of the arguments.

### Q: Which flags does `"strict": true` turn on? Is `noUncheckedIndexedAccess` one of them?

**A:** Your notes (§12) list `strictNullChecks`, `noImplicitAny`, `strictFunctionTypes`, `strictPropertyInitialization`, `strictBindCallApply` and `useUnknownInCatchVariables`. TypeScript's `strict` also includes `noImplicitThis` and `alwaysStrict`. `noUncheckedIndexedAccess` is not part of `strict`: you add it yourself, and it makes `arr[i]` be `T | undefined`.

### Q: Give one failing line for each: `noImplicitAny`, `strictNullChecks`, `strictPropertyInitialization`, `useUnknownInCatchVariables`, `strictBindCallApply`.

**A:** `noImplicitAny`: `function double(x) { return x * 2; }` (x has no type). `strictNullChecks`: `const el: HTMLElement = document.getElementById("app");` (it can be null). `strictPropertyInitialization`: a class field `name: string;` that is never assigned. `useUnknownInCatchVariables`: `catch (e) { console.log(e.message); }` (e is `unknown`). `strictBindCallApply`: `greet.call(null, 5)` when `greet` takes a string.

### Q: `noImplicitThis`: why does `this.count` fail inside a function returned from a method, and what are the fixes?

**A:** A normal function nested inside the method gets its own `this`, which TypeScript can't type, so it is an implicit `any`. Fix 1: return an arrow function, which keeps the outer `this`. Fix 2: give the inner function an explicit `this` parameter: `function (this: { count: number }) { return this.count; }`.

### Q: What do `?` and `readonly` do on an interface property, and what is an index signature for?

**A:** `?` means the property may be missing, so its type is `T | undefined` and you can set it later. `readonly` allows a value only when the object is created, and any later assignment is a compile error (checked at compile time only). An index signature `[name: string]: number` is for objects whose property names you don't know in advance but whose value type you do: every value must be a number. `Record<string, number>` means the same.

### Q: How do you extend an `interface` and combine `type`s, and what is declaration merging?

**A:** An interface extends with `extends`: `interface Quiz2 extends Base`. A type combines with `&`: `type Quiz3 = Base2 & { title: string }`. If you declare an `interface` twice with the same name, TypeScript merges them into one. Declaring a `type` twice with the same name is an error.

### Q: When do you pick `interface` and when `type`?

**A:** Use `interface` for object shapes that other code may extend or merge, such as a public API. Use `type` for unions (`string | number`), tuples, primitives and computed types, which an interface can't name. For a plain object shape either works, so follow what the rest of the project uses.

### Q: How is a TypeScript tuple different from an array, and what does an interface add for objects?

**A:** An array is any length of one type. A tuple has a fixed length and each position has its own type, so order matters: `[string, number]` accepts `["age", 30]` but not `[30, "age"]`. An interface names the shape of an object, so every property is checked, and a missing one such as `y` in `{ x: 1 }` is an error.

## D8 — Python collections (8 Oct)

### Q: Python tuple: what makes it different from a list, and can it be a dictionary key?

**A:** A tuple is an ordered, immutable sequence, so `t[0] = 9` raises `TypeError`. Because it can't change it is hashable, so it can be a dict key (`{(1, 2): "point"}`), and a list can't. A TypeScript tuple is only a compile-time type for a fixed-length array and is still a normal mutable array at runtime.

### Q: Python set: how do you take a union, an intersection and a difference?

**A:** A set holds unique items with fast membership checks and is unordered. Union `|`, intersection `&`, difference `-`: with `s1 = {1, 2, 3}` and `s2 = {2, 3, 4}`, `s1 | s2` is `{1, 2, 3, 4}`, `s1 & s2` is `{2, 3}` and `s1 - s2` is `{1}`.

### Q: Python dict: what is the difference between `d.get(k)` and `d[k]` for a missing key, what does `setdefault` do, and how do you count words?

**A:** `d[k]` raises `KeyError` for a missing key, while `d.get(k)` returns `None` (or a default you pass: `d.get(k, 0)`). `setdefault(k, v)` returns the existing value, or stores `v` and returns it. To count words: `counts[w] = counts.get(w, 0) + 1`.

### Q: Compare Python's tuple, list, set and dict: ordered, mutable, duplicates, and the closest JavaScript or TypeScript equivalent.

**A:** tuple: ordered, not mutable, duplicates allowed, like a TS tuple type. list: ordered, mutable, duplicates allowed, like an array. set: unordered, mutable, no duplicates, like `Set` (which keeps insertion order). dict: ordered by insertion, mutable, unique keys, like `Map` or an object. A dict key must be hashable, so a tuple can be a key but a list can't. A `Map` accepts any key.

## D9 — Java methods and recursion (17 Sep and 9 Oct)

### Q: What is the difference between a parameter and an argument, and what does `void` mean?

**A:** A parameter is the variable in the method definition, and an argument is the value you pass in when you call it. `void` means the method returns nothing.

### Q: Static vs instance method: can a `static` method use `this`, and how do you call each?

**A:** A `static` method belongs to the class and has no `this`, so it can't use instance fields; call it as `square(4)` or `M.square(4)`. An instance method needs an object, so you call it as `new M().plusBase(5)`.

### Q: What does a recursive method need, and what happens without it?

**A:** A base case that stops it, and every call must move closer to that base case. Each call adds a frame to the call stack, which has a fixed size, so without a base case Java throws `StackOverflowError`.

### Q: Java is pass-by-value: what happens to the caller's `int`, and what happens when a method changes an array it receives?

**A:** For an `int`, the method gets a copy, so the caller's value doesn't change. For an array it gets a copy of the reference: changing an element is visible to the caller, but pointing the parameter at a new array is not. Java is always pass-by-value.

## A20 — 24 Sep gaps (strings, array methods, React setup, P2, Java, TS)

### Q: `slice` vs `substring` on a string: what does each do with a negative index? Name four other string methods you use daily.

**A:** `"hello".slice(-3)` is `"llo"` (negative counts from the end). `"hello".substring(-3)` is `"hello"` (negatives become 0, and it swaps its arguments if start > end). Daily ones: `trim()`, `split(sep)`, `includes(x)`, `indexOf(x)` (-1 if missing), `replace` / `replaceAll`, `toUpperCase()`, `at(-1)`. Strings are immutable, so every one of these returns a new string.

### Q: `includes` vs `indexOf` on an array: which one finds `NaN`, and which one do you use for a yes/no check?

**A:** `[NaN].includes(NaN)` is `true` and `[NaN].indexOf(NaN)` is `-1`, because `indexOf` uses `===` and `NaN !== NaN`. For yes/no use `includes` (a boolean). Use `indexOf` only when you need the position.

### Q: `find` vs `findIndex`: what does each return when nothing matches?

**A:** `find` returns `undefined` and `findIndex` returns `-1`. So check `=== -1` for `findIndex`, never `if (idx)`, because index `0` is falsy.

### Q: `reverse`, `fill`, `shift`, `unshift`: which mutate, and what does each return?

**A:** All four mutate the array. `reverse()` and `fill(v)` return the same array. `shift()` returns the removed first item. `unshift(x)` returns the new length. Example: `const a = [1,2,3]; a.reverse() === a` is `true`, `a.unshift(0)` returns `4`.

### Q: `concat` and `join`: does either mutate? What does `join` do with `null` and `undefined`, and what is the default separator?

**A:** Neither mutates. `concat` returns a new array and flattens one level of array arguments: `[1,2].concat([3,[4]])` is `[1,2,3,[4]]`. `join` returns a string; the default separator is a comma (`[1,2].join()` is `"1,2"`), and `null` or `undefined` items become empty strings: `[1,null,undefined,2].join("-")` is `"1---2"`.

### Q: React Part 2: what is Vite, why do you need Node, and what is the command to start a React + TypeScript project?

**A:** Node runs the tooling (npm installs packages and runs scripts) on your machine; React itself runs in the browser. Vite is the dev server and bundler: it serves your files instantly with hot reload and builds the production bundle. Start a project with `npm create vite@latest study-agent-ui -- --template react-ts`, then `npm install` and `npm run dev`.

### Q: P2 Next/Previous buttons: write the state, the two handlers and the disabled conditions for 10 questions, with no wrap-around.

**A:** `const [index, setIndex] = useState(0);` then `<button onClick={() => setIndex(i => i - 1)} disabled={index === 0}>Previous</button>` and `<button onClick={() => setIndex(i => i + 1)} disabled={index === questions.length - 1}>Next</button>`. The updater form `i => i - 1` reads the latest state. Disabling at both ends stops the index going negative or past the last question.

### Q: Why does `questions[index]` need an `if (!question) return ...` guard in P2, and which flag causes it?

**A:** With `noUncheckedIndexedAccess` on, indexing an array gives `Question | undefined`, because the index might be out of range. The guard narrows it to `Question` before you render. Without the guard `tsc` errors with "possibly undefined"; `questions[index]!` also compiles but hides a real out-of-range bug.

### Q: Java is pass-by-value: what happens to a caller's `int` when a method does `x++`, to an array when the method does `a[0] = 9`, and when it does `a = new int[]{7}`?

**A:** `x++` changes only the method's copy, so the caller's `int` is unchanged. `a[0] = 9` follows the copied reference to the same array, so the caller sees `9`. `a = new int[]{7}` only repoints the local copy of the reference, so the caller still sees its old array. Verified: caller prints `1 9`. One line: Java passes everything by value, and for objects the value is the reference.

### Q: TypeScript: what is the difference between `void` and `undefined` as a return type, and why does `[1, 2].forEach(n => arr.push(n))` compile?

**A:** `void` means "ignore whatever comes back"; `undefined` means the function really returns the value `undefined`. A callback typed `() => void` may return something and TS ignores it, so the arrow function that returns `push`'s number is allowed. `forEach` itself returns `undefined`, so you can't chain after it.

### Q: TypeScript: when do you use a union parameter, an options object, or overloads?

**A:** Union first: one parameter takes several types and the return type is the same (`id: string | number`). Options object when there are several optional settings or boolean flags (`fetchUsers({ limit: 5, sortBy: "name" })`). Overloads last, only when the return type depends on which arguments were passed (`parse(input)` returns `object`, `parse(input, true)` returns `string`). Optional parameters (`level?: ...`) must come after required ones.

### Q: Java `equals` and `hashCode`: what is the contract, and what does the default `toString()` print?

**A:** If two objects are `equals`, they must have the same `hashCode`. Override both together, or `HashMap` and `HashSet` break: an equal key can land in a different bucket and not be found. The default `equals` is `==` (same reference). The default `toString()` prints `ClassName@hexHash`, e.g. `java.lang.Object@1b6d3586`, so override it to print useful values.

### Q: Java exceptions: checked vs unchecked, and does `finally` run when the `try` block returns?

**A:** Checked exceptions (`IOException`) must be caught or declared with `throws`, and the compiler enforces it. Unchecked ones (`RuntimeException` and its children, such as `NullPointerException`) are not enforced. `finally` runs even when `try` returns: `try { return 1; } finally { System.out.println("finally"); }` prints `finally`, then the caller gets `1` (verified).

### Q: Java `ArrayList` and `Iterator`: what happens when you remove from a list inside a for-each, and what are the safe ways?

**A:** It throws `ConcurrentModificationException` (verified), because the list changed under the iterator. Safe ways: `list.removeIf(x -> x % 2 == 0)` (verified, `[1, 2, 3, 4]` becomes `[1, 3]`), or call `iterator.remove()` on an explicit `Iterator`, or loop with an index from the end.

### Q: Java `HashMap`: what does `get` return for a missing key, can the key be null, and what does `getOrDefault` do?

**A:** `get` returns `null` for a missing key. A `HashMap` allows one `null` key and many `null` values. `getOrDefault(k, d)` returns `d` instead of `null`, so counting is `m.put(w, m.getOrDefault(w, 0) + 1)`. Verified: `m.get("x")` is `null`, `getOrDefault("x", 0)` is `0`, `m.get(null)` is `1` after `put(null, 1)`.
