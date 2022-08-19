import math
a, b, w = list(map(int, input().split()))

wg = w*1000

_min = math.ceil(wg/b)

if _min*a > wg:
    print("UNSATISFIABLE")
    exit()


ans_min = wg//b
if wg % b != 0:
    ans_min += 1

ans_max = wg//a
if wg % a != 0:
    if (wg % a) / (wg//a) > b-a:
        ans_max += 1

print(ans_min, ans_max)
