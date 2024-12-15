# tests/test_operations.py
import pytest
from app.operations.addition import Add
from app.operations.subtraction import Subtract
from app.operations.multiplication import Multiply
from app.operations.division import Divide

# Test Add operation
def test_add():
    assert Add.calculate(2, 3) == 5
    assert Add.calculate(-1, 1) == 0
    assert Add.calculate(-2, -3) == -5

# Test Subtract operation
def test_subtract():
    assert Subtract.calculate(5, 3) == 2
    assert Subtract.calculate(3, 5) == -2
    assert Subtract.calculate(-3, -5) == 2

# Test Multiply operation
def test_multiply():
    assert Multiply.calculate(2, 3) == 6
    assert Multiply.calculate(-2, 3) == -6
    assert Multiply.calculate(0, 3) == 0
    assert Multiply.calculate(0, 0) == 0

# Test Divide operation
def test_divide():
    assert Divide.calculate(6, 3) == 2
    assert Divide.calculate(-6, 3) == -2
    assert Divide.calculate(5, 2) == 2.5

    # Test division by zero
    with pytest.raises(ValueError):
        Divide.calculate(5, 0)
