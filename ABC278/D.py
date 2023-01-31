# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())
# query = [list(map(int, input().split())) for i in range(q)]

# for i in range(q):
#     if query[i][0] == 1:
# 多分ここがネック
#         a = [query[i][1]]*n
#     elif query[i][0] == 2:
#         a[query[i][1]-1] += query[i][2]
#     else:
#         print(a[query[i][1]-1])

n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
changed = [-1]*n

base = 0
change_idx = q
for i in range(q):
    if query[i][0] == 1:
        base = query[i][1]
        change_idx = i
    elif query[i][0] == 2:
        if i > change_idx and changed[query[i][1]-1] != change_idx:
            a[query[i][1]-1] = query[i][2]
            changed[query[i][1]-1] = change_idx
        else:
            a[query[i][1]-1] += query[i][2]
    else:
        # print(changed[query[i][1]-1], change_idx, base)
        if changed[query[i][1]-1] == change_idx:
            print(base+a[query[i][1]-1])
        else:
            if change_idx == q:
                print(a[query[i][1]-1])
            else:
                print(base)
    # print(base, change_idx, a, changed)
