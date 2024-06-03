x = int(input())

_max = 1
for b in range(1, x+1):
    for p in range(2, x+1):
        bp = pow(b, p)
        if bp <= x and bp > _max:
            _max = bp
        elif bp > x:
            break
print(_max)
