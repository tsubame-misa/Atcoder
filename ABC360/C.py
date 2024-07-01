n = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
box = [[] for i in range(n)]

for i in range(n):
    box[A[i] - 1].append(W[i])

ans = 0
for b in box:
    sorted_b = sorted(b)
    # print(sorted_b[:-1])
    ans += sum(sorted_b[:-1])
print(ans)
