n, w = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]

sorted_data = sorted(data, key=lambda x: x[0], reverse=True)

total_w = 0
total_d = 0

for i in range(n):
    if w-total_w >= sorted_data[i][1]:
        total_w += sorted_data[i][1]
        total_d += sorted_data[i][0]*sorted_data[i][1]
    else:
        total_d += sorted_data[i][0]*(w-total_w)
        total_w += (w-total_w)

print(total_d)
