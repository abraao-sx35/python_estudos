matrix_lista = [[0,0,0],
                [0,0,0],
                [0,0,0]]
listapar = []
for l in range(0,3):
    for c in range(0,3):
        matrix_lista[l][c] = int(input('digite um numero: '))

# verificar numeros pares na matrix
for zero in matrix_lista[0]:
    if zero % 2 == 0:
        listapar.append(zero)
for um in matrix_lista[1]:
    if um % 2 == 0:
        listapar.append(um)
for dois in matrix_lista[2]:
    if dois % 2 == 0:
        listapar.append(dois)
print(matrix_lista,)
print('=+='*30)
print(f'a soma dos valores pares sao {sum(listapar)}')
print(f'o maior valor na segunda coluna e {max(matrix_lista[1])}')
print(f'a soma da terceira e {sum(matrix_lista[2])}')