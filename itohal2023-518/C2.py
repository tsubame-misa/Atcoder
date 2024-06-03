N, M = list(map(int, input().split()))
sc = [list(map(int, input().split())) for i in range(M)]

ans = 10**(N-1)
end = 10**N

if N == 0:
    N = 1
    ans = 0
    end = 10
if N == 1:
    ans = 0

while ans < end:
    str_ans = str(ans)
    found = True
    for s, c in sc:
        if str_ans[s-1] != str(c):
            found = False
            break
    if found:
        print(ans)
        exit()

    ans += 1

print(-1)
