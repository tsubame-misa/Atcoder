s = input()
start = int(s[0]+s[1])
end = int(s[2]+s[3])

if 1 <= start <= 12 and 1 <= end <= 12:
    print("AMBIGUOUS")
elif 1 <= start <= 12 and (end > 12 or end == 0):
    print("MMYY")
elif (start > 12 or start == 0) and 1 <= end <= 12:
    print("YYMM")
else:
    print("NA")
