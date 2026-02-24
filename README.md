# Lab 2: Type Systems and Type Checking

**CSC3301 Programming Language Paradigms**
**Estimated Time:** 2-3 hours
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
2. Run all tests locally and ensure they pass: `pytest tests/ -v`
3. Complete `SUBMISSION.md`
4. Push your code to your repository before the deadline

---

## Grading

| Component | Points |
|-----------|--------|
| Task 1: Type Annotations | 20 |
| Task 2: Type Checker | 40 |
| Task 3: Coercion Analysis | 20 |
| Task 4: Static vs Dynamic | 20 |
| **Total** | 100 |

---

## Variant System

This lab uses a **variant-based assignment system** to provide each student with unique type coercion examples and type checking expressions.

### How It Works

1. **Automatic Generation**: When you accept this assignment through GitHub Classroom, a unique variant is automatically generated based on your GitHub username.

2. **Variant Configuration**: Your personalized configuration is stored in `.variant_config.json` and includes:
   - 3 Python type coercion examples
   - 3 JavaScript type coercion examples
   - 3 C type coercion examples
   - 6 type checking expressions for Task 2

3. **Personalized Assignment**: After variant generation, check `ASSIGNMENT.md` for your specific examples and expressions.

### Variant Components

#### Type Coercion Examples
Each student receives a unique set of type coercion examples from each language:

- **Python**: Examples of implicit type promotion, boolean conversion, string operations
- **JavaScript**: Examples of type coercion in arithmetic, comparison, and concatenation
- **C**: Examples of narrowing/widening conversions, signed/unsigned issues

#### Type Checking Expressions
Students receive different expressions to test their type checker implementation, including:
- Arithmetic operations with integers and floats
- String concatenation
- Boolean operations
- Comparison expressions
- Type error cases

### Testing with Variants

The test suite automatically loads your variant configuration:

```bash
# Run tests with your variant
pytest tests/visible/ -v

# Tests use fixtures from conftest.py that load .variant_config.json
```

### Manual Variant Generation

For instructors or testing purposes:

```bash
# Generate a variant for a specific student
python scripts/variant_generator.py <student_id>

# Generate the personalized assignment document
python scripts/generate_assignment.py
```

### Files Overview

| File | Purpose |
|------|---------|
| `scripts/variant_generator.py` | Generates unique variant configuration |
| `scripts/generate_assignment.py` | Creates personalized ASSIGNMENT.md |
| `tests/visible/conftest.py` | Pytest fixtures for variant loading |
| `.variant_config.json` | Generated variant configuration |
| `ASSIGNMENT_TEMPLATE.md` | Template with placeholders |
| `ASSIGNMENT.md` | Your personalized assignment |

### Academic Integrity

Each student's variant is deterministically generated from their student ID. Sharing solutions between students will be detected as the examples and expressions differ between variants.

---

## Getting Help

- Review lecture slides on type systems
- Check the type rules documentation in `src/task2_type_checker.py`
- Use `mypy` error messages to guide your type annotations
- Office hours: [See course schedule]
