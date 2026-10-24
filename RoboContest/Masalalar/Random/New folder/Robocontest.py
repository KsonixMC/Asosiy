# 1

# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())
# b = sorted(a)
# print(b[k-1])

# 2

# f = open('input.txt', 'r')
# s = f.readlines()
# f.close()
# I = 0
# maxv = float('-inf')
# for i in range(len(s)):
#     a = s[i].split()
#     z = a[0]
#     b = a[1:]
#     S = 0
#     for q in range(len(b)):
#         S += int(b[q])
#     if maxv < S:
#         maxv = S
#         I = z
# print(I)

# 3

# n, q = map(int, input().split())
#
# a = list(map(int, input().split()))
# mas = []
# for i in range(q):
#     x = int(input())
#     mas.append(x)
# mas2 = []
# for i in range(q):
#     y = 1
#     while True:
#         if mas[i]+y not in a:
#             mas2.append(mas[i]+y)
#             break
#         else:
#             y += 1
#
# for i in range(len(mas2)):
#     print(mas2[i])

n, q = map(int, input().split())
a = set(map(int, input().split()))

for i in range(q):
    x = int(input())
    y = x + 1
    while y in a:
        y += 1
    print(y)