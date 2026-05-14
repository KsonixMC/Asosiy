n = input()
a = []
a.extend(n)
S = 0
for i in range(len(a)):
    S += int(a[i])
if S%2 == 1:
    print('yes')
else:
    print('no')