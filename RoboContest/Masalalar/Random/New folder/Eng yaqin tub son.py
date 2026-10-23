def tub(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
d = 0
while True:
    a = n - d
    b = n + d
    if tub(a) and tub(b) and a != b:
        print(a, b)
        break
    elif tub(a):
        print(a)
        break
    elif tub(b):
        print(b)
        break
    d += 1