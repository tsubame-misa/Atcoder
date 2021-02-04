n, m, t = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(m)]
p = n
pre = 0
for i in range(m):
    p -= data[i][0]-pre
    if p <= 0:
        print("No")
        exit()
    p += data[i][1]-data[i][0]
    if p >= n:
        p = n
    pre = data[i][1]

p -= t-pre
if p <= 0:
    print("No")
else:
    print("Yes")
