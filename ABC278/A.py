n, k = list(map(int, input().split()))
a = list(map(str, input().split()))

ans = a[k:]
for i in range(k):
    ans.append("0")

if k <= n:
    print(' '.join(ans))
else:
    print(' '.join(ans[:n]))
