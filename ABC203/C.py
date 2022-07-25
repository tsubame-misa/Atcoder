n, k = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]

count_dic = dict()
for _a, b in data:
    if count_dic.get(_a) is None:
        count_dic[_a] = b
    else:
        count_dic[_a] += b

sorted_count_dic = sorted(count_dic.items())
pos = 0
dic_idx = 0

while (dic_idx == 0 and k == 0) or k > 0:
    if dic_idx >= len(sorted_count_dic) or sorted_count_dic[dic_idx][0]-pos > k:
        # 余ったお金で進める分
        pos += k
        break

    k -= sorted_count_dic[dic_idx][0]-pos
    k += sorted_count_dic[dic_idx][1]

    pos = sorted_count_dic[dic_idx][0]
    dic_idx += 1


print(pos)
