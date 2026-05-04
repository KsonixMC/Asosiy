N = int(input())
a = 1
for i in range(1, N+1):
    m = []
    for q in range(i):
        m.append(a)
        a += 1
    print(*m)
