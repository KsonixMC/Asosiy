n = input()
a = []
a.extend(n)
S = 0
for i in range(len(a)):
    match a[i]:
        case '0':
            S += 6
        case '1':
            S += 2
        case '2':
            S += 5
        case '3':
            S += 5
        case '4':
            S += 4
        case '5':
            S += 5
        case '6':
            S += 6
        case '7':
            S += 3
        case '8' :
            S += 7
        case '9':
            S += 6
print(S)