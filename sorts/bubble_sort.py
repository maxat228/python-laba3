from typing import Any

def bubble_sort(arr: list[Any]) -> list[Any]:
    a = arr.copy()
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a
