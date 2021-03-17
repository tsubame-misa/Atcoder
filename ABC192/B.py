s = input()
ans = "Yes"
for i in range(len(s)):
    if i % 2 == 0:
        if not s[i].islower():
            ans = "No"
    else:
        if not s[i].isupper():
            ans = "No"
print(ans)
