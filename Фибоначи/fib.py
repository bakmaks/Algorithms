from rcviz import viz
from PIL import Image
from alg_utils import timed


# @viz
def fib(n: int):
    """
    Простая рекурсивная ф. для вычисления числа Фибоначи.
    Очень медленная работа
    """
    assert n >= 0
    return n if n <= 1 else fib(n-1) + fib(n-2)
#----------------------------------------------------------------------------------------------------
# Глобальная переменная "cache", что бы при выходе из рекурсии повторно не вычилялись значения n
cache = {}

# @viz
def cache_fib(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else cache_fib(n-1) + cache_fib(n-2)
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
def memo_fib(n):
    """
    Простая рекурсивная ф. для вычисления числа Фибоначи с декоратором.
    """
    assert n >= 0
    return n if n <= 1 else memo_fib(n-1) + memo_fib(n-2)


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
if __name__ == '__main__':
    print(fib(8))     # 21
    # Строки вызываются если раскомментировать декоратор @viz у fib(n) и n <= 5
    # иначе очень большой файл изображения
    # image = Image.open('fib.png')
    # image.show()


    print(cache_fib(8))     # 21
    # Строки вызываются если раскомментировать декоратор @viz у cache_fib(n) и n <= 10
    # иначе очень большой файл изображения
    # image1 = Image.open('cache_fib.png')
    # image1.show()

    print(iter_fib(8))      # 21

    # Превышение глубины рекурсии
    # print(cache_fib(8000))   # RecursionError: maximum recursion depth exceeded in comparison


    print('Работа декоратора :')
    fib = memo(fib)

    print(fib(200))

    print(memo_fib(200))

    print('iter_fib, n = 8000')
    print(iter_fib(8000))

    print('Время выполнения функции iter_fib при n=8000:')
    print(timed(iter_fib, 8000))
