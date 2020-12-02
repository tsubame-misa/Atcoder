# "1234"を[1,2,3,4]に変換
d = list(map(int, list(s)))

# dataから3つずつの組み合わせを作ってくれる
for a, b, c in itertools.combinations(data, 3):
