N, M = list(map(int, input().split()))
S = [input() for i in range(N)]

# bit全探索
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
