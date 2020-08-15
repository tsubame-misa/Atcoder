x, n = list(map(int, input().split()))
p = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#p = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))
dif = 1000
ans = 1000
for i in range(-101, 110):
    if not(i in p):
        if abs(i-x) < dif:
            dif = abs(i-x)
            ans = i
        elif abs(i-x) == dif:
            if ans > i:
                ans = i

print(ans)
