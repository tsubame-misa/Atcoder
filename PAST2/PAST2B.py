import collections
s = input()
a = collections.Counter(s)
ans = list(a.items())
ans_sorted = sorted(ans, key=lambda x: x[1], reverse=True)
print(ans_sorted[0][0])
