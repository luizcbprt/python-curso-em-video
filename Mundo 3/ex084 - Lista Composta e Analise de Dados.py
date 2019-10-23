print('-=' * 25)
print(' Lista Composta e Analise de Dados'.center(50, ' '))
print('-=' * 25)

lstGeral = []
lstDado = []
lstPesado = []
lstLeve = []
qtdCad = maisPesado = maisLeve = 0

while True:
    nome = str(input('Informe o Nome: '))
    peso = float(input('Informe o Peso: '))
    lstDado.append(nome)
    lstDado.append(peso)
    lstGeral.append(lstDado[:])
    lstDado.clear()

    if qtdCad == 0:
        maisPesado = peso
        maisLeve = peso
        lstPesado.append(nome)
        lstLeve.append(nome)
    else:
        if peso > maisPesado:
            maisPesado = peso
            lstPesado.clear()
            lstPesado.append(nome)
        elif peso == maisPesado:
            lstPesado.append(nome)
        elif peso < maisLeve:
            maisLeve = peso
            lstLeve.clear()
            lstLeve.append(nome)
        elif peso == maisLeve:
            lstLeve.append(nome)

    qtdCad += 1


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N:' )).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram Cadastrados {qtdCad} pessoas')
print(f'As pessoas mais pesadas tiveram {maisPesado:.2f}KG e foram {lstPesado}')
print(f'As pessoas mais leves tiveram {maisLeve:.2f}KG e foram {lstLeve}')
print()
print(f'Lista Geral: {lstGeral}')

print('-=' * 25)
print(' Lista Composta e Analise de Dados'.center(50, ' '))
print('-=' * 25)

lstGeral = []
lstDado = []
lstPesado = []
lstLeve = []
qtdCad = maisPesado = maisLeve = 0

while True:
    nome = str(input('Informe o Nome: '))
    peso = float(input('Informe o Peso: '))
    lstDado.append(nome)
    lstDado.append(peso)
    lstGeral.append(lstDado[:])
    lstDado.clear()

    if qtdCad == 0:
        maisPesado = peso
        maisLeve = peso
        lstPesado.append(nome)
        lstLeve.append(nome)
    else:
        if peso > maisPesado:
            maisPesado = peso
            lstPesado.clear()
            lstPesado.append(nome)
        elif peso == maisPesado:
            lstPesado.append(nome)
        elif peso < maisLeve:
            maisLeve = peso
            lstLeve.clear()
            lstLeve.append(nome)
        elif peso == maisLeve:
            lstLeve.append(nome)

    qtdCad += 1


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N:' )).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram Cadastrados {qtdCad} pessoas')
print(f'As pessoas mais pesadas tiveram {maisPesado:.2f}KG e foram {lstPesado}')
print(f'As pessoas mais leves tiveram {maisLeve:.2f}KG e foram {lstLeve}')
print()
print(f'Lista Geral: {lstGeral}')
