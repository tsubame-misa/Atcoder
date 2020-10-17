import math
n = int(input())
a = list(map(int, input().split()))
ma = 0
yu = 0
che = []

for i in range(n):
    ma += abs(a[i])
    yu += pow(abs(a[i]), 2)
    che.append(abs(a[i]))

yu = math.sqrt(yu)
c = max(che)
print(ma)
print(yu)
print(c)
