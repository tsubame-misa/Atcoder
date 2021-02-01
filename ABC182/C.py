s = input()
total = 0
data = []
for i in range(len(s)):
    total += int(s[i])
    data.append(int(s[i]) % 3)

ans = 0
if total % 3 != 0 and len(s) <= 1:
    print(-1)
    exit()

if total % 3 == 1:
    if 1 in data:
        ans = 1
    else:
        if len(s) <= 2:
            ans = -1
        else:
            ans = 2
elif total % 3 == 2:
    if 2 in data:
        ans = 1
    else:
        if len(s) <= 2:
            ans = -1
        else:
            ans = 2

print(ans)

"""
0 3 6 9
1 4 7 10
2 5 8 11
total%3=1->mod=1の数を１つ引けばいい
　　　　    mod=0, 2しかない時->2つ以上あるはず, 2つ引く
"""
