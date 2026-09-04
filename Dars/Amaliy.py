# import random
#
# # n = random.randint(0, 10)
# n = 5
# mas = []
# for x in range(n):
#     row = []
#     for y in range(n):
#         row.append(random.randint(0, 9))
#     mas.append(row)
# [print(row) for row in mas]
# print('*'*20)
#
# # for y in range(n):
# #     for x in range(y, n-y):
# #         print(mas[x][y], end=' ')
# #     for x in range
#
# # for y in range(n):
# #     for x in range(y, n):
# #         print(mas[y][x], end= '  ')
# #     print()
#
# # mas1 = []
# # for i in range(n):
# #     row1 = []
# #     for q in range(n):
# #         row1.append(mas[q][i])
# #     mas1.append(row1)
# #     # print(row1, end='*')
# # [print(row1) for row1 in mas1]
#
# # print(mas[0][0])
# # print(mas[1][1])
# # print(mas[2][2])
# # print(mas[3][3])
# # print(mas[4][4])
# #
# # print(mas[0][1])
# # print(mas[1][2])
# # print(mas[2][3])
# # print(mas[3][4])
# #
# # print(mas[0][2])
# # print(mas[1][3])
# # print(mas[2][4])
# #
# # print(mas[0][3])
# # print(mas[1][4])
# #
# # print(mas[0][4])
#
#
#
# # for z in range(n):
# # for y in range(n):
# #     a = 0
# #     b = 0
# #     for x in range(n):
# #         print(mas[a][b], end=' ')
# #         a += 1;
# #         b += 1
#
# for z in range(n):
#     a = 0; b = 0
#     for y in range(n):
#         for x in range(x):
#             print(mas[a][b], end=' ')
#         a += 1; b += 1
#     n -=1




gap1 = "@  You can pass as many objects as you"

def masala(matn):
    maxc = float('inf'); max_suz=""
    for suz in matn.split():
        c = 0
        for xarf in suz:
            if ord(xarf) in {66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122}: c += 1
        if c <= maxc and c != 0:
            max_suz = suz; maxc = c
    return maxc, max_suz
print(masala(gap1))