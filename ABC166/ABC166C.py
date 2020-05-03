n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
ok = [0]*n
count = 0
check = [0]*n
for i in range(m):
    x, y = list(map(int, input().split()))
    if h[x-1] > h[y-1]:
        ok[x-1] += 1
    if h[y-1] > h[x-1]:
        ok[y-1] += 1
    check[x-1] += 1
    check[y-1] += 1

for i in range(n):
    if check[i] == ok[i]:
        count += 1

# print(ok)
# print(check)
print(count)
