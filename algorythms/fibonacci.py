def fibonacci(n: int) -> int:
    if isinstance(n, float):
        if n == int(n):
            n = int(n)
        else:
            raise TypeError("Номер члена последовательности должен быть целым числом!")

    if n < 0:
        raise ValueError("Номер члена последовательности Фибоначчи должен быть натуральным числом!")

    if n == 0:
        return 0

    if n == 1:
        return 1

    one, two = 1, 1
    for i in range(n - 1):
        one, two = two, one + two
    return one


def fibonacci_recursive(n: int) -> int:
    if isinstance(n, float):
        if n == int(n):
            n = int(n)
        else:
            raise TypeError("Номер члена последовательности должен быть целым числом!")

    if n < 0:
        raise ValueError("Номер члена последовательности Фибоначчи должен быть натуральным числом!")

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
