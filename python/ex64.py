print('\033[1;34mtratando valores ') 
numero = int(input('digite um numero [obs: 999 para parar]: '))
teste = numero
cont = 1
numero2 = 999
while numero != numero2:
    numero = int(input('digite um numero [obs: 999 para parar]: '))
    teste += numero
    cont += 1
print(f'voce digitou {cont - 1} numeros e a soma entre eles foi {teste - 999}')

