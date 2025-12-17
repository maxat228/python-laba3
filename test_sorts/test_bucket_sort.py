import pytest
from sorts.bucket_sort import bucket_sort

def test_bucket_sort_basic():
    assert bucket_sort([0.42, 0.32, 0.89, 0.11]) == [0.11, 0.32, 0.42, 0.89]

def test_bucket_sort_empty():
    assert bucket_sort([]) == []

def test_bucket_sort_single():
    assert bucket_sort([0.5]) == [0.5]

def test_bucket_sort_already_sorted():
    assert bucket_sort([0.1, 0.2, 0.3, 0.4, 0.5]) == [0.1, 0.2, 0.3, 0.4, 0.5]

def test_bucket_sort_reverse():
    assert bucket_sort([0.5, 0.4, 0.3, 0.2, 0.1]) == [0.1, 0.2, 0.3, 0.4, 0.5]

def test_bucket_sort_duplicates():
    assert bucket_sort([0.3, 0.1, 0.4, 0.1, 0.5]) == [0.1, 0.1, 0.3, 0.4, 0.5]

def test_bucket_sort_preserves_input():
    original = [0.3, 0.2, 0.1]
    result = bucket_sort(original)
    assert original == [0.3, 0.2, 0.1]
    assert result == [0.1, 0.2, 0.3]

def test_bucket_sort_random():
    import random
    random.seed(42)
    arr = [random.random() for _ in range(100)]
    result = bucket_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]

def test_bucket_sort_all_equal():
    assert bucket_sort([0.7, 0.7, 0.7, 0.7, 0.7]) == [0.7, 0.7, 0.7, 0.7, 0.7]

def test_bucket_sort_edge_cases():
    assert bucket_sort([0.0, 0.999, 0.5, 1.0]) == [0.0, 0.5, 0.999, 1.0]

def test_bucket_sort_negative():
    assert bucket_sort([-0.5, 0.0, 0.5]) == [-0.5, 0.0, 0.5]

def test_bucket_sort_out_of_range():
    assert bucket_sort([0.2, 0.8, 1.5]) == [0.2, 0.8, 1.5]

def test_bucket_sort_type_error_string():
    with pytest.raises(TypeError):
        bucket_sort(["0.1", "0.2", "0.3"])