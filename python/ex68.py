print('='*20)
print('cadastre uma pessoa')
print('='*20)
cont = maior18 = menor20 = 0
mylista = []
lista2 = []
while True:
    idade = int(input('qual sua idade?: '))
    nome = str(input('[M/F]: '))
    crtz = str(input('deseja continuar [S/N]:? ')).upper

    mylista.append(nome)
    m = mylista.count("m")
    f = mylista.count('f')

    print(f'temos {f} mulheres cadastradas e {m} homens cadastrados')
    





