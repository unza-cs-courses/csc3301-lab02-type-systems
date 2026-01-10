#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Lab 2: Type Systems
"""
import json
from pathlib import Path


def format_coercion_example(coercion: dict, index: int) -> str:
    """Format a single coercion example as markdown."""
    safe_str = "Safe" if coercion.get("safe", False) else "Unsafe"
    return f"""**Example {index}:** `{coercion['id']}`
```
{coercion['code']}
```
- **From Type:** `{coercion['from_type']}`
- **To Type:** `{coercion['to_type']}`
- **Result:** `{coercion['result']}`
- **Description:** {coercion['description']}
- **Safety:** {safe_str}
"""


def format_type_check_expression(test: dict, index: int) -> str:
    """Format a single type check expression as markdown."""
    return f"""**Expression {index}:** `{test['id']}`
```python
{test['expression']}
```
- **Expected Type:** `{test['expected_type']}`
- **Description:** {test['description']}
"""


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Format Python coercions
    python_coercions = "\n".join(
        format_coercion_example(c, i + 1)
        for i, c in enumerate(variant["python_coercions"])
    )

    # Format JavaScript coercions
    js_coercions = "\n".join(
        format_coercion_example(c, i + 1)
        for i, c in enumerate(variant["javascript_coercions"])
    )

    # Format C coercions
    c_coercions = "\n".join(
        format_coercion_example(c, i + 1)
        for i, c in enumerate(variant["c_coercions"])
    )

    # Format type check expressions
    type_check_exprs = "\n".join(
        format_type_check_expression(t, i + 1)
        for i, t in enumerate(variant["type_check_tests"])
    )

    # Replace placeholders
    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])
    assignment = assignment.replace("{{PYTHON_COERCIONS}}", python_coercions)
    assignment = assignment.replace("{{JAVASCRIPT_COERCIONS}}", js_coercions)
    assignment = assignment.replace("{{C_COERCIONS}}", c_coercions)
    assignment = assignment.replace("{{TYPE_CHECK_EXPRESSIONS}}", type_check_exprs)

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
