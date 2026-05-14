m = []
for i in range(7):
    a = list(map(int, input().split()))
    m.append(a)

for i in range(7):
    for q in range(7):
        if m[i][q] == 1:
            A = q
            B = i
print(abs(3-A)+abs(3-B))