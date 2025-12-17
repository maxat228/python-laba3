from generators.array_generators import *

def test_rand_int_array():
    arr = rand_int_array(10, 0, 5)
    assert len(arr) == 10
    for num in arr:
        assert 0 <= num <= 5

def test_nearly_sorted():
    arr = nearly_sorted(10, 3)
    assert len(arr) == 10
    assert set(arr) == set(range(10))

def test_many_duplicates():
    arr = many_duplicates(10, 3)
    assert len(arr) == 10
    for num in arr:
        assert 0 <= num <= 2

def test_reverse_sorted():
    arr = reverse_sorted(5)
    assert arr == [4, 3, 2, 1, 0]

def test_rand_float_array():
    arr = rand_float_array(10, 0.0, 1.0)
    assert len(arr) == 10
    for num in arr:
        assert 0.0 <= num <= 1.0

def test_random_seed():
    random.seed(42)
    arr1 = rand_int_array(5, 0, 10)
    random.seed(42)
    arr2 = rand_int_array(5, 0, 10)
    assert arr1 == arr2