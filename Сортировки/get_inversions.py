import sys


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

if __name__ == "__main__":
    reader = (map(int, line.split(' ')) for line in sys.stdin)
    a = list(next(reader))
    _, c = get_inversions_with_bubble_sort(a)
    print(c)