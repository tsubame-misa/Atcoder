n, t = list(map(int, input().split()))
s = input()
X = list(map(int, input().split()))

A = sorted([X[i] for i in range(n) if s[i] == "1"])
B = sorted([X[i] for i in range(n) if s[i] == "0"])


print(A)
print(B)

ans = 0
l, r = 0, 0
for i in range(len(A)):
    # Bi は A よりも大きい必要がある
    while l < len(B) and A[i] > B[l]:
        l += 1
    # B[i] - A <= t*2 であればすれ違う
    while r < len(B) and B[r] - A[i] <= t * 2:
        r += 1
    print(r - l, l, r)
    ans += r - l

print(ans)
