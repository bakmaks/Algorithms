from Сортировки.tools import *


def bubble_sort(b: list):
    """
    Сортировка методом пузырька
    :param b: Список
    :return: Сортированный список
    """
    a = b.copy()
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:       # Попарное сравнение
                not_sorted = True
                a[i], a[i+1] = a[i+1], a[i]     # обмен.
    return a


def selection_sort(b: list):
    """
    Сортировка выбором
    :param b: Список
    :return: Сортированный список
    """
    a = b.copy()
    N = len(a)
    for i in range(N):
        # Выбирается наименьший элемент из несортированной части массива
        # и заменяется с a[i], который является последним элементом сортированной части.
        # Несортированная, правая часть становится меньше на один эл.
        for n in range(i+1, N):
            if a[i] > a[n]:
                a[i], a[n] = a[n], a[i]
    return a


def insertion_sort(b: list):
    """
    Сортировка вставками
    :param b: Список
    :return: Сортированный список
    """
    a = b.copy()
    for i in range(1, len(a)):
        j = i
        # Массив делится на две части, левая - сортированная(состоит в начале из одного эл.)
        # и правая - не сортированная.
        # Берётся первый эл. из правой части массива и последовательно меняясь местами (пока
        # левый не станет меньше) вставляется на своё место в левой части. Правая часть становится
        # меньше на один эл.

        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a


def merge_sort(A):
    """
    Сортировка слиянием
    :param A: Список
    :return: Отсортированный список
    """
    len_a = len(A)
    if len_a < 2:                   # Если только один эл.
        return A[:]                 # возвращается копия

    middle = len_a // 2             # Середина списка

    L = merge_sort(A[:middle])      # Передаётся копия левой половины списка
    R = merge_sort(A[middle:])      # Передаётся копия правой половины списка
    return merge(L, R)              # Возврат слитого, сортированного списка.


def test_sorts(function, ls):
    print(function.__name__)
    for i in ls:
        print(ls[i])
        print(function(ls[i]))
        print()


lists = {
    '1': [],
    '2': [1],
    '3': [5, 6, 2, 7, 3],
    '4': [2, 1, 5, 3],
    '5': [3, 5, 1, 8, 4, 2, 7, 6, 0, 9],
    '6': [9, 8, 8, 7, 7, 3, 5, 6]
}

test_sorts(bubble_sort, lists)
test_sorts(selection_sort, lists)
test_sorts(insertion_sort, lists)
test_sorts(merge_sort, lists)
