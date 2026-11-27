# CSES Daily Study Workflow

## Goals

- Strengthen algorithmic thinking and programming fundamentals.
- Solve two new problems per day when feasible.
- Prioritize independent problem-solving over memorizing code.
- Retain knowledge through spaced repetition.
- Prepare for software engineering coding interviews.

## Phase 1 — Revise Previous Problems (30–45 minutes)

Run from the repository root:

```powershell
python scripts/revision_scheduler.py --due
```

- [ ] Complete assigned revision tasks.
- [ ] Recall the logic without opening previous solutions.
- [ ] Record time, hints, confidence and results in each `revision.md`.
- [ ] Mark successful revisions as completed.

## Phase 2 — Solve Each New Problem

### Step 1 — Understand the Problem (5–10 minutes)

- [ ] Read the entire problem statement.
- [ ] Explain the question in my own words.
- [ ] Identify inputs and expected outputs.
- [ ] Understand constraints.
- [ ] Manually solve the sample input.

### Step 2 — Develop the Logic (10–15 minutes)

- [ ] Identify possible algorithmic patterns.
- [ ] Think of a brute-force approach.
- [ ] Calculate its time complexity.
- [ ] Check whether it satisfies the constraints.
- [ ] Consider a more efficient approach.

### Step 3 — Design the Algorithm (5–10 minutes)

- [ ] Write the algorithm on paper.
- [ ] Write pseudocode.
- [ ] Perform a manual dry run.
- [ ] Identify edge cases.
- [ ] Explain why the algorithm works.

### Step 4 — Implementation (15–20 minutes)

- [ ] Implement independently in C++.
- [ ] Test sample inputs.
- [ ] Test edge cases.
- [ ] Debug errors independently.
- [ ] Submit to CSES.

### Step 5 — Analyze the Solution (5–10 minutes)

- [ ] Calculate time complexity.
- [ ] Calculate auxiliary space complexity.
- [ ] Consider possible optimizations.
- [ ] Explore alternative approaches if applicable.
- [ ] Implement in Python if useful.

### Step 6 — Document Learning (5–10 minutes)

- [ ] Complete `note.md`.
- [ ] Record mistakes and lessons in `MISTAKES.md` when useful.
- [ ] Identify the algorithmic pattern.
- [ ] Update `PATTERNS.md` and the relevant file in `patterns/`.
- [ ] Record the number of hints used.

### Step 7 — Schedule Revision (2–5 minutes)

After acceptance, generate the revision schedule. Example:

```powershell
python scripts/revision_scheduler.py --problem "Repetitions" --folder introductory-problems/03-repetitions
```

- [ ] Generate `revision.md`.
- [ ] Update `progress.md`.
- [ ] Update progress in `README.md`.
- [ ] Commit and push learning progress.

## Phase 3 — Rules for AI Assistance

| Time spent stuck | Action |
|---|---|
| First 15 minutes | Think independently |
| 15–25 minutes | Try examples and brute force |
| 25–35 minutes | Request a small conceptual hint |
| 35–45 minutes | Request an algorithmic hint |
| After 45 minutes | Study the approach if still stuck |
| After understanding | Close the explanation and implement independently |

Do not immediately request complete code. Record hints honestly.

## Phase 4 — Spaced Repetition

| Revision | Day | Learning objective | Task |
|---|---:|---|---|
| R0 | 0 | Understanding | Understand, dry-run and review mistakes |
| R1 | 1 | Active recall | Explain the logic without notes |
| R2 | 3 | Algorithm reconstruction | Write pseudocode and identify edge cases |
| R3 | 7 | Independent implementation | Code from scratch and submit |
| R4 | 14 | Interview simulation | Solve under a time limit and explain complexity |
| R5 | 30 | Optimization | Compare approaches and optimize where applicable |
| R6 | 60 | Knowledge transfer | Solve an unfamiliar problem using the same pattern |

Each problem has its own revision cycle. Prioritize overdue reviews and low-confidence problems.

## Recommended Daily Timetable

| Activity | Minutes |
|---|---:|
| Previous problem revision | 30 |
| New problem 1 | 60 |
| Break | 10 |
| New problem 2 | 60 |
| Documentation and GitHub | 20 |
| **Total** | **180** |

The timetable is a planning target, not a deadline. Individual step estimates total 47–80 minutes per problem including documentation and scheduling; harder problems may require more time. Reduce the number of new problems when necessary.

## Learning Sequence

Understand → Think independently → Brute force → Optimize → Pseudocode → Dry run → Implement → Test and submit → Analyze → Document → Revise → Master

## End-of-Day Checklist

- [ ] Complete scheduled revisions.
- [ ] Attempt new problems independently.
- [ ] Record accepted submissions accurately.
- [ ] Update notes, patterns and mistakes as needed.
- [ ] Generate revision schedules for newly accepted problems.
- [ ] Review Git changes and commit progress.

```powershell
git status
git add .
git commit -m "Update CSES learning and revision progress"
git push origin main
```

**One thoroughly understood problem is better than five copied solutions.**
