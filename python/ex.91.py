import random
from time import sleep
from operator import itemgetter
print('valores sorteados')
jogadores = {'jogador1':None,'jogador2':None,'jogador3':None,'jogador4':None}
for jogador in jogadores:
    n = random.randint(1,10)
    jogadores[jogador]=n
    print(jogador,"tirou no dado",n)
    sleep(0.5)
ranking = dict()
ranking = sorted(jogadores.items(),key=itemgetter(1) ,reverse=True)
print('=-='*30)
print('RANKING DOS JOGADORES')
for numeracao,pessoa in enumerate(ranking,start=1):
    print(numeracao,pessoa)



#emanuel vai te lascar!!