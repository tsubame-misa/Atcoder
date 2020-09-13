n = int(input())


def calc_eight(n):
    ans = 1
    mod = 10**9 + 7
    for i in range(n):
        ans *= 8
        ans %= mod
    return ans


def calc_ten(n):
    ans = 1
    mod = 10**9 + 7
    for i in range(n):
        ans *= 10
        ans %= mod
    return ans


def calc_nine(n):
    ans = 1
    mod = 10**9 + 7
    for i in range(n):
        ans *= 9
        ans %= mod
    return ans


if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    mod = 10**9 + 7
    _all = calc_ten(n)
    _all %= mod
    other = calc_eight(n)
    other %= mod
    nine = calc_nine(n)
    nine %= mod
    ans = _all-(nine*2-other)
    ans %= mod
    print(ans)
