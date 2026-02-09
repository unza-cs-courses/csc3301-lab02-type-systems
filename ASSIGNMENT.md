# Lab 2: Type Systems and Type Checking

**CSC3301 Programming Language Paradigms**
**Student ID:** systems
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

**Expression 1:** `tc_if_expr_int`
```python
IfExpr(BoolLit(True), IntLit(65), IntLit(97))
```
- **Expected Type:** `IntType`
- **Description:** If expression with integer branches

**Expression 2:** `tc_comparison`
```python
BinOp('==', IntLit(65), IntLit(97))
```
- **Expected Type:** `BoolType`
- **Description:** Equality comparison produces boolean

**Expression 3:** `tc_nested_arith`
```python
BinOp('+', BinOp('*', IntLit(5), IntLit(17)), IntLit(9))
```
- **Expected Type:** `IntType`
- **Description:** Nested arithmetic expression

**Expression 4:** `tc_less_than`
```python
BinOp('<', IntLit(65), IntLit(97))
```
- **Expected Type:** `BoolType`
- **Description:** Less-than comparison produces boolean

**Expression 5:** `tc_int_add`
```python
BinOp('+', IntLit(65), IntLit(97))
```
- **Expected Type:** `IntType`
- **Description:** Integer addition

**Expression 6:** `tc_type_error_str_int`
```python
BinOp('+', StringLit('check'), IntLit(value))
```
- **Expected Type:** `TypeError_`
- **Description:** Type error: cannot add string and int


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

**Example 1:** `py_bool_int_add`
```
result = True + 10
```
- **From Type:** `bool`
- **To Type:** `int`
- **Result:** `11`
- **Description:** Boolean treated as integer (True=1, False=0)
- **Safety:** Safe

**Example 2:** `py_int_float_add`
```
result = 5 + 3.14
```
- **From Type:** `int`
- **To Type:** `float`
- **Result:** `8.14`
- **Description:** Integer implicitly promoted to float in arithmetic
- **Safety:** Safe

**Example 3:** `py_float_floor`
```
result = 7.9 // 2
```
- **From Type:** `float // int`
- **To Type:** `float`
- **Result:** `3.0`
- **Description:** Floor division with float operand returns float
- **Safety:** Safe


### Your JavaScript Coercion Examples

**Example 1:** `js_bool_num`
```
let result = true + true;
```
- **From Type:** `boolean`
- **To Type:** `number`
- **Result:** `2`
- **Description:** Booleans coerced to numbers in arithmetic
- **Safety:** Unsafe

**Example 2:** `js_str_num_sub`
```
let result = '10' - 5;
```
- **From Type:** `string`
- **To Type:** `number`
- **Result:** `5`
- **Description:** String coerced to number in subtraction
- **Safety:** Unsafe

**Example 3:** `js_str_num_add`
```
let result = '5' + 3;
```
- **From Type:** `number`
- **To Type:** `string`
- **Result:** `'53'`
- **Description:** Number coerced to string in concatenation
- **Safety:** Unsafe


### Your C Coercion Examples

**Example 1:** `c_int_char`
```
char c = 300;
```
- **From Type:** `int`
- **To Type:** `char`
- **Result:** `44 (or platform-dependent)`
- **Description:** Integer overflow when narrowing to char
- **Safety:** Unsafe

**Example 2:** `c_char_int`
```
int i = 'A';
```
- **From Type:** `char`
- **To Type:** `int`
- **Result:** `65`
- **Description:** Character promoted to ASCII integer value
- **Safety:** Safe

**Example 3:** `c_float_int_assign`
```
int i = 3.7;
```
- **From Type:** `float`
- **To Type:** `int`
- **Result:** `3`
- **Description:** Float truncated to integer (data loss)
- **Safety:** Unsafe


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

*This assignment was generated for student systems. Do not share your variant with other students.*
