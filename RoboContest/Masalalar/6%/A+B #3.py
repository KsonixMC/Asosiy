a, b = map(str, input().split())

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al_mas = []
al_mas.extend(alph)
n = al_mas.index(a)
m = al_mas.index(b)
print(n+m+2)
