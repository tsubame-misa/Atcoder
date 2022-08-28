s = input()
t = input()

n = s

for i in range(2, len(t)):
    if (i == len(n) and len(n) != len(t)) or n[i] != t[i]:
        if t[i] == n[i-1] and n[i-1] == n[i-2]:
            n = n[:i] + t[i] + n[i:]
        else:
            print("No")
            exit()

if n != t:
    print("No")
else:
    print("Yes")
