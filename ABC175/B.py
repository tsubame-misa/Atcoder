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
n = int(input())
l = list(map(int, input().split()))
count = 0
data = []
for a, b, c in itertools.combinations(l, 3):
    if a+b > c and b+c > a and c+a > b:
        data.append([a, b, c])
for i in range(len(data)):
    if data[i][0] != data[i][1] and data[i][0] != data[i][2] and data[i][1] != data[i][2]:
        count += 1
print(count)
