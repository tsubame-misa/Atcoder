S = input()
upper_case = len([s for s in S if s == s.upper()])
lower_case = len([s for s in S if s == s.lower()])


if upper_case > lower_case:
    print(S.upper())
else:
    print(S.lower())
