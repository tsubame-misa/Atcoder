n, m, x = list(map(int, input().split()))

a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)


def calcPoint(point, n):
    for i in range(m):
        point[i] += a[n][i+1]
    return point


def judgePoint(point):
    for i in range(m):
        if point[i] < x:
            return False
    return True


ans = []
for i in range(2**n):  # patarn数
    buy = []
    for j in range(n):  # n bit
        if((i >> j) & 1):  # iをj bit 右にずらして1ならば
            buy.append(1)
        else:
            buy.append(0)
    price = 0
    point = [0]*m
    for i in range(n):
        if buy[i] == 1:
            calcPoint(point, i)
            price += a[i][0]
    if judgePoint(point):
        ans.append(price)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
