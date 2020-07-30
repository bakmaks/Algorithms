import sys


def count_sort(A, n, m):
    """
    Сортировка подсчётом.
    Первая строка содержит число 1 <= n <= 10^4, вторая — n натуральных чисел,
    не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.
    :param m - наибольшее число в списке
    :param n - кол-во чисел
    :param A - список чисел
    """
    a = [0] * m
    print(a)


if __name__ == '__main__':
    reader = (map(int, line.split()) for line in sys.stdin)
    n = list(next(reader))[0]
    print(str(n))
    x = list(next(reader))
    print(x)
    count_sort(x, n, 10)