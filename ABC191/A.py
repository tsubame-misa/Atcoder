v, t, s, d = list(map(int, input().split()))

if v*t <= d and d <= v*s:
    print("No")
else:
    print("Yes")
