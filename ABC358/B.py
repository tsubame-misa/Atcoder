N, A = list(map(int, input().split()))
T = list(map(int, input().split()))

time = 0
apply = False

for t in T:
    if time >= t:
        print(A + time)
        time += A
    else:
        print(t + A)
        time = t + A
