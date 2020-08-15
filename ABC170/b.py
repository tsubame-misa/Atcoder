x, y = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))

# xひき　y本
total = 0
for i in range(0, x+1):
    total = 2*i + 4*(x-i)

    if total == y:
        print("Yes")
        exit()
print("No")
