N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


sorted_A = sorted(A)
l = N - K - 1
diff = []

for i in range(N - l):
    # print(i, i + l, sorted_A[i + l], sorted_A[i])
    diff.append(sorted_A[i + l] - sorted_A[i])


# print(diff)
print(min(diff))
