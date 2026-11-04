import pytest
from calculator import Calculator

calc = Calculator()

# add
def test_add_positive():
    assert calc.add(2, 3) == 5

def test_add_negative():
    assert calc.add(-2, -3) == -5

def test_add_zero():
    assert calc.add(5, 0) == 5

# subtract
def test_subtract_positive():
    assert calc.subtract(5, 3) == 2

def test_subtract_negative_result():
    assert calc.subtract(3, 5) == -2

def test_subtract_zero():
    assert calc.subtract(5, 0) == 5

# multiply
def test_multiply_positive():
    assert calc.multiply(4, 3) == 12

def test_multiply_by_zero():
    assert calc.multiply(4, 0) == 0

def test_multiply_negative():
    assert calc.multiply(-4, 3) == -12

# divide
def test_divide_positive():
    assert calc.divide(10, 2) == 5

def test_divide_negative():
    assert calc.divide(-10, 2) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)