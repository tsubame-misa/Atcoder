n, q = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(q)]

follow = set()

for t, a, b in data:
    if t == 1:
        follow.add((a, b))
    elif t == 2:
        follow.discard((a, b))
    else:
        if (a, b) in follow and (b, a) in follow:
            print("Yes")
        else:
            print("No")
