n, x = list(map(int, input().split()))
A = list(map(int, input().split()))
find = False
for i in range(n):
    if A[i] != x:
        find = True
        print(A[i], end=" ")
if find == False:
    print("")
