A, B, C = map(int, input().split())
if abs(C-A) < abs(C-B):
  print('1-mushuk')
elif abs(C-A) > abs(C-B):
  print('2-mushuk')
else:
  print('sichqon')