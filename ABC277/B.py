n = int(input())
s = [str(input()) for i in range(n)]

list1 = ["H", "D", "C", "S"]
list2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

for i in range(n):
    if not(s[i][0] in list1 and s[i][1] in list2):
        print("No")
        exit()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if s[i] == s[j]:
            print("No")
            exit()

print("Yes")
