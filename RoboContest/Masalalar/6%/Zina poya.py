# n = int(input())
# a = 1
# S = 0
# c = 0
# while a+a**2 < n*2:
#     S += a
#     a += 1
#     c += 1
#     print(a)

import math

n = int(input())
k = int((-1 + math.isqrt(1 + 8 * n)) // 2)
print(k)