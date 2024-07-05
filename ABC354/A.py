H = int(input())

plant_h = 0
i = 0
while plant_h <= H:
    plant_h += 2**i
    i += 1

print(i)
