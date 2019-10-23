
print('-=' * 25)
print(' Matriz em Python - Metodo 3')
print('-=' * 25)

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Infome o numero para [{linha},{coluna}]: '))
print()
print(matriz)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^7} ]', end='')
    print()

print('-=' * 25)
print(' Matriz em Python - Metodo 3')
print('-=' * 25)

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Infome o numero para [{linha},{coluna}]: '))
print()
print(matriz)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^7} ]', end='')
    print()
