"""
Task 3: Type Coercion Analysis

This module explores how different programming languages handle type coercion
(automatic type conversion) and documents the safety implications.

Type Coercion:
- Implicit conversion of one type to another
- Every language handles this differently
- Some coercions are safe, others are dangerous

This task requires documenting coercion examples and implementing safe handling.

Your Personalized Coercion Examples:
------------------------------------
You have been assigned specific coercion examples in Python, JavaScript, and C.
Document each one and classify it as safe or unsafe.

Example Classification:
- SAFE: No information loss, intuitive behavior
  - int to float: 5 -> 5.0
  - float to int: Explicit cast with understanding of data loss
  - str to int: Explicit conversion of valid numeric string

- UNSAFE: Information loss or unexpected behavior
  - float to int: Loss of decimal part
  - str to int: May fail on invalid input
  - Implicit widening in C: 8-bit to 16-bit (implementation dependent)
"""

from typing import Union, Any, List, Dict


# TODO: Create a data structure to document your coercion examples
# This could be a list of dicts or a custom class
# Each entry should contain:
# - language: str (Python, JavaScript, or C)
# - example: str (e.g., "int(\"123\")")
# - from_type: str (e.g., "str")
# - to_type: str (e.g., "int")
# - safe: bool (True if safe, False if unsafe)
# - explanation: str (why it's safe or unsafe)

COERCION_EXAMPLES: List[Dict[str, Any]] = [
    # TODO: Add your 9 personalized coercion examples here
    # 3 from Python, 3 from JavaScript, 3 from C
    # Example:
    # {
    #     "language": "Python",
    #     "example": "int(5.7)",
    #     "from_type": "float",
    #     "to_type": "int",
    #     "safe": False,
    #     "explanation": "Information loss: decimal part (.7) is truncated"
    # },
]


def safe_add(a: Any, b: Any) -> Union[int, float, str]:
    """
    Safely add two values, handling type coercion carefully.

    This function demonstrates safe type handling by:
    1. Only allowing compatible types
    2. Raising TypeError for unsafe combinations
    3. Returning the appropriate result type

    Type Rules:
    - int + int = int
    - int + float = float (safe upcast)
    - float + float = float
    - str + str = str (concatenation)
    - int + str = TypeError (unsafe)
    - float + str = TypeError (unsafe)

    Args:
        a: First operand
        b: Second operand

    Returns:
        Result of addition with appropriate type

    Raises:
        TypeError: If the combination is unsafe
        TypeError: If types are not int, float, or str

    Example:
        safe_add(5, 3) -> 8
        safe_add(5, 3.5) -> 8.5
        safe_add("hello", " world") -> "hello world"
        safe_add(5, "hello") -> TypeError
    """
    # TODO: Implement safe addition with type checking
    # 1. Check types of a and b
    # 2. If both are int: return int result
    # 3. If one is float: return float result
    # 4. If both are str: return concatenated string
    # 5. Otherwise: raise TypeError with descriptive message
    pass


# TODO: Add any helper functions or additional analysis below
# For example, you might want to create functions to:
# - Check if a coercion is safe
# - Document implicit vs explicit coercions
# - Compare coercion behavior across languages
