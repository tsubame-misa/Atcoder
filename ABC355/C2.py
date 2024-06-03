n, T = list(map(int, input().split()))
A = list(map(int, input().split()))

col = [n for i in range(n)]
row = [n for i in range(n)]
naname1 = n
naname2 = n


for i in range(T):
    r = (A[i]-1)//n
    c = (A[i]-1)%n

    row[r] -= 1
    col[c] -= 1
    
    if r==c:
        naname1 -= 1
    
  
    if r+c == (n-1):
        naname2 -= 1

    # print("---------", A[i])

    # print(r+c, 2*(n-1))

    # print(row)
    # print(col)
    # print(naname1)
    # print(naname2)
    
    if 0 in [row[r], col[c], naname1, naname2]:
        print(i+1)
        exit()


print(-1)
