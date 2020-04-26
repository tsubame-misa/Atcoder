a, b, c, d = list(map(int, input().split()))
#a = list(map(int, input().split()))
count = 0
while a > 0 and c > 0:
    if count % 2 == 0:
        c -= b
    else:
        a -= d
    count += 1

if a <= 0:
    print("No")
else:
    print("Yes")
