import time


def timed(f, *args, n_iter=100):
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
