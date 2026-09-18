# Recur1

# def fact(N):
#     if N < 2:
#         return 1
#     return N*fact(N-1)
#
# print(fact(int(input('N1 = '))))
# print(fact(int(input('N2 = '))))
# print(fact(int(input('N3 = '))))

# Recur2

# def fact2(N):
#     if N%2==1:
#         if N<=2:
#             return 1
#         return N*fact2(N-2)
#     else:
#         if N<2:
#             return 1
#         return N*fact2(N-2)
#
# print(fact2(int(input('N1 = '))))
# print(fact2(int(input('N2 = '))))
# print(fact2(int(input('N3 = '))))

# Recur3

# def PowerN(X, N):
#     if N == 0:
#         return 1
#     if N == 1:
#         return X
#     if N>0 and N%2==0:
#         if N < 2:
#             return X ** N
#         else:
#             return (PowerN(X, N // 2)) ** 2
#     if N>2 and N%2==1:
#         return 2*PowerN(X, N-1)
#     if N < 0:
#         return 1/PowerN(X, -1*N)
# print(PowerN(int(input('X = ')), int(input('N = '))))

# Recur4
F1 = 1; F2 = 1

def F(N):
