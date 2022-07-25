a, b = list(map(int, input().split()))

if abs(a-b) == 1:
    print("Yes")
    exit()

if (a == 10 or b == 10) and abs(a-b) == 9:
    print("Yes")
    exit()

print("No")
