import math
n = int(input())

def tub(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

for i in range(n-1, 0 ,-1):
    if tub(i) == True:
        a = i
        break

f = 0
m = n+1
while f == 0:
    if tub(m) == True:
        b = m
        break
    else:
        m += 1

if abs(a-n) == abs(b-n):
    print(a, b)
else:
    print(min(abs(a-n), abs(b-n)))