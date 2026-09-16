H1, M1, S1 = map(int, input().split())
H2, M2, S2 = map(int, input().split())
A = H1*3600+M1*60+S1
B = H2*3600+M2*60+S2
print(B - A)