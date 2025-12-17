import time
from generators.array_generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted


def timer_once(func, arr):
    arr_copy = arr.copy()
    start = time.time()
    func(arr_copy)
    end = time.time()
    return end - start


def benchmark_sorts_simple():
    from sorts.bubble_sort import bubble_sort
    from sorts.quick_sort import quick_sort
    from sorts.heap_sort import heap_sort

    arrays = {
        "random_1000": rand_int_array(1000, 0, 10000),
        "nearly_sorted_1000": nearly_sorted(1000, 50),
        "reverse_1000": reverse_sorted(1000),
        "many_duplicates_1000": many_duplicates(1000, 10),
    }

    algorithms = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "heap_sort": heap_sort,
    }

    print("Benchmark results:")
    print("=" * 50)

    for algo_name, algo_func in algorithms.items():
        print(f"\n{algo_name}:")
        for arr_name, arr in arrays.items():
            time_taken = timer_once(algo_func, arr)
            print(f"  {arr_name}: {time_taken:.6f} sec")