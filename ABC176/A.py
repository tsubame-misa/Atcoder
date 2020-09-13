import math
n, x, t = list(map(int, input().split()))
ans = t * (math.ceil(n/x))
print(ans)
