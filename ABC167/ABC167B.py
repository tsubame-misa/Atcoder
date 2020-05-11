a, b, c, k = list(map(int, input().split()))
# a = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
#n = int(input())
# n, m = list(map(int, input().split()))
if a+b >= k:
    if k >= a:
        print(a)
    else:
        print(k)
else:
    print(a-(k-(a+b)))
