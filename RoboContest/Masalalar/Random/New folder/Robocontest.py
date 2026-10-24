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

# n, q = map(int, input().split())
# a = set(map(int, input().split()))
#
# for i in range(q):
#     x = int(input())
#     y = x + 1
#     while y in a:
#         y += 1
#     print(y)

# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# p = [0] * (n+1)
# for i in range(len(a)):
#     p[i+1] = p[i] + a[i]
#
# for i in range(q):
#     l, r = map(int, input().split())
#     print(p[r]-p[l-1])
# #
#
# import sys
#
# input = sys.stdin.buffer.readline
#
# n, q = map(int, input().split())
# a = list(map(int, input().split()))
#
# p = [0] * (n + 1)
#
# for i in range(n):
#     p[i + 1] = p[i] + a[i]
#
# for _ in range(q):
#     l, r = map(int, input().split())
#     print(p[r] - p[l - 1])

# 4

n, k = map(int, input().split())
a = list(map(int, input().split()))
maxv = float('-inf')
for i in range(n-k+1):
    s = 0
    for q in range(k):
        s += a[q]
    s /= k
    if maxv < s:
        maxv = s
        ind = i
print(maxv)