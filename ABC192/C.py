n, k = list(map(int, input().split()))
if k == 0:
    print(n)
else:
    for i in range(k):
        n = list(str(n))
        a = sorted(n)
        a = ''.join(a)
        b = sorted(n, reverse=True)
        b = ''.join(b)
        n = int(b)-int(a)
    print(n)
