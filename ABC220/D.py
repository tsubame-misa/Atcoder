# dpなのはわかった
n = int(input())
a = list(map(int, input().split()))

# A[i]まで処理が終わった時の配列の先頭の値がjなら1
dp = [[0 for i in range(10)] for j in range(n)]
dp[0][a[0]] = 1
mod = 998244353

# jを見れば配列を足して変化させなくてもわかる
for i in range(n-1):
    for j in range(10):
        d = dp[i][j] % mod
        dp[i+1][(j+a[i+1]) % 10] += d
        dp[i+1][j*a[i+1] % 10] += d

for ans in dp[-1]:
    print(ans % mod)
