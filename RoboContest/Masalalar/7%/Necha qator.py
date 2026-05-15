# a = ""
# c = 0
# while a != '.':
#     a = input()
#     c += 1
# print(c-1)

import sys
input = sys.stdin.readline

c = 0
while True:
    a = input().strip()
    if a == '.':
        break
    c += 1

print(c)