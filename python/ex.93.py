dict = {}
dict['nome'] = str(input('nome do jogador: '))
dict['partida'] = int(input(f'quantas partidas {dict["nome"]} jogou? '))
gol = []
for k in range(dict['partida']):
   gols = int(input(f'quantos gols na partida {k}? '))
   gol.append(gols)
   dict['gols'] = gol
   dict['total'] = sum(gol)
print('=+='*30)
print(dict.items())
print('=+='*30)
for valor in dict:
   print(valor)

