import itertools
s = input()

if len(s) == 1:
    if int(s) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

d = sorted(list(map(int, list(s))))
count = 0
for i in range(len(d)-2):
    count += 1
    if d[i] != d[i+1]:
        count = 0
    if count >= 3:
        d[i] = 0

d = sorted(d)
count = 0

for i in range(len(d)):
    if d[i] != 0:
        break
    count += 1
del d[:count]

if len(d) >= 3:
    for a, b, c in itertools.permutations(d, 3):
        n = a*100 + b*10 + c
        if n % 8 == 0:
            print("Yes")
            exit()
else:
    if (d[0]*10+d[1]) % 8 == 0 or (d[1]*10+d[0]) % 8 == 0:
        print("Yes")
        exit()
print("No")
