
print('-=' * 25)
print(' Lista com Pares e Ímpares')
print('-=' * 25)

lstGeral = [[],[]]

for indice in range(1,8):
    num = int(input(f'Informe o {indice}º valor: '))

    if num % 2 == 0:
        lstGeral[0].append(num)
    else:
        lstGeral[1].append(num)
lstGeral[0].sort()
lstGeral[1].sort()
print(f'A lista de Pares foi: {lstGeral[0]}')
print(f'A lista de Ímpares foi: {lstGeral[1]}')

print('-=' * 25)
print(' Lista com Pares e Ímpares')
print('-=' * 25)

lstGeral = [[],[]]

for indice in range(1,8):
    num = int(input(f'Informe o {indice}º valor: '))

    if num % 2 == 0:
        lstGeral[0].append(num)
    else:
        lstGeral[1].append(num)
lstGeral[0].sort()
lstGeral[1].sort()
print(f'A lista de Pares foi: {lstGeral[0]}')
print(f'A lista de Ímpares foi: {lstGeral[1]}')
