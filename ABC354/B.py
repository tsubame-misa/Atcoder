N = int(input())
data = [list(input().split()) for i in range(N)]
sorted_data = sorted(data, key=lambda x: x[0])

total = sum([int(d[1]) for d in data])
n = total % N

print(sorted_data[n][0])
