a, b, n = list(map(int, input().split()))

x = min(b-1, n)
ans = a*x//b - a*(x//b)

print(ans)
