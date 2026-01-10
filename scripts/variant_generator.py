#!/usr/bin/env python3
"""
Variant Generator for Lab 2: Type Systems
CSC3301 Programming Language Paradigms

Generates unique type coercion examples and type checking expressions
based on student ID hash for deterministic, personalized assignments.
"""
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


# =============================================================================
# TYPE COERCION EXAMPLES DATABASE
# =============================================================================

# Python type coercion examples (implicit and explicit)
PYTHON_COERCIONS = [
    {
        "id": "py_int_float_add",
        "code": "result = 5 + 3.14",
        "from_type": "int",
        "to_type": "float",
        "result": "8.14",
        "description": "Integer implicitly promoted to float in arithmetic",
        "safe": True
    },
    {
        "id": "py_bool_int_add",
        "code": "result = True + 10",
        "from_type": "bool",
        "to_type": "int",
        "result": "11",
        "description": "Boolean treated as integer (True=1, False=0)",
        "safe": True
    },
    {
        "id": "py_str_int_mult",
        "code": "result = 'ab' * 3",
        "from_type": "str * int",
        "to_type": "str",
        "result": "'ababab'",
        "description": "String repetition using integer multiplication",
        "safe": True
    },
    {
        "id": "py_float_int_div",
        "code": "result = 10 / 4",
        "from_type": "int / int",
        "to_type": "float",
        "result": "2.5",
        "description": "Division always produces float in Python 3",
        "safe": True
    },
    {
        "id": "py_list_bool",
        "code": "result = bool([1, 2, 3])",
        "from_type": "list",
        "to_type": "bool",
        "result": "True",
        "description": "Non-empty container evaluates to True",
        "safe": True
    },
    {
        "id": "py_none_bool",
        "code": "result = bool(None)",
        "from_type": "NoneType",
        "to_type": "bool",
        "result": "False",
        "description": "None evaluates to False in boolean context",
        "safe": True
    },
    {
        "id": "py_int_complex",
        "code": "result = 5 + 2j",
        "from_type": "int",
        "to_type": "complex",
        "result": "(5+2j)",
        "description": "Integer promoted to complex in arithmetic",
        "safe": True
    },
    {
        "id": "py_str_format",
        "code": "result = f'{42}'",
        "from_type": "int",
        "to_type": "str",
        "result": "'42'",
        "description": "Integer converted to string in f-string",
        "safe": True
    },
    {
        "id": "py_float_floor",
        "code": "result = 7.9 // 2",
        "from_type": "float // int",
        "to_type": "float",
        "result": "3.0",
        "description": "Floor division with float operand returns float",
        "safe": True
    },
]

# JavaScript type coercion examples
JAVASCRIPT_COERCIONS = [
    {
        "id": "js_str_num_add",
        "code": "let result = '5' + 3;",
        "from_type": "number",
        "to_type": "string",
        "result": "'53'",
        "description": "Number coerced to string in concatenation",
        "safe": False
    },
    {
        "id": "js_str_num_sub",
        "code": "let result = '10' - 5;",
        "from_type": "string",
        "to_type": "number",
        "result": "5",
        "description": "String coerced to number in subtraction",
        "safe": False
    },
    {
        "id": "js_bool_num",
        "code": "let result = true + true;",
        "from_type": "boolean",
        "to_type": "number",
        "result": "2",
        "description": "Booleans coerced to numbers in arithmetic",
        "safe": False
    },
    {
        "id": "js_null_num",
        "code": "let result = null + 5;",
        "from_type": "null",
        "to_type": "number",
        "result": "5",
        "description": "null coerced to 0 in numeric context",
        "safe": False
    },
    {
        "id": "js_undefined_str",
        "code": "let result = 'val: ' + undefined;",
        "from_type": "undefined",
        "to_type": "string",
        "result": "'val: undefined'",
        "description": "undefined converted to string 'undefined'",
        "safe": False
    },
    {
        "id": "js_array_num",
        "code": "let result = [1] + [2];",
        "from_type": "array",
        "to_type": "string",
        "result": "'12'",
        "description": "Arrays converted to strings then concatenated",
        "safe": False
    },
    {
        "id": "js_obj_num",
        "code": "let result = {} + [];",
        "from_type": "object/array",
        "to_type": "string/number",
        "result": "'[object Object]' or 0",
        "description": "Object/array coercion in addition (context-dependent)",
        "safe": False
    },
    {
        "id": "js_double_neg",
        "code": "let result = ~~'42.9';",
        "from_type": "string",
        "to_type": "number (int)",
        "result": "42",
        "description": "Double NOT truncates string to integer",
        "safe": False
    },
    {
        "id": "js_equality",
        "code": "let result = '0' == false;",
        "from_type": "string/boolean",
        "to_type": "number",
        "result": "true",
        "description": "Loose equality with type coercion",
        "safe": False
    },
]

# C type coercion examples
C_COERCIONS = [
    {
        "id": "c_int_float_assign",
        "code": "float f = 5;",
        "from_type": "int",
        "to_type": "float",
        "result": "5.0f",
        "description": "Integer implicitly promoted to float",
        "safe": True
    },
    {
        "id": "c_float_int_assign",
        "code": "int i = 3.7;",
        "from_type": "float",
        "to_type": "int",
        "result": "3",
        "description": "Float truncated to integer (data loss)",
        "safe": False
    },
    {
        "id": "c_char_int",
        "code": "int i = 'A';",
        "from_type": "char",
        "to_type": "int",
        "result": "65",
        "description": "Character promoted to ASCII integer value",
        "safe": True
    },
    {
        "id": "c_int_char",
        "code": "char c = 300;",
        "from_type": "int",
        "to_type": "char",
        "result": "44 (or platform-dependent)",
        "description": "Integer overflow when narrowing to char",
        "safe": False
    },
    {
        "id": "c_signed_unsigned",
        "code": "unsigned int u = -1;",
        "from_type": "signed int",
        "to_type": "unsigned int",
        "result": "4294967295 (UINT_MAX)",
        "description": "Signed to unsigned conversion wraps around",
        "safe": False
    },
    {
        "id": "c_ptr_int",
        "code": "int* p = (int*)0x1000;",
        "from_type": "integer literal",
        "to_type": "pointer",
        "result": "pointer to address 0x1000",
        "description": "Integer cast to pointer (explicit)",
        "safe": False
    },
    {
        "id": "c_double_float",
        "code": "float f = 3.14159265358979;",
        "from_type": "double",
        "to_type": "float",
        "result": "3.14159f (precision loss)",
        "description": "Double literal narrowed to float",
        "safe": False
    },
    {
        "id": "c_int_promotion",
        "code": "short a = 1, b = 2; int c = a + b;",
        "from_type": "short",
        "to_type": "int",
        "result": "3",
        "description": "Integer promotion in arithmetic",
        "safe": True
    },
    {
        "id": "c_void_ptr",
        "code": "void* v = malloc(10); int* p = v;",
        "from_type": "void*",
        "to_type": "int*",
        "result": "pointer to allocated memory",
        "description": "Void pointer implicitly converts (C only)",
        "safe": True
    },
]

# =============================================================================
# TYPE CHECKING EXPRESSIONS DATABASE
# =============================================================================

TYPE_CHECK_EXPRESSIONS = [
    {
        "id": "tc_int_add",
        "expression": "BinOp('+', IntLit(VAL1), IntLit(VAL2))",
        "expected_type": "IntType",
        "description": "Integer addition",
        "val_range": (1, 100)
    },
    {
        "id": "tc_float_add",
        "expression": "BinOp('+', FloatLit(VAL1), FloatLit(VAL2))",
        "expected_type": "FloatType",
        "description": "Float addition",
        "val_range": (1.0, 50.0)
    },
    {
        "id": "tc_mixed_add",
        "expression": "BinOp('+', IntLit(VAL1), FloatLit(VAL2))",
        "expected_type": "FloatType",
        "description": "Mixed int/float addition promotes to float",
        "val_range": (1, 100)
    },
    {
        "id": "tc_division",
        "expression": "BinOp('/', IntLit(VAL1), IntLit(VAL2))",
        "expected_type": "FloatType",
        "description": "Division always produces float",
        "val_range": (2, 50)
    },
    {
        "id": "tc_comparison",
        "expression": "BinOp('==', IntLit(VAL1), IntLit(VAL2))",
        "expected_type": "BoolType",
        "description": "Equality comparison produces boolean",
        "val_range": (1, 100)
    },
    {
        "id": "tc_less_than",
        "expression": "BinOp('<', IntLit(VAL1), IntLit(VAL2))",
        "expected_type": "BoolType",
        "description": "Less-than comparison produces boolean",
        "val_range": (1, 100)
    },
    {
        "id": "tc_bool_and",
        "expression": "BinOp('and', BoolLit(VAL1), BoolLit(VAL2))",
        "expected_type": "BoolType",
        "description": "Boolean AND operation",
        "val_range": (True, False)
    },
    {
        "id": "tc_bool_or",
        "expression": "BinOp('or', BoolLit(VAL1), BoolLit(VAL2))",
        "expected_type": "BoolType",
        "description": "Boolean OR operation",
        "val_range": (True, False)
    },
    {
        "id": "tc_string_concat",
        "expression": "BinOp('++', StringLit('VAL1'), StringLit('VAL2'))",
        "expected_type": "StringType",
        "description": "String concatenation",
        "val_range": ("hello", "world")
    },
    {
        "id": "tc_if_expr_int",
        "expression": "IfExpr(BoolLit(True), IntLit(VAL1), IntLit(VAL2))",
        "expected_type": "IntType",
        "description": "If expression with integer branches",
        "val_range": (1, 100)
    },
    {
        "id": "tc_nested_arith",
        "expression": "BinOp('+', BinOp('*', IntLit(VAL1), IntLit(VAL2)), IntLit(VAL3))",
        "expected_type": "IntType",
        "description": "Nested arithmetic expression",
        "val_range": (1, 20)
    },
    {
        "id": "tc_type_error_str_int",
        "expression": "BinOp('+', StringLit('VAL1'), IntLit(VAL2))",
        "expected_type": "TypeError_",
        "description": "Type error: cannot add string and int",
        "val_range": ("test", 42)
    },
    {
        "id": "tc_type_error_bool_arith",
        "expression": "BinOp('+', BoolLit(True), IntLit(VAL1))",
        "expected_type": "TypeError_",
        "description": "Type error: cannot add bool and int",
        "val_range": (1, 100)
    },
]

# String values for type check expressions
STRING_VALUES = [
    "hello", "world", "test", "foo", "bar", "alpha", "beta", "gamma",
    "type", "check", "expr", "value", "data", "code", "func"
]


def hash_student_id(student_id: str) -> int:
    """Create deterministic hash from student ID."""
    h = hashlib.sha256(student_id.encode()).hexdigest()
    return int(h, 16)


def select_items(items: list, seed: int, count: int) -> list:
    """Deterministically select items from a list."""
    n = len(items)
    selected = []
    for i in range(count):
        idx = (seed + i * 17) % n
        # Avoid duplicates
        while items[idx] in selected and len(selected) < n:
            idx = (idx + 1) % n
        selected.append(items[idx])
    return selected


def generate_value(seed: int, val_range: tuple, index: int) -> Any:
    """Generate a deterministic value within the given range."""
    if isinstance(val_range[0], bool):
        return bool((seed + index) % 2)
    elif isinstance(val_range[0], int):
        low, high = val_range
        return low + ((seed + index * 31) % (high - low + 1))
    elif isinstance(val_range[0], float):
        low, high = val_range
        return round(low + ((seed + index * 31) % int(high - low + 1)) + 0.5, 1)
    elif isinstance(val_range[0], str):
        # Return from string values list
        return STRING_VALUES[(seed + index) % len(STRING_VALUES)]
    return val_range[0]


def generate_variant(student_id: str) -> dict:
    """Generate a complete variant configuration for a student."""
    seed = hash_student_id(student_id)

    # Select 3 Python coercion examples
    python_examples = select_items(PYTHON_COERCIONS, seed, 3)

    # Select 3 JavaScript coercion examples
    js_examples = select_items(JAVASCRIPT_COERCIONS, seed + 1000, 3)

    # Select 3 C coercion examples
    c_examples = select_items(C_COERCIONS, seed + 2000, 3)

    # Select type checking expressions (5 regular + 1 error case)
    regular_exprs = [e for e in TYPE_CHECK_EXPRESSIONS if e["expected_type"] != "TypeError_"]
    error_exprs = [e for e in TYPE_CHECK_EXPRESSIONS if e["expected_type"] == "TypeError_"]

    selected_regular = select_items(regular_exprs, seed + 3000, 5)
    selected_error = select_items(error_exprs, seed + 4000, 1)

    # Generate concrete values for type check expressions
    type_check_tests = []
    for i, expr_template in enumerate(selected_regular + selected_error):
        expr = expr_template.copy()
        val1 = generate_value(seed + i * 100, expr["val_range"], 0)
        val2 = generate_value(seed + i * 100 + 1, expr["val_range"], 1)
        val3 = generate_value(seed + i * 100 + 2, expr["val_range"], 2) if "VAL3" in expr["expression"] else None

        # Substitute values in expression
        concrete_expr = expr["expression"]
        if isinstance(val1, str) and not isinstance(expr["val_range"][0], bool):
            concrete_expr = concrete_expr.replace("VAL1", val1)
        else:
            concrete_expr = concrete_expr.replace("VAL1", str(val1))

        if isinstance(val2, str) and not isinstance(expr["val_range"][0], bool):
            concrete_expr = concrete_expr.replace("VAL2", val2)
        else:
            concrete_expr = concrete_expr.replace("VAL2", str(val2))

        if val3 is not None:
            concrete_expr = concrete_expr.replace("VAL3", str(val3))

        type_check_tests.append({
            "id": expr["id"],
            "expression": concrete_expr,
            "expected_type": expr["expected_type"],
            "description": expr["description"],
            "values": {"val1": val1, "val2": val2, "val3": val3}
        })

    return {
        "student_id": student_id,
        "seed": seed % (2**32),  # Keep seed manageable
        "python_coercions": python_examples,
        "javascript_coercions": js_examples,
        "c_coercions": c_examples,
        "type_check_tests": type_check_tests,
        "metadata": {
            "lab": "Lab 2: Type Systems",
            "course": "CSC3301",
            "version": "1.0"
        }
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        sys.exit(1)

    student_id = sys.argv[1]

    # Generate variant
    variant = generate_variant(student_id)

    # Write to config file
    repo_root = Path(__file__).parent.parent
    config_path = repo_root / ".variant_config.json"

    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)

    print(f"Generated variant for student: {student_id}")
    print(f"Config saved to: {config_path}")
    print(f"\nVariant summary:")
    print(f"  - Python coercion examples: {len(variant['python_coercions'])}")
    print(f"  - JavaScript coercion examples: {len(variant['javascript_coercions'])}")
    print(f"  - C coercion examples: {len(variant['c_coercions'])}")
    print(f"  - Type check expressions: {len(variant['type_check_tests'])}")


if __name__ == "__main__":
    main()
