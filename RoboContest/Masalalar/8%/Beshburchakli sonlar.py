n = int(input())
s = 1
a = 4
for i in range(n-1):
    s += a
    a += 3
print(s)

n = int(input())
print(n * (3 * n - 1) // 2)