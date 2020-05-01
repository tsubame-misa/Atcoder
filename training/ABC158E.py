n, p = list(map(int, input().split()))
# a = list(map(int, input().split()))
s = input()
rem = [0 for i in range(p)]
total = 0
ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i+1
    print(ans)
else:
    for i in range(len(s)-1, -1, -1):
        total += int(s[i])*pow(10, len(s)-i-1, p)
        total %= p
        if total % p == 0:
            ans += 1
        ans += rem[total]
        rem[total] += 1

    print(ans)
