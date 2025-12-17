import pytest
from sorts.counting_sort import counting_sort

def test_counting_sort_basic():
    assert counting_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert counting_sort([]) == []
    assert counting_sort([1]) == [1]


def test_counting_sort_negatives():
    assert counting_sort([-5, 3, -1, 0, 2]) == [-5, -1, 0, 2, 3]


def test_counting_sort_duplicates():
    assert counting_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_counting_sort_type_errors():
    with pytest.raises(TypeError):
        counting_sort([1.5, 2.3, 0.7])

    with pytest.raises(TypeError):
        counting_sort(["a", "b", "c"])

    with pytest.raises(TypeError):
        counting_sort([1, "two", 3])


def test_counting_sort_key_cmp_error():
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3], key=lambda x: x, cmp=lambda a, b: 0)


def test_counting_sort_key_not_callable():
    with pytest.raises(TypeError):
        counting_sort([1, 2, 3], key="не функция")

    with pytest.raises(TypeError):
        counting_sort([1, 2, 3], key=123)


def test_cmp_not_callable():
    with pytest.raises(TypeError):
        counting_sort([1, 2, 3], cmp="не функция")

    with pytest.raises(TypeError):
        counting_sort([1, 2, 3], cmp=[1, 2, 3])