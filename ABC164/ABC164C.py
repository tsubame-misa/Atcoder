import collections
import sys
sys.setrecursionlimit(2000000)
# import math
# import itertools
# import statistics
# import numpy as np
n = int(input())
#a, b, c, d = list(map(int, input().split()))
#a = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(input())

s_count = collections.Counter(s)

print(len(s_count))
