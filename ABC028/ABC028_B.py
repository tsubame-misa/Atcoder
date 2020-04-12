import math
import itertools
import statistics
#import numpy as np
import collections

s = input()
l = ["A", "B", "C", "D", "E", "F"]
for i in range(len(l)):
    if i!=len(l)-1:
        print(s.count(l[i]), end=" ")
    else:
        print(s.count(l[i]))
