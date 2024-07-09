S = input()
T = input()

s_cnt = 0
ans = []
for i in range(len(T)):
    if T[i] == S[s_cnt]:
        ans.append(str(i + 1))
        s_cnt += 1


print(" ".join(ans))
