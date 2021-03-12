n, s, d = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]
count = 0
for x, y in data:
    if x >= s or y <= d:
        count += 1
if count < n:
    print("Yes")
else:
    print("No")
