



def controle_de_terreno():
    largura = float(input('digite a largura[m]: '))
    comprimento = float(input('digite o comprimento[m]: '))
    controle = largura * comprimento
    return controle


area = controle_de_terreno()
print(area)

