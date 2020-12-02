import itertools

n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

for a, b, c in itertools.combinations(data, 3):
    if a[0]-b[0] != 0 and a[0]-c[0] != 0:
        t1 = (a[1]-b[1])/(a[0]-b[0])
        t2 = (a[1]-c[1])/(a[0]-c[0])
        if t1 == t2:
            print("Yes")
            exit()
    if (a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]):
        print("Yes")
        exit()
print("No")
