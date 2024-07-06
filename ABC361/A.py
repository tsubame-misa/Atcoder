N, K, X = list(map(int, input().split()))
A = list(input().split())

print(" ".join(A[:K]) + " " + str(X) + " " + " ".join(A[K:]))
