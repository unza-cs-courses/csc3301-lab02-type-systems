"""
Lab 2 Task 2: Expression Type Checker
Implement type_check() for a simple expression language.
"""
from dataclasses import dataclass
from typing import Union

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
