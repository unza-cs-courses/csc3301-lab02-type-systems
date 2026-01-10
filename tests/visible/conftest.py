"""
Pytest fixtures for Lab 2: Type Systems
Loads variant configuration with sensible defaults for testing.
"""
import json
import pytest
from pathlib import Path
from typing import Any


# Default variant configuration for testing without a generated variant
DEFAULT_VARIANT = {
    "student_id": "default_student",
    "seed": 12345,
    "python_coercions": [
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
        }
    ],
    "javascript_coercions": [
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
        }
    ],
    "c_coercions": [
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
        }
    ],
    "type_check_tests": [
        {
            "id": "tc_int_add",
            "expression": "BinOp('+', IntLit(5), IntLit(10))",
            "expected_type": "IntType",
            "description": "Integer addition",
            "values": {"val1": 5, "val2": 10, "val3": None}
        },
        {
            "id": "tc_mixed_add",
            "expression": "BinOp('+', IntLit(3), FloatLit(2.5))",
            "expected_type": "FloatType",
            "description": "Mixed int/float addition promotes to float",
            "values": {"val1": 3, "val2": 2.5, "val3": None}
        },
        {
            "id": "tc_comparison",
            "expression": "BinOp('==', IntLit(5), IntLit(5))",
            "expected_type": "BoolType",
            "description": "Equality comparison produces boolean",
            "values": {"val1": 5, "val2": 5, "val3": None}
        },
        {
            "id": "tc_string_concat",
            "expression": "BinOp('++', StringLit('hello'), StringLit('world'))",
            "expected_type": "StringType",
            "description": "String concatenation",
            "values": {"val1": "hello", "val2": "world", "val3": None}
        },
        {
            "id": "tc_division",
            "expression": "BinOp('/', IntLit(10), IntLit(3))",
            "expected_type": "FloatType",
            "description": "Division always produces float",
            "values": {"val1": 10, "val2": 3, "val3": None}
        },
        {
            "id": "tc_type_error_str_int",
            "expression": "BinOp('+', StringLit('test'), IntLit(42))",
            "expected_type": "TypeError_",
            "description": "Type error: cannot add string and int",
            "values": {"val1": "test", "val2": 42, "val3": None}
        }
    ],
    "metadata": {
        "lab": "Lab 2: Type Systems",
        "course": "CSC3301",
        "version": "1.0"
    }
}


def load_variant_config() -> dict[str, Any]:
    """Load variant configuration from file or return defaults."""
    repo_root = Path(__file__).parent.parent.parent
    config_path = repo_root / ".variant_config.json"

    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return DEFAULT_VARIANT


@pytest.fixture(scope="session")
def variant_config() -> dict[str, Any]:
    """Fixture providing the variant configuration."""
    return load_variant_config()


@pytest.fixture(scope="session")
def student_id(variant_config: dict[str, Any]) -> str:
    """Fixture providing the student ID."""
    return variant_config["student_id"]


@pytest.fixture(scope="session")
def python_coercions(variant_config: dict[str, Any]) -> list[dict]:
    """Fixture providing Python type coercion examples."""
    return variant_config["python_coercions"]


@pytest.fixture(scope="session")
def javascript_coercions(variant_config: dict[str, Any]) -> list[dict]:
    """Fixture providing JavaScript type coercion examples."""
    return variant_config["javascript_coercions"]


@pytest.fixture(scope="session")
def c_coercions(variant_config: dict[str, Any]) -> list[dict]:
    """Fixture providing C type coercion examples."""
    return variant_config["c_coercions"]


@pytest.fixture(scope="session")
def type_check_tests(variant_config: dict[str, Any]) -> list[dict]:
    """Fixture providing type checking test expressions."""
    return variant_config["type_check_tests"]


@pytest.fixture(scope="session")
def all_coercions(python_coercions, javascript_coercions, c_coercions) -> dict[str, list[dict]]:
    """Fixture providing all coercion examples grouped by language."""
    return {
        "python": python_coercions,
        "javascript": javascript_coercions,
        "c": c_coercions
    }


@pytest.fixture
def safe_coercions(all_coercions) -> list[dict]:
    """Fixture providing only safe coercion examples."""
    safe = []
    for lang_coercions in all_coercions.values():
        safe.extend([c for c in lang_coercions if c.get("safe", False)])
    return safe


@pytest.fixture
def unsafe_coercions(all_coercions) -> list[dict]:
    """Fixture providing only unsafe coercion examples."""
    unsafe = []
    for lang_coercions in all_coercions.values():
        unsafe.extend([c for c in lang_coercions if not c.get("safe", True)])
    return unsafe
