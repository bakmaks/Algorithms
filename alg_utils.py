from matplotlib import pyplot as plt
import time


def timed(f, *args, n_iter=30):
    """
    Измеряет минимальное время выполнения функции f из n_iter вызовов.
    :param f: передаваемая функция
    :param args: список параметров f
    :param n_iter: кол-во вызовов
    :return: время выполнения
    """
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1-t0)
    return acc


def compare(fs, args, number_of_lists=1):
    """
    Графическое сравнение времени выполнения нескольких функций.
    :param fs: Список функций
    :param args: список аргументов
    :param number_of_lists: Количество списков в args
    """
    for f in fs:
        if number_of_lists == 1:
            plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        else:
            plt.plot([x for x in range(number_of_lists)],
                     [timed(f, arg) for arg in args],
                     label=f.__name__
                     )
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # list_of_args = [[x for x in range(10)] for x in range(3)]
    f = 'function'
    compare(f, 1)