---
title: DSA_Patterns_JavaScript_Study_Notes
topic: dsa
source_type: my-notes
source_file: STUDYNOTEs/DSA_Patterns_JavaScript_Study_Notes.md
---

# DSA Patterns in JavaScript

*Recognition clues • mental models • reusable templates • traps • practice problems*

**How to use these notes:** Do not memorize code line-by-line. First identify the clue in the problem, state the brute-force approach, identify repeated work, then choose the pattern. The templates below are concise JavaScript adaptations synthesized from the linked LeetCode study guides, including the sliding-window and dynamic-programming posts; they are not verbatim reproductions.

## 1. Pattern Recognition Map

| Pattern | Recognition clue |
|---|---|
| HashMap / Set | lookup, frequency, duplicates, complement, grouping |
| Two Pointers | sorted pair, opposite ends, in-place scanning |
| Sliding Window | contiguous subarray/substring; longest/shortest/count |
| Prefix / Suffix | information before/after each index; repeated range work |
| Binary Search | sorted data or monotonic true/false search space |
| Fast & Slow | cycle, linked-list middle, repeated-state traversal |
| Stack | matching/nesting, undo, deferred processing |
| Monotonic Stack | next/previous greater or smaller |
| Heap / Top K | K largest/smallest/most frequent; repeated min/max |
| Tree DFS | explore branches; subtree answers |
| Tree BFS | levels, shallowest/closest |
| Graph DFS/BFS | reachability, components, islands |
| Backtracking | all combinations/permutations/configurations |
| Dynamic Programming | overlapping subproblems + choices + optimal/count result |
| Intervals | overlap/merge/scheduling ranges |
| Bit Manipulation | XOR, masks, binary states, powers of two |
| Linked-list reversal (20.1) | reverse all or part of a list, in groups, or check a palindrome in O(1) space |
| Greedy (20.2) | a locally best choice is never undone; sort, then sweep |
| Shortest path / Dijkstra (20.3) | cheapest route in a weighted graph with non-negative edges |
| Grid traversal (20.4) | 2D grid with four neighbours: islands, flood fill, steps |
| Trie (20.5) | many words, prefix queries, autocomplete |

## 2. HashMap / Set

**Look for:** “Have I seen this?”, frequency counting, duplicates, complements, grouping by a signature.

**Mental model:** Store information now so a later lookup is O(1) on average.

### JavaScript template

```javascript
// Set: membership / duplicate
const seen = new Set();
for (const x of nums) {
  if (seen.has(x)) { /* found */ }
  seen.add(x);
}

// Map: frequency
const freq = new Map();
for (const x of nums) {
  freq.set(x, (freq.get(x) || 0) + 1);
}

// Complement: Two Sum
const pos = new Map();
for (let i = 0; i < nums.length; i++) {
  const need = target - nums[i];
  if (pos.has(need)) return [pos.get(need), i];
  pos.set(nums[i], i);
}
```

**Common traps:** Map uses .set/.get/.has and Set uses .add/.has. Use .size, not .length. Do not use map[key] for Map. Objects/arrays used as Map/Set keys compare by reference.

**Practice:** Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Top K Frequent Elements.

## 3. Two Pointers

**Look for:** sorted array + pair condition; compare opposite ends; remove/compact in place.

**Mental model:** Maintain two meaningful positions and move only the pointer that can improve the condition.

### JavaScript template

```javascript
let left = 0;
let right = nums.length - 1;

while (left < right) {
  const value = nums[left] + nums[right];

  if (value === target) return [left, right];
  if (value < target) left++;
  else right--;
}
```

**Common traps:** Two pointers are justified by structure (often sorting), not merely because a problem has two values.

**Practice:** Valid Palindrome, Two Sum II, Container With Most Water, 3Sum.

## 4. Sliding Window — adapted from the linked sliding-window posts

**Look for:** contiguous substring/subarray + longest, shortest, maximum, minimum, or count.

**Mental model:** Expand the right edge; when the window violates the rule, shrink the left edge. Each pointer normally moves forward only.

### JavaScript template

```javascript
// A. Fixed-size window
let left = 0;
let state = 0;

for (let right = 0; right < nums.length; right++) {
  state += nums[right];

  if (right - left + 1 > k) {
    state -= nums[left];
    left++;
  }

  if (right - left + 1 === k) {
    // update answer from current window
  }
}

// B. Variable-size window
left = 0;
for (let right = 0; right < nums.length; right++) {
  // include nums[right] in state

  while (/* window is invalid */) {
    // remove nums[left] from state
    left++;
  }

  // current window [left..right] is valid
  // update longest/shortest/count answer
}

// C. String window with frequency map
const count = new Map();
left = 0;

for (let right = 0; right < s.length; right++) {
  count.set(s[right], (count.get(s[right]) || 0) + 1);

  while (/* frequency constraint violated */) {
    const ch = s[left++];
    count.set(ch, count.get(ch) - 1);
    if (count.get(ch) === 0) count.delete(ch);
  }

  // update answer
}
```

**Common traps:** Sliding window generally requires a contiguous region. An inner while-loop does not automatically make it O(n²): if left and right each move forward at most n times, the scan is typically O(n).

**Practice:** Maximum Average Subarray I, Longest Substring Without Repeating Characters, Minimum Window Substring, Find All Anagrams in a String.

## 5. Prefix / Suffix

**Look for:** answer at i depends on everything before i and/or after i; repeated range calculation.

**Mental model:** Precompute accumulated information so each index can be answered without rescanning.

### JavaScript template

```javascript
const n = nums.length;
const prefix = new Array(n).fill(1);
const suffix = new Array(n).fill(1);

for (let i = 1; i < n; i++) {
  prefix[i] = prefix[i - 1] * nums[i - 1];
}

for (let i = n - 2; i >= 0; i--) {
  suffix[i] = suffix[i + 1] * nums[i + 1];
}

const ans = nums.map((_, i) => prefix[i] * suffix[i]);
```

**Practice:** Product of Array Except Self, Range Sum Query, Subarray Sum Equals K.

## 6. Binary Search

**Look for:** sorted values OR a monotonic condition such as false,false,false,true,true.

**Mental model:** Ask whether one comparison lets you discard half the remaining search space.

### JavaScript template

```javascript
let left = 0;
let right = nums.length - 1;

while (left <= right) {
  const mid = left + Math.floor((right - left) / 2);

  if (nums[mid] === target) return mid;
  if (nums[mid] < target) left = mid + 1;
  else right = mid - 1;
}
return -1;

// Boundary / answer-space idea:
// if (condition(mid)) right = mid;
// else left = mid + 1;
```

**Common traps:** Be explicit about whether right is inclusive or exclusive. Most binary-search bugs are boundary-definition bugs.

**Practice:** Binary Search, Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Koko Eating Bananas.

## 7. Fast & Slow Pointers

**Look for:** linked-list cycle, middle node, repeated-state/circular movement.

**Mental model:** One pointer moves one step; another moves two. In a cycle, they eventually meet.

### JavaScript template

```javascript
let slow = head;
let fast = head;

while (fast && fast.next) {
  slow = slow.next;
  fast = fast.next.next;
  if (slow === fast) return true;
}
return false;
```

**Practice:** Linked List Cycle, Middle of the Linked List, Find the Duplicate Number.

## 8. Stack / Monotonic Stack

**Look for:** nested matching for a normal stack; next/previous greater/smaller for monotonic stack.

**Mental model:** Keep unresolved items. A new item may resolve one or more items on the top.

### JavaScript template

```javascript
// Monotonic stack: next greater index
const stack = [];
const ans = new Array(nums.length).fill(-1);

for (let i = 0; i < nums.length; i++) {
  while (stack.length &&
         nums[i] > nums[stack[stack.length - 1]]) {
    const j = stack.pop();
    ans[j] = i;
  }
  stack.push(i);
}
```

**Common traps:** Decide whether the stack stores values or indexes. For distance/span questions, indexes are usually more useful.

**Practice:** Valid Parentheses, Daily Temperatures, Next Greater Element, Largest Rectangle in Histogram.

## 9. Heap / Top K

**Look for:** top K, kth largest/smallest, repeatedly extract min/max.

**Mental model:** Keep only the best K candidates instead of sorting everything when appropriate.

### JavaScript template

```javascript
// Conceptual min-heap strategy for top K:
// for each candidate:
//   push candidate
//   if heap.size > k: pop minimum
// heap now contains the best k
//
// On LeetCode, heap API availability can differ by environment;
// learn the invariant before memorizing library syntax.
```

**Practice:** Top K Frequent Elements, Kth Largest Element in an Array, Merge K Sorted Lists.

## 10. Tree DFS & BFS

**Look for:** DFS for branch/subtree reasoning; BFS for level order, nearest/shallowest.

**Mental model:** DFS goes deep before returning. BFS processes all nodes at one distance before the next.

### JavaScript template

```javascript
// DFS
function dfs(node) {
  if (!node) return;
  // preorder work
  dfs(node.left);
  // inorder work
  dfs(node.right);
  // postorder work
}

// BFS (use a head index to avoid repeated shift cost)
const queue = [root];
let head = 0;

while (head < queue.length) {
  const levelSize = queue.length - head;

  for (let i = 0; i < levelSize; i++) {
    const node = queue[head++];
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
}
```

**Practice:** Maximum Depth of Binary Tree, Invert Binary Tree, Binary Tree Level Order Traversal, Same Tree.

## 11. Graph DFS & BFS

**Look for:** connected components, islands, reachability, shortest unweighted path.

**Mental model:** Mark visited so each state is processed once; DFS explores a component deeply, BFS expands by distance.

### JavaScript template

```javascript
// DFS adjacency-list skeleton
const visited = new Set();

function dfs(node) {
  if (visited.has(node)) return;
  visited.add(node);

  for (const next of graph.get(node) || []) {
    dfs(next);
  }
}

// BFS
const queue = [start];
let head = 0;
visited.clear();
visited.add(start);

while (head < queue.length) {
  const node = queue[head++];

  for (const next of graph.get(node) || []) {
    if (!visited.has(next)) {
      visited.add(next);
      queue.push(next);
    }
  }
}
```

**Common traps:** Mark a node visited when enqueuing it, not later, to avoid duplicate queue entries.

**Practice:** Number of Islands, Clone Graph, Rotting Oranges, Course Schedule, Keys and Rooms.

## 12. Backtracking

**Look for:** all subsets, permutations, combinations, arrangements, paths under constraints.

**Mental model:** Choose → explore → undo. The path represents the current partial solution.

### JavaScript template

```javascript
const result = [];

function backtrack(path, choices) {
  if (/* complete solution */) {
    result.push([...path]);
    return;
  }

  for (const choice of choices) {
    if (/* choice invalid */) continue;

    path.push(choice);          // choose
    backtrack(path, choices);   // explore
    path.pop();                 // undo
  }
}
```

**Common traps:** Push a COPY of path into results: [...path]. Otherwise later mutations change the stored result.

**Practice:** Subsets, Permutations, Combination Sum, Palindrome Partitioning, N-Queens.

## 13. Dynamic Programming — adapted from the linked DP pattern posts

**Look for:** choices + repeated subproblems; count ways, min/max cost, feasibility, sequence/string/grid state.

**Mental model:** Define the state in one sentence. Write the recurrence. Add base cases. Then choose memoization or tabulation.

### JavaScript template

```javascript
// A. Top-down memoization
const memo = new Map();

function dp(state) {
  if (/* base case */) return /* base value */;

  const key = String(state); // use a stable key for multi-part state
  if (memo.has(key)) return memo.get(key);

  const answer = /* combine dp(smallerState) results */;
  memo.set(key, answer);
  return answer;
}

// B. Bottom-up 1D
const dp1 = new Array(n + 1).fill(0);
dp1[0] = /* base value */;

for (let i = 1; i <= n; i++) {
  dp1[i] = /* transition from earlier states */;
}

// C. 0/1 choice pattern
// state: best answer using first i items with capacity c
// transition:
// skip item  -> previous state
// take item  -> item value + previous state with reduced capacity
//
// Space-optimized 0/1 knapsack idea:
const best = new Array(capacity + 1).fill(0);
for (let i = 0; i < weights.length; i++) {
  for (let c = capacity; c >= weights[i]; c--) {
    best[c] = Math.max(
      best[c],
      best[c - weights[i]] + values[i]
    );
  }
}
```

**Common traps:** Before coding, finish: “dp[state] means ____.” For 0/1 knapsack space optimization, capacity moves backward so the same item is not reused in the same iteration. For unbounded choices, direction often changes.

**Practice:** Climbing Stairs, House Robber, Coin Change, Unique Paths, Longest Common Subsequence, Target Sum, 0/1 Knapsack family.

## 14. Intervals

**Look for:** ranges with start/end; overlaps; scheduling.

**Mental model:** Sort by a meaningful endpoint, then compare the current interval with the last accepted/merged interval.

### JavaScript template

```javascript
intervals.sort((a, b) => a[0] - b[0]);
const merged = [];

for (const cur of intervals) {
  if (!merged.length ||
      merged[merged.length - 1][1] < cur[0]) {
    merged.push([...cur]);
  } else {
    merged[merged.length - 1][1] =
      Math.max(merged[merged.length - 1][1], cur[1]);
  }
}
```

**Practice:** Merge Intervals, Insert Interval, Non-overlapping Intervals, Meeting Rooms.

## 15. Bit Manipulation

**Look for:** XOR cancellation, bit flags/masks, odd/even, powers of two.

**Mental model:** Represent boolean state in bits and use bitwise operations to test/change state.

### JavaScript template

```javascript
// test bit i
const isSet = (n & (1 << i)) !== 0;

// set / clear / toggle
n = n | (1 << i);
n = n & ~(1 << i);
n = n ^ (1 << i);

// XOR cancellation
let x = 0;
for (const n of nums) x ^= n;
// x ^ x = 0; x ^ 0 = x
```

**Practice:** Single Number, Counting Bits, Number of 1 Bits, Subsets via bitmask.

## 16. Your Current Problems → Pattern

| Problem | Pattern | Recognition thought |
|---|---|---|
| Two Sum | HashMap + complement | For current x, need target - x; have I seen it? |
| Two Sum II | Two pointers | Sorted + pair target. |
| Valid Palindrome | Two pointers | Compare opposite ends after skipping/cleaning non-alphanumerics. |
| Group Anagrams | HashMap + signature | Group strings that share the same canonical representation. |
| Top K Frequent | Frequency map + bucket/heap | Count first, then select the best K. |
| Product Except Self | Prefix/suffix | Answer at i = information left of i × information right of i. |

## 17. JavaScript DSA Traps

**Loop boundary:** Use i < nums.length, not i <= nums.length.

**Block scope:** let i inside for(...) is scoped to that loop/block; use braces.

**Assignment vs comparison:** = assigns; === compares.

**Map:** map.set(k,v), map.get(k), map.has(k), map.size.

**Set:** set.add(v), set.has(v), set.size; iterate with for...of.

**Falsy index 0:** Do not use if (seen[x]) when 0 is a valid stored value; use Map.has or x in object.

**Queue performance:** For BFS, prefer an array + head index over repeated Array.shift() for large inputs.

**Deep copy:** JSON.parse(JSON.stringify(x)) loses/changes unsupported JS values and Map/Set; structuredClone supports many more built-in types.

**Object identity:** Two separately created arrays/objects are different Map/Set keys even if contents look identical.

## 18. Problem-Solving Checklist

1. What exactly is the output: pair, count, maximum/minimum, path, group, boolean?

2. What special property is given: sorted, contiguous, unique, tree, graph, positive values, K?

3. What is the brute-force solution?

4. What work does brute force repeat?

5. Can a Map/Set remember that work?

6. Does sorted order justify two pointers or binary search?

7. Is the region contiguous, suggesting a sliding window or prefix sum?

8. Is this “all possibilities,” suggesting backtracking?

9. Are the same states solved repeatedly, suggesting DP?

10. State the invariant before coding: what must remain true while the loop/recursion runs?

## 19. Source Notes

**LeetCode collection of famous template/pattern posts:** https://leetcode.com/discuss/post/2007535/

**Sliding-window substring template:** https://leetcode.com/discuss/post/136523/

**Dynamic Programming Patterns (0/1 knapsack and related families):** https://leetcode.com/discuss/post/1437879/

**LeetCode study-guide collection / pattern index:** https://leetcode.com/discuss/post/1367727/

**"20 DSA patterns" list that section 20 is organised around (Ashish Pratap Singh, 19 Jan 2026):** https://blog.algomaster.io/p/20-dsa-patterns

**Copyright note:** The templates in this notebook are original, compact JavaScript study adaptations based on the concepts in the linked resources. They intentionally do not reproduce the source posts verbatim. Section 20 was written the same way: the pattern names and problem numbers come from the list above, and the JavaScript templates and examples are original and were run to check them.

## 20. More patterns: the ones sections 2–15 do not cover

**Added 22 Oct 2026.** A popular "20 DSA patterns" list (see Source Notes) names twenty families. Fifteen of them already have a section above. These five did not, so this part adds them, with original JavaScript templates that were run and checked.

| New section | Recognition clue |
|---|---|
| 20.1 Linked-list in-place reversal | reverse all or part of a list, in groups, or check a list for a palindrome, with O(1) extra space |
| 20.2 Greedy | one locally best choice at each step never has to be undone (sort, then sweep) |
| 20.3 Shortest path (Dijkstra) | cheapest route in a graph whose edges have non-negative weights |
| 20.4 Grid / matrix traversal | a 2D grid with neighbours up, down, left, right: islands, flood fill, shortest steps |
| 20.5 Trie (prefix search) | many words, prefix queries, autocomplete, "starts with" |

### 20.1 Linked-list in-place reversal

**Look for:** reverse a list or a section of it, swap nodes in pairs, reverse in groups of k, or compare the second half of a list with the first (palindrome).

**Idea:** walk the list once and turn each `next` pointer around. Three variables are enough: `prev`, `curr` and `next`. Save `next` **before** you overwrite `curr.next`, or you lose the rest of the list.

```js
class ListNode {
  constructor(val, next = null) { this.val = val; this.next = next; }
}
const fromArray = (a) => a.reduceRight((next, val) => new ListNode(val, next), null);
const toArray = (head) => { const out = []; for (let n = head; n; n = n.next) out.push(n.val); return out; };

// Reverse the whole list
function reverseList(head) {
  let prev = null;
  let curr = head;
  while (curr) {
    const next = curr.next;   // 1. remember the rest
    curr.next = prev;         // 2. turn the pointer around
    prev = curr;              // 3. step forward
    curr = next;
  }
  return prev;                // prev is the new head
}

// Reverse only positions left..right (1-based). A dummy node means the head can change safely.
function reverseBetween(head, left, right) {
  const dummy = new ListNode(0, head);
  let before = dummy;
  for (let i = 1; i < left; i++) before = before.next;   // the node just before position `left`

  let curr = before.next;
  for (let i = 0; i < right - left; i++) {
    const moving = curr.next;          // take the next node...
    curr.next = moving.next;
    moving.next = before.next;         // ...and put it at the front of the reversed section
    before.next = moving;
  }
  return dummy.next;
}

console.log(toArray(reverseList(fromArray([1, 2, 3, 4, 5]))));            // => [ 5, 4, 3, 2, 1 ]
console.log(toArray(reverseBetween(fromArray([1, 2, 3, 4, 5]), 2, 4)));   // => [ 1, 4, 3, 2, 5 ]
console.log(toArray(reverseBetween(fromArray([1, 2, 3, 4, 5]), 1, 5)));   // => [ 5, 4, 3, 2, 1 ]
console.log(toArray(reverseList(null)));                                  // => []
```

**Traps:** forgetting to save `next` first; returning `head` instead of `prev` after a full reversal; using no dummy node when `left` is 1.
**Practice:** Reverse Linked List (206), Reverse Linked List II (92), Swap Nodes in Pairs (24), Reverse Nodes in k-Group (25), Palindrome Linked List (234).
**Complexity:** O(n) time, O(1) space.

### 20.2 Greedy

**Look for:** "maximum number of...", "minimum number of...", scheduling, or reachability, where a locally best choice can be proved never to hurt later. If you cannot argue why the greedy choice is safe, suspect DP.

**Idea:** usually **sort by the right key, then sweep once**, keeping a little state. For choosing the most non-overlapping intervals the right key is the **end** time: finishing earliest leaves the most room.

```js
// Most non-overlapping intervals: sort by END time, keep an interval if it starts after the last kept one ended
function maxNonOverlapping(intervals) {
  const sorted = [...intervals].sort((a, b) => a[1] - b[1]);
  let count = 0;
  let lastEnd = -Infinity;
  for (const [start, end] of sorted) {
    if (start >= lastEnd) {   // fits after the last chosen one
      count++;
      lastEnd = end;
    }
  }
  return count;
}

// Jump Game: track the farthest index reachable so far; if you stand beyond it, you are stuck
function canJump(nums) {
  let farthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false;
    farthest = Math.max(farthest, i + nums[i]);
  }
  return true;
}

console.log(maxNonOverlapping([[1, 3], [2, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]]));   // => 4
console.log(canJump([2, 3, 1, 1, 4]));   // => true
console.log(canJump([3, 2, 1, 0, 4]));   // => false
```

**Traps:** sorting by start time when the end time is the right key; assuming greedy works for something like coin change with arbitrary coins (it does not, which is why that is a DP problem).
**Practice:** Jump Game (55), Jump Game II (45), Gas Station (134), Non-overlapping Intervals (435), Partition Labels (763), Task Scheduler (621).
**Complexity:** O(n log n) for the sort, then O(n).

### 20.3 Shortest path (Dijkstra)

**Look for:** a graph with weights on the edges and a question like "cheapest way from A to every node" or "minimum time for a signal to reach all nodes". With **unweighted** edges, plain BFS is enough. Dijkstra needs **non-negative** weights (negative weights need Bellman-Ford).

**Idea:** keep the best known distance to each node. Repeatedly take the unfinished node with the **smallest** distance from a min-heap and try to improve its neighbours. JavaScript has no built-in heap, so write a small one.

```js
class MinHeap {
  constructor() { this.a = []; }
  get size() { return this.a.length; }
  push(item) {                          // item is [priority, value]
    const a = this.a; a.push(item);
    let i = a.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (a[p][0] <= a[i][0]) break;
      [a[p], a[i]] = [a[i], a[p]]; i = p;
    }
  }
  pop() {
    const a = this.a; const top = a[0]; const last = a.pop();
    if (a.length) {
      a[0] = last;
      let i = 0;
      while (true) {
        let l = 2 * i + 1, r = l + 1, m = i;
        if (l < a.length && a[l][0] < a[m][0]) m = l;
        if (r < a.length && a[r][0] < a[m][0]) m = r;
        if (m === i) break;
        [a[m], a[i]] = [a[i], a[m]]; i = m;
      }
    }
    return top;
  }
}

// edges: [from, to, weight]; nodes are 1..n. Returns the distance to every node.
function dijkstra(n, edges, source) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [u, v, w] of edges) graph[u].push([v, w]);

  const dist = Array(n + 1).fill(Infinity);
  dist[source] = 0;
  const heap = new MinHeap();
  heap.push([0, source]);

  while (heap.size) {
    const [d, node] = heap.pop();
    if (d > dist[node]) continue;               // a better route was already found: skip this stale entry
    for (const [next, w] of graph[node]) {
      if (d + w < dist[next]) {
        dist[next] = d + w;
        heap.push([dist[next], next]);
      }
    }
  }
  return dist;
}

// Network Delay Time: time until every node has the signal, or -1 if some node is unreachable
function networkDelay(times, n, k) {
  const dist = dijkstra(n, times, k).slice(1);
  const worst = Math.max(...dist);
  return worst === Infinity ? -1 : worst;
}

console.log(networkDelay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2));   // => 2
console.log(networkDelay([[1, 2, 1]], 2, 2));                          // => -1
console.log(dijkstra(4, [[1, 2, 4], [1, 3, 1], [3, 2, 2], [2, 4, 1]], 1));   // => [ Infinity, 0, 3, 1, 4 ]
```

**Traps:** forgetting the "skip stale entries" check (it still gives the right answer, but slower); using Dijkstra with negative weights; treating unreachable nodes as 0 instead of `Infinity`.
**Practice:** Network Delay Time (743), Cheapest Flights Within K Stops (787), Path With Minimum Effort (1631), Swim in Rising Water (778), Path with Maximum Probability (1514).
**Complexity:** O((V + E) log V) with a heap.

### 20.4 Grid / matrix traversal

**Look for:** a 2D array where each cell connects to its neighbours: count islands, fill a region, find the shortest number of steps, spread from several sources at once (rotting oranges).

**Idea:** it is Graph DFS/BFS (section 11) where the "neighbours" are the four cells around you. Use a direction table so you write the neighbour loop once, and **check the bounds before reading** the cell.

```js
const DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]];   // down, up, right, left

// Number of Islands: DFS that sinks each island so it is counted once
function numIslands(grid) {
  const g = grid.map((row) => [...row]);            // work on a copy
  const rows = g.length, cols = g[0].length;
  let islands = 0;

  function sink(r, c) {
    if (r < 0 || r >= rows || c < 0 || c >= cols || g[r][c] !== "1") return;   // bounds first
    g[r][c] = "0";                                  // mark visited
    for (const [dr, dc] of DIRS) sink(r + dr, c + dc);
  }

  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      if (g[r][c] === "1") { islands++; sink(r, c); }
  return islands;
}

// Shortest steps from top-left to bottom-right through open cells (0 = open, 1 = wall): BFS by layers
function shortestPath(grid) {
  const rows = grid.length, cols = grid[0].length;
  if (grid[0][0] === 1 || grid[rows - 1][cols - 1] === 1) return -1;
  const seen = Array.from({ length: rows }, () => Array(cols).fill(false));
  const queue = [[0, 0, 0]];                        // [row, col, steps]
  seen[0][0] = true;
  for (let head = 0; head < queue.length; head++) { // an index instead of shift() keeps it O(1) per step
    const [r, c, steps] = queue[head];
    if (r === rows - 1 && c === cols - 1) return steps;
    for (const [dr, dc] of DIRS) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] === 0) {
        seen[nr][nc] = true;                        // mark when you ENQUEUE, not when you dequeue
        queue.push([nr, nc, steps + 1]);
      }
    }
  }
  return -1;
}

const islandGrid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];
console.log(numIslands(islandGrid));                                       // => 3
console.log(shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0]]));              // => 4
console.log(shortestPath([[0, 1], [1, 0]]));                               // => -1
```

**Traps:** reading `g[r][c]` before checking the bounds (the check must come first, or you read `undefined` and crash on a missing row); marking visited too late in BFS so cells enter the queue many times; using `queue.shift()` in a big BFS (it is O(n), so use an index pointer); mutating the input when the caller still needs it.
**Practice:** Number of Islands (200), Flood Fill (733), Max Area of Island (695), Surrounded Regions (130), Rotting Oranges (994), Pacific Atlantic Water Flow (417).
**Complexity:** O(rows × cols) time and space.

### 20.5 Trie (prefix search)

**Look for:** a set of words and queries about **prefixes**: does any word start with these letters, autocomplete, or find every word from a dictionary inside a grid. A hash set answers "is this whole word present?" but cannot answer "does anything start with this?" quickly.

**Idea:** a tree where each edge is one character and each node can be marked "a word ends here". Walking a prefix costs O(length of the prefix), no matter how many words are stored.

```js
class TrieNode {
  constructor() { this.children = new Map(); this.isWord = false; }
}

class Trie {
  constructor() { this.root = new TrieNode(); }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
    }
    node.isWord = true;                 // the path alone is not enough: mark where a word ends
  }

  #walk(text) {                         // follow `text`; return the last node, or null if the path breaks
    let node = this.root;
    for (const ch of text) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node;
  }

  search(word) { const n = this.#walk(word); return n !== null && n.isWord; }
  startsWith(prefix) { return this.#walk(prefix) !== null; }
}

const trie = new Trie();
trie.insert("apple");
console.log(trie.search("apple"));       // => true
console.log(trie.search("app"));         // => false
// "app" is a prefix of "apple", but no word ends there, so search is false while startsWith is true
console.log(trie.startsWith("app"));     // => true
trie.insert("app");
console.log(trie.search("app"));         // => true
console.log(trie.startsWith("b"));       // => false
```

**Traps:** returning true for `search("app")` just because the path exists (check `isWord`); using a 26-slot array for input that is not only lowercase letters (a `Map` is safer); building a trie for a problem a plain `Set` solves.
**Practice:** Implement Trie (208), Design Add and Search Words (211), Word Search II (212), Replace Words (648), Longest Word in Dictionary (720).
**Complexity:** insert, search and prefix check are O(L) for a word of length L; space is O(total characters stored).

### 20.6 The twenty patterns and where each lives in this notebook

| # | Pattern | Section |
|---|---|---|
| 1 | Prefix sum | 5 |
| 2 | Two pointers | 3 |
| 3 | Sliding window | 4 |
| 4 | Fast and slow pointers | 7 |
| 5 | Linked-list in-place reversal | 20.1 |
| 6 | Frequency counting | 2 |
| 7 | Monotonic stack | 8 |
| 8 | Bit manipulation | 15 |
| 9 | Top K elements | 9 |
| 10 | Overlapping intervals | 14 |
| 11 | Modified binary search | 6 |
| 12 | Binary tree traversal | 10 |
| 13 | Depth-first search | 10 and 11 |
| 14 | Breadth-first search | 10 and 11 |
| 15 | Shortest path | 20.3 |
| 16 | Matrix traversal | 20.4 |
| 17 | Backtracking | 12 |
| 18 | Trie (prefix search) | 20.5 |
| 19 | Greedy | 20.2 |
| 20 | Dynamic programming families (Fibonacci-style, 0/1 knapsack, longest common subsequence, longest increasing subsequence) | 13 |

For your daily schedule: Week 3 covers the stack patterns (Valid Parentheses, Min Stack, Evaluate RPN, Daily Temperatures), which are section 8 here.
