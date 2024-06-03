h, m = list(map(int, input().split()))

h_end = 23
m_end = 59

test_h = h
test_m = m

total = h_end*m_end
i = 0

while i < total:
    a = test_h//10
    b = test_h % 10
    c = test_m//10
    d = test_m % 10
    if a*10+c <= h_end and b*10+d <= m_end:
        break

    if test_m < m_end:
        test_m += 1
    else:
        test_m = 0
        if test_h < h_end:
            test_h += 1
        else:
            test_h = 0


print(test_h, test_m)
