import random

m = int(input('m = '))
n = int(input('n = '))
mas = []
c = 0
for y in range(m):
    row = []
    for x in range(n):
        row.append(int(input('a=')))
        # row.append(random.randint(1, 9))
        # row.append(c)
        # c += 1
    mas.append(row)
[print(row) for row in mas]
print('**'*20)

# # import random
# #
# # m = int(input('m='))
# # n = int(input('n='))
# # maxv = float('-inf')
# # mas = []
# #
# # for qator in range(m):
# #     row = []
# #     for ustun in range(n):
# #         row.append(random.randint(10, 99))
# #     mas.append(row)
# # [print(row) for row in mas]
# # c = -1
# # for row in mas:
# #     c += 1
# #     d = -1
# #     for i in row:
# #         d += 1
# #         if i > maxv:
# #             maxv = i
# #             a = d
# #             b = c
# # print('row =', b, '; index =', a, '; maxv =', maxv)


# # matrix1
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(10*y)
# #     mas.append(row)
# # [print(row) for row in mas]

# # matrix2
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(5*x)
# #     mas.append(row)
# # [print(row) for row in mas]

# # matrix3
# # m = int(input('m='))
# # n = int(input('n='))
# # m_mas = [random.randint(0,99) for _ in range(m)]
# # mas = []
# # print('m_mas =', m_mas)
# # row = []
# # for y in range(m):
# #     row = [m_mas[y]]
# #     for x in range(1, n):
# #         row.append(m_mas[y])
# #     mas.append(row)
# # [print(row) for row in mas]

# # m = int(input('m='))
# # n = int(input('n='))
# # m_mas = [random.randint(0,99) for _ in range(m)]
# # mas = []
# # print('m_mas =', m_mas)
# # row = []
# # for y in range(m):
# #     mas.append(m_mas)
# # [print(row) for row in mas]

# # # matrix4
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# # m_mas = [random.randint(10,99) for _ in range(n)]
# # print("m_mas =", m_mas)
# # for y in range(m):
# #     row = [m_mas[y]]
# #     for x in range(1, n):
# #         row.append(m_mas[y])
# #     mas.append(row)
# # [print(row) for row in mas]

# # matrix5
# # m = int(input('m='))
# # n = int(input('n='))
# # d = int(input('d='))
# # b = d
# # d_mas = [int(input('a=')) for _ in range(m)]
# # print('d_mas =', d_mas)
# # mas = []
# #
# # for y in range(m):
# #     d = b
# #     row = [d_mas[y]]
# #     for x in range(1, n):
# #         row.append(d_mas[y] + d)
# #         d += b
# #     mas.append(row)
# # [print(row) for row in mas]


# # m = int(input('m='))
# # n = int(input('n='))
# # d = int(input('d='))
# #
# # d_mas = [random.randint(10, 99) for _ in range(m)]
# # print('d_mas =', d_mas)
# #
# # mas = [
# #     [d_mas[y] + d * x for x in range(n)]
# #     for y in range(m)
# # ]
# #
# # for row in mas:
# #     print(row)

# # matrix6

# # m = int(input('m='))
# # n = int(input('n='))
# # q = int(input('q='))
# # b = q
# # m_mas = [random.randint(10, 99) for _ in range(m)]
# # print('m_mas =', m_mas)
# # mas = []
# #
# # for y in range(m):
# #     q = b
# #     row = [m_mas[y]]
# #     for x in range(1, n):
# #         a = m_mas[y] * q
# #         row.append(a)
# #         m_mas[y] = a
# #     mas.append(row)
# # [print(row) for row in mas]

# # matrix7
# # m = int(input('m='))
# # n = int(input('n='))
# # k = int(input('k='))
# # mas = []
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(random.randint(10,99))
# #     if y == k:
# #         a = row
# #     mas.append(row)
# # print('a =', a)

# # matrix8
# # m = int(input('m='))
# # n = int(input('n='))
# # k = int(input('k='))
# # mas = []
# # b = []
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         a = random.randint(10,99)
# #         row.append(a)
# #         if x == k:
# #             b.append(a)
# #     mas.append(row)
# # [print(row) for row in mas]
# # print('b =', b)

# # matrix9
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(random.randint(10,99))
# #     mas.append(row)
# # [print(row) for row in mas]
# # print("**"*20)
# # for i in range(0, len(mas), 2):
# #     print(mas[i])

# # matrix10
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(random.randint(10,99))
# #     mas.append(row)
# # [print(row) for row in mas]
# # print("**"*20)
# # for i in range(1, len(mas), 2):
# #     print(mas[i])

# # matrix11
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(random.randint(10,99))
# #     mas.append(row)
# # [print(row) for row in mas]
# # print("**"*20)
# # q = 0
# # for i in range(m):
# #     if i%2==0:
# #         print(mas[i])
# #     elif i%2==1:
# #         mas[i].reverse()
# #         print(mas[i])

# # matrix12
# # m = int(input('m='))
# # n = int(input('n='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(n):
# #         row.append(random.randint(10, 99))
# #     mas.append(row)
# # [print(row) for row in mas]
# # for i in range(n):
# #     if i%2 == 0:
# #         for q in range(m):
# #             print(mas[q][i], end=' ')
# #     elif i%2 == 1:
# #         for q in range(m-1, -1, -1):
# #             print(mas[q][i], end=' ')

# # matrix13
# # m = int(input('m='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(m):
# #         row.append(random.randint(10, 50))
# #     mas.append(row)
# # [print(row) for row in mas]
# # print('**'*20)

# #
# # for y in range(m):
# #     for x in range(m-y):
# #         print(mas[y][x], end=', ')
# #     print('\t', end=' ')
# #     for x in range(y+1, m):
# #         print(mas[x][m-y-1], end=', ')
# #     print(f'{y=}')


# # m = M
# # i = m-1
# # j = 1
# # for w in range(m//2):
# #     for q in range(j, m):
# #         print(mas[q][i], end=', ')
# #     i -= 1; j += 1; m -= 1

# # j = 0
# # for i in range(m-1, -1, -1):
# #     for q in range(j, m):
# #         print(mas[i][q], end=', ')
# #     m -=1
# #     j += 1

# # i = 0
# # j = 1
# # for w in range(m//2):
# #     for q in range(j, m):
# #         print(mas[q][i], end=', ')
# #     i += 1; j += 1; m -= 1

# # matrix13**2

# # for y in range(m):
# #     for x in range(m-y-1):
# #         print(mas[x][m-y-1], end=' ')
# #     print('\t', end=', ')
# #     for x in range(m-y-1, -1, -1):
# #         print(mas[m-y-1][x], end=', ')
# #     print(f'{y=}')


# # martix13**3

# # for y in range(m):
# #     for x in range(m-y):
# #         print(mas[x][y], end=', ')
# #     print('\t', end=', ')
# #     for x in range(y, m-1):
# #         print(mas[m-y-1][x+1], end=', ')
# #     print(f'{y=}')

# # matrix13**4

# # for y in range(m):
# #     for x in range(m-1, y-1, -1):
# #         print(mas[y][x], end=', ')
# #     print('\t', end=' ')
# #     for x in range(y+1, m):
# #         print(mas[x][y], end=', ')
# #     print(f'{y=}')

# # matrix14
# #
# # m = int(input('m='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(m):
# #         row.append(random.randint(10, 50))
# #     mas.append(row)
# # [print(row) for row in mas]
# # print('**'*20)
# #
# # for y in range(m):
# #     for x in range(m-y):
# #         print(mas[x][y], end=', ')
# #     print('\t', end=', ')
# #     for x in range(y, m-1):
# #         print(mas[m-y-1][x+1], end=', ')
# #     print(f'{y=}')

# # /****************************************
# # m = int(input('m='))
# # mas = []
# #
# # for y in range(m):
# #     row = []
# #     for x in range(m):
# #         row.append(random.randint(10,99))
# #     mas.append(row)
# # [print(row) for row in mas]
# #
# # for y in range(m//2):
# #     for x in range(y, m-y-1):
# #         print(mas[y][x], end=', ')
# #     print('\t', end=' ')
# #     for x in range(y, m-y-1):
# #         print(mas[x][m-y-1], end=', ')
# #     print('\t', end=' ')
# #     for x in range(m-y-1, y, -1):
# #         print(mas[m-y-1][x], end=', ')
# #     print('\t', end=' ')
# #     for x in range(m-y-1, y, -1):
# #         print(mas[x][y], end=', ')
# #     print('\t', end=' ')
# # if m%2 == 1:
# #     print(mas[m//2][m//2])

# #
# ##c = 1
# ##for y in range(m//2):
# ##    for x in range(y, m - y-1):
# ##        mas[y][x] = c
# ##        c += 1
# ##    for x in range(y, m-y-1):
# ##        mas[x][m-y-1] = c
# ##        c += 1
# ##    for x in range(m-y-1, y, -1):
# ##        mas[m-y-1][x] = c
# ##        c += 1
# ##    for x in range(m-y-1, y, -1):
# ##        mas[x][y] = c
# ##        c += 1
# ##if m%2==1:
# ##    mas[m//2][m//2] = m**2
# ##[print(row) for row in mas]


# # matrix16
# ##c = 1
# ##for y in range(m//2):
# ##    for x in range(y, m-y-1):
# ##        mas[x][y] = c
# ##        c += 1
# ##    for x in range(y, m-y-1):
# ##        mas[m-y-1][x] = c
# ##        c += 1
# ##    for x in range(m-y-1, y-1, -1):
# ##        mas[x][m-y-1] = c
# ##        c += 1
# ##    for x in range(m-y-2, y, -1):
# ##        mas[y][x] = c
# ##        c += 1
# ##if m%2==1:
# ##    mas[m//2][m//2] = m**2
# ##[print(row) for row in mas]

# ##matrix17
# ##S1 = 0; S2 = 1; Q = 0
# ##
# ##k = int(input('k='))
# ##for y in range(m):
# ##    if y == k:
# ##        for x in range(n):
# ##            S1 += mas[y][x]
# ##            S2 *= mas[y][x]
# ##            Q = mas[y]
# ##print('Q =', Q)
# ##print('S1 =', S1)
# ##print('S2 =', S2)

# ##matrix18

# ##S1 = 0; S2 = 1;
# ##Q = []
# ##
# ##k = int(input('k = '))
# ##
# ##for y in range(n):
# ##    if y==k:
# ##        for x in range(m):
# ##            S1 += mas[x][y]
# ##            S2 *= mas[x][y]
# ##            Q.append(mas[x][y])
# ##print('Q = ', Q)
# ##print('S1 = ', S1)
# ##print('S2 = ', S2)

# ##matrix19
# ##
# ##for y in range(m):
# ##    S1 = 0; S2 = 1
# ##    for x in range(n):
# ##        S1 += mas[y][x]
# ##        S2 *= mas[y][x]
# ##    print(S1, S2, y)

# ##matrix20

# ##for y in range(n-1):
# ##    S1 = 0; S2 = 1; Q = []
# ##    for x in range(m):
# ##        S1 += mas[x][y]
# ##        S2 *= mas[x][y]
# ##        Q.append(mas[x][y])
# ##    print(Q)
# ##    print(S1, S2, y)

# ##matrix21

# # for y in range(m):
# #     S = 0; Q = []
# #     for x in range(1, n, 2):
# #         S += mas[y][x]
# #         Q.append(mas[y][x])
# #     print(Q)
# #     print(S/(n//2))

# # matrix22
# # for y in range(n):
# #     S = 0; Q = []
# #     for x in range(0, m, 2):
# #         S += mas[x][y]
# #         Q.append(mas[x][y])
# #     print(Q)
# #     print(S)

# # matrix23
# # for y in range(m):
# #     minv = float('inf')
# #     for x in range(n):
# #         if minv > mas[y][x]:
# #             minv = mas[y][x]
# #     print(minv)

# # matrix24
# # for y in range(n):
# #     maxv = float('-inf')
# #     for x in range(m):
# #         if maxv < mas[x][y]:
# #             maxv = mas[x][y]
# #     print(maxv)

# # matrix25
# # maxv = float('-inf')
# # a = 0
# # for y in range(m):
# #     S = 0
# #     for x in range(n):
# #         S += mas[y][x]
# #     if maxv < S:
# #         maxv = S
# #         a = y
# # print(maxv, a)

# # matrix26

# ##minv = float('inf')
# ##a=0
# ##
# ##for y in range(n):
# ##    S = 1
# ##    for x in range(m):
# ##        S *= mas[x][y]
# ##    if minv > S:
# ##        minv = S
# ##        a = y
# ##print(minv, a)


# ##matrix27

# ##minv = float('inf')
# ##Q = []; a = 0
# ##for y in range(m):
# ##    S = 0
# ##    for x in range(n):
# ##        S += mas[y][x]
# ##    if minv > S:
# ##        minv = S
# ##        a = y
# ##Q.append(mas[a])
# ##maxv = float('-inf')
# ##for i in range(n):
# ##    if maxv < Q[0][i]:
# ##        maxv = Q[0][i]
# ##print(Q)
# ##print(maxv)
# ##print(S)

# ##matrix28

# ##maxv = float('-inf')
# ##a = 0; q1 = 0
# ##for y in range(n):
# ##    S = 0; q = []
# ##    for x in range(m):
# ##        S += mas[x][y]
# ##        q.append(mas[x][y])
# ##    if maxv < S:
# ##        maxv = S
# ##        a = y
# ##        q1 = q
# ##minv = float('inf')
# ##for i in range(m):
# ##    if minv > q1[i]:
# ##        minv = q1[i]
# ##print(q1)
# ##print(minv)
# ##print(maxv)

# ##matrix29
# ##q = []
# ##for y in range(m):
# ##    S = 0
# ##    for x in range(n):
# ##        S += mas[y][x]
# ##    q.append(S/n)
# ##print(q)
# ##for y in range(m):
# ##    q1 = []
# ##    for x in range(n):
# ##        if mas[y][x] < q[y]:
# ##            q1.append(mas[y][x])
# ##    print(q1)

# ##matrix30

# ##q = []
# ##for y in range(n):
# ##    s = 0
# ##    for x in range(m):
# ##        s += mas[x][y]
# ##    q.append(s/m)
# ##print(q)
# ##for y in range(n):
# ##    q1 = []
# ##    for x in range(m):
# ##        if mas[x][y] > q[y]:
# ##            q1.append(mas[x][y])
# ##    print(q1)

# ##matrix31

# ##q = []
# ##S = 0
# ##for y in range(m):
# ##    s = 0
# ##    for x in range(n):
# ##        S += mas[y][x]
# ##        s += mas[y][x]
# ##    q.append(round(s/n, 1))
# ##A = round(S/(m*n), 1)
# ##print(q, A)
# ##a = 0
# ##minv = float('inf')
# ##for i in range(m):
# ##    if minv >= abs(A-q[i]):
# ##        minv = abs(A-q[i])
# ##        a = q[i]
# ##        b = i
# ##print(a, b)
# ##q = []
# ##S = 0
# ##for y in range(n):
# ##    s = 0
# ##    for x in range(m):
# ##        S += mas[x][y]
# ##        s += mas[x][y]
# ##    q.append(round(s/n, 1))
# ##A = round(S/(m*n), 1)
# ##print(q, A)
# ##a = 0
# ##minv = float('inf')
# ##for i in range(n):
# ##    if minv >= abs(A-q[i]):
# ##        minv = abs(A-q[i])
# ##        a = q[i]
# ##        b = i
# ##print(a, b)

# ##matrix32
# # f = False
# # for y in range(m):
# #     c1 = 0; c0 = 0
# #     for x in range(n):
# #         if mas[y][x] < 0:
# #             c1 += 1
# #         elif mas[y][x] > 0:
# #             c0 += 1
# #     if c1 == c0:
# #         f = True
# #         a = y
# # if f:
# #     print(a)
# # else:
# #     print("Bunday satr yo'q")

# # matrix33
# # f = False
# # for y in range(n):
# #     c1 = 0; c0 = 0; q=[]; q1 = 0
# #     for x in range(m):
# #         q.append(mas[x][y])
# #         if mas[x][y] < 0:
# #             c1 += 1
# #         elif mas[x][y] > 0:
# #             c0 += 1
# #     print(q)
# #     if c1 == c0:
# #         f = True
# #         a = y
# #         q1 = q
# # if f:
# #     print(a)
# #     print(q1)
# # else:
# #     print("Bunday ustun yo'q")

# # matrix34

# # q = "Bunday satr yo'q"
# # for y in range(m):
# #     c = 0
# #     for x in range(n):
# #         if mas[y][x]%2==0:
# #             c += 1
# #     if c == n:
# #         q = y
# # print(q)

# # matrix35

# # q = "Bunday ustun yo'q"
# #
# # for y in range(n):
# #     c = 0
# #     for x in range(m):
# #         if mas[x][y]%2==1:
# #             c += 1
# #     if c == m:
# #         q = y
# #         break
# # print(q)

# # matrix36
# # S = 0
# # for y in range(1, m):
# #     c = 0
# #     for x in range(n):
# #         if mas[y][x] == mas[0][x]:
# #             c += 1
# #     if c == n:
# #         S += 1
# # print(S)

# # matrix37

# # S = 0
# # for y in range(n):
# #     c = 0
# #     for x in range(m-1, -1, -1):
# #         if mas[x][y] == mas[x][-1]:
# #             c += 1
# #     if c == m:
# #         S += 1
# # print(S-1)

# # matrix38
# # S = 0
# # for i in range(m):
# #     f = True
# #     for q in range(i+1, m):
# #         if mas[i] == mas[q]:
# #             f = False
# #     if f:
# #         S += 1
# # print(S)

# # matrix39

# # mas1 = []
# # for y in range(n):
# #     row = []
# #     for x in range(m):
# #         row.append(mas[x][y])
# #     mas1.append(row)
# # [print(row) for row in mas1]
# #
# # S = 0
# # for i in range(m):
# #     f = True
# #     for q in range(i+1, m):
# #         if mas1[i] == mas1[q]:
# #             f = False
# #     if f:
# #         S += 1
# # print(S)

# # matrix40

# # maxv = float('-inf')
# # a = 0
# # for y in range(m):
# #     for x in range(n):
# #         if mas[y].count(mas[y][x]) > maxv:
# #             maxv = mas[y].count(mas[y][x])
# #             a = y
# #             b = maxv
# #             c = mas[y][x]
# # print(a, c, b)

# # matrix41

# # mas1 = []
# # for y in range(n):
# #     row = []
# #     for x in range(m):
# #         row.append(mas[x][y])
# #     mas1.append(row)
# # [print(row) for row in mas1]
# #
# # maxv = float('-inf')
# # a = 0
# # for y in range(m):
# #     for x in range(n):
# #         if mas1[y].count(mas1[y][x]) > maxv:
# #             maxv = mas1[y].count(mas1[y][x])
# #             a = y
# #             b = maxv
# #             c = mas1[y][x]
# # print(a, c, b)

# # matrix42

# # c = 0
# # for y in range(m):
# #     f = True
# #     for x in range(n-1):
# #         if mas[y][x] >= mas[y][x+1]:
# #             f = False
# #             break
# #     if f:
# #         c += 1
# # print(c)

# # matrix43

# c = 0
# for y in range(n):
#     f = True
#     for x in range(m-1):
#         if mas[x][y] <= mas[x+1][y]:
#             f = False
#             break
#     if f:
#         c += 1
# print(c)

# # matrix44

# S = 0; c3 = 0
# for y in range(m):
#     f = True; c1 = 0; c2 = 0
#     for x in range(n-1):
#         if mas[y][x] < mas[y][x+1]:
#             c1 += 1
#         if mas[y][x] > mas[y][x+1]:
#             c2 += 1
#     if c1 == n-1 or c2 == n-1:
#         print(min(mas[y]))
#     else:
#         c3 += 1
# if c3 == m:
#     print(0)

# matrix45

# mas1 = []
# for i in range(n):
#     row1 = []
#     for q in range(m):
#         row1.append(mas[q][i])
#     mas1.append(row1)
# [print(row1) for row1 in mas1]


# S = 0; c3 = 0
# for y in range(m):
#     f = True; c1 = 0; c2 = 0
#     for x in range(n-1):
#         if mas1[y][x] < mas1[y][x+1]:
#             c1 += 1
#         if mas1[y][x] > mas1[y][x+1]:
#             c2 += 1
#     if c1 == n-1 or c2 == n-1:
#         print(max(mas1[y]))
#     else:
#         c3 += 1
# if c3 == m:
#     print(0)

# matrix46

