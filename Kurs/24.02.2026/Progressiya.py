a2 = 1
a1 = 2
eps = 1e-8
q = 1
while a1 > eps:
    a1, a2 = 2/(a1+a2**2*q**2),a1
    print(F"{q:2d}-qadam:: {a2:10.9f} {a1:10.9f}")
    q+=1
