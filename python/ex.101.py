import datetime
ano = datetime.datetime.now().year

def voto():
    pessoa = int(input('em qual ano vc nasceu? '))
    idade = ano - pessoa
    if idade <= 17:
        print('com',idade,'voce nao e permitido votar')
    if 18 <= idade <= 79 :
        print('com',idade,'seu voto e obrigatorio')
    if idade >= 80:
        print('com',idade,'seu voto e opcional')

print('=+='*20)
voto()