
# def segments_covered_with_dots():
#     """
#     Необходимо найти множество точек, для которого каждый из отрезков
#     содержит хотя бы одну из точек(не обязательно точка должна лежать на каждом отрезке сразу)
#     и размер множества был бы минимальным.
#
#     :return:
#     """
#     print('Введите кол-во строк:')
#     seg_numbers = int(input())
#     seg_dict = {}
#     seg_list = []
#     print('Введите отрезок:')
#     for i in range(seg_numbers):
#         key = tuple(map(int, input().split(' ')))
#         seg_dict[key] = False                       # Если ещё не просматривали отрезок
#         seg_list.append(key)                        # Список отрезков
#     seg_list.sort(key=lambda x: x[1])               # сортировка по второму элементу пары
#     dots = set()
#     for segment in seg_list:                        # Выбираем отрезок
#         if seg_dict[segment] is False:
#             for key in seg_dict:
#                 # Если правая точка, выбранного отрезка,
#                 # попадает на отрезок из словаря
#                 if key[0] <= segment[1] <= key[1]:
#                     dots.add(segment[1])        # точка заносится в множество
#                     seg_dict[key] = True        # данный отрезок просмотрен и на нём есть точка
#     print(len(dots))
#     print(' '.join(list(map(str, dots))))
#
#
# segments_covered_with_dots()


def b():
    segments = sorted([sorted(map(int, input().split())) for i in range(int(input()))], key=lambda x: x[1])
    dots = [segments.pop(0)[1]]
    for l, r in segments:
        if l > dots[-1]:
            dots.append(r)
    print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))

b()