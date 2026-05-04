##N = int(input())
##if N%400 == 0 or (N%4==0 and N%4!=0):
##    print('Kabisa yili')
##else:
##    print('Kabisa yili emas')

N = int(input())
if N%400 == 0 or (N%4==0 and N%100!=0):
    print('Kabisa yili')
else:
    print('Kabisa yili emas')
