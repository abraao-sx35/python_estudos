from random import choice
numeros = (1,2,3,4,5,6,7,8,9)
escolha4 = choice(numeros)
escolha3 = choice(numeros)
escolha2 = choice(numeros)
escolha1 = choice(numeros)
numeros2 = (escolha4,escolha1,escolha2,escolha3)
print('os numeros sorteados foram:',escolha1 , escolha2 ,escolha3, escolha4)
print(f'o menor numero foi {max(numeros2)}\n o maior numero foi {min(numeros2)}')

