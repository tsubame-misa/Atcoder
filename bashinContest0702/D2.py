import networkx as nx

n = int(input())
XY = [list(map(int, input().split())) for i in range(n)]

x_brack = [x for x, y in XY]
x_min = min(x_brack)
x_max = max(x_brack)
x_range = x_max - x_min + 3

y_brack = [y for x, y in XY]
y_min = min(y_brack)
y_max = max(y_brack)
y_range = y_max - y_min + 3

# print(x_min, x_max)
# print(y_min, y_max)
# print("range", x_range, y_range)


map = [[0 for i in range(y_min - 1, y_max + 2)] for i in range(x_min - 1, x_max + 2)]

# print(len(map), len(map[0]))

for x, y in XY:
    # print(
    #     x,
    #     y,
    #     x - x_min + 1,
    #     y - y_min + 1,
    # )
    map[x - x_min + 1][y - y_min + 1] = 1
    # map[x][y] = 1

# print(map)

G = [[[] for i in range(x_min - 1, x_max + 2)] for i in range(y_min - 1, y_max + 2)]

edge_list = []
node_list = []

for x, y in XY:
    i = x - x_min + 1
    j = y - y_min + 1

    print(i, j, i * y_range + j)
    node_list.append(i * y_range + j)

    if map[i - 1][j - 1] == 1:
        # G[i][j].append([i - 1, j - 1])
        edge_list.append([i * y_range + j, (i - 1) * y_range + (j - 1)])
    if map[i - 1][j] == 1:
        # G[i][j].append([i, j])
        edge_list.append([i * y_range + j, (i - 1) * y_range + (j)])
    if map[i][j - 1] == 1:
        # G[i][j].append([i, j])
        edge_list.append([i * y_range + j, (i) * y_range + (j - 1)])
    if map[i][j + 1] == 1:
        # G[i][j].append([i, j])
        edge_list.append([i * y_range + j, (i) * y_range + (j + 1)])
    if map[i + 1][j] == 1:
        # G[i][j].append([i, j])
        edge_list.append([i * y_range + j, (i + 1) * y_range + (j)])
    if map[i + 1][j + 1] == 1:
        # G[i][j].append([i, j])
        edge_list.append([i * y_range + j, (i + 1) * y_range + (j + 1)])

# print(edge_list)
# print(node_list)

# print(G)

# グラフ作成
G = nx.Graph()
G.add_edges_from(edge_list)
G.add_nodes_from(node_list)

connected = len([c for c in nx.connected_components(G)])

print(connected)
