n = int(input())
a = list(map(int, input().split()))


def findAns(i, x, count):
    if i == x:
        return count
    else:
        return findAns(i, a[x-1], count+1)


for i in range(n):
    print(findAns(i+1, a[i], 1), end=" ")
print()
