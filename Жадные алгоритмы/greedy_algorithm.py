
def segments_covered_with_dots():
    """
    Необходимо найти множество точек, для которого каждый из отрезков, лежащих на прямой,
    (отрезки могут лежать друг на друге) содержит хотя бы одну из точек
    (не обязательно точка должна лежать на каждом отрезке сразу)
    и размер множества был бы минимальным.

    :return:
    """
    print('Введите кол-во строк:')
    seg_numbers = int(input())
    seg_list = []
    print('Введите отрезок:')
    for i in range(seg_numbers):
        key = sorted(map(int, input().split(' ')))
        seg_list.append(key)                        # Список отрезков
    seg_list.sort(key=lambda x: x[1])               # Отрезки сортируются по правым концам
    dots = [seg_list.pop(0)[1]]                     # выбирается правая точка первого отрезка и заносится в список
    for left_dot, right_dot in seg_list:            # Выбираем левый и правый концы отрезка
        # Если точка меньше левого конца следующего отрезка, то правая точка этого отрезка заносится во множество.
        # Отрезки были упорядочены по правым концам, соответсвенно - если правая точка первого отрезка
        # больше чем левые концы последующих отрезков, значит она также будет лежать
        # и на них. Как только она становится меньше чем левый конец следующего отрезка,
        # правая точка этого отрезка заносится во множество и т. д.
        if dots[-1] < left_dot:
            dots.append(right_dot)
    print(len(dots))
    print(' '.join(list(map(str, dots))))

# Примеры работы
# Sample Input 1:
#
# 3    Кол-во отрезков.
# 1 3
# 2 5
# 3 6
# Sample Output 1:
#
# 1     Кол-во точек во множестве
# 3     Сами точки

# Sample Input 2:
#
# 4     Кол-во отрезков
# 4 7
# 1 3
# 2 5
# 5 6
# Sample Output 2:
#
# 2     Кол-во точек во множестве
# 3 6   Сами точки
#-----------------------------------------------------------------------------------------------------------------

def continuous_backpack():
    """
    Первая строка содержит количество предметов и вместимость рюкзака.
    Каждая из следующих n строк задаёт стоимость и объём предмета (все числа целые).
    Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
    стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
    с точностью не менее трёх знаков после запятой.
    У каждой вещи вычисляется удельная стоимость, затем они сортируются  в порядке
    убывания удельной стоимости. Затем заполняется рюкзак, сначала предметами  с самой дорогй
    удельной стоимостью, потом берётся предмет с меньшей стоимостью и т. д.
    :return:
    """
    N, W = map(int, input('Введите чере пробел кол-во предметов и вместимость рюкзака: ').split())
    L = []
    for i in range(N):
        c, w = map(int, input('Введите чере пробел стоимось предмета и объём:').split())
        L.append([(c/w if w > 0 else 0), w])    # c/w - удельная стоимость, w - объём вещи.
    max_cost = 0
    L.sort(key=lambda x: x[0], reverse=True)    # Сортировка по убыванию удельной стоимости.
    for thing in L:
        if W > thing[1]:        # Объём рюкзака больше объёма вещи.
            max_cost += thing[0] * thing[1]
            W -= thing[1]       # Объём рюкзака уменьшается на объём вещи
        else:                   # Если объём рюкзака меньше объёма вещи
            max_cost += W * thing[0]
            break
    print('{0:.3f}'.format(max_cost))

# Sample Input:
#
# 3 50
# 60 20
# 100 50
# 120 30

# Sample Output:
#
# 180.000

#------------------------------------------------------------------------------------------------------------


def various_terms():
    """
    По данному числу 1 <= n <= 10^9 найдите максимальное число k, для которого n можно
    представить как сумму k различных(не повторяющихся) натуральных слагаемых. Выведите в первой строке число k,
    во второй — k слагаемых.
    :return:
    """
    n = int(input())
    assert n > 0
    k = 2
    out_str = [1]
    sum_num = 1
    run = True
    if n <= 2:
        print('{}\n{}'.format(1, n))
    else:
        while run:
            if n - sum_num > k * 2:
                out_str.append(k)
                sum_num += k
                k += 1
            else:
                out_str.append(n - sum_num)
                print(k)
                print(*out_str)
                run = False




# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 2
# 1 3
# Sample Input 2:
#
# 6
# Sample Output 2:
#
# 3
# 1 2 3
#---------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # segments_covered_with_dots()
    # continuous_backpack()
    various_terms()
