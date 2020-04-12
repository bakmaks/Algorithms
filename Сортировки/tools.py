def check_sorted(A: list, ascending=True):
    """

    :param A: Список
    :param ascending: Если True, то список должен быть осортирован по возростанию, если False - по убыванию.
    :return: Возвращает True если список сортированный, иначе - False.
    """
    flag = True                 # Если массив сортирован
    mn = 2 * ascending - 1      # Множитель для переключения проверки сортировки по возр. или убыв.
    for i in range(len(A) - 1):
        if mn*A[i] > mn*A[i+1]:     # Если требуется проверка по убываню, то с помощью мн - условие меняется.
            flag = False
            break
    return flag


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

def merge(A: list, B: list):
    len_a = len(A)
    len_b = len(B)
    i = k = n = 0                       # Начальные индексы списков
    C = [0] * (len_a + len_b)           # Временный список

    while i < len_a and k < len_b:      # Пока в том и др. списке есть эл.
        if A[i] <= B[k]:
            C[n] = A[i]                 # Во временный список заносится меньший эл.
            i += 1                      # Индекс списка с меньшим эл. переходит на следующий эл.
        else:
            C[n] = B[k]
            k += 1
        n += 1                      # Индекс временновго списка передв. вперёд на один эл.

    while i < len_a:                    # Если в A или в B остались элементы
        C[n] = A[i]
        i += 1; n += 1
    while k < len_b:
        C[n] = B[k]
        k += 1; n += 1
    return C


if __name__ == "__main__":
    a = {
        'not sorted': [1,6,4,5],
        'sorted ascending': [0,2,6,9,10,50],
        'sorted descending': [9,8,7,6,5]
         }
    for type_of_list in a:
        print(type_of_list, a[type_of_list])
        if type_of_list == 'sorted descending':
            print(check_sorted(a[type_of_list], ascending=False))
        else:
            print(check_sorted(a[type_of_list]))
