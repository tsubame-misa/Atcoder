s, t = list(input().split())

for w in range(1, len(s) - 1):
    w_array = [s[x : x + w] for x in range(0, len(s), w)]
    for c in range(0, w):
        c_str = "".join([w_str[c] for w_str in w_array if len(w_str) > c])
        if c_str == t:
            print("Yes")
            exit()
print("No")
