x = int(input())
#n, m = list(map(int, input().split()))
#a, b = list(map(int, input().split()))
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
money = 100
year = 0
while money < x:
    money *= 1.01
    money = money//1
    year += 1

print(year)
