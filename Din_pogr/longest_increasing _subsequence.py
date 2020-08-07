def LIS(A: list, n: int):
    """
    Дано целое число 1 ≤ n ≤ 10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9.
    Выведите максимальное 1 ≤ k ≤ n, для которого найдётся подпоследовательность 1 ≤ i1 < i2 < … < ik ≤ n
    длины k, в которой каждый элемент делится на предыдущий (формально: для  всех 1 ≤ j < k,
    A[i_j]|A[i_{j+1}]).

    Пример:
    вход: [3 6 7 12]
    ответ: 3

    :param A: Список
    :param n: Длина списка
    """
    ans = 0
    d = [0] * n
    for i in range(n):
        d[i] = 1
        for j in range(0, i-1):
            if A[j] < A[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    for i in range(n):
        print(max(ans, d[i]), end=' ')


if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    LIS(x, n)
