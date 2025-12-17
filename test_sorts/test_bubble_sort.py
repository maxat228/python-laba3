import pytest
from sorts.bubble_sort import bubble_sort

def test_bubble_sort_basic():
    assert bubble_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_with_key():
    data = [(1, 5), (2, 3), (3, 8), (4, 1)]
    result = bubble_sort(data, key=lambda x: x[1])
    assert result == [(4, 1), (2, 3), (1, 5), (3, 8)]

    strings = ["привет", "проверяющий", "я", "старался"]
    result = bubble_sort(strings, key=len)
    assert result == ["я", "привет", "старался", "проверяющий"]


def test_bubble_sort_with_cmp():

    def reverse_cmp(a, b):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0

    assert bubble_sort([1, 3, 2, 4], cmp=reverse_cmp) == [4, 3, 2, 1]


def test_bubble_sort_error():
    with pytest.raises(ValueError):
        bubble_sort([1, 2, 3], key=lambda x: x, cmp=lambda a, b: 0)


def test_bubble_sort_stability():
    data = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
    result = bubble_sort(data, key=lambda x: x[0])
    assert result == [(1, 'a'), (1, 'c'), (2, 'b'), (3, 'd')]


def test_bubble_sort_types():
    assert bubble_sort(['c', 'b', 'a']) == ['a', 'b', 'c']
    assert bubble_sort([3.5, 1.2, 2.8]) == [1.2, 2.8, 3.5]


def test_bubble_sort_large_sorted():
    sorted_arr = list(range(1000))
    result = bubble_sort(sorted_arr)
    assert result == sorted_arr