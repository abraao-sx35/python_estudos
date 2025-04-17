numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez') #tupla

while True:
 n2 = int(input('digite um numero entre 0 e 10: ')) 
 if 0 <= n2 <= 10:
   print(f'voce digitou o numero {numero[n2]}')
   break
 else:
  n2 = int(input('tente novamente , digite um numero entre 0 e 10: '))
 if 0 <= n2 <= 10:
  print(f'voce digitou o numero {numero[n2]}')
