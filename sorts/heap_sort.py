from typing import Any, Callable
from functools import cmp_to_key

def heap_sort(arr: list[Any], key: Callable[[Any], Any] = None, cmp: Callable[[Any, Any], int] = None) -> list[Any]:
    if key and not callable(key):
        raise TypeError('Ключ должен быть функцией!')
    if cmp and not callable(cmp):
        raise TypeError('Компаратор должен быть функцией!')
    if key and cmp:
        raise ValueError('Для heap сортировки нельзя использовать одновременно ключ и компаратор!')

    if not arr:
        return []

    a = arr.copy()
    n = len(arr)

    if cmp:
        key_func = cmp_to_key(cmp)
    elif key:
        key_func = key
    else:
        key_func = lambda x: x

    class Element:
        __slots__ = ('value', 'key')
        def __init__(self, value):
            self.value = value
            self.key = key_func(value)

        def __lt__(self, other):
            return self.key < other.key

        def __le__(self, other):
            return self.key <= other.key

        def __gt__(self, other):
            return self.key > other.key

        def __ge__(self, other):
            return self.key >= other.key

        def __eq__(self, other):
            return self.key == other.key

    elements = [Element(i) for i in a]

    def heapify(arr_heap: list[Any], n_heap: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n_heap and arr_heap[left] > arr_heap[largest]:
            largest = left

        if right < n_heap and arr_heap[right] > arr_heap[largest]:
            largest = right

        if largest != i:
            arr_heap[i], arr_heap[largest] = arr_heap[largest], arr_heap[i]
            heapify(arr_heap, n_heap, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(elements, n, i)

    for i in range(n - 1, 0, -1):
        elements[0], elements[i] = elements[i], elements[0]
        heapify(elements, i, 0)

    return [elem.value for elem in elements]






