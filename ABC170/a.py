a = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))

for i in range(5):
    if a[i] == 0:
        print(i+1)
