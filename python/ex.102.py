import math


def fatorial():
    numero = int(input('digite um numero para fazer o fatorial: '))
    calculo = str(input('deseja ver como funciona?[s/n]: ')).lower()
    if calculo == 'n':
        resultado = math.factorial(numero)
        print(f'o resultado e {resultado}')
    if calculo == 's':
        c = numero
        f = 1
        while c > 0:
            print(f'{c}',end="")
            print('x' if c > 1 else '=',end="")
            f *= c
            c -= 1
        print(f'{f}')

fatorial()
    