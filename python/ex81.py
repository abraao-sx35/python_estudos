lista = []
while True:
    n = int(input('digite um valor: ')) ##pede pra digitar um valor
    lista.append(n)  #colocando valor na lista
    reverso = lista.sort(reverse=True) #revertendo a lista
    s_n = str(input('quer continuar[s/n]? ')).lower()
    if s_n == 'n':  #se o usuario digitar nao, o loop fecha
        break
print(f'voce digitou {len(lista)}\n sua lista em ordem decresente e {lista}')
if 5 in lista: #se o numero 5 estiver na lista vai mostrar
        print('5 esta na lista')
