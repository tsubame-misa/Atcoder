import math
a, b, d = list(map(int, input().split()))

l = math.sqrt(a*a+b*b)
theta = math.atan2(b, a)
theta += math.radians(d)

_a = l*math.cos(theta)
_b = l*math.sin(theta)

print(_a, _b)
