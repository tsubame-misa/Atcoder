N, M, K = list(map(int, input().split()))
C = []
A = []
R = []
for i in range(M):
    data = list(input().split())
    C.append(int(data[0]))
    R.append(data[-1])
    A.append(list(map(lambda x: int(x) - 1, data[1:-1])))

ans = 0

for bit in range(1 << N):
    flg = True
    for i in range(M):
        cnt = 0
        for j in range(C[i]):
            if (bit >> A[i][j]) & 1:
                cnt += 1
        if cnt >= K:
            if R[i] == "x":
                flg = False
        else:
            if R[i] == "o":
                flg = False
    if flg:
        ans += 1

print(ans)
