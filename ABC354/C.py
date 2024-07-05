N = int(input())
data = [list(map(int, input().split())) + [(i + 1)] for i in range(N)]
# print(data)
sorted_data = sorted(data, key=lambda x: int(x[1]))

ans = []
max_level = 0

for i in range(N):
    if sorted_data[i][0] > max_level:
        ans.append(sorted_data[i][2])
        max_level = sorted_data[i][0]

print(len(ans))
sorted_ans = sorted(ans)
# print(sorted_ans)
print(" ".join([str(s) for s in sorted_ans]))
