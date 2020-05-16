import heapq
n = int(input())
# query = [list(map(int, input().split())) for i in range(n)]
day = [[] for i in range(n)]
for i in range(n):
    a, b = list(map(int, input().split()))
    day[a-1].append(b)

data = []
heapq.heapify(data)
a = 0
for i in range(n):
    for j in range(len(day[i])):
        heapq.heappush(data, day[i][j]*-1)
    a += heapq.heappop(data)*-1
    print(a)
    # print(data)
