from sorts.quick_sort import quick_sort

def test_quick_sort_basic():
    assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_quick_sort_empty():
    assert quick_sort([]) == []

def test_quick_sort_single():
    assert quick_sort([42]) == [42]

def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quick_sort_duplicates():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_quick_sort_negative():
    assert quick_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]

def test_quick_sort_mixed_types():
    assert quick_sort([3.14, 2.71, 1.41, 2.0, 0.0]) == [0.0, 1.41, 2.0, 2.71, 3.14]

def test_quick_sort_preserves_input():
    original = [3, 2, 1]
    result = quick_sort(original)
    assert original == [3, 2, 1]
    assert result == [1, 2, 3]

def test_quick_sort_random():
    import random
    random.seed(42)
    arr = [random.randint(0, 100) for _ in range(100)]
    result = quick_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]