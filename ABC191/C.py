h, w = list(map(int, input().split()))
data = [input() for i in range(h)]
ans = 0
for i in range(h-1):
    for j in range(w-1):
        count = 0
        if data[i][j] == "#":
            count += 1
        if data[i+1][j] == "#":
            count += 1
        if data[i+1][j+1] == "#":
            count += 1
        if data[i][j+1] == "#":
            count += 1
        if count == 1 or count == 3:
            ans += 1
print(ans)
