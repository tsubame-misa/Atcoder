n, k = list(map(int, input().split()))
# r = list(map(int, input().split()))
total = 0
if n >= k:
    total += (1/n)*(n-k+1)
# print(total)

for i in range(min(n, k-1)):
    count = 0
    b = i+1
    while k > b:
        b *= 2
        count += 1
    # print(count)
    a = 1/(n*pow(2, count))
    total += a

print(total)
