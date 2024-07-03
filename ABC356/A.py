n, l, r = list(map(int, input().split()))

s = [i + 1 for i in range(n)]
sorted_s = sorted(s[l - 1 : r], reverse=True)

ans = [str(a) for a in s[: l - 1] + sorted_s + s[r:]]
print(" ".join(ans))
