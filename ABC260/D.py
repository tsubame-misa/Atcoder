import bisect

n, k = list(map(int, input().split()))
p = list(map(int, input().split()))


# count = [0]*(n+1)
# card = []


stage = {}
ans = [-1]*n

for i in range(n):
    x = p[i]
    # 二部探索
    keys = sorted(list(stage.keys()))
    over_x_min = bisect.bisect(keys, x)
    search_x = x
    # print("x", x, "i", i+1, over_x_min)
    # print(over_x_min, keys, x)
    if len(keys) > 0 and len(keys) > over_x_min and keys[over_x_min] > x:
        stage[keys[over_x_min]].append(x)

        if keys[over_x_min] > x:
            stage[x] = stage[keys[over_x_min]]
            # stage[keys[over_x_min]] = []
            stage.pop(keys[over_x_min])
        else:
            search_x = keys[over_x_min]

    else:
        stage[x] = [x]

    print(stage)

    if len(stage[search_x]) == k:
        # print(stage)
        for sc in stage[search_x]:
            ans[sc-1] = i+1
        # stage[search_x] = []
        stage.pop(search_x)


for a in ans:
    print(a)
