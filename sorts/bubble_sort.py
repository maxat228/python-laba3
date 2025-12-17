from typing import Any, Callable
from functools import cmp_to_key

def bubble_sort(arr: list[Any], key: Callable[[Any], Any] = None, cmp: Callable[[Any, Any], int] = None) -> list[Any]:
    if key and not callable(key):
        raise TypeError('Ключ должен быть функцией!')

    if cmp and not callable(cmp):
        raise TypeError('Компаратор должен быть функцией!')

    if key and cmp:
        raise ValueError('Для сортировки пузырьком нельзя использовать одновременно ключ и компаратор!')

    a = arr.copy()
    n = len(a)

    if cmp:
        key = cmp_to_key(cmp)

    if key is not None:
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if key(a[j]) > key(a[j + 1]):
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
    else:
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break

    return a
