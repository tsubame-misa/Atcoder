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
a, b, h, m = list(map(int, input().split()))
if h >= 12:
    h -= 12
ms = 360*(m/60)
ns = 360*(h/12) + 30*(m/60)

mx = b*math.cos(math.radians(ms))
my = b*math.sin(math.radians(ms))
hx = a*math.cos(math.radians(ns))
hy = a*math.sin(math.radians(ns))

ans = math.sqrt((mx-hx)**2 + (my-hy)**2)
print(ans)
