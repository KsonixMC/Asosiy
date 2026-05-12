# ~~~~~~~~~1~~~~~~~~~~

# l, r = map(int, input().split())
# for i in range(l, r+1):
#     a =

# l, r = map(int, input().split())
# S = 0
# mas1 = []
# a = 0
# for i in range(l, r+1):
#     a = str(i)
#     mas1.extend(a)
# print(sum(int(x) for x in mas1))



# ~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~

# n = int(input())
# m = [i for i in range(n)]
#
# for i in range(n):
#

# ~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~
#

#
# import math
# T = int(input())
#
# for i in range(T):
#     a,b,c = map(int, input().split())
#     if c <= max(a, b) and c % math.gcd(a, b) == 0:
#         print('YES')
#     else:
#         print('NO')



# ~~~~~~~~~~~~~~~~~~~4~~~~~~~~~~~~~~~~~~~~~~~~~~

# n = int(input())
# a = list(map(int, input().split()))
# maxv = float('-inf')
# for i in range(n):
#     c = 0
#     for j in range(n):
#         if a[i] == a[j]:
#             c += 1
#     if maxv < c:
#         maxv = c
# print(maxv)

# n = int(input())
# a = list(map(int, input().split()))
# maxv = float('-inf')
#
# for i in range(n):
#     if maxv < a.count(a[i]):
#         maxv = a.count(a[i])
# print(maxv)

# n = int(input())
# a = list(map(int, input().split()))
#
# freq = {}
# for x in a:
#     freq[x] = freq.get(x, 0) + 1
#
# print(max(freq.values()))

# from sympy import symbols, solve, Eq
#
# c = float(input())
# n = int(input())
#
# x = symbols('x')
#
# a = Eq(n*x**n+x**(1/n), c)
# b = solve(a, x)
# print(b[0])
#
# c = float(input())
# n = int(input())
# x = 1
# while n*x**n+x**(1/n) != c:
#     x += .0000001
# print(x)
