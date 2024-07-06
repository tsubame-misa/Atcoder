N = int(input())
S = input()
T = input()


s_w_cnt = S.count("W")
s_b_cnt = S.count("B")
t_w_cnt = T.count("W")
t_b_cnt = T.count("B")

if s_w_cnt != t_w_cnt or s_b_cnt != t_b_cnt:
    print("No")
    exit()
