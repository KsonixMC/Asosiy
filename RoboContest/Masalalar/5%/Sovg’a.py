a = list(map(int, input().split()))
S = int(input())
b = sum(a)
if S - b > 0:
  print(S-b)
else:
  print(0)
