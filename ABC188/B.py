n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0
for i in range(n):
    total += a[i]*b[i]
if total == 0:
    print("Yes")
else:
    print("No")
