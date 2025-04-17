dados = []
while True:
    nome = str(input('digite seu nome: '))
    nota1 = float(input('sua primeira nota: '))
    nota2 = float(input('sua segunda nota: '))
    parada = str(input('deseja continuar[s/n]: ')).lower().strip()
    dados.append([nome,nota1,nota2])
    if parada == "n":
        break
for numeracao, pessoa, in enumerate(dados):
    media = (pessoa[1] + pessoa[2])/ 2
    print('N.O',numeracao, f'nome: {pessoa[0]}','media:',media)
while True:
    aluno = int(input('deseja olha a nota de qual aluno? [999 parada]:  '))
    if aluno == 999:
        break
    else:
        for numeracao in dados:
            if aluno in numeracao:
                print(pessoa)
    


