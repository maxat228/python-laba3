import pytest
from algorythms.fibonacci import fibonacci, fibonacci_recursive

def test_correct_number_fibonacci():
    cases = {0: 0, 1: 1, 2: 1, 3: 2, 5: 5, 10: 55, 20: 6765, 30: 832040}
    for key in cases.keys():
        assert cases[key] == fibonacci(key)
        assert cases[key] == fibonacci_recursive(key)

def test_negative_number_fibonacci():
    with pytest.raises(ValueError):
        fibonacci(-1916)
        fibonacci_recursive(-1916)

    with pytest.raises(ValueError):
        fibonacci(-1935)
        fibonacci_recursive(-1935)

def test_float_with_decimal_fibonacci():
    with pytest.raises(TypeError):
        fibonacci(04.05)
        fibonacci_recursive(04.05)

    with pytest.raises(TypeError):
        fibonacci(26.09)
        fibonacci_recursive(26.09)

def test_float_without_decimal_fibonacci():
    assert fibonacci(5.0) == 5
    assert fibonacci_recursive(5.0) == 5
    assert fibonacci(1.0) == 1
    assert fibonacci_recursive(1.0) == 1
    assert fibonacci(32.0) == 2178309
    assert fibonacci_recursive(32.0) == 2178309

def test_fibonacci_consistency():
    for n in range(2, 20):
        assert fibonacci(n + 1) == fibonacci(n) + fibonacci(n - 1)
        assert fibonacci_recursive(n + 1) == fibonacci(n) + fibonacci(n - 1)
