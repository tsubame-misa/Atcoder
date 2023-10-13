N = int(input())

memo = {}


def cal(n):
    if n == 0:
        memo[n] = 1
        return 1

    # 既に計算した項なら保存した情報を使う
    if n in memo.keys():
        return memo[n]

    memo[n] = cal(n//2) + cal(n//3)
    return memo[n]


print(cal(N))
