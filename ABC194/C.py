n = int(input())
a = list(map(int, input().split()))
s = 0
s2 = 0
for i in range(n):
    s += a[i]**2
    s2 += a[i]
ans = n*s - s2**2
print(ans)
