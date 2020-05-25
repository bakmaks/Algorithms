
def get_inversions_with_bubble_sort(b: list):
    """
    Наивный алгоритм посчёта инверсий
    Сортировка методом пузырька
    :param b: Список
    :return: Сортированный список, кол-во инверсий.
    """
    a = b[:]
    not_sorted = True
    count = 0           # Счётчик инверсий
    while not_sorted:
        not_sorted = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:  # Попарное сравнение
                not_sorted = True
                a[i], a[i + 1] = a[i + 1], a[i]  # обмен.
                count += 1
    return a, count


#######################################################################################################################
Count = {'count': 0}    # Счётчик инверсий
def get_inversions_with_merge_sort(A: list):
    def merge(A: list, B: list):
        len_a = len(A)
        len_b = len(B)
        i = k = n = 0  # Начальные индексы списков
        C = [0] * (len_a + len_b)  # Временный список

        while i < len_a and k < len_b:  # Пока в том и др. списке есть эл.
            if A[i] <= B[k]:
                C[n] = A[i]  # Во временный список заносится меньший эл.
                i += 1  # Индекс списка с меньшим эл. переходит на следующий эл.
            else:
                C[n] = B[k]
                k += 1
                Count['count'] += (len_a - i)   # СЧЁТЧИК ИНВЕРСИЙ
            n += 1  # Индекс временновго списка передв. вперёд на один эл.

        while i < len_a:  # Если в A или в B остались элементы
            C[n] = A[i]
            i += 1;
            n += 1
        while k < len_b:
            C[n] = B[k]
            k += 1;
            n += 1
        return C

    len_a = len(A)
    if len_a < 2:                   # Если только один эл.
        return A[:]                 # возвращается копия

    middle = len_a // 2             # Середина списка

    L = get_inversions_with_merge_sort(A[:middle])      # Передаётся копия левой половины списка
    R = get_inversions_with_merge_sort(A[middle:])      # Передаётся копия правой половины списка
    return merge(L, R)              # Возврат слитого, сортированного списка.

########################################################################################################################


if __name__ == "__main__":
    # print('введите список: ')
    # reader = (map(int, line.split(' ')) for line in sys.stdin)
    # a = list(next(reader))
    # get_inversions_with_bubble_sort(a)
    # print(c)
    # a = [randint(0,100) for i in range(7)]
    # print(a)
    # # a = [3,2,1]
    # print(get_inversions_with_merge_sort(a))
    x = list(map(int, '6 5 8 6 0 4'.split()))
    get_inversions_with_merge_sort(x)
    print(Count['count'])