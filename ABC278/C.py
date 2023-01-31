# TLE followが10^9^2になるから？
# n, q = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(q)]
# follow = [[0 for i in range(q+1)] for j in range(q+1)]

# for i in range(q):
#     if data[i][0] == 1:
#         follow[data[i][1]][data[i][2]] = 1
#     elif data[i][0] == 2:
#         follow[data[i][1]][data[i][2]] = 0
#     else:
#         mutual_follow = follow[data[i][1]][data[i]
#                                            [2]] and follow[data[i][2]][data[i][1]]
#         if mutual_follow:
#             print("Yes")
#         else:
#             print("No")

n, q = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(q)]
# 入力として与えられる可能性のある順序対は N(N−1) 通りありますが、集合 S のサイズは全体を通してたかだか Q
follow = set()

for i in range(q):
    if data[i][0] == 1:
        follow.add((data[i][1], data[i][2]))
    elif data[i][0] == 2:
        follow.discard((data[i][1], data[i][2]))
    else:
        mutual_follow = (data[i][1], data[i][2]) in follow and (
            data[i][2], data[i][1]) in follow
        if mutual_follow:
            print("Yes")
        else:
            print("No")
