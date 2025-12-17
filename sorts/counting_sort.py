def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

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
