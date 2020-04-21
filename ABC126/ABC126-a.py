n, k = list(map(int, input().split()))
# r = list(map(int, input().split()))
s = input()

for i in range(n):
    if i == k-1:
        print(s[i].swapcase(), end="")
    else:
        print(s[i], end="")
