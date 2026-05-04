import random

##array1
##n = int(input("n="))
##v = []
##for i in range(1,(2*n+1),2):
##    v.append(i)
##print(v)

##array2

##n = int(input('n='))
##v = []
##
##for i in range(n+1):
##    v.append(2**i)
##print(v)

##array3

##n = int(input('n='))
##A = int(input('A='))
##D = int(input('D='))
##v = [A]
##
##for i in range(1, n):
##    A += D
##    v.append(A)
##print(v)
##print(len(v))

##array4

##n = int(input('n='))
##A = int(input('A='))
##D = int(input('D='))
##v = [A]
##
##for i in range(1, n):
##    A*=D
##    v.append(A)
##print(v)
##print(len(v))

##array5

##n = int(input('n='))
##F0 = 1
##F1 = 1
##v = [F0, F1]
##
##for i in range(2, n):
##    F = F0 + F1
##    v.append(F)
##    F0 = F1
##    F1 = F
##print(v)

##array6

##n = int(input('n='))
##A = int(input('A='))
##B = int(input('B='))
##v = [A, B]
##S = 0
##D = A + B
##
##for i in range(2, n):
##    S += D
##    D = S
##    v.append(S)
##print(v)

##array7

# n = int(input('n='))
# v = []
# for i in range(n):
#     a = random.randint(0, 99)
#     v.append(a)
# v.reverse()
# print(v)

# array8

# n = int(input('n='))
# S = 0
# v = []
# for i in range(n):
#     a = random.randint(0,99)
#     if a % 2 == 1:
#         v.append(a)
#         S += 1
# print(v)
# print('S=',S)

# array9
#
# n = int(input('n='))
# S = 0
# v = []
# v1 = []
# for i in range(n):
#     a = random.randint(0,99)
#     v1.append(a)
#     if a % 2 == 0:
#         v.append(a)
#         S += 1
# print(v1)
# print(v[::-1])
# print('S=',S)

# array10

# n = int(input('N='))
# S = 0
# v = []
# v1 = []
# v2 = []
# for i in range(n):
#     a = random.randint(0,99)
#     v2.append(a)
#     if a % 2 == 0:
#         v.append(a)
#     if a % 2 == 1:
#         v1.append(a)
# print(v2)
# print(v)
# print(v1[::-1])

# array11

# n = int(input('n='))
# K = int(input('K='))
# v = []
#
# for i in range(n):
#     a = random.randint(0, 99)
#     v.append(a)
# print(v)
# print(v[::K])

# array12

# n = int(input('n='))
# v = []
# for i in range(n):
#     a = random.randint(0, 99)
#     v.append(a)
# print(v)
# print(v[::2])

# ..........

# array 18

# n = int(input('n='))
# v = []
#
# for i in range(n):
#     a = random.randint(0,99)
#     v.append(a)
#     minv = v[-1]
# print('v-1=',v[-1])
# for i in range(n):
#     if minv > v[i]:
#         minv = v[i]
# print(v)
# print(minv)

# array19
#
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     a = random.randint(0, 99)
#     v.append(a)
#     minv = v[-1]
#     maxv = v[0]
# for i in range(n):
#     if minv > v[i]:
#         minv = v[i]
#         break
# for i in range(n):
#     if maxv < v[i]:
#         maxv = v[i]
# print(v)
# print('first little one than -1 is', minv)
# print('last big one than 0 is', maxv)

# array20

# n = int(input('n='))
# K = int(input('K='))
# L = int(input('L='))
# v = []
# S = 0
# for i in range(n):
#     v.append(random.randint(0,99))
#     if K<i<L:
#         S += v[i]
# print(v)
# print(S)

# array21

# n = int(input('n='))
# K = int(input('K='))
# L = int(input('K='))
# v = []
# S = 0
# D = 0
# for i in range(n):
#     v.append(random.randint(0,99))
#     if K<i<L:
#         S += v[i]
#         D += 1
# print(v)
# print(S/D)

# ----------------------------------------

# array112
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0, 99))
# print(v)
# for i in range(n):
#     for j in range(n-1):
#         if v[j] > v[j+1]:
#             v[j], v[j+1] = v[j+1], v[j]
# print(v)

# array113

# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# for i in range(n):
#     for j in range(n):
#         if v[i] < v[j]:
#             v[i], v[j] = v[j], v[i]
#     print(v)

# array25
# import random
# n = int(input())
# a = []
# for i in range(n):
#     a.append(random.randint(1, 10))
# print(a)
#
# q = a[1] / a[0]
# gp = True
#
# for i in range(2, n):
#     if a[i] / a[i-1] != q:
#         gp = False
#         break
#
# if gp:
#     print(q)
# else:
#     print(0)

# array26
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# f = True
# for i in range(n-1):
#     if v[i]%2 == v[i+1]%2:
#         f = False
#         break
# if f:
#     print(0)
# else:
#     print(i+1)

# array27
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(int(input('a=')))
# print(v)
# f = True
# for i in range(n-1):
#     if (v[i]>0 and v[i+1]>0) or (v[i]<0 and v[i+1]<0):
#         f = False
#         break
# if f:
#     print(0)
# else:
#     print(f, i+1)

# array28
# n = int(input('n='))
# minv = float('inf')
# v = []
#
# for i in range(n):
#     v.append(int(input('a=')))
# print(v)
#
# for i in range(0, n, 2):
#     if minv > v[i]:
#         minv = v[i]
# print(minv)

# array29
# n = int(input('n='))
# maxv = float('-inf')
# v = []
#
# for i in range(n):
#     v.append(int(input(f'a{i}=')))
# print(v)
#
# for i in range(1, n, 2):
#     if maxv < v[i]:
#         maxv = v[i]
# print(maxv)

# array30
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# S = 0
# for i in range(n-1):
#     if v[i] > v[i+1]:
#         S += 1
#         print(i)
# print('S =', S)

# array31
# n = int(input('n='))
# v = []
# S = 0
# d = []
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# S = 0
# for i in range(n-1):
#     if v[i] < v[i-1]:
#         S += 1
#         d.append(i)
# d.reverse()
# print(d)
# print(S)

# array32
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
#
# for i in range(n-1):
#     if v[i-1] < v[i] > v[i+1]:
#         S = i
# print(S)

# array34
# n = int(input('n='))
# minv = float('-inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
#
# for i in range(1,n-1):
#     if v[i-1]>v[i]<v[i+1]:
#         if minv < v[i]:
#             minv = v[i]
# print('min =', minv)

# array35
# n = int(input('n='))
# maxv = float('inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
#
# for i in range(1, n-1):
#     if v[i-1] < v[i] > v[i+1]:
#         print(v[i])
#         if maxv > v[i]:
#             maxv = v[i]
# print('max =', maxv)

# array36
# n = int(input('n='))
# maxv = float('-inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
#
# for i in range(n-1):
#     if v[i-1] < v[i] < v[i+1] or v[i-1] > v[i] > v[i+1]:
#         print(v[i])
#         if maxv < v[i]:
#             maxv = v[i]
# print('max =', maxv)

# array37
# n = int(input('n='))
# v = [1, 2, 3,4,5,6,7,-1,0,3,-5,3, 5, 7, 0, 12, 24, 36]
# n = len(v)
#
# for i in range(n):
#     v.append(int(input(f'a{i+1}=')))
# print(v)
# q = v[1] - v[0]
# c = 2
# oraliq_soni = 0
# for x in range(2, n):
#     if v[x] - v[x-1] == q and x < n-1:
#         c += 1
#     else:
#         if c >= 3:
#             oraliq_soni += 1
#         c = 2
#         q = v[x] - v[x-1]
# print(oraliq_soni)

# oraliq_soni = 0
# for x in range(2, n-1):
#     q0 = v[x] - v[x-1]
#     q1 = v[x-1] - v[x-2]
#     if q0 == q1 and v[x+1] - v[x] != q0 or x==n-2:
#         print(x, q0, q1, v[x+1] - v[x])
#         oraliq_soni += 1
# print(oraliq_soni)

#
# v = [1, 2, 3,4,5,6,7,-1,0,3,-5,3, 5, 7, 0, 12, 24, 36]
# n = len(v)
# print(v)
#
# q = v[1] - v[0]
# c = 2
# S = 0
#
# for i in range(2, n-1):
#     if v[i] - v[i-1] == q:
#         c += 1
#     else:
#         if c >= 3:
#             S += 1
#         c = 2
#         q = v[i] - v[i-1]
# if c >= 3:
#     S += 1
# print(S)


# array38

# v = [9,8,7,6,5,1,0,-1,-2,0,9,1,2,10,5,0,1]
# n = len(v)
# print(v)
#
# S = 0
# q = v[0] - v[1]
# c = 0
#
# for i in range(2, n-1):
#     print('i =', i)
#     if v[i+1] - v[i] == q:
#         c += 1
#     else:
#         if c >= 3:
#             print(v[i], v[i+1])
#             S += 1
#         c = 2
#         q = v[i+1] - v[i]
# if c>=3:
#     S += 1
#
# print(S)

# array39
# v = [10, 9, 8, 7, 8 ,9 ,10, 0 ,-10, -20, 1, 3, 4, 5, 6, 10, 7, 6, 5, 4]
# n = len(v)
# print(v)
#
# S = 0
# q1 = v[1] - v[0]
# q2 = v[0] - v[1]
# q = v[1] - v[0]
# c = 0
# c1 = c2 = 0
#
# for i in range(1, n):
#     if v[i] - v[i-1] == q1:
#         c += 1
#     elif v[i-1] - v[i] == q2:
#         c += 1
#     else:
#         if c >= 3:
#             S += 1
#         c = 2
#         q1 = v[i] - v[i-1]
#         q2 = v[i+1] - v[i]
# if c >= 3:
#     S += 1
# print(S)

# v = [10, 9, 8, 7, 8 ,9 ,10, 0 ,-10, -20, 1, 3, 4, 5, 6, 10, 7, 6, 5, 4]
#
# n = len(v)
# S = 0
# c = 1
# print(v)
#
# for i in range(1, n):
#     if (v[i] - v[i-1]) * (v[i-1] - v[i-2] if i > 1 else 1) > 0:
#         c += 1
#     else:
#         if c >= 3:
#             S += 1
#         c = 2
#
# if c >= 3:
#     S += 1
#
# print(S)

# array40
# n = int(input('n='))
# R = float(input('R='))
# minv = float('inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# a = 0
# for i in range(n):
#     if minv > abs(R - v[i]):
#         minv = abs(R - v[i])
#         a = v[i]
# print(a)

# array41
# n = int(input('n='))
# maxv = float('-inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# a = b = 0
# for i in range(n-1):
#     if maxv < v[i] + v[i+1]:
#         maxv = v[i] + v[i+1]
#         a = v[i]
#         b = v[i+1]
# print(a, b)

# array42
# n = int(input('n='))
# R = float(input('R='))
# minv = float('inf')
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
#
# a = b = 0
#
# for i in range(n-1):
#     if minv > abs(R - (v[i] + v[i+1])):
#         minv = abs(R - (v[i] + v[i+1]))
#         a = v[i]
#         b = v[i+1]
# print(a, b)

# array43
# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(random.randint(0,99))
# v.sort()
# print(v)
# S = 0
#
# for i in range(n):
#     if v[i-1] != v[i]:
#         S += 1
# print(S)

# array44
# n = int(input('n='))
# v = []
# d = []
# q = []
# S = 0
# for i in range(n):
#     a = int(input('a='))
#     v.append(a)
#     if v.count(a) == 2:
#         d.append(v.index(a))
#         d.append(i)
#         q.append(a)
#         S += 1
# for i in range(S):
#     print(q[i], ' soni')
# for i in range(S*2):
#     print(d[i])

# n = int(input('n='))
# v = []
#
# for i in range(n):
#     v.append(int(input(f'a{i+1}=')))
# print(v)
#
# for d in range(n):
#     for q in range(d+1, n):
#         if v[d] == v[q]:
#             print(v[d], d ,q)

# array45
# n = int(input('n='))
# v = []
# minv = float('inf')
#
# for i in range(n):
#     v.append(random.randint(0,99))
# print(v)
# a = b = 0
# for i in range(n-1):
#     if minv > abs(v[i] - v[i+1]):
#         minv = abs(v[i] - v[i+1])
#         print('minv =', minv)
#         a = v[i]
#         b = v[i+1]
# print(a,b)

# array46
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# minv = float('inf')
# R = int(input('R='))
# print(v)
# a = b = 0
# for i in range(n):
#     for q in range(i+1, n):
#         print(v[i], v[q])
#         if minv > abs(R - (v[i] + v[q])):
#             minv = abs(R - (v[i] + v[q]))
#             a = v[i]
#             b = v[q]
# print('main',a, b)

# array47
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# for i in range(n):
#     f = True
#     for q in range(i+1, n):
#         if v[i] == v[q]:
#             f = False
#     if f:
#         print(v[i], end=" ")

# array48
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# maxv = float('-inf')
# print(v)
# a = 0
# for i in range(n):
#     S = 0
#     for q in range(i+1, n):
#         if v[i] == v[q]:
#             S += 1
#     if maxv < S:
#         maxv = S
#         a = v[i]
# print(a)

# array49
##n = int(input('n='))
##v = [random.randint(0,99) for _ in range(n)]
##print(v)
##
##for i in range(n):
##    print('i =', i, f'v{i} =', v[i])
##    if v.count(v[i]) != 1 or v[i] > n:
##        print('error is ', i, v[i])
##        break

##array50
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# S = 0
# for i in range(n-1):
#     if v[i] > v[i+1]:
#         print(v[i], ' > ', v[i+1])
#         S += 1
# print(S)

# array51
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = [random.randint(0,99) for _ in range(n)]
# print(a)
# print(b)
# print('='*40)
# c = b.copy()
# b = a.copy()
# print(c)
# print(b)

# array52
# n = int(input('n='))
# a = [random.randint(0,20) for _ in range(n)]
# print(a)
# b = []
# for i in range(n-1):
#     if a[i] < 5:
#         b.append(2*a[i])
#         print('2 *', a[i])
#     else:
#         b.append(a[i]/2)
#         print(a[i], '/ 2')
# print(b)

# array53
# n = int(input('n='))
# a = [random.randint(0,20) for _ in range(n)]
# b = [random.randint(0,20) for _ in range(n)]
# print(a)
# print(b)
# c = []
# for i in range(n):
#     if a[i] > b[i]:
#         c.append(a[i])
#     else:
#         c.append(b[i])
# print(c)

# array54
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = []
# print(a)
# for i in range(n):
#     if a[i]%2 == 0:
#         b.append(a[i])
# print(len(b))
# print(b)

# array55
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = []
# print(a)
#
# for i in range(1, n, 2):
#     b.append(a[i])
# print(b)
# print(len(b))

# array56
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = []
# print(a)
#
# for i in range(3, n, 3):
#     b.append(a[i])
# print(b)
# print(len(b))

# array57
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = []
# print(a)
# for i in range(0, n, 2):
#     b.append(a[i])
# for i in range(1, n, 2):
#     b.append(a[i])
# print(b)

# array58
# n = int(input('n='))
# a = [random.randint(0,9) for _ in range(n)]
# b = []
# print(a)
# for i in range(n):
#     S = 0
#     for q in range(0, i+1):
#         S += a[q]
#     b.append(S)
# print(b)

# array59
# n =  int(input('n='))
# a = [random.randint(0,9) for _ in range(n)]
# b = []
# print(a)
# for i in range(n):
#     S = 0
#     for q in range(0, i+1):
#         S += a[q]
#     if i == 0:
#         b.append(0/S)
#     else:
#         b.append(S / i)
# print(b)

# array60
# n = int(input('n='))
# a = [random.randint(0,9) for _ in range(n)]
# b = []
# print(a)
#
# for i in range(n):
#     S = 0
#     for q in range(i, n-1):
#         S += a[q]
#     b.append(S)
# print(b)

# array61
# n = int(input('n='))
# a = [random.randint(0,9) for _ in range(n)]
# b = []
# print(a)
#
# for i in range(n):
#     S = 0
#     d = 0
#     for q in range(i, n):
#         S += a[q]
#         d += 1
#     b.append(S/d)
# print(b)

# array62
# n = int(input('n='))
# a = [random.randint(-10, 10) for _ in range(n)]
# b = []
# c = []
# print(a)
# for i in range(n):
#     if a[i] > 0:
#         b.append(a[i])
#     elif a[i] < 0:
#         c.append(a[i])
# print(len(b), b)
# print(len(c), c)

##array63
##n = 5
##a = [random.randint(0, 15) for _ in range(n)]
##b = [random.randint(10, 20) for _ in range(n)]
##a.sort()
##b.sort()
##print(a)
##print(b)
##c = []
##while a or b:
##    if a and not b:
##        c.append(a.pop(0))
##    elif b and not a:
##        c.append(b.pop(0))
##    elif a[0] < b[0]:
##        c.append(a.pop(0))
##    else:
##        c.append(b.pop(0))
##print(c)
##print(len(c))


# array64
##n = int(input('n='))
##a = [random.randint(0,5) for _ in range(n)]
##b = [random.randint(5, 10) for _ in range(n)]
##c = [random.randint(10, 15) for _ in range(n)]
##a.sort()
##b.sort()
##c.sort()
##print(a)
##print(b)
##print(c)
#
# while a or b or c:
#     if a and not b and not c:
#         d.append(a.pop(0))
#     elif not a and b and not c:
#         d.append(b.pop(0))
#     elif not a and not b and c:
#         d.append(c.pop(0))
#     elif a and b and not c:
#         if a[0] <= b[0]:
#             d.append(a.pop(0))
#         else:
#             d.append(b.pop(0))
#     elif a and not b and c:
#         if a[0] <= c[0]:
#             d.append(a.pop(0))
#         else:
#             d.append(c.pop(0))
#     elif not a and b and c:
#         if b[0] <= c[0]:
#             d.append(b.pop(0))
#         else:
#             d.append(c.pop(0))
#
#     elif a[0] <= b[0] <= c[0] or a[0] <= c[0] <= b[0]:
#         d.append(a.pop(0))
#     elif b[0] <= a[0] <= c[0] or b[0] <= c[0] <= a[0]:
#         d.append(b.pop(0))
#     else:
#         d.append(c.pop(0))
# print(d)
# print('len =', len(d))

# array65
# n = int(input('n='))
# k = int(input('k='))
# a = [random.randint(0,99) for _ in range(n)]
# print(a)
# b = a[k]
# for i in range(n):
#     print('i =', i)
#     d = a[i] + b
#     print('d =', a[i], '+', b)
#     print('d =', d)
#     a.pop(i)
#     a.insert(i, d)
#     print('a =', a)
# print(a)

# n = int(input('n='))
# k = int(input('k='))
# a = [random.randint(0,99) for _ in range(n)]
# print(a)
# b = a[k]
#
# for i in range(n):
#     a[i] = a[i] + b
# print(a)

# array66
# n = int(input('n='))
# v = [random.randint(0,99) for _  in range(n)]
# print(v)
# for i in range(n):
#     if v[i]%2 == 0:
#         b = v[i]
#         break
# for i in range(n):
#     if v[i]%2 == 0 and v[i] != 0:
#         v[i] = v[i] + b
# print(v)

# array67
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# for i in range(n):
#     if v[i]%2 == 1:
#         b = v[i]
# print('b =', b)
# for i in range(n):
#     if v[i]%2 == 1:
#         v[i] = v[i] + b
# print(v)

# array68
# n = int(input('n='))
# maxv = float('-inf')
# minv = float('inf')
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n):
#     if maxv < v[i]:
#         maxv = v[i]
#     if minv > v[i]:
#         minv = v[i]
# print(minv, maxv)
# for i in range(n):
#     if v[i] == minv:
#         v[i] = maxv
#     elif v[i] == maxv:
#         v[i] = minv
# print(v)

# array69
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(0, n, 2):
#     v[i], v[i+1] = v[i+1], v[i]
# print(v)

# array70
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# b = n//2
# for i in range(b):
#     v[i], v[b+i] = v[b+i], v[i]
# print(v)

# array71
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# b = -1
# for i in range(n//2):
#     v[i], v[b] = v[b], v[i]
#     b -= 1
# print(v)

# array72
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# h = int(input('h='))
# print(a)
# for i in range(int(((h+1) - (k-1)) / 2)):
#     a[k], a[h] = a[h], a[k]
#     k += 1
#     h -= 1
# print(a)

# while k < h:
#     a[k], a[h] = a[h],a[k]
#     k += 1
#     h -= 1
# print(a)

# array73
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# h = int(input('h='))
# k += 1
# h -= 1
# print(a)
# while k < h:
#     a[k], a[h] = a[h],a[k]
#     k += 1
#     h -= 1
# print(a)

# array74
# n = int(input('n='))
# a = [random.randint(0,50) for _ in range(n)]
# maxv = float('-inf')
# minv = float('inf')
# print(a)
# for i in range(n):
#     if maxv <= a[i]:
#         maxv = a[i]
#         maxv_i = i
#     if minv > a[i]:
#         minv = a[i]
#         minv_i = i
# if minv_i < maxv_i:
#     x = minv_i+1
#     z = maxv_i
# else:
#     x = maxv_i+1
#     z = minv_i
# for i in range(x, z):
#     a[i] = 0
# print(a)

# array75
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# maxv = float('-inf')
# minv = float('inf')
# print(a)
# for i in range(n):
#     if minv > a[i]:
#         minv = a[i]
#         minv_i = i
#     if maxv < a[i]:
#         maxv = a[i]
#         maxv_i = i
# if minv_i < maxv_i:
#     x,z = minv_i, maxv_i
# else:
#     x,z = maxv_i, minv_i
# for i in range(int(abs((z+1)-x)/2)):
#     a[x], a[z] = a[z], a[x]
#     x += 1
#     z -= 1
# print(a)

# array76
# n = int(input('n='))
# a = [random.randint(0,99) for _ in range(n)]
# b = []
# print(a)
# for i in range(1, n-1):
#     if a[i-1] < a[i] > a[i+1]:
#         b.append(i)
# for i in b:
#     a[i] = 0
# print(a)

# array77
# n = int(input('n='))
# a = [random.randint(0,50) for _ in range(n)]
# b = []
# print(a)
#
# for i in range(1,n-1):
#     if a[i-1] > a[i] < a[i+1]:
#         b.append(i)
# for i in b:
#     a[i] = a[i]**2
# print(a)

# array78
# n = int(input('n='))
# a = [random.randint(0,50) for _ in range(n)]
# print(a)
#
# for i in range(n-1):
#     # print(f'({a[i]} + {a[i+1]})/2 =', (a[i]+a[i+1])/2)
#     a[i] = (a[i] + a[i+1])/2
# print(a)

# array79
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-1, 0, -1):
#     v[i] = v[i-1]
# v[0] = 0
# print(v)

# array80
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-1):
#     v[i] = v[i+1]
# v[-1] = 0
# print(v)

# array81
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# print(v)
# for i in range(n-1, k-1, -1):
#     v[i] = v[i-k]
# for q in range(0, k):
#     v[q] = 0
# print(v)

# array82
# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-k):
#     v[i] = v[i+k]
# for q in range(n-k, n):
#     v[q] = 0
# print(v)

# array83
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# a = v[n-1]
# for i in range(n-1, -1, -1):
#     if i == 0:
#         v[i] = a
#     else:
#         v[i] = v[i-1]
# print(v)

# array84
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# a = v[0]
# for i in range(n-1):
#     v[i] = v[i+1]
# v[n-1] = a
# print(v)

# array85
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# a = []
# b = 0
# print(v)
#
# for i in range(n-1, n-k-1, -1):
#     a.insert(0, v[i])
# for i in range(n-1, -1, -1):
#     v[i] = v[i-k]
# if a:
#     for q in a:
#         v[b] = a[b]
#         b += 1
# print(v)

# array86
# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0,99) for _ in range(n)]
# a = []
# print(v)
# for i in range(k):
#     a.append(v[i])
# for i in range(n-k):
#     v[i] = v[i+k]
# q = 0
# for i in range(n-k, n):
#     v[i] = a[q]
#     q += 1
# print(v)

# --------------------------------

# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0, 99) for _ in range(n)]
# print(v)
#
# v = v[k:] + v[:k]
#
# print(v)


# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# v = v[n-k:] + v[:n-k]

# print(v)

# -------------------------------------------------

# array87
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n-1)]
# v.sort()
# v.insert(0,int(input('v0 =')))
# print(v)
# b = v[0]
# for i in range(1, n-1):
#     if v[i] < v[0] <v[i+1]:
#         v.pop(0)
#         v.insert(i, b)
#     elif v[0] > v[-1]:
#         v.pop(0)
#         v.append(b)
# print(v)

# array88
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n-1)]
# v.sort()
# v.append(int(input(f'v[{n-1}]=')))
# b = v[-1]
# if n == 2:
#     if v[-1] < v[0]:
#         v[-1], v[0] = v[0], v[-1]
# elif n >= 3:
#     for i in range(n - 2, 0, -1):
#         if v[i - 1] < v[-1] < v[i]:
#             v.pop(-1)
#             v.insert(i, b)
#         elif v[-1] < v[0]:
#             v.pop(-1)
#             v.insert(0, b)
# print(v)

# array89
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n-1)]
# v.sort()
# v.insert(random.randint(1, 5), int(input('a=')))
# print(v)
#
# for i in range(n):
#     for j in range(n-1):
#         if v[j] > v[j+1]:
#             v[j], v[j+1] = v[j+1], v[j]
# print(v)

# array90
# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0,99) for _ in range(n)]
# v.pop(k)
# print(v)



# array87 -------------------------------------

# n = 10
# v = []
#
# for _ in range(n-1):
#     v.append(int(random.randint(0,90)))
# v.sort()
# v.insert(0, int(input('birinchisi=')))
# print(v)
#
# if v[0] > v[-1]:
#     v.append(v.pop(0))
# else:
#     for x in range(2, n):
#         if v[x-1] <= v[0] <= v[x]:
#             v.insert(x, v[0])
#             v.pop(0)
#             break
# print(v)
# a = v[0]
# for x in range(1, n):
#     if a < v[x]:
#         v[x-1] = a
#         break
#     else:
#         v[x-1] = v[x]
# else:
#     v[-1] = a
# print(v)

# for x in range(1, n):
#     if a < v[x]:
#         break
# print(x)
# if a > v[-1]: v = v[1:] + [a]
# else: v = v[1:x] + [a] + v[x:]
# print(v)

# -------------------------------------------------------

# array91
# n = int(input('n='))
# k = int(input('k='))
# m = int(input('m='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(m, k+1, -1):
#     v.pop(i)
# print(v, len(v)

# array92
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-1, 0, -1):
#      if v[i]%2 == 1:
#          v.pop(i)
# print(v, len(v))

# array93
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-1, 0, -1):
#     if v[i]%2 == 0:
#         v.pop(i)
# print(v)

# array94
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# a = v.copy()
#
# for i in range(1, n, 2):
#     a.pop(i)
# print(a)

# n = int(input("n="))
# # arr = list(map(int, input("Elementlarni kiriting: ").split()))
# arr = [random.randint(0,99) for _ in range(n)]
# print(arr)
#
# natija = [arr[i] for i in range(0, n, 2)]  # step=2 -> juft indekslar
#
# print("Elementlar soni:", len(natija))
# print("Massiv:", natija)

# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# a = []
#
# for i in range(0, n, 2):
#     a.append(v[i])
# print(len(a))
# print(a)

# array95
# n = int(input('n='))
# v = [random.randint(0, 10) for _ in range(n)]
# print(v)
#
# for i in range(n-1):
#     if v[i] == v[i+1]:
#         v.pop(i)
# print(v)

# array96 ???
# n = int(input('n='))
# v = [random.randint(0,10) for _ in range(n)]
# print(v)
# a = []
#
# for i in range(n):
#     f = 1
#     for j in range(n):
#         if v[i] == v[j]:
#             f += 1
#             if f > 2:
#                 break
#     if f < 3:
#         a.append(v[i])
# print(a)

#

# n = int(input('n=')) ???
# v = [random.randint(0, 10) for _ in range(n)]
# a = []
# print(v)
# c = 0
# for i in range(n):
#     if v.count(v[i]) > 1:
#         c += 1
#         if c == 1:
#             a.append(v[i])
#             b = v.index(v[i], i, n)
#     if v.count(v[i]) == 1:
#         a.append(v[i])
#         # a.append(v[b])
# print(a)

# n = int(input('n=')) ???
# v = [random.randint(0,10) for _ in range(n)]
# v = [9, 8, 5, 0, 3, 2, 2, 9, 7, 3, 9, 1]
# n = len(v)
# d = v.copy()
# a = []
# print(v)
# c = 0
# for i in range(n):
#     if v.count(v[i]) > 1:
#         c += 1
#         if c == 1:
#             a.append(v[i])
#             b = v.index(v[i], i+1, n)
#         else:
#             d[i] = 'z'
# s = 0
# for i in range(b):
#     if d[i] == str:
#         s += 1
# d.insert(abs(s-b), v[b])
#
# while d.count('z') != 0:
#     d.remove('z')
# print(d)

# array96
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n):
#     for j in range(i+1, n):
#         if v[i] == v[j]:
#             v[j] = 'z'
# while v.count('z') != 0:
#     v.remove('z')
# print(v)

# array97
# n = int(input('n='))
# v = [random.randint(0,10) for _ in range(n)]
# print(v)
#
# for i in range(n):
#     for j in range(i+1, n):
#         if v[i] == v[j]:
#             v[i] = 'z'
# while v.count('z') != 0:
#     v.remove('z')
# print(v)

# array98
# n = int(input('n='))
# v = [random.randint(0,5) for _ in range(n)]
# a = []
# print(v)
# for i in range(n):
#     c = 0
#     for j in range(n):
#         if v[i] == v[j]:
#             c += 1
#             if c >= 3:
#                 a.append(v[i])
# print(a)

# array99
# n = int(input('n='))
# v = [random.randint(0,5) for _ in range(n)]
# print(v)
# a = []
# for i in range(n):
#     c = 0
#     for j in range(n):
#         if v[i] == v[j]:
#             c += 1
#     if c <= 2:
#         a.append(v[i])
# print(a)
# print(len(a))

# array100
# n = int(input('n='))
# v = [random.randint(0,6) for _ in range(n)]
# print(v)
# a = []
# for i in range(n):
#     c = 0
#     for j in range(n):
#         if v[i] == v[j]:
#             c += 1
#     if c != 2:
#         a.append(v[i])
# print(a)

# array101
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# print(v)
#
# for i in range(n-1):
#     if i == k:
#         v.insert(i, 0)
# print(v)

# array102
# n = int(input('n='))
# k = int(input('k='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
#
# for i in range(n-1):
#     if i == k:
#         v.insert(i+1, 0)
# print(v)

# array103
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# print(v)
# minv = float('inf')
# maxv = float('-inf')
#
# for i in range(n-1):
#     if minv > v[i]:
#         minv = v[i]
#         a = i
#     if maxv < v[i]:
#         maxv = v[i]
#         b = i
# v.insert(a, 0)
# v.insert(b+1, 0)
# print(minv, maxv)
# print(v)

# array104
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# m_mas = [random.randint(0, 0) for _ in range(int(input('m=')))]
# print(v)
#
# for i in range(n-1):
#     if i == k:
#         for q in m_mas:
#             v.insert(i, q)
# print(v)

# array105
# n = int(input('n='))
# v = [random.randint(0,99) for _ in range(n)]
# k = int(input('k='))
# m = int(input('m='))
# m_mas = [random.randint(0,0) for _ in range(m)]
# print(v)
#
# for i in range(n):
#     if i == k:
#         for q in m_mas:
#             v.insert(i+1, q)
# print(v)

# array106
# n = int(input('n='))
# v = [random.randint(10, 99) for _ in range(n)]
# print(v)
# a = []
#
# for i in range(0, n, 2):
#     a.append(v[i])
# print(a)
# v.extend(a)
# print(v)

# array107
# n = int(input('n='))
# v = [random.randint(10, 99) for _ in range(n)]
# print(v)
# a = []
# for i in range(1, n, 2):
#     a.append(v[i])
# print(a)
# m = len(a)
#
# for x in range(m-1):
#     v.append(a[x])
#     v.append(a[x])
# print(v)

# array108
# n = int(input('n='))
# v = [random.randint(-50, 50) for _ in range(n)]
# print(v)
# a = v.copy()
#
# for i in range(n-1, -1, -1):
#     if v[i] > 0:
#         a.insert(i, 0)
# print(a)

# array109
# n = int(input('n='))
# v = [random.randint(-50, 50) for _ in range(n)]
# print(v)
# a = v.copy()
#
# for i in range(n-1, 0, -1):
#     if v[i] < 0:
#         a.insert(i+1, 0)
# print(a)

# arry110
# n = int(input('n='))
# v = [random.randint(10, 99) for _ in range(n)]
# print(v)
# a = []
#
# for i in range(n):
#     if v[i] % 2 == 0:
#         a.append(v[i])
# v.extend(a)
# print(v)

# array111
# n = int(input('n='))
# v = [random.randint(10, 99) for _ in range(n)]
# print(v)
# a = []
# for i in range(n):
#     if v[i]%2 == 1:
#         a.append(v[i])
# print(a)
# v.extend(a)
# print(v)

