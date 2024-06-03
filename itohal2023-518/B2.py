H, W = list(map(int, input().split()))
a = [list(map(str, input().split())) for i in range(H)]

tb = ""
for i in range(W+2):
    tb += "#"

print(tb)
for i in range(H):
    line = "#" + "".join(a[i]) + "#"
    print(line)
print(tb)
