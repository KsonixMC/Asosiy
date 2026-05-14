n = int(input())
if n%50 <= 25 and n%50 != 0:
    print('O__')
elif 25 < n%50 <= 29:
    print('OO_')
elif 29 < n%50 <= 35:
    print('_O_')
elif 35 < n%50 <= 50 or n%50==0:
    print('__O')