def partition(a, l, r):
    """
    Возвращает значение индекса массива, при котором в левой части массива оказываются все элементы
    меньшие чем X, а в правой большие чем X. Изначально барьерным элементом выбирается первый элемент массива.
    :param a: массив
    :param l: Начальный индекс барьерного элемента
    :param r: Индекс конечного элемента
    :return: Окончательный индекс барьерного элемента
    """
    X = a[l]    # Барьерный эл.
    j = l       # Изначальный индекс барьерного эл.
    for i in range(l + 1, r):
        if a[i] <= X:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(A, l=0, r=None):
    """
    Быстрая сортировка без выделения дополнительной памяти
    :param A: Сортируемый массив
    :param l: Начало массива
    :param r: Длина массива
    :return: Выход если массив пустой
    """
    r = r if r is not None else len(A)
    if l >= r:
        return
    m = partition(A, l, r)
    quick_sort(A, l, m)
    quick_sort(A, m + 1, r)


# def quicksort(nums, fst, lst):
#     if fst >= lst: return
#
#     i, j = fst, lst
#     pivot = nums[random.randint(fst, lst)]
#
#     while i <= j:
#         while nums[i] < pivot: i += 1
#         while nums[j] > pivot: j -= 1
#         if i <= j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i, j = i + 1, j - 1
#     quicksort(nums, fst, j)
#     quicksort(nums, i, lst)

if __name__ == '__main__':
    y = []
    quick_sort(y)
    print(y)
    # quicksort(y, 0, len(y))
    # print(y)
