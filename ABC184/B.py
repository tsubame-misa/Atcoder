n, x = list(map(int, input().split()))
s = input()
point = x
for i in range(n):
    if s[i] == "o":
        point += 1
    else:
        if point != 0:
            point -= 1
print(point)
