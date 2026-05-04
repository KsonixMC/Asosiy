N = int(input())
mas = list(map(int, input().split()))
print(mas)
maxv = float('-inf')
for i in range(N):
    if maxv < mas.count(mas[i]):
        maxv = mas.count(mas[i])
print(N-maxv)
