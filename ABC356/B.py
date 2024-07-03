N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(N)]

for i in range(M):
    eated_a = sum([x[i] for x in X])
    if eated_a < A[i]:
        print("No")
        exit()

print("Yes")
