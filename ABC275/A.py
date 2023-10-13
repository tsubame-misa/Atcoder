N = int(input())
H = list(map(int, input().split()))

_max = max(H)
print(H.index(_max)+1)
