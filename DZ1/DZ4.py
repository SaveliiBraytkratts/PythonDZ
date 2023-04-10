a,b = int(input('Видите 1-ю сторону: ')),int(input('Видите 2-ю сторону: '))
k = int(input('Видите кол-во долек: '))
if k%a == 0 or k%b == 0:
    print('Yes')
else:
    print('No')