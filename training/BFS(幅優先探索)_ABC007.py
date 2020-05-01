from collections import deque
import sys
sys.setrecursionlimit(2000000)

h, w = list(map(int, input().split()))
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [[j for j in input()] for i in range(h)]

c[gy-1][gx-1] = 'g'  # 大事
count = [[-1]*w for i in range(h)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
count[sy-1][sx-1] = 0  # 初期ノード
q = deque()
q.append([sy-1, sx-1])
while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y+d[i][0], x+d[i][1]
        if count[ny][nx] == -1 and 0 <= ny and ny < h and 0 <= nx and nx < w and c[ny][nx] == ".":
            count[ny][nx] = count[y][x] + 1
            q.append([ny, nx])
        elif ny == gy-1 and nx == gx-1:
            print(count[y][x]+1)
            exit()

print(0)
