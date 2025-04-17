print( 'gerador de pa')
termo = int(input('qual primeiro termo? '))
razao = int(input('qual a razao? '))
count = 1
pa = termo
while count <= 10:
    print(f"{pa}-",end="")
    pa += razao
    count += 1
print('pausa')