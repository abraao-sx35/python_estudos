def numero():
    while True:
        numero_inteiro = input('digite um numero: ')
        if isinstance (numero_inteiro,int):
            print(f"o numero digita foi {numero_inteiro}") #isinstance ele verificar o valor que vc deseja passar
            break
        else:
            print('erro!! digite um numero')


numero()
