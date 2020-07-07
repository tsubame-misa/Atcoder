from collections import deque
# from math import factorial
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
n, m = list(map(int, input().split()))
room = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    room[a-1].append(b-1)
    room[b-1].append(a-1)

ans = [-1]*n


def bfs(i):
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for i in range(len(room[x])):
            if ans[room[x][i]] == -1:
                q.append(room[x][i])
                ans[room[x][i]] = x
    return


bfs(0)
print("Yes")
for i in range(1, n):
    print(ans[i]+1)
