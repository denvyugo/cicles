n = input('введите натуральное число: ')
d = input('введите цифру: ')
e = 0
for c in n:
    if c == d:
        e += 1

print(f'количество цифр {d} в числе {n}: {e} шт.')