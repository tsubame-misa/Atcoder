from collections import deque
import sys
sys.setrecursionlimit(2000000)
# import math
# from functools import reduce
# import math
# import itertools
# import statistics
# import numpy as np
# import collections
# n = int(input())
h, w = list(map(int, input().split()))
c = []
sx = -1
sy = -1
gx = -1
gy = -1
for i in range(h):
    a = input()
    if "s" in a:
        sx = a.find("s")
        sy = i
    if "g" in a:
        gx = a.find("g")
        gy = i
    c.append(a)

check = [[0]*w for i in range(h)]
check[sy][sx] = 1
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 上下左右の移動距離
stack = [[sy, sx]]

while stack:
    y, x = stack.pop()
    for i in range(4):
        ny, nx = y+dx_dy[i][0], x+dx_dy[i][1]
        if 0 <= nx < w and 0 <= ny < h and check[ny][nx] == 0 and c[ny][nx] != "#":
            check[ny][nx] = 1
            stack.append([ny, nx])
        print(stack)
    if check[gy][gx] == 1:
        print("Yes")
        exit()

print("No")
