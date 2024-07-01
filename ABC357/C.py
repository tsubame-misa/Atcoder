n = int(input())

data = [["#" for i in range(pow(3, n))] for j in range(pow(3, n))]


k = n
while k > 0:
    for i in range(pow(3, n)):
        for j in range(pow(3, n)):
            m = pow(3, k)
            q = pow(3, k - 1)
            if q <= j % m and j % m < q * 2 and q <= i % m and i % m < q * 2:
                data[i][j] = "."

    k -= 1

for i in range(pow(3, n)):
    print("".join(data[i]))
