import numpy as np

n, T = list(map(int, input().split()))
A = list(map(int, input().split()))

#単位行列
I = np.identity(n)
#単位行列と逆のやつ
I2 = []
for i in range(n):
    b = [0 for i in range(n)]
    b[n-1-i] = 1
    I2.append(b)
I22 = np.array(I2)

#列ベクトル
x = np.array([1 for i in range(n)])

# ビンゴ表
gyoretu2 = []
for i in range(n):
    a  = [0 for i in range(n)]
    gyoretu2.append(a)

gyouretu = np.array(gyoretu2)

for i in range(T):
    row = (A[i]-1)//n
    col = (A[i]-1)%n
    gyouretu[row,col] = 1


    for j in range(n):
        # 行のチェック
        a = gyouretu[j] @ x.T
        if a == n:
            print(i+1)
            exit()
        # 列のチェック
        a = gyouretu[:,j] @ x
        if a == n:
            print(i+1)
            exit()
    
    # 対角のチェック
    if np.trace(gyouretu@I) == n:
        print(i+1)
        exit()
    
    if np.trace(gyouretu@I22) == n:
        print(i+1)
        exit()

print(-1)
