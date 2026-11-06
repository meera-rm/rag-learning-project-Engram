---
title: DSA-COMPLETE-NOTES
topic: dsa
source_type: my-notes
source_file: STUDYNOTEs/DSA-COMPLETE-NOTES.md
---

# DSA — Complete Notes, Solved in JavaScript, Python and Java

> One pattern per part. Every problem solved three times — JavaScript, Python, Java — because the
> algorithm is the same and only the idioms differ, and seeing that is half the point.
> Companion to `STUDY-GUIDE-DAILY-TRACKS.md`, where this is the 08:00 block, every day, for twelve weeks.

**Which language to interview in:** Python. Least syntax between you and the idea. Java is here
because `user-service` is Java and some companies mandate it. JavaScript is here because it's the
language you'll be strongest in by November and because frontend screens will demand it.

---

## How to use this file

Do **not** read it front to back. It's a reference organised by pattern, and patterns are learned by
solving, not reading.

Each morning, starting 08:00:
1. Read the pattern's **"When to reach for it"** section — 5 minutes.
2. Read the **template** — 5 minutes.
3. Solve the day's problem yourself, timed, in Python. **45 minutes.**
4. *Then* read this file's solution. Compare. Note the difference.
5. Re-implement in JS and Java from memory — 10 minutes. This is fast because the algorithm is
   already in your head; you're only translating idioms.

The three-language pass is not busywork. It forces you to separate *the algorithm* from *the syntax*,
which is exactly the separation an interview tests.

### Table of contents

**Part 0 — Foundations**
0. Logic Before DSA — the Seven Steps, stuck strategies, trace tables
1. The Method — six steps, every problem
2. Complexity — Big-O in practice
3. Data Structures — the eight that matter
4. Language Idioms Side by Side

**Part 1 — The Twelve Patterns**
5. Arrays & Hashing
6. Two Pointers
7. Sliding Window
8. Stack
9. Binary Search
10. Linked List
11. Trees
12. Heap & Intervals
13. Backtracking
14. Graphs
15. Dynamic Programming
16. Prefix Sum
17. Bit Manipulation
18. Fast and Slow Pointers
19. Monotonic Queue
20. Greedy
21. Divide and Conquer, Sorting, and the Master Theorem
22. Union-Find (Disjoint Set Union)
23. Trie (Prefix Tree)
24. Matrix Traversal
25. The 25-Pattern Map

**Part 2 — Reference**
26. Pattern Recognition — Signal → Pattern
27. The 55-Problem Tracker
28. Interview Communication

---
---

# Part 0 — Foundations

## 0. Logic Before DSA — Work It Out on Paper First

Patterns are the layer *above* this. Before you can recognise that a problem is a stack problem, you
have to be able to solve one small case by hand and notice what you did. That skill is separate, it's
trainable, and it's the one most people skip.

### The Seven Steps

From Duke's Programming Fundamentals course. **Steps 1–4 happen on paper. Never start at step 5.**

| # | Step | What it means |
|---|---|---|
| 1 | **Solve one small example by hand** | Take `"([)]"` and check it yourself. No code. |
| 2 | **Write down exactly what you did** | *"Saw `(`, remembered it. Saw `[`, remembered it. Saw `)`, but the last one I remembered was `[`, so it's invalid."* |
| 3 | **Generalise** | *"A closer must match the most recent opener."* That's a stack — and you found it yourself, rather than recalling it. |
| 4 | **Test the steps by hand on edge cases** | Empty input, one item, duplicates, zero or negatives. |
| 5 | **Write the code** | Now syntax is the easy part. |
| 6 | **Run the tests** | |
| 7 | **Debug by tracing** | Not by guessing and re-running. |

The whole point of steps 1–3: **your hand solution already contains the algorithm.** Writing it down
makes the hidden steps visible so you can generalise them. Jumping to step 5 means writing code for an
algorithm you haven't worked out yet, which is why it feels like staring at a blank editor.

### What to do when stuck

From *Think Like a Programmer* by V. Anton Spraul.

| Strategy | What it means | Example |
|---|---|---|
| **Have a plan** | Always know your next move, even if it's "try a tiny example" | Act instead of staring |
| **Restate it** | Rewrite the problem in your own words and name the exact output | Two Sum becomes *"for each number, does its partner exist?"* |
| **Divide it** | Split into subproblems you can solve separately | Parse input → process → format output |
| **Start with what you know** | Solve the part you already can | Write the loop first, work out the check later |
| **Reduce it** | Drop a constraint and solve the easier version | Solve with no duplicates, then add duplicate handling |
| **Find an analogy** | Have you solved something similar? | Brackets and undo both mean "most recent first" → stack |
| **Experiment** | Run small tests to learn how something behaves | Check what `map.get()` returns for a missing key |
| **Manage frustration** | Stuck 20 minutes on one approach? Switch strategy or take a break | Walking away is a valid move |

"Restate" and "reduce" are the two that pay most often. Restating Two Sum into "does its partner
exist?" points straight at a hash lookup. Reducing "longest substring without repeating characters"
to "does this string have any repeat?" gets you a working check you can then extend.

### Trace tables

One column per variable, one row per step. **If you can't fill the table, you don't understand the
code yet.** Running the code tells you the answer is wrong; tracing tells you *which line and which
value* made it wrong.

```javascript
let n = 123, rev = 0;
while (n > 0) {
  rev = rev * 10 + n % 10;
  n = Math.floor(n / 10);
}
```

| Step | n | rev |
|---|---|---|
| start | 123 | 0 |
| pass 1 | 12 | 3 |
| pass 2 | 1 | 32 |
| pass 3 | 0 | 321 |

`n % 10` peels off the last digit; `Math.floor(n / 10)` removes it. That digit-peeling pattern shows
up in palindrome-number and digit-sum problems — which you'd notice from the trace, not from the code.

**Two more worth tracing by hand this week:**

```javascript
let sum = 0;                          // start: i –, sum 0
for (let i = 1; i <= 3; i++) sum += i;  // pass 1: 1,1 · pass 2: 2,3 · pass 3: 3,6
// Stops when i becomes 4. Being clear about the stop condition prevents off-by-one bugs.

const count = 0;
const a = count || 5;                 // 5  — || treats 0 as missing
const b = count ?? 5;                 // 0  — ?? only replaces null/undefined
const c = count ? "yes" : "no";       // "no"
// Counters, indexes and prices are often 0. Default to ?? for them.
```

### The three language traps that break hand-traces

| Language | Trap | Reality |
|---|---|---|
| JavaScript | `0 \|\| 5` | Returns `5`. `0 ?? 5` returns `0`. Use `??` for anything that can legitimately be zero. |
| JavaScript | Object as a counter | Objects stringify every key, so `1` and `"1"` collide. `Map` keeps types, has `.size`, and has no inherited keys. |
| Java | `==` on Strings | Compares object identity, not text. `new String("hi") == "hi"` is `false`. Always `.equals()`. |

### The bridge to patterns

| Question | The signal | What it means |
|---|---|---|
| Why write brute force first? | — | It's a correct baseline to test against, and it shows you where the repeated work is |
| When do I reach for a hash map? | You keep searching for something you've already seen | Remember it once, look it up instantly |
| What does a nested loop cost? | Two loops over n items | About n × n steps — O(n²) |
| "Most recent first" | Brackets, undo, backtracking | Stack |
| "Level by level" / shortest path | — | Queue, BFS |

### A two-week on-ramp

If the Seven Steps are new to you, run this before starting the pattern parts. It fits inside the
same 08:00 block.

| Days | Focus | How |
|---|---|---|
| 1–3 | Conditionals and loops | Two problems a day, all Seven Steps |
| 4–7 | Arrays and strings | Draw a trace table for every solution |
| 8–10 | Functions and recursion | Use "divide" and "reduce" on purpose |
| 11–14 | Easy problems | Brute force first, then optimise |

**Per problem: steps 1–4 on paper, then code it, then trace it.** All three, every time.

---

## 1. The Method — Six Steps, Every Problem

Follow this literally. The point is that under interview pressure you fall back to a routine, and this
is the routine.

**1. Restate.** Say the problem back in your own words, out loud. Write down the input type, the
output type, and any constraint given. Half of all wrong answers are answers to a different question.

**2. Examples.** Write one normal case and one edge case *before* you think about the solution:
- Empty input — `[]`, `""`, `null`
- One element
- All identical elements
- Negative numbers
- Already sorted / reverse sorted

**3. Brute force first.** State it and its complexity out loud, always. It proves you understand the
problem, it gives you a fallback if you run out of time, and the optimisation usually comes from
looking at what the brute force repeats.

**4. Optimise.** Ask exactly one question: *what work am I repeating?* Then:

| Repeated work | Removes it |
|---|---|
| Searching a collection over and over | Hash map / hash set — O(n) → O(1) lookup |
| Recomputing a sum over a range | Prefix sums, or a sliding window |
| Re-sorting, or needing order | Sort once up front — O(n log n) |
| Re-exploring the same subproblem | Memoisation → dynamic programming |
| Repeatedly finding the min or max | Heap |
| Nested loops over a sorted array | Two pointers |

**5. Code it.** Then **trace one example by hand, line by line, on paper.** Not mentally. This catches
off-by-ones before the interviewer does.

**6. Complexity.** State time and space explicitly, before anyone asks and before you look at any
solution. Include the recursion stack in space.

### The 35-minute rule

Stuck at 35 minutes with no working approach: read the solution. Then **close it** and write the code
from scratch yourself. Log it as unsolved and re-solve it three days later.

Struggling past 35 minutes teaches nothing. Struggling for 30 minutes and then reading teaches a lot.

### Log every problem

`dsa/log.md`:

```markdown
| Date | Problem | Pattern | Min | Unaided | Insight | Re-solve |
|---|---|---|---|---|---|---|
| 2026-09-11 | Two Sum | Arrays/Hashing | 12 | Y | Store complement, not value | — |
| 2026-09-12 | 3Sum | Two Pointers | 45 | N | Sort first; skip duplicates at both levels | 09-15 |
```

That table is the single most honest signal in your whole study plan. Week 11 is built from it.

## 2. Complexity — Big-O in Practice

Big-O describes how runtime grows as input grows. Constants and lower-order terms drop: O(2n + 5)
is O(n).

| Notation | Name | n = 1,000 | Typical source |
|---|---|---|---|
| O(1) | Constant | 1 | Hash lookup, array index, stack push |
| O(log n) | Logarithmic | 10 | Binary search, balanced tree, heap push |
| O(n) | Linear | 1,000 | One pass over the input |
| O(n log n) | Linearithmic | 10,000 | Sorting, heap-based selection |
| O(n²) | Quadratic | 1,000,000 | Nested loop over the same input |
| O(2ⁿ) | Exponential | 10³⁰¹ | Naive recursion on subsets |
| O(n!) | Factorial | — | Permutations |

### Reading complexity off code

```python
for x in arr:               # O(n)
    ...

for x in arr:               # O(n²) — nested over the same input
    for y in arr:
        ...

for x in arr:               # O(n·m) — different inputs, NOT n²
    for y in other:
        ...

while n > 0: n //= 2        # O(log n) — halving each step

arr.sort()                  # O(n log n)
if x in hashset:            # O(1)
if x in list:               # O(n)  ← the classic accidental O(n²)
```

That last pair is worth internalising: `x in list` is a linear scan. Inside a loop, it silently makes
your solution quadratic. `x in set` is constant.

### The constraint tells you the answer

Interview constraints are a hint about the intended complexity:

| n up to | Intended solution |
|---|---|
| 10–12 | O(n!) — permutations |
| 20–25 | O(2ⁿ) — subsets, backtracking |
| 100–500 | O(n³) |
| 1,000–5,000 | O(n²) |
| 10⁵–10⁶ | O(n log n) or O(n) |
| 10⁹ | O(log n) or O(1) |

n = 10⁵ means "don't write a nested loop." Say that out loud in the interview — it shows you read the
constraints.

### Space complexity

Count everything you allocate that scales with input, **including the recursion stack**.

```python
def sum_to(n):              # O(n) SPACE — n stack frames
    if n == 0: return 0
    return n + sum_to(n - 1)

def sum_to(n):              # O(1) space
    total = 0
    for i in range(n + 1): total += i
    return total
```

Output space usually doesn't count unless the question is about it.

## 3. Data Structures — the Eight That Matter

| Structure | Access | Search | Insert | Delete | Use when |
|---|---|---|---|---|---|
| **Array** | O(1) | O(n) | O(n) | O(n) | Index access, known size, cache-friendly iteration |
| **Dynamic array** | O(1) | O(n) | O(1)* | O(n) | The default list type in all three languages |
| **Hash map / set** | — | O(1) | O(1) | O(1) | Counting, seen-before, complement lookup, grouping |
| **Linked list** | O(n) | O(n) | O(1) | O(1) | O(1) insert/delete at a known node; LRU caches |
| **Stack (LIFO)** | O(n) | O(n) | O(1) | O(1) | Matching pairs, undo, "most recent unmatched", DFS |
| **Queue (FIFO)** | O(n) | O(n) | O(1) | O(1) | BFS, level order, scheduling |
| **Heap** | O(1) peek | O(n) | O(log n) | O(log n) | Top-K, running median, always-need-the-min |
| **Binary search tree** | O(log n) | O(log n) | O(log n) | O(log n) | Sorted order + fast lookup (O(n) if unbalanced) |

\* amortised — occasional resize is O(n)

### The five recognition rules

1. **"Have I seen this before?"** → hash set
2. **"How many times?"** → hash map of counts
3. **"Most recent unmatched thing"** → stack
4. **"Shortest path" / "level by level"** → queue (BFS)
5. **"Top K" / "K largest" / "running min"** → heap

## 4. Language Idioms Side by Side

The algorithms are identical. These are the only things that change.

### Arrays / lists

| | JavaScript | Python | Java |
|---|---|---|---|
| Create | `const a = []` | `a = []` | `int[] a = new int[n]` / `List<Integer> a = new ArrayList<>()` |
| Length | `a.length` | `len(a)` | `a.length` / `a.size()` |
| Append | `a.push(x)` | `a.append(x)` | `a.add(x)` |
| Pop last | `a.pop()` | `a.pop()` | `a.remove(a.size()-1)` |
| Last element | `a.at(-1)` | `a[-1]` | `a.get(a.size()-1)` |
| Slice | `a.slice(i, j)` | `a[i:j]` | `Arrays.copyOfRange(a, i, j)` |
| Sort numbers | `a.sort((x,y)=>x-y)` | `a.sort()` | `Arrays.sort(a)` |
| Sort by key | `a.sort((x,y)=>x.v-y.v)` | `a.sort(key=lambda x: x.v)` | `a.sort(Comparator.comparingInt(x -> x.v))` |
| Reverse | `a.reverse()` | `a.reverse()` / `a[::-1]` | `Collections.reverse(a)` |
| Fill | `new Array(n).fill(0)` | `[0] * n` | `new int[n]` (zeroed) |
| 2D fill | `Array.from({length:m},()=>new Array(n).fill(0))` | `[[0]*n for _ in range(m)]` | `new int[m][n]` |

⚠ **JavaScript `a.sort()` sorts as strings.** `[10,9].sort()` gives `[10,9]`. Always pass a comparator.
⚠ **Python `[[0]*n]*m` shares rows.** Use the comprehension form.

### Hash map / set

| | JavaScript | Python | Java |
|---|---|---|---|
| Map create | `const m = new Map()` | `m = {}` | `Map<K,V> m = new HashMap<>()` |
| Set create | `const s = new Set()` | `s = set()` | `Set<T> s = new HashSet<>()` |
| Put | `m.set(k, v)` | `m[k] = v` | `m.put(k, v)` |
| Get | `m.get(k)` | `m[k]` | `m.get(k)` |
| Get with default | `m.get(k) ?? 0` | `m.get(k, 0)` | `m.getOrDefault(k, 0)` |
| Has | `m.has(k)` | `k in m` | `m.containsKey(k)` |
| Increment count | `m.set(k, (m.get(k)??0)+1)` | `m[k] = m.get(k,0)+1` | `m.merge(k, 1, Integer::sum)` |
| Counter | — | `Counter(arr)` | — |
| Default dict | — | `defaultdict(list)` | `m.computeIfAbsent(k, x->new ArrayList<>())` |
| Size | `m.size` | `len(m)` | `m.size()` |
| Iterate | `for (const [k,v] of m)` | `for k, v in m.items()` | `for (var e : m.entrySet())` |

Python's `collections.Counter` and `defaultdict` save real time — use them.

### Stack and queue

| | JavaScript | Python | Java |
|---|---|---|---|
| Stack | array + `push`/`pop` | list + `append`/`pop` | `Deque<T> st = new ArrayDeque<>()` — `push`/`pop`/`peek` |
| Queue | array + `push`/`shift` (O(n)!) | `deque` + `append`/`popleft` | `Deque<T> q = new ArrayDeque<>()` — `offer`/`poll` |

⚠ **JS `shift()` is O(n).** For BFS on large inputs, use an index pointer instead of shifting.
⚠ **Python `list.pop(0)` is O(n).** Always `from collections import deque`.
⚠ **Java: use `ArrayDeque`, not `Stack`.** `Stack` is a legacy synchronised class.

### Heap

| | JavaScript | Python | Java |
|---|---|---|---|
| Min-heap | **none built in** — write one, or sort | `heapq` on a list | `new PriorityQueue<>()` |
| Push | — | `heappush(h, x)` | `pq.offer(x)` |
| Pop min | — | `heappop(h)` | `pq.poll()` |
| Peek | — | `h[0]` | `pq.peek()` |
| Max-heap | — | push `-x`, negate on pop | `new PriorityQueue<>(Comparator.reverseOrder())` |
| Heapify | — | `heapify(list)` — O(n) | `new PriorityQueue<>(collection)` |

**JavaScript has no built-in heap.** In an interview, say so and either write a small one or use a
sorted array with the complexity trade-off stated. This is a real reason to interview in Python.

### Strings

| | JavaScript | Python | Java |
|---|---|---|---|
| Char at | `s[i]` | `s[i]` | `s.charAt(i)` |
| To chars | `[...s]` | `list(s)` | `s.toCharArray()` |
| Join | `arr.join("")` | `"".join(arr)` | `String.join("", list)` |
| Build in a loop | array + `join` | list + `join` | `StringBuilder` |
| Substring | `s.slice(i,j)` | `s[i:j]` | `s.substring(i,j)` |
| Char → index | `s.charCodeAt(i)-97` | `ord(c)-97` | `c - 'a'` |
| Sort chars | `[...s].sort().join("")` | `"".join(sorted(s))` | `char[] c=s.toCharArray(); Arrays.sort(c)` |

⚠ **Strings are immutable in all three.** Concatenating in a loop is O(n²). Build into an array or
`StringBuilder` and join once.

### Integer limits

| | JavaScript | Python | Java |
|---|---|---|---|
| Max int | `Number.MAX_SAFE_INTEGER` (2⁵³−1) | unbounded | `Integer.MAX_VALUE` (2³¹−1) |
| Infinity | `Infinity` | `float('inf')` | `Integer.MAX_VALUE` |
| Integer division | `Math.floor(a/b)` | `a // b` | `a / b` (ints) |
| Overflow | silent precision loss | never | **wraps around** |

⚠ **Java overflow is the binary-search bug**: `(l + r) / 2` overflows. Always `l + (r - l) / 2`.
⚠ **Python `-7 // 2` is `-4`**, not `-3` — it floors toward negative infinity. Use `int(-7/2)` for truncation.

---
---

# Part 1 — The Twelve Patterns

## 5. Arrays & Hashing

### When to reach for it

- "Have I seen this before?" → **hash set**
- "How many times does X appear?" → **hash map of counts**
- "Find two things that combine to a target" → **store the complement**
- "Group things that share a property" → **hash map keyed by that property**
- Any time you're about to write a nested loop that searches the same array

**The core trade:** O(n) extra space buys you O(n²) → O(n) time. Almost always worth it.

### Template

```python
seen = {}                       # or set()
for i, x in enumerate(arr):
    if <condition involving seen>:
        return <answer>
    seen[key(x)] = i            # store AFTER checking, or you match x with itself
```

---

### 5.1 Contains Duplicate

*Given an integer array, return true if any value appears at least twice.*

**Brute force:** compare every pair — O(n²).
**Insight:** a set's size tells you whether anything repeated. One pass, O(n).

```javascript
function containsDuplicate(nums) {
  const seen = new Set();
  for (const n of nums) {
    if (seen.has(n)) return true;
    seen.add(n);
  }
  return false;
}
// or: return new Set(nums).size !== nums.length;
```
```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
    # or: return len(set(nums)) != len(nums)
```
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int n : nums) {
        if (!seen.add(n)) return true;   // add returns false if already present
    }
    return false;
}
```

**Time O(n) · Space O(n).** Java's `Set.add` returning a boolean saves the separate `contains` call.

---

### 5.2 Valid Anagram

*Given two strings, return true if t is an anagram of s.*

**Insight:** anagrams have identical character counts. Sorting works — O(n log n) — but counting is O(n).

```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = new Map();
  for (const c of s) count.set(c, (count.get(c) ?? 0) + 1);
  for (const c of t) {
    const n = count.get(c);
    if (!n) return false;
    count.set(c, n - 1);
  }
  return true;
}
```
```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return len(s) == len(t) and Counter(s) == Counter(t)

# without Counter, to show the mechanism:
def is_anagram_manual(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if count.get(c, 0) == 0:
            return False
        count[c] -= 1
    return True
```
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] count = new int[26];                    // lowercase a-z only
    for (int i = 0; i < s.length(); i++) {
        count[s.charAt(i) - 'a']++;
        count[t.charAt(i) - 'a']--;
    }
    for (int c : count) if (c != 0) return false;
    return true;
}
```

**Time O(n) · Space O(1)** — the alphabet is bounded at 26, so the count array is constant space.
The single-pass increment/decrement in the Java version is the cleanest form; mention it even if you
write another language.

---

### 5.3 Two Sum

*Given an array and a target, return indices of the two numbers that add to target.*

**Brute force:** every pair — O(n²).
**Insight — the one to remember:** for each number, you know exactly what its partner must be.
Store the **complement**, not the value. Then it's a lookup.

```javascript
function twoSum(nums, target) {
  const seen = new Map();                   // value -> index
  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);                   // AFTER the check
  }
  return [];
}
```
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                               # value -> index
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
```
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int need = target - nums[i];
        if (seen.containsKey(need)) return new int[]{seen.get(need), i};
        seen.put(nums[i], i);
    }
    return new int[]{};
}
```

**Time O(n) · Space O(n).** Storing after the check is what prevents matching an element with itself
when `target == 2 * nums[i]`.

---

### 5.4 Group Anagrams

*Group strings that are anagrams of each other.*

**Insight:** you need a **canonical key** that all anagrams share. Two options — sorted characters
(O(k log k) per word), or a 26-length count tuple (O(k)).

```javascript
function groupAnagrams(strs) {
  const groups = new Map();
  for (const s of strs) {
    const key = [...s].sort().join("");
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(s);
  }
  return [...groups.values()];
}
```
```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = [0] * 26                      # count-based key — O(k), beats sorting
        for c in s:
            key[ord(c) - ord('a')] += 1
        groups[tuple(key)].append(s)        # list is unhashable; tuple is
    return list(groups.values())
```
```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> groups = new HashMap<>();
    for (String s : strs) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        String key = Arrays.toString(count);
        groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(groups.values());
}
```

**Time O(n·k) with the count key** (n words, k average length) · **Space O(n·k).**
`computeIfAbsent` and `defaultdict` are the idiomatic "get or create the bucket" forms.

---

### 5.5 Top K Frequent Elements

*Return the k most frequent elements.*

**Three approaches, worth knowing all three:**
1. Count, then sort by count — O(n log n).
2. Count, then a min-heap of size k — O(n log k). Better when k ≪ n.
3. **Bucket sort** — O(n). A value can appear at most n times, so index buckets by frequency.

```javascript
function topKFrequent(nums, k) {
  const count = new Map();
  for (const n of nums) count.set(n, (count.get(n) ?? 0) + 1);

  const buckets = Array.from({ length: nums.length + 1 }, () => []);
  for (const [num, freq] of count) buckets[freq].push(num);

  const out = [];
  for (let f = buckets.length - 1; f >= 0 && out.length < k; f--) {
    for (const num of buckets[f]) {
      out.push(num);
      if (out.length === k) break;
    }
  }
  return out;
}
```
```python
from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    out = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            out.append(num)
            if len(out) == k:
                return out
    return out

# heap version — O(n log k)
def top_k_heap(nums, k):
    return [n for n, _ in Counter(nums).most_common(k)]
```
```java
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int n : nums) count.merge(n, 1, Integer::sum);

    List<Integer>[] buckets = new List[nums.length + 1];
    for (var e : count.entrySet()) {
        int f = e.getValue();
        if (buckets[f] == null) buckets[f] = new ArrayList<>();
        buckets[f].add(e.getKey());
    }

    int[] out = new int[k];
    int idx = 0;
    for (int f = buckets.length - 1; f >= 0 && idx < k; f--) {
        if (buckets[f] == null) continue;
        for (int num : buckets[f]) {
            out[idx++] = num;
            if (idx == k) break;
        }
    }
    return out;
}
```

**Bucket sort: Time O(n) · Space O(n).** The insight — frequency is bounded by n, so it can be an
array index — is a genuinely reusable trick.

---

### 5.6 Product of Array Except Self

*Return an array where `out[i]` is the product of all elements except `nums[i]`. No division. O(n).*

**Insight:** `out[i] = (product of everything left of i) × (product of everything right of i)`.
Two passes, and the output array holds the intermediate results — O(1) extra space.

```javascript
function productExceptSelf(nums) {
  const n = nums.length;
  const out = new Array(n).fill(1);

  let left = 1;
  for (let i = 0; i < n; i++) { out[i] = left; left *= nums[i]; }

  let right = 1;
  for (let i = n - 1; i >= 0; i--) { out[i] *= right; right *= nums[i]; }

  return out;
}
```
```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n

    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]

    return out
```
```java
public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] out = new int[n];

    int left = 1;
    for (int i = 0; i < n; i++) { out[i] = left; left *= nums[i]; }

    int right = 1;
    for (int i = n - 1; i >= 0; i--) { out[i] *= right; right *= nums[i]; }

    return out;
}
```

**Time O(n) · Space O(1)** excluding the output. The prefix/suffix-pass idea reappears constantly —
in range sums, in trapping rain water, in candy distribution.

---

## 6. Two Pointers

### When to reach for it

- The input is **sorted**, or sorting it doesn't break the problem
- "Find a pair / triplet that sums to X"
- Palindromes, reversing in place
- Removing duplicates in place
- You're about to write a nested loop over a sorted array

**Two shapes:**
- **Converging** — `left = 0`, `right = n-1`, move inward. Pairs, palindromes, containers.
- **Fast/slow** — both start left, move at different rates. In-place removal, cycle detection.

### Template

```python
left, right = 0, len(arr) - 1
while left < right:
    current = f(arr[left], arr[right])
    if current == target:
        return [left, right]
    elif current < target:
        left += 1                    # need bigger — only left can help
    else:
        right -= 1                   # need smaller — only right can help
```

**The whole idea:** on sorted input, each comparison lets you *eliminate* one pointer's position
entirely. That's what turns O(n²) into O(n).

---

### 6.1 Valid Palindrome

*Ignoring non-alphanumeric characters and case, is the string a palindrome?*

```javascript
function isPalindrome(s) {
  const ok = c => /[a-z0-9]/i.test(c);
  let l = 0, r = s.length - 1;
  while (l < r) {
    while (l < r && !ok(s[l])) l++;
    while (l < r && !ok(s[r])) r--;
    if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    l++; r--;
  }
  return true;
}
```
```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True
```
```java
public boolean isPalindrome(String s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
        if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r)))
            return false;
        l++; r--;
    }
    return true;
}
```

**Time O(n) · Space O(1).** The `l < r` guard inside the inner `while` loops is what stops a
non-alphanumeric-only string from running off the end.

---

### 6.2 Two Sum II — Input Array Is Sorted

*Same as Two Sum, but the array is sorted and you must use O(1) space.*

**Insight:** sorted input means no hash map is needed. Sum too small → only moving `left` right can
increase it. Too big → only moving `right` left can decrease it.

```javascript
function twoSumII(numbers, target) {
  let l = 0, r = numbers.length - 1;
  while (l < r) {
    const sum = numbers[l] + numbers[r];
    if (sum === target) return [l + 1, r + 1];   // 1-indexed
    if (sum < target) l++;
    else r--;
  }
  return [];
}
```
```python
def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l + 1, r + 1]
        if total < target:
            l += 1
        else:
            r -= 1
    return []
```
```java
public int[] twoSumII(int[] numbers, int target) {
    int l = 0, r = numbers.length - 1;
    while (l < r) {
        int sum = numbers[l] + numbers[r];
        if (sum == target) return new int[]{l + 1, r + 1};
        if (sum < target) l++;
        else r--;
    }
    return new int[]{};
}
```

**Time O(n) · Space O(1).**

---

### 6.3 3Sum

*Find all unique triplets that sum to zero.*

**Insight:** sort, fix one element, then it's Two Sum II on the rest. **The hard part is
deduplication** — skip duplicates at both the outer and inner level.

```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const out = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;                          // sorted: no way back to zero
    if (i > 0 && nums[i] === nums[i - 1]) continue;  // skip duplicate anchors

    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      const sum = nums[i] + nums[l] + nums[r];
      if (sum < 0) l++;
      else if (sum > 0) r--;
      else {
        out.push([nums[i], nums[l], nums[r]]);
        l++; r--;
        while (l < r && nums[l] === nums[l - 1]) l++;   // skip duplicate lefts
        while (l < r && nums[r] === nums[r + 1]) r--;   // skip duplicate rights
      }
    }
  }
  return out;
}
```
```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    out = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    return out
```
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> out = new ArrayList<>();

    for (int i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        int l = i + 1, r = nums.length - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum < 0) l++;
            else if (sum > 0) r--;
            else {
                out.add(Arrays.asList(nums[i], nums[l], nums[r]));
                l++; r--;
                while (l < r && nums[l] == nums[l - 1]) l++;
                while (l < r && nums[r] == nums[r + 1]) r--;
            }
        }
    }
    return out;
}
```

**Time O(n²) · Space O(1)** excluding output (O(n) for the sort in some languages).
This is the highest-value problem in the pattern. If you can write it unaided with correct
deduplication, you own two pointers.

---

### 6.4 Container With Most Water

*Each element is a wall height. Find two walls holding the most water.*

**Insight:** area = `min(h[l], h[r]) × (r - l)`. Start at the widest pair. Moving the **taller** wall
inward can only shrink the area — width drops and the height is still capped by the shorter wall. So
always move the shorter one; that's the only move that can possibly help.

```javascript
function maxArea(height) {
  let l = 0, r = height.length - 1, best = 0;
  while (l < r) {
    best = Math.max(best, Math.min(height[l], height[r]) * (r - l));
    if (height[l] < height[r]) l++;
    else r--;
  }
  return best;
}
```
```python
def max_area(height: list[int]) -> int:
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
```
```java
public int maxArea(int[] height) {
    int l = 0, r = height.length - 1, best = 0;
    while (l < r) {
        best = Math.max(best, Math.min(height[l], height[r]) * (r - l));
        if (height[l] < height[r]) l++;
        else r--;
    }
    return best;
}
```

**Time O(n) · Space O(1).** Be ready to *justify* why moving the shorter wall is safe — that argument
is what the interviewer is actually testing.

---

## 7. Sliding Window

### When to reach for it

- "Longest / shortest / maximum **contiguous** subarray or substring"
- "**Subarray** with sum / at most K distinct / no repeats"
- The brute force is "check every subarray" — O(n²) or O(n³)

**Two shapes:**
- **Fixed size** — window of exactly k. Slide: add right, remove left.
- **Variable size** — grow right until invalid, then shrink left until valid again.

### Template — variable size

```python
left = 0
state = {}                        # whatever "valid" needs to track
best = 0

for right in range(len(arr)):
    add arr[right] to state

    while <window is invalid>:    # shrink
        remove arr[left] from state
        left += 1

    best = max(best, right - left + 1)   # window is valid here
```

Each element enters once and leaves once → **O(n)**, despite the nested loop.

---

### 7.1 Best Time to Buy and Sell Stock

*One buy, one sell, later. Maximum profit.*

**Insight:** track the minimum price seen so far; at each day the best profit ending today is
`price - minSoFar`. A degenerate sliding window — left only moves when a new minimum appears.

```javascript
function maxProfit(prices) {
  let minPrice = Infinity, best = 0;
  for (const p of prices) {
    minPrice = Math.min(minPrice, p);
    best = Math.max(best, p - minPrice);
  }
  return best;
}
```
```python
def max_profit(prices: list[int]) -> int:
    min_price, best = float('inf'), 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best
```
```java
public int maxProfit(int[] prices) {
    int minPrice = Integer.MAX_VALUE, best = 0;
    for (int p : prices) {
        minPrice = Math.min(minPrice, p);
        best = Math.max(best, p - minPrice);
    }
    return best;
}
```

**Time O(n) · Space O(1).**

---

### 7.2 Longest Substring Without Repeating Characters

**Insight:** grow right; when the incoming character is already in the window, shrink left until it
isn't. A map of `char → last index` lets you jump left straight past the duplicate.

```javascript
function lengthOfLongestSubstring(s) {
  const lastSeen = new Map();
  let left = 0, best = 0;

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    if (lastSeen.has(c) && lastSeen.get(c) >= left) {
      left = lastSeen.get(c) + 1;          // jump, don't crawl
    }
    lastSeen.set(c, right);
    best = Math.max(best, right - left + 1);
  }
  return best;
}
```
```python
def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = best = 0

    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        last_seen[c] = right
        best = max(best, right - left + 1)
    return best
```
```java
public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> lastSeen = new HashMap<>();
    int left = 0, best = 0;

    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
            left = lastSeen.get(c) + 1;
        }
        lastSeen.put(c, right);
        best = Math.max(best, right - left + 1);
    }
    return best;
}
```

**Time O(n) · Space O(min(n, alphabet)).** The `>= left` check matters — a character seen *before* the
current window must be ignored.

---

### 7.3 Longest Repeating Character Replacement

*Replace at most k characters to get the longest run of one repeated character.*

**Insight:** a window is valid when `windowLength - countOfMostFrequentChar <= k` — that difference is
how many replacements it would need.

```javascript
function characterReplacement(s, k) {
  const count = new Map();
  let left = 0, maxCount = 0, best = 0;

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    count.set(c, (count.get(c) ?? 0) + 1);
    maxCount = Math.max(maxCount, count.get(c));

    while (right - left + 1 - maxCount > k) {
      count.set(s[left], count.get(s[left]) - 1);
      left++;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}
```
```python
def character_replacement(s: str, k: int) -> int:
    count = {}
    left = max_count = best = 0

    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        max_count = max(max_count, count[c])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)
    return best
```
```java
public int characterReplacement(String s, int k) {
    int[] count = new int[26];
    int left = 0, maxCount = 0, best = 0;

    for (int right = 0; right < s.length(); right++) {
        maxCount = Math.max(maxCount, ++count[s.charAt(right) - 'A']);

        while (right - left + 1 - maxCount > k) {
            count[s.charAt(left) - 'A']--;
            left++;
        }
        best = Math.max(best, right - left + 1);
    }
    return best;
}
```

**Time O(n) · Space O(26) = O(1).** Note `maxCount` is never decreased — that looks wrong but is
correct, because the answer can only improve when a *larger* maxCount appears.

---

### 7.4 Minimum Window Substring

*Smallest substring of s containing every character of t, including duplicates.*

The hardest sliding-window problem, and the one that proves you know the pattern.

**Insight:** track `have` (how many required characters are satisfied) against `need` (how many
distinct characters t requires). Grow right until `have == need`, then shrink left as far as
possible while still valid, recording the best.

```javascript
function minWindow(s, t) {
  if (!t || !s) return "";
  const need = new Map();
  for (const c of t) need.set(c, (need.get(c) ?? 0) + 1);

  const window = new Map();
  let have = 0, required = need.size;
  let best = [-1, -1], bestLen = Infinity, left = 0;

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    window.set(c, (window.get(c) ?? 0) + 1);
    if (need.has(c) && window.get(c) === need.get(c)) have++;

    while (have === required) {
      if (right - left + 1 < bestLen) {
        best = [left, right];
        bestLen = right - left + 1;
      }
      const lc = s[left];
      window.set(lc, window.get(lc) - 1);
      if (need.has(lc) && window.get(lc) < need.get(lc)) have--;
      left++;
    }
  }
  return bestLen === Infinity ? "" : s.slice(best[0], best[1] + 1);
}
```
```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    window = {}
    have, required = 0, len(need)
    best_len, best = float('inf'), [-1, -1]
    left = 0

    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            have += 1

        while have == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = [left, right]

            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1

    l, r = best
    return s[l:r + 1] if best_len != float('inf') else ""
```
```java
public String minWindow(String s, String t) {
    if (s.isEmpty() || t.isEmpty()) return "";
    Map<Character, Integer> need = new HashMap<>();
    for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);

    Map<Character, Integer> window = new HashMap<>();
    int have = 0, required = need.size();
    int bestLen = Integer.MAX_VALUE, bestL = 0, left = 0;

    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        window.merge(c, 1, Integer::sum);
        if (need.containsKey(c) && window.get(c).equals(need.get(c))) have++;

        while (have == required) {
            if (right - left + 1 < bestLen) {
                bestLen = right - left + 1;
                bestL = left;
            }
            char lc = s.charAt(left);
            window.merge(lc, -1, Integer::sum);
            if (need.containsKey(lc) && window.get(lc) < need.get(lc)) have--;
            left++;
        }
    }
    return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestL, bestL + bestLen);
}
```

**Time O(n + m) · Space O(alphabet).**
⚠ **Java trap:** `window.get(c).equals(need.get(c))` — these are `Integer` objects, and `==` compares
references above 127. Use `.equals()`.

---

## 8. Stack

### When to reach for it

- Matching pairs — brackets, tags, quotes
- "The most recent unmatched thing"
- Undo, backtracking a path, expression evaluation
- **"Next greater / next smaller element"** → monotonic stack
- Iterative DFS

### Template — monotonic stack

```python
stack = []                          # holds indices, usually
for i, x in enumerate(arr):
    while stack and arr[stack[-1]] < x:      # < for next-greater, > for next-smaller
        j = stack.pop()
        result[j] = i - j                    # x is the answer for index j
    stack.append(i)
```

Each index is pushed once and popped once → **O(n)**, despite the inner loop.

---

### 8.1 Valid Parentheses

```javascript
function isValid(s) {
  const pairs = { ')': '(', ']': '[', '}': '{' };
  const stack = [];
  for (const c of s) {
    if (c in pairs) {
      if (stack.pop() !== pairs[c]) return false;
    } else {
      stack.push(c);
    }
  }
  return stack.length === 0;
}
```
```python
def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return not stack
```
```java
public boolean isValid(String s) {
    Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if (pairs.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        } else {
            stack.push(c);
        }
    }
    return stack.isEmpty();
}
```

**Time O(n) · Space O(n).** The final emptiness check is what catches `"((("`.

---

### 8.2 Min Stack

*A stack with `push`, `pop`, `top` and `getMin`, all O(1).*

**Insight:** store the minimum *alongside* each element. Then the min for the current stack state is
always on top.

```javascript
class MinStack {
  constructor() { this.stack = []; }                 // [value, minAtThisPoint]
  push(val) {
    const min = this.stack.length ? Math.min(val, this.getMin()) : val;
    this.stack.push([val, min]);
  }
  pop()    { this.stack.pop(); }
  top()    { return this.stack.at(-1)[0]; }
  getMin() { return this.stack.at(-1)[1]; }
}
```
```python
class MinStack:
    def __init__(self):
        self.stack = []                              # (value, min_at_this_point)

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```
```java
class MinStack {
    private final Deque<int[]> stack = new ArrayDeque<>();   // {value, minAtThisPoint}

    public void push(int val) {
        int min = stack.isEmpty() ? val : Math.min(val, stack.peek()[1]);
        stack.push(new int[]{val, min});
    }
    public void pop()    { stack.pop(); }
    public int top()     { return stack.peek()[0]; }
    public int getMin()  { return stack.peek()[1]; }
}
```

**All operations O(1) · Space O(n).**

---

### 8.3 Evaluate Reverse Polish Notation

```javascript
function evalRPN(tokens) {
  const stack = [];
  const ops = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => Math.trunc(a / b)          // truncate toward zero
  };
  for (const t of tokens) {
    if (t in ops) {
      const b = stack.pop(), a = stack.pop();
      stack.push(ops[t](a, b));               // order matters for - and /
    } else {
      stack.push(Number(t));
    }
  }
  return stack.pop();
}
```
```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),          # int() truncates; // floors — wrong for negatives
    }
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]
```
```java
public int evalRPN(String[] tokens) {
    Deque<Integer> stack = new ArrayDeque<>();
    for (String t : tokens) {
        switch (t) {
            case "+" -> stack.push(stack.pop() + stack.pop());
            case "*" -> stack.push(stack.pop() * stack.pop());
            case "-" -> { int b = stack.pop(), a = stack.pop(); stack.push(a - b); }
            case "/" -> { int b = stack.pop(), a = stack.pop(); stack.push(a / b); }
            default  -> stack.push(Integer.parseInt(t));
        }
    }
    return stack.pop();
}
```

**Time O(n) · Space O(n).**
⚠ **Python trap:** `-7 // 2` is `-4` (floors). RPN wants truncation toward zero: `int(-7 / 2)` is `-3`.

---

### 8.4 Daily Temperatures

*For each day, how many days until a warmer temperature? 0 if never.*

The canonical **monotonic stack** problem.

```javascript
function dailyTemperatures(temps) {
  const out = new Array(temps.length).fill(0);
  const stack = [];                          // indices, temps decreasing

  for (let i = 0; i < temps.length; i++) {
    while (stack.length && temps[i] > temps[stack.at(-1)]) {
      const j = stack.pop();
      out[j] = i - j;
    }
    stack.push(i);
  }
  return out;
}
```
```python
def daily_temperatures(temps: list[int]) -> list[int]:
    out = [0] * len(temps)
    stack = []                                 # indices, temps decreasing

    for i, t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            j = stack.pop()
            out[j] = i - j
        stack.append(i)
    return out
```
```java
public int[] dailyTemperatures(int[] temps) {
    int[] out = new int[temps.length];
    Deque<Integer> stack = new ArrayDeque<>();

    for (int i = 0; i < temps.length; i++) {
        while (!stack.isEmpty() && temps[i] > temps[stack.peek()]) {
            int j = stack.pop();
            out[j] = i - j;
        }
        stack.push(i);
    }
    return out;
}
```

**Time O(n) · Space O(n).** Anything left on the stack at the end never found a warmer day — and
those entries are already 0.

---

### 8.5 Largest Rectangle in Histogram

*Hard. Worth it — it's the monotonic stack at full strength.*

**Insight:** for each bar, the largest rectangle *with that bar as the height* extends left and right
until a shorter bar. A stack of increasing heights gives both boundaries: when you pop a bar, the new
stack top is its left boundary and the current index is its right.

```javascript
function largestRectangleArea(heights) {
  const stack = [];                          // indices, heights increasing
  let best = 0;

  for (let i = 0; i <= heights.length; i++) {
    const h = i === heights.length ? 0 : heights[i];   // sentinel flushes the stack
    while (stack.length && heights[stack.at(-1)] >= h) {
      const height = heights[stack.pop()];
      const left = stack.length ? stack.at(-1) + 1 : 0;
      best = Math.max(best, height * (i - left));
    }
    stack.push(i);
  }
  return best;
}
```
```python
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []                                 # indices, heights increasing
    best = 0

    for i in range(len(heights) + 1):
        h = 0 if i == len(heights) else heights[i]     # sentinel
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best
```
```java
public int largestRectangleArea(int[] heights) {
    Deque<Integer> stack = new ArrayDeque<>();
    int best = 0;

    for (int i = 0; i <= heights.length; i++) {
        int h = (i == heights.length) ? 0 : heights[i];
        while (!stack.isEmpty() && heights[stack.peek()] >= h) {
            int height = heights[stack.pop()];
            int left = stack.isEmpty() ? 0 : stack.peek() + 1;
            best = Math.max(best, height * (i - left));
        }
        stack.push(i);
    }
    return best;
}
```

**Time O(n) · Space O(n).** The sentinel `0` at the end is the trick that avoids a separate
flush loop — a technique worth stealing for other stack problems.

---

## 9. Binary Search

### When to reach for it

- Sorted array, find a value or a boundary
- The constraint says n up to 10⁹ — only O(log n) survives
- **"Minimum / maximum value that satisfies a condition"** → binary search the **answer space**,
  not the array. This is the version that separates people.

### Template — the one to memorise

```python
left, right = 0, len(arr) - 1          # INCLUSIVE bounds

while left <= right:                   # <= because bounds are inclusive
    mid = left + (right - left) // 2   # overflow-safe
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1                 # +1 and -1 or you loop forever
    else:
        right = mid - 1

return -1                              # left is now the insertion point
```

Three things cause every binary search bug: the `<=` vs `<`, the `mid ± 1`, and forgetting that
`left` ends up at the insertion point.

---

### 9.1 Binary Search

```javascript
function search(nums, target) {
  let l = 0, r = nums.length - 1;
  while (l <= r) {
    const mid = l + Math.floor((r - l) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) l = mid + 1;
    else r = mid - 1;
  }
  return -1;
}
```
```python
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```
```java
public int search(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;          // NOT (l + r) / 2 — overflows
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}
```

**Time O(log n) · Space O(1).**

---

### 9.2 Search a 2D Matrix

*Rows sorted, and each row's first element is greater than the previous row's last.*

**Insight:** it's one sorted array of length m×n. Map index `i` to `(i / cols, i % cols)`.

```javascript
function searchMatrix(matrix, target) {
  const rows = matrix.length, cols = matrix[0].length;
  let l = 0, r = rows * cols - 1;

  while (l <= r) {
    const mid = l + Math.floor((r - l) / 2);
    const val = matrix[Math.floor(mid / cols)][mid % cols];
    if (val === target) return true;
    if (val < target) l = mid + 1;
    else r = mid - 1;
  }
  return false;
}
```
```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    l, r = 0, rows * cols - 1

    while l <= r:
        mid = l + (r - l) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        if val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False
```
```java
public boolean searchMatrix(int[][] matrix, int target) {
    int rows = matrix.length, cols = matrix[0].length;
    int l = 0, r = rows * cols - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = matrix[mid / cols][mid % cols];
        if (val == target) return true;
        if (val < target) l = mid + 1;
        else r = mid - 1;
    }
    return false;
}
```

**Time O(log(m·n)) · Space O(1).**

---

### 9.3 Koko Eating Bananas

*Piles of bananas, h hours. Find the minimum eating speed k that finishes in time.*

**The answer-space problem.** You're not searching the array — you're searching k, from 1 to
max(piles). The condition "can finish at speed k" is monotonic: if k works, k+1 works. That
monotonicity is what makes binary search legal.

```javascript
function minEatingSpeed(piles, h) {
  const canFinish = k =>
    piles.reduce((hours, p) => hours + Math.ceil(p / k), 0) <= h;

  let l = 1, r = Math.max(...piles);
  while (l < r) {
    const mid = l + Math.floor((r - l) / 2);
    if (canFinish(mid)) r = mid;        // mid works — it might be the answer, keep it
    else l = mid + 1;                   // too slow
  }
  return l;
}
```
```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def can_finish(k: int) -> bool:
        return sum(math.ceil(p / k) for p in piles) <= h

    l, r = 1, max(piles)
    while l < r:
        mid = l + (r - l) // 2
        if can_finish(mid):
            r = mid                      # keep mid as a candidate
        else:
            l = mid + 1
    return l
```
```java
public int minEatingSpeed(int[] piles, int h) {
    int l = 1, r = Arrays.stream(piles).max().getAsInt();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (canFinish(piles, mid, h)) r = mid;
        else l = mid + 1;
    }
    return l;
}

private boolean canFinish(int[] piles, int k, int h) {
    long hours = 0;
    for (int p : piles) hours += (p + k - 1) / k;      // ceil without floating point
    return hours <= h;
}
```

**Time O(n log(max(piles))) · Space O(1).**
Note the template changes: `while l < r` with `r = mid` (not `mid - 1`), because mid may *be* the
answer. This "find the minimum that works" form is worth memorising separately.

---

### 9.4 Search in Rotated Sorted Array

**Insight:** at any midpoint, **one half is always properly sorted.** Work out which, then check
whether the target lies inside that sorted half. If yes, search it; if not, search the other.

```javascript
function searchRotated(nums, target) {
  let l = 0, r = nums.length - 1;
  while (l <= r) {
    const mid = l + Math.floor((r - l) / 2);
    if (nums[mid] === target) return mid;

    if (nums[l] <= nums[mid]) {                       // left half sorted
      if (nums[l] <= target && target < nums[mid]) r = mid - 1;
      else l = mid + 1;
    } else {                                          // right half sorted
      if (nums[mid] < target && target <= nums[r]) l = mid + 1;
      else r = mid - 1;
    }
  }
  return -1;
}
```
```python
def search_rotated(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:                       # left half sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:                                          # right half sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```
```java
public int searchRotated(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target) return mid;

        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) r = mid - 1;
            else l = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[r]) l = mid + 1;
            else r = mid - 1;
        }
    }
    return -1;
}
```

**Time O(log n) · Space O(1).** The `<=` in `nums[l] <= nums[mid]` handles the two-element case.

---

### 9.5 Median of Two Sorted Arrays

*Hard. O(log(min(m,n))) required.*

**Insight:** don't merge. **Partition** both arrays so the left parts together hold exactly half the
elements, and every element on the left is ≤ every element on the right. Binary search the partition
point of the *smaller* array.

```python
def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a                                    # always binary search the smaller

    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    lo, hi = 0, m

    while lo <= hi:
        i = (lo + hi) // 2                             # elements taken from a
        j = half - i                                   # elements taken from b

        a_left  = a[i - 1] if i > 0 else float('-inf')
        a_right = a[i]     if i < m else float('inf')
        b_left  = b[j - 1] if j > 0 else float('-inf')
        b_right = b[j]     if j < n else float('inf')

        if a_left <= b_right and b_left <= a_right:    # correct partition
            if (m + n) % 2:
                return max(a_left, b_left)             # odd — left side has the extra
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            hi = i - 1                                 # took too many from a
        else:
            lo = i + 1                                 # took too few from a
    return 0.0
```
```javascript
function findMedianSortedArrays(a, b) {
  if (a.length > b.length) [a, b] = [b, a];
  const m = a.length, n = b.length, half = Math.floor((m + n + 1) / 2);
  let lo = 0, hi = m;

  while (lo <= hi) {
    const i = Math.floor((lo + hi) / 2);
    const j = half - i;

    const aLeft  = i > 0 ? a[i - 1] : -Infinity;
    const aRight = i < m ? a[i]     :  Infinity;
    const bLeft  = j > 0 ? b[j - 1] : -Infinity;
    const bRight = j < n ? b[j]     :  Infinity;

    if (aLeft <= bRight && bLeft <= aRight) {
      if ((m + n) % 2) return Math.max(aLeft, bLeft);
      return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2;
    } else if (aLeft > bRight) hi = i - 1;
    else lo = i + 1;
  }
  return 0;
}
```
```java
public double findMedianSortedArrays(int[] a, int[] b) {
    if (a.length > b.length) { int[] t = a; a = b; b = t; }
    int m = a.length, n = b.length, half = (m + n + 1) / 2;
    int lo = 0, hi = m;

    while (lo <= hi) {
        int i = (lo + hi) / 2;
        int j = half - i;

        int aLeft  = i > 0 ? a[i - 1] : Integer.MIN_VALUE;
        int aRight = i < m ? a[i]     : Integer.MAX_VALUE;
        int bLeft  = j > 0 ? b[j - 1] : Integer.MIN_VALUE;
        int bRight = j < n ? b[j]     : Integer.MAX_VALUE;

        if (aLeft <= bRight && bLeft <= aRight) {
            if ((m + n) % 2 == 1) return Math.max(aLeft, bLeft);
            return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2.0;
        } else if (aLeft > bRight) hi = i - 1;
        else lo = i + 1;
    }
    return 0.0;
}
```

**Time O(log(min(m,n))) · Space O(1).** Don't expect to get this unaided the first time. Understand
the partition idea; the code follows from it.

---

## 10. Linked List

### When to reach for it

- The input *is* a linked list
- O(1) insert/delete at a known position matters
- LRU cache — hash map + doubly linked list

### The two techniques that solve most of them

**1. Dummy head.** Allocate a fake node before the real head. Every edge case about "what if the head
changes" disappears.

**2. Fast/slow pointers.** Slow moves one, fast moves two. When fast hits the end, slow is at the
middle. If they ever meet, there's a cycle.

### Node definitions

```javascript
class ListNode {
  constructor(val = 0, next = null) { this.val = val; this.next = next; }
}
```
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
```java
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
```

---

### 10.1 Reverse Linked List

**Insight:** three pointers — prev, curr, next. Save next before you break the link.

```javascript
function reverseList(head) {
  let prev = null, curr = head;
  while (curr) {
    const next = curr.next;      // save before breaking
    curr.next = prev;            // reverse the pointer
    prev = curr;                 // advance both
    curr = next;
  }
  return prev;                   // prev is the new head
}
```
```python
def reverse_list(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next   # simultaneous assignment
    return prev
```
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

**Time O(n) · Space O(1).** Python's tuple assignment evaluates the whole right side first, which is
why the one-liner is safe. Write the explicit version in an interview — it's clearer.

---

### 10.2 Merge Two Sorted Lists

**Insight:** dummy head. Without it you need a special case for choosing the first node.

```javascript
function mergeTwoLists(l1, l2) {
  const dummy = new ListNode();
  let tail = dummy;

  while (l1 && l2) {
    if (l1.val <= l2.val) { tail.next = l1; l1 = l1.next; }
    else                  { tail.next = l2; l2 = l2.next; }
    tail = tail.next;
  }
  tail.next = l1 ?? l2;              // attach whatever remains
  return dummy.next;
}
```
```python
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next
```
```java
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(), tail = dummy;

    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) { tail.next = l1; l1 = l1.next; }
        else                  { tail.next = l2; l2 = l2.next; }
        tail = tail.next;
    }
    tail.next = (l1 != null) ? l1 : l2;
    return dummy.next;
}
```

**Time O(n + m) · Space O(1).**

---

### 10.3 Remove Nth Node From End

**Insight:** two pointers n apart. When the leading one hits the end, the trailing one is at the node
*before* the target. Dummy head handles "remove the head itself".

```javascript
function removeNthFromEnd(head, n) {
  const dummy = new ListNode(0, head);
  let lead = dummy, trail = dummy;

  for (let i = 0; i <= n; i++) lead = lead.next;   // open a gap of n+1
  while (lead) { lead = lead.next; trail = trail.next; }

  trail.next = trail.next.next;                    // skip the target
  return dummy.next;
}
```
```python
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    lead = trail = dummy

    for _ in range(n + 1):
        lead = lead.next
    while lead:
        lead, trail = lead.next, trail.next

    trail.next = trail.next.next
    return dummy.next
```
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0, head);
    ListNode lead = dummy, trail = dummy;

    for (int i = 0; i <= n; i++) lead = lead.next;
    while (lead != null) { lead = lead.next; trail = trail.next; }

    trail.next = trail.next.next;
    return dummy.next;
}
```

**Time O(n), one pass · Space O(1).** The gap is `n + 1`, not `n` — you need to land on the *previous*
node.

---

### 10.4 Reorder List

*L0 → L1 → … → Ln becomes L0 → Ln → L1 → Ln-1 → …*

**Three sub-problems you already know:** find the middle (fast/slow), reverse the second half,
merge alternately.

```javascript
function reorderList(head) {
  if (!head || !head.next) return;

  // 1. find the middle
  let slow = head, fast = head;
  while (fast.next && fast.next.next) { slow = slow.next; fast = fast.next.next; }

  // 2. reverse the second half
  let second = slow.next;
  slow.next = null;
  let prev = null;
  while (second) { const nxt = second.next; second.next = prev; prev = second; second = nxt; }

  // 3. merge alternately
  let first = head; second = prev;
  while (second) {
    const n1 = first.next, n2 = second.next;
    first.next = second;
    second.next = n1;
    first = n1; second = n2;
  }
}
```
```python
def reorder_list(head: ListNode) -> None:
    if not head or not head.next:
        return

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

    second, slow.next = slow.next, None
    prev = None
    while second:
        second.next, prev, second = prev, second, second.next

    first, second = head, prev
    while second:
        n1, n2 = first.next, second.next
        first.next, second.next = second, n1
        first, second = n1, n2
```
```java
public void reorderList(ListNode head) {
    if (head == null || head.next == null) return;

    ListNode slow = head, fast = head;
    while (fast.next != null && fast.next.next != null) {
        slow = slow.next; fast = fast.next.next;
    }

    ListNode second = slow.next, prev = null;
    slow.next = null;
    while (second != null) {
        ListNode nxt = second.next;
        second.next = prev; prev = second; second = nxt;
    }

    ListNode first = head; second = prev;
    while (second != null) {
        ListNode n1 = first.next, n2 = second.next;
        first.next = second; second.next = n1;
        first = n1; second = n2;
    }
}
```

**Time O(n) · Space O(1).** Composed entirely of 10.1 and the fast/slow technique — say that out loud
when you solve it.

---

### 10.5 LRU Cache

*get and put in O(1).*

**Insight:** hash map for O(1) lookup + **doubly** linked list for O(1) reordering. Head = most
recently used, tail = least. Python's `OrderedDict` does both, but write it manually first.

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                       # key -> Node
        self.head, self.tail = Node(), Node() # sentinels
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)              # mark as most recent
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert_front(node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```
```javascript
class LRUCache {
  constructor(capacity) {
    this.cap = capacity;
    this.map = new Map();            // JS Map preserves insertion order — exploit it
  }
  get(key) {
    if (!this.map.has(key)) return -1;
    const val = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, val);          // re-insert → now most recent
    return val;
  }
  put(key, value) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, value);
    if (this.map.size > this.cap) {
      this.map.delete(this.map.keys().next().value);   // oldest key
    }
  }
}
```
```java
class LRUCache {
    private final int cap;
    private final LinkedHashMap<Integer, Integer> map;

    public LRUCache(int capacity) {
        this.cap = capacity;
        // accessOrder = true → get() moves the entry to the end
        this.map = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > cap;
            }
        };
    }
    public int get(int key)             { return map.getOrDefault(key, -1); }
    public void put(int key, int value) { map.put(key, value); }
}
```

**Both operations O(1) · Space O(capacity).**
JavaScript's `Map` and Java's `LinkedHashMap` give you insertion order for free — say you know the
manual doubly-linked-list version exists, then use the shortcut. That reads as knowing your tools.

---

## 11. Trees

### When to reach for it

- Hierarchical data, BSTs, file systems, expression parsing
- "Traverse", "depth", "path", "ancestor"

**Recursion is the default.** A tree problem is almost always: solve for the left subtree, solve for
the right, combine.

### The four traversals

| Traversal | Order | Use for |
|---|---|---|
| **Pre-order** | node, left, right | Copying a tree, serialising |
| **In-order** | left, node, right | **BST → sorted order** |
| **Post-order** | left, right, node | Deleting, computing heights bottom-up |
| **Level-order** | BFS by depth | Anything about levels or shortest path |

### Node definitions

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```
```java
class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}
```

---

### 11.1 Invert Binary Tree

```javascript
function invertTree(root) {
  if (!root) return null;
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
  return root;
}
```
```python
def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```
```java
public TreeNode invertTree(TreeNode root) {
    if (root == null) return null;
    TreeNode left = invertTree(root.left);
    root.left = invertTree(root.right);
    root.right = left;
    return root;
}
```

**Time O(n) · Space O(h)** where h is height — the recursion stack.
⚠ The Java version needs the temporary; without it you'd invert the already-inverted subtree.

---

### 11.2 Maximum Depth

```javascript
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```
```python
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```
```java
public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

**Time O(n) · Space O(h).** The three-line shape — base case, recurse both sides, combine — is the
template for most tree problems.

---

### 11.3 Same Tree

```javascript
function isSameTree(p, q) {
  if (!p && !q) return true;
  if (!p || !q || p.val !== q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```
```python
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```
```java
public boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null) return true;
    if (p == null || q == null || p.val != q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

**Time O(n) · Space O(h).**

---

### 11.4 Binary Tree Level Order Traversal

**The BFS template.** Snapshot the queue size at the start of each level — that's what separates
levels without storing depth on each node.

```javascript
function levelOrder(root) {
  if (!root) return [];
  const out = [], queue = [root];

  while (queue.length) {
    const levelSize = queue.length;              // snapshot BEFORE adding children
    const level = [];
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      level.push(node.val);
      if (node.left)  queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    out.push(level);
  }
  return out;
}
```
```python
from collections import deque

def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    out, queue = [], deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):              # snapshot the size
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(level)
    return out
```
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> out = new ArrayList<>();
    if (root == null) return out;

    Deque<TreeNode> queue = new ArrayDeque<>();
    queue.offer(root);

    while (!queue.isEmpty()) {
        int levelSize = queue.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < levelSize; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            if (node.left  != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        out.add(level);
    }
    return out;
}
```

**Time O(n) · Space O(w)** where w is the maximum width.
⚠ **JS `shift()` is O(n)** — this is O(n²) on a wide tree. Use an index pointer for large inputs.

---

### 11.5 Validate Binary Search Tree

**The classic trap:** checking only `left.val < node.val < right.val` is wrong. A node deep in the
left subtree must still be less than an *ancestor*. Pass down valid `(min, max)` bounds.

```javascript
function isValidBST(root, min = -Infinity, max = Infinity) {
  if (!root) return true;
  if (root.val <= min || root.val >= max) return false;
  return isValidBST(root.left, min, root.val)
      && isValidBST(root.right, root.val, max);
}
```
```python
def is_valid_bst(root: TreeNode, low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val)
            and is_valid_bst(root.right, root.val, high))
```
```java
public boolean isValidBST(TreeNode root) {
    return validate(root, null, null);
}

private boolean validate(TreeNode node, Integer low, Integer high) {
    if (node == null) return true;
    if (low != null && node.val <= low) return false;
    if (high != null && node.val >= high) return false;
    return validate(node.left, low, node.val)
        && validate(node.right, node.val, high);
}
```

**Time O(n) · Space O(h).** Java uses `Integer` nulls rather than `MIN_VALUE`/`MAX_VALUE` sentinels,
because a node might legitimately hold those values.

**Alternative:** in-order traversal of a valid BST is strictly increasing. Check that instead.

---

### 11.6 Lowest Common Ancestor of a BST

**Insight:** exploit the ordering. If both targets are smaller, go left. Both larger, go right. Split
across the current node — this node *is* the answer.

```javascript
function lowestCommonAncestor(root, p, q) {
  let node = root;
  while (node) {
    if (p.val < node.val && q.val < node.val)      node = node.left;
    else if (p.val > node.val && q.val > node.val) node = node.right;
    else return node;                               // they diverge here
  }
  return null;
}
```
```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return None
```
```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    TreeNode node = root;
    while (node != null) {
        if (p.val < node.val && q.val < node.val)      node = node.left;
        else if (p.val > node.val && q.val > node.val) node = node.right;
        else return node;
    }
    return null;
}
```

**Time O(h) · Space O(1) iterative.** For a *general* binary tree the answer is different — recurse
both sides and return the node where both come back non-null.

---

## 12. Heap & Intervals

### When to reach for a heap

- **"Top K"** / "K largest" / "K closest" → heap of size K, O(n log k)
- "Running median" → two heaps, max-heap for the low half, min-heap for the high half
- "Always process the smallest/largest next" → scheduling, Dijkstra, merging sorted lists

**Rule:** for K largest, use a **min**-heap of size K — the smallest of your K best sits on top, ready
to be evicted. For K smallest, a max-heap. This inversion catches people out.

### When to reach for intervals

Any problem about ranges, meetings, or overlaps. **Almost always: sort by start time first.** Two
intervals `[a,b]` and `[c,d]` overlap when `a <= d && c <= b`.

---

### 12.1 Kth Largest Element in an Array

```javascript
// JS has no heap. Sorting is O(n log n) — say so and move on, or use quickselect.
function findKthLargest(nums, k) {
  return nums.sort((a, b) => b - a)[k - 1];
}

// Quickselect — O(n) average, what an interviewer wants to hear
function findKthLargestQS(nums, k) {
  const target = nums.length - k;                 // kth largest = index n-k when sorted asc

  function select(l, r) {
    const pivot = nums[r];
    let p = l;
    for (let i = l; i < r; i++) {
      if (nums[i] <= pivot) { [nums[i], nums[p]] = [nums[p], nums[i]]; p++; }
    }
    [nums[p], nums[r]] = [nums[r], nums[p]];

    if (p > target)      return select(l, p - 1);
    else if (p < target) return select(p + 1, r);
    else                 return nums[p];
  }
  return select(0, nums.length - 1);
}
```
```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []                                     # min-heap of size k
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)                   # evict the smallest
    return heap[0]

# one-liner
def find_kth_largest_short(nums, k):
    return heapq.nlargest(k, nums)[-1]
```
```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> heap = new PriorityQueue<>();   // min-heap
    for (int n : nums) {
        heap.offer(n);
        if (heap.size() > k) heap.poll();
    }
    return heap.peek();
}
```

**Heap: Time O(n log k) · Space O(k).** Quickselect: O(n) average, O(n²) worst, O(1) space.

---

### 12.2 Task Scheduler

*Same tasks need n cooldown units between them. Minimum total time?*

**Insight:** the most frequent task determines the answer. It creates `maxFreq - 1` gaps of size
`n + 1`, and the tasks tying for most-frequent occupy the final slot.

```javascript
function leastInterval(tasks, n) {
  const counts = new Map();
  for (const t of tasks) counts.set(t, (counts.get(t) ?? 0) + 1);

  const maxFreq = Math.max(...counts.values());
  const maxCount = [...counts.values()].filter(c => c === maxFreq).length;

  return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount);
}
```
```python
from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for c in counts.values() if c == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```
```java
public int leastInterval(char[] tasks, int n) {
    int[] counts = new int[26];
    for (char t : tasks) counts[t - 'A']++;

    int maxFreq = 0, maxCount = 0;
    for (int c : counts) {
        if (c > maxFreq) { maxFreq = c; maxCount = 1; }
        else if (c == maxFreq) maxCount++;
    }
    return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount);
}
```

**Time O(n) · Space O(1).** The `max(tasks.length, …)` handles the case where there are so many
distinct tasks that no idling is needed.

---

### 12.3 Insert Interval

*Intervals are sorted and non-overlapping. Insert a new one, merging as needed.*

```javascript
function insert(intervals, newInterval) {
  const out = [];
  let i = 0, [start, end] = newInterval;

  while (i < intervals.length && intervals[i][1] < start) out.push(intervals[i++]);   // before

  while (i < intervals.length && intervals[i][0] <= end) {                            // overlapping
    start = Math.min(start, intervals[i][0]);
    end   = Math.max(end,   intervals[i][1]);
    i++;
  }
  out.push([start, end]);

  while (i < intervals.length) out.push(intervals[i++]);                              // after
  return out;
}
```
```python
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    out = []
    i, n = 0, len(intervals)
    start, end = new_interval

    while i < n and intervals[i][1] < start:
        out.append(intervals[i]); i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end   = max(end,   intervals[i][1])
        i += 1
    out.append([start, end])

    while i < n:
        out.append(intervals[i]); i += 1
    return out
```
```java
public int[][] insert(int[][] intervals, int[] newInterval) {
    List<int[]> out = new ArrayList<>();
    int i = 0, n = intervals.length;
    int start = newInterval[0], end = newInterval[1];

    while (i < n && intervals[i][1] < start) out.add(intervals[i++]);

    while (i < n && intervals[i][0] <= end) {
        start = Math.min(start, intervals[i][0]);
        end   = Math.max(end,   intervals[i][1]);
        i++;
    }
    out.add(new int[]{start, end});

    while (i < n) out.add(intervals[i++]);
    return out.toArray(new int[0][]);
}
```

**Time O(n) · Space O(n).** Three phases — before, overlapping, after — is the shape to remember.

---

### 12.4 Merge Intervals

```javascript
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const out = [intervals[0]];

  for (const [start, end] of intervals.slice(1)) {
    const last = out.at(-1);
    if (start <= last[1]) last[1] = Math.max(last[1], end);   // overlap → extend
    else out.push([start, end]);
  }
  return out;
}
```
```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
```
```java
public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> out = new ArrayList<>();
    out.add(intervals[0]);

    for (int i = 1; i < intervals.length; i++) {
        int[] last = out.get(out.size() - 1);
        if (intervals[i][0] <= last[1]) last[1] = Math.max(last[1], intervals[i][1]);
        else out.add(intervals[i]);
    }
    return out.toArray(new int[0][]);
}
```

**Time O(n log n) for the sort · Space O(n).** `max(last[1], end)` matters — one interval can fully
contain another.

---

### 12.5 Non-overlapping Intervals

*Minimum removals so no intervals overlap.*

**Insight — greedy:** sort by **end** time, not start. When two overlap, always keep the one that
ends earliest; it leaves the most room for what follows.

```javascript
function eraseOverlapIntervals(intervals) {
  intervals.sort((a, b) => a[1] - b[1]);          // by END
  let removals = 0, prevEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < prevEnd) removals++;     // overlaps — drop this one
    else prevEnd = intervals[i][1];
  }
  return removals;
}
```
```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])             # by END
    removals, prev_end = 0, intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:
            removals += 1
        else:
            prev_end = end
    return removals
```
```java
public int eraseOverlapIntervals(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
    int removals = 0, prevEnd = intervals[0][1];

    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < prevEnd) removals++;
        else prevEnd = intervals[i][1];
    }
    return removals;
}
```

**Time O(n log n) · Space O(1).** Sorting by end rather than start is the entire insight — be ready
to argue why it's optimal.

---

## 13. Backtracking

### When to reach for it

- "All combinations / permutations / subsets"
- "Find every path that…"
- Constraint puzzles — N-Queens, Sudoku, word search
- The constraint is tiny — n ≤ 20 signals O(2ⁿ), n ≤ 12 signals O(n!)

### Template — choose, explore, un-choose

```python
def backtrack(path, choices):
    if <goal reached>:
        result.append(path[:])          # COPY — path keeps mutating
        return

    for choice in choices:
        if not valid(choice):
            continue

        path.append(choice)             # 1. choose
        backtrack(path, next_choices)   # 2. explore
        path.pop()                      # 3. UN-CHOOSE ← the step people forget
```

**Two bugs cause 90% of failures:** forgetting `path.pop()`, and appending `path` instead of a copy.

---

### 13.1 Subsets

*All possible subsets of a distinct-integer array (the power set).*

```javascript
function subsets(nums) {
  const out = [], path = [];

  function backtrack(start) {
    out.push([...path]);                       // every node is a valid subset
    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]);
      backtrack(i + 1);
      path.pop();
    }
  }
  backtrack(0);
  return out;
}
```
```python
def subsets(nums: list[int]) -> list[list[int]]:
    out, path = [], []

    def backtrack(start: int) -> None:
        out.append(path[:])                    # copy
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return out
```
```java
public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> out = new ArrayList<>();
    backtrack(nums, 0, new ArrayList<>(), out);
    return out;
}

private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> out) {
    out.add(new ArrayList<>(path));            // copy
    for (int i = start; i < nums.length; i++) {
        path.add(nums[i]);
        backtrack(nums, i + 1, path, out);
        path.remove(path.size() - 1);
    }
}
```

**Time O(n · 2ⁿ) · Space O(n)** for the recursion. `start` is what prevents duplicate subsets in a
different order.

---

### 13.2 Combination Sum

*Numbers may be reused. Find all combinations summing to target.*

```javascript
function combinationSum(candidates, target) {
  const out = [], path = [];

  function backtrack(start, remaining) {
    if (remaining === 0) { out.push([...path]); return; }
    if (remaining < 0) return;

    for (let i = start; i < candidates.length; i++) {
      path.push(candidates[i]);
      backtrack(i, remaining - candidates[i]);    // i, not i+1 — reuse allowed
      path.pop();
    }
  }
  backtrack(0, target);
  return out;
}
```
```python
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    out, path = [], []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            out.append(path[:]); return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])   # i allows reuse
            path.pop()

    backtrack(0, target)
    return out
```
```java
public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> out = new ArrayList<>();
    backtrack(candidates, 0, target, new ArrayList<>(), out);
    return out;
}

private void backtrack(int[] c, int start, int remaining,
                       List<Integer> path, List<List<Integer>> out) {
    if (remaining == 0) { out.add(new ArrayList<>(path)); return; }
    if (remaining < 0) return;

    for (int i = start; i < c.length; i++) {
        path.add(c[i]);
        backtrack(c, i, remaining - c[i], path, out);
        path.remove(path.size() - 1);
    }
}
```

**Passing `i` instead of `i + 1` is the whole difference** between "reuse allowed" and "each used
once". Sorting the candidates first lets you `break` instead of `return` when remaining goes negative.

---

### 13.3 Permutations

```javascript
function permute(nums) {
  const out = [], path = [], used = new Array(nums.length).fill(false);

  function backtrack() {
    if (path.length === nums.length) { out.push([...path]); return; }

    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;  path.push(nums[i]);
      backtrack();
      path.pop();      used[i] = false;
    }
  }
  backtrack();
  return out;
}
```
```python
def permute(nums: list[int]) -> list[list[int]]:
    out, path = [], []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            out.append(path[:]); return

        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True;  path.append(n)
            backtrack()
            path.pop();      used[i] = False

    backtrack()
    return out
```
```java
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> out = new ArrayList<>();
    backtrack(nums, new boolean[nums.length], new ArrayList<>(), out);
    return out;
}

private void backtrack(int[] nums, boolean[] used,
                       List<Integer> path, List<List<Integer>> out) {
    if (path.size() == nums.length) { out.add(new ArrayList<>(path)); return; }

    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;  path.add(nums[i]);
        backtrack(nums, used, path, out);
        path.remove(path.size() - 1);  used[i] = false;
    }
}
```

**Time O(n · n!) · Space O(n).** Permutations start from 0 every time (order matters), unlike
subsets which use `start`. That contrast is worth stating out loud.

---

### 13.4 Word Search

*Does the word exist in the grid, moving up/down/left/right without reusing a cell?*

```javascript
function exist(board, word) {
  const rows = board.length, cols = board[0].length;

  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] !== word[i]) return false;

    const temp = board[r][c];
    board[r][c] = '#';                              // mark visited in place

    const found = dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1)
               || dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1);

    board[r][c] = temp;                             // un-choose
    return found;
  }

  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      if (dfs(r, c, 0)) return true;
  return false;
}
```
```python
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        temp, board[r][c] = board[r][c], '#'        # mark visited

        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                 or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

        board[r][c] = temp                          # un-choose
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
```
```java
public boolean exist(char[][] board, String word) {
    for (int r = 0; r < board.length; r++)
        for (int c = 0; c < board[0].length; c++)
            if (dfs(board, word, r, c, 0)) return true;
    return false;
}

private boolean dfs(char[][] b, String w, int r, int c, int i) {
    if (i == w.length()) return true;
    if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != w.charAt(i))
        return false;

    char temp = b[r][c];
    b[r][c] = '#';

    boolean found = dfs(b, w, r + 1, c, i + 1) || dfs(b, w, r - 1, c, i + 1)
                 || dfs(b, w, r, c + 1, i + 1) || dfs(b, w, r, c - 1, i + 1);

    b[r][c] = temp;
    return found;
}
```

**Time O(m·n·4^L) · Space O(L).** Marking the board in place instead of keeping a visited set is the
memory trick — and restoring it is the un-choose step.

---

### 13.5 N-Queens

**Insight:** place one queen per row. Track three sets of attacked positions — columns, both diagonal
directions. For a cell `(r, c)`: the `↘` diagonal is constant in `r - c`, the `↙` in `r + c`.

```python
def solve_n_queens(n: int) -> list[list[str]]:
    out = []
    cols, diag, anti = set(), set(), set()          # r-c and r+c
    board = [['.'] * n for _ in range(n)]

    def backtrack(r: int) -> None:
        if r == n:
            out.append([''.join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue

            cols.add(c); diag.add(r - c); anti.add(r + c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            cols.remove(c); diag.remove(r - c); anti.remove(r + c)
            board[r][c] = '.'

    backtrack(0)
    return out
```
```javascript
function solveNQueens(n) {
  const out = [];
  const cols = new Set(), diag = new Set(), anti = new Set();
  const board = Array.from({ length: n }, () => new Array(n).fill('.'));

  function backtrack(r) {
    if (r === n) { out.push(board.map(row => row.join(''))); return; }

    for (let c = 0; c < n; c++) {
      if (cols.has(c) || diag.has(r - c) || anti.has(r + c)) continue;

      cols.add(c); diag.add(r - c); anti.add(r + c);
      board[r][c] = 'Q';

      backtrack(r + 1);

      cols.delete(c); diag.delete(r - c); anti.delete(r + c);
      board[r][c] = '.';
    }
  }
  backtrack(0);
  return out;
}
```
```java
public List<List<String>> solveNQueens(int n) {
    List<List<String>> out = new ArrayList<>();
    Set<Integer> cols = new HashSet<>(), diag = new HashSet<>(), anti = new HashSet<>();
    char[][] board = new char[n][n];
    for (char[] row : board) Arrays.fill(row, '.');

    backtrack(0, n, board, cols, diag, anti, out);
    return out;
}

private void backtrack(int r, int n, char[][] board, Set<Integer> cols,
                       Set<Integer> diag, Set<Integer> anti, List<List<String>> out) {
    if (r == n) {
        List<String> sol = new ArrayList<>();
        for (char[] row : board) sol.add(new String(row));
        out.add(sol);
        return;
    }

    for (int c = 0; c < n; c++) {
        if (cols.contains(c) || diag.contains(r - c) || anti.contains(r + c)) continue;

        cols.add(c); diag.add(r - c); anti.add(r + c);
        board[r][c] = 'Q';

        backtrack(r + 1, n, board, cols, diag, anti, out);

        cols.remove(c); diag.remove(r - c); anti.remove(r + c);
        board[r][c] = '.';
    }
}
```

**Time O(n!) · Space O(n²).** The `r-c` / `r+c` diagonal identity is the reusable insight — it shows
up in any grid-diagonal problem.

---

## 14. Graphs

### When to reach for it

- Explicit graphs — nodes and edges, adjacency lists
- **Grids are graphs.** Each cell is a node; neighbours are the four (or eight) adjacent cells.
- Dependencies, prerequisites, ordering → topological sort
- "Connected components", "islands", "can I reach X from Y"

### DFS or BFS?

| | DFS | BFS |
|---|---|---|
| Structure | Recursion or a stack | Queue |
| Finds | *A* path, all paths, components | The **shortest** path (unweighted) |
| Use for | Islands, cycles, backtracking, topo sort | Shortest path, level order, nearest thing |
| Space | O(depth) | O(width) |

**Always keep a `visited` set.** Without one, any cycle is an infinite loop. This is the single most
common graph bug.

### Templates

```python
# DFS on a grid
def dfs(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols: return
    if (r, c) in visited or grid[r][c] != target: return
    visited.add((r, c))
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        dfs(r + dr, c + dc)

# BFS on a graph
from collections import deque
def bfs(start):
    queue, visited = deque([start]), {start}
    steps = 0
    while queue:
        for _ in range(len(queue)):          # one level at a time
            node = queue.popleft()
            if node == goal: return steps
            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)          # mark on ENQUEUE, not dequeue
                    queue.append(nb)
        steps += 1
    return -1
```

⚠ **Mark visited when you enqueue, not when you dequeue.** Otherwise a node can be queued many times.

---

### 14.1 Number of Islands

*Count connected groups of '1' in a grid.*

```javascript
function numIslands(grid) {
  if (!grid.length) return 0;
  const rows = grid.length, cols = grid[0].length;
  let count = 0;

  function sink(r, c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] !== '1') return;
    grid[r][c] = '0';                        // sink it — doubles as visited
    sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1);
  }

  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      if (grid[r][c] === '1') { count++; sink(r, c); }

  return count;
}
```
```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r: int, c: int) -> None:
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'                     # sink — doubles as visited
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)
    return count
```
```java
public int numIslands(char[][] grid) {
    if (grid.length == 0) return 0;
    int count = 0;
    for (int r = 0; r < grid.length; r++)
        for (int c = 0; c < grid[0].length; c++)
            if (grid[r][c] == '1') { count++; sink(grid, r, c); }
    return count;
}

private void sink(char[][] g, int r, int c) {
    if (r < 0 || c < 0 || r >= g.length || c >= g[0].length || g[r][c] != '1') return;
    g[r][c] = '0';
    sink(g, r + 1, c); sink(g, r - 1, c); sink(g, r, c + 1); sink(g, r, c - 1);
}
```

**Time O(m·n) · Space O(m·n)** worst-case recursion. Sinking in place avoids a separate visited set —
mention that you're mutating the input, since some interviewers care.

---

### 14.2 Clone Graph

**Insight:** a hash map from original node → clone serves as both the visited set and the lookup for
already-cloned neighbours.

```javascript
function cloneGraph(node, seen = new Map()) {
  if (!node) return null;
  if (seen.has(node)) return seen.get(node);

  const copy = new Node(node.val);
  seen.set(node, copy);                          // BEFORE recursing — breaks cycles

  for (const nb of node.neighbors) {
    copy.neighbors.push(cloneGraph(nb, seen));
  }
  return copy;
}
```
```python
def clone_graph(node: 'Node', seen: dict = None) -> 'Node':
    if not node:
        return None
    if seen is None:
        seen = {}
    if node in seen:
        return seen[node]

    copy = Node(node.val)
    seen[node] = copy                            # before recursing

    for nb in node.neighbors:
        copy.neighbors.append(clone_graph(nb, seen))
    return copy
```
```java
public Node cloneGraph(Node node) {
    return clone(node, new HashMap<>());
}

private Node clone(Node node, Map<Node, Node> seen) {
    if (node == null) return null;
    if (seen.containsKey(node)) return seen.get(node);

    Node copy = new Node(node.val);
    seen.put(node, copy);                        // before recursing

    for (Node nb : node.neighbors) {
        copy.neighbors.add(clone(nb, seen));
    }
    return copy;
}
```

**Time O(V + E) · Space O(V).** Registering the clone *before* recursing is what stops a cycle from
recursing forever.

---

### 14.3 Course Schedule

*Can you finish all courses given prerequisites? — cycle detection in a directed graph.*

**Two approaches:** DFS with three states (unvisited / in-progress / done), or Kahn's algorithm
(BFS on in-degrees). Kahn's also gives you the topological order for free.

```javascript
function canFinish(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const inDegree = new Array(numCourses).fill(0);

  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    inDegree[course]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) if (inDegree[i] === 0) queue.push(i);

  let done = 0;
  while (queue.length) {
    const node = queue.pop();
    done++;
    for (const next of graph[node]) {
      if (--inDegree[next] === 0) queue.push(next);
    }
  }
  return done === numCourses;                    // if not, a cycle blocked us
}
```
```python
from collections import deque

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    done = 0

    while queue:
        node = queue.popleft()
        done += 1
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return done == num_courses
```
```java
public boolean canFinish(int numCourses, int[][] prerequisites) {
    List<List<Integer>> graph = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
    int[] inDegree = new int[numCourses];

    for (int[] p : prerequisites) {
        graph.get(p[1]).add(p[0]);
        inDegree[p[0]]++;
    }

    Deque<Integer> queue = new ArrayDeque<>();
    for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) queue.offer(i);

    int done = 0;
    while (!queue.isEmpty()) {
        int node = queue.poll();
        done++;
        for (int next : graph.get(node)) {
            if (--inDegree[next] == 0) queue.offer(next);
        }
    }
    return done == numCourses;
}
```

**Time O(V + E) · Space O(V + E).** Collect the nodes as you pop them and you have the topological
order — that's the answer to Course Schedule II, for free.

---

### 14.4 Pacific Atlantic Water Flow

*Which cells can drain to both oceans?*

**Insight — invert the problem.** Don't simulate flow from each cell (O(m²n²)). Start from each
ocean's border and walk *uphill*, marking reachable cells. The answer is the intersection.

```python
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
        if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r, c) in visited or heights[r][c] < prev_height):
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])                    # top edge
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])     # bottom edge
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])                    # left edge
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])     # right edge

    return [list(cell) for cell in pacific & atlantic]
```
```javascript
function pacificAtlantic(heights) {
  if (!heights.length) return [];
  const rows = heights.length, cols = heights[0].length;
  const pacific = new Set(), atlantic = new Set();

  function dfs(r, c, visited, prevHeight) {
    const key = `${r},${c}`;
    if (r < 0 || c < 0 || r >= rows || c >= cols
        || visited.has(key) || heights[r][c] < prevHeight) return;
    visited.add(key);
    for (const [dr, dc] of [[1,0],[-1,0],[0,1],[0,-1]])
      dfs(r + dr, c + dc, visited, heights[r][c]);
  }

  for (let c = 0; c < cols; c++) {
    dfs(0, c, pacific, heights[0][c]);
    dfs(rows - 1, c, atlantic, heights[rows - 1][c]);
  }
  for (let r = 0; r < rows; r++) {
    dfs(r, 0, pacific, heights[r][0]);
    dfs(r, cols - 1, atlantic, heights[r][cols - 1]);
  }

  return [...pacific].filter(k => atlantic.has(k)).map(k => k.split(',').map(Number));
}
```
```java
public List<List<Integer>> pacificAtlantic(int[][] heights) {
    int rows = heights.length, cols = heights[0].length;
    boolean[][] pac = new boolean[rows][cols], atl = new boolean[rows][cols];

    for (int c = 0; c < cols; c++) {
        dfs(heights, 0, c, pac, heights[0][c]);
        dfs(heights, rows - 1, c, atl, heights[rows - 1][c]);
    }
    for (int r = 0; r < rows; r++) {
        dfs(heights, r, 0, pac, heights[r][0]);
        dfs(heights, r, cols - 1, atl, heights[r][cols - 1]);
    }

    List<List<Integer>> out = new ArrayList<>();
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (pac[r][c] && atl[r][c]) out.add(List.of(r, c));
    return out;
}

private void dfs(int[][] h, int r, int c, boolean[][] seen, int prev) {
    if (r < 0 || c < 0 || r >= h.length || c >= h[0].length
        || seen[r][c] || h[r][c] < prev) return;
    seen[r][c] = true;
    dfs(h, r + 1, c, seen, h[r][c]); dfs(h, r - 1, c, seen, h[r][c]);
    dfs(h, r, c + 1, seen, h[r][c]); dfs(h, r, c - 1, seen, h[r][c]);
}
```

**Time O(m·n) · Space O(m·n).** "Work backwards from the goal" is a reusable move — it also solves
Rotting Oranges and Walls and Gates.

---

### 14.5 Topological Sort (Course Schedule II)

*Return a valid course order, or empty if impossible.*

Kahn's algorithm from 14.3, collecting the output.

```python
from collections import deque

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_courses else []      # short → cycle
```
```javascript
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const inDegree = new Array(numCourses).fill(0);

  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    inDegree[course]++;
  }

  const queue = [], order = [];
  for (let i = 0; i < numCourses; i++) if (inDegree[i] === 0) queue.push(i);

  while (queue.length) {
    const node = queue.pop();
    order.push(node);
    for (const next of graph[node]) if (--inDegree[next] === 0) queue.push(next);
  }
  return order.length === numCourses ? order : [];
}
```
```java
public int[] findOrder(int numCourses, int[][] prerequisites) {
    List<List<Integer>> graph = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
    int[] inDegree = new int[numCourses];

    for (int[] p : prerequisites) {
        graph.get(p[1]).add(p[0]);
        inDegree[p[0]]++;
    }

    Deque<Integer> queue = new ArrayDeque<>();
    for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) queue.offer(i);

    int[] order = new int[numCourses];
    int idx = 0;
    while (!queue.isEmpty()) {
        int node = queue.poll();
        order[idx++] = node;
        for (int next : graph.get(node)) if (--inDegree[next] == 0) queue.offer(next);
    }
    return idx == numCourses ? order : new int[0];
}
```

**Time O(V + E) · Space O(V + E).** "A shorter output than expected means a cycle" is the check.
This is also exactly how Airflow decides DAG task order — worth saying in a data engineering interview.

---

## 15. Dynamic Programming

### When to reach for it

- "Maximum / minimum / number of ways to…"
- The brute force is exponential and **recomputes the same subproblems**
- Choices at each step, and past choices constrain future ones

### The method — always in this order

1. **Write the recursion.** Ignore efficiency completely. Define what `f(i)` means in one sentence.
2. **Add memoisation.** A dict or array keyed by the arguments. Now it's top-down DP. Usually enough.
3. **Convert to a table** only if you need to — bottom-up, iterative.
4. **Reduce space** if only the last few states matter — often O(n) → O(1).

Doing this in order is the whole skill. People fail DP by trying to write the table first.

### Two shapes

```python
# Top-down — recursion + memo. Write this first, every time.
from functools import cache

@cache
def f(i):
    if i <= 1: return base_case
    return combine(f(i - 1), f(i - 2))

# Bottom-up — table
dp = [0] * (n + 1)
dp[0], dp[1] = base0, base1
for i in range(2, n + 1):
    dp[i] = combine(dp[i - 1], dp[i - 2])
return dp[n]
```

---

### 15.1 Climbing Stairs

*1 or 2 steps at a time. How many ways to reach step n?*

**Recursion:** `ways(n) = ways(n-1) + ways(n-2)`. It's Fibonacci. Only the last two values matter, so
space collapses to O(1).

```javascript
function climbStairs(n) {
  let prev = 1, curr = 1;
  for (let i = 2; i <= n; i++) {
    [prev, curr] = [curr, prev + curr];
  }
  return curr;
}
```
```python
def climb_stairs(n: int) -> int:
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```
```java
public int climbStairs(int n) {
    int prev = 1, curr = 1;
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}
```

**Time O(n) · Space O(1).** Naive recursion is O(2ⁿ) — say that, then show the fix.

---

### 15.2 House Robber

*Can't rob adjacent houses. Maximum total?*

**Recursion:** at each house, `max(rob it + best from i-2, skip it and take best from i-1)`.

```javascript
function rob(nums) {
  let twoBack = 0, oneBack = 0;
  for (const n of nums) {
    [twoBack, oneBack] = [oneBack, Math.max(oneBack, twoBack + n)];
  }
  return oneBack;
}
```
```python
def rob(nums: list[int]) -> int:
    two_back, one_back = 0, 0
    for n in nums:
        two_back, one_back = one_back, max(one_back, two_back + n)
    return one_back
```
```java
public int rob(int[] nums) {
    int twoBack = 0, oneBack = 0;
    for (int n : nums) {
        int take = twoBack + n;
        twoBack = oneBack;
        oneBack = Math.max(oneBack, take);
    }
    return oneBack;
}
```

**Time O(n) · Space O(1).** House Robber II (houses in a circle) is this run twice — once excluding
the first house, once excluding the last — then take the max.

---

### 15.3 Coin Change

*Fewest coins to make `amount`, or −1.*

**Recursion:** `f(amount) = 1 + min(f(amount - coin))` over every coin that fits. The classic
unbounded knapsack.

```javascript
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (let a = 1; a <= amount; a++) {
    for (const coin of coins) {
      if (coin <= a) dp[a] = Math.min(dp[a], 1 + dp[a - coin]);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}
```
```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    return dp[amount] if dp[amount] != float('inf') else -1
```
```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);                 // sentinel > any real answer
    dp[0] = 0;

    for (int a = 1; a <= amount; a++) {
        for (int coin : coins) {
            if (coin <= a) dp[a] = Math.min(dp[a], 1 + dp[a - coin]);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
```

**Time O(amount · coins) · Space O(amount).** Greedy — always take the largest coin — is *wrong*:
coins `[1,3,4]`, amount 6 gives greedy 4+1+1 = 3 coins, but 3+3 = 2 is optimal. Be ready to give
that counter-example.

---

### 15.4 Longest Increasing Subsequence

**O(n²) DP:** `dp[i]` = length of the LIS ending at i.
**O(n log n):** maintain a `tails` array where `tails[k]` is the smallest possible tail of an
increasing subsequence of length k+1, and binary search the insert position.

```javascript
// O(n log n)
function lengthOfLIS(nums) {
  const tails = [];
  for (const n of nums) {
    let l = 0, r = tails.length;
    while (l < r) {                              // leftmost position where tails[m] >= n
      const m = (l + r) >> 1;
      if (tails[m] < n) l = m + 1;
      else r = m;
    }
    tails[l] = n;                                // replace, or append if l === length
  }
  return tails.length;
}
```
```python
from bisect import bisect_left

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for n in nums:
        i = bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)

# O(n^2) version — write this first in an interview
def length_of_lis_n2(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```
```java
public int lengthOfLIS(int[] nums) {
    List<Integer> tails = new ArrayList<>();
    for (int n : nums) {
        int i = Collections.binarySearch(tails, n);
        if (i < 0) i = -(i + 1);                 // insertion point
        if (i == tails.size()) tails.add(n);
        else tails.set(i, n);
    }
    return tails.size();
}
```

**O(n log n) · Space O(n).** `tails` is **not** the actual subsequence — only its length is correct.
Say that; it's a common follow-up.

---

### 15.5 Word Break

*Can s be segmented into dictionary words?*

**Recursion:** `f(i)` = "can s[i:] be segmented?" → true if some dictionary word matches at i and
`f(i + len(word))` is true.

```javascript
function wordBreak(s, wordDict) {
  const words = new Set(wordDict);
  const dp = new Array(s.length + 1).fill(false);
  dp[s.length] = true;                           // empty suffix is segmentable

  for (let i = s.length - 1; i >= 0; i--) {
    for (const w of words) {
      if (i + w.length <= s.length && s.startsWith(w, i) && dp[i + w.length]) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[0];
}
```
```python
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in words:
            if s.startswith(w, i) and dp[i + len(w)]:
                dp[i] = True
                break
    return dp[0]
```
```java
public boolean wordBreak(String s, List<String> wordDict) {
    Set<String> words = new HashSet<>(wordDict);
    boolean[] dp = new boolean[s.length() + 1];
    dp[s.length()] = true;

    for (int i = s.length() - 1; i >= 0; i--) {
        for (String w : words) {
            if (i + w.length() <= s.length()
                && s.startsWith(w, i) && dp[i + w.length()]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[0];
}
```

**Time O(n · m · k) · Space O(n)** — n = length of s, m = dictionary size, k = average word length.

---
---

## 16. Prefix Sum

**When:** repeated range-sum queries · "subarray sums to K" · "equal number of X and Y"

Precompute cumulative sums once; every range query is then one subtraction.

```python
prefix = [0]
for n in nums:
    prefix.append(prefix[-1] + n)
# sum of nums[i..j] inclusive:
range_sum = prefix[j + 1] - prefix[i]
```

### Subarray Sum Equals K

**Insight:** `sum(i..j) == k` means `prefix[j] - prefix[i-1] == k`, so for each running sum look up
`running - k` in a map of counts. Same complement trick as Two Sum (§5.3), applied to prefixes.

```javascript
function subarraySum(nums, k) {
  const counts = new Map([[0, 1]]);      // empty prefix seen once
  let running = 0, total = 0;
  for (const n of nums) {
    running += n;
    total += counts.get(running - k) ?? 0;
    counts.set(running, (counts.get(running) ?? 0) + 1);
  }
  return total;
}
```
```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    running = total = 0
    for n in nums:
        running += n
        total += counts[running - k]
        counts[running] += 1
    return total
```
```java
public int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> counts = new HashMap<>();
    counts.put(0, 1);
    int running = 0, total = 0;
    for (int n : nums) {
        running += n;
        total += counts.getOrDefault(running - k, 0);
        counts.merge(running, 1, Integer::sum);
    }
    return total;
}
```

**Time O(n) · Space O(n).** Seeding the map with `{0: 1}` is what makes a prefix that *is* k count.

**2D prefix sums** extend it: `sum(r1..r2, c1..c2) = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`.
The two subtractions remove overlapping regions, and the final add puts back the corner removed twice.

---

## 17. Bit Manipulation

**When:** "without extra space" · "appears once / twice" · subsets of a small set · flags and masks

```
x & 1          odd/even test
x >> 1         divide by 2      x << 1   multiply by 2
x & (x - 1)    clears the lowest set bit
x & -x         isolates the lowest set bit
x ^ x == 0     a value XORed with itself vanishes
x ^ 0 == x     XOR with zero is identity
```

XOR is the workhorse: **self-inverse and commutative**, so pairs cancel regardless of order.

### Single Number

*Every element appears twice except one. Find it. O(1) space.*

```javascript
const singleNumber = nums => nums.reduce((acc, n) => acc ^ n, 0);
```
```python
from functools import reduce
from operator import xor

def single_number(nums: list[int]) -> int:
    return reduce(xor, nums, 0)
```
```java
public int singleNumber(int[] nums) {
    int acc = 0;
    for (int n : nums) acc ^= n;
    return acc;
}
```

Every pair cancels to 0; the loner survives. **Time O(n) · Space O(1).**

### Counting bits, and subsets

```javascript
function hammingWeight(n) {
  let count = 0;
  while (n) { n &= n - 1; count++; }     // clears one set bit per pass
  return count;
}

// Every subset of an n-element set, via the bits of 0..2^n-1
function subsetsBitmask(nums) {
  const out = [];
  for (let mask = 0; mask < (1 << nums.length); mask++) {
    const subset = [];
    for (let i = 0; i < nums.length; i++) if (mask & (1 << i)) subset.push(nums[i]);
    out.push(subset);
  }
  return out;
}
```
```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
    # or: return bin(n).count('1')
```
```java
public int hammingWeight(int n) {
    int count = 0;
    while (n != 0) { n &= n - 1; count++; }
    return count;
    // or: return Integer.bitCount(n);
}
```

⚠ **Language differences that bite.** JavaScript bitwise operators coerce to **32-bit signed** — above
2³¹ they silently break, and `>>>` is the unsigned right shift. Python integers are arbitrary
precision and negative numbers behave as if infinitely sign-extended, so `~x == -x-1` always. Java
`int` is 32-bit and `>>>` is unsigned; use `Integer.bitCount`, `Long.bitCount`.

---

## 18. Fast and Slow Pointers

Introduced inside §10, but it's a pattern in its own right — and it's the answer to a class of
problems that look unrelated.

**When:** cycle detection · finding the middle · finding the k-th from the end · "without extra space"

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next            # 1 step
    fast = fast.next.next       # 2 steps
    if slow is fast:            # they met — there's a cycle
        break
```

**Why it works:** inside a cycle the fast pointer gains one position per iteration on the slow one, so
it must eventually land on it. No cycle means fast reaches the end first.

### Linked List Cycle, and where it starts

```javascript
function detectCycle(head) {
  let slow = head, fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {                    // cycle confirmed
      let entry = head;
      while (entry !== slow) { entry = entry.next; slow = slow.next; }
      return entry;                          // the node where the cycle begins
    }
  }
  return null;
}
```
```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            entry = head
            while entry is not slow:
                entry, slow = entry.next, slow.next
            return entry
    return None
```
```java
public ListNode detectCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next; fast = fast.next.next;
        if (slow == fast) {
            ListNode entry = head;
            while (entry != slow) { entry = entry.next; slow = slow.next; }
            return entry;
        }
    }
    return null;
}
```

**Time O(n) · Space O(1).** The second phase — resetting one pointer to the head and advancing both
one step until they meet — lands exactly on the cycle entrance (Floyd's algorithm). Be ready to say
you know *that* it works even if you can't derive the proof under pressure.

The same trick finds duplicates in an array where values are indices (Find the Duplicate Number) —
treat `nums[i]` as a "next pointer" and the duplicate is the cycle entrance.

---

## 19. Monotonic Queue

The sibling of the monotonic stack (§8.4). A **deque** kept in decreasing order gives you the maximum
of a sliding window in O(1) amortised.

**When:** "maximum/minimum of every window of size k" · window problems where the answer is an extreme

```javascript
function maxSlidingWindow(nums, k) {
  const deque = [];                       // indices, values decreasing
  const out = [];

  for (let i = 0; i < nums.length; i++) {
    while (deque.length && deque[0] <= i - k) deque.shift();          // drop out-of-window
    while (deque.length && nums[deque.at(-1)] <= nums[i]) deque.pop(); // drop smaller — never the max again
    deque.push(i);
    if (i >= k - 1) out.push(nums[deque[0]]);                          // front is the max
  }
  return out;
}
```
```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq, out = deque(), []
    for i, n in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```
```java
public int[] maxSlidingWindow(int[] nums, int k) {
    Deque<Integer> dq = new ArrayDeque<>();
    int[] out = new int[nums.length - k + 1];
    int idx = 0;
    for (int i = 0; i < nums.length; i++) {
        while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
        while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
        dq.offerLast(i);
        if (i >= k - 1) out[idx++] = nums[dq.peekFirst()];
    }
    return out;
}
```

**Time O(n) · Space O(k).** Each index is pushed once and popped once. The insight worth stating: a
smaller value that arrives *later* than a bigger one can never be the window maximum while the bigger
one is still in range — so you can discard it immediately.

---

## 20. Greedy

**When:** "maximum number of…" · scheduling · "minimum steps to…" where a local rule provably works

Greedy makes the locally best choice and never reconsiders. That's why it's fast and why it's often
wrong. **The interview skill is justifying it, or producing the counter-example that kills it.**

### Activity selection — the canonical case

Maximum non-overlapping intervals. **Sort by end time**, always take the earliest-finishing compatible
activity, because it leaves the most room for everything after.

```javascript
function maxActivities(intervals) {
  intervals.sort((a, b) => a[1] - b[1]);
  let count = 0, lastEnd = -Infinity;
  for (const [start, end] of intervals) {
    if (start >= lastEnd) { count++; lastEnd = end; }
  }
  return count;
}
```
```python
def max_activities(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count, last_end = 0, float('-inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```
```java
public int maxActivities(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
    int count = 0, lastEnd = Integer.MIN_VALUE;
    for (int[] iv : intervals) {
        if (iv[0] >= lastEnd) { count++; lastEnd = iv[1]; }
    }
    return count;
}
```

### Jump Game — greedy on reach

```python
def can_jump(nums: list[int]) -> bool:
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False              # can't even get here
        reach = max(reach, i + n)
    return True
```

### When greedy is wrong

**Coin Change with coins `[1, 3, 4]`, amount 6.** Greedy takes 4, then 1, then 1 — three coins.
Optimal is 3 + 3 — two coins. Greedy fails because taking the largest coin isn't provably safe.

**Have that counter-example ready.** "Why not greedy?" is a standard follow-up on Coin Change (§15.3),
and answering it with a concrete failing input is the difference between sounding rehearsed and
sounding like you understand the problem.

**Greedy is safe when** the problem has the *greedy-choice property* — a globally optimal solution can
be built from locally optimal choices — usually because sorting establishes an ordering where one
choice provably dominates. If you can't argue that, use DP.

---

## 21. Divide and Conquer, Sorting, and the Master Theorem

**When:** the input splits into independent halves · "sort" · "count inversions" · "closest pair"

Three steps: **divide** into subproblems, **conquer** them recursively, **combine** the results.

### Merge sort — the shape to know

```javascript
function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = arr.length >> 1;
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));
  return merge(left, right);
}

function merge(a, b) {
  const out = [];
  let i = 0, j = 0;
  while (i < a.length && j < b.length) out.push(a[i] <= b[j] ? a[i++] : b[j++]);
  return out.concat(a.slice(i), b.slice(j));
}
```
```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]
```
```java
public int[] mergeSort(int[] arr) {
    if (arr.length <= 1) return arr;
    int mid = arr.length / 2;
    int[] left  = mergeSort(Arrays.copyOfRange(arr, 0, mid));
    int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));

    int[] out = new int[arr.length];
    int i = 0, j = 0, k = 0;
    while (i < left.length && j < right.length)
        out[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
    while (i < left.length)  out[k++] = left[i++];
    while (j < right.length) out[k++] = right[j++];
    return out;
}
```

**Time O(n log n) · Space O(n).** Merge sort is **stable**; quicksort isn't. That's why Java's
`Arrays.sort` uses quicksort for primitives and a merge variant for objects — stability only matters
when equal elements are distinguishable.

### The sorting comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quicksort | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | O(k) | ✅ |

Quicksort's worst case is already-sorted input with a naive pivot — randomised or median-of-three
pivots avoid it. Counting sort beats the O(n log n) comparison bound because it doesn't compare;
it needs a small bounded key range.

Python's `sorted` is **Timsort** (merge + insertion hybrid, stable, O(n) on nearly-sorted data).
JavaScript's `Array.sort` is required to be stable since ES2019.

### The Master Theorem

For a recurrence of the form **T(n) = a·T(n/b) + f(n)** — *a* subproblems, each of size *n/b*, plus
*f(n)* work to split and combine:

| Case | Condition | Result |
|---|---|---|
| 1 | f(n) grows slower than n^(log_b a) | T(n) = Θ(n^(log_b a)) — the recursion dominates |
| 2 | f(n) ≈ n^(log_b a) | T(n) = Θ(n^(log_b a) · log n) |
| 3 | f(n) grows faster than n^(log_b a) | T(n) = Θ(f(n)) — the combine step dominates |

Worked examples:

| Recurrence | a, b, f(n) | Result | Where |
|---|---|---|---|
| T(n) = 2T(n/2) + O(n) | 2, 2, n | **O(n log n)** | Merge sort — case 2 |
| T(n) = 2T(n/2) + O(1) | 2, 2, 1 | **O(n)** | Tree traversal — case 1 |
| T(n) = T(n/2) + O(1) | 1, 2, 1 | **O(log n)** | Binary search — case 2 |
| T(n) = 2T(n/2) + O(n²) | 2, 2, n² | **O(n²)** | Case 3 |

You rarely need it to *solve* an interview problem, but being able to say "that's 2T(n/2) + O(n), so
O(n log n)" when asked to analyse a recursive function is a strong signal.

### Amortized analysis

Some operations are occasionally expensive but cheap on average across a sequence.

**Dynamic array append:** usually O(1), but when full it allocates double and copies everything —
O(n). Because doubling means that copy happens only every n appends, the *amortised* cost is O(1).
Total work for n appends is n + n/2 + n/4 + … < 2n.

This is why `list.append`, `arr.push` and `ArrayList.add` are all documented as amortised O(1), and
why pre-sizing a list matters when you know the final length.

---

## 22. Union-Find (Disjoint Set Union)

**When:** "are these connected?" · counting connected components · detecting a cycle in an
**undirected** graph · Kruskal's minimum spanning tree · redundant connections

Near-O(1) per operation with both optimisations: **path compression** (flatten while finding) and
**union by rank** (attach the shorter tree under the taller).

```javascript
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(0);
    this.count = n;                               // number of components
  }

  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);   // path compression
    return this.parent[x];
  }

  union(a, b) {
    const ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;                  // already connected — this edge is redundant
    if (this.rank[ra] < this.rank[rb]) this.parent[ra] = rb;
    else if (this.rank[ra] > this.rank[rb]) this.parent[rb] = ra;
    else { this.parent[rb] = ra; this.rank[ra]++; }
    this.count--;
    return true;
  }
}
```
```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])     # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
```
```java
class UnionFind {
    private final int[] parent, rank;
    int count;

    UnionFind(int n) {
        parent = new int[n]; rank = new int[n]; count = n;
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) { int t = ra; ra = rb; rb = t; }
        parent[rb] = ra;
        if (rank[ra] == rank[rb]) rank[ra]++;
        count--;
        return true;
    }
}
```

**Time O(α(n)) per operation** — the inverse Ackermann function, below 5 for any input that fits in
the universe. Treat it as O(1) and say so.

### Redundant Connection

*Return the edge that creates a cycle.*

```python
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges) + 1)
    for a, b in edges:
        if not uf.union(a, b):        # already connected → this edge closes a cycle
            return [a, b]
    return []
```

**Union-Find vs DFS for connectivity:** DFS is fine for a static graph you traverse once. Union-Find
wins when edges **arrive over time** and you need connectivity answered as you go — you can't re-run
DFS after every edge.

---

## 23. Trie (Prefix Tree)

**When:** autocomplete · "does any word start with…" · dictionary lookup · word-search-in-grid with
many words · IP routing

Stores strings character by character, so every shared prefix is stored once.

```javascript
class TrieNode {
  constructor() { this.children = new Map(); this.isEnd = false; }
}

class Trie {
  constructor() { this.root = new TrieNode(); }

  insert(word) {
    let node = this.root;
    for (const c of word) {
      if (!node.children.has(c)) node.children.set(c, new TrieNode());
      node = node.children.get(c);
    }
    node.isEnd = true;
  }

  _walk(prefix) {
    let node = this.root;
    for (const c of prefix) {
      if (!node.children.has(c)) return null;
      node = node.children.get(c);
    }
    return node;
  }

  search(word)          { const n = this._walk(word);   return n !== null && n.isEnd; }
  startsWith(prefix)    { return this._walk(prefix) !== null; }
}
```
```python
class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.is_end = True

    def _walk(self, prefix: str) -> TrieNode | None:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
```
```java
class Trie {
    private static class Node {
        Node[] children = new Node[26];       // lowercase only — a Map for a wider alphabet
        boolean isEnd;
    }
    private final Node root = new Node();

    public void insert(String word) {
        Node node = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) node.children[i] = new Node();
            node = node.children[i];
        }
        node.isEnd = true;
    }

    private Node walk(String prefix) {
        Node node = root;
        for (char c : prefix.toCharArray()) {
            node = node.children[c - 'a'];
            if (node == null) return null;
        }
        return node;
    }

    public boolean search(String word)     { Node n = walk(word);   return n != null && n.isEnd; }
    public boolean startsWith(String pre)  { return walk(pre) != null; }
}
```

**Insert and search O(m)** in the length of the word — **independent of how many words are stored.**
That's the point: a hash set gives O(1) exact lookup but cannot answer "does anything start with
this?" without scanning everything.

**Space** is O(total characters), worst case, but shared prefixes collapse. `isEnd` is essential —
without it, inserting `"card"` would make `"car"` appear to be a stored word.

---

## 24. Matrix Traversal

Grids are graphs (§14), but a few matrix-specific manipulations come up often enough to know cold.

```python
DIRS4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIRS8 = DIRS4 + ((1, 1), (1, -1), (-1, 1), (-1, -1))

def neighbours(r, c, rows, cols):
    for dr, dc in DIRS4:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```

### Rotate an image 90° clockwise, in place

**Insight:** transpose, then reverse each row. Two simple passes instead of one confusing index formula.

```javascript
function rotate(matrix) {
  const n = matrix.length;
  for (let i = 0; i < n; i++)                       // transpose
    for (let j = i + 1; j < n; j++)
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
  for (const row of matrix) row.reverse();          // reverse each row
}
```
```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```
```java
public void rotate(int[][] matrix) {
    int n = matrix.length;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            int t = matrix[i][j]; matrix[i][j] = matrix[j][i]; matrix[j][i] = t;
        }
    for (int[] row : matrix) {
        for (int l = 0, r = n - 1; l < r; l++, r--) {
            int t = row[l]; row[l] = row[r]; row[r] = t;
        }
    }
}
```

### Spiral order

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1): out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1): out.append(matrix[r][right])
        right -= 1
        if top <= bottom:                          # guard — a single remaining row
            for c in range(right, left - 1, -1): out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:                          # guard — a single remaining column
            for r in range(bottom, top - 1, -1): out.append(matrix[r][left])
            left += 1
    return out
```

The two guards are the whole difficulty — without them a single leftover row or column gets emitted
twice. **Set Matrix Zeroes** is the other common one: use the first row and column as your marker
storage to get O(1) extra space.

---

## 25. The 25-Pattern Map

A wider taxonomy than the twelve in Part 1, and a checklist for whether anything is still unfamiliar.

| # | Pattern | Section here | Example problem |
|---|---|---|---|
| 1 | Sliding Window | §7 | Longest Substring Without Repeating |
| 2 | Two Pointers | §6 | 3Sum, Container With Most Water |
| 3 | Fast & Slow Pointers | §18 | Linked List Cycle |
| 4 | Merge Intervals | §12 | Merge Intervals |
| 5 | Binary Search | §9 | Binary Search |
| 6 | Modified Binary Search | §9.4 | Search in Rotated Sorted Array |
| 7 | Binary Search on Answer | §9.3 | Koko Eating Bananas |
| 8 | Prefix Sum | §16 | Subarray Sum Equals K |
| 9 | Hash Map / Frequency | §5 | Two Sum, Group Anagrams |
| 10 | Monotonic Stack | §8.4 | Daily Temperatures |
| 11 | Stack Simulation | §8.1 | Valid Parentheses |
| 12 | Monotonic Queue | §19 | Sliding Window Maximum |
| 13 | Linked List Reversal | §10.1 | Reverse Linked List |
| 14 | In-place List Manipulation | §10.4 | Reorder List |
| 15 | Top K Elements | §12.1 | Kth Largest |
| 16 | Bit Manipulation | §17 | Single Number |
| 17 | Matrix Traversal | §24 | Rotate Image, Spiral Order |
| 18 | DFS | §14 | Number of Islands |
| 19 | BFS | §11.4, §14 | Level Order, shortest path |
| 20 | Backtracking | §13 | N-Queens, Subsets |
| 21 | 1D Dynamic Programming | §15 | Climbing Stairs, House Robber |
| 22 | 2D Dynamic Programming | §15 | LCS, edit distance |
| 23 | Greedy | §20 | Activity Selection, Jump Game |
| 24 | Union-Find (DSU) | §22 | Redundant Connection |
| 25 | Trie | §23 | Implement Trie, autocomplete |

Also covered here but not on that list: **Divide and Conquer + the Master Theorem** (§21), **sorting
algorithms and stability** (§21), and **amortized analysis** (§21).

**The five tips that came with the taxonomy, and they're right:** identify the pattern first ·
practise similar problems together · understand the approach rather than memorising code · dry-run
with examples · then write the clean optimal solution.

---

# Part 2 — Reference

## 26. Pattern Recognition — Signal → Pattern

The interview skill isn't knowing the patterns. It's recognising which one a problem is, in the first
two minutes. This table is that mapping.

| The problem says… | Reach for | Section |
|---|---|---|
| "Have I seen this before?" | Hash set | §5 |
| "How many times?" / "most frequent" | Hash map of counts | §5 |
| "Two numbers that sum to X" | Hash map of complements | §5.3 |
| "Group by some property" | Hash map keyed by a canonical form | §5.4 |
| "Top K" / "K largest" | Heap of size K, or bucket sort | §5.5, §12.1 |
| Sorted array + find a pair | Two pointers, converging | §6 |
| Palindrome / reverse in place | Two pointers, converging | §6.1 |
| "Remove duplicates in place" | Two pointers, fast/slow | §6 |
| **Contiguous** subarray or substring | Sliding window | §7 |
| "Longest substring with condition X" | Variable sliding window | §7.2 |
| Matching brackets / "most recent unmatched" | Stack | §8.1 |
| "Next greater / smaller element" | Monotonic stack | §8.4 |
| Sorted array + find a value | Binary search | §9 |
| "Minimum X such that condition holds" | **Binary search the answer space** | §9.3 |
| n up to 10⁹ | O(log n) — binary search or maths | §2 |
| Head might change | Dummy head node | §10.2 |
| "Middle of the list" / "detect a cycle" | Fast/slow pointers | §10.3 |
| O(1) get and put with eviction | Hash map + doubly linked list | §10.5 |
| Anything about a tree | Recursion — left, right, combine | §11 |
| "Level by level" / "shortest path unweighted" | BFS with a queue | §11.4, §14 |
| BST + "sorted order" | In-order traversal | §11 |
| Overlapping ranges / meetings | Sort by start, then compare | §12.4 |
| "Maximum non-overlapping" | Sort by **end**, greedy | §12.5 |
| "All combinations / permutations / subsets" | Backtracking | §13 |
| n ≤ 20 | O(2ⁿ) — subsets, backtracking | §2 |
| n ≤ 12 | O(n!) — permutations | §2 |
| Grid + "connected regions" | DFS or BFS flood fill | §14.1 |
| Dependencies / prerequisites / ordering | Topological sort | §14.5 |
| "Can I reach X from Y" | DFS/BFS + visited set | §14 |
| "Number of ways" / "min or max total" | Dynamic programming | §15 |
| Brute force recomputes subproblems | Memoise it | §15 |

### The two-minute opening

Say this out loud, in order, before writing any code:

1. "The input is ___, the output is ___."
2. "The brute force is ___, which is O(___)."
3. "The repeated work is ___."
4. "That suggests ___ [pattern], which should get us to O(___)."
5. "Let me check the edge cases: empty, single element, all duplicates."

An interviewer who hears that has already decided you're competent, before you write a line.

---

## 27. The 55-Problem Tracker

Weeks follow the DSA column of `plans/DAILY-TOPICS-SCHEDULE.md`. Log each in `dsa/log.md`. Re-solve anything marked ✗ three days later.

| # | Problem | Pattern | Wk | Difficulty | Solved | Re-solve |
|---|---|---|---|---|---|---|
| 1 | Contains Duplicate | Arrays & Hashing | 0 | Easy | ☐ | |
| 2 | Valid Anagram | Arrays & Hashing | 0 | Easy | ☐ | |
| 3 | Two Sum | Arrays & Hashing | 0 | Easy | ☐ | |
| 4 | Group Anagrams | Arrays & Hashing | 1 | Medium | ☐ | |
| 5 | Top K Frequent Elements | Arrays & Hashing | 1 | Medium | ☐ | |
| 6 | Product of Array Except Self | Arrays & Hashing | 1 | Medium | ☐ | |
| 7 | Valid Palindrome | Two Pointers | 1 | Easy | ☐ | |
| 8 | Two Sum II | Two Pointers | 1 | Medium | ☐ | |
| 9 | 3Sum | Two Pointers | 2 | Medium | ☐ | |
| 10 | Container With Most Water | Two Pointers | 2 | Medium | ☐ | |
| 11 | Best Time to Buy and Sell Stock | Sliding Window | 2 | Easy | ☐ | |
| 12 | Longest Substring Without Repeating | Sliding Window | 2 | Medium | ☐ | |
| 13 | Longest Repeating Char Replacement | Sliding Window | 2 | Medium | ☐ | |
| 14 | Minimum Window Substring | Sliding Window | 3 | **Hard** | ☐ | |
| 15 | Valid Parentheses | Stack | 3 | Easy | ☐ | |
| 16 | Min Stack | Stack | 3 | Medium | ☐ | |
| 17 | Evaluate RPN | Stack | 3 | Medium | ☐ | |
| 18 | Daily Temperatures | Stack | 3 | Medium | ☐ | |
| 19 | Largest Rectangle in Histogram | Stack | 4 | **Hard** | ☐ | |
| 20 | Binary Search | Binary Search | 4 | Easy | ☐ | |
| 21 | Search a 2D Matrix | Binary Search | 4 | Medium | ☐ | |
| 22 | Koko Eating Bananas | Binary Search | 4 | Medium | ☐ | |
| 23 | Search in Rotated Sorted Array | Binary Search | 4 | Medium | ☐ | |
| 24 | Median of Two Sorted Arrays | Binary Search | 5 | **Hard** | ☐ | |
| 25 | Reverse Linked List | Linked List | 5 | Easy | ☐ | |
| 26 | Merge Two Sorted Lists | Linked List | 5 | Easy | ☐ | |
| 27 | Remove Nth Node From End | Linked List | 5 | Medium | ☐ | |
| 28 | Reorder List | Linked List | 5 | Medium | ☐ | |
| 29 | LRU Cache | Linked List | 6 | Medium | ☐ | |
| 30 | Invert Binary Tree | Trees | 6 | Easy | ☐ | |
| 31 | Maximum Depth of Binary Tree | Trees | 6 | Easy | ☐ | |
| 32 | Same Tree | Trees | 6 | Easy | ☐ | |
| 33 | Level Order Traversal | Trees | 6 | Medium | ☐ | |
| 34 | Validate BST | Trees | 7 | Medium | ☐ | |
| 35 | Lowest Common Ancestor of a BST | Trees | 7 | Medium | ☐ | |
| 36 | Kth Largest Element | Heap | 7 | Medium | ☐ | |
| 37 | Task Scheduler | Heap | 7 | Medium | ☐ | |
| 38 | Insert Interval | Intervals | 7 | Medium | ☐ | |
| 39 | Merge Intervals | Intervals | 8 | Medium | ☐ | |
| 40 | Non-overlapping Intervals | Intervals | 8 | Medium | ☐ | |
| 41 | Subsets | Backtracking | 8 | Medium | ☐ | |
| 42 | Combination Sum | Backtracking | 8 | Medium | ☐ | |
| 43 | Permutations | Backtracking | 8 | Medium | ☐ | |
| 44 | Word Search | Backtracking | 9 | Medium | ☐ | |
| 45 | N-Queens | Backtracking | 9 | **Hard** | ☐ | |
| 46 | Number of Islands | Graphs | 9 | Medium | ☐ | |
| 47 | Clone Graph | Graphs | 9 | Medium | ☐ | |
| 48 | Course Schedule | Graphs | 9 | Medium | ☐ | |
| 49 | Pacific Atlantic Water Flow | Graphs | 10 | Medium | ☐ | |
| 50 | Course Schedule II (Topo Sort) | Graphs | 10 | Medium | ☐ | |
| 51 | Climbing Stairs | DP | 10 | Easy | ☐ | |
| 52 | House Robber | DP | 10 | Medium | ☐ | |
| 53 | Coin Change | DP | 10 | Medium | ☐ | |
| 54 | Longest Increasing Subsequence | DP | 11 | Medium | ☐ | |
| 55 | Word Break | DP | 11 | Medium | ☐ | |

**Week 12: re-solve the ten you marked hardest.** If one is still hard, it's a pattern gap, not a
memory gap — reread that pattern's "when to reach for it" section.

### The six that matter most

If you only have time to truly own six, own these. Each is the purest expression of its pattern, and
each is asked constantly:

**Two Sum** (hash complement) · **3Sum** (two pointers + dedup) · **Longest Substring Without
Repeating** (variable window) · **Daily Temperatures** (monotonic stack) · **Number of Islands**
(flood fill) · **Coin Change** (DP from recursion).

---

## 28. Interview Communication

The code is maybe half the score. The rest is how you work.

**Think out loud, always.** Silence reads as being stuck. "I'm considering a hash map here because…"
is worth more than the same idea arrived at silently.

**Ask before assuming.** Can the input be empty? Are there duplicates? Is it sorted? Can values be
negative? How large is n? Each question is a point in your favour, and the answers narrow the solution.

**State the brute force before optimising.** It proves you understand the problem, and it's your
fallback if time runs out. Never skip it, even when you already see the optimal answer.

**Write the complexity down as you go**, before you're asked.

**When stuck, say what you've ruled out.** "Sorting doesn't help because it destroys the index
mapping" invites a hint. Sitting silently doesn't.

**Test out loud.** Walk your normal case through the code line by line, then your edge case. Catching
your own off-by-one is a strong signal.

**Take the hint.** An interviewer offering one isn't a failure — ignoring it is.

### The three things that lose offers

1. **Silence.** They can't score reasoning they can't hear.
2. **Coding immediately.** Two minutes of clarifying and planning saves fifteen of rewriting.
3. **Defending a wrong answer.** When they push back, re-check. Say "let me trace that case" and
   actually trace it.

### The end-of-round question

Have one ready. "What does the data platform look like today — where does most of the pipeline
complexity live?" beats "what's the culture like." It's the same principle as the whole file: be
specific.

---

## Sources

- `java-springboot-complete-notes/JAVA-COMPLETE-NOTES.md` **Part 23** — Problem Solving: DSA Patterns
  and Complexity. Searching, sorting, the data-structure complexity table, the core patterns and the
  problem-solving method. The seed this file grew from.
- `dsa/logic-building-study-guide.html` — the source for **§0, Logic Before DSA**: the Seven Steps
  (from Duke's Programming Fundamentals course), the stuck-strategies table (from *Think Like a
  Programmer* by V. Anton Spraul), trace tables, the language traps and the two-week on-ramp.
- `dsa/1788750814842.pdf` — "25 DSA Patterns That Solve 80% of Coding Interview Problems" by
  **@AdarsChetan**. Used as a taxonomy to audit coverage; it's what identified §16–§24 as gaps.
  The pattern map in §25 follows its numbering.
- **Problem set:** NeetCode 150 pattern order, trimmed to 55 problems across 12 weeks.
- **Language idioms:** cross-checked against `javascriptnotes/JAVASCRIPT-COMPLETE-NOTES.md`,
  `Python  Notes and Interview/PYTHON-LEARNING-NOTES.md` and `JAVA-COMPLETE-NOTES.md` Parts 16 and 19.

### Further reading, not reproduced here

`dsa/DSA_Complete_Interview_Guide_1760994845.pdf` is **"Data Structures and Algorithms Made Easy" by
Narasimha Karumanchi** (CareerMonk Publications, 2017) — a commercially published, copyrighted book
carrying an explicit all-rights-reserved notice. Its text, problem sets and diagrams are **not**
reproduced in this file, and shouldn't be.

It's a good reference, so here's a map from this file to its chapters when you want to go deeper.
Read it there; write your own notes from it.

| This file | That book |
|---|---|
| §2 Complexity · §21 Master Theorem, amortized | Ch 1 — Introduction (1.13–1.28) |
| §13 Backtracking | Ch 2 — Recursion and Backtracking |
| §10, §18 Linked lists, fast/slow | Ch 3 — Linked Lists |
| §8, §19 Stack, monotonic queue | Ch 4 — Stacks · Ch 5 — Queues |
| §11 Trees | Ch 6 — Trees |
| §12 Heap | Ch 7 — Priority Queues and Heaps |
| §22 Union-Find | Ch 8 — Disjoint Sets ADT |
| §14 Graphs | Ch 9 — Graph Algorithms |
| §21 Sorting · §9 Binary search | Ch 10 — Sorting · Ch 11 — Searching |
| §12.1 Quickselect | Ch 12 — Selection Algorithms |
| §5 Hashing | Ch 14 — Hashing |
| §23 Trie · string problems | Ch 15 — String Algorithms |
| §20 Greedy · §21 Divide and conquer · §15 DP | Ch 16–19 — Algorithm Design Techniques |

Every solution here is written to be typed from memory in an interview — no library shortcuts that
hide the algorithm, and the language-specific traps called out where they bite.
