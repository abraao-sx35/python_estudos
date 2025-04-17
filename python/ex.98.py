import time

print('contagem de 1 ate 10 de 1 em 1')
for numero in range(1,11):
    print(numero,end="",flush=True)
    time.sleep(0.8)
print()

print('contagem de 10 ate 0 de 2 em 2')
for segundo in range(10,-2,-2):
    print(segundo,end="",flush=True)
    time.sleep(0.8)
print()

def contador():
    inicio = int(input('incio: '))
    meio = int(input('fim: '))
    fim = int(input('de quantos em quantos numeros'))
    for i in range(inicio,meio,fim):
        print(i)

contador()