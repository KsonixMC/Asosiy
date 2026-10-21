n, m, x = map(int, input().split())

c = [0] * m

for v in map(int, input().split()):
    c[v % m] += 1

j = 0

for r in range(m):
    for q in range(r, m):
        if (r * q) % m == x:
            if r == q:
                j += c[r] * (c[r] - 1) // 2
            else:
                j += c[r] * c[q]

print(j)
