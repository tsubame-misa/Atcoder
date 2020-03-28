import math
import itertools
import statistics
#import collections
#x = int(input())
k, n = (map(int, input().split()))
#A= (map(int, input().split()))
A =  list(map(int, input().split()))

dif = 0
dif_index = -1
for i in range(n-1):
    if A[i+1]-A[i] >= dif:
        dif = A[i+1]-A[i]
        dif_index = i+1

if A[0] > 0:
    if A[0]+(k-A[-1]) >= dif:
       dif =  A[0]+(k-A[-1])

else :
    if k-A[-1] >= dif:
        dif = k-A[-1] 
        dif_index = 0

print(k-dif)


