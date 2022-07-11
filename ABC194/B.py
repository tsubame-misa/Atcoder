n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if i != j:
            a = max(data[i][0], data[j][1])
        else:
            a = data[i][0]+data[j][1]
        ans.append(a)
print(min(ans))
