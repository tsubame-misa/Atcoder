n = int(input())
XY = [list(map(int, input().split())) for i in range(n)]

w = 1005

map = [[0 for i in range(-w, w)] for i in range(-w, w)]

for x, y in XY:
    map[x + w][y + w] = 1


G = [[[] for i in range(-w, w)] for i in range(-w, w)]

for x, y in XY:
    x += w
    y += w
    if map[x - 1][y - 1] == 1:
        G[x][y].append([x - 1, y - 1])
    if map[x - 1][y] == 1:
        G[x][y].append([x - 1, y])
    if map[x][y - 1] == 1:
        G[x][y].append([x, y - 1])
    if map[x][y + 1] == 1:
        G[x][y].append([x, y + 1])
    if map[x + 1][y] == 1:
        G[x][y].append([x + 1, y])
    if map[x + 1][y + 1] == 1:
        G[x][y].append([x + 1, y + 1])


visited = [[0 for i in range(-w, w)] for i in range(-w, w)]
visited_node = []
stack = []
cnt = 0
for xy in XY:
    x = xy[0]
    y = xy[1]
    if not (xy in visited_node):
        stack = [xy]
        visited[x][y] = 1
        cnt += 1
    while stack:
        px, py = stack.pop()
        px += w
        py += w
        for cxw, cyw in G[px][py]:
            cx = cxw - w
            cy = cyw - w
            if not visited[cxw][cyw]:
                stack.append([cx, cy])
                visited[cxw][cyw] = 1
                visited_node.append([cx, cy])

# print(visited)
print(cnt)
