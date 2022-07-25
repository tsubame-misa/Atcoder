n, x = list(map(int, input().split()))
jump = [list(map(int, input().split()))for i in range(n)]

dp = [[0 for i in range(x+1)] for j in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(x):
        if dp[i][j] == 1:
            if j+jump[i][0] <= x:
                dp[i+1][j+jump[i][0]] = 1
            if j+jump[i][1] <= x:
                dp[i+1][j+jump[i][1]] = 1
    # print(dp)

if dp[n][x] == 1:
    print("Yes")
else:
    print("No")
