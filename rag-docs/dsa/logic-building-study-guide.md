---
title: logic-building-study-guide
topic: dsa
source_type: my-notes
source_file: STUDYNOTEs/logic-building-study-guide.html
---

Logic before DSA

Work it out on paper first. Then write the code.

Progress: 0 of 0 done

Cheat sheet

Flashcards

Quiz

Trace practice

Progress

The Seven Steps

From Duke's Programming Fundamentals course. Steps 1 to 4 happen on paper. Never start at step 5.

1.  Solve one small example by hand. Take "([)]" and check it yourself.
2.  Write down exactly what you did. "Saw (, remembered it. Saw [, remembered it. Saw ), but the last one I remembered was [, so it's invalid."
3.  Generalize. "A closer must match the most recent opener." That's a stack, and you found it yourself.
4.  Test the steps by hand on edge cases. Empty input, one item, duplicates, zero or negatives.
5.  Write the code. Now syntax is the easy part.
6.  Run the tests.
7.  Debug by tracing, not by guessing and re-running.

What to do when stuck

From Think Like a Programmer by V. Anton Spraul, summarized.

  Strategy                   What it means                                                       Example
  -------------------------- ------------------------------------------------------------------- -----------------------------------------------------------------
  Have a plan                Always know your next move, even if it's "try a tiny example"       Act instead of staring at the problem
  Restate it                 Rewrite the problem in your own words and name the exact output     Two Sum becomes "for each number, does its partner exist?"
  Divide it                  Split into subproblems you can solve separately                     Parse input, then process, then format output
  Start with what you know   Solve the part you already can                                      Write the loop first, work out the check later
  Reduce it                  Drop a constraint and solve the easier version                      Solve with no duplicates, then add duplicate handling
  Find an analogy            Ask whether you've solved something similar                         Brackets and undo both mean "most recent first," so use a stack
  Experiment                 Run small tests to learn how something behaves                      Check what map.get() returns for a missing key
  Manage frustration         Stuck 20 minutes on one approach? Switch strategy or take a break   Walking away is a valid move

Trace tables

One column per variable, one row per step. If you can't fill the table, you don't understand the code yet.

    let sum = 0;
    for (let i = 1; i <= 3; i++) sum += i;

  Step     i   sum
  -------- --- -----
  start    –   0
  loop 1   1   1
  loop 2   2   3
  loop 3   3   6

Tracing catches language traps that break correct logic. In JavaScript, 0 || 5 gives 5 because || treats 0 as "missing." 0 ?? 5 gives 0. In Java, compare strings with .equals(), not ==.

The bridge into DSA

From Daniel Zingaro's approach in Learn to Code by Solving Problems, summarized.

1.  Brute force first. Try every possibility, often with a nested loop. It gives you a correct answer to test against.
2.  Measure it. Nested loops over n items take about n × n steps.
3.  Find the repeated work. If you keep searching for something you've already seen, remember it in a hash map or set.
4.  Optimize only after the brute force is correct.

Real-world link: "Find duplicate records in today's batch" is a loop plus "have I seen this key?" In DSA that's a hash set. In Spark it's dropDuplicates() or a MERGE key. Logic first, tool second.

Skill phases

  Phase          Practice problems                                      Logic lesson
  -------------- ------------------------------------------------------ -------------------------------------
  Conditionals   FizzBuzz, leap year, largest of 3                      Order of checks matters
  Loops          Sum of digits, reverse a number, prime check           What stays true on every pass
  Arrays         Second largest, move zeros to end, count frequencies   Track state while scanning once
  Strings        Palindrome, anagram check, count words                 Two pointers and counting
  Functions      Password validator built from small checks             Decomposition
  Recursion      Factorial, power(x, n), reverse a string               Base case plus a smaller subproblem

Tick these off in the Progress tab.

Where to practice

Exercism (JavaScript or Java track)

Free, with automatic tests and human mentor feedback that catches language traps. Your main practice site.

Schoolabe logic-building problems

280+ problems grouped by phase. Use it when you run out of problems in the Progress tab.

Duke's Programming Fundamentals, week 1

Optional. Free to audit. Watch it to see the Seven Steps demonstrated.

Click or press Space to flip

Previous

Next

Shuffle

Keyboard: left and right arrows move between cards.

0 / 0 Answer each question to see the explanation.

Restart quiz

Fill in each variable's value after every step, then check your table. Grey cells are given.

Check my table

Show answers

Clear

For each problem: steps 1 to 4 on paper, then code it, then trace it.

Two-week plan

Reset all progress


## Flashcards

### Q: What is step 1 of the Seven Steps?

**A:** Solve one small example by hand, before touching any code.

### Q: Why write down exactly what you did (step 2)?

**A:** Your hand solution already contains the algorithm. Writing it down makes the hidden steps visible so you can generalize them.

### Q: What does "generalize" mean in step 3?

**A:** Replace specific values with rules that work for any input. "Compare with [" becomes "compare with the most recent opener."

### Q: When should you start writing code?

**A:** Step 5, only after your steps pass hand tests on edge cases.

### Q: Which edge cases should you test by hand every time?

**A:** Empty input, a single item, duplicates or all-same values, zero or negatives, and very large input.

### Q: What is the "restate" strategy?

**A:** Rewrite the problem in your own words and name the exact output. Two Sum becomes "for each number, does target minus it exist?"

### Q: What is the "reduce" strategy?

**A:** Drop a constraint, solve the easier version, then add the constraint back.

### Q: What is the "divide" strategy?

**A:** Split the problem into subproblems you can solve separately, like parse, then process, then format.

### Q: Brackets and undo/redo share one pattern. What is it?

**A:** "Most recent first," which means a stack. That is the analogy strategy.

### Q: You have been stuck for 20+ minutes on one approach. What now?

**A:** Switch strategy (restate, reduce, or a smaller example) or take a short break. Note exactly where you got stuck.

### Q: What is a trace table?

**A:** A table with one column per variable and one row per executed step, showing each value as the code runs.

### Q: Why trace instead of just running the code?

**A:** Running tells you the answer is wrong. Tracing tells you which line and which value made it wrong.

### Q: Why write a brute-force solution first?

**A:** It gives you a correct baseline to test against and shows you where the repeated work is.

### Q: What signal tells you to use a hash map or set?

**A:** You keep searching for something you have already seen. Remember it once, look it up instantly.

### Q: Nested loops over n items cost roughly how much?

**A:** About n × n steps, written O(n²).

### Q: JavaScript: what do 0 || 5 and 0 ?? 5 return?

**A:** 0 || 5 returns 5, because || treats 0, "" and false as missing. 0 ?? 5 returns 0, because ?? only replaces null and undefined.

### Q: JavaScript: why use Map instead of a plain object for counting?

**A:** Map keeps key types (1 and "1" stay different), has .size, and has no inherited keys. Objects turn every key into a string.

### Q: Java: what is the difference between == and .equals() for Strings?

**A:** == checks whether both are the same object in memory. .equals() checks whether the text is the same. Use .equals().
