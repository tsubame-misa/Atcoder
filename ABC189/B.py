n, x = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]
total = 0
for i in range(n):
    total += data[i][0]*data[i][1]
    if total > x*100:
        print(i+1)
        exit()
print(-1)
