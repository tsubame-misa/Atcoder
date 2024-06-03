n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = sorted(A+B)

for i in range(len(d)-1):
    if d[i] in A:
        if d[i+1] in A:
            print("Yes")
            exit()
 
print("No")