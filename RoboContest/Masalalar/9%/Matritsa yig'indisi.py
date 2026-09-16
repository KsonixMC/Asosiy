def print2(massive):
    for line in massive:
        print(' '.join(map(str, line)))

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
for i in range(N):
    B.append(list(map(int, input().split())))

V = [[A[i][q] + B[i][q] for q in range(M)] for i in range(N)]
print2(V)