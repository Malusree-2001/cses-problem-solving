# 1083 - Missing Number

**Link:** https://cses.fi/problemset/task/1083
**Status:** Accepted. 14/14 tests passed, slowest test 0.07 s (limit 1.00 s).
**Language:** C++ (C++20)

## Problem in my own words
The input has n, then n − 1 distinct numbers, each between 1 and n. Exactly one value from 1 to n is missing. Print it.

- Input size: 2 ≤ n ≤ 2 × 10^5
- Numbers can come in any order. The input is not sorted.

## Concepts used
- Arithmetic series formula: the sum of 1 to n is n × (n + 1) / 2
- Running total in a `for` loop
- Reading input one value at a time with `cin`
- `long long` for values that can exceed the `int` range

## Key idea
The sum of 1 to n covers every value. The input covers every value except the missing one. So:

missing = (sum of 1 to n) − (sum of the input numbers)

Binary search would need the input sorted, and sorting costs more time than this method.

## Approach
1. Read n.
2. Compute the expected sum: `n * (n + 1) / 2`.
3. Loop n − 1 times. Each time, read one number and add it to `total`.
4. Print `sum − total`.

Worked example: n = 5, input `2 3 1 5`.
- Expected sum: 5 × 6 / 2 = 15
- Input sum: 2 + 3 + 1 + 5 = 11
- Missing: 15 − 11 = 4

## Final code
```cpp
#include <iostream>
using namespace std;
int main(){
    long long n;
    cin >> n;
    long long sum = n * (n + 1) / 2;
    long long total = 0;
    for (long long i = 0; i < n - 1; i++)
    {
        long long x;
        cin >> x;
        total += x;
    }
    cout << sum - total;
}
```

## Why each part is needed
- `long long n` and `sum`: for n near 200,000, `n * (n + 1)` is about 4 × 10^10, which overflows `int`.
- `i < n - 1`: the input holds n − 1 numbers. Looping to `n` would try to read one number too many.
- `long long x` inside the loop: each input value is read into `x`, added to `total`, then replaced by the next value. Only one input value exists in memory at a time.
- `sum − total`: expected minus actual. The reverse gives a negative number.

## Hints used
- Sum of 1 to n is fixed, so the difference between the two sums is the missing value
- Binary search needs sorted input, and this input isn't sorted
- Confirmed the expected sum for n = 5 (15) by adding 1 + 2 + 3 + 4 + 5

## Time complexity
O(n). The loop runs n − 1 times, and each pass does a constant amount of work.

## Space complexity
O(1). The program stores only n, sum, total, i, and x, and none of them grows with n.

## Mistakes and debugging lessons

### 1. Loop bound
- **What I wrote:** `for (i = 0; i < n; i++)`
- **Mistake:** The input has n − 1 numbers. With `i < n`, the loop tries to read one extra value.
- **Fix:** `i < n - 1`

### 2. Integer overflow
- **What I wrote:** `int` for n and the sum.
- **Mistake:** `n * (n + 1)` can exceed the `int` range for large n.
- **Fix:** `long long` for n, sum, total, and x.

### 3. Subtraction order
- **What I wrote:** "present minus expected" in my pseudocode.
- **Mistake:** That gives a negative number for this problem.
- **Fix:** expected − present, which is `sum − total`.

### 4. Space complexity
- **What I guessed:** O(n), on the assumption that the input is stored.
- **Mistake:** The program reads each number into `x` and never keeps it.
- **Correct answer:** O(1). Only fixed-size variables are used.

### 5. Describing `total`
- **What I said:** That `total` keeps n − 1 numbers.
- **Mistake:** `total` is one running sum, not a list.
- **Correct answer:** One number, updated after each read.

## Key takeaway
When a set of values is complete except for one, compare the sum of the full range with the sum of what you have. The difference is the missing value. This needs one pass and constant extra memory.

## Suggested commit message
Solve CSES 1083 Missing Number (O(n) time, O(1) space)