"""
Lab 2 Task 2: Expression Type Checker
Implement type_check() for a simple expression language.
"""
from dataclasses import dataclass
from typing import Union, Any

# AST Node definitions
@dataclass
class IntLit:
    value: int

@dataclass
class FloatLit:
    value: float

@dataclass
class BoolLit:
    value: bool

@dataclass
class StringLit:
    value: str

@dataclass
class BinOp:
    op: str  # '+', '-', '*', '/', '==', '<', '>', 'and', 'or', '++'
    left: 'Expr'
    right: 'Expr'

@dataclass
class IfExpr:
    condition: 'Expr'
    then_branch: 'Expr'
    else_branch: 'Expr'

Expr = Union[IntLit, FloatLit, BoolLit, StringLit, BinOp, IfExpr]

# Type representations
class Type:
    pass

@dataclass
class IntType(Type):
    pass

@dataclass
class FloatType(Type):
    pass

@dataclass
class BoolType(Type):
    pass

@dataclass
class StringType(Type):
    pass

@dataclass
class TypeError_(Type):
    message: str


def type_check(expr: Expr) -> Type:
    """
    Determine the type of an expression.

    Type Rules:
    - IntLit -> IntType
    - FloatLit -> FloatType
    - BoolLit -> BoolType
    - StringLit -> StringType
    - Int + Int -> Int
    - Int + Float or Float + Int -> Float
    - Float + Float -> Float
    - Int / Int -> Float (division always produces float)
    - Bool and Bool -> Bool
    - Bool or Bool -> Bool
    - String ++ String -> String
    - Int == Int -> Bool (comparison produces bool)
    - IfExpr: condition must be Bool, branches must have same type

    Returns TypeError_ with message for invalid operations.
    """
    # YOUR CODE HERE
    pass


def check_type_compatibility(expected_type: type, value: Any) -> bool:
    """
    Check if a runtime value is compatible with an expected Python type.

    This function performs runtime type compatibility checking, supporting:
    - Built-in types: int, float, str, bool, list, dict, set, tuple
    - NoneType and None values
    - Subtype relationships (e.g., bool is a subtype of int in Python)
    - Custom type hierarchies

    Args:
        expected_type: A Python type object (e.g., int, str, list, etc.)
        value: The runtime value to check for compatibility

    Returns:
        True if value is compatible with expected_type, False otherwise

    Examples:
        check_type_compatibility(int, 42) -> True
        check_type_compatibility(int, 42.5) -> False
        check_type_compatibility(list, [1, 2, 3]) -> True
        check_type_compatibility(str, "hello") -> True
        check_type_compatibility(type(None), None) -> True
        check_type_compatibility(int, True) -> True  # bool is subtype of int

    Notes:
        - Handle NoneType by checking against type(None)
        - Consider isinstance() for subtype checking
        - Handle special cases like bool being a subtype of int
    """
    # TODO: Implement type compatibility checking
    raise NotImplementedError("check_type_compatibility not yet implemented")


def infer_type(value: Any) -> type:
    """
    Infer the Python type of a runtime value.

    This function analyzes a given value and returns its corresponding Python type.
    It should handle all basic Python types and support type inference for:
    - Numeric types: int, float, bool
    - String type: str
    - Collection types: list, dict, set, tuple
    - None type: NoneType

    Args:
        value: Any Python value

    Returns:
        The inferred type of the value as a Python type object

    Examples:
        infer_type(42) -> int
        infer_type(3.14) -> float
        infer_type("hello") -> str
        infer_type([1, 2, 3]) -> list
        infer_type({'a': 1}) -> dict
        infer_type(None) -> type(None)
        infer_type(True) -> bool

    Notes:
        - Use type() or isinstance() to determine the value's type
        - Consider the distinction between bool and int (even though bool is a subclass of int)
        - Preserve the exact type, not parent types
    """
    # TODO: Implement type inference
    raise NotImplementedError("infer_type not yet implemented")


# Test expressions
if __name__ == "__main__":
    # Test: 1 + 2 -> Int
    e1 = BinOp('+', IntLit(1), IntLit(2))
    print(f"1 + 2: {type_check(e1)}")
    
    # Test: 1 + 2.0 -> Float
    e2 = BinOp('+', IntLit(1), FloatLit(2.0))
    print(f"1 + 2.0: {type_check(e2)}")
    
    # Test: "hello" ++ "world" -> String
    e3 = BinOp('++', StringLit("hello"), StringLit("world"))
    print(f'"hello" ++ "world": {type_check(e3)}')
    
    # Test: 1 + "hello" -> TypeError
    e4 = BinOp('+', IntLit(1), StringLit("hello"))
    print(f'1 + "hello": {type_check(e4)}')
