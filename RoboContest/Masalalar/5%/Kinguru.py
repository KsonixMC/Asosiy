x1, v1, x2, v2 = map(int, input().split())
S = 0
while x1 != x2 and S != 10001:
    x1 += v1
    x2 += v2
    S += 1
if S == 10001:
    print('NO')
else:
    print('YES')

x1, v1, x2, v2 = map(int, input().split())

if v1 == v2:
    print("YES" if x1 == x2 else "NO")
else:
    diff_x = x2 - x1
    diff_v = v1 - v2
    if diff_v != 0 and diff_x % diff_v == 0 and diff_x // diff_v > 0:
        print("YES")
    else:
        print("NO")
