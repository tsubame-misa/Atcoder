n = int(input())
a = list(map(int, input().split()))
data = [0 for i in range(2*pow(10, 5)+1)]


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


for num in a:
    data[num] += 1

ans = 0
for num in a:
    divs = make_divisors(num)
    for d in divs:
        cnt_j = data[d]
        cnt_k = data[num//d]
        ans += cnt_j*cnt_k

print(int(ans))
