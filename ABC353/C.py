N = int(input())
A = list(map(int, input().split()))

all_sum = sum(A)
sorted_A = sorted(A)
mod = pow(10, 8)

over_num = 0
r = N - 1
for i in range(N):
    r = max(r, i)
    # print("ir", i, r)
    while r > i and sorted_A[i] + sorted_A[r] >= mod:
        # print("r", r)
        r -= 1
    over_num += N - 1 - r
    # print("over_num", over_num)


print(all_sum * (N - 1) - over_num * mod)
