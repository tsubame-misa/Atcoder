n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))
a = [i for i in range(n+1)]  # 1~nまで
ans = 0
mod = pow(10, 9)+7
sum_min = sum(a[:k])  # 前からkコの和
sum_max = sum(a[-k:])  # 後ろからkコ
for i in range(k, n+1):
    ans += sum_max-sum_min+1
    ans %= mod
    sum_min += a[i]  # 足してく
    sum_max += a[-i-1]
ans += 1  # 全部選んだ時
print(ans % mod)
