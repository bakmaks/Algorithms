from rcviz import viz
from PIL import Image


# @viz
def fib1(n: int):
    """
    Простая рекурсивная ф. для вычисления числа Фибоначи.
    Очень медленная работа
    """
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)
#----------------------------------------------------------------------------------------------------
# Глобальная переменная "cache", что бы при выходе из рекурсии повторно не вычилялись значения n
cache = {}

# @viz
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]
#------------------------------------------------------------------------------------------------------


def memo(func):
    """
    Декоратор для кеширования функции для вычислени чисел фибоначи.
    При этом мы избавляемся от ранеее объявленной, глобальной переменной "cache"
    :param func:
    :return:
    """
    temp = {}
    def wrap(n):
        if n not in temp:
            temp[n] = func(n)
        return temp[n]

    return wrap


@memo
def fib(n):
    """
    Простая рекурсивная ф. для вычисления числа Фибоначи с декоратором.
    """
    assert n >= 0
    return n if n <= 1 else fib(n-1) + fib(n-2)


def iter_fib(n):
    """
    Вычисление числа Фибоначи с помощью итерраций.
    :param n:
    :return:
    """
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib1(8))     # 21
# Строки вызываются если раскомментировать декоратор @viz у fib1(n) и n <= 5
# иначе очень большой файл изображения
# image = Image.open('fib1.png')
# image.show()


print(fib2(8))     # 21
# Строки вызываются если раскомментировать декоратор @viz у fib2(n) и n <= 10
# иначе очень большой файл изображения
# image1 = Image.open('fib2.png')
# image1.show()

print(iter_fib(8))      # 21

# Превышение глубины рекурсии
# print(fib2(8000))   # RecursionError: maximum recursion depth exceeded in comparison


print('Работа декоратора :')
fib1 = memo(fib1)

print(fib1(200))

print(fib(200))

print('iter_fib, n = 8000')
print(iter_fib(8000))
