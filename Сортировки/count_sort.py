import sys
from collections import Counter


def count_sort(A, m):
    """
    Сортировка подсчётом.
    Первая строка содержит число 1 <= n <= 10^4, вторая — n натуральных чисел,
    не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.

    :param m - наибольшее число в списке
    :param A - список чисел
    """
    a = Counter(A)  # Подсчёт кол-ва одинаковых значений
    for key in range(m+1):    # Перебор значений по порядку. Известно, что значения  < 11
        if key in a:          # Если значение есть в словаре
            for _ in range(a[key]):
                print(key, end=' ')   # Печать через пробел


if __name__ == '__main__':
    # Ввод списка. (через пробел)
    reader = (map(int, line.split()) for line in sys.stdin)
    x = list(next(reader))
    print(x)
    count_sort(x, 10)
