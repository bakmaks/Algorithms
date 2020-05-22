from collections import deque

def bubble_sort(b: list):
    """
    Сортировка методом пузырька
    :param b: Список
    :return: Сортированный список
    """
    a = b[:]
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
    a = b[:]
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
    a = b[:]
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

##############################################################################################################
def merge(A: list, B: list):
    """
    Функция слияния двух сортированных списков. Попарно соавниваются эл. двух списков. Меньший эл. заносится
    во временный список. Индекс списка из которого эл. был перенесён во временный список сдвигается на
    след. эл., у др. списка индекс остаётся неизменным, и соответсвенно увеличивается индекс
    временного списка. Действия повторяются до тех пор, пока в одном из списсков не закончатся эл.
    Оставшиеся эл. переносятся во временный список

    :param A: список
    :param B: список
    :return: C список слитый из двух A и B
    """
    len_a = len(A)
    len_b = len(B)
    i = k = n = 0                       # Начальные индексы списков
    C = [0] * (len_a + len_b)           # Временный список

    count = 0

    while i < len_a and k < len_b:      # Пока в том и др. списке есть эл.
        if A[i] <= B[k]:
            C[n] = A[i]                 # Во временный список заносится меньший эл.
            i += 1                      # Индекс списка с меньшим эл. переходит на следующий эл.

        else:
            C[n] = B[k]
            k += 1

            count += 1

        n += 1                      # Индекс временновго списка передв. вперёд на один эл.
    print('count', count)
    while i < len_a:                    # Если в A или в B остались элементы
        C[n] = A[i]
        i += 1; n += 1
    while k < len_b:
        C[n] = B[k]
        k += 1; n += 1
    return C, count


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

##################################################################################################################
def iter_merge_sort(a):
    sort_deque = deque(a)
    g_count = 0
    while len(sort_deque) > 1:
        one = sort_deque.popleft()
        two = sort_deque.popleft()
        one = one if type(one) is list else [one]
        two = two if type(two) is list else [two]
        el, t_count = merge(one, two)
        g_count += t_count
        sort_deque.append(el)
    print('g_count =', g_count)
    return [] if len(sort_deque) == 0 else sort_deque.pop()

##################################################################################################################

def hoar_sort(A):
    if len(A) <= 1:
        return A
    barrier = A[0]          # Барьерный элемент
    L, M, R = [], [], []    # Списки для эл. слева, равных барьеру и справа.
    for x in A:
        if x < barrier:     # Если меньше барьера
            L.append(x)
        elif x == barrier:  # Если равно барьеру
            M.append(x)
        else:
            R.append(x)
    # Слияние отсортированных элементов
    return hoar_sort(L) + M + hoar_sort(R)

x = [1, 2, 3, 5, 4]

print(iter_merge_sort(x))