n, m = list(map(int, input().split()))
H = list(map(int, input().split()))

ans = 0
for h in H:
    m -= h
    if m >= 0:
        ans += 1
    else:
        break

print(ans)
