n = int(input())
a = list(map(int, input().split()))
minv = float('inf')

for i in range(n):
    if minv > a.count(a[i]):
        minv = a.count(a[i])
        b = a[i]
print(b)