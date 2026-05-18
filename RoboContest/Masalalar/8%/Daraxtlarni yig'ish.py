t = int(input())
for i in range(t):
    n = int(input())
    a = []
    a.extend(str(bin(n)[2:]))
    print(a.count('1'))