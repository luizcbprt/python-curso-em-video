
print('-=' * 25)
print('Dividindo Valores em Varias Listas'.center(50, ' '))
print('-=' * 25)

lstGeral = []
lstPar = []
lstImpar = []

while True:
    num = int(input('Informe um Numero: '))

    lstGeral.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break

for valor in lstGeral:
    if valor % 2 == 0:
        lstPar.append(valor)
    else:
        lstImpar.append(valor)

print(f'A lista Geral é: {lstGeral}')
print(f'Os Pares são: {lstPar}')
print(f'A lista Impar é: {lstImpar}')

print('-=' * 25)
print('Dividindo Valores em Varias Listas'.center(50, ' '))
print('-=' * 25)

lstGeral = []
lstPar = []
lstImpar = []

while True:
    num = int(input('Informe um Numero: '))

    lstGeral.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break

for valor in lstGeral:
    if valor % 2 == 0:
        lstPar.append(valor)
    else:
        lstImpar.append(valor)

print(f'A lista Geral é: {lstGeral}')
print(f'Os Pares são: {lstPar}')
print(f'A lista Impar é: {lstImpar}')

