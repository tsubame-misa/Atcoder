s = input()
if len(s) == 1:
    print(2)
elif len(s) == 2:
    if s[0] != s[1]:
        print(7)
    else:
        print(6)
else:
    _one = []
    _two = []
    _three = []
    ans = 0
    for i in range(len(s)):
        _one.append(s[i])
    one = list(set(_one))
    ans += len(one)+1

    for i in range(len(s)-1):
        _two.append(s[i:i+2])
    two = list(set(_two))
    ans += len(two)+1
    l = {}
    r = {}
    for i in range(len(two)):
        l[two[i][0]] = 1
        r[two[i][1]] = 1
    ans += len(l)
    ans += len(r)

    for i in range(len(s)-2):
        _three.append(s[i:i+3])
    three = list(set(_three))
    ans += len(three)+1
    a = {}
    b = {}
    c = {}
    for i in range(len(three)):
        a[three[i][0]] = 1
        b[three[i][1]] = 1
        c[three[i][2]] = 1
    ans += len(a)
    ans += len(b)
    ans += len(c)

    A = []
    B = []
    C = []
    for i in range(len(three)):
        A.append(three[i][:-1])
        B.append(three[i][1:])
        ss = three[i][0]+three[i][2]
        C.append(ss)
    AA = set(A)
    BB = set(B)
    CC = set(C)
    ans += len(AA)
    ans += len(BB)
    ans += len(CC)

    print(ans)
