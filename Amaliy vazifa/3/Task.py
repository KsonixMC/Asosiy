n = int(input('n = '))

S = 0
ishora = 1
c = 0
for i in range(1, 2*n, 2):
    if c%2 == 0:
        surat = i*(i+1)*(i+2)*(i+3)
        maxraj = (i+5) + (i+6) + (i+7) + (i+8)
    elif c%2 == 1:
        surat = i/(i+1)/(i+2)/(i+3)
        maxraj = (i+5) - (i+6) - (i+7) - (i+8)
    S += ishora * (surat/maxraj)
    ishora *= -1
    c += 1
print(S)