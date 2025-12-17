import pytest
from sorts.bucket_sort import bucket_sort

def test_bucket_sort_basic():
    assert bucket_sort([]) == []
    assert bucket_sort([5.5]) == [5.5]
    assert bucket_sort([0.78, 0.17, 0.39]) == [0.17, 0.39, 0.78]


def test_bucket_sort_negative():
    assert bucket_sort([-5.5, 3.2, -1.1, 0.0]) == [-5.5, -1.1, 0.0, 3.2]


def test_bucket_sort_different_buckets():
    arr = [0.78, 0.17, 0.39, 0.26]
    assert bucket_sort(arr, num_buckets=1) == sorted(arr)
    assert bucket_sort(arr, num_buckets=5) == sorted(arr)
    assert bucket_sort(arr, num_buckets=100) == sorted(arr)


def test_bucket_sort_with_key():
    data = [{"x": 0.7}, {"x": 0.2}, {"x": 0.5}]
    result = bucket_sort(data, key=lambda d: d["x"])
    assert result == [{"x": 0.2}, {"x": 0.5}, {"x": 0.7}]


def test_bucket_sort_with_cmp():
    def reverse_cmp(a, b):
        return 1 if a < b else (-1 if a > b else 0)

    assert bucket_sort([0.3, 0.1, 0.9], cmp=reverse_cmp) == [0.9, 0.3, 0.1]


def test_bucket_sort_type_errors():
    with pytest.raises(TypeError):
        bucket_sort(["a", "b", "c"])

    with pytest.raises(TypeError):
        bucket_sort([1, 2, 3], num_buckets="sixseven")


def test_bucket_sort_parameter_errors():
    with pytest.raises(ValueError):
        bucket_sort([1, 2, 3], key=lambda x: x, cmp=lambda a, b: 0)

    with pytest.raises(TypeError):
        bucket_sort([1, 2, 3], key="какая-то фигня")


def test_bucket_sort_all_equal():
    assert bucket_sort([3.14, 3.14, 3.14]) == [3.14, 3.14, 3.14]
    assert bucket_sort([0, 0, 0]) == [0, 0, 0]


def test_bucket_sort_edge_case():
    assert bucket_sort([0.0, 0.999, 0.001]) == [0.0, 0.001, 0.999]