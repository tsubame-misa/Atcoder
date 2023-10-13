a, b = list(map(str, input().split()))

for i in range(min(len(a), len(b))):
    if int(a[len(a)-1-i]) + int(b[len(b)-1-i]) >= 10:
        print("Hard")
        exit()

print("Easy")
