x, y, a, b = list(map(int, input().split()))
cnt = 0
while x*a < x+b and a*x <= y:
    x *= a
    cnt += 1
c2 = (y-x-1)//b
print(cnt+c2)
