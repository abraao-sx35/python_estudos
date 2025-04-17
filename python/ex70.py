import time
lista_nomes = []
lista = [] #lista vazia
print('='*20)
print('loja baratao do abraao')
print('='*20)
while True: #loop
    produto = str(input('nome do produto: ')) #perguntando nome do produto
    preco = float(input('preço do produto: ')) #perguntando preço
    continuar = str(input('deseja continuar[s/n]? ')).upper() #perguntando se deseja continuar

    lista_nomes.append(produto)
    lista.append(preco) #adicionando os precos a lista
    soma = sum(lista) #soamndo os itens da listas
    minimo = min(lista) #menor valor da lista
    maximo = max(lista) #maior valor da lista

    if continuar == "N":
        break
print('calculando sua compra.....')
time.sleep(2)
print(f'sua compra deu {soma} \n o produto mais caro foi {maximo} \n o produto mais barato da sua compra foi {minimo}')
print(f'seus produtos comprados foram: {lista_nomes} ')