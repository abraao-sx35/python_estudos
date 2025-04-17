escreva = ('ola mundo')
string = '='
def palavra_Sem_espaco():
    global string
    for palavra in escreva:
            if palavra != " ":
                string += '='
    return string


resultado = palavra_Sem_espaco()
print(resultado)
print(escreva)
print(resultado)