n = int(input())

if n % 10:




km = n // 1000000
m = n % 1000000 // 1000
sm = n % 1000
mm = n % 10
print(f'{km} km {m} m {sm} sm {mm} mm')

# 1 234 56 7 => 1 km 234 m 56 sm 7 m