---
title: TS-COMPLETE-NOTES
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/TS-COMPLETE-NOTES.md
---

# TypeScript — Complete Notes, Written as the Delta from JavaScript

> You already know JavaScript. TypeScript is JavaScript plus a **compile-time type layer that is
> erased before anything runs**. So this file doesn't re-teach the language — it covers only what's
> actually new, and the places the type system surprises people who already write JS well.
> Companion to `javascriptnotes/JAVASCRIPT-COMPLETE-NOTES.md`. Section references marked **JS §n**
> point there.

---

## The one-paragraph version

Every valid JavaScript file is a valid TypeScript file. You add annotations; `tsc` checks them and
then **deletes them**, emitting plain JavaScript. Nothing about runtime behaviour changes — no new
data structures, no new operators that survive compilation, no runtime type checking. If you're
debugging behaviour, you're debugging JavaScript. If you're fighting a red squiggle, you're fighting
a compiler that never sees your program run.

That single fact explains most of TypeScript's strangeness, and it's the thing to say out loud in an
interview.

```typescript
// what you write
function greet(name: string): string { return `Hi, ${name}`; }

// what actually runs
function greet(name) { return `Hi, ${name}`; }
```

## What's genuinely new — the whole list

| | JavaScript | TypeScript adds |
|---|---|---|
| Variables | `let x = 5` | `let x: number = 5` — and usually you omit it, because inference |
| Functions | `function f(a, b) {}` | Parameter and return types; optional and default params are typed |
| Objects | `{ name: "M" }` | `interface`/`type` describing the shape |
| Arrays | `[1, 2]` | `number[]`, and **tuples** — `[string, number]` |
| Reuse | Duck typing at runtime | **Generics** — type parameters checked at compile time |
| Null safety | Runtime `?.` and `??` | `strictNullChecks` — the compiler forces you to handle it |
| Narrowing | `typeof` checks you remember to write | The compiler *tracks* those checks and narrows the type |
| Enums | Object literals by convention | `enum` (a real runtime construct — the one exception to erasure) |
| Modules | ESM (JS §68) | Same, plus `import type` and `.d.ts` declaration files |
| Classes | ES6 classes (JS §41) | `public`/`private`/`protected`, `readonly`, `abstract`, parameter properties |

Everything else — closures, `this`, prototypes, async, the event loop — is **identical**. Your
JavaScript knowledge transfers whole.

### Table of contents

1. Setup, `tsc`, and how it fits a project
2. Basic Types and Inference
3. `any`, `unknown`, `never` — and why `any` defeats the point
4. Arrays, Tuples, and Objects
5. Interfaces vs Type Aliases
6. Unions, Literals, and Narrowing
7. Functions in Depth
8. Generics
9. Utility Types
10. Classes in TypeScript
11. Modules, Declaration Files, and Third-Party Types
12. `tsconfig.json` and `strict`
13. TypeScript with React
14. TypeScript with Node and Express
15. Migrating JavaScript to TypeScript
16. The Twelve Traps
17. Cheat Sheet
18. Practice

Appendix A. 25 Days TypeScript Challenge (Days 2–13) — screenshot notes

---

## 1. Setup, `tsc`, and How It Fits a Project

```bash
npm i -D typescript @types/node
npx tsc --init            # creates tsconfig.json
npx tsc                   # compile
npx tsc --watch           # recompile on save
npx tsc --noEmit          # type-check only — what CI runs
```

**Three ways TypeScript reaches production:**

1. **`tsc` emits JavaScript** — the plain path. Slowest, but it type-checks.
2. **A bundler strips types** (esbuild, swc, Vite, Next.js) — fast, but **does not type-check**.
   You run `tsc --noEmit` separately in CI.
3. **Runtime strips types** (`ts-node`, Node 22+ with `--experimental-strip-types`, Bun, Deno).

Point 2 catches people out: your build passing does **not** mean your types are correct. Type
checking and bundling are separate jobs in most modern setups.

## 2. Basic Types and Inference

```typescript
let count: number = 42;
let name: string = "Jane Doe";
let active: boolean = true;
let nothing: null = null;
let missing: undefined = undefined;
let big: bigint = 100n;
let sym: symbol = Symbol("id");
```

**But don't write most of those.** TypeScript infers:

```typescript
let count = 42;              // inferred number
const name = "Jane Doe";        // inferred "Jane Doe" — a literal type, because const can't change
let items = [1, 2, 3];       // inferred number[]
```

**Annotate in exactly three places:** function parameters, function return types when they're not
obvious, and variables declared without an initialiser. Everywhere else, let inference work —
over-annotating is noise, and it's the most common beginner tell.

```typescript
// ✅ worth annotating
function total(items: CartItem[]): number { … }
let selected: User | null = null;

// ❌ noise
const names: string[] = users.map((u: User): string => u.name);
const names = users.map(u => u.name);        // same types, inferred
```

### `let` vs `const` widening

```typescript
let a = "hello";       // string      — can be reassigned, so widened
const b = "hello";     // "hello"     — literal type
```

This matters constantly with unions:

```typescript
type Method = "GET" | "POST";
let m = "GET";                    // inferred string — NOT assignable to Method
const m2 = "GET";                 // inferred "GET"  — assignable
fetch(url, { method: m });        // ❌ error
fetch(url, { method: m2 });       // ✅
// fix for let: let m: Method = "GET";  or  as const
```

## 3. `any`, `unknown`, `never`

```typescript
let a: any;         // disables checking entirely — a hole in the type system
let u: unknown;     // "I don't know yet" — safe, must be narrowed before use
let n: never;       // a value that can never exist
```

```typescript
const data: any = JSON.parse(input);
data.whatever.nonsense();          // compiles fine, crashes at runtime

const safe: unknown = JSON.parse(input);
safe.whatever;                     // ❌ compile error — good
if (typeof safe === "object" && safe !== null && "id" in safe) {
  safe.id;                         // ✅ narrowed
}
```

**Rule: `unknown` at every boundary.** `JSON.parse`, `fetch` responses, `localStorage`, form input,
third-party callbacks. Then narrow. Reaching for `any` there is exactly where runtime bugs come from,
and it's the single biggest thing separating TypeScript that helps from TypeScript that's theatre.

**`never`** appears in three places you'll actually meet:

```typescript
function fail(msg: string): never { throw new Error(msg); }   // never returns

type A = string & number;                                      // impossible → never

// Exhaustiveness checking — the genuinely useful one
type Shape = Circle | Square;
function area(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.r ** 2;
    case "square": return s.side ** 2;
    default:
      const _exhaustive: never = s;      // ❌ compile error if you add a Shape and forget a case
      return _exhaustive;
  }
}
```

That last pattern is worth memorising. Add a variant to the union and every unhandled `switch` breaks
the build — the compiler becomes your checklist.

## 4. Arrays, Tuples, and Objects

```typescript
let nums: number[] = [1, 2, 3];
let nums2: Array<number> = [1, 2, 3];          // identical
let mixed: (string | number)[] = [1, "a"];
let readonlyNums: readonly number[] = [1, 2];  // no push, no mutation
let matrix: number[][] = [[1, 2], [3, 4]];

// Tuples — fixed length, fixed types per position. New in TS.
let pair: [string, number] = ["age", 30];
let [key, value] = pair;                        // key: string, value: number
let named: [x: number, y: number] = [1, 2];     // labels, for readability
let rest: [string, ...number[]] = ["a", 1, 2];

// This is what useState returns
const state: [string, (v: string) => void] = useState("");
```

Objects — inline, or named (see §5):

```typescript
let user: { name: string; age: number; email?: string } = { name: "M", age: 30 };
//                                       ^ optional
```

### `as const`

```typescript
const config = { url: "/api", method: "GET" };
// inferred: { url: string; method: string }

const config2 = { url: "/api", method: "GET" } as const;
// inferred: { readonly url: "/api"; readonly method: "GET" }

const ROLES = ["admin", "user"] as const;
type Role = typeof ROLES[number];              // "admin" | "user"
```

That last two-liner — a runtime array *and* a derived union type from one source — is a pattern you'll
use constantly. No duplication between the values and the type.

## 5. Interfaces vs Type Aliases

```typescript
interface User {
  id: number;
  name: string;
  email?: string;             // optional
  readonly createdAt: Date;   // can't reassign after construction
}

type UserT = {
  id: number;
  name: string;
};
```

**They're almost interchangeable.** The real differences:

| | `interface` | `type` |
|---|---|---|
| Object shapes | ✅ | ✅ |
| Unions | ❌ | ✅ `type R = "a" \| "b"` |
| Primitives, tuples | ❌ | ✅ `type ID = string` |
| Extending | `extends` | `&` intersection |
| **Declaration merging** | ✅ reopens and merges | ❌ duplicate error |
| Mapped/conditional types | ❌ | ✅ |

```typescript
// Extending
interface Admin extends User { role: "admin"; }
type AdminT = UserT & { role: "admin" };

// Declaration merging — interface only. This is how you augment library types.
interface Window { myApp: AppState; }        // adds to the global Window
```

**Practical rule:** `interface` for object shapes you might extend or augment — especially public API
surfaces and anything a library consumer touches. `type` for everything else — unions, primitives,
tuples, function types, and anything computed. Don't spend time agonising; teams pick one and move on.

### Index signatures

```typescript
interface Counts { [key: string]: number; }
const c: Counts = { a: 1, b: 2 };

// Prefer Record when the keys are known
type Scores = Record<"math" | "science", number>;
```

## 6. Unions, Literals, and Narrowing

This is where TypeScript earns its keep, and where it's most different from JS thinking.

```typescript
type Status = "idle" | "loading" | "success" | "error";
type ID = string | number;

let s: Status = "idle";
s = "pending";                    // ❌ not assignable
```

### Narrowing — the compiler follows your checks

```typescript
function format(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();       // narrowed to string
  }
  return value.toFixed(2);            // narrowed to number — no else needed
}
```

Every narrowing mechanism:

```typescript
typeof x === "string"                 // primitives
x instanceof Date                     // classes
"role" in obj                         // property presence
Array.isArray(x)                      // arrays
if (x) { }                            // truthiness — removes null | undefined | "" | 0
x === null                            // equality
if (!user) return;                    // early return narrows the rest of the function
```

### Discriminated unions — the most valuable pattern in the language

Give every member a shared literal field. The compiler then narrows the *whole object* from one check.

```typescript
type Result =
  | { status: "success"; data: User[] }
  | { status: "error"; message: string }
  | { status: "loading" };

function render(r: Result) {
  switch (r.status) {
    case "success": return r.data.length;    // data exists here, message doesn't
    case "error":   return r.message;        // message exists here, data doesn't
    case "loading": return "…";
  }
}
```

This models "loading OR loaded OR failed" so the impossible states can't be represented — you cannot
have `data` and `message` at once. It replaces the JavaScript habit of `{ data: null, error: null,
loading: true }` where every field is optional and every access needs a guard.

### Custom type guards

```typescript
function isUser(x: unknown): x is User {          // "x is User" — a type predicate
  return typeof x === "object" && x !== null && "id" in x && "name" in x;
}

if (isUser(data)) { data.name; }                  // narrowed
```

`x is User` is a promise you make to the compiler — it doesn't verify your logic. A wrong type guard
is as dangerous as `any`. For real validation at a boundary, use **Zod** and get the type for free:

```typescript
import { z } from "zod";
const UserSchema = z.object({ id: z.number(), name: z.string() });
type User = z.infer<typeof UserSchema>;           // type derived from the validator
const user = UserSchema.parse(json);              // throws on bad data, and is typed
```

## 7. Functions in Depth

```typescript
function add(a: number, b: number): number { return a + b; }
const addArrow = (a: number, b: number): number => a + b;

function greet(name: string, greeting = "Hello"): string { … }   // default — type inferred
function log(msg: string, level?: "warn" | "error"): void { … }  // optional — msg: string | undefined
function sum(...nums: number[]): number { … }                     // rest

// Function types
type Handler = (event: MouseEvent) => void;
type Reducer<S, A> = (state: S, action: A) => S;

// void vs undefined
function f(): void { }              // returns nothing meaningful
function g(): undefined { return undefined; }   // explicitly returns undefined
```

**Optional parameters must come last**, and `?` means the type includes `undefined`.

### Overloads

TypeScript has no runtime overloading (JS doesn't). It has *declared* overloads over one implementation:

```typescript
function parse(input: string): object;
function parse(input: string, raw: true): string;
function parse(input: string, raw?: boolean): object | string {
  return raw ? input : JSON.parse(input);
}
```

Usually a union or an options object is clearer. Reach for overloads only when the return type
genuinely depends on the arguments.

### `this` typing

```typescript
function handler(this: HTMLButtonElement, e: MouseEvent) {
  this.disabled = true;                    // `this` is typed, and erased at compile time
}
```

The rules for what `this` *is* are unchanged from JavaScript (**JS §37**). TypeScript only lets you
declare what you expect.

## 8. Generics

A type parameter — the same idea as Java generics, and one of the few places TypeScript is genuinely
new rather than annotation.

```typescript
function identity<T>(value: T): T { return value; }
identity("hi");            // T inferred as string
identity<number>(42);      // explicit

function first<T>(arr: T[]): T | undefined { return arr[0]; }
```

Without generics you'd write `any` and lose the return type. With them, the relationship between
input and output is preserved.

### Constraints

```typescript
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
longest("abc", "de");        // ✅ strings have length
longest([1,2], [3]);         // ✅ arrays do too
longest(1, 2);               // ❌ numbers don't
```

### `keyof` and indexed access

```typescript
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: 1, name: "Jane Doe" };
getProp(user, "name");       // string
getProp(user, "id");         // number
getProp(user, "nope");       // ❌ not a key of user
```

That signature is worth being able to write from memory — it's a common interview question and it
appears throughout real codebases.

### Generic interfaces and classes

```typescript
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  save(entity: T): Promise<T>;
}

class Box<T> {
  constructor(private value: T) {}
  get(): T { return this.value; }
}
```

### Defaults

```typescript
interface ApiResponse<T = unknown> { data: T; status: number; }
```

### Generics vs `any`: same `T` in and out

`T` can be any type — `boolean`, `string`, `number`, an array, an object — but it is decided **once per
call**, and every place that uses `T` in that call must match. That is the difference from `any`.

```typescript
function idAny(value: any): any { return value; }
function idT<T>(value: T): T { return value; }

const a = idAny("hi");
a.toFixed(2);              // compiles, crashes at runtime: strings have no toFixed
const t = idT("hi");       // T = string, so t is a string
t.toFixed(2);              // ❌ caught while you write it
t.toUpperCase();           // ✅

idT(true);                 // T = boolean
idT(42);                   // T = number
idT([1, 2]);               // T = number[]
```

The parameter `value: T` and the return type `: T` are the same `T`, so the body can only return
something it knows is a `T`:

```typescript
function bad<T>(value: T): T {
  return "hello";          // ❌ T might be a number
}
```

Different letters mean different types: `function pair<T, U>(a: T, b: U): [T, U]`. In `first<T>(arr: T[])`
the `T` is the item type, so `first([1, 2, 3])` is `number | undefined` and `first(["a"])` is
`string | undefined`.

### Worked example: `maxBy`

Return the whole item with the largest value of one property. Start from the plain JavaScript loop,
then add types.

```javascript
function maxBy(items, key) {
  let best = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) {
      best = item;
    }
  }
  return best;
}
```

```typescript
function maxBy<T extends object, K extends keyof T>(items: T[], key: K): T | undefined {
  let best: T | undefined = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) {
      best = item;
    }
  }
  return best;
}

const people = [
  { name: "Ann", age: 30, score: 8.5 },
  { name: "Bo", age: 25, score: 9.1 },
];
maxBy(people, "age")?.name;     // "Ann"
maxBy([], "age");               // undefined
maxBy(people, "height");        // ❌ not a key of the person
```

- `T` is one item, so the list is `T[]`; `K` is a property name of one item.
- The result is one whole item, or `undefined` for an empty list.
- `T extends object`: a bare `T` could be `null`, and `best[key]` would be an error.
- `best: T | undefined`: without the annotation TypeScript can't tell what `best[key]` is.

This version still accepts `"name"` (a string property) and compares alphabetically. To refuse
non-number properties, constrain the key.

**Way 1: `Record<K, number>`** — each item must have a numeric property called `K`.

```typescript
function maxBy<K extends string, T extends Record<K, number>>(items: T[], key: K): T | undefined {
  let best: T | undefined = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) {
      best = item;
    }
  }
  return best;
}

const people = [
  { name: "Ann", age: 30, score: 8.5 },
  { name: "Bo", age: 25, score: 9.1 },
];
maxBy(people, "score");         // ✅
maxBy(people, "name");          // ❌ 'name' is a string, not a number
maxBy(people, "height");        // ❌ property 'height' is missing
```

The two errors differ: `"name"` exists but holds a string; `"height"` is missing altogether.

**Way 2: a helper type that lists the number keys**

```typescript
type NumberKeys<T> = { [P in keyof T]: T[P] extends number ? P : never }[keyof T];

type Person = { name: string; age: number; score: number };
type PN = NumberKeys<Person>;                       // "age" | "score"
const ok: PN = "age";
const bad: PN = "name";                             // ❌ not a number key

type NoNumbers = NumberKeys<{ a: string; b: boolean }>;   // never: nothing is a number
const none: NoNumbers = "a";                        // ❌ nothing can be assigned to never

function maxBy<T extends object, K extends NumberKeys<T>>(items: T[], key: K): T | undefined {
  let best: T | undefined = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) best = item;
  }
  return best;
}
const people: Person[] = [{ name: "Ann", age: 30, score: 8.5 }];
maxBy(people, "age");
maxBy(people, "name");                              // ❌ "name" is not in "age" | "score"
```

How `NumberKeys<Person>` is built, in three moves:

1. Loop over each key `P`. If its value type extends `number`, keep the key name; otherwise use `never`.
2. That gives `{ name: never; age: "age"; score: "score" }`.
3. `[keyof T]` reads all the values out as a union. `never` disappears from a union, leaving `"age" | "score"`.

If no property is a number, every value is `never`, so the result is `never` and no key can be passed.

### Why `maxBy` returns `| undefined`, and what happens if you drop it

The function returns `undefined` when the list is empty: the loop never runs, so `best` is never assigned.
If the list has at least one item, the first item always becomes `best`. TypeScript can't know whether the
list you pass is empty, so the honest return type is `T | undefined`.

```typescript
function maxBy<K extends string, T extends Record<K, number>>(items: T[], key: K): T | undefined {
  let best: T | undefined = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) best = item;
  }
  return best;
}
const people = [{ name: "Ann", age: 30 }, { name: "Bo", age: 25 }];
const oldest = maxBy(people, "age");
oldest.name;        // ❌ 'oldest' is possibly undefined
oldest?.name;       // ✅ undefined if there was no item
if (oldest) {
  oldest.name;      // ✅ narrowed to the person type
}
```

The same reason is behind `first<T>(arr: T[]): T | undefined` and `arr[0]` being `T | undefined` under
`noUncheckedIndexedAccess`: an empty array has no first or biggest element.

**If you leave `undefined` off the return type, the compiler refuses.**

```typescript
function maxBad<K extends string, T extends Record<K, number>>(items: T[], key: K): T {
  let best: T | undefined = undefined;
  for (const item of items) {
    if (best === undefined || item[key] > best[key]) best = item;
  }
  return best;      // ❌ Type 'T | undefined' is not assignable to type 'T'
}

function maxBad2<K extends string, T extends Record<K, number>>(items: T[], key: K): T {
  let best: T = items[0];   // ❌ items[0] is T | undefined under noUncheckedIndexedAccess
  for (const item of items) {
    if (item[key] > best[key]) best = item;
  }
  return best;
}
```

Writing `return best!` silences it, but on an empty list the caller then crashes later with
`Cannot read properties of undefined`, away from the real cause.

**The honest way to return a plain `T`:** throw when there is nothing to return.

```typescript
function maxOrThrow<K extends string, T extends Record<K, number>>(items: T[], key: K): T {
  let best = items[0];
  if (best === undefined) throw new Error("empty list");
  for (const item of items) {
    if (item[key] > best[key]) best = item;
  }
  return best;
}
console.log(maxOrThrow([{ a: 1 }, { a: 5 }], "a"));   // { a: 5 }
```

Pick `T | undefined` when an empty list is a normal case (like `Array.find`), and `T` plus a throw when an
empty list is a bug in the caller.

### `NumberKeys<Person>` is a type-level function call

`type PN = NumberKeys<Person>` does not make an object with Person's values. It calls a function on
types: `NumberKeys` takes `Person` in and hands back a new type, and `PN` is the name for the result.

```typescript
type NumberKeys<T> = { [P in keyof T]: T[P] extends number ? P : never }[keyof T];
type Person = { name: string; age: number; score: number };
type PN = NumberKeys<Person>;     // "age" | "score"

const a: PN = "age";       // ✅
const b: PN = "score";     // ✅
const c: PN = "name";      // ❌ name holds a string
const d: PN = 30;          // ❌ PN is made of key names, not values

type Product = { title: string; price: number; stock: number; inStock: boolean };
type PK = NumberKeys<Product>;    // "price" | "stock"
```

`PN` is a union of two string literals: the names of the properties that hold a number. Compare it with
a function: `double(5)` gives `10`, and `NumberKeys<Person>` gives `"age" | "score"`. `NumberKeys<T>` is the
function, `T` its parameter, `Person` the argument. The real values (30, 8.5) never appear, because this
all happens on types before the program runs.

### `StringKeys` and the general `KeysOfType`

Change the type after `extends`, or make it a second parameter.

```typescript
type StringKeys<T> = { [P in keyof T]: T[P] extends string ? P : never }[keyof T];
const k: StringKeys<{ name: string }> = "name";
const j: StringKeys<{ name: string; age: number }> = "age";   // ❌ only "name" is a string key

type KeysOfType<T, V> = { [P in keyof T]: T[P] extends V ? P : never }[keyof T];
type A = KeysOfType<{ a: string; b: number; c: number }, number>;    // "b" | "c"
type B = KeysOfType<{ a: string; b: number; c: boolean }, boolean>;  // "c"
const a1: A = "b";
const b1: B = "a";                                                    // ❌ "a" holds a string
```

`NumberKeys<T>` is `KeysOfType<T, number>`, and `StringKeys<T>` is `KeysOfType<T, string>`.

### `Record<K, V>` refresher

`Record<K, V>` is an object type whose keys are `K` and whose values all have type `V`. The first
parameter names the keys (joined with `|`); the second is the one value type shared by every key.
(The list of utility types is in §9.)

```typescript
type Difficulty = "easy" | "medium" | "hard";

const colours: Record<Difficulty, string> = { easy: "green", medium: "orange", hard: "red" };   // ✅
const missing: Record<Difficulty, string> = { easy: "green", medium: "orange" };                  // ❌ 'hard' is missing
const extra: Record<Difficulty, string> = { easy: "g", medium: "o", hard: "r", insane: "x" };     // ❌ 'insane' does not exist
const wrongValue: Record<Difficulty, string> = { easy: 1, medium: "o", hard: "r" };               // ❌ number is not a string
```

`Record<Difficulty, string>` is the same as `{ easy: string; medium: string; hard: string }`. Every key
must be present, no extras are allowed, and every value must match `V`. Add a fourth difficulty later
and every `Record<Difficulty, ...>` fails to compile until you give the new key a value.

Three uses:

```typescript
const lookup: Record<string, number> = { a: 1, b: 2 };
lookup["anything"] = 3;                       // ✅ with a plain string key, any key is allowed
const x = lookup["zzz"];                      // number | undefined under noUncheckedIndexedAccess

const y: Record<"age", number> = { age: 5 };  // same as { age: number }: a required property
```

- `Record<Union, V>` is a table with one entry per member of the union.
- `Record<string, V>` is a dictionary where the keys are not fixed.
- `Record<"one", V>` says "must have this property". In `T extends Record<K, number>` it means "T has a property called `K`, and it holds a number".

**The union is the list of keys, not "either a or b".** `Record<"a" | "b", boolean>` is the same as
`{ a: boolean; b: boolean }`, and both properties are required.

```typescript
type R1 = Record<"a" | "b", boolean>;
type R2 = { a: boolean; b: boolean };           // the same type

const y1: Record<"a" | "b", boolean> = { a: true };              // ❌ Property 'b' is missing
const y2: Record<"a" | "b", boolean> = { b: true };              // ❌ Property 'a' is missing
const y3: Record<"a" | "b", boolean> = { a: true, b: false };    // ✅
```

The "or" lives in a **value** type: `{ k: "a" | "b" }` means `k` holds one of two strings;
`Record<"a" | "b", boolean>` means two properties. `Record` takes exactly two things (the keys and one
value type), so it cannot describe an object whose keys hold different types.

TypeScript reports the first mistake it finds, so fixing one error can reveal the next:

```typescript
const w1: Record<"a" | "b", boolean> = { a: 1 };            // ❌ number is not boolean (b is also missing, not reported yet)
const w2: Record<"a" | "b", boolean> = { a: 1, b: true };   // ❌ still number is not boolean
const w3: Record<"a" | "b", boolean> = { a: true, b: false };   // ✅ both parts must be right
```

**All keys optional:** `Partial<Record<...>>` relaxes every key, including the ones you wanted required.

```typescript
const a: Partial<Record<"x" | "y" | "z", number>> = { x: 1, y: 2 };   // ✅
const b: Partial<Record<"x" | "y" | "z", number>> = {};              // ✅ nothing is required
const e: Record<"x" | "y" | "z", number> = { x: 1, y: 2 };           // ❌ without Partial, 'z' is missing
```

**Only `z` optional:** combine two types with `&`, a `Record` for the required keys and a small object
type for the optional one.

```typescript
type T = Record<"x" | "y", number> & { z?: number };

const c: T = { x: 1, y: 2 };          // ✅
const d: T = { x: 1 };                // ❌ Property 'y' is missing: x and y are still required
```

### Generic functions with callbacks: reading the signature

A function type as a parameter carries its own type parameters. In `applyTo<T, U>`, `T` is inferred from the
first argument, and `U` is inferred from what the callback returns.

```typescript
function applyTo<T, U>(value: T, fn: (v: T) => U): U {
  return fn(value);
}
const a = applyTo(5, (n) => String(n));       // U is string
const b = applyTo("hi", (s) => s.length);     // U is number
const c: number = applyTo(5, (n) => String(n));   // ❌ string is not a number
```

### `map`, `filter` and `find`

`map` changes the item's type, so it needs two type parameters. `filter` keeps each item as it is, so one is
enough: the predicate always returns `boolean`, which is fixed and needs no parameter. `find` returns an item
or nothing.

```typescript
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  const res: U[] = [];
  for (const item of arr) {
    res.push(fn(item));
  }
  return res;
}

function filter<T>(arr: T[], pred: (item: T) => boolean): T[] {
  const res: T[] = [];
  for (const item of arr) {
    if (pred(item)) res.push(item);
  }
  return res;
}

function find<T>(arr: T[], pred: (item: T) => boolean): T | undefined {
  for (const item of arr) {
    if (pred(item)) return item;
  }
  return undefined;
}

const lens = map(["a", "bb", "ccc"], (s) => s.length);                  // number[]  [1, 2, 3]
const strs = map([1, 2, 3], (n) => String(n));                          // string[]
const evens = filter([1, 2, 3, 4], (n) => n % 2 === 0);                 // number[]  [2, 4]
const firstBig = find([1, 5, 9], (n) => n > 4);                         // number | undefined  5
const chained = map(filter([1, 2, 3, 4], (n) => n > 1), (n) => n * 10); // [20, 30, 40]
const bad1: string[] = lens;                                            // ❌ lens is number[]
map([1, 2], (s: string) => s);                                          // ❌ the callback expects a string
filter(["a"], (n: number) => n > 1);                                    // ❌ same reason
```

Mistakes to avoid:

- **Reusing the parameter name for the result.** `let arr = []` inside a function whose parameter is `arr` is
  `Duplicate identifier 'arr'`, and the loop would run over the new empty list. Name the result `res` or `out`
  and give it a type (`const res: U[] = []`).
- **Hard-coding a concrete type in a generic function.** `find(...): number | undefined` fails with
  `Type 'T' is not assignable to type 'number | undefined'`. If the function returns an item, the return type
  has `T` in it.
- **Writing `if (pred(item) res.push(item)`.** The condition needs its own closing parenthesis.

### `every`, `some` and `count`

`every` stops at the first failure. Ask "is there an item that does NOT pass?" and return `false` as soon as you
find one. An empty list has no failing item, so `every` is `true`. The slow version tests every item and
builds a helper list of `true` values; the early return does the same job in fewer predicate calls.

```typescript
function every<T>(arr: T[], pred: (item: T) => boolean): boolean {
  for (const item of arr) {
    if (!pred(item)) return false;
  }
  return true;
}
function some<T>(arr: T[], pred: (item: T) => boolean): boolean {
  for (const item of arr) if (pred(item)) return true;
  return false;
}
function count<T>(arr: T[], pred: (item: T) => boolean): number {
  let n = 0;
  for (const item of arr) if (pred(item)) n++;
  return n;
}

every([2, 4], (n) => n % 2 === 0);      // true
every([2, 3], (n) => n % 2 === 0);      // false
every([], () => false);                  // true: nothing fails
let calls = 0;
every([1, 2, 3, 4, 5], (n) => { calls++; return n < 2; });
console.log(calls);                      // => 2
```

`some`, `count` and `every` have one type parameter. `T` appears only in the parameters, because the result
is `boolean` or `number`, not a `T`. Compare `find`, whose result is a `T`.

### `pluckAll`, `reduce`, `groupBy` and `partition`

```typescript
function pluckAll<T, K extends keyof T>(arr: T[], key: K): T[K][] {
  const out: T[K][] = [];
  for (const item of arr) out.push(item[key]);
  return out;
}

function reduce<T, A>(arr: T[], fn: (acc: A, item: T) => A, init: A): A {
  let acc = init;
  for (const item of arr) acc = fn(acc, item);
  return acc;
}

function groupBy<T, K extends string>(arr: T[], keyFn: (item: T) => K): Record<string, T[]> {
  const out: Record<string, T[]> = {};
  for (const item of arr) {
    const k = keyFn(item);
    (out[k] ??= []).push(item);
  }
  return out;
}

function partition<T>(arr: T[], pred: (item: T) => boolean): [T[], T[]] {
  const yes: T[] = [];
  const no: T[] = [];
  for (const item of arr) (pred(item) ? yes : no).push(item);
  return [yes, no];
}

const people = [{ name: "Ann", age: 30 }, { name: "Bo", age: 17 }, { name: "Cy", age: 45 }];
pluckAll(people, "name");                        // string[]  ["Ann", "Bo", "Cy"]
const ages: number[] = pluckAll(people, "age");  // ✅
const bad: string[] = pluckAll(people, "age");   // ❌ number[] is not string[]
pluckAll(people, "height");                      // ❌ not a key

reduce([1, 2, 3, 4], (sum, n) => sum + n, 0);                          // 10  (A = number)
reduce(["a", "bb"], (m, s) => m + s.length, 0);                        // 3   (T = string, A = number)
reduce(people, (names, p) => [...names, p.name], [] as string[]);      // A = string[]
groupBy(people, (p) => (p.age >= 18 ? "adult" : "minor"));             // { adult: [Ann, Cy], minor: [Bo] }
const [adults, minors] = partition(people, (p) => p.age >= 18);        // 2 and 1
```

In `reduce`, `A` is the accumulator type and can differ from `T`. It is inferred from `init`, which is why an
empty starting list needs `[] as string[]`.

### A generic interface and the classes that implement it

`implements Box<number>` **fixes** `T`, so the class has no type parameter of its own. `GenericBox<T>
implements Box<T>` **passes `T` through**, so the class is generic too. An interface can also be implemented
by a plain object.

```typescript
interface Box<T> { get(): T; set(v: T): void }

class NumBox implements Box<number> {
  constructor(private v: number) {}
  get(): number { return this.v; }
  set(v: number): void { this.v = v; }
}
class GenericBox<T> implements Box<T> {
  constructor(private v: T) {}
  get(): T { return this.v; }
  set(v: T): void { this.v = v; }
}

const nb = new NumBox(1);
nb.set(2);
nb.set("x");                       // ❌ string is not a number
const gb = new GenericBox("hi");   // T inferred as string
gb.set("yo");
gb.set(5);                         // ❌ number is not a string

interface Comparer<T> { compare(a: T, b: T): number }
const byLength: Comparer<string> = { compare: (a, b) => a.length - b.length };
byLength.compare("aa", "b");       // 1
```

### Generic classes: `Stack<T>` and `Queue<T>`

On a generic class, `T` is fixed when you create the instance (`new Stack<number>()`), and every method uses
that one `T`. A generic function picks `T` again on every call.

```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T): void {
    this.items.push(item);
  }
  pop(): T | undefined {
    return this.items.pop();
  }
  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
}

const s = new Stack<number>();
s.push(1);
s.push(2);
console.log(s.pop());       // => 2
s.push("three");            // ❌ a string is not a number
```

A **queue** has the same shape as a stack. The only difference is which end `dequeue` removes from: a stack
removes the **last** item added (`pop`, last in first out), a queue removes the **first** item added (`shift`,
first in first out). `enqueue` adds to the back with `push`.

```typescript
class Queue<T> {
  private items: T[] = [];

  enqueue(x: T): void {
    this.items.push(x);          // add to the back
  }

  dequeue(): T | undefined {
    return this.items.shift();   // remove from the front; undefined if empty
  }

  get size(): number {
    return this.items.length;
  }
}

const q = new Queue<number>();
q.enqueue(1);
q.enqueue(2);
console.log(q.dequeue());   // => 1
console.log(q.size);        // => 1
console.log(q.dequeue());   // => 2
console.log(q.dequeue());   // => undefined
q.enqueue("x");             // ❌ a string is not a number
```

Both classes return `T | undefined` on removal, because the array can be empty. Both keep `items` private, so
callers can only use the methods. `get size()` is a getter: read it as `q.size`, without parentheses. For
`[1, 2, 3]` (1 added first), one removal gives `3` from a stack and `1` from a queue. If `dequeue` used `pop`
instead of `shift`, it would be a stack. `shift()` is O(n) because the remaining items move one place; that is
fine for small queues, and a high-volume queue would keep a head index instead.

### A generic interface and an implementing class: `Repository<T>`

An interface is a contract with no code: anything that calls itself a `Repository<T>` must have these three
methods. `T` is the kind of thing it stores. A class that `implements` it promises to provide all three; if one
is missing the compiler says `Class 'X' incorrectly implements interface 'Repository<T>'. Property 'all' is missing`.

```typescript
interface Question {
  id: number;
  text: string;
  difficulty: "easy" | "medium" | "hard";
}

interface Repository<T> {
  findById(id: number): T | undefined;
  save(entity: T): T;
  all(): T[];
}

class InMemoryRepo<T extends { id: number }> implements Repository<T> {
  protected items: T[] = [];

  findById(id: number): T | undefined {
    for (const item of this.items) {
      if (item.id === id) return item;
    }
    return undefined;
  }

  save(entity: T): T {
    const i = this.items.findIndex((x) => x.id === entity.id);
    if (i === -1) {
      this.items.push(entity);       // new id: add it
    } else {
      this.items[i] = entity;        // same id: replace it
    }
    return entity;
  }

  all(): T[] {
    return [...this.items];          // a copy, so callers can't change the repo from outside
  }
}

class QuestionRepo extends InMemoryRepo<Question> {
  byDifficulty(d: Question["difficulty"]): Question[] {
    return this.items.filter((q) => q.difficulty === d);
  }
}

const repo = new QuestionRepo();
repo.save({ id: 1, text: "closure?", difficulty: "easy" });
repo.save({ id: 2, text: "event loop?", difficulty: "hard" });
repo.save({ id: 1, text: "closure? v2", difficulty: "easy" });   // replaces id 1
console.log(repo.all().length);                   // => 2
console.log(repo.findById(1)?.text);              // => closure? v2
console.log(repo.findById(9));                    // => undefined
console.log(repo.byDifficulty("hard").length);    // => 1

repo.save({ id: 3, text: "x", difficulty: "impossible" });   // ❌ not one of the three difficulties
new InMemoryRepo<{ name: string }>();                        // ❌ Property 'id' is missing
```

- **`T extends { id: number }` on the class, but not on the interface.** The interface never reads `id`, so it
  accepts any `T`. The class reads `x.id` in `findById` and `save`, so it needs the constraint; without it
  `x.id` fails with `Property 'id' does not exist on type 'T'`.
- **`protected items`** is like `private`, but subclasses such as `QuestionRepo` can use it too.
- **`save`** uses `findIndex`, which returns `-1` for "not found": `-1` means push, any other number means
  replace that position.
- **`all()` returns `[...this.items]`.** If it returned `this.items`, a caller doing `repo.all().pop()` would
  shrink the repo itself.
- **`QuestionRepo extends InMemoryRepo<Question>` fixes `T`**, so `QuestionRepo` has no type parameter of its
  own. It inherits `findById`, `save` and `all` and adds one method. This is the same "fix `T`" move as
  `class NumBox implements Box<number>`.

### Small generic helpers: `last`, `swap`, `unique`

```typescript
function last<T>(arr: T[]): T | undefined {
  return arr[arr.length - 1];       // an empty array gives arr[-1], which is undefined
}

function swap<T, U>(pair: [T, U]): [U, T] {
  return [pair[1], pair[0]];        // build a NEW pair; T and U come out in the opposite order
}

function unique<T>(arr: T[]): T[] {
  return [...new Set(arr)];
}

last([1, 2, 3]);               // 3
last([]);                      // undefined
swap([1, "a"]);                // ["a", 1], typed [string, number]
swap([1, 2, 3]);               // ❌ a 3-element tuple is not a [T, U] pair
const s: number[] = unique(["a"]);   // ❌ string[] is not number[]
```

- In `swap`, `T` is the type of the first element and `U` the type of the second. Writing `[pair[0], pair[1]] = [pair[1], pair[0]]`
  fails (`Type 'U' is not assignable to type 'T'`) and would also change the caller's array. Return a new pair.
- The `[T, U]` parameter type already rejects a non-pair at compile time, so a runtime `"not a pair"` check
  is dead code.
- `unique` with a `Set` is O(n). A `Set` treats `NaN` as equal to `NaN`, and compares objects by reference.

The loop version of `unique` needs **two** containers: a `Set<T>` to ask "have I met this?", and a `T[]` to
return in the original order.

```typescript
function uniqueLoop<T>(arr: T[]): T[] {
  const seen = new Set<T>();
  const result: T[] = [];
  for (const item of arr) {
    if (!seen.has(item)) {
      seen.add(item);               // Set uses add; an array uses push
      result.push(item);
    }
  }
  return result;
}
```

### `zip`, `mapValues`, `sortBy` and `countBy`

```typescript
function zip<T, U>(a: T[], b: U[]): [T, U][] {
  const result: [T, U][] = [];
  const n = Math.min(a.length, b.length);   // stop at the shorter list
  for (let i = 0; i < n; i++) {
    result.push([a[i] as T, b[i] as U]);    // safe: i < n, but the compiler can't prove it
  }
  return result;
}

function mapValues<T, U>(obj: Record<string, T>, fn: (v: T) => U): Record<string, U> {
  const out: Record<string, U> = {};
  for (const [key, value] of Object.entries(obj)) {
    out[key] = fn(value);
  }
  return out;
}

function sortBy<T, K extends keyof T>(arr: T[], key: K): T[] {
  return [...arr].sort((a, b) => {
    if (a[key] < b[key]) { return -1 }
    else if (a[key] > b[key]) { return 1 }
    else { return 0 }
  });
}

function countBy<T>(arr: T[], keyFn: (item: T) => string): Record<string, number> {
  const out: Record<string, number> = {};
  for (const item of arr) {
    const k = keyFn(item);
    out[k] = (out[k] ?? 0) + 1;
  }
  return out;
}

zip([1, 2, 3], ["a", "b"]);                          // [[1, "a"], [2, "b"]]
zip(1, ["a"]);                                       // ❌ a number is not an array
mapValues({ a: 1, b: 2 }, (n) => n * 10);            // { a: 10, b: 20 }
const people = [{ n: "Ann", a: 30 }, { n: "Bo", a: 25 }];
sortBy(people, "a").map((p) => p.n);                 // ["Bo", "Ann"]; people itself is unchanged
sortBy([{ n: "x" }], "age");                         // ❌ "age" is not a key
countBy(["apple", "avocado", "banana"], (w) => w[0] ?? "");   // { a: 2, b: 1 }
```

- **`zip` uses an index loop** because it needs the same position in two lists. `Math.min` gives the number
  of pairs. `as T` is a cast you can justify by the loop bound; compare `return best!` in `maxBy`, where the
  empty list really could reach it.
- **`mapValues` builds a new object.** Assigning `fn(value)` back into `obj` fails
  (`Type 'U' is not assignable to type 'T'`) and would change the caller's object.
- **`sortBy` sorts a copy.** `sort` changes the array it runs on, so copy with `[...arr]` first. For ascending
  order, `a < b` returns `-1` and `a > b` returns `1`; the opposite signs give descending. The condition after
  `if` needs parentheses.
- **`countBy` counts by the key from `keyFn`**, not by the item. `out[k] ?? 0` supplies the starting 0 for a
  key seen for the first time. A `Map<string, number>` works too; finish with `Object.fromEntries(map)`.

The pattern behind all of these: build a **new** result with its own type annotation, fill it from the
input, and return it. The input is never changed.

### TypeScript syntax cheat sheet: types, interfaces and generics

#### 1. `type` vs `interface`

```typescript
type UserType = { id: number; name: string };       // an object shape
interface UserInterface { id: number; name: string } // the same thing
type Id = number;                                    // only `type` can name these
type Level = "easy" | "hard";
type Pair = [number, string];
```

Object shape: either works. Use `interface` for objects, and `type` for everything else (unions, tuples, derived
types like `Partial<X>`).

The punctuation:

| Where | Separator | Example |
|---|---|---|
| `type X = ...` | the `=` is required | `type Id = number;` |
| `interface` / object type | `;` between fields | `{ id: number; name: string }` |
| object **value** | `,` between entries | `{ id: 1, name: "Ann" }` |
| variable | `: type = value` | `const u: UserType = {...}` |

#### 2. The model: `< >` are parentheses for types

| Values | Types |
|---|---|
| `function add(a, b)` declares parameters | `function first<T>` declares **type parameters** |
| `add(1, 2)` passes arguments | `first<number>(...)` passes **type arguments** |

Only two positions use `< >`.

**Position 1, declaring (creates the names):**

```typescript
function identity<T>(value: T): T { return value; }
interface Box<T> { value: T }
type Wrapper<T> = { inner: T };
class Stack<T> { items: T[] = []; }
type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };
```

**Position 2, using (supplies real types):**

```typescript
type UserType = { id: number; name: string };
interface Box<T> { value: T }
class Stack<T> { items: T[] = []; }
function identity<T>(value: T): T { return value; }

const x = identity<number>(5);
const bx: Box<string> = { value: "hi" };
const st = new Stack<number>();
const r1: Record<string, number> = { a: 1 };
const pr: Promise<string> = Promise.resolve("x");
type P = Pick<UserType, "id">;
```

Test for any `< >`: is a name being **created** (declare) or a type **supplied** (use)?

#### 3. Reading `<T, K extends keyof T>`

```typescript
function getKey<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: 1, name: "Ann" };
getKey(user, "name");     // ✅ typed string
getKey(user, "email");    // ❌ not a key of user: "name" | "id"
```

- The comma separates type parameters, just as it separates function parameters.
- `T` is any type.
- `K extends keyof T` is a rule on `K` only: it must be one of T's keys.
- The order doesn't matter (`<K extends keyof T, T>` also compiles), but `T` first is easier to read.

#### 4. A syntax drill, with the correct answers

```typescript
// 1. generic function: returns ONE item, not a list
function last<T>(arr: T[]): T | undefined {
  return arr[arr.length - 1];
}

// 2. generic interface: fields, not parameters
interface ApiResponse<T> {
  data: T;
  status: number;
}

// 3. generic type alias: declare <A, B> after the name, tuple is just [A, B]
type Pair<A, B> = [A, B];

// 4. a variable: the type, then = value
const scores: Record<string, number> = { math: 90, art: 85 };

// 5. Record with a union of keys: all keys required
const flags: Record<"dark" | "beta", boolean> = { dark: true, beta: false };

// 6. two type parameters with a constraint
function getKey<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

#### 5. `Record<K, V>`

`Record` takes **two** type arguments separated by a comma:

```typescript
type A = Record<string, number>;          // string keys, number values
type B = Record<"a" | "b", boolean>;      // keys are "a" and "b", both required
const bad1: Record<string> = {};          // ❌ Generic type 'Record' requires 2 type argument(s)
```

**Inside `< >` you only write types separated by commas. A colon or a semicolon is a sign you're in the wrong place.**

#### 6. The errors and what they mean

| Error message | What went wrong |
|---|---|
| `Generic type 'X' requires N type argument(s)` | you left out the `< >` or some of its arguments |
| `'=' expected` | you wrote `type Name: ...` instead of `type Name = ...` |
| `'>' expected` | a colon or similar sits inside `< >` |
| `must return a value` | the function has a return type but no `return` |
| `Type 'string' is not assignable to type 'number'` | a value or type is in the wrong slot (for example `Pair<number, string>` with `["a", 1]`) |

```typescript
interface Box<T> { value: T }
type Pair<A, B> = [A, B];
const bad2: Box = { value: 1 };                    // ❌ Generic type 'Box<T>' requires 1 type argument(s)
const bad3: Pair<number, string> = ["a", 1];       // ❌ the slots are in the wrong order
```

#### 7. Mistakes to recognise

| You wrote | Should be | Why |
|---|---|---|
| `type X: Foo` | `type X = Foo` | `type` needs `=` |
| `Omit<User, id>` | `Omit<User, "id">` | keys in `Omit`, `Pick` are strings |
| `{ a: 1; b: 2 }` as a value | `{ a: 1, b: 2 }` | values use commas |
| `age?: 40` in a value | `age: 40` | `?` is for types only |
| `new` as a variable name | any other name | `new` is reserved |
| `T[] \| undefined` for `last` | `T \| undefined` | returns one item |
| `{(data:T,status:number)}` in an interface | `{ data: T; status: number }` | fields, not parameters |
| `type Pair = (pair:[A,B])` | `type Pair<A, B> = [A, B]` | declare `<A, B>`; a tuple is just `[A, B]` |

## 9. Utility Types

Built-in type transformations. These are the ones you'll actually use.

```typescript
interface User { id: number; name: string; email: string; age?: number; }

Partial<User>                  // every property optional — PATCH payloads
Required<User>                 // every property required
Readonly<User>                 // every property readonly
Pick<User, "id" | "name">      // subset
Omit<User, "id">               // everything except — creating a new record
Record<string, number>         // { [k: string]: number }
Record<"a" | "b", User>        // exactly two keys

// Function and promise types
ReturnType<typeof getUser>     // what it returns
Parameters<typeof getUser>     // its params as a tuple
Awaited<Promise<User>>         // User — unwraps promises

// Union manipulation
Exclude<"a" | "b" | "c", "a">  // "b" | "c"
Extract<"a" | "b", "a" | "z">  // "a"
NonNullable<string | null>     // string
```

Real use:

```typescript
type CreateUser = Omit<User, "id" | "createdAt">;    // no id yet — server assigns it
type UpdateUser = Partial<CreateUser>;                // PATCH — any subset
type UserSummary = Pick<User, "id" | "name">;         // list view
```

Deriving these from one `User` rather than declaring four near-identical interfaces is the point.
One source of truth; change `User` and every derived type follows.

### `typeof` and `keyof` on values

```typescript
const config = { url: "/api", retries: 3 };
type Config = typeof config;                 // { url: string; retries: number }
type ConfigKey = keyof typeof config;        // "url" | "retries"
```

## 10. Classes in TypeScript

JavaScript classes (**JS §41**) plus access modifiers and a few conveniences.

```typescript
class BankAccount {
  private balance = 0;                  // TS-only — erased at compile time
  #realPrivate = 0;                     // JS private field — enforced at RUNTIME
  protected readonly owner: string;
  static count = 0;

  constructor(owner: string, private currency: string = "INR") {
    //                      ^^^^^^^ parameter property — declares AND assigns this.currency
    this.owner = owner;
    BankAccount.count++;
  }

  deposit(amount: number): this {       // `this` return type enables chaining
    if (amount <= 0) throw new RangeError("must be positive");
    this.balance += amount;
    return this;
  }

  get formatted(): string { return `${this.currency} ${this.balance}`; }
}

abstract class Shape {
  abstract area(): number;              // subclasses must implement
  describe(): string { return `Area: ${this.area()}`; }
}

class Circle extends Shape implements Comparable {
  constructor(private r: number) { super(); }
  area(): number { return Math.PI * this.r ** 2; }
}
```

⚠ **`private` is compile-time only.** It's erased, and at runtime the field is fully accessible —
`(acc as any).balance` reads it. `#field` is the real thing. Say this in an interview; it's a
frequent gotcha question.

**`implements` vs `extends`:** `implements` only checks that the shape matches — it inherits nothing.

## 11. Modules, Declaration Files, Third-Party Types

Module syntax is identical to ES modules (**JS §68**), plus:

```typescript
import type { User } from "./types";          // erased entirely — no runtime import
import { type User, getUser } from "./api";   // inline type import
export type { User };
```

`import type` matters: it guarantees the import disappears, avoiding circular-dependency problems and
accidental side effects from a module you only wanted a type from.

### Declaration files

`.d.ts` files carry types with no implementation.

```typescript
// types/global.d.ts
declare module "*.css";
declare module "untyped-lib" { export function doThing(x: string): number; }

declare global {
  interface Window { myApp: AppState; }
}
export {};                                     // makes the file a module
```

### Getting types for a library

1. Bundled — most modern packages ship their own. Nothing to do.
2. `@types/*` from DefinitelyTyped — `npm i -D @types/express`.
3. Neither — write a minimal `.d.ts` yourself, or `declare module "x";` to silence it as `any`.

## 12. `tsconfig.json` and `strict`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist"
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

**`strict: true` is the whole point.** It turns on:

| Flag | What it catches |
|---|---|
| `strictNullChecks` | ⭐ `null`/`undefined` must be handled explicitly |
| `noImplicitAny` | Untyped parameters become errors instead of silent `any` |
| `strictFunctionTypes` | Unsafe callback parameter variance |
| `strictPropertyInitialization` | Class fields never assigned |
| `strictBindCallApply` | Wrong args to `call`/`apply`/`bind` |
| `useUnknownInCatchVariables` | `catch (e)` is `unknown`, not `any` |

`strictNullChecks` alone is most of TypeScript's real-world value:

```typescript
const el = document.getElementById("app");
el.innerHTML = "";              // ❌ Object is possibly null
el?.innerHTML                   // ✅
if (!el) return;                // ✅ narrowed after this
```

**`noUncheckedIndexedAccess`** isn't in `strict` but should be on — it makes `arr[i]` return
`T | undefined`, which is the truth.

## 13. TypeScript with React

```tsx
// Props — an interface, destructured
interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: "primary" | "secondary";
  children?: React.ReactNode;
}

function Button({ label, onClick, variant = "primary" }: ButtonProps) {
  return <button className={variant} onClick={onClick}>{label}</button>;
}
```

**Don't use `React.FC`.** It adds an implicit `children` you may not want and complicates generics.
Annotate the props parameter, as above.

### Hooks

```tsx
const [count, setCount] = useState(0);                   // inferred number
const [user, setUser] = useState<User | null>(null);     // annotate when it starts null
const [items, setItems] = useState<Item[]>([]);          // annotate empty arrays

const inputRef = useRef<HTMLInputElement>(null);         // DOM refs
const timerRef = useRef<number | undefined>(undefined);  // mutable value refs

const memo = useMemo<Result>(() => compute(a, b), [a, b]);
const cb = useCallback((id: string) => select(id), []);

// Reducers — a discriminated union is exactly right here
type Action =
  | { type: "increment" }
  | { type: "set"; payload: number };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "increment": return state + 1;
    case "set":       return action.payload;
  }
}
```

`useState<User | null>(null)` is the annotation you'll write most — without it, TS infers `null` and
you can never set a user.

### Events

```tsx
const onChange = (e: React.ChangeEvent<HTMLInputElement>) => setValue(e.target.value);
const onSubmit = (e: React.FormEvent<HTMLFormElement>) => { e.preventDefault(); };
const onClick  = (e: React.MouseEvent<HTMLButtonElement>) => { … };
```

Let inference do it when the handler is inline: `onChange={e => …}` types `e` automatically.

### Async data — a discriminated union beats three booleans

```tsx
type State<T> =
  | { status: "loading" }
  | { status: "error"; error: Error }
  | { status: "success"; data: T };
```

That's §6's pattern applied to the most common React problem there is.

## 14. TypeScript with Node and Express

```bash
npm i -D typescript @types/node @types/express tsx
```

```typescript
import express, { Request, Response, NextFunction } from "express";

const app = express();

interface CreateUserBody { email: string; password: string; }

app.post("/api/v1/users",
  (req: Request<{}, {}, CreateUserBody>, res: Response) => {
    const { email, password } = req.body;      // typed
    res.status(201).json({ email });
  });

// Error middleware — four params, in this order
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
  res.status(500).json({ code: "INTERNAL", message: "Something went wrong" });
});
```

⚠ **`req.body` is `any` by default.** Express can't know the shape. Type the generic as above — and
still validate at runtime with Zod, because a type annotation checks nothing about the actual payload.

**Typed environment variables:**

```typescript
const env = z.object({
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
}).parse(process.env);                          // fails loudly at startup, not at 3am
```

## 15. Migrating JavaScript to TypeScript

The path that works, in order:

1. `npm i -D typescript && npx tsc --init`
2. Set `"allowJs": true`, `"strict": false`. Everything still compiles.
3. Rename **one leaf file** `.js` → `.ts`. Fix its errors. Commit.
4. Work upward through the dependency graph — leaves first, entry points last.
5. Once everything is `.ts`, turn on `strict` and fix in this order: `noImplicitAny`, then
   `strictNullChecks` (the big one), then the rest.
6. Ban `any` in review. `// @ts-expect-error` with a reason is acceptable; bare `any` isn't.

**Do not** rename everything at once and try to fix thousands of errors. That's how migrations get
abandoned.

## 16. The Twelve Traps

| # | Trap | Reality |
|---|---|---|
| 1 | Expecting runtime type checking | Types are **erased**. Validate at boundaries with Zod. |
| 2 | `any` to silence an error | It disables checking transitively. Use `unknown` and narrow. |
| 3 | `as` to force a type | An assertion, not a conversion. `{} as User` compiles and crashes later. |
| 4 | `private` means private | Compile-time only. `#field` is the runtime one. |
| 5 | `arr[10]` is safe | It's `T`, but at runtime it's `undefined`. Turn on `noUncheckedIndexedAccess`. |
| 6 | `catch (e)` gives an Error | It's `unknown`. Narrow with `e instanceof Error`. |
| 7 | Enums are free | `enum` emits real runtime code. Prefer `as const` unions. |
| 8 | Interfaces validate at runtime | They don't exist at runtime at all. |
| 9 | `useState(null)` then set an object | Inferred `null`. Write `useState<User \| null>(null)`. |
| 10 | Build passing = types correct | Bundlers strip types without checking. Run `tsc --noEmit`. |
| 11 | Over-annotating everything | Inference is better than you are. Annotate boundaries only. |
| 12 | `let x = "GET"` in a union slot | `let` widens to `string`. Use `const`, `as const`, or annotate. |

## 17. Cheat Sheet

**The mental model:** TypeScript is a linter with a very good memory. It runs before your code and
then vanishes.

**Annotate:** function params · non-obvious return types · uninitialised variables · `useState` that
starts `null` or empty. **Infer everything else.**

**`unknown` at every boundary** — `JSON.parse`, `fetch`, `localStorage`, `process.env`, form input.

**`strict: true`**, always. Plus `noUncheckedIndexedAccess`.

**Discriminated unions** for anything with modes — loading/error/success, action types, shape kinds.
Add `const _e: never = x` in the default case for exhaustiveness.

**`interface`** for object shapes and public APIs. **`type`** for unions, primitives, tuples, computed.

**Derive, don't duplicate:** `Omit`, `Pick`, `Partial`, `Record`, `ReturnType`, `z.infer`.

**Generics:** `<T extends { length: number }>` to constrain · `<T, K extends keyof T>(o: T, k: K): T[K]`
to index safely.

**`as const`** to get literal types and to derive a union from a runtime array.

**Never:** bare `any` · `as` to escape an error · trusting a type at a network boundary.

## 18. Practice

1. Convert five of your Week 1 JavaScript exercises to TypeScript. `strict: true`, zero `any`.
2. Type a `fetch` wrapper: generic over the response, `unknown` before narrowing, typed errors.
3. Model a form state as a discriminated union with exhaustive handling.
4. Write `getProp<T, K extends keyof T>` from memory. Then `pluck<T, K>(arr: T[], key: K): T[K][]`.
5. Build `CreateUser`, `UpdateUser` and `UserSummary` from one `User` using utility types only.
6. Type a React component with props, `useState<T | null>`, a typed ref, and a typed event handler.
7. Type an Express route end to end — body, params, query, response — then add Zod validation.
8. Take an untyped npm package and write a minimal `.d.ts` for the three functions you use.
9. Turn on `noUncheckedIndexedAccess` in an existing project and fix everything it finds.
10. Write the exhaustiveness-checking `never` pattern from memory, then add a union member and watch it fail.

---

## Sources

Written as a delta from `javascriptnotes/JAVASCRIPT-COMPLETE-NOTES.md` — every section there on
closures (§19), `this` (§37), prototypes (§40), classes (§41), async (§59–65) and modules (§68)
applies unchanged to TypeScript, and is not repeated here.

Cross-referenced against `java-springboot-complete-notes/JAVA-COMPLETE-NOTES.md` Part 16 for the
generics comparison — TypeScript's generics are structurally checked and fully erased, Java's are
nominally checked and also erased, which is why `List<String>` and `Array<string>` behave differently
than you'd expect coming from either direction.

React patterns cross-referenced against `REACT-COMPLETE-NOTES.md` Ch 5–7.

---

# Appendix A — 25 Days TypeScript Challenge (Days 2–13)

Transcribed from the infographic screenshots in `typescriptnotes/`. Kept in the original
day-by-day form. Overlaps with §1–§12 above are intentional — this is the spaced-repetition
pass, not a replacement.

## Day 2 — Setting Up TypeScript

Install, compile, run. TypeScript never runs directly; `tsc` transpiles it to JavaScript first.

```bash
npm install -g typescript   # 1. install globally
tsc -v                      # 2. verify
```

```ts
// 3. app.ts
let message: string = "Hello, TypeScript!";
console.log(message);
```

```bash
tsc app.ts    # 4. compile → app.js
node app.js   # 5. run → Hello, TypeScript!
```

Compilation flow: `app.ts` → `tsc` → `app.js`.

**Takeaway:** TypeScript must be compiled to JavaScript before it can run in the browser or Node.

## Day 3 — Basic Types

| Type | Represents | Example |
|---|---|---|
| `string` | textual data | `let name: string = "Basavaraju";` |
| `number` | integer or float | `let age: number = 21;` `let price: number = 99.99;` |
| `boolean` | true/false | `let isActive: boolean = true;` |
| `any` | any value at all | `let data: any = "Hello"; data = 100; data = true;` |
| `unknown` | like `any` but safe | `let value: unknown = "TypeScript";` — needs a type check before use |
| `void` | function returns nothing | `function greet(): void { console.log("Hi there!"); }` |
| `null` | intentional absence | `let empty: null = null;` |
| `undefined` | declared, not assigned | `let notAssigned: undefined = undefined;` |

```ts
let title: string = "TypeScript Basics";
let views: number = 1500;
let isPublished: boolean = true;
let author: string | null = "Basavaraju";
let rating: number | undefined;

console.log(title, views, isPublished, author, rating);
```

**Why types:** catch errors early, readable code, better DX, predictable code.

## Day 4 — Arrays & Tuples

```ts
// 1. type[] syntax
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["Basavaraju", "Priya", "Karthik"];
let isActive: boolean[] = [true, false, true];

// 2. Array<type> syntax
let scores: Array<number> = [85, 90, 95];
let cities: Array<string> = ["Chennai", "Coimbatore", "Bangalore"];
```

Common operations: `numbers.push(6)`, `numbers.pop()`, `numbers.length`, `numbers[0]`,
`numbers.forEach(n => console.log(n))`.

```ts
// Tuple — fixed length, positional types
let user: [number, string, boolean] = [1, "Basavaraju", true];
console.log(user[0]); // 1
console.log(user[1]); // Basavaraju
console.log(user[2]); // true

let product: [string, number, boolean] = ["Laptop", 55000, true];
```

Tuples: fixed length, ordered, different data types allowed, type-safe structure.

| Feature | Array | Tuple |
|---|---|---|
| Length | Dynamic | Fixed |
| Types | Same type | Different types allowed |
| Declaration | `let arr: number[]` | `let tup: [number, string]` |
| Use case | List of similar items | Fixed structure, multiple types |

**Takeaway:** arrays for a list of similar items; tuples for a fixed structure with different types.

## Day 5 — Type Aliases & Union Types

```ts
// Type aliases — a new name for an existing type
type UserId = number;
type UserName = string;
type IsActive = boolean;

let id: UserId = 101;
let name: UserName = "Basavaraju";
let active: IsActive = true;
```

```ts
// Union types — a value that can be one of several types
type ID = number | string;
type Status = "success" | "error" | "loading";
type User = { id: ID; name: string };

let id1: ID = 101;        // number
let id2: ID = "U101";     // string
let s1: Status = "success";
let s2: Status = "loading";
```

```ts
// Practical
type UserRole = "admin" | "editor" | "viewer";
type UserID = number | string;

type User = {
  id: UserID;
  name: string;
  role: UserRole;
  isActive: boolean;
};

const user1: User = { id: 1, name: "Basavaraju", role: "admin", isActive: true };
const user2: User = { id: "U102", name: "Priya", role: "editor", isActive: false };
```

| Feature | Type Aliases | Union Types |
|---|---|---|
| Purpose | New name for a type | Allow multiple types in a variable |
| Example | `type ID = number;` | `type ID = number \| string;` |
| Use case | Reusability, readability | Flexibility, multiple possibilities |
| Change impact | Easy to update everywhere | Used for different value types |

## Day 6 — Functions

```ts
// No params, no return
function sayHello(): void {
  console.log("Hello, TypeScript!");
}

// Typed params and return
function add(a: number, b: number): number {
  return a + b;
}
const result: number = add(10, 20); // 30

// Multiple params
function greet(name: string, age: number): string {
  return `Hi, I'm ${name} and I'm ${age} years old.`;
}

// Optional parameter — ?
function greetUser(name: string, age?: number): string {
  if (age) return `Hi ${name}, you are ${age} years old.`;
  return `Hi ${name}!`;
}
greetUser("Basu");      // Hi Basu!
greetUser("Basu", 21);  // Hi Basu, you are 21 years old.

// Default parameter
function power(base: number, exponent: number = 2): number {
  return Math.pow(base, exponent);
}
power(5);     // 25
power(5, 3);  // 125

// Practical
type User = { id: number; name: string; isActive: boolean };
function createUser(id: number, name: string, isActive: boolean = true): User {
  return { id, name, isActive };
}
```

`void` means the function doesn't return a value. `?` makes a parameter optional. A default
value is used when the argument is not provided.

**Takeaway:** Functions + Types = reusable, predictable, bug-free code.

## Day 7 — Object Types & Interfaces

```ts
// Inline object type — fine for small objects, not reusable
let user: { id: number; name: string; isActive: boolean } = {
  id: 1,
  name: "Basavaraju",
  isActive: true
};
```

```ts
// Interface — reusable across files, cleaner, supports advanced features
interface User {
  id: number;
  name: string;
  isActive: boolean;
}

let user: User = { id: 1, name: "Basavaraju", isActive: true };
```

```ts
// Optional and readonly
interface Product {
  id: number;
  name: string;
  price?: number;            // optional
  readonly createdAt: Date;  // cannot be reassigned
}

// Extending
interface Animal { name: string; }
interface Dog extends Animal { breed: string; }
```

```ts
// Practical
interface Employee {
  id: number;
  name: string;
  department?: string;
  readonly joinedAt: Date;
}
const emp: Employee = { id: 101, name: "Basu", joinedAt: new Date() };
console.log(emp);
```

`?` → optional property. `readonly` → prevents modification.

## Day 8 — Enums & Literal Types

```ts
// String enum
enum Role {
  Admin = "ADMIN",
  User  = "USER",
  Guest = "GUEST"
}
let userRole: Role = Role.Admin;
console.log(userRole); // ADMIN

// Numeric enum — auto-numbered from 0
enum Direction { Up, Down, Left, Right }
console.log(Direction.Up); // 0
```

```ts
// Literal types
let status: "success" | "error" | "loading";
status = "success";
// status = "pending"; // Error

type UserRole = "admin" | "user" | "guest";
let role: UserRole = "admin";
```

| Feature | Enums | Literal Types |
|---|---|---|
| Values | Named constants | Specific values (strings/numbers) |
| Readability | High (self-explanatory) | High (explicit values) |
| Use case | Fixed set of related values | Restrict a variable to certain values |
| Example | `enum Status { Active, Inactive }` | `type Status = "active" \| "inactive";` |

```ts
// Practical
enum PaymentMethod { Cash = "CASH", Card = "CARD", UPI = "UPI" }
type OrderStatus = "pending" | "success" | "failed";

let payment: PaymentMethod = PaymentMethod.UPI;
let status: OrderStatus = "pending";
```

Enums suit fixed sets like payment methods and roles; literal types suit allowing only specific values.

## Day 9 — Type Narrowing & Type Guards

Narrowing reduces a variable's type to something more specific inside a block.

```ts
type StringOrNumber = string | number;

function printValue(value: StringOrNumber) {
  if (typeof value === "string") {
    console.log(value.toUpperCase()); // string
  } else {
    console.log(value.toFixed(2));    // number
  }
}
printValue("Hello");
printValue(123.456);
```

Three built-in guards:

- `typeof` — primitives: `typeof value === "string"`
- `instanceof` — classes and objects: `value instanceof Date`
- `in` — property existence: `"name" in obj`

```ts
type Fish = { swim: () => void };
type Bird = { fly: () => void };
type Animal = Fish | Bird;

function move(animal: Animal) {
  if ("swim" in animal) {
    animal.swim();  // Fish
  } else {
    animal.fly();   // Bird
  }
}

// Custom type guard
function isFish(animal: Animal): animal is Fish {
  return (animal as Fish).swim !== undefined;
}
```

```ts
// Practical
type User  = { name: string; role: "admin" | "user" };
type Guest = { name: string; guest: true };
type Person = User | Guest;

function getRole(person: Person): string {
  if ("role" in person) return person.role;
  return "Guest";
}
getRole({ name: "Basu", role: "admin" }); // admin
getRole({ name: "Priya", guest: true });  // Guest
```

## Day 10 — Type Assertions & `keyof`

```ts
// Assertion — override the inferred type when you know better
let value: unknown = "Hello";
let length: number = (value as string).length;
console.log(length); // 5

// DOM
const input = document.getElementById("name") as HTMLInputElement;
console.log(input.value); // now TypeScript knows it's an input element
```

Uses the `as` keyword (or `<type>` syntax). It is not a replacement for proper type checking —
without the assertion TypeScript treats the element as a generic `HTMLElement` and won't allow `.value`.

```ts
// keyof — union of an object type's keys
type User = { id: number; name: string; email: string };
type UserKeys = keyof User;  // "id" | "name" | "email"

let key: UserKeys;
key = "name"; // valid
// key = "age"; // Error
```

```ts
// keyof + generics
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user: User = { id: 1, name: "Basu", email: "basu@gmail.com" };
getProperty(user, "name"); // Basu
```

```ts
// Practical
type Car = { brand: string; model: string; year: number };
type CarKeys = keyof Car;

function getCarValue(car: Car, key: CarKeys): string | number {
  return car[key];
}
getCarValue(car, "brand"); // "Toyota"
getCarValue(car, "year");  // 2022
```

**Takeaway:** type assertion tells TypeScript the exact type; `keyof` gets a union of object keys.
Together they make code flexible and safe — useful for APIs, dynamic forms, configs, reusable components.

## Day 11 — Generics

```ts
function identity<T>(value: T): T {
  return value;
}
identity<string>("Hello"); // Hello
identity<number>(123);     // 123
```

```ts
// Generic function over arrays
function getFirstElement<T>(arr: T[]): T {
  return arr[0];
}
const num = getFirstElement<number>([1, 2, 3]); // 1
const str = getFirstElement<string>(["a", "b", "c"]); // a
```

```ts
// Generic interface
interface ApiResponse<T> {
  data: T;
  message: string;
  status: boolean;
}

type User = { id: number; name: string };
const response: ApiResponse<User> = {
  data: { id: 1, name: "Basu" },
  message: "Success",
  status: true
};
```

```ts
// Generic class
class Box<T> {
  private value: T;
  constructor(value: T) { this.value = value; }
  getValue(): T { return this.value; }
}
const numBox = new Box<number>(100);
console.log(numBox.getValue()); // 100
```

Real-world use: API responses, data structures (lists, stacks, trees), React components, utility functions.

## Day 12 — Utility Types

Built-in types that build new types from existing ones.

```ts
type User = { id: number; name: string; email: string };
```

| Utility | Does | Example |
|---|---|---|
| `Partial<T>` | all properties optional | `type PartialUser = Partial<User>;` |
| `Required<T>` | all properties required | `type RequiredUser = Required<PartialUser>;` |
| `Readonly<T>` | all properties readonly | `type ReadonlyUser = Readonly<User>;` |
| `Pick<T, K>` | select specific properties | `type NameOnly = Pick<User, "name">;` |
| `Omit<T, K>` | remove specific properties | `type WithoutEmail = Omit<User, "email">;` |
| `Record<K, T>` | object type from keys and value type | `type RoleMap = Record<string, number>;` |

```ts
type UpdateUser       = Partial<User>;            // { id?: number; name?: string; email?: string }
type UserWithoutEmail = Omit<User, "email">;      // { id: number; name: string }
type ReadOnlyUser     = Readonly<User>;           // { readonly id: number; ... }
type UserRoles        = Record<"admin" | "user", number>; // { admin: number; user: number }
```

**When to use:** API responses, updating or patching data, reusable components, complex data
structures, large-scale applications.

## Day 13 — Advanced Functions & Function Types

```ts
// Function type annotation
const add: (a: number, b: number) => number = (a, b) => {
  return a + b;
};
console.log(add(5, 3)); // 8
```

```ts
// Overloading — multiple signatures, one implementation
function getData(id: number): string;
function getData(name: string): string;
function getData(param: number | string): string {
  return typeof param === "number"
    ? `User ID: ${param}`
    : `User Name: ${param}`;
}
getData(101);    // User ID: 101
getData("Basu"); // User Name: Basu
```

```ts
// Higher-order function
function multiplyBy(n: number) {
  return (x: number) => x * n;
}
const double = multiplyBy(2);
console.log(double(5)); // 10
```

```ts
// Function types via type alias
type MathOperation = (a: number, b: number) => number;
const add: MathOperation = (a, b) => a + b;
console.log(add(10, 20)); // 30

// …or via interface
interface Operation {
  (a: number, b: number): number;
}
const multiply: Operation = (a, b) => a * b;
console.log(multiply(6, 7)); // 42
```

```ts
// Practical
type ProcessData = (data: string) => string;
function processData(data: string, callback: ProcessData) {
  return callback(data.toUpperCase());
}
const result = processData("hello", (text) => `Processed: ${text}`);
console.log(result); // Processed: HELLO
```

Real-world uses: API calls and data fetching, event handling, callbacks and async functions,
reusable components, large-scale applications.

---

### Appendix A sources

13 screenshots in `typescriptnotes/` from the LinkedIn "25 Days TypeScript Challenge" series
by Basavaraju, Days 2–13 (Day 4 appears twice). Days 1 and 14–25 are not in the folder.
