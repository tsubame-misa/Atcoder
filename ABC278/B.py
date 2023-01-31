h, m = list(map(int, input().split()))


def start_min(_h):
    if h == _h:
        return m
    return 0


def end_min(_h):
    if h == _h:
        return m
    return 60


for _h in range(h, 24):
    start_m = start_min(_h)
    for _m in range(start_m, 60):
        a = str(_h//10)
        b = str(_h % 10)
        c = str(_m//10)
        d = str(_m % 10)
        ac = a+c
        bd = b+d
        if int(ac) < 24 and int(bd) < 60:
            print(_h, _m)
            exit()
print(0, 0)
