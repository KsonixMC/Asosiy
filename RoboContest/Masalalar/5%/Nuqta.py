N = int(input())

for i in range(N):
    Ax, Ay, Bx, By = map(int, input().split())
    if Bx > Ax:
        a = Bx - Ax
        p1 = Bx + a
    else:
        a = abs(Ax - Bx)
        p1 = Bx - a
    if By > Ay:
        b = By - Ay
        p2 = By + b
    else:
        b = Ay - By
        p2 = By - b
    print(p1, p2)
