from collections import deque
# from math import factorial
# import collections
# import sys
# sys.setrecursionlimit(2000000)
# import math
# import itertools
# import statistics
# import numpy as np
k = int(input())
#n, k = list(map(int, input().split()))
#a = list(map(int, input().split()))
"""
k回これをやる
• Queue に対して Dequeue を行う。取り出した要素を x とする。
１． x mod 10 ̸= 0 なら、 10x + (x mod 10) − 1 を Enqueue する。
２． 10x + (x mod 10) を Enqueue する。
３．x mod 10 ̸= 9 なら、 10x + (x mod 10) + 1 を Enqueue する。
K 回目の操作において取り出した数が、 K 番目の Lunlun Number となっています。
1,2,3で前後で隣同士の差が1のやつを並べてる
"""
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(k):
    x = q.popleft()
    a = 10*x+(x % 10)
    if x % 10 != 0:
        q.append(a-1)
    q.append(a)
    if x % 10 != 9:
        q.append(a+1)

print(x)
# print(q)
