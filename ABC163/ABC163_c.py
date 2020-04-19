n = int(input())
#n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
count = [0]*n
for i in range(n-1):
    count[a[i]-1] += 1

for i in range(n):
    print(count[i])
