import heapq
n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]
data = sorted(data, key=lambda x: (x[0], -x[1]))
for i in range(n):
    data[i][1] *= -1
idx = 0
q = []
ans = 0
heapq.heapify(q)
ans = 0
j = 0
for i in range(m):
    while j < len(data) and data[j][0] == i+1:
        heapq.heappush(q, data[j][1])
        j += 1
    if q:
        ans += heapq.heappop(q)*(-1)

print(ans)
