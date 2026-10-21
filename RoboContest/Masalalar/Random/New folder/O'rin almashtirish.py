n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    for q in range(i+1, len(a)):
        if a[i] > a[q]:
            a[i], a[q] = a[q], a[i]
print(a)

#