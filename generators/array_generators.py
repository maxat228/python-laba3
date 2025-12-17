import random

def rand_int_array(n, lo, hi):
    result = []
    for _ in range(n):
        result.append(random.randint(lo, hi))
    return result


def nearly_sorted(n, swaps):
    arr = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n, k_unique=5):
    arr = []
    for _ in range(n):
        arr.append(random.randint(0, k_unique-1))
    return arr


def reverse_sorted(n):
    return list(range(n-1, -1, -1))


def rand_float_array(n, lo=0.0, hi=1.0):
    arr = []
    for _ in range(n):
        arr.append(random.uniform(lo, hi))
    return arr
