<<<<<<< Updated upstream
print('-=' * 25)
print(' Matriz em Python - Metodo 2')
print('-=' * 25)

matriz = [[], [], []]

for coluna in range(0, 3):
    matriz[coluna].append(input(f'informe a linha {coluna}: '))
    for linha in range(0,2):
        matriz[coluna].append(input(f'Informe a coluna {linha}º: '))

for indice in matriz[0]:
    print(f'[ {indice} ]', end='')
print()
for indice in matriz[1]:
    print(f'[ {indice} ]', end='')
print()
for indice in matriz[2]:
    print(f'[ {indice} ]', end='')
=======
print('-=' * 25)
print(' Matriz em Python - Metodo 2')
print('-=' * 25)

matriz = [[], [], []]

for coluna in range(0, 3):
    matriz[coluna].append(input(f'informe a linha {coluna}: '))
    for linha in range(0,2):
        matriz[coluna].append(input(f'Informe a coluna {linha}º: '))

for indice in matriz[0]:
    print(f'[ {indice} ]', end='')
print()
for indice in matriz[1]:
    print(f'[ {indice} ]', end='')
print()
for indice in matriz[2]:
    print(f'[ {indice} ]', end='')
