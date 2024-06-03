a, b = list(map(str, input().split()))

for i in range(len(min(a, b))):
    a_int = int(a[len(a)-1-i])
    b_int = int(b[len(b)-1-i])
    if a_int + b_int >= 10:
        print("Hard")
        exit()
print("Easy")
