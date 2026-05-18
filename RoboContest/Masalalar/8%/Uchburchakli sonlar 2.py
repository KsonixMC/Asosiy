t = int(input())
m = []
m1 = []
m2 = []
for i in range(1000):
    m.append(i)
    m1.append(sum(m))

a = list(map(int, input().split()))
for q in range(len(a)):
    if a[q] not in m1:
        s = '0'
    else:
        s = '1'
    m2.append(s)
z = ''
for i in range(len(m2)):
    z += m2[i]
print(z)