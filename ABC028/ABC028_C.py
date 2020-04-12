import math
import itertools
import statistics
#import numpy as np
import collections
n = list(map(int, input().split()))
l = list(itertools.combinations(n, 3))

s = []
for i in range(len(l)):
    s.append(sum(l[i]))

ss = list(set(s))
ss.sort()

print(ss[-3])

