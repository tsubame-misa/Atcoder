from collections import deque
import sys
sys.setrecursionlimit(2000000)

n, X, Y = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(n)]
glit = [["."]*400 for i in range(400)]

sx = 199
sy = 199
gx = X+200-1
gy = Y+200-1
glit[sy][sx] = 0
glit[gy][gx] = "g"

for a, b in xy:
    glit[b+200-1][a+200-1] = "#"

d = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1]]
q = deque()
q.append([sy, sx])
while q:
    y, x = q.popleft()
    for i in range(6):
        ny, nx = y+d[i][0], x+d[i][1]
        """
        for i in range(190, 210):
            for j in range(190, 210):
                print(glit[i][j], end="")
            print()
        print()
        """

        if glit[ny][nx] == "." and 0 <= ny and ny < 400 and 0 <= nx and nx <= 400:
            glit[ny][nx] = glit[y][x]+1
            q.append([ny, nx])
            # print(glit[ny][nx])
        elif glit[ny][nx] == "g":
            print(glit[y][x]+1)

            for i in range(190, 210):
                for j in range(190, 210):
                    print(glit[i][j], end="")
                print()

            exit()
print(-1)
