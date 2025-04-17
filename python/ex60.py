n = int(input('digite seu numero fatorial: '))
cont = 1
re = 1
while cont <= n :
    re *=  cont
    cont += 1

print(f'a conta de {n}! e {re}')

