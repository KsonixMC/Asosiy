import random

# matrix3

# m = int(input('m='))
# n = int(input('n='))
# a = []
# for i in range(m):
#     a.append(random.randint(0, 10))
# b = []
# for i in range(n):
#     b.append(a)
# [print(row) for row in b]

# matrix6

m = int(input('m='))
n = int(input('n='))
q = int(input('q='))

a = []
for i in range(m):
    a.append(random.randint(0,9))
print(a)
print('*'*20)

b = []
for i in range(n):
    row = []
    for x in range(1, m):
        row.append(a[i]*10)
    print(row)
[print(row) for row in b]