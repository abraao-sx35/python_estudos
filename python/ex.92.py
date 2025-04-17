import datetime
dados = {}
while True:
    dados['nome'] = str(input('nome:'))
    dados['nascimento']= int(input('em que ano vc nasceu: '))
    data_atual =datetime.datetime.now().year
    idade = data_atual - dados['nascimento']
    dados['ctps'] = int(input('carteira de trabalho [0 igual que nao tem]: '))
    if dados['ctps'] == 0:  
     print('seu nome e',dados['nome'])
     print('sua idade em anos e',idade)
     print('ctps tem o valor de ',dados['ctps'])
     break
    else:
     dados['contratacao'] = int(input('ano de contratacao: '))
     dados['salario'] = float(input('salario tem o valor de: '))
     print('seu nome e',dados['nome'])
     print('sua idade em anos e',idade)
     print('ctps tem o valor de ',dados['ctps'])
     print('contratacao tem o valor de',dados['contratacao'])
     print('salario tem o valor de',dados['salario'])
     break
