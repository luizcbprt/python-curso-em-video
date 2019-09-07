<<<<<<< Updated upstream
print('-=' * 25)
print(' Lista Composta e Analise de Dados - Metodo 2')
print('-=' * 25)

lstPrinc = []
lstTemp = []
menorPeso = maiorPeso = 0

while True:
    lstTemp.append(str(input('Informe um Nome: ')))
    lstTemp.append(float(input('Informe um Peso: ')))

    if len(lstPrinc) == 0:
        maiorPeso = menorPeso = lstTemp[1] # Peso
    else:
        if lstTemp[1] > maiorPeso:
            maiorPeso = lstTemp[1]
        elif lstTemp[1] < menorPeso:
            menorPeso = lstTemp[1]

    lstPrinc.append(lstTemp[:])
    lstTemp.clear()


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Voce cadastrou {len(lstPrinc)} pessoas.')
print(f'O Maior peso foi {maiorPeso}KG. ', end='')
for tstPeso in lstPrinc:
    if tstPeso[1] == maiorPeso:
        print(f'{[tstPeso[0]]}', end='')
print()
print(f'O Menor peso foi {menorPeso}KG. ', end='')
for tstPeso in lstPrinc:
    if tstPeso[1] == menorPeso:
        print(f'{[tstPeso[0]]}', end='')
=======
print('-=' * 25)
print(' Lista Composta e Analise de Dados - Metodo 2')
print('-=' * 25)

lstPrinc = []
lstTemp = []
menorPeso = maiorPeso = 0

while True:
    lstTemp.append(str(input('Informe um Nome: ')))
    lstTemp.append(float(input('Informe um Peso: ')))

    if len(lstPrinc) == 0:
        maiorPeso = menorPeso = lstTemp[1] # Peso
    else:
        if lstTemp[1] > maiorPeso:
            maiorPeso = lstTemp[1]
        elif lstTemp[1] < menorPeso:
            menorPeso = lstTemp[1]

    lstPrinc.append(lstTemp[:])
    lstTemp.clear()


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Voce cadastrou {len(lstPrinc)} pessoas.')
print(f'O Maior peso foi {maiorPeso}KG. ', end='')
for tstPeso in lstPrinc:
    if tstPeso[1] == maiorPeso:
        print(f'{[tstPeso[0]]}', end='')
print()
print(f'O Menor peso foi {menorPeso}KG. ', end='')
for tstPeso in lstPrinc:
    if tstPeso[1] == menorPeso:
        print(f'{[tstPeso[0]]}', end='')
>>>>>>> Stashed changes
