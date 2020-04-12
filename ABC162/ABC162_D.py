n = int(input())
s = input()
count = 0

for i in range(n):
    a = s[i:]
    if s[i]=="R":
        point = a.count("G")*a.count("B")
    elif s[i]=="G":
        point = a.count("R")*a.count("B")
    else:
        point = a.count("R")*a.count("G")
    count += point

#j-i=k-jではない 2j=k+i i=2j-k
#rgb

kom = 0
for i in range(n):
    for j in range(i+1, n):
        if 2*j-i < n:
            if s[i]!=s[j] and s[i]!=s[2*j-i] and s[j]!=s[2*j-i]:
                kom += 1


print(count-kom)



