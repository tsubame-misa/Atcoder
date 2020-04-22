import sys
sys.setrecursionlimit(2000000)

h, w = list(map(int, input().split()))
#from collections import deque
c = []
sx = -1
sy = -1
for i in range(h):
    a = input()
    if "s" in a:
        sx = a.find("s")
        sy = i
    c.append(a)

check = [[0]*w for i in range(h)]


def search(x, y):
    # 迷路の外か壁の時
    if x < 0 or x >= w or y < 0 or y >= h or c[y][x] == "#":
        return
    # 訪問済み
    if check[y][x] == 1:
        return

    if c[y][x] == "g":
        print("Yes")
        exit()

    check[y][x] = 1
    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)


search(sx, sy)
print("No")
