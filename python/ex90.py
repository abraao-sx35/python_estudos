aluno = {}
aluno['nome'] = str(input('qual seu nome: '))
aluno['nota'] = float(input('qual sua nota: '))
if aluno['nota'] <= 5:
    print(aluno,'\n aluno em situacao reprovado')
if aluno['nota'] >= 7:
    print(aluno,'\n aluno aprovado')




