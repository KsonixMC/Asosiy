import math
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

##def TriangleP(k1, k2):
##    k3 = (k1**2 + k2**2)**.5
##
##    return k3 + k1 + k2
##
##A = int(input('A = '))
##B = int(input('B = '))
##
##print(TriangleP(A, B))

##FunSimple21

##def SumRange(a, b):
##    if b < a:
##        return 0
##    else:
##        S = 0
##        for i in range(a, b+1):
##            S += i
##        return S
##
##A = int(input('A = '))
##B = int(input('B = '))
##C = int(input('C = '))
##
##print(SumRange(A, B))
##print(SumRange(B, C))

##FunSimple22

##def Calc(A, B, Op):
##    S = 0
##    if Op == 1:
##        S = A - B
##    elif Op == 2:
##        S = A * B
##    elif Op == 3:
##        S = A / B
##    else:
##        S = A + B
##    return S
##
##a = float(input('A = '))
##b = float(input('B = '))
##
##N1 = int(input('N1 = '))
##N2 = int(input('N2 = '))
##N3 = int(input('N3 = '))
##N4 = int(input('N4 = '))
##
##print(Calc(a, b, N1))
##print(Calc(a, b, N2))
##print(Calc(a, b, N3))
##print(Calc(a, b, N4))

##FunSimple23

##def Quarter(x, y):
##    if x > 0 and y > 0:
##        return 1
##    elif x < 0 and y > 0:
##        return 2
##    elif x < 0 and y < 0:
##        return 3
##    elif x > 0 and y < 0:
##        return 4
##    else:
##        return 'no quarter'
##
##px1 = int(input('px1 = '))
##py1 = int(input('py1 = '))
##px2 = int(input('px2 = '))
##py2 = int(input('py2 = '))
##px3 = int(input('px3 = '))
##py3 = int(input('py3 = '))
##px4 = int(input('px4 = '))
##py4 = int(input('py4 = '))
##
##print(Quarter(px1, py1))
##print(Quarter(px2, py2))
##print(Quarter(px3, py3))
##print(Quarter(px4, py4))

##FunSimple24

##def Even(k):
##    if k%2 == 0:
##        return True
##    else:
##        return False
##
##K1 = int(input('k1 = '))
##K2 = int(input('k2 = '))
##K3 = int(input('k3 = '))
##print(Even(K1))
##print(Even(K2))
##print(Even(K3))

##FunSimple25

##def IsSquare(k):
##    if k**.5 == int(k**.5):
##        return True
##    else:
##        return False
##
##K1 = int(input('K1 = '))
##K2 = int(input('K2 = '))
##K3 = int(input('K3 = '))
##
##print(IsSquare(K1))
##print(IsSquare(K2))
##print(IsSquare(K3))

##FunSimple26

##def IsPower5(k):
##    c = 0
##    while k != 1 and k >= 5:
##        k /= 5
##        if k == int(k):
##            c += 1
##    
##    if c == 0:
##        return False
##    else:
##        return True
##
##K1 = int(input('K1 = '))
##K2 = int(input('K2 = '))
##K3 = int(input('K3 = '))
##
##print(IsPower5(K1))
##print(IsPower5(K2))
##print(IsPower5(K3))

##FunSimple27

##def IsPower(k, n):
##    c = 0
##    while k != 0 and k >= n:
##        if k % n != 0:
##            break
##        k //= n
##        c += 1
##    if k == 1:
##        return True
##    else:
##        return False
##
##N = int(input('N = '))
##
##K1 = int(input('K1 = '))
##K2 = int(input('K2 = '))
##K3 = int(input('K3 = '))
##K4 = int(input('K4 = '))
##K5 = int(input('K5 = '))
##
##print(IsPower(K1, N))
##print(IsPower(K2, N))
##print(IsPower(K3, N))
##print(IsPower(K4, N))
##print(IsPower(K5, N))

##FunSimple28

##def IsPrime(n):
##    x = 2
##    a = 0
##    while x < n:
##        if n%x == 0:
##            a = False
##            break
##        else:
##            a = True
##        
##        x += 1
##    else:
##        a = True
##    return a
##            
##k = int(input('k = '))
##
##for i in range(k):
##    a = int(input('a = '))
##    print(IsPrime(a))

##FunSimple29

# def DigitCount(k):
#     a = k.count('')
#     return a-1
# k1 = input('k1 = ')
# k2 = input('k2 = ')
# k3 = input('k3 = ')
# k4 = input('k4 = ')
# k5 = input('k5 = ')

# print(DigitCount(k1))
# print(DigitCount(k2))
# print(DigitCount(k3))
# print(DigitCount(k4))
# print(DigitCount(k5))

# FunSimple30

# def DigitN(k, n):
#     if len(k) < n:
#         return -1
#     else:
#         return k[n-1]

# n = int(input('n = '))
# k1 = input('k1 = ')
# k2 = input('k2 = ')
# k3 = input('k3 = ')

# print(DigitN(k1, n))
# print(DigitN(k2, n))
# print(DigitN(k3, n))

# FunSimple31

# def IsPalindrom(N):
#     def DigitCount(k):
#         a = k.count('')
#         c = a-1
#         return c
#     c = len(N)

#     Answer = '404'
#     for i in range(c//2):
#         if N[i] != N[-i-1]:
#             Answer = False
#             break
#         else:
#             Answer = True
#     return Answer

# K1 = input('K1 = ')
# K2 = input('K2 = ')
# K3 = input('K3 = ')
# K4 = input('K4 = ')
# K5 = input('K5 = ')

# c = 0

# mas = [K1, K2, K3, K4, K5]

# for i in range(5):
#     if IsPalindrom(mas[i]):
#         c += 1
#     else:
#         continue

# print(c)

# FunSimple32

# def DegToRad(d):
#     return d*(3.1415/180)

# print(DegToRad(float(input('D = '))))
# print(DegToRad(float(input('D = '))))
# print(DegToRad(float(input('D = '))))

# FunSimple33

# def RadToDeg(d):
#     return d*(180/3.1415)

# print(RadToDeg(float(input('R = '))))
# print(RadToDeg(float(input('R = '))))
# print(RadToDeg(float(input('R = '))))

# FunSimple34

# def Fact(N):
#     a = 1
#     S = 1
#     while a != N+1:
#         S *= a
#         a += 1
#     return S

# print(Fact(int(input('N = '))))
# print(Fact(int(input('N = '))))
# print(Fact(int(input('N = '))))

# FunSimple35

# def Fact2(N):
#     if N != 0:
#         if N%2 == 0:
#             a = 2
#         else:
#             a = 1
#         b = N
#         while b != a:
#             b -= 2
#             N *= b
#         return N
#     else:
#         return 'None'

# print(Fact2(int(input('N = '))))
# print(Fact2(int(input('N = '))))
# print(Fact2(int(input('N = '))))

# FunSimple36

# def Fib(N):
    
#     a = 0
#     b = 1
#     c = 1

#     for i in range(1, N): 
#         c = a + b
#         a = b
#         b = c

#     return c

# print(Fib(int(input('N = '))))

# FunSimple37

# def Power1(A, B):
#     return A**B

# for i in range(3):
#     print(Power1(float(input(f'A{i+1} = ')), float(input(f'B{i+1} = '))))

# FunSimple38

# def Power2(A, N):
#     if N > 0:
#         S = 'N > 0'
#         A1 = A
#         for i in range(N-1):
#             A *= A1
#         return A

#     if N == 0:
#         S = 'N == 0'
#         return 1.0

#     if N < 0:
#         S = 'N < 0'
#         A1 = A
#         for i in range(N*(-1)-1):
#             A *= A1
#         return 1/A

# print(Power2(float(input('A = ')), int(input('M = '))))
# print(Power2(float(input('A = ')), int(input('N = '))))
# print(Power2(float(input('A = ')), int(input('K = '))))

# FunSimple39

# def Power1(A, N):
#     return A**N

# def Power2(A, N):
#     if N > 0:
#         A1 = A
#         for i in range(int(N)-1):
#             A *= A1
#         return A

#     if N == 0:
#         return 1.0

#     if N < 0:
#         A1 = A
#         for i in range(int(N*(-1))-1):
#             A *= A1
#         return 1/A

# def Power3(A, N):
#     if N % 1 > 0:
#         return Power2(A, N//1)
#     else:
#         return Power1(A, N)

# print(Power3(float(input('A = ')), float(input('N = '))))
# print(Power3(float(input('A = ')), float(input('M = '))))
# print(Power3(float(input('A = ')), float(input('K = '))))

# FunSimple40

# def Exp1(x, eps):
#     S = 1
#     a = 1
#     member = 1.0
#     while True:
#         member = (x**a) / math.factorial(a)
#         if abs(member) <= eps:
#             break
#         S += member
#         a += 1

#     return S

# print(Exp1(float(input('x = ')), float(input('eps1 = '))))
# print(Exp1(float(input('x = ')), float(input('eps2 = '))))
# print(Exp1(float(input('x = ')), float(input('eps3 = '))))

# FunSimple41

# def sin1(x, eps):
#     S = 0
#     a = 1
#     member = 1.0
#     ishora = 1
#     while True:
#         member = (x**a) / math.factorial(a)
#         if abs(member) <= eps:
#             break
#         S += (member*ishora)
#         a += 2
#         ishora *= -1

#     return S

# print(sin1(float(input('x = ')), float(input('eps1 = '))))
# print(sin1(float(input('x = ')), float(input('eps2 = '))))
# print(sin1(float(input('x = ')), float(input('eps3 = '))))

# FunSimple42

# def sin1(x, eps):
#     S = 0
#     a = 0
#     member = 1.0
#     ishora = 1
#     while True:
#         member = (x**a) / math.factorial(a)
#         if abs(member) <= eps:
#             break
#         S += (member*ishora)
#         a += 2
#         ishora *= -1

#     return S

# print(sin1(float(input('x = ')), float(input('eps1 = '))))
# print(sin1(float(input('x = ')), float(input('eps2 = '))))
# print(sin1(float(input('x = ')), float(input('eps3 = '))))

# FunSimple43

# def sin1(x, eps):
#     S = 0
#     a = 1
#     member = 1.0
#     ishora = 1
#     while True:
#         member = (x**a) / a
#         if abs(member) <= eps:
#             break
#         S += (member*ishora)
#         a += 1
#         ishora *= -1

#     return S

# print(sin1(float(input('x = ')), float(input('eps1 = '))))
# print(sin1(float(input('x = ')), float(input('eps2 = '))))
# print(sin1(float(input('x = ')), float(input('eps3 = '))))

# FunSimple44

# def sin1(x, eps):
#     S = 0
#     a = 1
#     member = 1.0
#     ishora = 1
#     while True:
#         member = (x**a) / a
#         if abs(member) <= eps:
#             break
#         S += (member*ishora)
#         a += 2
#         ishora *= -1

#     return S

# print(sin1(float(input('x = ')), float(input('eps1 = '))))
# print(sin1(float(input('x = ')), float(input('eps2 = '))))
# print(sin1(float(input('x = ')), float(input('eps3 = '))))

# FunSimple45

# Solve with tutor

# FunSimple46

# def EKUB(A, B):
#     a = 2
#     mas = [1]
#     while a <= A and a <= B:
#         if A % a == 0 and B % a == 0:
#             mas.append(a)
#             a += 1
#         else:
#             a += 1
#             continue
#     return mas[-1]

# print(EKUB(int(input('A = ')), int(input('B = '))))
# print(EKUB(int(input('A = ')), int(input('C = '))))
# print(EKUB(int(input('A = ')), int(input('D = '))))

# FunSimple47

# def EKUB(A, B):
#     a = 2
#     mas = [1]
#     while a <= A and a <= B:
#         if A % a == 0 and B % a == 0:
#             mas.append(a)
#             a += 1
#         else:
#             a += 1
#             continue
#     return mas[-1]

# def Frac1(a, b):
#     o = EKUB(a, b)
#     return f'{int(a/o)}/{int(b/o)}'

# print(Frac1(int(input('Surat = ')), int(input('Maxraj = '))))
# print(Frac1(int(input('Surat = ')), int(input('Maxraj = '))))
# print(Frac1(int(input('Surat = ')), int(input('Maxraj = '))))

# FunSimple48

# def EKUB(A, B):
#     a = 2
#     mas = [1]
#     while a <= A and a <= B:
#         if A % a == 0 and B % a == 0:
#             mas.append(a)
#             a += 1
#         else:
#             a += 1
#             continue
#     return mas[-1]

# def EKUK(A, B):
#     S = A * B / EKUB(A, B)
#     return S

# print(EKUK(int(input('A = ')), int(input('B = '))))
# print(EKUK(int(input('A = ')), int(input('C = '))))
# print(EKUK(int(input('A = ')), int(input('D = '))))

# FunSimple49

# def EKUB(A, B):
#     a = 2
#     mas = [1]
#     while a <= A and a <= B:
#         if A % a == 0 and B % a == 0:
#             mas.append(a)
#             a += 1
#         else:
#             a += 1
#             continue
#     return mas[-1]

# def EKUB3(A, B, C):
#     S = EKUB(EKUB(A, B), C)
#     return S

# print(EKUB3(int(input('A = ')), int(input('B = ')), int(input('C = '))))
# print(EKUB3(int(input('A = ')), int(input('C = ')), int(input('D = '))))
# print(EKUB3(int(input('A = ')), int(input('B = ')), int(input('D = '))))

# FunSimple50

# def TimeToHMS(T):
#     H = T//3600
#     M = (T%3600)//60
#     S = T%60
#     if H < 10:
#         h = f'0{H}'
#     else:
#         h = H
#     if M < 10:
#         m = f'0{M}'
#     else:
#         m = M
#     if S < 10:
#         s = f'0{S}'
#     else:
#         s = S
#
#     return f'{h}:{m}:{s}'
#
# print(TimeToHMS(int(input('T1 = '))))
# print(TimeToHMS(int(input('T2 = '))))
# print(TimeToHMS(int(input('T3= '))))

# FunSimple51
#
# def IncTime(H, M, S):
#     h = H*3600
#     m = M*60
#     s = S
#
#     return h+m+s
#
# print(IncTime(int(input('H = ')), int(input('M = ')), int(input('S = '))))

# FunSimple52

# def IsLeapYear(Y):
#     if Y % 100 == 0:
#         if Y % 400 == 0:
#             Answer = True
#         else:
#             Answer = False
#     else:
#         if Y % 4 == 0:
#             Answer = True
#         else:
#             Answer = False
#     return Answer
#
# print(IsLeapYear(int(input('Year = '))))
# print(IsLeapYear(int(input('Year = '))))
# print(IsLeapYear(int(input('Year = '))))
# print(IsLeapYear(int(input('Year = '))))
# print(IsLeapYear(int(input('Year = '))))

# FunSimple53

# def IsLeapYear(Y):
#     if Y % 100 == 0:
#         if Y % 400 == 0:
#             Answer = True
#         else:
#             Answer = False
#     else:
#         if Y % 4 == 0:
#             Answer = True
#         else:
#             Answer = False
#     return Answer
#
# def MonthDays(M, Y):
#     if IsLeapYear(Y) == False:
#         match M:
#             case 1:
#                 return 31
#             case 2:
#                 return 28
#             case 3:
#                 return 31
#             case 4:
#                 return 30
#             case 5:
#                 return 31
#             case 6:
#                 return 30
#             case 7:
#                 return 31
#             case 8:
#                 return 31
#             case 9:
#                 return 30
#             case 10:
#                 return 31
#             case 11:
#                 return 30
#             case 12:
#                 return 31
#             case _:
#                 return "out of year"
#     else:
#         match M:
#             case 1:
#                 return 31
#             case 2:
#                 return 29
#             case 3:
#                 return 31
#             case 4:
#                 return 30
#             case 5:
#                 return 31
#             case 6:
#                 return 30
#             case 7:
#                 return 31
#             case 8:
#                 return 31
#             case 9:
#                 return 30
#             case 10:
#                 return 31
#             case 11:
#                 return 30
#             case 12:
#                 return 31
#             case _:
#                 return "out of year"
#
# print(MonthDays(int(input("Month = ")), int(input('Year = '))))

# def IsLeapYear(Y):

#     if Y % 100 == 0:
#         if Y % 400 == 0:
#             Answer = True
#         else:
#             Answer = False
#     else:
#         if Y % 4 == 0:
#             Answer = True
#         else:
#             Answer = False
#     return Answer
#
#
# def MonthDays(M, Y):
#     if M < 1 or M > 12:
#         return "out of year"
#
#     Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if IsLeapYear(Y) and M == 2:
#         return 29
#     else:
#         return Days[M - 1]
#
#
# Y = int(input("Year = "))
# M1 = int(input("M1 = "))
# M2 = int(input("M2 = "))
# M3 = int(input("M3 = "))
#
# print("M1 oyidagi kunlar soni =", MonthDays(M1, Y))
# print("M2 oyidagi kunlar soni =", MonthDays(M2, Y))
# print("M3 oyidagi kunlar soni =", MonthDays(M3, Y))

# FunSimple54

