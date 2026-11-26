# Algorithmic Pattern Library

Use this file after attempting recall, not while testing yourself.

## Current patterns

| Pattern | Recognition clue | Example | Complexity of suggested approach |
|---|---|---|---|
| Simulation | Repeatedly apply a rule until a stopping condition | [Weird Algorithm](https://cses.fi/problemset/task/1068/) | O(k) time, O(1) auxiliary space; k is the number of steps |
| Arithmetic sum | One value missing from a known consecutive range | [Missing Number](https://cses.fi/problemset/task/1083/) | O(n) time, O(1) auxiliary space when streaming input |

These are reference approaches, not claims about the exact implementations in my repository.

## Recall prompts

### Weird Algorithm
- What determines the next value?
- When should the loop stop?
- Which integer type safely handles intermediate values?

### Missing Number
- How can the expected and observed values be compared?
- Can the problem be solved without sorting or storing the entire input?
- Where might integer overflow occur?

## Future patterns

- [ ] Linear traversal and running state
- [ ] Hashing
- [ ] Two pointers
- [ ] Sliding window
- [ ] Prefix sums
- [ ] Binary search
- [ ] Greedy
- [ ] Stack and monotonic stack
- [ ] Recursion and backtracking
- [ ] BFS and DFS
- [ ] Dynamic programming
- [ ] Union-find
- [ ] Shortest paths
- [ ] Tree traversal

## New pattern template

### Pattern name
- Recognition clues:
- Core idea:
- Invariant or correctness argument:
- Complexity:
- Common mistakes:
- Related problems:
