n = int(input())

a = 2**(2*n+1)-2**(n+1)+1
b = 2**(2*n+1)+2**(n+1)+1

if a % 5 == 0:
    print('A')
if b % 5 == 0:
    print('B')



n = int(input())

a = (pow(2, 2*n+1, 5) - pow(2, n+1, 5) + 1) % 5
b = (pow(2, 2*n+1, 5) + pow(2, n+1, 5) + 1) % 5

if a == 0:
    print('A')
elif b == 0:
    print('B')