n = int(input())
A = list(map(int, input().split()))
a = max(A[:2**n//2])
b = max(A[2**n//2:])
print(A.index(min(a, b))+1)
