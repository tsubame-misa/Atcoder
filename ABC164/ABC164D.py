
s = input()
ans = 0
# 2019までの余りの分布
U = [0 for i in range(2019)]
mod = 2019
sum_i_to_n = 0
for i in range(len(s)-1, -1, -1):
    # 後ろから見てく
    # 後ろからi桁目までの合計を2019で割ったやつを足していってる
    # pow(10, 桁数,　mod)
    sum_i_to_n += int(s[i]) * pow(10, len(s)-i-1, mod)
    sum_i_to_n %= mod
    #print(str(sum_i_to_n)+" "+str(s[i:]))
    if sum_i_to_n % mod == 0:
        # 2019で割り切れたら
        ans += 1
    # if U[sum_i_to_n] >= 1:
        #print("-----", end="")
        #print(s[i:], end="")
        #print(" amari=", end="")
        # print(sum_i_to_n)
    # 1817181712114と81712114はあまりが同じ。
    # 5で割って3余るやつ同士を引くと、5で割り切れる理論。
    # 例)293%3=2 743%3=2 (743-293)%3==0
    # 二つの差の1817100000000は2019の倍数よって18171も2019の倍数
    ans += U[sum_i_to_n]
    U[sum_i_to_n] += 1

print(ans)
