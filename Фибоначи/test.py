from matplotlib import pyplot as plt
from alg_utils import timed
from Фибоначи.fib import fib, iter_fib


def compare(fs, args):
    """
    Сравнение времени выполнения нескольки функций
    :param fs: Список функций
    :param args: список аргументов
    """
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


compare([fib, iter_fib], list(range(20)))

