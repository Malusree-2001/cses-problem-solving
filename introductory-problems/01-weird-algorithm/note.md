# 1068 - Weird Algorithm

**Link:** https://cses.fi/problemset/task/1068
**Status:** Solved.

## Concepts used
- `while` loop
- `%` (modulo) to test even/odd
- Integer division `/`
- Printing values as they change

## My approach
Print the starting n. While n is not 1: if n is even, n = n / 2; otherwise n = 3 * n + 1, then print n. The loop stops at 1, so the final value 1 is printed.

## Hints used
- Meaning of `%` and integer `/`
- Where to place the print statements (before the loop and inside it)
- Fixing the type and spelling of `n`

## Time complexity
O(L), where L is the number of steps until n reaches 1.

## Space complexity
O(1). Only n is stored.

## Mistakes and debugging lessons

### 1. Expected a decimal from integer division
- **Before:** Said `7 / 2` gives 3.5.
- **Mistake:** Assumed `/` on two integers keeps the fractional part.
- **How it changed:** After a hint, answered 2 for `10 / 4`.
- **Right answer:** Integer `/` drops the fraction. `7 / 2` is 3.

### 2. Printed only the final value
- **Before:** Printed `n` only at the end, which is always 1.
- **Mistake:** Missed the intermediate values in the sequence.
- **How it changed:** Added `cout << n << " ";` before the loop and inside it, after each update.
- **Right answer:** For n = 2, the output is `2 1`. For n = 1, the output is `1`.

### 3. Type and spelling
- **Before:** Wrote `Long Long n;` and used `int`.
- **Mistake:** C++ is case-sensitive and has no `Long` type. `int` can overflow for large starting values.
- **How it changed:** Not fixed yet.
- **Right answer:** `long long n;`

## Key takeaway
Print each value at the point it's produced, and use integer division when you need the whole-number result.

## Suggested commit message
Solve CSES 1068 Weird Algorithm (solved)