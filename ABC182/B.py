n = int(input())
A = list(map(int, input().split()))
ans = 0
ans_n = -1
for i in range(2, max(A)+1):
    # print(i)
    total = 0
    for a in A:
        if a % i == 0:
            total += 1
    if ans < total:
        ans = total
        ans_n = i

print(ans_n)
