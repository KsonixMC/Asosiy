# t1

# N = int(input("n="))
# K = int(input("k="))
# with open("File.txt", 'w') as f:
#     for x in range(N):
#         f.write('%'*K)
#         f.write("\n")

# t2

# N = int(input('N = '))
# i = 97
# S = ''
# with open("File.txt", 'w') as f:
#     for x in range(N):
#         S += chr(i)
#         f.write(S)
#         f.write("\n")
#         i += 1

# t3

# N = int(input('N = '))
# i = 65
# S = ''
# with open("File.txt", 'w') as f:
#     for x in range(N):
#         S += chr(i)
#         f.write(S)
#         for q in range(N-x-1):
#             f.write('*')
#         f.write('\n')
#         i += 1

# t4

# c1 = 0
# c2 = 0
# with open('File.txt', 'r') as f:
#     for line in f:
#         c2 += len(line.rstrip('\n'))
#         c1 += 1
# print(c1)
# print(c2)

# t5

# s = input('s = ')
# f = open('File.txt', 'a')
# f.write(s)
# f.close()

# t6

# f1 = open('File1.txt', 'a')
# f2 = open('File2.txt', 'r')
# s = f2.read()
# f1.write(s)

# t7
#
# s = input('s = ')
# f1 = open('File1.txt', 'r')
# a = f1.read()
# f1.close()
# f2 = open('File1.txt', 'w')
# f2.write(s)
# f2.write(a)
# f2.close()

# t8

# f1 = open('File1.txt', 'r')
# s = f1.read()
# f1.close()
#
# f2 = open('File2.txt', 'r')
# a = f2.read()
# f2.close()
#
# f1 = open('File1.txt', 'w')
# f1.write(a)
# f1.write(s)
# f1.close()


# t9

# k = int(input('k = '))
#
# f = open('File1.txt', 'r')
# s = f.readlines()
# f.close()
# if len(s) >= k:
#     T = True
#     satr1 = []
#     for i in range(k-1):
#         satr1.append(s[i])
#     satr2 = []
#     for i in range(k-1, len(s)):
#         satr2.append(s[i])
#     print('satr2 =', satr2)
# else:
#     T = False
#
# if T == True:
#     f = open('File1.txt', 'w')
#     for i in range(len(satr1)):
#         f.write(satr1[i])
#     f.write('\n')
#     for i in range(len(satr2)):
#         f.write(satr2[i])
#     f.close()

# t10

# k = int(input('k = '))
#
# f = open('File1.txt', 'r')
# s = f.readlines()
# f.close()
# if len(s) >= k:
#     T = True
#     satr1 = []
#     for i in range(k):
#         satr1.append(s[i])
#     satr2 = []
#     for i in range(k, len(s)):
#         satr2.append(s[i])
#     print('satr2 =', satr2)
# else:
#     T = False
#
# if T == True:
#     f = open('File1.txt', 'w')
#     for i in range(len(satr1)):
#         f.write(satr1[i])
#     f.write('\n')
#     for i in range(len(satr2)):
#         f.write(satr2[i])
#     f.close()


# t11

# f = open('File1.txt', 'r')
# s = []
# for line in f:
#     if len(line) == 1:
#         if ord(line[0]) == 10:
#             s.append('\n')
#             s.append('\n')
#     else:
#         s.append(line)
# f.close()
# f = open('File1.txt', 'w')
# for i in range(len(s)):
#     f.write(s[i])

# t12

# satr = input('s = ')
# f = open('File1.txt', 'r')
# s = []
# for line in f:
#     if len(line) == 1:
#         if ord(line[0]) == 10:
#             s.append(satr)
#             s.append('\n')
#     else:
#         s.append(line)
# f.close()
# f = open('File1.txt', 'w')
# for i in range(len(s)):
#     f.write(s[i])


# t13

# f = open('File1.txt', 'r')
# s = f.readlines()
# f.close()
# f = open('File1.txt', 'w')
# s.pop(0)
# for i in range(len(s)):
#     f.write(s[i])

# t14

# f = open('File1.txt', 'r')
# s = f.readlines()
# s.pop(-1)
# f.close()
# f = open('File1.txt', 'w')
#
# for i in range(len(s)):
#     f.write(s[i])

# t15

# k = int(input('k = '))
# f = open('File1.txt', 'r')
# s = f.readlines()
#
# if len(s) >= k:
#     line1 = []
#     for i in range(0, k-1):
#         line1.append(s[i])
#     line2 = []
#     for i in range(k, len(s)):
#         line2.append(s[i])
# f.close()
# f = open('File1.txt', 'w')
# for i in range(len(line1)):
#     f.write(line1[i])
# for i in range(len(line2)):
#     f.write(line2[i])

# t16

f = open('File1.txt', 'r')
s = f.readlines()
a = ''
for i in range(len(s)):
