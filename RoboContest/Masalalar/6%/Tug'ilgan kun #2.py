n, k = map(int, input().split())
a = list(map(int, input().split()))
S = 0
for i in range(n):
    if a[i] >= 0:
        S += a[i]
print(S)