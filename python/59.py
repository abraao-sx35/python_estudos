n1 = float(input('primeiro valor: '))
n2 = float(input('segundo valor: '))
sair = False
while not sair:
    print('(1) somar ')
    print('(2) multiplicar')
    print('(3) novos numeros')
    print('(4) sair do programa')
    escolha = str(input('oque voce deseja?: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'a soma entre {n1} e {n2} foi {soma}')
    if escolha == 2:
        multi = n1 * n2 
        print(f'a multiplicacao entre {n1} e {n2} foi {multi}')
    if escolha == 3:
        n1 = float(input('primero novo valor: '))
        n2 = float(input('segundo novo valor: '))
    if escolha == 4:
        sair =True


