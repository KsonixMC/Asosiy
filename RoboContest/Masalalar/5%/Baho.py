n = int(input())

if n >= 38:
    if n%10 <= 5:
        a = n//10*10+5
    elif n%10 > 5:
        a = n//10*10+10
    if a-n<3:
        b = a
    elif a-n>=3:
        b = n
    print(b)
else:
    print(n)
    print(n)
    
