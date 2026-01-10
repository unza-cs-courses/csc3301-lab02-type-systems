# Lab 2: Type Systems and Type Checking

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Estimated Time:** 2-3 hours
**Points:** 100

---

## Your Personalized Assignment

This assignment has been generated specifically for you based on your student ID. The type coercion examples and type checking expressions below are unique to your variant.

---

## Task 1: Type Annotations (20 points)

Open `src/task1_annotations.py`. Add complete type hints to all functions and the class so that `mypy --strict` passes with zero errors.

```bash
mypy src/task1_annotations.py --strict
```

**Requirements:**
- All function parameters must have type annotations
- All return types must be specified
- Class attributes must be properly typed
- Use appropriate types from the `typing` module where needed

---

## Task 2: Expression Type Checker (40 points)

Open `src/task2_type_checker.py`. Implement the `type_check(expr)` function that determines the type of expressions in a simple language.

### Your Type Checking Expressions

Implement the type checker to correctly handle these expressions from your variant:

{{TYPE_CHECK_EXPRESSIONS}}

### Type Rules Reference

| Expression | Result Type |
|------------|-------------|
| `IntLit` | `IntType` |
| `FloatLit` | `FloatType` |
| `BoolLit` | `BoolType` |
| `StringLit` | `StringType` |
| `Int + Int` | `IntType` |
| `Int + Float` or `Float + Int` | `FloatType` |
| `Float + Float` | `FloatType` |
| `Int / Int` | `FloatType` (division always produces float) |
| `Bool and Bool` | `BoolType` |
| `Bool or Bool` | `BoolType` |
| `String ++ String` | `StringType` |
| `Int == Int` | `BoolType` |
| `Int < Int` | `BoolType` |
| `IfExpr` | Type of branches (must match) |

---

## Task 3: Type Coercion Analysis (20 points)

Open `src/task3_coercion.py` and analyze the following type coercion examples that have been assigned to you.

### Your Python Coercion Examples

{{PYTHON_COERCIONS}}

### Your JavaScript Coercion Examples

{{JAVASCRIPT_COERCIONS}}

### Your C Coercion Examples

{{C_COERCIONS}}

### Requirements

For each coercion example above:

1. **Document** the coercion in the appropriate section of `src/task3_coercion.py`
2. **Classify** each as safe or unsafe and explain why
3. **Implement** `safe_add(a, b)` function that:
   - Only performs addition if types are compatible
   - Raises `TypeError` for unsafe coercions
   - Returns appropriate result type

---

## Task 4: Static vs Dynamic Trade-offs (20 points)

Open `src/task4_tradeoffs.py`. Implement a `PriorityQueue` twice:

### Part A: Duck-Typed Version (Dynamic)
```python
class DuckTypedPriorityQueue:
    """Priority queue that accepts any comparable items."""
    pass
```

### Part B: Generic Typed Version (Static)
```python
from typing import Generic, TypeVar
T = TypeVar('T', bound='Comparable')

class TypedPriorityQueue(Generic[T]):
    """Priority queue with type bounds."""
    pass
```

### Analysis Required

Include a 200-word analysis in the module docstring addressing:
- When would you choose duck typing?
- When would you choose static generics?
- What are the trade-offs in terms of:
  - Type safety
  - Code flexibility
  - IDE support
  - Runtime performance

---

## Submission Checklist

- [ ] Task 1: `mypy --strict` passes on `src/task1_annotations.py`
- [ ] Task 2: Type checker handles all your variant expressions correctly
- [ ] Task 3: All 9 coercion examples documented with safe/unsafe classification
- [ ] Task 4: Both PriorityQueue implementations complete with analysis
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Complete `SUBMISSION.md` with reflection

---

## Running Tests

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run with variant configuration
pytest tests/visible/ -v --tb=short

# Check type annotations
mypy src/task1_annotations.py --strict
```

---

## Grading

| Component | Points |
|-----------|--------|
| Task 1: Type Annotations | 20 |
| Task 2: Type Checker | 40 |
| Task 3: Coercion Analysis | 20 |
| Task 4: Static vs Dynamic | 20 |
| **Total** | **100** |

---

*This assignment was generated for student {{STUDENT_ID}}. Do not share your variant with other students.*
