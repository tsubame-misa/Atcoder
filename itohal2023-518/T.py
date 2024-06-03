from collections import deque

# 地図の作成
# bfsでゴールまでいけるか探索


# nl = lines[0].split()
# n = int(inpu)
# l = int(nl[1])

n, l = list(map(int, input().split()))
lines = [list(map(int, input().split())) for i in range(n)]

_map = [[0]*(l+2) for i in range(l+2)]
print(_map)
print()


def bfs(_map):
    map_len = len(_map)
    d = [[float("inf")] * len(_map) for i in range(len(_map))]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    sx = 0
    sy = 0
    gx = len(_map)-1
    gy = len(_map)-1

    que = []
    que.append((sx, sy))
    d[sx][sy] = 0

    # BFS本体 キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.pop()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx and p[1] == gy:
            break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を (nx, ny) とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != inf なら訪れたことがある
            if 0 <= nx < map_len and 0 <= ny < map_len and _map[nx][ny] == 0 and d[nx][ny] == float("inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]


for i in range(n):
    # data = list(map(int, lines[i].split()))
    data = lines[i]

    if data[0] == data[2]:
        y_min = min(data[1], data[3])
        y_max = max(data[1], data[3])
        if y_min == 0:
            _map[0][data[0]] = 8
        if y_max == l:
            _map[l+1][data[0]] = 8
        for j in range(y_min+1, y_max+1):
            _map[j][data[0]] = 8
    else:
        x_min = min(data[0], data[2])
        x_max = max(data[0], data[2])
        if x_min == 0:
            _map[data[1]][0] = 8
        if x_max == l:
            _map[data[1]][l+1] = 8
        for j in range(x_min+1, x_max+1):
            _map[data[1]][j] = 8

    print("i", i+1, data)

    for j in range(len(_map)):
        print(_map[j])

    print(bfs(_map))

    if bfs(_map) == float("inf"):
        print("NO")
        print(i+1)
        exit()

    print("-------------------")

    # print(_map)
    # print("d[gx][gy]", bfs(_map))
    # print("--------------------")
