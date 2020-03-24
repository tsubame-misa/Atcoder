
import math
import itertools
import statistics
#import collections
n = int(input())
s = input()

amari = 0
plus = 0

for i in range(n):
    if s[i]=="(":
        plus += 1
    else:
        if plus <= 0:
            amari +=1
        else:
            plus -= 1

for i in range(amari):
    print("(", end="")

print(s, end="")

for i in range(plus):
    print(")", end="")





