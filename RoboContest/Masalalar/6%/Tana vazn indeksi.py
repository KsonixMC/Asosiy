v, b = map(int, input().split())
if (10000*v)/b**2 < 16:
  print('Yuqori vazn yetishmasligi')
elif 16 <= (10000*v)/b**2 < 18.5:
  print('Vazn yetishmasligi')
elif 18.5 <= (10000*v)/b**2 <= 25:
  print('Ideal vazn')
elif 25 < (10000*v)/b**2 <= 30:
  print('Ortiqcha vazn')
elif 30 < (10000*v)/b**2 <= 35:
  print('Semizlikning I darajasi')
elif 35 < (10000*v)/b**2 <= 40:
  print('Semizlikning II darajasi')
elif 40 < (10000*v)/b**2:
  print('Semizlikning III darajasi')