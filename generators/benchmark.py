import time
import random
from generators.array_generators import *
from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.heap_sort import heap_sort
from sorts.counting_sort import counting_sort
from sorts.radix_sort import radix_sort
from sorts.bucket_sort import bucket_sort


def benchmark():
    random.seed(42)

    array_sizes = [10, 50, 100, 500, 1000]
    arrays = {}

    for size in array_sizes:
        arrays[f"случайные_{size}"] = rand_int_array(size, 0, size * 10)
        arrays[f"почти_отсорт_{size}"] = nearly_sorted(size, max(1, size // 20))
        arrays[f"обратные_{size}"] = reverse_sorted(size)
        arrays[f"дубликаты_{size}"] = many_duplicates(size, max(3, size // 30))
        arrays[f"дробные_{size}"] = rand_float_array(size)

    sorts = [
        ("Пузырьком", bubble_sort, "любые"),
        ("Быстрая", quick_sort, "любые"),
        ("Кучей", heap_sort, "любые"),
        ("Подсчётом", counting_sort, "целые"),
        ("Поразрядная", radix_sort, "целые"),
        ("Блочная", bucket_sort, "дробные"),
    ]

    print("БЕНЧМАРК: Сортировки на массивах разного размера")
    print("=" * 80)
    print(f"Тестовые размеры: {array_sizes}")
    print(f"Всего тестовых массивов: {len(arrays)}")
    print("-" * 80)

    results_by_size = {size: {} for size in array_sizes}

    for name, func, data_type in sorts:
        print(f"\n{name} ({data_type}):")
        print("-" * 40)

        for arr_name, arr in arrays.items():
            arr_size = int(arr_name.split('_')[-1])

            if data_type == "целые" and "дробные" in arr_name:
                continue
            if data_type == "дробные" and "дробные" not in arr_name:
                continue

            try:
                arr_copy = arr.copy()
                start = time.perf_counter()
                func(arr_copy)
                end = time.perf_counter()
                time_taken = end - start

                if arr_size not in results_by_size:
                    results_by_size[arr_size] = {}
                results_by_size[arr_size][name] = results_by_size[arr_size].get(name, [])
                results_by_size[arr_size][name].append(time_taken)

                print(f"  {arr_name}: {time_taken:.6f} сек")
            except Exception as e:
                print(f"  {arr_name}: ОШИБКА ({type(e).__name__})")

    print("\n" + "=" * 80)
    print("СВОДНАЯ ТАБЛИЦА: Среднее время по размерам массивов")
    print("=" * 80)
    print(
        f"{'Размер':<10} | {'Пузырьком':<12} | {'Быстрая':<10} | {'Кучей':<10} | {'Подсчётом':<12} | {'Поразрядная':<12} | {'Блочная':<10}")
    print("-" * 80)

    for size in array_sizes:
        row = [f"{size}"]
        for algo_name, _, _ in sorts:
            if algo_name in results_by_size.get(size, {}):
                times = results_by_size[size][algo_name]
                if times:
                    avg_time = sum(times) / len(times)
                    row.append(f"{avg_time:.6f}")
                else:
                    row.append("   -   ")
            else:
                row.append("   -   ")

        print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<10} | {row[3]:<10} | {row[4]:<12} | {row[5]:<12} | {row[6]:<10}")

    print("=" * 80)
