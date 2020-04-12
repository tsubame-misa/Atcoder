
import math
import itertools
import statistics
#import numpy as np
import collections
n, k = list(map(int, input().split()))
#n以下から等確率に選ぶ　3回動かす 中央値がkになる
p = n*n*n
a = (k-1)*(n-k)*6 + ((k-1)+(n-k))*3 + 1
print(a)
print(a/p)