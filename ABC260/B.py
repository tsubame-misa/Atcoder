n, x, y, z = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

data = [[a[i], b[i], i+1] for i in range(n)]
ans = []

sorted_data = sorted(data, key=lambda x: (x[0], -1*x[2]), reverse=True)

for i in range(min(x, len(sorted_data))):
    ans.append(sorted_data[i][2])

sorted_data = sorted(sorted_data[x:], key=lambda x: (
    x[1], -1*x[2]), reverse=True)

for i in range(min(y, len(sorted_data))):
    ans.append(sorted_data[i][2])

sorted_data = sorted(sorted_data[y:], key=lambda x: (
    x[0]+x[1], -1*x[2]), reverse=True)

for i in range(min(z, len(sorted_data))):
    ans.append(sorted_data[i][2])


sorted_ans = sorted(ans)
for i in range(len(sorted_ans)):
    print(sorted_ans[i])
