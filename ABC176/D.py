####不正解########

import datetime
from decimal import Decimal, ROUND_DOWN
import heapq
from fractions import gcd
from functools import reduce
from collections import deque
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
h, w = list(map(int, input().split()))
Ch, Cw = list(map(int, input().split()))
Dh, Dw = list(map(int, input().split()))
s = [input() for i in range(h)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
q = deque()
count = [[0 for j in range(w)] for i in range(h)]
mark = 1
"""
for i in range(h):
    for j in range(w):
        print(count[i][j], end="")
    print()
"""
for i in range(h):
    for j in range(w):
        if s[i][j] == "." and count[i][j] == 0:
            # print(str(i)+","+str(j))
            q.append([i, j])  # (x, y)
            count[i][j] = mark
            # search
            while q:
                y, x = q.popleft()
                for i in range(4):
                    nx, ny = x+d[i][1], y+d[i][0]
                    if 0 <= ny and ny < h and 0 <= nx and nx < w and s[ny][nx] == "." and count[ny][nx] == 0:
                        count[ny][nx] = mark
                        q.append([ny, nx])
            mark += 1
"""
for i in range(h):
    for j in range(w):
        print(count[i][j], end="")
    print()
"""

if count[Ch-1][Cw-1] == count[Dh-1][Dw-1]:
    print(0)
    exit()

path = []
for i in range(h):
    for j in range(w):
        if count[i][j] != 0:
            for k in range(max(0, i-2), min(h, i+2)):
                for l in range(max(0, j-2), min(w, j+2)):
                    if count[k][l] != 0 and count[k][l] != count[i][j]:
                        path.append([count[k][l], count[i][j]])

# print(path)
pair = [[] for i in range(mark-1)]
for i in range(len(path)):
    if not(path[i][1] in pair[path[i][0]-1]):
        pair[path[i][0]-1].append(path[i][1])
    if not(path[i][0] in pair[path[i][1]-1]):
        pair[path[i][1]-1].append(path[i][0])
# print(pair)

start = count[Ch-1][Cw-1]
end = count[Dh-1][Dw-1]

# print(start)
# print(end)

q = []
visited = [0 for i in range(mark-1)]
q.append(start-1)
root = []
while q:
    point = q.pop()
    for i in range(len(pair[point])):
        _next = pair[point][i]
        root.append(_next-1)
        if _next == end:
            print(len(root))
            # print(root)
            exit()
        if visited[_next-1] == 0:
            q.append(_next-1)
print(-1)
