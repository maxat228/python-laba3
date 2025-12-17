import pytest
from sorts.radix_sort import radix_sort

def test_radix_sort_basic():
    assert radix_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_radix_sort_empty():
    assert radix_sort([]) == []

def test_radix_sort_single():
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_radix_sort_reverse():
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_radix_sort_duplicates():
    assert radix_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_radix_sort_negative():
    assert radix_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]

def test_radix_sort_preserves_input():
    original = [3, 2, 1]
    result = radix_sort(original)
    assert original == [3, 2, 1]
    assert result == [1, 2, 3]

def test_radix_sort_random():
    import random
    random.seed(42)
    arr = [random.randint(0, 100) for _ in range(100)]
    result = radix_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]

def test_radix_sort_all_equal():
    assert radix_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]

def test_radix_sort_large_numbers():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_zeros():
    assert radix_sort([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_radix_sort_mixed_negative_positive():
    assert radix_sort([-10, 5, -3, 8, -1, 0]) == [-10, -3, -1, 0, 5, 8]

def test_radix_sort_type_error_float():
    with pytest.raises(TypeError):
        radix_sort([3.14, 2.71, 1.41])

def test_radix_sort_type_error_string():
    with pytest.raises(TypeError):
        radix_sort(["abc", "def", "ghi"])