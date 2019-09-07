<<<<<<< Updated upstream
print('-=' * 25)
print('Analise de Dados em Tupla'.center(50, ' '))
print('-=' * 25)

numeros = (int(input('Informe o 1º numero: ')),
           int(input('Informe o 2º numero: ')),
           int(input('Informe o 3º numero: ')),
           int(input('Informe o 4º numero: ')))

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 está na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não apareceu')
print(f'Os numeros pares são: ', end='')
for par in numeros:
    if par % 2 == 0:
        print(f'{par}', end='')
=======
print('-=' * 25)
print('Analise de Dados em Tupla'.center(50, ' '))
print('-=' * 25)

numeros = (int(input('Informe o 1º numero: ')),
           int(input('Informe o 2º numero: ')),
           int(input('Informe o 3º numero: ')),
           int(input('Informe o 4º numero: ')))

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 está na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não apareceu')
print(f'Os numeros pares são: ', end='')
for par in numeros:
    if par % 2 == 0:
        print(f'{par}', end='')
>>>>>>> Stashed changes
