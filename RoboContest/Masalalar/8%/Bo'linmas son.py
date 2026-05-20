n, k = map(int, input().split())

q = n // (k - 1)
r = n % (k - 1)

if r == 0:
    print(q * k - 1)
else:
    print(q * k + r)