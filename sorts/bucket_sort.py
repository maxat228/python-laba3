from sorts.bubble_sort import bubble_sort
from typing import Any, Callable
from functools import cmp_to_key

def bucket_sort(arr: list[float],
                key: Callable[[Any], Any] = None,
                cmp: Callable[[Any, Any], int] = None,
                num_buckets: int = 10) -> list[float]:
    if key and not callable(key):
        raise TypeError('Ключ должен быть функцией!')

    if cmp and not callable(cmp):
        raise TypeError('Компаратор должен быть функцией!')

    if key and cmp:
        raise ValueError('Для сортировки с корзинами нельзя использовать одновременно ключ и компаратор!')

    if not isinstance(num_buckets, int):
        raise TypeError('Количество корзин должно быть натуральным числом!')

    if not arr:
        return []

    if cmp:
        return bubble_sort(arr, key=cmp_to_key(cmp))


    a = arr.copy()

    def get_value(x):
        return key(x) if key else x

    values = [get_value(x) for x in a]

    if not key:
        if not all(isinstance(v, (int, float)) for v in values):
            raise TypeError("Bucket sort без key работает только с числами!")

    mini, maxi = min(values), max(values)

    if mini == maxi:
        return a

    buckets = {i: [] for i in range(num_buckets)}
    result = []

    for item, num in zip(a, values):
        norm = (num - mini) / (maxi - mini)
        idx = int(norm * num_buckets)

        if idx == num_buckets:
            idx = num_buckets - 1

        buckets[idx].append(item)

    for bucket in buckets.values():
        result.extend(bubble_sort(bucket, key=key))

    return result


