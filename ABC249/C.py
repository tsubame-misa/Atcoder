import itertools

n, k = list(map(int, input().split()))
s = [input().split() for i in range(n)]

max_count = 0

for i in range(n+1):
    for pair in itertools.combinations(s, i):
        char_dict = dict()
        count = 0
        for str in pair:
            for j in range(len(str[0])):
                if char_dict.get(str[0][j]) is None:
                    char_dict[str[0][j]] = 1
                else:
                    char_dict[str[0][j]] += 1

        for v in char_dict.values():
            if v == k:
                count += 1
        if count > max_count:
            max_count = count

print(max_count)
