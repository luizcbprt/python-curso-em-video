<<<<<<< Updated upstream
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética - While'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
cont = 0

while cont < 10:
    print('{} ->'.format(soma), end=' ')
    soma += razao
    cont += 1
print('\nSoma total da PA: {}'.format(soma))
=======
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética - While'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
cont = 0

while cont < 10:
    print('{} ->'.format(soma), end=' ')
    soma += razao
    cont += 1
print('\nSoma total da PA: {}'.format(soma))
>>>>>>> Stashed changes
