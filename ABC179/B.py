n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(1, n-1):
    if data[i][0] == data[i][1] and data[i-1][0] == data[i-1][1] and data[i+1][0] == data[i+1][1]:
        print("Yes")
        exit()

print("No")
