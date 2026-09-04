import random



m = int(input("m="))
n = int(input('n='))

mas = []
for i in range(m):
    row = []
    for q in range(n):
        row.append(random.randint(0,9))
    mas.append(row)
[print(row) for row in mas]
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

b = []
for y in range(n):
    row1 = []
    for x in range(m):
        row1.append(
