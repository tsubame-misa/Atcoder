n, m = list(map(int, input().split()))
s = []
for i in range(m):
    a = list(map(int, input().split()))
    s.append(a)
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    on = []
    for j in range(n):
        if((i >> j) & 1):
            on.append(1)
        else:
            on.append(0)
    count = 0
    for j in range(m):
        total = 0
        for k in range(s[j][0]):
            if on[s[j][k+1]-1] == 1:
                total += 1

        if total % 2 == p[j]:
            count += 1
    if count == m:
        ans += 1

print(ans)
