def notas():
    armarzena_notas = []
    for nota in range(0,3):
        n = int(input('digite sua nota: '))
        armarzena_notas.append(n)
    situacao = str(input('deseja ver sua situacao?: ')).strip().lower()
    if situacao in "sim":
        dados = {"total": 3,
             "maior": max(armarzena_notas),
             'menor': min(armarzena_notas),
             "media": (nota+nota+nota)/2,
            }
        if dados["media"] >= 7:
            print(dados)
            print('situaçao esta boa')
        else:
            print(dados)
            print('situaçao esta ruim')
    else:
        dados = {"total": len(armarzena_notas),
             "maior": max(armarzena_notas),
             'menor': min(armarzena_notas),
             "media": (nota+nota+nota)/2,
            }
        print(dados)


notas()