def gcd(a: int, b: int):
    """
    Нахождение наибольшего общего делителя рекурсивно
    """
    return a if b == 0 else gcd(b, a % b)


a, b = 10, 4
print("НОД от ", a, b)
print(gcd(4,10))                   # 2
print()
a, b = 63967072, 14159572
print("НОД от ", a, b)
print(gcd(63967072, 14159572))      # 4
print()
a, b = 18, 35
print("НОД от ", a, b)
print(gcd(18, 35))                  # 1
