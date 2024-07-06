a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

# r1 = [
#     [a, b, c],
#     [d, b, c],
#     [d, e, c],
#     [a, e, c],
#     [a, b, f],
#     [d, b, f],
#     [d, e, f],
#     [a, e, f],
# ]

# r2 = [
#     [g, h, i],
#     [j, h, i],
#     [j, k, i],
#     [g, k, i],
#     [g, h, l],
#     [j, h, l],
#     [j, k, l],
#     [g, k, l],
# ]

test = [j - a, d - g, k - b, e - h, f - i, l - c]

for i in range(len(test)):
    if test[i] <= 0:
        print("No")
        exit()

print("Yes")

# # x座標が被っていなければ
# print(j - a, g - d)
# if not (j - a > 0 or d - g > 0):
#     print("No")
#     exit()

# # Y
# print(k - b, e - h)
# if not (k - b > 0 or e - h > 0):
#     print("No")
#     exit()


# # Z
# print(f - i, l - c)
# if not (f - i > 0 or l - c > 0):
#     print("No")
#     exit()

# print("Yes")
