````md
# Week 1 Homework: Evidence Desk Patterns

## Student Name

Sushant Thapa

---

# Summary

This homework focuses on applying core data structure patterns using Python.
The assignment includes implementing efficient solutions using dictionaries,
sets, stacks, queues, and sorting algorithms.

The main objective is to strengthen problem-solving skills while practicing
time complexity analysis and structured programming techniques.

Topics covered in this homework include:

- Frequency counting with dictionaries
- Duplicate detection using sets
- Stack matching using lists
- Lookup tables with dictionaries
- Queue processing using deque
- Sorting and scanning techniques

---

# How to Run Tests

From the repository root, run:

```bash
pytest -q
````

To run a specific test file:

```bash
pytest -q tests/test_challenges.py
```

---

# Required Problems

Completed functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

---

# Optional Challenges

Completed optional functions:

1. `process_reports`
2. `largest_time_gap`

Optional tests are skipped by default.
To run them, remove the `@pytest.mark.skip(...)` line above the optional test.

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency Counting

### Data Structure

Dictionary (`dict`)

### Approach

* Step 1: Create an empty dictionary to store counts.
* Step 2: Iterate through the evidence list.
* Step 3: Update the frequency count for each evidence label.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

### Explanation

The algorithm loops through the list once while using dictionary lookups
and updates, which operate in constant average time.

### Edge Cases Checked

* [x] Empty list
* [x] One item
* [x] Repeated items
* [x] Different labels

---

## 2. Repeat Suspect ID

### Pattern

Seen-Before Detection

### Data Structure

Set (`set`)

### Approach

* Step 1: Create an empty set called `seen_ids`.
* Step 2: Iterate through each suspect ID.
* Step 3: Return the first ID already present in the set.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

### Explanation

Each ID is visited once, and set membership checks are constant time on
average, making the solution efficient.

### Edge Cases Checked

* [x] Empty list
* [x] No repeated IDs
* [x] First two IDs match
* [x] Multiple repeated IDs

---

## 3. Evidence Tag Validator

### Pattern

Stack Matching

### Data Structure

List used as a Stack

### Approach

* Step 1: Push opening brackets onto the stack.
* Step 2: Compare closing brackets with the stack top.
* Step 3: Ensure all brackets are matched correctly.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

### Explanation

The algorithm processes each character once while maintaining nesting order
using Last-In-First-Out stack behavior.

### Edge Cases Checked

* [x] Empty string
* [x] Correctly nested tags
* [x] Mismatched tags
* [x] Closing tag before opening tag
* [x] Unclosed opening tag
* [x] Non-bracket characters

---

## 4. Alias Directory

### Pattern

Lookup Table

### Data Structure

Dictionary (`dict`)

### Approach

* Step 1: Search the alias dictionary.
* Step 2: Return the matching real name or `None`.

### Complexity

* Time: `O(1)`
* Space: `O(1)`

### Explanation

Dictionary lookup operations are constant average time.

### Edge Cases Checked

* [x] Known alias
* [x] Unknown alias
* [x] Empty dictionary

---

# Assistance & Sources

## AI Used?

* [x] Yes
* [ ] No

## If yes, what did AI help with?

* Improving documentation formatting
* Reviewing algorithm complexity
* Refining code structure and readability

## Other Sources

* Python Official Documentation
* Course Lecture Slides
* Classroom Notes

```
```
