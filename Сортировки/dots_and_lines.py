import sys

reader = (map(int, line.split(' ')) for line in sys.stdin)
# print('Введите кол-во отреков и точек, через пробел:\n')
n, m = next(reader)
lines = []
for i in range(n):
    # print('Введите координаты отрезка, через пробел:\n')
    lines.append(tuple(next(reader)))
# print('Введите точки, через пробел:\n')
dots = list(next(reader))
print(lines)
print(dots)