h, w = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(h)]
_min = 1000
for i in range(h):
    _min = min(_min, min(data[i]))

total = 0
for i in range(h):
    for j in range(w):
        total += data[i][j]-_min

print(total)
