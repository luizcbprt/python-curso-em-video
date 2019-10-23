
print('-=' * 25)
print('{:-^50}'.format(' Analise de Dados em Tupla'))
print('-=' * 25)

n1 = n2 = n3 = n4 = 0

n1 = int(input('Informe o 1º numero: '))
n2 = int(input('Informe o 2º numero: '))
n3 = int(input('Informe o 3º numero: '))
n4 = int(input('Informe o 4º numero: '))

numeros = (n1, n2, n3, n4)

print(f'O numero 9 apareceu {numeros.count(9)} vezes')
print(f'O numero 3 está na posição {numeros.index(3,0) + 1}' if numeros.count(3) > 0 else 'Não foi informado 3')
print('Os numeros pares são: ', end='')
for par in numeros:
    if par % 2 == 0:
        print(par, end=' ')

print('-=' * 25)
print('{:-^50}'.format(' Analise de Dados em Tupla'))
print('-=' * 25)

n1 = n2 = n3 = n4 = 0

n1 = int(input('Informe o 1º numero: '))
n2 = int(input('Informe o 2º numero: '))
n3 = int(input('Informe o 3º numero: '))
n4 = int(input('Informe o 4º numero: '))

numeros = (n1, n2, n3, n4)

print(f'O numero 9 apareceu {numeros.count(9)} vezes')
print(f'O numero 3 está na posição {numeros.index(3,0) + 1}' if numeros.count(3) > 0 else 'Não foi informado 3')
print('Os numeros pares são: ', end='')
for par in numeros:
    if par % 2 == 0:
        print(par, end=' ')

