n = input()
m = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
m1 = []
m1.extend(m)
a = []
a.extend(n)
for i in range(52):
    print(f'{m1[i]} {a.count(m1[i])}')