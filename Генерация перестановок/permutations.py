def generate_number(N: int, M: int, prefix=None):
    """
    Генерирует все числа с лидирующими не значащими нулями.
    :param N:   основание системы счисления, N <= 10
    :param M:   длина числа
    :param prefix:  список перестановок
    :return:    выход при M == 0
    """
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


def generate_permutations(N: int, M: int=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом - prefix
    :param N:   основание системы счисления, N <= 10
    :param M:   длина числа
    :param prefix:  список перестановок
    :return:
    """
    M = N if M == -1 else M         # По умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()


# generate_number(3, 3)

generate_permutations(4)