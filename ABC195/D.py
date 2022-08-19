n, m, q = list(map(int, input().split()))
wv = [list(map(int, input().split())) for i in range(n)]
x = list(map(int, input().split()))
query = [list(map(int, input().split())) for i in range(q)]

wv_sorted = sorted(wv, key=lambda x: (x[1], x[0]), reverse=True)

for i in range(q):
    ans = 0
    usable_xs = []
    for j in range(m):
        if not(query[i][0]-1 <= j and j <= query[i][1]-1):
            usable_xs.append([x[j], 0])
    usable_xs = sorted(usable_xs, key=lambda x: (x[0]))

    for j in range(n):
        for k in range(len(usable_xs)):
            if wv_sorted[j][0] <= usable_xs[k][0] and usable_xs[k][1] == 0:
                ans += wv_sorted[j][1]
                usable_xs[k][1] = 1
                break
    print(ans)
