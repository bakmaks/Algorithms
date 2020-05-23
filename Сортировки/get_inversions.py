import sys
from collections import deque


def get_inversions_with_bubble_sort(b: list):
    """
    Сортировка методом пузырька
    :param b: Список
    :return: Сортированный список
    """
    a = b[:]
    not_sorted = True
    count = 0
    while not_sorted:
        not_sorted = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:       # Попарное сравнение
                not_sorted = True
                a[i], a[i+1] = a[i+1], a[i]     # обмен.
                count += 1
    return a, count

#######################################################################################################################

def get_inversions_with_merge_sort(a: list):
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
        i = k = n = 0  # Начальные индексы списков
        C = [0] * (len_a + len_b)  # Временный список

        while i < len_a and k < len_b:  # Пока в том и др. списке есть эл.
            if A[i] <= B[k]:
                C[n] = A[i]  # Во временный список заносится меньший эл.
                i += 1  # Индекс списка с меньшим эл. переходит на следующий эл.
            else:
                C[n] = B[k]
                k += 1
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

    sort_deque = deque(a)

    while len(sort_deque) > 1:
        one = sort_deque.popleft()
        two = sort_deque.popleft()
        one = one if type(one) is list else [one]
        two = two if type(two) is list else [two]
        sort_deque.append(merge(one, two))
    return [] if len(sort_deque) == 0 else sort_deque.pop()


if __name__ == "__main__":
    reader = (map(int, line.split(' ')) for line in sys.stdin)
    a = list(next(reader))
    _, c = get_inversions_with_bubble_sort(a)
    print(c)