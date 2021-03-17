x = int(input())
ans = 0
while (x+ans) % 100 != 0:
    ans += 1
if ans == 0:
    ans = 100
print(ans)
