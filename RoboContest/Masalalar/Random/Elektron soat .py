n = int(input())

h = n//3600%24
m = n//60%60
if m < 10:
    m = f'0{m}'
s = n%60
if s < 10:
    s = f'0{s}'
print(f'{h}:{m}:{s}')