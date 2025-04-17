valor = []
lispar = []
lisimpar = []
for c in range(7):
    valores = int(input('digite os valores: '))
    valor.append(valores)
for v in valor: #pra cada valor na lista
    if v % 2 == 0: #divida ele por 2 e veja se e 0, se for adicione na lista par
      lispar.append(v)
    else: #se nao for adicione na lista impar
        lisimpar.append(v)
print(f'os numeros pares foram {lispar}')
print(f'os numeros impares foram {lisimpar}')