import math
n = int(input())
a = 1
b = 1
for i in range(11):
    a *= n-1-i
    b *= i+1
print(a//b)
