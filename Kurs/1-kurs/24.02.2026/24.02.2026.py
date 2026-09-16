'''N = int(input('N='))
S = 0
d = float('inf')
f = 0
for i in range(N):
    a = int(input(f'a{i+1}='))
    if a < d:
        d = a
    if d > f:
        S+=1
        f = a
print(S)


N = int(input('N='))
S = 0

a1 = int(input('a1='))

for i in range(2, N+1):
    a = int(input(f'a{i}='))

    if a1 > a:
        S += 1
    a1 = a
        
print(S)'''


a = 1
a1 = int(input('a='))
S = 0

while a != 0:
    a = int(input('a='))
    if a1 > a:
        S += 1
    a1 = a
print(S-1)
