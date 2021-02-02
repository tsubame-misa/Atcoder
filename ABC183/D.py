n, w = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]
l = 10**5*2+1
alls = [0]*l
for i in range(n):
    alls[data[i][0]] += data[i][2]
    alls[data[i][1]] -= data[i][2]

ruiseki = [0]
for i in range(l):
    a = ruiseki[i]+alls[i]
    if a > w:
        print("No")
        exit()
    ruiseki.append(a)
print("Yes")