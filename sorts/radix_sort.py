def radix_sort(arr: list[int]) -> list[int]:
    if not all(isinstance(i, int) for i in arr):
        raise TypeError("Сортировка Radix работает только с целыми числами!")

    if not arr or len(arr) == 1:
        return arr.copy()

    positive = [i for i in arr if i >= 0]
    negative = [abs(i) for i in arr if i < 0]

    result = []
    buckets = {i: [] for i in range(10)}

    if negative:
        current = negative.copy()
        maxi = max(current)
        divider = 1

        while maxi // divider > 0:
            for num in current:
                digit = (num // divider) % 10
                buckets[digit].append(num)

            current = []
            for digit in range(10):
                current.extend(buckets[digit])
                buckets[digit].clear()

            divider *= 10

        result.extend([-i for i in reversed(current)])

    if positive:
        current = positive.copy()
        maxi = max(current)
        divider = 1

        while maxi // divider > 0:
            for num in current:
                digit = (num // divider) % 10
                buckets[digit].append(num)

            current = []
            for digit in range(10):
                current.extend(buckets[digit])
                buckets[digit].clear()

            divider *= 10

        result.extend(current)

    return result
