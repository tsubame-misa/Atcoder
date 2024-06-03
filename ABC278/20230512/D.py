n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]


# print("------------")

# 問題点？ Xqがデカイ

# 1：リセット
# 2：AiにXqだけ可算
# 3：出力

base = 0
change_cnt = 0
changed = [0]*n

# 辞書でやった方がシンプル
# 辞書の初期化はO(1)

for i in range(q):
    if query[i][0] == 1:
        base = query[i][1]
        change_cnt += 1
    elif query[i][0] == 2:
        if change_cnt == changed[query[i][1]-1]:
            a[query[i][1]-1] += query[i][2]
        else:
            a[query[i][1]-1] = query[i][2]
            changed[query[i][1]-1] = change_cnt
    else:
        if change_cnt == changed[query[i][1]-1]:
            print(base+a[query[i][1]-1])
        else:
            print(base)


"""
n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]


# print("------------")

# 問題点？ Xqがデカイ

# 1：リセット
# 2：AiにXqだけ可算
# 3：出力

base = 0
change_cnt = 0
changed = [0]*n

for i in range(q):
    # print(a)
    if query[i][0] == 1:
        base = query[i][1]
        # こいつか？？？
        a = [0]*n
        # print("base ", base, "a ", a)
    elif query[i][0] == 2:
        a[query[i][1]-1] += query[i][2]
        # print(a)
    else:
        print(base+a[query[i][1]-1])

"""
