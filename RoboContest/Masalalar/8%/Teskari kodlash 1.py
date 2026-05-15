T = int(input())
for i in range(T):
    S = []
    a = int(input())
    while a >= 1:
        S.append(a % 2)
        a //= 2
    print(S.count(1))
