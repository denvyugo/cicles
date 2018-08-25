n = int(input('введите число элементов последовательности: '))
SEQUENCE_COEFFICIENT = -0.5
e = 1
s = 0
for _ in range(0, n):
    s += e
    e = e * SEQUENCE_COEFFICIENT

print(f'сумма {n} элементов: {s}')