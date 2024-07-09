n = int(input())
s = [input() for i in range(n)]
cnt = 0
for name in s:
    if name == "Takahashi":
        cnt += 1
print(cnt)
