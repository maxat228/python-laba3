import pytest
from sorts.quick_sort import quick_sort

def test_quick_sort_basic():
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]
    assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 2, 3, 4]) == [1, 2, 2, 3, 4]


def test_quick_sort_reverse():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([10, 8, 6, 4, 2]) == [2, 4, 6, 8, 10]


def test_quick_sort_negative():
    assert quick_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]
    assert quick_sort([-10, -5, -20]) == [-20, -10, -5]


def test_quick_sort_with_key():
    data = [{"x": 3}, {"x": 1}, {"x": 2}]
    result = quick_sort(data, key=lambda d: d["x"])
    assert result == [{"x": 1}, {"x": 2}, {"x": 3}]

    data = [(3, "c"), (1, "a"), (2, "b")]
    result = quick_sort(data, key=lambda x: x[0])
    assert result == [(1, "a"), (2, "b"), (3, "c")]


def test_quick_sort_with_cmp():
    def reverse_cmp(a, b):
        return 1 if a < b else (-1 if a > b else 0)

    result = quick_sort([3, 1, 4, 2], cmp=reverse_cmp)
    assert result == [4, 3, 2, 1]


def test_quick_sort_type_errors():
    with pytest.raises(TypeError):
        quick_sort([1, 2, 3], key="снова какая-то фигня")

    with pytest.raises(TypeError):
        quick_sort([1, 2, 3], cmp=168)

    with pytest.raises(ValueError):
        quick_sort([1, 2, 3], key=lambda x: x, cmp=lambda a, b: 0)


def test_quick_sort_preserves_input():
    original = [3, 1, 4, 2]
    result = quick_sort(original)
    assert original == [3, 1, 4, 2]
    assert result == [1, 2, 3, 4]


def test_quick_sort_random():
    import random
    random.seed(42)

    for _ in range(10):
        n = random.randint(0, 20)
        arr = [random.randint(-100, 100) for _ in range(n)]
        expected = sorted(arr)
        result = quick_sort(arr)
        assert result == expected
