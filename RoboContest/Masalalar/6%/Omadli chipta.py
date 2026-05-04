n = int(input())
a = n//1000
b = n%1000
s1 = 0; s2 = 0
while a != 0:
    s1 += a % 10
    a = a // 10
while b != 0:
    s2 += b % 10
    b = b // 10
if s1 == s2:
    print("YES")
else:
    print("NO")