str = input()
is_lower = False
is_upper = False
char_dic = dict()

for s in str:
    if s.islower():
        is_lower = True
    if s.isupper():
        is_upper = True
    if char_dic.get(s) is None:
        char_dic[s] = 1
    else:
        char_dic[s] += 1

# print(is_lower)
# print(is_upper)
# print(len(char_dic), len(str))

if is_lower and is_upper and len(char_dic) == len(str):
    print("Yes")
else:
    print("No")
