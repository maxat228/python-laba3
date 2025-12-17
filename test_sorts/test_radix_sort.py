import pytest
from sorts.radix_sort import radix_sort

def test_radix_sort_empty():
    assert radix_sort([]) == []
    assert radix_sort([]) == sorted([])


def test_radix_sort_single():
    assert radix_sort([5]) == [5]
    assert radix_sort([-5]) == [-5]
    assert radix_sort([0]) == [0]


def test_radix_sort_positive_only():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_radix_sort_negative_only():
    assert radix_sort([-5, -1, -3, -2]) == [-5, -3, -2, -1]
    assert radix_sort([-10, -5, -20]) == [-20, -10, -5]
    assert radix_sort([-1]) == [-1]


def test_radix_sort_mixed():
    assert radix_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]
    assert radix_sort([-10, 5, -3, 7, 0]) == [-10, -3, 0, 5, 7]
    assert radix_sort([0, -1, 1]) == [-1, 0, 1]


def test_radix_sort_duplicates():
    assert radix_sort([5, -2, 0, 5, -2, 10, 0, -2, 5]) == [-2, -2, -2, 0, 0, 5, 5, 5, 10]
    assert radix_sort([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert radix_sort([-1, -1, -1]) == [-1, -1, -1]


def test_radix_sort_large_numbers():
    assert radix_sort([10000, -5000, 2500, -7500, 0]) == [-7500, -5000, 0, 2500, 10000]
    assert radix_sort([999, -999, 0]) == [-999, 0, 999]


def test_radix_sort_already_sorted():
    assert radix_sort([-10, -5, 0, 3, 7, 12]) == [-10, -5, 0, 3, 7, 12]
    assert radix_sort([-3, -2, -1]) == [-3, -2, -1]


def test_radix_sort_reverse_sorted():
    assert radix_sort([100, 50, 10, 0, -10, -50]) == [-50, -10, 0, 10, 50, 100]
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_radix_sort_zeros():
    assert radix_sort([0, 0, 0]) == [0, 0, 0]
    assert radix_sort([-1, 0, 1, 0]) == [-1, 0, 0, 1]


def test_radix_sort_preserves_input():
    original = [-5, 3, -1, 0, 2]
    result = radix_sort(original)
    assert original == [-5, 3, -1, 0, 2]
    assert result == [-5, -1, 0, 2, 3]


def test_radix_sort_complex():
    arr = [999, -999, 0, 123, -456, 789, -123, 456, -789, 5, 5, 5, -3, -3]
    expected = sorted(arr)
    result = radix_sort(arr)
    assert result == expected


def test_radix_sort_edge_cases():
    assert radix_sort([7, 7, 7]) == [7, 7, 7]
    assert radix_sort([-4, -4, -4]) == [-4, -4, -4]
    assert radix_sort([1, -1, 1, -1]) == [-1, -1, 1, 1]
    assert radix_sort([1000, -1000, 0]) == [-1000, 0, 1000]


def test_radix_sort_random():
    import random

    random.seed(42)
    for _ in range(10):
        n = random.randint(0, 20)
        arr = [random.randint(-1000, 1000) for _ in range(n)]

        expected = sorted(arr)
        result = radix_sort(arr)

        assert result == expected


def test_radix_sort_type_error_float():
    with pytest.raises(TypeError):
        radix_sort([1.5, 2.3, 0.7])

    with pytest.raises(TypeError):
        radix_sort([1, 2.5, 3])

    with pytest.raises(TypeError):
        radix_sort([0.0])


def test_radix_sort_type_error_string():
    with pytest.raises(TypeError):
        radix_sort(["a", "b", "c"])

    with pytest.raises(TypeError):
        radix_sort([1, "two", 3])


def test_radix_sort_type_error_mixed():
    with pytest.raises(TypeError):
        radix_sort([1, 2, [3, 4]])

    with pytest.raises(TypeError):
        radix_sort([1, {"a": 1}, 3])

    with pytest.raises(TypeError):
        radix_sort([None, 1, 2])