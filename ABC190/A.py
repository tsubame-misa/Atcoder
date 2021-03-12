t, a, c = list(map(int, input().split()))
if c == 0:
    if a < t:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if a <= t:
        print("Takahashi")
    else:
        print("Aoki")
