n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# 1回回してみないとdp[i-1]が更新された時の場合を取れないから2周する
for i in range(2*n):
    t[i % n] = min(t[i % n], t[(i-1) % n]+s[(i-1) % n])

for ans in t:
    print(ans)
