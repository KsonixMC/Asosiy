"""String63. O’zbekcha so’zlardan iborat satr va K soni berilgan (0 < K < 10). Satrni o’ngga K
ta siklik siljitish orqali kodlovchi programma tuzilsin. Ya’ni alfavitdagi harflar o’zidan K ta keyin
turgan harf bilan almashtiriladi. Tinish belgilari va probel o’zgarishsiz qoldirilsin.
Masalan: K = 2; ABCD Natija : CDEF"""

matn = input("matn")
k = int(input("k="))
matn2 = ""
# for ch in matn:
#     if 65 <= ord(ch) <= 90:
#         ch2 = (ord(ch) + k - 65) % 26 + 65
#     elif 97 <= ord(ch) <= 122:
#         ch2 = (ord(ch) + k - 97) % 26 + 97
#     else:
#         ch2 = ord(ch)
#     matn2 += chr(ch2)
#     print(ch, ch2)
#     print(matn, matn2)

for ch in matn:
    if 65 <= ord(ch) <= 90:
        if ord(ch) + k > 90:
            matn2 += chr(ord(ch) + k - 26)
        else:
            matn2 += chr(ord(ch) + k)
    elif 97 <= ord(ch) <= 122:
        if ord(ch) + k > 122:
            matn2 += chr(ord(ch) + k - 26)
        else:
            matn2 += chr(ord(ch) + k)
    else:
        matn2 += ch
print(matn2)