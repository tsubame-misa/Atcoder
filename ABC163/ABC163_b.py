n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
total = sum(a)

if n-total >= 0:
    print(n-total)
else:
    print(-1)
