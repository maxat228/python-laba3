from typing import Any, Callable
# from functools import cmp_to_key

def counting_sort(arr: list[int], key: Callable[[Any], Any] = None, cmp: Callable[[Any, Any], int] = None) -> list[int]:
    if not arr:
        return []

    if not all(isinstance(i, int) for i in arr):
        raise TypeError("Сортировка подсчетом работает только с целыми числами!")

    if key and not callable(key):
        raise TypeError('Ключ должен быть функцией!')

    if cmp and not callable(cmp):
        raise TypeError('Компаратор должен быть функцией!')

    if key and cmp:
        raise ValueError('Для сортировки подсчетом нельзя использовать одновременно ключ и компаратор!')

    # А как дальше key и cmp встроить сюда, я не знаю
    # Во-первых, эта сортировка работает только с целыми числами
    # Во-вторых элементы между собой я никак не сравниваю
    # В-третьих, далее в цикле я использую значения как индексы списка
    # Вот эти три проблемы мне всю малину портят

    mini, maxi = min(arr), max(arr)
    range_size = maxi - mini + 1

    count = [0] * range_size

    result = []
    for num in arr:
        count[num - mini] += 1

    for i in range(range_size):
        num = mini + i
        result.extend([num] * count[i])

    return result
