# A, B = list(map(int, input().split()))
# S = list(map(input().split())

"""
import itertools
s = []
for i in range(N):
    s.append(int(input()))


for i in range(n):
    x,y = [int(j) for j in input().split()]
    dataX.append(x)
    dataY.append(y)

二次元配列
for i in range(n):
    d.append([int(j) for j in input().split()])

integer_set = [list(map(int, input().split())) for _ in range(q)]


c = [[j for j in input()] for i in range(h)]

sp.sort(key=lambda x:(x[1], -x[2]))
sorted_data = sorted(data, key=lambda x:(x[1], x[2]))
コレクションのvalue値を取る時
for v in a.values():
        if v%2!=0:
            even = False

二次元配列
road = [[0]*n]*n　こうやって書くと全部更新されるから
road = [[0]*n for i in range(n)]って書くといい

一番回数の多いもの取得
l = collections.Counter(s)
a = l.most_common()[0][0]

forの逆
for i in reversed(range(0, n)):

順列重複あり
ans = list(itertools.product(l, repeat=n))

l_sorted = sorted(l, key=lambda x: x[1], reverse=True)
第二引数降順
ans = sorted(s, key=lambda x: (x[0], -x[1]))
a_count = collections.Counter(a)
a_list = list(a_count.items())

y = ''.join(list(reversed(x)))

"""

import heapq
from fractions import gcd
from functools import reduce
from collections import deque
# from math import factorial
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
# import statistics
# import numpy as np
# n = int(input())
# a, b, c, k = list(map(int, input().split()))
# a = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
# n = int(input())
# a, b, h, m = list(map(int, input().split()))
n, m, q = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# k = int(input())
# a = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
# py = [list(map(int, input().split())) for i in range(m)]
# b = list(map(int, input().split()))
point = [n]*m
pepole = [[0]*m for i in range(n)]
print(point)
print(pepole)


def total(k):
    ans = 0
    # print(pepole)
    for i in range(m):
        # print(pepole[k][i])
        ans += pepole[k][i]*point[i]
    # print(ans)
    return ans


Ans = []
for i in range(q):
    s = list(map(int, input().split()))
    # print(s)
    if s[0] == 1:
        Ans.append(total(s[1]-1))
    else:
        # print(s[2])
        point[s[2]-1] -= 1
        pepole[s[1]-1][s[2]-1] = 1

for a in Ans:
    print(a)
