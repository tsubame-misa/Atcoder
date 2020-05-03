n, m, q = list(map(int, input().split()))
abcd = []
for i in range(q):
    x, y, z, k = [int(j) for j in input().split()]
    abcd.append([x, y, z, k])

s = [0]*n
ans = 0


def dfs(s, num, i):
    if i == n:
        global ans
        total = 0
        for j in range(q):
            if s[abcd[j][1]-1]-s[abcd[j][0]-1] == abcd[j][2]:
                total += abcd[j][3]
        ans = max(ans, total)
        return
    else:
        # s[0]が1~mまで　s[1]が~mまで　全部調べる準備
        for j in range(num, m+1):
            s[i] = j
            # 次のs[]の最小値はj
            dfs(s, j, i+1)


dfs(s, 1, 0)
print(ans)
