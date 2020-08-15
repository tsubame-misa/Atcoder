h, w, f = list(map(int, input().split()))
c = [input() for i in range(h)]
count = 0
bit_h = []
for k in range(2**h):
    hh = []
    for l in range(h):
        if((k >> l) & 1):
            hh.append(1)
        else:
            hh.append(0)
    bit_h.append(hh)

bit_w = []
for i in range(2**w):
    ww = []
    for j in range(w):
        if((i >> j) & 1):
            ww.append(1)
        else:
            ww.append(0)
    bit_w.append(ww)

# print(bit_h)
# print(bit_w)

ans = 0
for i in range(len(bit_h)):
    for j in range(len(bit_w)):
        count = 0
        for k in range(h):
            for l in range(w):
                if bit_h[i][k] == 1 and bit_w[j][l] == 1 and c[k][l] == "#":
                    count += 1
        # print(count)
        if count == f:
            ans += 1
print(ans)


""""
def Qc():
    h, w, k = map(int, input().split())
    lines = [input() for v in range(h)]
    ans = 0
    for ir in range(2 ** h):
        for ic in range(2 ** w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if (ir >> i) & 1 and (ic >> j) & 1:
                        if lines[i][j] == '#':
                            cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
 
 
if __name__ == '__main__':
    Qc()
"""
