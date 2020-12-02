def calc_sum(n):
    return n*(n+1)/2


n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
total = 0
for a, b in data:
    total += calc_sum(b)-calc_sum(a-1)

print(int(total))
