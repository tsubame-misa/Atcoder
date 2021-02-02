import itertools
n, k = list(map(int, input().split()))
T = [list(map(int, input().split())) for i in range(n)]
count = 0
for v in itertools.permutations([i for i in range(1, n)], n-1):
    total = T[0][v[0]]
    pre = v[0]
    for i in range(n-1):
        total += T[pre][v[i]]
        pre = v[i]
    total += T[pre][0]
    if total == k:
        count += 1

print(count)
