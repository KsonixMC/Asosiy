n = int(input())
a = list(map(int, input().split()))
b = a.pop(a.index(max(a)))

print(max(a))