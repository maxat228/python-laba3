def bucket_sort(arr: list[float]) -> list[float]:
    if not arr:
        return []

    a = arr.copy()
    n = len(a)

    min_val = min(a)
    max_val = max(a)

    if min_val == max_val:
        return a

    normalized = []
    for num in a:
        norm = (num - min_val) / (max_val - min_val)
        normalized.append(norm)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        idx = int(normalized[i] * n)
        if idx == n:
            idx = n - 1
        buckets[idx].append(a[i])

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result