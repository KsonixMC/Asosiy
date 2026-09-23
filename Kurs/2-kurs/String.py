# string1
#
# n = input()
# print(ord(n))

# string2

# n = int(input('n = '))
# print(chr(n))

# string3

# n = input('n = ')
# print(chr(ord(n)-1))
# print(chr(ord(n)+1))

# string4

# n = int(input('n = '))
# mas= []
# for i in range(65, 91):
#     mas.append(chr(i))
#
# for i in range(n):
#     print(mas[i])

# string5

# n = int(input('n = '))
# mas=[]
# for i in range(122, 98, -1):
#     mas.append(chr(i))
# for i in range(n):
#     print(mas[i])

# string6

# n = input('n = ')
# if 48 <= ord(n) <= 57:
#     print('digit')
# elif 65 <= ord(n) <= 90:
#     print('lotin')
# elif 97 <= ord(n) <= 122:
#     print('lotin')
# else:
#     print(0)

# string7

# satr = input()
# print(ord(satr[0]), ord(satr[-1]))

# string8

# n = int(input('n = '))
# s = input()
# print(s*n)

# string9

# s1 = input()
# s2 = input()
# print(s1 + s2)

# string10

# s = input()
# mas = []
# for i in range(len(s)-1, -1, -1):
#     mas.append(s[i])
# S = ''
# for i in range(len(s)):
#     S += mas[i]
# print(S)

# string11

# s = input()
# S = ' '.join(s)
# print(S)

# string12

# n = int(input('n = '))
# s = input()
# smbl = '*'*n
# print(smbl.join(s))

# string13

# s = input()
# c = 0
# for i in range(len(s)):
#     if 48 <= ord(s[i]) <= 57:
#         c += 1
# print(c)

# string14

# s = input()
# c = 0
# for i in range(len(s)):
#     if 65 <= ord(s[i]) <= 90:
#         c += 1
# print(c)

# string15

# a = input()
# b = 0
# for i in range(len(a)):
#     if a[i] in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю':
#         b += 1
# print(b)

# string16

# s = input()
# print(s.lower())

# string17

# s = input()
# print(s.lower())

# string18

# s = input()
# print(s.swapcase())

# string19

# A = 1 s == '123' or s == '-123'
# A = 2 s == '123.123' or s == '-123.123'
# A = 0 not int() and not float()


# s = input()
#
# if (s.isdecimal() == True) or (s.startswith('-') and s[1:].isdecimal()==True) or (s.isdecimal() == True) or (s.startswith('+') and s[1:].isdecimal()==True ):
#     print(1)
#     exit()
#
# if s.count('.') == 1:
#     m = s.split('.')
#     m0 = m[0]
#     m1 = m[1]
#     if m0.startswith('-')==True and m0[1:].isdecimal()==True and m1.startswith('-')==False:
#         print(2)
#         exit()
#     if m0.startswith('-')==False and m0.isdecimal()==True and m1.startswith('-')==False:
#         print(2)
#         exit()
#     if m0.startswith('+')==True and m0[1:].isdecimal()==True and m1.startswith('+')==False:
#         print(2)
#         exit()
#     if m0.startswith('+')==False and m0.isdecimal()==True and m1.startswith('+')==False:
#         print(2)
#         exit()
# if (s.startswith('-') and s[1:].isdecimal()==False) or (s.startswith('+') and s[1:].isdecimal()==False):
#     print(0)
#     exit()
# elif s.isdecimal() == False:
#     print(0)
#     exit()
#

# string20

# s = input()
# for i in range(len(s)):
#     print(s[i], end=' ')

# string21

# s = input()
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end=' ')

# string22

# s = input()
# S = 0
# for i in range(len(s)):
#     S += int(s[i])
# print(S)


# string23

# s = input()
# S = 0
# # m = s
# for i in range(0, len(s), 2):
#     m = s[i:]
#     print(m)
#     if len(m) > 1:
#         if m[1] == '+':
#             S += int(m[0])
#     else:
#         S += int(s[-1])
#     # if m[1] == '-':
#     #     S -= int(m[0])
#     # m = s[i+2:]
# print(S)

# string23

# s = '12+13-14+25-123'
#
# m =[]
# amal = []
# i = 0
# while len(s) != 0:
#     S = ''
#     i = 0
#     while i < len(s) and (s[i] != '+' and s[i] != '-'):
#         S += s[i]
#         i += 1
#     if i < len(s) and (s[i] == '+' or s[i] == '-'):
#         amal.append(s[i])
#     m.append(S)
#     if i < len(s):
#         s = s[i+1:]
#     else:
#         s = ''
# print(m)
# print(amal)
#
# y = int(m[0])
#
# for i in range(len(amal)):
#     if amal[i] == '+':
#         y += int(m[i+1])
#     if amal[i] == '-':
#         y -= int(m[i+1])
# print(y)

# string24

# s = input('s = ')
# print(str(int(s, 2)))

# string25

# s = input('s = ')
# print(str(bin(int(s))))

# string26

# n = int(input('n = '))
# s = input('s = ')
#
# if len(s) < n:
#     print(s.rjust(n, '.'))
# if len(s) > n:
#     c = 1
#     while len(s) > n:
#         s = s[c:]
#     print(s)

# string27

# n1 = int(input('n1 = '))
# n2 = int(input('n2 = '))
#
# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# s3 = s1[0:n1] + s2[-n2:]
#
# print(s3)

# string28

# c = input('c = ')
# s1 = input('s1 = ')
# s = ''
#
# for i in range(len(s1)):
#     if s1[i] == c:
#         s += c
#     s += s1[i]
# print(s)

# string29

# c = input('c = ')
#
# s1 = input('s1 = ')
# s2 = input('s2 = ')
# s = ''
# for i in range(len(s1)):
#     if s1[i] == c:
#         s += s2
#     s += s1[i]
# print(s)

# string30

# c = input('c = ')
#
# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# for i in range(len(s1)):
#     if s1[i] == c:
#         print(i, s1[i])
#         s1 = s1[0:i+1] + s2 + s1[i+1:]
#     else:
#         pass
# print(s1)

# string31

# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# if s2 in s1:
#     print(True)
# else:
#     print(False)

# string32

# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# print(s1.count(s2))

# string33

# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# for i in range(len(s1)):
#     if s2 in s1:
#         s1 = s1[:s1.index(s2)]+s1[s1.index(s2)+len(s2):]
#         break
# print(s1)

# string34

# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# a = s1.rfind(s2)
#
# if a != -1:
#     s1 = s1[:a] + s1[a+len(s2):]
# else:
#     pass
#
# print(s1)

# string35

# s1 = input('s1 = ')
# s2 = input('s2 = ')
#
# for i in range(s1.count(s2)):
#     s1 = s1[:s1.index(s2)] + s1[s1.index(s2)+len(s2):]
# print(s1)

# string36

# s1 = input('s1 = ')
# s2 = input('s2 = ')
# s3 = input('s3 = ')
#
# a = s1.find(s2)
#
# s1 = s1[:a] + s3 + s1[a+len(s2):]
# print(s1)

# string37

# s1 = input('s1 = ')
# s2 = input('s2 = ')
# s3 = input('s3 = ')
#
# a = s1.rfind(s2)
#
# s1 = s1[:a] + s3 + s1[a+len(s2):]
# print(s1)

# string38

# s1 = input('s1 = ')
# s2 = input('s2 = ')
# s3 = input('s3 = ')
#
# for i in range(s1.count(s2)):
#     a = s1.find(s2)
#     s1 = s1[:a] + s3 + s1[a+len(s2):]
# print(s1)

# string39

# s = input('s = ')
#
# space1 = s.find(' ')
# if space1 != -1 and s.count(' ') > 1:
#     s = s[space1+1:]
#     print(s[:s.find(' ')])
# else:
#     print("''")

# string40

# s = input('s = ')
#
# space1 = s.find(' ')
# if space1 != -1 and s.count(' ') > 1:
#     space2 = s.rfind(' ')
#     print(s[space1+1:space2])
# else:
#     print("''")

# string41

# s = input('s = ')
# print(s.count(' ')+1)

# string42

# s = input('s = ')
# s = s.split(' ')
#
# for i in range(len(s)):
#     startswith = s[i][0]
#     endswith = s[i][-1]
#     for q in range(i+1, len(s)):
#         if

"not finished"