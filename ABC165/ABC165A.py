k = int(input())
#n, m = list(map(int, input().split()))
a, b = list(map(int, input().split()))
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
for i in range(a, b+1):
    if i % k == 0:
        print("OK")
        exit()

print("NG")
