x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = (abs(x2 - x1)**2 + abs(y2 - y1)**2)**0.5
b = (abs(x3 - x2)**2 + abs(y3 - y2)**2)**0.5
c = (abs(x1 - x3)**2 + abs(y1 - y3)**2)**0.5

if a < b+c and b < a+c and c < a+b:
    print('uchburchak')
else:
    print('uchburchak emas')