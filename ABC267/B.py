S = str(input())
pin = [[6], [3], [7, 1], [4, 0], [8, 2], [5], [9]]

# ピン1が倒れている
r1 = S[0] == "0"
# 立っているピンが 1本以上存在する。
r2 = []
# ピンが全て倒れている列が存在する。
r3 = []

for i in range(len(pin)):
    stand = False
    drop = True
    for p in pin[i]:
        if S[p] == "1":
            stand = True
            drop = False
    if stand:
        r2.append(i)
    if drop:
        r3.append(i)


if not r1:
    print("No")
    exit()

for i in range(len(r2)-1):
    x_0 = r2[i]
    x_1 = r2[i+1]
    if x_1 - x_0 >= 2:
        print("Yes")
        exit()

print("No")
