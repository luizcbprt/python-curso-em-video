
print('-=' * 25)
print(' Extraindo dados de uma lista '.center(50, ' '))
print('-=' * 25)

lista = []
continuar = ' '
qtdDigit = 0

while True:
    num = int(input('Informe um numero: '))

    lista.append(num)
    qtdDigit += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Fora digitados {qtdDigit} numeros!')
#print(f'Fora digitados {len(lista)} numeros!')
lista.sort(reverse=True)
print(f'A lista ao contrario é: {lista}')
if 5 in lista:
    print('O Numero 5 está na lista')
else:
    print('O numero 5 NAO foi digitado')

print('-=' * 25)
print(' Extraindo dados de uma lista '.center(50, ' '))
print('-=' * 25)

lista = []
continuar = ' '
qtdDigit = 0

while True:
    num = int(input('Informe um numero: '))

    lista.append(num)
    qtdDigit += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Fora digitados {qtdDigit} numeros!')
#print(f'Fora digitados {len(lista)} numeros!')
lista.sort(reverse=True)
print(f'A lista ao contrario é: {lista}')
if 5 in lista:
    print('O Numero 5 está na lista')
else:
    print('O numero 5 NAO foi digitado')

