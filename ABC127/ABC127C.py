n, m = list(map(int, input().split()))
# = list(map(int, input().split()))
# x = list(map(int, input().split()))
# abc = [int(input()) for i in range(5)]
# n = int(input())
# n, m = list(map(int, input().split()))
l = []
r = []
for i in range(m):
    a, b = list(map(int, input().split()))
    l.append(a-1)
    r.append(b-1)

end = n-1
start = 0
for i in range(m):
    if start <= l[i] and r[i] <= end:
        start = l[i]
        end = r[i]
    elif l[i] < start and r[i] <= end:
        end = r[i]
    elif start <= l[i] and end < r[i]:
        start = l[i]

    if end-start+1 < 0:
        print(0)
        exit()
print(end-start+1)
