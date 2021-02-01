n = int(input())
A = list(map(int, input().split()))

ans = 0
ruiseki = [0]
maxs = [0]
for i in range(n):
    a = ruiseki[i]+A[i]
    ruiseki.append(a)
    maxs.append(max(maxs[i], a))

point = 0
for i in range(1, n+1):
    ans = max(ans, point+maxs[i])
    point += ruiseki[i]

print(ans)
