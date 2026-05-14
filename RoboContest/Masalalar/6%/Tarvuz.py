n, a, b = map(int, input().split())

if (100-b) == 0:
    print(0.00000)
else:
    result = n * (100-a) / (100-b)
    print(f'{result:.5f}')