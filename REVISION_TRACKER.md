# CSES Revision Tracker

Use active recall and spaced repetition to develop independent problem-solving skills. Acceptance is not the same as mastery.

## Central revision queue

| Problem | Initial revision | Next review | Confidence | Status |
|---|---|---|---|---|
| [Weird Algorithm](introductory-problems/01-weird-algorithm/) | 2026-11-26 | 2026-11-26 | Not assessed | Pending |
| [Missing Number](introductory-problems/02-Missing-number/) | 2026-11-26 | 2026-11-26 | Not assessed | Pending |

The dates above are proposed initial reviews, not completed reviews. Add Repetitions after acceptance.

## Revision methodology

| Revision | Offset | Objective | Suggested minutes |
|---|---:|---|---:|
| R0 | 0 | Understand and dry-run | 20 |
| R1 | 1 | Active recall | 5 |
| R2 | 3 | Pseudocode and edge cases | 10 |
| R3 | 7 | Independent implementation | 20 |
| R4 | 14 | Timed interview simulation | 15 |
| R5 | 30 | Compare approaches and optimize | 20 |
| R6 | 60 | Transfer to an unfamiliar problem | 25 |

### R0 — Initial revision
- [ ] Explain the problem, input, output and constraints.
- [ ] Dry-run examples manually.
- [ ] Understand brute force and the selected approach.
- [ ] Review code, mistakes, correctness and complexity.

### R1 — Day 1
- [ ] Close notes and code.
- [ ] Recall the problem and explain the algorithm aloud.
- [ ] Recall important steps and mistakes.
- [ ] Check against notes only afterward.

### R2 — Day 3
- [ ] Read only the problem statement.
- [ ] Reconstruct the algorithm and pseudocode.
- [ ] Dry-run and identify edge cases.
- [ ] Explain time and space complexity.

### R3 — Day 7
- [ ] Start with a blank source file.
- [ ] Implement without hints, AI or previous code.
- [ ] Test examples and edge cases; submit to CSES.
- [ ] Record result, time and mistakes.

### R4 — Day 14
- [ ] Set a timer and explain the problem aloud.
- [ ] Discuss brute force and justify the selected algorithm.
- [ ] Implement, test and explain complexity independently.
- [ ] Record time and possible interview follow-ups.

### R5 — Day 30
- [ ] Solve independently.
- [ ] Compare alternative approaches where applicable.
- [ ] Consider overflow, memory and changed constraints.
- [ ] Optionally implement in another language.

### R6 — Day 60
- [ ] Identify the original algorithmic pattern.
- [ ] Choose a similar but unfamiliar problem.
- [ ] Adapt, implement and test the approach independently.
- [ ] Explain differences and complexity.

## Confidence and retry rules

| Level | Meaning | Action |
|---|---|---|
| 1 | Cannot recall | Retry tomorrow |
| 2 | Significant hints required | Retry within 2 days |
| 3 | Understand but struggle to implement | Retry within 3 days |
| 4 | Independent solution and explanation | Continue schedule |
| 5 | Can transfer to unfamiliar problems | Long-term review |

A failed review remains incomplete. Add an earlier retry and adjust later dates manually if needed. Never mark a review successful merely because code looks familiar.

## Daily workflow

1. Check due reviews before solving new problems.
2. Open the problem statement, not the old solution.
3. Perform the scheduled task and record actual results in its `revision.md`.
4. Update the central queue with the next review date.
5. Continue new problems as time permits.

## Scheduler

From the repository root, run:

```bash
python scripts/revision_scheduler.py --problem "Repetitions" --folder introductory-problems/03-repetitions --start 2026-11-26
```

Use the actual initial revision date. The script generates a problem-specific `revision.md` and refuses to overwrite existing history. To list pending reviews due today or earlier:

```bash
python scripts/revision_scheduler.py --due
```

The due report scans individual `revision.md` files; the central queue is maintained manually. Mark individual schedule rows Completed only after successful review.
