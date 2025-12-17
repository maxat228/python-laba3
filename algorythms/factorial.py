def factorial(n: int) -> int:
    if isinstance(n, float):
        if n == int(n):
            n = int(n)
        else:
            raise TypeError("Факториал определен только для неотрицательных целых чисел!")

    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел!")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if isinstance(n, float):
        if n == int(n):
            n = int(n)
        else:
            raise TypeError("Факториал определен только для неотрицательных целых чисел!")

    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел!")

    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
