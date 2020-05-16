s, t = list(input().split())

a = 0
b = 0
minus = False
minus2 = False
for i in range(2):
    if ord(s[i]) >= 49 and ord(s[i]) <= 57:
        a = int(s[i])
    if s[i] == "B":
        minus = True
for i in range(2):
    if ord(t[i]) >= 49 and ord(t[i]) <= 57:
        b = int(t[i])
    if t[i] == "B":
        minus2 = True
if minus:
    a *= -1
if minus2:
    b *= -1
if minus != minus2:
    print(abs(a-b)-1)
else:
    print(abs(a-b))
