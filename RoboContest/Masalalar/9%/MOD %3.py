N = input()
v = []
v.extend(N)
if sum(map(int, v)) % 3 == 0:
    print('Yes')
else:
    print('No')