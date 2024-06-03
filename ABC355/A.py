a, b = list(map(int, input().split()))
data =[1,2,3]

if a==b:
    print(-1)
else:
    ans = list(filter(lambda x: not(x in [a, b]), data))
    print(ans[0])
