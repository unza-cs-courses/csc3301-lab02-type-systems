# Lab 2: Type Systems and Type Checking

**CSC3301 Programming Language Paradigms**  
**Estimated Time:** 2–3 hours  
**Points:** 100

---

## Purpose

This lab explores type systems: how programming languages categorize values and enforce constraints at compile-time or runtime. You will add type hints to Python code, implement a simple type checker for an expression language, and analyze type coercion across different languages.

---

## Learning Outcomes

By completing this lab, you will be able to:

1. Add comprehensive type annotations to Python code
2. Use mypy for static type checking
3. Implement a basic type checker using pattern matching
4. Distinguish between static and dynamic typing trade-offs
5. Identify safe vs unsafe type coercions

---

## Tasks

### Task 1: Type Annotations (20 points)

Open `src/task1_annotations.py`. Add complete type hints to all functions and the class so that `mypy --strict` passes with zero errors.

```bash
mypy src/task1_annotations.py --strict
```

### Task 2: Expression Type Checker (40 points)

Open `src/task2_type_checker.py`. Implement the `type_check(expr)` function that determines the type of expressions in a simple language:

- Types: `Int`, `Float`, `Bool`, `String`
- Operations: `+`, `-`, `*`, `/`, `==`, `<`, `>`, `and`, `or`, `++` (string concat)
- Type rules are specified in the file

### Task 3: Type Coercion Analysis (20 points)

Open `src/task3_coercion.py`. Document 9 examples of type coercion (3 each from Python, JavaScript, C) and implement a `safe_add()` function that rejects unsafe coercions.

### Task 4: Static vs Dynamic Trade-offs (20 points)

Open `src/task4_tradeoffs.py`. Implement a `PriorityQueue` twice:
- Duck-typed version (dynamic)
- Generic typed version with type bounds (static)

Include a 200-word analysis in the docstring.

---

## Submission

1. Ensure `mypy --strict` passes on Task 1
2. All tests pass: `pytest tests/ -v`
3. Complete `SUBMISSION.md`
4. Push to trigger autograding

---

## Grading

| Component | Points |
|-----------|--------|
| Task 1: Type Annotations | 20 |
| Task 2: Type Checker | 40 |
| Task 3: Coercion Analysis | 20 |
| Task 4: Static vs Dynamic | 20 |
| **Total** | 100 |
