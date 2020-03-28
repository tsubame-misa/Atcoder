import math
import itertools
import statistics
#import collections
x = int(input())
#A = (map(int, input().split()))

total = 0
total += (x//500) *1000
x = x%500

total += (x//100)* 20 *5
x = x%100
total += (x//50) *10*5
x = x%50
total += (x//10) * 2*5
x = x%10
total += (x//5) *5

print(total)

