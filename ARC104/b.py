# pypy->OK  python->TLE
a, s = list(input().split())
n = int(a)
A = [0 for i in range(n+1)]
T = [0 for i in range(n+1)]
C = [0 for i in range(n+1)]
G = [0 for i in range(n+1)]

for i in range(1, n+1):

    if s[i-1] == "A":
        A[i] = A[i-1]+1
        T[i] = T[i-1]
        G[i] = G[i-1]
        C[i] = C[i-1]
    elif s[i-1] == "T":
        A[i] = A[i-1]
        T[i] = T[i-1]+1
        G[i] = G[i-1]
        C[i] = C[i-1]
    elif s[i-1] == "C":
        A[i] = A[i-1]
        T[i] = T[i-1]
        G[i] = G[i-1]
        C[i] = C[i-1]+1
    else:
        A[i] = A[i-1]
        T[i] = T[i-1]
        G[i] = G[i-1]+1
        C[i] = C[i-1]

cnt = 0
for i in range(1, n):
    for j in range(1, n-i+1):
        if A[j+i]-A[j-1] == T[j+i]-T[j-1] and G[j+i]-G[j-1] == C[j+i]-C[j-1]:
            cnt += 1

print(cnt)
