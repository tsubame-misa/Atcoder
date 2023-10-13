from collections import defaultdict, deque

n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

d = defaultdict(list)

for a, b in p:
    d[a].append(b)
    d[b].append(a)


# bfs
q = [1]
visited = {1}
while len(q) > 0:
    v = q.pop()
    for i in d[v]:
        if not i in visited:
            visited.add(i)
            q.append(i)

print(max(visited))
