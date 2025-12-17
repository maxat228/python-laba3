import pytest
from sorts.counting_sort import counting_sort

def test_counting_sort_basic():
    assert counting_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_counting_sort_empty():
    assert counting_sort([]) == []

def test_counting_sort_single():
    assert counting_sort([42]) == [42]

def test_counting_sort_already_sorted():
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_counting_sort_reverse():
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_counting_sort_duplicates():
    assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_counting_sort_negative():
    assert counting_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]

def test_counting_sort_preserves_input():
    original = [3, 2, 1]
    result = counting_sort(original)
    assert original == [3, 2, 1]
    assert result == [1, 2, 3]

def test_counting_sort_random():
    import random
    random.seed(42)
    arr = [random.randint(0, 100) for _ in range(100)]
    result = counting_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]

def test_counting_sort_all_equal():
    assert counting_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]

def test_counting_sort_large_range():
    assert counting_sort([1000, 1, 500, 999]) == [1, 500, 999, 1000]

def test_counting_sort_type_error_float():
    with pytest.raises(TypeError):
        counting_sort([3.14, 2.71, 1.41])