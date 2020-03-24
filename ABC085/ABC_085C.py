import math
import itertools
import statistics
import collections
 
#n = int(input())
#n枚　y円
 
n, y = list(map(int, input().split()))
 
for i in range(0, n+1):
    for j in range(0, n+1-i):
        money = 1000*i
        money += (5000*j + 10000*(n-i-j))
        if money == y and n==i+j+(n-i-j):
            print(str(n-i-j)+" "+str(j)+" "+str(i))
            exit()
 
print("-1 -1 -1")
 
 