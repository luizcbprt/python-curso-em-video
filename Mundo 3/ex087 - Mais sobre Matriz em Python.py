<<<<<<< Updated upstream
print('-=' * 25)
print(' Mais sobre Matriz em Python ')
print('-=' * 25)

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPar = somaCol3 = maiorLinha2 = 0

for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Infome o numero para [{linha},{coluna}]: '))
        matriz[linha][coluna] = num
        if num % 2 == 0: # Soma os Pares
            somaPar += num
        if coluna == 2: #Soma os Valores da Terceira Coluna
            somaCol3 += num
        if linha == 1 and coluna == 0: # Armazena o Maior valor da 2º Linha
            maiorLinha2 = num
        elif linha == 1:
            if num > maiorLinha2:
                maiorLinha2 = num

print('--' * 25)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()
print('--' * 25)
print(f'A soma dos Pares é {somaPar}')
print(f'A soma da 3º Coluna é: {somaCol3}')
print(f'O Maior valor da 2º Linha foi: {maiorLinha2}')
=======
print('-=' * 25)
print(' Mais sobre Matriz em Python ')
print('-=' * 25)

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPar = somaCol3 = maiorLinha2 = 0

for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Infome o numero para [{linha},{coluna}]: '))
        matriz[linha][coluna] = num
        if num % 2 == 0: # Soma os Pares
            somaPar += num
        if coluna == 2: #Soma os Valores da Terceira Coluna
            somaCol3 += num
        if linha == 1 and coluna == 0: # Armazena o Maior valor da 2º Linha
            maiorLinha2 = num
        elif linha == 1:
            if num > maiorLinha2:
                maiorLinha2 = num

print('--' * 25)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()
print('--' * 25)
print(f'A soma dos Pares é {somaPar}')
print(f'A soma da 3º Coluna é: {somaCol3}')
print(f'O Maior valor da 2º Linha foi: {maiorLinha2}')
>>>>>>> Stashed changes
