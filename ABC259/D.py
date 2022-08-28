import math
n = int(input())
sx, sy, tx, ty = list(map(int, input().split()))
circles = [list(map(int, input().split()))for i in range(n)]

path = [[0]*n for i in range(n)]
start = -1
goal = -1

for i in range(n):
    for j in range(n):
        d = (circles[i][0]-circles[j][0])*(circles[i][0]-circles[j][0]) + \
            (circles[i][1]-circles[j][1]) * (circles[i][1]-circles[j][1])
        if (circles[i][2]-circles[j][2])*(circles[i][2]-circles[j][2]) <= d and d <= (circles[i][2]+circles[j][2])*(circles[i][2]+circles[j][2]):
            path[i][j] = 1
    sd = (sx-circles[i][0])*(sx-circles[i][0]) + \
        (sy-circles[i][1])*(sy-circles[i][1])
    gd = (tx-circles[i][0])*(tx-circles[i][0]) + \
        (ty-circles[i][1])*(ty-circles[i][1])
    if sd == circles[i][2]*circles[i][2]:
        start = i
    if gd == circles[i][2]*circles[i][2]:
        goal = i


visited = [0]*n
visited[start] = 1
stack = [start]
while stack:
    x = stack.pop()
    for i in range(n):
        if path[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            stack.append(i)
    if visited[goal] == 1:
        print("Yes")
        exit()

print("No")
