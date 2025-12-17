import pytest
from math import factorial as f
from algorythms.factorial import factorial, factorial_recursive

def test_correct_number_factorial():
    for i in range(0, 15):
        assert factorial(i) == f(i)
        assert factorial_recursive(i) == f(i)

def test_negative_number_factorial():
    with pytest.raises(ValueError):
        factorial(-10)
        factorial_recursive(-10)

def test_float_with_decimal_factorial():
    with pytest.raises(TypeError):
        factorial(3.14)
        factorial_recursive(3.14)

def test_float_without_decimal_factorial():
    assert factorial(5.0) == 120
    assert factorial_recursive(5.0) == 120

def test_factorial_consistency():
    for n in range(2, 10):
        assert factorial(n) == n * factorial(n - 1)
        assert factorial_recursive(n) == n * factorial_recursive(n - 1)