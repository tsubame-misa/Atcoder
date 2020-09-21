n = int(input())
cnt = 0
for i in range(1, n):
    a = (n-1)//i
    cnt += a

print(cnt)
