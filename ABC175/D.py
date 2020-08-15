import heapq
from fractions import gcd
from functools import reduce
from collections import deque
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
c = list(map(int, input().split()))
data = []
for i in range(len(p)):
    p[i] -= 1

for i in range(n):
    data.append([p[i], c[i], 0])

# print(p)
ans = []
cnt = 0
for i in range(n):
    score = 0
    find = False
    point = i
    _max = -10**9
    cnt = 0
    path = [i]
    while cnt < k and find == False:
        # print(point)
        """
        if data[point][2] == 2:
            print("find")
            find = True
        else:
        """
        point = p[point]
        score += c[point]
        #data[point][2] += 1
        path.append(point)
        if score >= _max:
            _max = score
        cnt += 1
        # print(score)
    # print(path)
    """
    if find == True:
        roop = []
        for i in range(len(path)):
            if path[i] == point:
                roop = path[i:]
                print("point:"+" "+str(point), end=" ")
                print("roop ", end=" ")
                print(roop)
                break

    if sum(roop) > 0:
        score += (k-cnt)//len(roop) * sum(roop)
        cnt += (k-cnt)//len(roop) * len(roop)
        if score > _max:
            _max = score
        for i in range(k-cnt):
            score += c[roop[i]]
            if score > _max:
                _max = score
    """
    ans.append(_max)
    #print(path, end=" score")
    #print(_max, end=" path len")
    # print(len(path))

print(ans)
print(max(ans))
