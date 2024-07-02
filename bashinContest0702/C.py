N, M = list(map(int, input().split()))
PY = [list(map(int, input().split())) for i in range(M)]

for i in range(M):
    PY[i].append(i)

sorted_PY = sorted(PY, key=lambda x: x[1])
p_cnt = [0 for i in range(N)]

for i in range(M):
    p = sorted_PY[i][0]
    idx = p_cnt[p - 1]
    id = str(p).zfill(6) + str(idx + 1).zfill(6)
    sorted_PY[i].append(id)
    p_cnt[p - 1] += 1


sorted_PY = sorted(PY, key=lambda x: x[2])
for i in range(M):
    print(sorted_PY[i][3])
