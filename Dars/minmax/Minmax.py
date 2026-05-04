'''N = int(input('nechta son:'))
minv = float('inf')
for i in range(N):
    a = int(input('a='))
    if minv>a:
        minv = a
print(minv)

-------------------------------1

N = int(input('nechta son:'))
maxv = 0
minv = float('inf')
for i in range(N):
    a = int(input('a='))
    if maxv < a:
        maxv = a
    if minv>a:
        minv = a
print('Max=',maxv)
print('Min=', minv)

---------------------------------2

N = int(input('Nechta son='))
minS = float('inf')
for i in range(N):
    a = int(input('a tomon = '))
    b = int(input('b tomon = '))
    S = a * b
    if minS > S:
        minS = S
print('Yuzasi', minS, "bo'lgani eng kichik")'''

'''----self----'''

N = int(input('Nechta son:'))
minv = float('inf')
t = 0
t1 = 0
S = 1
for i in range(N):
    a = int(input('a='))
    t += 1
    if minv>a:
        minv = a
        t1 = t
        S+=1
print(minv, t1, S)
