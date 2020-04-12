from Сортировки.sorts import *
from alg_utils import *
import random as rnd


def check_sorted(A: list, ascending=True):
    """
    Функция проверяет отсортирован ли список
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




def test_sorts(functions, lsts):
    for function in functions:
        print(function.__name__)
        i = 1
        for lst in lsts:
            sorted_lst = function(lst)
            if check_sorted(sorted_lst):
                print("тест № {} пройден\n".format(i))
            else:
                print("Тест № {} не пройден, должно быть\n{},\n а получено:\n{}\n".
                      format(i, sorted(lst), lst))
            i += 1
        print('-'*70)


if __name__ == '__main__':
    lists = [[], [1]]
    for i in range(3, 7):
        a = [x for x in range(rnd.randint(2, 10))]
        rnd.shuffle(a)
        lists.append(a)

    lists = sorted(lists, key=len)

    function_lst = [bubble_sort, selection_sort, insertion_sort, merge_sort, hoar_sort]

    test_sorts(function_lst, lists)


