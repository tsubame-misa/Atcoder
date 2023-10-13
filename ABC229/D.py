s = input()
k = int(input())

# .がn個の区間の長さの最大値を求める

r = 0
ans = 0
count = 0
for l in range(len(s)):
    while(r < len(s)-1 and count <= k):
        # print("b", l, r, count)
        r += 1
        if s[r] == ".":
            count += 1

        # print(" ", l, r, count, ans)
    if count > k:
        # rが次に行っているので
        ans = max(ans, r-l-1)
    else:
        ans = max(ans, r-l)

    # print("m", l, r, count, ans)
    if l == r:
        r += 1
    if s[l] == ".":
        count -= 1

print(ans+1)

# 0123456789
# XX...X.X.X.
# 2
