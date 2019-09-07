<<<<<<< Updated upstream
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = 0
contador = 0
for cont in range(1, 11):
    contador += 1
    if cont == 1:
        soma += prim_termo + razao
    else:
        soma += razao
    print('{} ->'.format(soma), end=' ')
print('\nSoma total da PA: {}'.format(soma))
=======
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = 0
contador = 0
for cont in range(1, 11):
    contador += 1
    if cont == 1:
        soma += prim_termo + razao
    else:
        soma += razao
    print('{} ->'.format(soma), end=' ')
print('\nSoma total da PA: {}'.format(soma))
>>>>>>> Stashed changes
