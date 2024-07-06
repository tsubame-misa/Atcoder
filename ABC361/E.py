N = int(input())
town_map = [[] for i in range(N)]

sum_dist = 0
for i in range(N - 1):
    data = list(map(int, input().split()))
    town_map[data[0] - 1].append([data[1] - 1, data[2]])
    town_map[data[1] - 1].append([data[0] - 1, data[2]])
    sum_dist += data[2] * 2

print(sum_dist)

# 隣接ノードが1だけの街
print(town_map)
one = sorted([m[0] for m in town_map if len(m) == 1], key=lambda x: x[1], reverse=True)

sum_dist -= one[0][1] * 2
sum_dist += one[0][1]

sum_dist -= one[1][1] * 2
sum_dist += one[1][1]

print(sum_dist)
