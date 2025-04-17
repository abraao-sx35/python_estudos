dados = {}
idade = []
nomes = []
while True:
    #verificando nome
    nome = str(input('digite seu nome: '))
    nomes.append(nome)
    total_nomes = len(nomes)

    #verificando sexo
    dados['sexo'] = str(input('sexo[f/m]')).upper()
    if dados['sexo'] not in ['F','M']:
        print('ERRO , digite apenas [f ou m]')
        dados['sexo'] = str(input('sexo[f/m]')).upper()

    #verificando idade
    dados['idade'] = int(input('idade: '))
    idade.append(dados['idade'])
    media = (sum(idade)) / total_nomes
    
    #verificando pausa
    parada = str(input('quer continuar[s/n]: ')).upper()
    if parada not in ['S','N']:
        print('erro responda S ou N')
        parada = str(input('quer continuar[s/n]: ')).upper()
    if parada == "N":
        break

    #saida do codigo
print(' a quantidade de pessoas no total sao: ',total_nomes)
print('as medias de idade',media)



