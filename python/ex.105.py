
def sistema_ajuda():
    while True:
        escolha = str(input('função ou biblioteca: ')).lower().strip()
        if escolha == "sair":
            break
        else:
            print('acessando o manual de comando de ',escolha)
            print(f"{help(escolha)}")



sistema_ajuda()