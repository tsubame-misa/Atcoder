import itertools
n = int(input())
A = list(map(int, input().split()))
A.sort()
ruiseki = list(itertools.accumulate(A))
_sum = sum(A)
total = 0
for i in range(n):
    total += _sum-ruiseki[i]-(n-i-1)*A[i]
print(total)
