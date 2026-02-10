"""
Task 4: Static vs Dynamic Type Systems - Trade-offs

This module explores the trade-offs between dynamic typing (duck typing) and
static typing (generics) by implementing a PriorityQueue twice.

The fundamental question:
When should you use duck typing vs static generics?

Duck Typing (Dynamic):
- "If it walks like a duck and quacks like a duck, it's a duck"
- No explicit interface requirements
- Maximum flexibility, but less compiler support
- Runtime errors only

Static Generics (Static):
- Explicit type bounds and constraints
- Compile-time checking (via mypy)
- Better IDE support and documentation
- Safer but less flexible

Your Assignment:
1. Implement DuckTypedPriorityQueue using dynamic typing
2. Implement GenericPriorityQueue using TypeVar and Generic
3. Analyze the trade-offs in the module docstring (200+ words)
"""

from typing import Any, Generic, TypeVar, List, Optional, Protocol
from abc import ABC, abstractmethod
import heapq


class Comparable(Protocol):
    """
    Protocol defining what makes something 'comparable'.

    This is structural typing: any object with __lt__ is Comparable.
    """

    def __lt__(self, other: Any) -> bool:
        """Less-than comparison."""
        ...


T = TypeVar("T", bound=Comparable)


class DuckTypedPriorityQueue:
    """
    Priority queue using duck typing (no type restrictions).

    This queue accepts any items that support comparison operations.
    No explicit type checking - if it can be compared, it works.

    Advantages:
    - Maximum flexibility
    - No type declaration needed
    - Can mix different comparable types

    Disadvantages:
    - Runtime errors if items aren't comparable
    - IDE doesn't know what type to expect
    - Harder to document requirements
    """

    def __init__(self) -> None:
        """Initialize an empty priority queue using a list as a heap."""
        # TODO: Initialize heap storage
        pass

    def push(self, item: Any) -> None:
        """
        Add an item to the priority queue.

        Args:
            item: Any item that supports comparison (has __lt__ method)

        Raises:
            TypeError: At runtime, only if item doesn't support comparison
        """
        # TODO: Add item to heap
        # Hint: Use heapq.heappush()
        pass

    def pop(self) -> Any:
        """
        Remove and return the smallest item.

        Returns:
            The smallest item in the queue

        Raises:
            IndexError: If the queue is empty
        """
        # TODO: Remove and return minimum item
        # Hint: Use heapq.heappop()
        pass

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue has no items, False otherwise
        """
        # TODO: Check if heap is empty
        pass


class GenericPriorityQueue(Generic[T]):
    """
    Priority queue using static generics (type-safe).

    This queue is parameterized by type T, which must be comparable.
    Type checkers like mypy can verify correctness at development time.

    Advantages:
    - Type safety (mypy catches mistakes)
    - Better IDE support and autocomplete
    - Clear documentation of what types work
    - Self-documenting code

    Disadvantages:
    - More verbose declaration
    - Type bounds can be restrictive
    - Requires mypy setup
    """

    def __init__(self) -> None:
        """Initialize an empty generic priority queue."""
        # TODO: Initialize heap storage
        pass

    def push(self, item: T) -> None:
        """
        Add an item to the priority queue.

        Args:
            item: An item of type T (must be comparable)

        Note:
            Type checkers verify that item is of type T at development time.
        """
        # TODO: Add item to heap
        pass

    def pop(self) -> T:
        """
        Remove and return the smallest item.

        Returns:
            The smallest item of type T

        Raises:
            IndexError: If the queue is empty
        """
        # TODO: Remove and return minimum item
        pass

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue has no items, False otherwise
        """
        # TODO: Check if heap is empty
        pass


def compare_approaches() -> str:
    """
    Analyze and document the trade-offs between duck typing and generics.

    This function should return a comprehensive analysis (200+ words) covering:

    1. Type Safety:
       - How do duck typing and generics differ in catching type errors?
       - When are errors detected (compile vs runtime)?

    2. Flexibility:
       - Which approach is more flexible?
       - How do they handle heterogeneous data?

    3. IDE Support:
       - How does each approach affect IDE features?
       - Code completion, jump-to-definition, refactoring?

    4. Runtime Performance:
       - Does static typing have runtime overhead?
       - Any performance differences in execution?

    5. Maintainability:
       - Which is easier to maintain long-term?
       - How do they scale to large codebases?

    Returns:
        A multi-paragraph analysis of the trade-offs
    """
    # TODO: Write a comprehensive analysis
    # This should be 200+ words covering the points above
    # You can use this template as a starting point:

    analysis = """
    # Trade-offs: Duck Typing vs Static Generics

    ## Type Safety
    TODO: Explain differences in type checking...

    ## Flexibility
    TODO: Discuss flexibility trade-offs...

    ## IDE Support
    TODO: Analyze IDE integration...

    ## Runtime Performance
    TODO: Discuss any performance implications...

    ## Maintainability
    TODO: Analyze long-term maintenance...

    ## Conclusion
    TODO: Summarize when to use each approach...
    """

    return analysis


# TODO: Add example usage demonstrating both approaches

# Example for DuckTypedPriorityQueue:
# queue = DuckTypedPriorityQueue()
# queue.push(3)
# queue.push(1)
# queue.push(2)
# print(queue.pop())  # 1
# print(queue.pop())  # 2

# Example for GenericPriorityQueue:
# queue: GenericPriorityQueue[int] = GenericPriorityQueue()
# queue.push(3)      # mypy checks this is int
# queue.push(1)
# queue.push(2)
# val = queue.pop()  # mypy knows val is int
