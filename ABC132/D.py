from fractions import gcd
import itertools
import collections

n, k = list(map(int, input().split()))

M = 1000000007
f = [1]
g = [1]
for i in range(1, 2*n+1):
    f.append(i*f[i-1] % M)  # 階乗
    g.append(pow(f[i], -1, M))  # f[i]の逆元

for i in range(1, k+1):
    if n-k < i-1:
        print(0)
    else:
        a_com = f[n-k+1]*g[i] % M*g[n-k+1-i] % M
        b_com = f[k-1]*g[i-1] % M*g[k-i] % M
        print(a_com*b_com % M)
