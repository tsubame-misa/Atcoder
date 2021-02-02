sx, sy, gx, gy = list(map(int, input().split()))
a = (gy+sy)/(sx-gx)
b = sy - a*sx
x = -b/a
print(x)
