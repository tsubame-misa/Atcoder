r, d, x2000 = list(map(int, input().split()))
# x = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
# n = int(input())
# n, m = list(map(int, input().split()))
x = [x2000]
for i in range(10):
    b = r*x[i]-d
    x.append(b)
    print(b)
