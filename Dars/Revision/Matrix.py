import random
def print2(massive):
    print('_' * ((len(str(massive[0]))-str(massive[0]).count(','))+2))

    for line in massive:
        print('|', end=' ')
        [print(x, end=' ') for x in line]
        print('|')
    print('-' * ((len(str(massive[0]))-str(massive[0]).count(','))+2))

m = int(input("qator="))
n = int(input('ustun='))

mas = []
for i in range(m):
    row = []
    for q in range(n):
        row.append(random.randint(0,1))
    mas.append(row)
# [print(row) for row in mas]
print2(mas)




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

##m = int(input('m='))
##n = int(input('n='))
##v = int(input('q='))
##
##a = []
##for i in range(m):
##    a.append(random.randint(0,9))
##print(a)
##print('*'*20)
##
##b = []
##
##for i in range(m):
##    row = []
##    for q in range(n):
##        if q == 0:
##            row.append(a[i])
##        else:
##            z = row[q-1]*v
##            row.append(z)
##    b.append(row)
##[print(row) for row in b]

##matrix9

##for x in range(0, m, 2):
##    print(mas[x])

##matrix12

# b = []
#
# for y in range(n):
#     row1 = []
#     for x in range(m):
#         row1.append(mas[x][y])
#     b.append(row1)
# [print(row1) for row1 in b]
#
# for i in range(n):
#     print('i =', i)
#     if i%2==1:
#         for q in range(m-1, -1, -1):
#             # print('q =', q)
#             print(b[i][q])
#     else:
#         for q in range(m):
#             print(b[i][q])

# matrix15

# for y in range(m//2+1):
    # for x in range(y, m-y):
    #     print(mas[y][x], end=' ')

# for y in range(m-1, -1, -1):
#     for x in range(m-y-1, y+1):
#         print(mas[x][y], end=' ')

for asosiy in range((min(m,n)+1)//2):
    # print("---")
    for tepa in range(0+asosiy, n-asosiy):
        print(mas[asosiy][tepa], end=' ')
    # print("J")
    for ung in range(1+asosiy, m-asosiy):
        print(mas[ung][n-1-asosiy], end=' ')
    # print("___")
    for past in range(n-1-asosiy-1,-1+asosiy,-1):
        print(mas[m-1-asosiy][past], end=' ')
        # print(mas[past][m-1-asosiy])
    # print('L')
    for chap in range(m-1-asosiy-1,0+asosiy,-1):
        print(mas[chap][0+asosiy], end=' ')
    # print('/')
