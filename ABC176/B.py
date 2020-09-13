n = int(input())
s = str(n)
total = 0
for i in range(len(s)):
    total += int(s[i])
if total % 9 == 0:
    print("Yes")
else:
    print("No")
