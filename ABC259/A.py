n, m, x, t, d = list(map(int, input().split()))

if m >= x and m <= n:
    print(t)
    exit()

start = t-(x)*d
print(start+m*d)
