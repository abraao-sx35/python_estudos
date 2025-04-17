print('-\033[1;34m'*20)
termos = int(input('\033[1;31mquantos termos voce deseja: '))
t1 = 0
t2 = 1
cont = 3
while cont <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'\033[1;31m{t3}-\033[1;31m',end="")
    cont += 1
print('fim')
