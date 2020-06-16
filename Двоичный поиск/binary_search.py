# В первой строке даны целое число 1 <= n <= 10^5 и массив A[1…n] из n различных натуральных чисел,
# не превышающих 10^9, в порядке возрастания, во второй — целое число 1 <= k <= 10^5
# и k натуральных чисел b_1,..., b_k, не превышающих 10^9. Для каждого i от 1 до k необходимо
# вывести индекс 1 <= j <= n, для которого A[j]=b_i, или -1, если такого j нет.

def binary_search(lst, el, index_one=False):
    """
    ВЫводит индекс найденного элемента, или -1 , если элемент не найден.
    :param lst: список для поиска
    :param el: элемент который надо искать
    :param index_one: True, если отсчёт начинается с единицы, а не с нуля.
    :return: индекс найденного эл. или -1, если такого нет.
    """
    l, r = 0, len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] == el:
            return m if index_one else m+1
        elif A[m] > el:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    n, *A = map(int, input().split())
    k, *B = map(int, input().split())
    result = []
    i = 0
    while i < k:
        result.append(binary_search(A, B[i]))
        i += 1
    print(*result)

    # 5 1 5 8 12 13
    # 5 8 1 23 1 11