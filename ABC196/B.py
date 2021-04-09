a = input()
point_idx = a.find(".")
if point_idx != -1:
    print(a[:point_idx])
else:
    print(a)
