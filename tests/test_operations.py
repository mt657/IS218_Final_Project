# tests/test_operations.py
import pytest
from app.operations.addition import Add
from app.operations.subtraction import Subtract
from app.operations.multiplication import Multiply
from app.operations.division import Divide

# Test Add operation
def test_add():
    add = Add()
    assert add.calculate(2, 3) == 5
    assert add.calculate(-1, 1) == 0
    assert add.calculate(-2, -3) == -5

# Test Subtract operation
def test_subtract():
    subtract = Subtract()
    assert subtract.calculate(5, 3) == 2
    assert subtract.calculate(3, 5) == -2
    assert subtract.calculate(-3, -5) == 2

# Test Multiply operation
def test_multiply():
    multiply = Multiply()
    assert multiply.calculate(2, 3) == 6
    assert multiply.calculate(-2, 3) == -6
    assert multiply.calculate(0, 3) == 0
    assert multiply.calculate(0, 0) == 0

# Test Divide operation
def test_divide():
    divide = Divide()
    assert divide.calculate(6, 3) == 2
    assert divide.calculate(-6, 3) == -2
    assert divide.calculate(5, 2) == 2.5

    # Test division by zero
    with pytest.raises(ValueError):
        divide.calculate(5, 0)
