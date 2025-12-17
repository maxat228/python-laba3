import random
import pytest
from sorts.heap_sort import heap_sort

def test_basic_sort():
    assert heap_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]


def test_empty():
    assert heap_sort([]) == []


def test_single():
    assert heap_sort([42]) == [42]


def test_sorted():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reversed():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_random():
    random.seed(42)
    arr = [random.randint(-100, 100) for _ in range(50)]
    result = heap_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]
    assert arr != result


def test_duplicates():
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_key():
    arr = ["яблоко", "банан", "апельсин", "киви"]
    result = heap_sort(arr, key=len)
    assert [len(s) for s in result] == [4, 5, 6, 8]


def test_cmp():
    def cmp_desc(a: int, b: int) -> int:
        if a < b: return 1
        if a > b: return -1
        return 0

    arr = [3, 1, 4, 2]
    result = heap_sort(arr, cmp=cmp_desc)
    assert result == [4, 3, 2, 1]


def test_immutability():
    original = [3, 2, 1]
    heap_sort(original)
    assert original == [3, 2, 1]


def test_all_equal():
    assert heap_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]


def test_key_not_callable():
    with pytest.raises(TypeError):
        heap_sort([1, 2, 3], key="в очередной раз какая-то фигня")


def test_cmp_not_callable():
    with pytest.raises(TypeError):
        heap_sort([1, 2, 3], cmp=313)


def test_key_and_cmp_together():
    with pytest.raises(ValueError):
        heap_sort([1, 2, 3], key=len, cmp=lambda a, b: 0)
