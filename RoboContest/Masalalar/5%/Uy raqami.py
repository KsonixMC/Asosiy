N = int(input())
M = []
for i in range(1, N+1):
    if i + i%100 == N:
        M.append(i)
for q in range(len(M)):
    print(M[q], end=' ')
