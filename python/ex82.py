valor = []
lispar = []
lisimpar = []
while True:
    valores = int(input('digite um valor: '))
    valor.append(valores) #adicionando valor na lista
    desicao = str(input('deseja continuar?: ')) 
    if desicao in "nN": #parando o loop com n,N
        break
for v in valor: #pra cada valor na lista
    if v % 2 == 0: #divida ele por 2 e veja se e 0, se for adicione na lista par
      lispar.append(v)
    else: #se nao for adicione na lista impar
        lisimpar.append(v)
print(f'a lista completa e {valor}')
print(f'a lista par e {lispar}')
print(f'a lista impar e {lisimpar}')