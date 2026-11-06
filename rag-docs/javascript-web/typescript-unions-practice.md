---
title: typescript-unions-practice
topic: javascript-web
source_type: my-notes
source_file: STUDYNOTEs/concepts/typescript-unions-practice.md
---

# TypeScript Unions, Literals and Narrowing — Practice Questions

All of `ts-strict-demo/src/unions-narrowing.ts` as questions to answer before you look. Part 1 is unions, Part 2 is literal types, Part 3 is narrowing, Part 4 is the two compiler options (`strictNullChecks`, `noUncheckedIndexedAccess`).

## How to practice

1. Cover the answer. Read the **Describe** question and say the answer out loud or write it down.
2. Do the **Write** task by typing the code yourself, in `ts-strict-demo/src/practice.ts`. Start the file with `export {};`.
3. Check it with `cd ts-strict-demo && npx tsc -p strict-plus.json`. No output means it compiles.
4. A task that says **must fail** needs a `// @ts-expect-error` line above the broken line. If the line is not really an error, `tsc` tells you.
5. Open the answer and compare.

---

## The config files in `ts-strict-demo/`

Three small tsconfig files. Run one with `tsc -p <name>.json`. All three share `target: ES2022`, `module: ESNext`, `moduleResolution: bundler`, `noEmit`, `skipLibCheck` and `include: ["src"]`. They differ only in the strictness flags.

| File | What it is |
|---|---|
| `strict.json` | The strict baseline: `"strict": true`. Turns on `strictNullChecks`, `noImplicitAny`, `strictFunctionTypes`, `strictPropertyInitialization`, `strictBindCallApply` and more. |
| `strict-plus.json` | `strict.json` plus `"noUncheckedIndexedAccess": true`. `unions-narrowing.ts` is written for this one: `arr[0]` becomes `T \| undefined`. That flag is not part of `strict`, so you add it yourself. |
| `off.json` | The same options with `"strict": false`. With it, four of the ❌ lines in `unions-narrowing.ts` stop being errors, so `tsc` reports "Unused `@ts-expect-error`" for them. That is what strict catches. |

```json
// strict.json
{ "compilerOptions": { "target": "ES2022", "module": "ESNext", "moduleResolution": "bundler", "noEmit": true, "skipLibCheck": true, "strict": true }, "include": ["src"] }

// strict-plus.json
{ "compilerOptions": { "target": "ES2022", "module": "ESNext", "moduleResolution": "bundler", "noEmit": true, "skipLibCheck": true, "strict": true, "noUncheckedIndexedAccess": true }, "include": ["src"] }

// off.json
{ "compilerOptions": { "target": "ES2022", "module": "ESNext", "moduleResolution": "bundler", "noEmit": true, "skipLibCheck": true, "strict": false }, "include": ["src"] }
```

The `//` file-name lines above are labels for you, not valid JSON, so don't paste the block into a file as it is.

---

## Narrowing cheat sheet: what removes what

```text
typeof x === "string"    primitives             x instanceof Date     classes
"role" in obj            property presence      Array.isArray(x)      arrays
if (x)                   drops null/undefined/""/0/false
x === null / x !== undefined                    equality
if (!x) return / throw   early exit narrows the REST of the function
obj.kind === "a"         discriminated union    function isX(v): v is X   custom guard
assertX(v)               asserts v is X         x = value             assignment narrows
```

| Check | Type before | Type inside, after the check |
|---|---|---|
| `typeof x === "string"` | `string \| number` | `string` |
| `x instanceof Date` | `Date \| string` | `Date` |
| `"role" in obj` | `Admin \| Guest` | `Admin` (the one that has `role`) |
| `Array.isArray(x)` | `string \| string[]` | `string[]` |
| `if (x)` | `string \| null \| undefined` | `string` (it also drops `""`, `0` and `false`) |
| `x === null` / `x !== undefined` | `string \| null` | `null`, or `string` |
| `if (!x) return` or `throw` | `User \| undefined` | `User` for the rest of the function |
| `obj.kind === "a"` | a union where every member has a `kind` field | just the member whose `kind` is `"a"` |
| `function isX(v): v is X` | `unknown` | `X` (you wrote the check and the compiler trusts it) |
| `assertX(v)` | `unknown` | `X` after the call (it throws otherwise) |
| `x = value` | `string \| number` | the type of what you assigned |

---

## 1.1 Basic union

**Describe:** What does `string | number` mean? What can a variable of that type hold, and what can't it hold?

**Write:** Declare `id` as a string-or-number. Give it a number, then a string. Then add a third assignment that must fail.

<details>
<summary>Answer</summary>

`|` reads as "or". The variable can hold a `string` or a `number`, and nothing else.

```ts
let id: string | number = 101;
id = "A-101";        // ✅ string is allowed
id = true;           // ❌ boolean is not in the union
```

The error is: `Type 'boolean' is not assignable to type 'string | number'`.
</details>

---

## 1.2 Only the shared members are usable

**Describe:** Why can you call `.toString()` on a `string | number` but not `.toUpperCase()`?

**Write:** Write `shout(v: string | number)` that calls `v.toString()` (allowed) and `v.toUpperCase()` (must fail). Then write `shoutFixed` that returns the value as a string, uppercased if it is a string.

<details>
<summary>Answer</summary>

Before you narrow, TypeScript only lets you use what every member of the union has. `string` and `number` both have `toString`, but only `string` has `toUpperCase`. To use `toUpperCase` you check the type first.

```ts
function shout(v: string | number) {
  v.toString();      // ✅ both have it
  v.toUpperCase();   // ❌ number has no toUpperCase
}

function shoutFixed(v: string | number): string {
  if (typeof v === "string") return v.toUpperCase();   // v is string here
  return v.toFixed(0);                                  // v is number here
}
```
</details>

---

## 1.3 Union of arrays vs array of unions

**Describe:** What is the difference between `string[] | number[]` and `(string | number)[]`?

**Write:** Declare one variable that can hold `["x", 1]`, and one that is either an all-string array or an all-number array. Then try to put `["x", 1]` in the second one (must fail).

<details>
<summary>Answer</summary>

`(string | number)[]` is an array where each element can be a string or a number, so mixing is allowed. `string[] | number[]` is one array that is all strings or all numbers. The whole array is one kind.

```ts
const mixed: (string | number)[] = ["x", 1];     // ✅ each element may differ
const oneKind: string[] | number[] = ["x"];      // ✅ all strings
const bad: string[] | number[] = ["x", 1];       // ❌ a mix is neither
```
</details>

---

## 1.4 Union with `null`

**Describe:** Why does `s.split(" ")` fail when `s` is `string | null`? Which compiler option makes this an error?

**Write:** Write `firstWord(s: string | null): string` that returns the first word, or `""` when `s` is `null`. First write the broken version (must fail), then the fixed one.

<details>
<summary>Answer</summary>

`s` might be `null`, and `null` has no `.split`. The option is `strictNullChecks` (part of `strict`). Without it, `null` would be allowed everywhere and the crash would happen at runtime instead.

```ts
function firstWordBad(s: string | null): string {
  return s.split(" ")[0] ?? "";    // ❌ 's' is possibly 'null'
}

function firstWord(s: string | null): string {
  if (s === null) return "";       // handle null first
  return s.split(" ")[0] ?? "";    // s is string from here
}
```

The `?? ""` is there because `noUncheckedIndexedAccess` makes `split(" ")[0]` a `string | undefined`.
</details>

---

## 1.5 Union of objects

**Describe:** For a `Cat | Dog` value, which properties can you read without checking?

**Write:** Define `Cat` (`name`, `meow`) and `Dog` (`name`, `bark`). In `intro(p: Cat | Dog)`, read `p.name` (allowed), call `p.bark()` (must fail), then call `bark` safely using `in`.

<details>
<summary>Answer</summary>

Only the properties that every member has, here `name`. `bark` exists on `Dog` only, so it needs a check.

```ts
type Cat = { name: string; meow: () => void };
type Dog = { name: string; bark: () => void };

function intro(p: Cat | Dog) {
  p.name;                       // ✅ shared
  p.bark();                     // ❌ bark is not on Cat
  if ("bark" in p) p.bark();    // ✅ narrowed to Dog
}
```
</details>

---

## 1.6 Unions in parameters and return types

**Describe:** What does a return type of `number | null` tell the caller?

**Write:** Write `parseId(input: string): number | null` that returns `null` when the text is not a number. Then call it and add 1 to the result, once unsafely (must fail) and once safely.

<details>
<summary>Answer</summary>

It tells the caller "this might not produce a number, handle the `null`". The compiler forces the caller to check.

```ts
function parseId(input: string): number | null {
  const n = Number(input);
  return Number.isNaN(n) ? null : n;
}

const result = parseId("42");
result + 1;                          // ❌ 'result' is possibly 'null'
if (result !== null) result + 1;     // ✅ number here
```
</details>

---

## 1.7 Unions of unions and optional parameters

**Describe:** (a) If `Primitive = string | number | boolean` and `Value = Primitive | null | undefined`, how many members does `Value` have? (b) What is the type of `name` inside `function greet(name?: string)`?

**Write:** Define both types. Then write `greet(name?: string): string` that returns the name, or `"friend"` when it is missing. Inside it, copy `name` into a variable typed `string | undefined` to prove the types match.

<details>
<summary>Answer</summary>

(a) Five: `string | number | boolean | null | undefined`. A union inside a union flattens into one list.

(b) `string | undefined`. The `?` on a parameter adds `undefined`.

```ts
type Primitive = string | number | boolean;
type Value = Primitive | null | undefined;

function greet(name?: string): string {
  const n: string | undefined = name;   // ✅ identical type
  return n ?? "friend";
}
```
</details>

---

## 1.8 Put it together (uses a little narrowing)

**Write:** Write `formatId(id: string | number | null): string`. It returns `"none"` for `null`, the uppercased text for a string, and `ID-` followed by the number for a number.

<details>
<summary>Answer</summary>

```ts
function formatId(id: string | number | null): string {
  if (id === null) return "none";
  if (typeof id === "string") return id.toUpperCase();
  return `ID-${id}`;               // only number is left
}
```

Each check removes one member from the union. After `null` and `string` are handled, only `number` remains.
</details>

---

**Part 2: Literal types** (a type that is one exact value)

---

## 2.1 String, number and boolean literals

**Describe:** What is a literal type, and how is `"easy" | "medium" | "hard"` different from `string`?

**Write:** Define `Difficulty` and assign `"easy"` to a variable of that type, then assign `"expert"` (must fail). Define `Dice` as 1 to 6, assign 4, then assign 7 (must fail).

<details>
<summary>Answer</summary>

A literal type allows one exact value. `string` accepts any text. The union accepts only those three words, so a typo like `"midium"` is a compile error.

```ts
type Difficulty = "easy" | "medium" | "hard";
let d: Difficulty = "easy";
d = "expert";               // ❌ not one of the three

type Dice = 1 | 2 | 3 | 4 | 5 | 6;
const roll: Dice = 4;       // ✅
const badRoll: Dice = 7;    // ❌
```
</details>

---

## 2.2 `const` keeps the literal, `let` widens it

**Describe:** Why can `const k = "easy"` be used as a `Difficulty` but `let w = "easy"` can't?

**Write:** Declare both, then try to assign each to a `Difficulty` variable.

<details>
<summary>Answer</summary>

A `const` can never change, so TypeScript keeps the exact type `"easy"`. A `let` can be reassigned to any text, so TypeScript widens it to `string`, and `string` is wider than `Difficulty`. To keep it narrow, annotate it: `let w: Difficulty = "easy"`.

```ts
type Difficulty = "easy" | "medium" | "hard";
const k = "easy";                  // type "easy"
let w = "easy";                    // type string
const fromConst: Difficulty = k;   // ✅
const fromLet: Difficulty = w;     // ❌ string is wider than Difficulty
```
</details>

---

## 2.3 The object-property widening trap

**Describe:** Why does `send(req.method, req.url)` fail when `req = { method: "GET", url: "/q" }`? Name two fixes.

**Write:** Write `send(method: "GET" | "POST", url: string)`. Call it with a plain `req` object (must fail), then fix it two ways.

<details>
<summary>Answer</summary>

Properties of an object are mutable, so `method` is widened to `string`. Fix 1: `as const` freezes the whole object into readonly literals. Fix 2: `as const` on just the one property.

```ts
function send(method: "GET" | "POST", url: string) {
  return `${method} ${url}`;
}

const req = { method: "GET", url: "/q" };                   // method is string
send(req.method, req.url);                                  // ❌ string is not "GET" | "POST"

const reqConst = { method: "GET", url: "/q" } as const;     // every property readonly + literal
send(reqConst.method, reqConst.url);                        // ✅

const reqOne = { method: "GET" as const, url: "/q" };       // freeze only method
send(reqOne.method, reqOne.url);                            // ✅
```
</details>

---

## 2.4 `as const` array into a union

**Describe:** How do you get a union type out of an array that also exists at runtime? Why is that better than writing the union and the array separately?

**Write:** Create `LEVELS` with `"easy"`, `"medium"`, `"hard"`. Derive a `Level` type from it. Write a guard `isLevel(x: string): x is Level`. Assign a bad value to `Level` (must fail).

<details>
<summary>Answer</summary>

`as const` makes the array a readonly tuple of literals, and `(typeof LEVELS)[number]` reads out its element types as a union. One list feeds both the runtime and the type, so they can't drift apart.

```ts
const LEVELS = ["easy", "medium", "hard"] as const;
type Level = (typeof LEVELS)[number];       // "easy" | "medium" | "hard"

function isLevel(x: string): x is Level {
  return (LEVELS as readonly string[]).includes(x);
}

const l: Level = "easy";      // ✅
const m: Level = "expert";    // ❌
```
</details>

---

## 2.5 A literal union as the keys of a `Record`

**Describe:** What happens if a `Record<Difficulty, string>` is missing a key? Why is that useful?

**Write:** Build a colour map for all three difficulties, then one that forgets `hard` (must fail).

<details>
<summary>Answer</summary>

It is a compile error. If you add a fourth difficulty later, every `Record` keyed by it fails until you add the new key. Your `DifficultyBadge` colour map in `study-agent-ui` works this way.

```ts
type Difficulty = "easy" | "medium" | "hard";
const colours: Record<Difficulty, string> = { easy: "green", medium: "orange", hard: "red" };   // ✅
const missing: Record<Difficulty, string> = { easy: "green", medium: "orange" };                // ❌ "hard" is missing
```
</details>

---

## 2.6 Template literal types

**Describe:** What does `` `${Difficulty}-badge` `` build?

**Write:** Define `BadgeClass` from `Difficulty`. Assign `"easy-badge"`, then `"expert-badge"` (must fail).

<details>
<summary>Answer</summary>

It builds a new union by combining each member: `"easy-badge" | "medium-badge" | "hard-badge"`.

```ts
type Difficulty = "easy" | "medium" | "hard";
type BadgeClass = `${Difficulty}-badge`;
const ok: BadgeClass = "easy-badge";       // ✅
const bad: BadgeClass = "expert-badge";    // ❌
```
</details>

---

**Part 3: Narrowing** (the compiler follows your checks)

---

## 3.1 `typeof`

**Describe:** What does `typeof v === "string"` do to the type of `v` inside the `if`? Why doesn't `typeof v === "object"` remove `null`?

**Write:** Write `format(v: string | number | boolean | null | undefined): string`: uppercase a string, `toFixed(2)` a number, `"yes"`/`"no"` for a boolean, `"empty"` otherwise. Then write `nullTrap(v: object | null)` that checks `typeof v === "object"` and calls `v.toString()` (must fail).

<details>
<summary>Answer</summary>

Inside the `if`, `v` is only that type, and the other members are removed. `typeof null` is `"object"` in JavaScript, so that check still allows `null` through.

```ts
function format(v: string | number | boolean | null | undefined): string {
  if (typeof v === "string") return v.toUpperCase();
  if (typeof v === "number") return v.toFixed(2);
  if (typeof v === "boolean") return v ? "yes" : "no";
  return "empty";                       // only null | undefined are left
}

function nullTrap(v: object | null) {
  if (typeof v === "object") {
    v.toString();                       // ❌ v may still be null
  }
}
```
</details>

---

## 3.2 Truthiness

**Describe:** What does `if (s)` remove from `string | null | undefined`? What is the trap with numbers?

**Write:** Write `len(s: string | null | undefined): number`. Then write `wrongCount` and `rightCount` for `number | undefined`, where `0` is a valid count.

<details>
<summary>Answer</summary>

`if (s)` removes `null`, `undefined`, and also `""`, `0` and `false`. The trap is that a real `0` or empty string is thrown away too. Compare with `!== undefined` when `0` is valid.

```ts
function len(s: string | null | undefined): number {
  if (s) return s.length;
  return 0;
}

function wrongCount(count: number | undefined): number {
  if (count) return count;                // 0 is falsy: a real 0 falls through to -1
  return -1;
}

function rightCount(count: number | undefined): number {
  if (count !== undefined) return count;  // 0 survives
  return -1;
}
```
</details>

---

## 3.3 Equality

**Describe:** If `a: string | number` and `b: string | boolean`, what is the type of `a` inside `if (a === b)`?

**Write:** Write `sameType` using that check, and `notNull(x: string | null): number` that returns the length or 0.

<details>
<summary>Answer</summary>

`string`. They can only be equal if they share a type, and `string` is the only type the two unions have in common.

```ts
function sameType(a: string | number, b: string | boolean) {
  if (a === b) {
    const onlyString: string = a;       // the only type both share
    return onlyString;
  }
  return null;
}

function notNull(x: string | null): number {
  if (x !== null) return x.length;
  return 0;
}
```
</details>

---

## 3.4 `in`

**Describe:** What does `"permissions" in u` check, and how does it narrow?

**Write:** Define `Admin` (`name`, `permissions: string[]`) and `Guest` (`name`, `visitedFrom: string`). Write `info(u: Admin | Guest)` that returns the permission count for an admin and `visitedFrom` for a guest.

<details>
<summary>Answer</summary>

It checks that the property exists on the object. The compiler keeps the union members that have it inside the `if`, and the rest after.

```ts
type Admin = { name: string; permissions: string[] };
type Guest = { name: string; visitedFrom: string };

function info(u: Admin | Guest) {
  if ("permissions" in u) return u.permissions.length;   // Admin
  return u.visitedFrom;                                   // Guest
}
```
</details>

---

## 3.5 `instanceof`

**Describe:** When do you use `instanceof` instead of `typeof`?

**Write:** Write `when(date: Date | string): string` and `errorMessage(e: unknown): string`.

<details>
<summary>Answer</summary>

`typeof` only tells apart primitives. For classes (`Date`, `Error`, your own), use `instanceof`. It is the standard way to narrow a caught error from `unknown`.

```ts
function when(date: Date | string): string {
  if (date instanceof Date) return date.toISOString();
  return date;
}

function errorMessage(e: unknown): string {
  if (e instanceof Error) return e.message;
  return String(e);
}
```
</details>

---

## 3.6 `Array.isArray`

**Describe:** Why is `typeof x === "object"` a bad way to tell an array from a non-array?

**Write:** Write `toList(x: string | string[]): string[]` that always returns an array.

<details>
<summary>Answer</summary>

`typeof` an array is `"object"`, just like `null` and plain objects. `Array.isArray` is the check TypeScript understands.

```ts
function toList(x: string | string[]): string[] {
  return Array.isArray(x) ? x : [x];
}
```
</details>

---

## 3.7 Early return or throw

**Describe:** What does `if (!user) throw ...` do to the rest of the function?

**Write:** Write `userName(user: { name: string } | undefined): string` that throws when the user is missing.

<details>
<summary>Answer</summary>

After the line, the compiler knows `user` is defined for the rest of the function, because the missing case already left. This is the guard clause pattern, and it is why `App.tsx` has `if (!question) return ...`.

```ts
function userName(user: { name: string } | undefined): string {
  if (!user) throw new Error("no user");
  return user.name;                     // user is defined from here
}
```
</details>

---

## 3.8 Assignment narrows

**Describe:** If `let v: string | number = "hi"`, what type does `v` have on the next line?

**Write:** Call `v.toUpperCase()`, assign `v = 5`, then call `v.toFixed()`.

<details>
<summary>Answer</summary>

The assignment narrows it to what you assigned: `string` after `"hi"`, then `number` after `5`.

```ts
let v: string | number = "hi";
v.toUpperCase();   // ✅ narrowed to string by the assignment
v = 5;
v.toFixed();       // ✅ now number
```
</details>

---

## 3.9 `typeof` "function"

**Describe:** How do you safely call a value that is `(() => void) | string`?

**Write:** Write `run(cb: (() => void) | string)` that calls `cb` only when it is a function.

<details>
<summary>Answer</summary>

Check `typeof cb === "function"`. Inside the `if`, `cb` is the function type and you can call it.

```ts
function run(cb: (() => void) | string) {
  if (typeof cb === "function") cb();
}
```
</details>

---

## 3.10 Discriminated unions and exhaustiveness

**Describe:** What is a discriminated union? What does the `never` check in the `default` branch give you?

**Write:** Define `Shape` as circle (`radius`), rect (`w`, `h`) and tri (`base`, `height`), each with a `kind`. Write `area(s: Shape)` with a `switch` and an `assertNever` default. Then write `areaBroken` that forgets `tri` (must fail).

<details>
<summary>Answer</summary>

Every member has a shared literal field (the discriminant, here `kind`). Checking it narrows the whole object, so `s.radius` only exists in the `"circle"` case. In `default`, if every case is handled `s` is `never`. If you forget a case, `s` is not `never`, and `assertNever(s)` becomes a compile error naming the missing case.

```ts
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rect"; w: number; h: number }
  | { kind: "tri"; base: number; height: number };

function assertNever(x: never): never {
  throw new Error(`unhandled: ${JSON.stringify(x)}`);
}

function area(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2;
    case "rect":   return s.w * s.h;
    case "tri":    return (s.base * s.height) / 2;
    default:       return assertNever(s);
  }
}

function areaBroken(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2;
    case "rect":   return s.w * s.h;
    default:       return assertNever(s);   // ❌ "tri" is not handled
  }
}
```
</details>

---

## 3.11 The project one: `LoadState`

**Describe:** Why is `{ status: "loading" } | { status: "error"; message: string } | { status: "ready"; questions: Question[] }` better than one object with optional `data`, `error` and `loading` fields?

**Write:** Define `LoadState`. Write `describe(s: LoadState): string`. Then try to build `{ status: "loading", questions: [] }` (must fail).

<details>
<summary>Answer</summary>

With optional fields every combination is allowed, including impossible ones like loading with an error. The union only allows the three valid shapes, so impossible states can't be built.

```ts
type Difficulty = "easy" | "medium" | "hard";
type Question = { text: string; difficulty: Difficulty };

type LoadState =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "ready"; questions: Question[] };

function assertNever(x: never): never {
  throw new Error(`unhandled: ${JSON.stringify(x)}`);
}

function describe(s: LoadState): string {
  switch (s.status) {
    case "loading": return "Loading…";
    case "error":   return `Failed: ${s.message}`;
    case "ready":   return `${s.questions.length} questions`;
    default:        return assertNever(s);
  }
}

const impossible: LoadState = { status: "loading", questions: [] };   // ❌ loading has no questions
```
</details>

---

## 3.12 Custom type guards

**Describe:** What does `x is Question` promise? What is the risk?

**Write:** Write `isQuestion(x: unknown): x is Question`. Then use a guard inside `.filter` to turn `(string | number | null)[]` into `string[]`, and into `(string | number)[]`. Then write the same two filters again without the explicit guard. Finally, find a condition where leaving the guard out stops working.

<details>
<summary>Answer</summary>

It is a promise you make to the compiler: "when this returns true, `x` is a `Question`". The compiler does not check your logic, so a wrong guard is as dangerous as `any`. A guard in `.filter` changes the element type of the result.

With TypeScript 5.5 and later (your demo has 5.9.3), the compiler works out the guard itself for a simple one-condition check, so you can leave it out. That is the safer choice, because the type comes from the condition and not from what you typed. For a complicated condition it cannot infer the guard, and you must write it yourself.

```ts
type Question = { text: string; difficulty: string };

function isQuestion(x: unknown): x is Question {
  return typeof x === "object" && x !== null && "text" in x && "difficulty" in x;
}

const mixed: (string | number | null)[] = ["a", 1, null, "b"];

// Explicit guard: you write the promise
const onlyStrings = mixed.filter((x): x is string => typeof x === "string");     // string[]
const noNulls = mixed.filter((x): x is string | number => x !== null);          // (string | number)[]

// Inferred guard (TypeScript 5.5+): the compiler derives it from the condition
const onlyStrings2 = mixed.filter(x => typeof x === "string");                   // string[]
const noNulls2 = mixed.filter(x => x !== null);                                   // (string | number)[]

// A complicated condition is NOT inferred: the type stays (string | number | null)[]
const notNullOrA = mixed.filter(x => x !== null && x !== "a");
const stillNullable: (string | number)[] = notNullOrA;     // ❌ the compiler could not infer the guard

// So here you write the guard yourself
const cleaned = mixed.filter((x): x is string | number => x !== null && x !== "a");   // (string | number)[]
```

Use the explicit form when the condition is complicated, when you are writing a reusable helper like `isQuestion`, or when the code must compile on a TypeScript older than 5.5.
</details>

---

## 3.13 Assertion functions

**Describe:** How is `asserts x is string` different from a normal guard returning `x is string`?

**Write:** Write `assertIsString(x: unknown): asserts x is string` that throws if it isn't. Use it in `useIt(value: unknown)` and call `.toUpperCase()` after.

<details>
<summary>Answer</summary>

A normal guard returns a boolean that you test in an `if`. An assertion function throws when the check fails, so everything after the call is narrowed, with no `if` needed.

```ts
function assertIsString(x: unknown): asserts x is string {
  if (typeof x !== "string") throw new Error("not a string");
}

function useIt(value: unknown) {
  assertIsString(value);
  return value.toUpperCase();     // value is string from here
}
```
</details>

---

## 3.14 Narrowing `unknown`

**Describe:** Why is `JSON.parse` result best typed as `unknown`? What checks do you need before reading `.name`?

**Write:** Write `readName(json: string): string` that parses the text and returns `name` only if it is a string, otherwise throws.

<details>
<summary>Answer</summary>

You don't know the shape of outside data, so `unknown` forces you to check it before use. You need to check it is a non-null object, that `"name"` exists, and that it is a string.

```ts
function readName(json: string): string {
  const data: unknown = JSON.parse(json);
  if (typeof data === "object" && data !== null && "name" in data && typeof data.name === "string") {
    return data.name;
  }
  throw new Error("bad shape");
}
```
</details>

---

## 3.15 Narrowing and callbacks

**Describe:** When does narrowing survive inside a callback, and when is it lost?

**Write:** Write `constKeeps` that narrows a `const` and uses it in a `.map` callback. Write `letLoses` that narrows a `let`, creates a function using it, and then reassigns the `let` (must fail).

<details>
<summary>Answer</summary>

A `const` can't change, so the narrowing is safe inside callbacks. A `let` that is reassigned later might be different when the callback runs, so TypeScript drops the narrowing.

```ts
function constKeeps(maybe: string | undefined) {
  const s = maybe;
  if (s !== undefined) {
    return ["a"].map(() => s.length);   // ✅ const: narrowing survives
  }
  return [];
}

function letLoses(maybe: string | undefined) {
  let s = maybe;
  if (s !== undefined) {
    const f = () => s.length;           // ❌ s is reassigned below, so narrowing is lost
    s = undefined;
    return f;
  }
  return undefined;
}
```
</details>

---

## 3.16 `?.`, `??` and `!` are not narrowing

**Describe:** What does `!` do? How is it different from a check?

**Write:** Write `email(u: Profile | undefined): string` using `?.` and `??`. Write `focusIt(el: HTMLElement | null)` using `!`.

<details>
<summary>Answer</summary>

`?.` stops at `undefined` safely and `??` gives a fallback. `!` just tells the compiler "trust me, it isn't null". It checks nothing, so it crashes at runtime if you're wrong.

```ts
type Profile = { profile?: { email?: string } };

function email(u: Profile | undefined): string {
  return u?.profile?.email ?? "no email";    // ✅ safe chain with a fallback
}

function focusIt(el: HTMLElement | null) {
  el!.focus();     // "!" is not narrowing: it crashes at runtime if el is null
}
```
</details>

---

**Part 4: The two compiler options**

---

## 4.1 `strictNullChecks`

**Describe:** What error does `let x: string = null` give? What do you change to allow `null`?

**Write:** Write the failing line, then the fixed one.

<details>
<summary>Answer</summary>

The error is `Type 'null' is not assignable to type 'string'.` Add `null` to the type. With the option off, there is no error and the crash happens at runtime.

```ts
let x: string = null;            // ❌ Type 'null' is not assignable to type 'string'
let y: string | null = null;     // ✅
```
</details>

---

## 4.2 `noUncheckedIndexedAccess`

**Describe:** With this option on, what is the type of `arr[0]`? Is `??` the only way to handle it?

**Write:** Take `words = "hello world".split(" ")`. Show the unsafe use (must fail), then four safe ways, then one way that avoids indexing.

<details>
<summary>Answer</summary>

`arr[0]` becomes `string | undefined`, because the index might be out of range. `??` is only one of the ways. You can give a fallback, check, use `?.`, or assert with `!`. Or avoid indexing with `for...of` or `.map`, which give a plain `string`.

```ts
const words = "hello world".split(" ");

const a = words[0];                      // string | undefined
a.toUpperCase();                         // ❌ 'a' is possibly 'undefined'

const first = words[0] ?? "";            // 1. fallback
const w = words[1];
if (w !== undefined) w.toUpperCase();    // 2. check
words[0]?.toUpperCase();                 // 3. optional call
words[0]!.toUpperCase();                 // 4. "trust me"
for (const word of words) word.toUpperCase();   // 5. no indexing, plain string
```
</details>

---

## Redo from memory (22:00)

Close the notes and answer without looking:

**Unions**
1. What does `|` mean in a type?
2. Why can't you call `.toUpperCase()` on `string | number`?
3. What is the difference between `string[] | number[]` and `(string | number)[]`?
4. Which compiler option makes `string | null` dangerous to use unchecked?
5. What type does an optional parameter `name?: string` have inside the function?

**Literals**
6. Why does `const k = "easy"` work as a `Difficulty` but `let w = "easy"` doesn't?
7. How do you get a union type out of a runtime array?
8. What happens when a `Record<Difficulty, string>` is missing a key?

**Narrowing**
9. Why does `typeof v === "object"` not remove `null`?
10. Why is `if (count)` wrong when `0` is a valid count?
11. What does the `never` check in a `switch` default give you?
12. What does `x is T` promise, and what is the risk?
13. When does narrowing survive inside a callback?

**Options**
14. What error does `let x: string = null` give?
15. Name three ways to handle `arr[0]` being `string | undefined`.
