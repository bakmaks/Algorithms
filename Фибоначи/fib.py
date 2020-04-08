def fib1(n: int):
    """
    Простая рекурсивная ф. для вычисления числа Фибоначи.
    Очень медленная работа
    """
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)

# Глобальная переменная "cache", что бы при выходе из рекурсии повторно не вычилялись значения n
cache = {}

def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]


print(fib1(8))     # 21

print(fib2(8))     # 21
print(fib2(800))

# Превышение глубины рекурсии
print(fib2(8000))   # RecursionError: maximum recursion depth exceeded in comparison

