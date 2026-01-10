"""Lab 2 Test Suite"""
import pytest
import subprocess

class TestTask1Annotations:
    def test_mypy_passes(self):
        """mypy --strict should pass."""
        result = subprocess.run(
            ["mypy", "src/task1_annotations.py", "--strict"],
            capture_output=True, text=True
        )
        assert result.returncode == 0, f"mypy errors:\n{result.stdout}"

class TestTask2TypeChecker:
    def test_int_literal(self):
        from src.task2_type_checker import type_check, IntLit, IntType
        assert isinstance(type_check(IntLit(42)), IntType)
    
    def test_int_addition(self):
        from src.task2_type_checker import type_check, IntLit, BinOp, IntType
        expr = BinOp('+', IntLit(1), IntLit(2))
        assert isinstance(type_check(expr), IntType)
    
    def test_int_float_addition(self):
        from src.task2_type_checker import type_check, IntLit, FloatLit, BinOp, FloatType
        expr = BinOp('+', IntLit(1), FloatLit(2.0))
        assert isinstance(type_check(expr), FloatType)
    
    def test_type_error(self):
        from src.task2_type_checker import type_check, IntLit, StringLit, BinOp, TypeError_
        expr = BinOp('+', IntLit(1), StringLit("hi"))
        assert isinstance(type_check(expr), TypeError_)
