# def length(a):
#     lena = len(a)
#     return lena
#
# def qatiyatli_son(b):
#     if length(b) == 1:
#         return True
#     elif length(b) > 1:
#         if int(b) % length(b) == 0:
#             sh1 = True
#         else:
#             sh1 = False
#         if qatiyatli_son(str(int(b)//length(b))):
#             sh2 = True
#         else:
#             sh2 = False
#     return sh1 == sh2
#
# a = input()
#
# print(qatiyatli_son(a))

# Begin9

# a = int(input())
# b = int(input())
# print((a*b)**.5)

# Begin13

# r1, r2 = map(int, input().split())
# p = 3.14
# s1 = p * r1**2
# s2 = p * r2**2
# print(f'{abs(s1-s2):.2f}')

# Begin14
#
# l = float(input())
# p = 3.14
#
# r = l/(2*p)
#
# s = p*r**2
#
# print(f'{r:.2f} {s:.2f}')

# Begin16

# x1, x2 = map(int, input().split())
# print(abs(x1-x2))


# Begin17

# a, b, c = map(int, input().split())
#
# ac = abs(a-c)
# bc = abs(b-c)
# print(ac + bc)

# Begin18

# a, b, c = map(int, input().split())
# ac = abs(a-c)
# bc = abs(b-c)
# print(ac*bc)4

# Begin21

# x1, y1, x2, y2, x3, y3 = map(int, input().split())
#
# a = abs(x2-x1)
# b = abs(y2-y1)
# c = (a**2 + b**2)**.5
#
# print(a, b, c)
# P = a + b + c
# p = P/2
# s = (p*(p-a)*(p-b)*(p-c))**.5
# print(f'{s:.2f} {P:.2f}')

# Begin23
#
# a, b, c = map(int, input().split())
#
# a, b, c = b, c, a
# print(a, b, c)


# Begin29

a = int(input())
p = 3.14
print(f'{180/p*a:.4f}')