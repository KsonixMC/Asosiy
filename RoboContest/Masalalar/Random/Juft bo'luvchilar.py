import math

t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2:
        print(0)
    else:
        i = 1
        c = 0
        while i <= math.isqrt(n):  # ← faqat shu o'zgardi
            if n % i == 0:
                if i % 2 == 0:
                    c += 1
                if i != n // i and (n // i) % 2 == 0:
                    c += 1
            i += 1
        print(c)