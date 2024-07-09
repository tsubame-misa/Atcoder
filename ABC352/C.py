N = int(input())
data = [list(map(int, input().split())) for i in range(N)]

max_v = max([s[1] - s[0] for s in data])
print(max_v + sum([s[0] for s in data]))
