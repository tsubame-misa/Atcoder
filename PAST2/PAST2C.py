n = int(input())
s = []
for i in range(n):
    s.append(input())

ans = []
a = ""
for j in range(len(s[0])):
    if s[-2][j] == "#":
        if j == 0:
            if s[-1][j] == "X" or s[-1][j+1] == "X":
                a += "X"
            else:
                a += "#"
        elif j == 2*len(s)-1:
            if s[-1][j-1] == "X" or s[-1][j] == "X":
                a += "X"
            else:
                a += "#"
        else:
            # print("!!"+s[i+1][j-1]+s[i+1][j]+s[i+1][j+1])
            if s[-1][j-1] == "X" or s[-1][j] == "X" or s[-1][j+1] == "X":
                a += "X"
            else:
                a += "#"
    elif s[-2][j] == "X":
        a += "X"
    else:
        a += "."
ans.append(a)

cnt = 0
for i in range(n-3, -1, -1):
    a = ""
    for j in range(len(s[0])):
        if s[i][j] == "#":
            if j == 0:
                if ans[cnt][j] == "X" or ans[cnt][j+1] == "X":
                    a += "X"
                else:
                    a += "#"
            elif j == 2*len(s)-1:
                if ans[cnt][j-1] == "X" or ans[cnt][j] == "X":
                    a += "X"
                else:
                    a += "#"
            else:
                if ans[cnt][j-1] == "X" or ans[cnt][j] == "X" or ans[cnt][j+1] == "X":
                    a += "X"
                else:
                    a += "#"
        elif s[i][j] == "X":
            a += "X"
        else:
            a += "."
    cnt += 1
    ans.append(a)

for i in range(n-2, -1, -1):
    print(ans[i])

print(s[-1])
