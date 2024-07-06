N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
zanseki = K
i = 0
while i < N:
    if zanseki >= A[i]:
        zanseki -= A[i]
        i += 1
    else:
        ans += 1
        zanseki = K

if zanseki != K:
    ans += 1

print(ans)
