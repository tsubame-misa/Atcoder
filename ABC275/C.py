import itertools
from collections import defaultdict


def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


S = [input() for i in range(9)]
# 任意の4点で l, l, l*(2)**0.5

pone_index = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            pone_index.append([i, j])

count = 0
for (p1, p2, p3, p4) in itertools.combinations(pone_index, 4):
    d = []
    for pair in [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]]:
        d.append(dist(pair[0], pair[1]))
    d = sorted(d)
    if (d[0] == d[1] and d[1] == d[2] and d[2] == d[3]) and (d[4] == d[5]):
        count += 1

print(count)
