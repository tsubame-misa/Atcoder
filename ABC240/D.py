n = int(input())
a = list(map(int, input().split()))

stack = []
ans_cnt = 0


for i in range(n):
    if len(stack) > 0:
        if stack[-1][0] != a[i]:
            stack.append([a[i], 1])
            ans_cnt += 1
        else:
            stack[-1] = [stack[-1][0], stack[-1][1]+1]
            ans_cnt += 1
    else:
        stack.append([a[i], 1])
        ans_cnt += 1

    if len(stack) > 0 and stack[-1][0] == stack[-1][1]:
        ans_cnt -= stack[-1][0]
        stack.pop()

    print(ans_cnt)
