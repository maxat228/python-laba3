import sys

from algorythms.factorial import factorial, factorial_recursive
from algorythms.fibonacci import fibonacci, fibonacci_recursive

from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.heap_sort import heap_sort

from data_structures.stack import Stack
from data_structures.queue import Queue

# Импорт генераторов
from generators.array_generators import (
    rand_int_array, nearly_sorted, many_duplicates,
    reverse_sorted, rand_float_array
)

from generators.benchmark import benchmark_sorts_simple


def demo_algorithms():
    print("=== Алгоритмы ===")
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial_recursive(5) = {factorial_recursive(5)}")
    print(f"fib(10) = {fibonacci(10)}")
    print(f"fib_recursive(10) = {fibonacci_recursive(10)}")
    print()


def demo_sorts():
    print("=== Сортировки ===")
    arr = [3, 1, 4, 1, 5, 9, 2]
    print(f"Исходный: {arr}")
    print(f"bubble_sort: {bubble_sort(arr)}")
    print(f"quick_sort: {quick_sort(arr)}")
    print(f"heap_sort: {heap_sort(arr)}")
    print()


def demo_structures():
    print("=== Структуры данных ===")

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Stack: push(1), push(2), pop() = {stack.pop()}")

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Queue: enqueue(1), enqueue(2), dequeue() = {queue.dequeue()}")
    print()


def demo_generators():
    print("=== Генераторы ===")
    print(f"rand_int_array(5, 1, 10) = {rand_int_array(5, 1, 10)}")
    print(f"nearly_sorted(5, 2) = {nearly_sorted(5, 2)}")
    print(f"many_duplicates(5, 2) = {many_duplicates(5, 2)}")
    print(f"reverse_sorted(5) = {reverse_sorted(5)}")
    print(f"rand_float_array(3) = {rand_float_array(3)}")
    print()


def run_benchmark():
    print("=== Бенчмарк сортировок ===")
    benchmark_sorts_simple()
    print()


def show_help():
    print("Использование: python main.py [команда]")
    print("Команды:")
    print("  all         - запустить всё")
    print("  algorithms  - демо алгоритмов")
    print("  sorts       - демо сортировок")
    print("  structures  - демо структур данных")
    print("  generators  - демо генераторов")
    print("  benchmark   - запустить бенчмарк")
    print("  help        - эта справка")
    print()


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "all":
        demo_algorithms()
        demo_sorts()
        demo_structures()
        demo_generators()
        run_benchmark()

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
        print(f"Неизвестная команда: {command}")
        show_help()


if __name__ == "__main__":
    main()