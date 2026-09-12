# FunSimple1

# def PowerA3(a):
#     a = a**3
#     return a
#
# A = float(input('A = '))
# B = float(input('B = '))
# C = float(input('C = '))
# D = int(input('D = '))
# E = int(input('E = '))
#
# print(PowerA3(A))
# print(PowerA3(B))
# print(PowerA3(C))
# print(PowerA3(D))
# print(PowerA3(E))

# FunSimple2

# def PowerA234(v):
#     a = v**2
#     b = v**3
#     c = v**4
#     return a, b, c
#
# A = float(input('A = '))
# B = float(input('B = '))
# C = float(input('C = '))
#
# print(PowerA234(A))
# print(PowerA234(B))
# print(PowerA234(C))

# FunSimple3

# def MEAN(v1, v2):
#     a = (v1+v2)/2
#     g = (v1*v2)**.5
#
#     return a, g
#
# A = int(input('A = '))
# B = int(input('B = '))
# C = int(input('C = '))
# D = int(input('D = '))
#
# print(MEAN(A, B))
# print(MEAN(A, C))
# print(MEAN(A, D))

# FunSimple4

# def Triangle(v):
#     S = (3**.5)/4*v**2
#     P = 3*v
#
#     return S, P
# a = int(input('tomon = '))
# print(Triangle(a))

# FunSimple5

# def RectPS(a, b, c, d):
#     X = max(a, c) - min(a, c)
#     Y = max(b, d) - min(b, d)
#     S = X * Y
#     P = (X + Y) * 2
#     return S, P
#
# x1 = int(input('x1 = '))
# y1 = int(input('y1 = '))
# x2 = int(input('x2 = '))
# y2 = int(input('y2 = '))
#
# print(RectPS(x1, y1, x2, y2))

# FunSimple6

# def DigitCountSum(v):
#     mas = []
#     mas.extend(v)
#
#     c = len(mas)
#     s = 0
#     for i in range(c):
#         s += int(mas[i])
#     return c, s
#
# a = input('a = ')
# b = input('b = ')
# c = input('c = ')
#
# print(DigitCountSum(a))
# print(DigitCountSum(b))
# print(DigitCountSum(c))

# FunSimple7

# def InvertDigit(v):
#     mas = []
#     mas.extend(v)
#
#     mas.reverse()
#     c = len(mas)
#     s = ''
#     for i in range(c):
#         s += mas[i]
#
#     return s
#
# a = int(input('a = '))
#
# b = str(a)
#
# print(InvertDigit(b))

# FunSimple8

# def AddRightDigit(v, addon):
#     mas = []
#     mas.extend(v)
#
#     mas.append(addon)
#
#     c = len(mas)
#     s = ''
#     for i in range(c):
#         s += mas[i]
#
#     return s
#
#
# K = int(input('K = '))
# R = int(input('R = '))
#
# K1 = str(K)
# R1 = str(R)
#
# print(AddRightDigit(K1, R1))

# FunSimple9

# def AddLeftDigit(v, addon):
#     mas = []
#     mas.extend(v)
#
#     mas.insert(0, addon)
#
#     c = len(mas)
#     s = ''
#     for i in range(c):
#         s += mas[i]
#
#     return s
#
# K = int(input('K = '))
# R = int(input('R = '))
#
# K1 = str(K)
# R1 = str(R)
#
# print(AddLeftDigit(K1, R1))

# FunSimple10

# def Swap(v1, v2):
#     v1, v2 = v2, v1
#     return v1, v2
#
# A = int(input('A = '))
# B = int(input('B = '))
# C = int(input('C = '))
# D = int(input('D = '))
#
# print(Swap(A, B))
# print(Swap(C, D))

# FunSimple12

# def SortInc(a, b, c):
#     mas = []
#     m = [a, b, c]
#     mas.append(a)
#     mas.append(b)
#     mas.append(c)
#
#     mas.sort()
#
#     a, b, c = mas[0], mas[1], mas[-1]
#     return  a, b, c
#
#
# A1 = int(input('A1 = '))
# B1 = int(input('B2 = '))
# C1 = int(input('C3 = '))
#
# A2 = int(input('A2 = '))
# B2 = int(input('B2 = '))
# C2 = int(input('C2 = '))
#
# print(SortInc(A1, B1, C1))
# print(SortInc(A2, B2, C2))

# FunSimple13

# def SortInc(a, b, c):
#     mas = []
#     m = [a, b, c]
#     mas.append(a)
#     mas.append(b)
#     mas.append(c)
#
#     mas.sort(reverse=True)
#
#     a, b, c = mas[0], mas[1], mas[-1]
#     return  a, b, c
#
#
# A1 = int(input('A1 = '))
# B1 = int(input('B2 = '))
# C1 = int(input('C3 = '))
#
# A2 = int(input('A2 = '))
# B2 = int(input('B2 = '))
# C2 = int(input('C2 = '))
#
# print(SortInc(A1, B1, C1))
# print(SortInc(A2, B2, C2))

# FunSimple14

# def ShiftRight3(a, b, c):
#     a, b, c, = b, c, a
#     return a, b, c
#
# A1 = int(input('A1 = '))
# B1 = int(input('B2 = '))
# C1 = int(input('C3 = '))
#
# A2 = int(input('A2 = '))
# B2 = int(input('B2 = '))
# C2 = int(input('C2 = '))
#
# print(ShiftRight3(A1, B1, C1))
# print(ShiftRight3(A2, B2, C2))

# FunSimple15
#
# def ShiftRight3(a, b, c):
#     a, b, c, = c, a, b
#     return a, b, c
#
# A1 = int(input('A1 = '))
# B1 = int(input('B2 = '))
# C1 = int(input('C3 = '))
#
# A2 = int(input('A2 = '))
# B2 = int(input('B2 = '))
# C2 = int(input('C2 = '))
#
# print(ShiftRight3(A1, B1, C1))
# print(ShiftRight3(A2, B2, C2))

# FunSimple16

# def ishora(v):
#     if v > 0:
#         a = 1
#     elif v == 0:
#         a = 0
#     else:
#         a = -1
#
#     return a
#
# a = int(input('a = '))
# b = int(input('b = '))
#
# print(ishora(a), ishora(b))
# print(ishora(a) + ishora(b))

# FunSimple17

# x = None
# def tenglama(a, b, c):
#     D = b**2-4*a*c
#     if D > 0:
#         x1 = (-1 * b + D**.5)/2*a
#         x2 = (-1 * b - D**.5)/2*a
#         return x1, x2
#     if D == 0:
#         x = -1 * b / 2 * a
#         return x
#     if D < 0:
#         x = None
#         return x
#
# A = int(input('A = '))
# B = int(input('B = '))
# C = int(input('C = '))
#
# print(tenglama(A, B, C))

# FunSimple18

# def CrclS(r):
#     pi = 3.1415
#     S = pi * r**2
#     return S
#
# r1 = int(input('r1 = '))
# r2 = int(input('r2 = '))
# r3 = int(input('r3 = '))
#
# print(CrclS(r1))
# print(CrclS(r2))
# print(CrclS(r3))

# FunSimple19

# def RingS(r):
#     pi = 3.1415
#     S = pi*r**2
#     return S
#
# r1 = int(input('r1 = '))
# r2 = int(input('r2 = '))
#
# print(max(RingS(r1), RingS(r2)) - min(RingS(r1), RingS(r2)))

# FunSimple20

def TriangleP(k1, k2):
    k3 = (k1**2 + k2**2)**.5

    return k3 + k1 + k2

A = int(input('A = '))
B = int(input('B = '))

