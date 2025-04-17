print('progressao aritrimetrica v3')
primeiro = int(input('qual o primeiro termo: '))
razao = int(input('qual a razao: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while count <= total:
    print(f'{termo}-',end="")
    termo += razao
    count += 1
  print('pausa')
  mais = int(input('quantos termos vc quer mostrar a mais: '))
print('fim')








