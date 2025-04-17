numeros = []
for c in range(4):
    n = int(input('digite um numero: '))
    numeros.append(n)
    cont = 0
    if numeros[0] % 2 == 0:
      cont += 1
else:
    if numeros[1] % 2 == 0:
        cont += 1
    if numeros[2] % 2 == 0:
        cont += 1
    if numeros[3] % 2 == 0:
        cont += 1
    nove = numeros.count(9)
tupla = tuple(numeros)
print(f'voce digitou os valores {tupla}     \n o valor {tupla[2]} apareceu na posicao 3')
print(f'o numero nove apareceu {nove} vezes \n apareceu  {cont} numeros pares')

        
