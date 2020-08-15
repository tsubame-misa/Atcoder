import datetime
from decimal import Decimal, ROUND_DOWN
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
# n, m, p = list(map(int, input().split()))
# a = list(map(int, input().split()))
#
#  abc = [int(input()) for i in range(5)]
#n = int(input())
#n, m = list(map(int, input().split()))
x, k, d = list(map(int, input().split()))
#l = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
# data = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
# for i in range(1, int(n**0.5)+1):

shou = x//d
amari = x % d

if x >= 0:
    if shou <= k:
        k -= shou
        if k % 2 == 0:
            ans = amari
        else:
            ans = min(abs(amari+d), abs(amari-d))
    else:
        ans = x-d*k
else:
    if -1*shou <= k:
        k += shou
        if k % 2 == 0:
            ans = amari
        else:
            ans = min(abs(amari+d), abs(amari-d))
    else:
        ans = abs(x+d*k)


# print(shou)
# print(amari)

print(ans)
