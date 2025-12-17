from typing import Any, Callable, List
from functools import cmp_to_key

def quick_sort(arr: list[Any], key: Callable[[Any], Any] = None, cmp: Callable[[Any, Any], int] = None) -> List[Any]:
    if key and not callable(key):
        raise TypeError('Ключ должен быть функцией!')

    if cmp and not callable(cmp):
        raise TypeError('Компаратор должен быть функцией!')

    if key and cmp:
        raise ValueError('Для быстрой сортировки нельзя использовать одновременно ключ и компаратор!')

    if cmp:
        key = cmp_to_key(cmp)

    a = arr.copy()

    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    def compare(a, b):
        if key:
            a_key = key(a)
            b_key = key(b)
            return (a_key > b_key) - (a_key < b_key)
        return (a > b) - (a < b)

    left, middle, right = [], [], []

    for num in a:
        comp = compare(num, pivot)
        if comp < 0:
            left.append(num)
        elif not comp:
            middle.append(num)
        else:
            right.append(num)

    return quick_sort(left, key=key) + middle + quick_sort(right, key=key)
