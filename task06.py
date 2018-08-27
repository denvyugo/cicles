import random

MAX_TRY = 10
n = random.randint(0,100)
t = 1
while t <= MAX_TRY:
    m = int(input('угадайте число от 0 до 100? '))
    if m != n:
        t += 1
        if n < m:
            print('загаданное число меньше')
        else:
            print('загаданное число больше')
        if t > 10:
            print(f'число попыток превышено, не угадали {n}')
            break
    else:
        print(f'угадали за {t} попыток!')
        break
