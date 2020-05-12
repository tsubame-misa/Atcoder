n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
# x = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
# n = int(input())
# n, m = list(map(int, input().split()))
bc = [list(map(int, input().split())) for i in range(m)]
a.sort()
bc_sorted = sorted(bc, key=lambda x: x[1], reverse=True)
l = 0
for i in range(m):
    l += bc[i][0]
j = 0
for i in range(min(l, n)):
    if a[i] <= bc_sorted[j][1]:
        a[i] = bc_sorted[j][1]
        bc_sorted[j][0] -= 1
        if bc_sorted[j][0] == 0:
            j += 1
    else:
        break
print(sum(a))
