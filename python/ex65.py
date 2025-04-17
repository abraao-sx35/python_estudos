print('menor e maior valor')
numero2 = "s"
cont = 0
mylist = []
while numero2 != 'n':
    numero = int(input('digite um numero: '))
    numero2 = str(input('deseja continuar?[s/n]: ')).lower()
    mylist.append(numero)
    maior = max(mylist)
    menor = min(mylist)
    soma = sum(mylist) 
    media = soma
    cont += 1
    media2 = media / cont
    if numero2 == "n":
        print(f'voce digitou {cont} numeros a media dos numeros foi {media2} \n o maior numero foi {maior} o menor foi {menor}')
        break
    


