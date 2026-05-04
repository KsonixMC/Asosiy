a = list(map(int, input().split()))
minv = min(a)
maxv = max(a)

total = sum(a)
print(total-maxv, total-minv)
