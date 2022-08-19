n = int(input())

if n < 1000:
    print(0)
    exit()

ans = 0
i = 1000
while i <= n:
    ans += n-i + 1
    i *= 1000

print(ans)
