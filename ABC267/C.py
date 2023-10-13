N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

_max = -1*float("inf")

for i in range(N-M+1):
    total = 0

    for j in range(M):
        total += A[i+j]*(j+1)

    if total > _max:
        _max = total
