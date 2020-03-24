import math
import itertools
import statistics
import collections

n = int(input())
#a = list(map(int, input().split()))
d = []
for i in range(n):
    d.append(int(input()))

d.sort(reverse=True)
count = 1
for i in range(n-1):
    if d[i]>d[i+1]:
        count +=1

#print(d)
print(count)
