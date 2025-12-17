def heap_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    a = arr.copy()
    n = len(a)

    def heapify(arr_heap, n_heap, i):
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
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a
