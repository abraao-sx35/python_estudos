print('='*20)
print('banco do abraao')
print('='*20)
saque = int(input('quanto voce deseja sacar? '))
total = saque
ced = 100
totalced = 0
while True:
    if total >= ced:
     total -= ced
     totalced += 1
    else:
     print(f'seu saque de {saque} voce recebeu {totalced} notas de {ced} reais')
     if ced == 100:
        ced = 20
     elif ced == 20:
        ced = 10
     elif ced == 10:
        ced = 1
     totalced = 0
     if total == 0:
        break








