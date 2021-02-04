import math
n, m = list(map(int, input().split()))
if m == 0:
    print(1)
    exit()
A = list(map(int, input().split()))
A.sort()
p = [A[0]-1]
for i in range(m-1):
    p.append(A[i+1]-A[i]-1)
if A[-1] != n:
    p.append(n-A[-1])
if max(p) == 0:
    print(0)
else:
    p.sort()
    k = 0
    for i in range(len(p)):
        if p[i] != 0:
            k = p[i]
            break
    total = 0
    for i in range(len(p)):
        total += math.ceil(p[i]/k)
    print(total)
    print(p)
