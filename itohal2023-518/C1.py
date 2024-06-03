import itertools

n = int(input())
point = [list(map(int, input().split())) for i in range(n)]

point_comb = itertools.combinations(point, 3)

cnt = 0
for pc in point_comb:
    s = (pc[1][0]-pc[0][0])*(pc[2][1]-pc[0][1]) - \
        (pc[2][0]-pc[0][0])*(pc[1][1]-pc[0][1])
    if s != 0:
        cnt += 1

print(cnt)
