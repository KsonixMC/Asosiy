##2

##n = int(input('n='))
##v = []
##
##for i in range(n+1):
##    v.append(2**i)
##print(v)

##3

##n = int(input('n='))
##A = int(input('A='))
##D = int(input('D='))
##v = [A]
##
##for i in range(1, n):
##    A += D
##    v.append(A)
##print(v)

##4

##n = int(input('n='))
##A = int(input('A='))
##D = int(input('D='))
##v = []
##
##for i in range(1, n):
##    A *= D
##    v.append(A)
##print(v)

##5

##n = int(input('n='))
##F0 = 1
##F1 = 1
##v = [F0, F1]
##
##for i in range(1, n-1):
##    F = F0 + F1
##    v.append(F)
##    F0 = F1
##    F1 = F
##print(v)
    
##6

n = int(input('n='))
A = int(input('A='))
B = int(input('B='))
v = [A, B]

for i in range(n):
    a = A + B
    A = B
    B = a
    for q in range(a):
        B += a
        v.append(B)
        print(v)
print(v)
