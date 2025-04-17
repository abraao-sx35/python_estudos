valores = []
from time import sleep
while True:
    n = int(input('digite um valor: ')) #pede pra digitar um valor
    if n in valores: # se o  valor ja estiver na lista nao e adicionado
        print('o valor foi duplicado... nao foi adicionado')
    else: #se o valor nao estiver e adicionado na lista
        print('valor adicionado com sucesso...')
        valores.append(n) #adicionando o valor
    sleep(0.5)
    s_n = str(input('deseja continuar[s/n]: ')).lower()
    if s_n == "n": #se o usuario digitar nao, o loop fecha
        break
print(f'voce digitou {valores}')