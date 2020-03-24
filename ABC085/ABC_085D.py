import math
import itertools
import statistics
#import collections

n, h = list(map(int, input().split()))
a = [] #降る
b = [] #投げる

for i in range(n):
    x,y = [int(j) for j in input().split()]
    a.append(x)
    b.append(y)


b2 = sorted(b, reverse=True)
total = 0
a_max = max(a)

#投げた方が強いやつを全部投げた
for i in range(n):
    if b2[i] >= a_max:
        total += b2[i]
        if total >= h:
            print(i+1)
            exit()


count = 0
remain_hp = h

#振るより投げた方がいいやつを投げる
for i in range(n):
    if b[i] >= a_max:
        remain_hp -= b[i]
        count +=1
#振って一番削れるのでやる
count += math.ceil(remain_hp/a_max)
print(count)



