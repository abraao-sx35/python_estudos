from random import randint

numeros_lista = []
def sorteia():
    for numeros in range(5):
        x = randint(0,10)
        numeros_lista.append(x)
    print(numeros_lista)
sorteia()

lista_par = []
def numeros_pares():
    for valor in (numeros_lista):
        if valor % 2 == 0:
           lista_par.append(valor)
           sum(lista_par)
    print(f'entre os numeros {numeros_lista} os numeros pares foram {lista_par} a soma \n e de {sum(lista_par)}')
numeros_pares()
           


