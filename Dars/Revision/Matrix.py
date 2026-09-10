import random
# def print2(massive):
#     print('_' * ((len(str(massive[0]))-str(massive[0]).count(','))+2))
#
#     for line in massive:
#         print('|', end=' ')
#         [print(x, end=' ') for x in line]
#         print('|')
#     print('-' * ((len(str(massive[0]))-str(massive[0]).count(','))+2))

m = int(input("qator(m)="))

mas = []
for i in range(m):
    row = []
    for q in range(m):
        row.append(random.randint(10, 99))
        # row.append(int(input()))
    mas.append(row)
[print(row) for row in mas]
# print2(mas)

print('*'*20)


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

# a = 1
#
# for asosiy in range((min(m,n)+1)//2):
#     # print("---")
#     for tepa in range(0+asosiy, n-asosiy):
#         mas[asosiy][tepa] = a
#         a += 1
#         # print(mas[asosiy][tepa], end=' ')
#     # print("J")
#     for ung in range(1+asosiy, m-asosiy):
#         mas[ung][n-1-asosiy] = a
#         a += 1
#         # print(mas[ung][n-1-asosiy], end=' ')
#     # print("___")
#     for past in range(n-1-asosiy-1,-1+asosiy,-1):
#         mas[m-1-asosiy][past] = a
#         a += 1
#         # print(mas[m-1-asosiy][past], end=' ')
#     # print('L')
#     for chap in range(m-1-asosiy-1,0+asosiy,-1):
#         mas[chap][0+asosiy] = a
#         a += 1
#         # print(mas[chap][0+asosiy], end=' ')
#     # print('/')
#
# [print(row) for row in mas]


# matrix18

# k = int(input('k = '))
#
# Y = 0
# K = 0
#
# for x in range(m):
#     Y += mas[x][k]
#     K *= mas[x][k]
# print(Y, K)

# matrix21

# for x in range(m):
#     s = 0
#     for y in range(1, n, 2):
#         s += mas[x][y]
#         a = s / (n//2)
#     print(a)
#     print('*'*10)


# matrix24

# for y in range(n):
#     maxv = float('-inf')
#     for x in range(m):
#         if maxv < mas[x][y]:
#             maxv = mas[x][y]
#     print(maxv)

# matrix27

# minv = float('inf')
# for x in range(m):
#     s = 0
#     for y in range(n):
#         s += mas[x][y]
#     if minv > s:
#         minv = s
#         a = mas[x]
#
# maxv = float('-inf')
# for i in range(n):
#     if maxv < a[i]:
#         maxv = a[i]
# print(maxv)

# matrix30

# b = []
# for y in range(n):
#     s = 0
#     for x in range(m):
#         s += mas[x][y]
#         a = s / m
#     b.append(a)
#
# for y in range(n):
#     c = 0
#     for x in range(m):
#         if b[y] < mas[x][y]:
#             c += 1
#     print(c, b[y])

# matrix33

# a = '404'
# for y in range(n):
#     c1 = 0
#     c2 = 0
#     for x in range(m):
#         if mas[x][y] > 0:
#             c1 += 1
#         if mas[x][y] < 0:
#             c2 += 1
#         if mas[x][y] == 0:
#             continue
#     if c1 == c2:
#         a = y
# print(a)

# matrix36

# a = mas[0]
# C = 0
# for x in range(1, m):
#     c = 0
#     for y in range(n):
#         if mas[x][y] == a[y]:
#             c += 1
#     if c == n:
#         C += 1
# print(C)


# matrix39

# b = []
# for y in range(n):
#     a = []
#     for x in range(m):
#         a.append(mas[x][y])
#     b.append(a)
# [print(row) for row in b]

# for x in range(n):
#     q = b[x]
#     for y in range(m):
#         for z in range(m):
#             if

# matrix42

# C = 0
# for x in range(m):
#     c = 0
#     for y in range(n-1):
#         if mas[x][y] < mas[x][y+1]:
#             c += 1
#     if c == n-1:
#         C += 1
# print(C)

# matrix45

# b = []
# for i in range(n):
#     row = []
#     for q in range(m):
#         row.append(mas[q][i])
#     b.append(row)
# [print(row) for row in b]
#
# maxv = []
# C = 0
# for y in range(n):
#     c1 = 0
#     c2 = 0
#     for x in range(m-1):
#         if b[y][x] < b[y][x+1]:
#             c1 += 1
#         if b[y][x] > b[y][x+1]:
#             c2 += 1
#     if (c1 == m-1) or (c2 == m-1):
#         C += 1
#         maxv.append(max(b[y]))
# if len(maxv) == 0:
#     print(0)
# else:
#     print(max(maxv))

# matrix48

# k1 = int(input('k1 = '))
# k2 = int(input('k2 = '))

# K1 = []
# K2 = []

# for i in range(m):
#     K1.append(mas[i][k1])
#     K2.append(mas[i][k2])

# mas[i][k1] = K2[i]
# mas[i][k2] = K1[i]
# [print(row) for row in mas]

# matrix51

# maxv = float('-inf')
# minv = float('inf')

# for i in range(m):
#     for q in range(n):
#         if maxv < mas[i][q]:
#             maxv = mas[i][q]
#             maxv_ind = i
#             maxv_satr = mas[i]
#         if minv > mas[i][q]:
#             minv = mas[i][q]
#             minv_ind = i
#             minv_satr = mas[i]
# print('maxv =>', maxv, maxv_ind)
# print('minv =>', minv, minv_ind)

# mas[maxv_ind] = minv_satr
# mas[minv_ind] = maxv_satr
# [print(row) for row in mas]

# matrix54

# a = []
# for i in range(m):
#     a.append(mas[i][-1])

# z = 0

# for i in range(n):
#     c = 0
#     b = []
#     for q in range(m):
#         b.append(mas[q][i])
#         if mas[q][i] < 0:
#             c += 1
#     if c == m:
#         g = i
#         z = b

# if z:
#     print(z, a, g)
#     for y in range(m):
#         mas[y][-1] = z[y]
#         mas[y][g] = a[y]
# else:
#     pass
#     print(404)
# [print(row) for row in mas]

# matrix57

# one = []
# four = []

# for i in range(m//2):
#     one_row = []
#     for q in range(n//2):
#         one_row.append(mas[i][q])
#     one.append(one_row)
# print(one)

# for i in range(m//2, m):
#     four_row = []
#     for q in range(n//2, n):
#         four_row.append(mas[i][q])
#     four.append(four_row)
# print(four)
# print('-'*20)

# for i in range(m//2):
#     for q in range(n//2):
#         mas[i][q] = four[i][q]

# a = 0
# for i in range(m//2, m):
#     b = 0
#     for q in range(n//2, n):
        
#         mas[i][q] = one[a][b]
#         b += 1
#     a += 1
# [print(row) for row in mas]

# matrix60
#
# b = []
# for x in range(m):
#     b_row = []
#     for y in range(n):
#         b_row.append(mas[x][y])
#     b.append(b_row)
#
#
# for x in range(m):
#     b[x].reverse()
#     mas[x] = b[x]
# [print(row) for row in mas]

# matrix63

# minv = float('inf')
# for x in range(m):
#     for y in range(n):
#         if minv > mas[x][y]:
#             minv = mas[x][y]
#             a = x
# mas.pop(a)
#
# [print(row) for row in mas]

# matrix66

# a = 0
# for y in range(n):
#     c = 0
#     for x in range(m):
#         if mas[x][y] < 0:
#             c += 1
#     if c == m:
#         a = y
# if a:
#     print(a)
#     for i in range(m):
#         mas[i].pop(a)
#     [print(row) for row in mas]
# else:
#     pass

# matrix69

# k = int(input('k = '))
#
# for y in range(m):
#     mas[y].insert(k+1, 1)
# [print(row) for row in mas]

# matrix72

# a = ''
# for y in range(n):
#     c = 0
#     for x in range(m):
#         if mas[x][y] > 0:
#             c += 1
#     if c == m:
#         a = y
#         break
# print(a)
# if a > -1:
#     for i in range(m):
#         mas[i].insert(a+1, 1)
# else:
#     pass
# [print(row) for row in mas]

# matrix75

# for x in range(m):
#     for y in range(1, n-1):
#         if mas[x][y-1] < mas[x][y] > mas[x][y+1]:
#             mas[x][y] = 0
# [print(row) for row in mas]

# matrix78

# a = []
# for x in range(m):
#     minv = float('inf')
#     for y in range(n):
#         if minv > mas[x][y]:
#             minv = mas[x][y]
#     a.append(minv)
# print(a)
#
# for i in range(m):
#     for q in range(m):
#         if a[i] < a[q]:
#             a[i], a[q] = a[q], a[i]
#             mas[i], mas[q] = mas[q], mas[i]
# print(a)
# print('8'*20)
# [print(row) for row in mas]

# matrix81

# s = 0
# a = m-1
# for i in range(m):
#     s += mas[i][a]
#     # print(mas[i][a])
#     a -= 1
# print(s/m)

# matrix84

