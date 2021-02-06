n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(i+1, n):
        a = (data[j][1]-data[i][1]) / (data[j][0]-data[i][0])
        if a >= -1 and a <= 1:
            count += 1
print(count)
