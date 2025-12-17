from sorts.heap_sort import heap_sort

def test_heap_sort_basic():
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_heap_sort_empty():
    assert heap_sort([]) == []

def test_heap_sort_single():
    assert heap_sort([42]) == [42]

def test_heap_sort_already_sorted():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_heap_sort_duplicates():
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_heap_sort_negative():
    assert heap_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]

def test_heap_sort_mixed_types():
    assert heap_sort([3.14, 2.71, 1.41, 2.0, 0.0]) == [0.0, 1.41, 2.0, 2.71, 3.14]

def test_heap_sort_preserves_input():
    original = [3, 2, 1]
    result = heap_sort(original)
    assert original == [3, 2, 1]
    assert result == [1, 2, 3]

def test_heap_sort_random():
    import random
    random.seed(42)
    arr = [random.randint(0, 100) for _ in range(100)]
    result = heap_sort(arr)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]

def test_heap_sort_all_equal():
    assert heap_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]