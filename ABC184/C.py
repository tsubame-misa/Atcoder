r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))

if r1 == r2 and c1 == c2:
    print(0)
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
    print(1)
else:
    if (r1+c1+r2+c2) % 2 == 0:
        print(2)
    elif abs(r1-r2)+abs(c1-c2) <= 6:
        print(2)
    elif abs(r1+c1-(r2+c2))<=3 or abs((r1-c1)-(r2-c2))<=3:
        print(2)
    else:
        print(3)