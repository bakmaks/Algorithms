def ext(a: float, n: int):
    """
    Быстрое возведение в степень. Использование рекурсии.
    Если n чётное, то a**n = (a**2)**(n/2)
    Если n нечётное, то a**n = a**(n-1) * a
    :param a: число
    :param n: степень
    :return:
    """
    if n == 0:
        return 1
    elif n % 2 == 1:    # n нечётное
        return ext(a, n - 1) * a
    else:               # n чётное
        return ext(a ** 2, n // 2)


print('встроенная pow = ', pow(2, 10))
print('ext = ', ext(2, 10))