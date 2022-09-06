import math
Ax, Ay = list(map(int, input().split()))
Bx, By = list(map(int, input().split()))
Cx, Cy = list(map(int, input().split()))
Dx, Dy = list(map(int, input().split()))


def f0(x, y):
    return (Ax-Cx)*(y-Ay) - (Ay-Cy)*(x-Ax)


def f1(x, y):
    return (Bx-Dx)*(y-By) - (By-Dy)*(x-Bx)


def sign(x):
    if x > 0:
        return 1
    return 0


if sign(f0(Bx, By)) != sign(f0(Dx, Dy)) and sign(f1(Ax, Ay)) != sign(f1(Cx, Cy)):
    print("Yes")
else:
    print("No")
