from matplotlib import pyplot as plt
from alg_utils import timed
from Фибоначи.fib import fib, iter_fib


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


def x_eq_y(n):
    return n


compare([fib, iter_fib], list(range(20)))

