N = int(input("n="))
K = int(input("k="))
with open("test99.txt", 'w') as f:
    for x in range(N):
        f.write('*'*K)
        f.write("\n")