
import math
import itertools
import statistics
#import collections
n = int(input())
a = list(map(int, input().split()))
#a.sort()

#rate = [400, 800, 1200, 1600, 2000, 24000, 2800, 3200]
count = [0]*9
for i in range(n):
    if a[i] < 400:
        count[0] += 1
    elif a[i] < 800:
        count[1] += 1
    elif a[i] < 1200:
        count[2] += 1
    elif a[i] < 1600:
        count[3] += 1
    elif a[i] < 2000:
        count[4] += 1
    elif a[i] < 2400:
        count[5] += 1
    elif a[i] < 2800:
        count[6] +=1
    elif a[i] < 3200:
        count[7] +=1
    else:
        count[8] += 1


ans = 0
for i in range(0, 8):
    if count[i] > 0:
        ans += 1


ans_max = ans+count[8]

"""
if ans+count[8] <= 8:
    ans_max = ans+count[8]
else:
    ans_max = 8
"""
   
if ans==0:
    ans = 1

print(str(ans)+" "+str(ans_max))

        
