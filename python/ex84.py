galera = []
total = []
maiorp = menorp = 0
while True:
    galera.append(str(input('digite seu nome: ')))
    galera.append(str(input('digite seu peso: ')))
    reps = str(input('quer continuar[s/n]? '))
    total.append(galera[:])
    galera.clear()
    if reps in 'Nn':
        break
print(f'ao todo voce cadastrou {len(total)} de pessoas')
print(f'o maior peso foi {max(total)}')
print(f'o menor peso foi {min(total)}')

