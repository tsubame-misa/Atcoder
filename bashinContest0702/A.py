n, l = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = 0
for a in A:
    if a >= l:
        cnt += 1

print(cnt)
