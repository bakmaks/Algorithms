def huffman_coding(s):  # s = 'abacabad'
    """
    По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
    постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
    встречающихся в строке, и размер получившейся закодированной строки. В следующих k строках
    запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.
    :param s: str строка которую надо закодировать.
    :return: codes - словарь с символами и их кодами, encode_str - закодированная строка
    """
    if s == '' or s is None:
        print('0:', '0')
        return {'0': '0'}, ''
    codes = {}  # Словарь кодов символов {'символ': 'код'}

    def tree_walk(tree, code=''):
        """
        Совершается рекурсивный обход двоичного дерева в глубину. Если заход в первую ветку в code
        добавляется ноль, если во вторую - добавляется единица. В итоге, когда доходит до листа,
        в codes добавляется пара 'символ: код_символа'.
        :param tree: Двоичное дерево, состоящее из массивов.
        :param code: Строка содержащая код символа.
        """
        len_tree = len(tree)
        if len_tree == 3:  # Если это ветка
            tree_walk(tree[-2], code + '0')  # Заход на первую ветку
            tree_walk(tree[-3], code + '1')  # Заход на вторую ветку
        else:  # Если это лист
            codes[tree[0]] = code  # Добавление пары 'символ: код'

    def search_prev(f, lst_with_frq):
        """
        Возвращает индекс после которого надо вставлять новый элемент.
        :param f: int частота символа или сумма частот двух символов
        :param lst_with_frq: list  список символов с частотами вхождения символов
        :return: int индекс
        """
        k = 0
        while k < len(lst_with_frq):
            if lst_with_frq[k][-1] < f:
                k += 1
            else:
                return k
        return k

    frequency_of_occurrence = {}
    # Подсчёт кол-ва вхождений символов в строку
    for letter in s:
        if letter in frequency_of_occurrence:
            frequency_of_occurrence[letter] += 1
        else:
            frequency_of_occurrence[letter] = 1

    lst = []
    # Получаем начальное состояние списка. Каждый элемент списка состоит из списка, где нулевой эл.
    # это символ, а первый - частота вхождения символа в строку.
    for key in frequency_of_occurrence:
        lst.append([key, frequency_of_occurrence[key]])

    len_lst = len(lst)
    if len_lst <= 1:
        codes = {lst[0][0]: '0'}
    else:
        # Сортировка списка по частоте вхождений
        lst.sort(key=lambda x: x[1])  # lst = [['c', 1], ['d', 1], ['b', 2], ['a', 4]]
        # print(s)

        # Составление двоичного дерева
        while len(lst) > 1:
            # Из списка извлекаются два первых элемента с минимальными частотами.
            # Из них формируется ветка(список), вершина которой, это сумма частот предыдущих
            # двух элементов.
            l_leaf, r_leaf = lst.pop(0), lst.pop(0)
            frq = l_leaf[-1] + r_leaf[-1]
            # Получившийся элемент вставляется в отсортированный список, не нарушая сортировки.
            lst.insert(search_prev(frq, lst), [l_leaf, r_leaf, frq])

        tree_walk(lst[-1])
    # Формирование выходных данных

    l_keys = list(codes.keys())

    encode_str = ''
    for ch in s:
        encode_str += codes[ch]

    print(len_lst, len(encode_str))
    [print(x, codes[x], sep=': ') for x in sorted(l_keys)]
    print(encode_str)
    return codes, encode_str


def decode_encoded_str(some_codes: dict, some_encoded_str: str):
    reversed_codes = {value: key for key, value in some_codes.items()}
    decoded_str, acc = '', ''
    for ch in some_encoded_str:
        acc += ch
        if acc in reversed_codes:
            decoded_str += reversed_codes[acc]
            acc = ''
    print(decoded_str)


if __name__ == '__main__':
    str_list = ['', 'a', 'ddd', 'abacabad', 'beep boop beer!', 'accepted']
    encoded_dict, encoded_str = huffman_coding(str_list[5])
    decode_encoded_str(encoded_dict, encoded_str)