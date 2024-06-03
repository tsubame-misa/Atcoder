
import collections
import itertools

H, W, N, h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
num_cnt = collections.Counter(list(itertools.chain.from_iterable(A)))

# 見るグリットを固定すれば3乗で間に合うらしい

for i in range(H-h+1):
    for j in range(W-w+1):
        k = i
        black_num = []
        for h_i in range(k, k+h):
            l = j
            black_num.append(A[h_i][w_i])
        black_num_cnt = collections.Counter(black_num)

        ans = 0
        for p in range(N):
            if num_cnt[p+1] > black_num_cnt[p+1]:
                ans += 1
        print(ans, end=" ")
    print()

"""
# 幇助原理
# 縦横トータル - 列のいらない部分 - 行のいらない部分 + 左上のいらない部分を2回引いてるから足さないといけない


H, W, N, h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
count = [[[0]*(N+1) for i in range(W+1)] for j in range(H+1)]

# 初期状態
for i in range(1, H+1):
    for j in range(1, W+1):
        count[i][j][A[i-1][j-1]-1] = 1

# 累積
for i in range(1, H+1):
    for j in range(1, W+1):
        for k in range(N+1):
            count[i][j][k] += count[i-1][j][k] + \
                count[i][j-1][k] - count[i-1][j-1][k]

for i in range(H-h+1):
    for j in range(W-w+1):
        ans = 0
        for k in range(N+1):
            if count[H][W][k] - (count[i+h][j+w][k] - count[i][j+w][k] - count[i+h][j][k] + count[i][j][k]):
                ans += 1
        print(ans, end=" ")
    print()

"""
