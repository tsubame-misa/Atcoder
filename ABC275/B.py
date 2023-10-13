A, B, C, D, E, F = list(map(int, input().split()))
mod = 998244353

A %= mod
B %= mod
C %= mod
D %= mod
E %= mod
F %= mod

print(((A*B*C) % mod - (D*E*F) % mod) % mod)
