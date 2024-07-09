N, X, Y, Z = list(map(int, input().split()))

sorted_XY = sorted([X, Y])

if sorted_XY[0] <= Z and Z <= sorted_XY[1]:
    print("Yes")
    exit()

print("No")
