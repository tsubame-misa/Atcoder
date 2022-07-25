A, B, C, D, E, F, X = list(map(int, input().split()))


takahashi_c = A+C
aoki_c = D+F


takahashi = X//takahashi_c*(A*B)

if X % takahashi_c >= A:
    takahashi += A*B
else:
    takahashi += (X % takahashi_c)*B


aoki = X//aoki_c*(D*E)
if X % aoki_c >= D:
    aoki += D*E
else:
    aoki += (X % aoki_c)*E


if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
