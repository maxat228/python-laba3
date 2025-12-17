import sys
import random

from algorythms.factorial import factorial, factorial_recursive
from algorythms.fibonacci import fibonacci, fibonacci_recursive

from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.heap_sort import heap_sort
from sorts.counting_sort import counting_sort
from sorts.radix_sort import radix_sort
from sorts.bucket_sort import bucket_sort

from data_structures.stack import Stack
from data_structures.queue import Queue

from generators.array_generators import (
    rand_int_array, nearly_sorted, many_duplicates,
    reverse_sorted, rand_float_array
)

from generators.benchmark import benchmark

def run_benchmark():
    print("=" * 60)
    print("БЕНЧМАРК: Сравнение скорости 6 сортировок")
    print("=" * 60)
    benchmark()
    print()


def demo_algorithms():
    number = random.randint(1, 20)
    print("=== Математические алгоритмы ===")
    print(f"Факториал итеративный ({number}!): {factorial(number)}")
    print(f"Факториал рекурсивный ({number}!): {factorial_recursive(number)}")
    print(f"Число Фибоначчи итеративное (F({number})): {fibonacci(number)}")
    print(f"Число Фибоначчи рекурсивное (F({number})): {fibonacci_recursive(number)}")
    print()


def demo_sorts():
    print("=== 6 Алгоритмов сортировки ===")

    random.seed(42)

    small_arr = [3, 1, 4, 1, 5, 9, 2]
    print(f"Исходный массив: {small_arr}")
    print(f"• bubble_sort:    {bubble_sort(small_arr.copy())}")
    print(f"• quick_sort:     {quick_sort(small_arr.copy())}")
    print(f"• heap_sort:      {heap_sort(small_arr.copy())}")

    int_arr = rand_int_array(8, 0, 20)
    print(f"\nДля counting/radix sort: {int_arr}")
    print(f"• counting_sort:  {counting_sort(int_arr.copy())}")
    print(f"• radix_sort:     {radix_sort(int_arr.copy())}")

    float_arr = rand_float_array(6)
    print(f"\nДля bucket_sort: {[round(x, 3) for x in float_arr]}")
    print(f"• bucket_sort:    {[round(x, 3) for x in bucket_sort(float_arr.copy())]}")
    print()


def demo_structures():
    print("=== Структуры данных ===")

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack: push(10, 20, 30)")
    print(f"• pop() = {stack.pop()}")  # 30
    print(f"• pop() = {stack.pop()}")  # 20
    print(f"• Осталось в стеке: {len(stack)} элемент")

    queue = Queue()
    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")
    print(f"\nQueue: enqueue('первый', 'второй', 'третий')")
    print(f"• dequeue() = '{queue.dequeue()}'")
    print(f"• dequeue() = '{queue.dequeue()}'")
    print()


def demo_generators():
    number = random.randint(1, 100)
    unique = random.randint(3, 10)
    swaps = random.randint(3, 10)
    print("=== 5 Генераторов тестовых массивов ===")

    random.seed(123)

    print(f"1. rand_int_array({number}, 1, 10):")
    print(f"   {rand_int_array(number, 1, 10)}")

    print(f"\n2. nearly_sorted({number}, {swaps}):")
    arr = nearly_sorted(number, swaps)
    print(f"   {arr}  # почти отсортирован")

    print(f"\n3. many_duplicates({number}, {unique}):")
    print(f"   {many_duplicates(number, unique)}")

    print(f"\n4. reverse_sorted({number}):")
    print(f"   {reverse_sorted(number)}")

    print(f"\n5. rand_float_array({number}):")
    floats = rand_float_array(number)
    print(f"   {[round(x, 3) for x in floats]}  # числа 0.0..1.0")
    print()


def demo_all():
    print("\n" + "=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 3: АЛГОРИТМИЧЕСКИЙ МИНИ-ПАКЕТ")
    print("=" * 60 + "\n")

    demo_algorithms()
    demo_sorts()
    demo_structures()
    demo_generators()
    run_benchmark()

    print("=" * 60)
    print("Демонстрация завершена!")
    print("=" * 60)


def show_help():
    print("Использование: python main.py [команда]\n")
    print("Команды:")
    print("  all         - Полная демонстрация (алгоритмы + сортировки + структуры + генераторы + бенчмарк)")
    print("  algorithms  - Математические алгоритмы (факториал и числа Фибоначчи)")
    print("  sorts       - 6 алгоритмов сортировки с примерами")
    print("  structures  - Структуры данных Stack и Queue")
    print("  generators  - 5 генераторов тестовых массивов")
    print("  benchmark   - Сравнение скорости всех сортировок (таблица)")
    print("  help        - Эта справка")
    print("\nПример: python main.py all")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "all":
        demo_all()
    elif command == "algorithms":
        demo_algorithms()
    elif command == "sorts":
        demo_sorts()
    elif command == "structures":
        demo_structures()
    elif command == "generators":
        demo_generators()
    elif command == "benchmark":
        run_benchmark()
    elif command == "help":
        show_help()
    else:
        print(f"Ошибка: неизвестная команда '{command}'\n")
        show_help()


if __name__ == "__main__":
    main()
