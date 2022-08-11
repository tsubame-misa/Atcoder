n = int(input())
a = list(map(int, input().split()))
x = int(input())


a_sum = sum(a)

a_div = x//a_sum

ans = n*a_div

x -= a_sum*a_div


for i in range(len(a)):
    x -= a[i]
    ans += 1
    if x < 0:
        print(ans)
        exit()
