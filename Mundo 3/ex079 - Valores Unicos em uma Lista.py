<<<<<<< Updated upstream
print('-=' * 25)
print('Valoes Unicos em uma Lista'.center(50, ' '))
print('-=' * 25)

lista = []
while True:
    opcao = valor = ' '
    valor = int(input('Informe um Valor: '))
    if valor in lista:
        print('Valor Duplicado. Não irei adicionar!')
    else:
        print(f'Valor {valor} adicionado')
        lista.append(valor)

    while opcao not in 'SN':
        opcao = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
lista.sort()
print(f'A lista é: {lista}')
print('FIM DO PROGRAMA')
=======
print('-=' * 25)
print('Valoes Unicos em uma Lista'.center(50, ' '))
print('-=' * 25)

lista = []
while True:
    opcao = valor = ' '
    valor = int(input('Informe um Valor: '))
    if valor in lista:
        print('Valor Duplicado. Não irei adicionar!')
    else:
        print(f'Valor {valor} adicionado')
        lista.append(valor)

    while opcao not in 'SN':
        opcao = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
lista.sort()
print(f'A lista é: {lista}')
print('FIM DO PROGRAMA')
>>>>>>> Stashed changes
