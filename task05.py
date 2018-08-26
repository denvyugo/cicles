SYMBOL1 = 32
SYMBOL2 = 127
s = SYMBOL1
while s <= SYMBOL2:
    l = ''
    for _ in range(0,10):
        l = l + f'{s:5}-{chr(s)}'
        s += 1
        if s > SYMBOL2:
            break
    print(l)
