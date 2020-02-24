
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética - While'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
for cont in range(10):
    print('{} ->'.format(soma), end=' ')
    soma += razao
print('\nSoma total da PA: {}'.format(soma))

print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética - While'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
for _ in range(10):
    print('{} ->'.format(soma), end=' ')
    soma += razao
print('\nSoma total da PA: {}'.format(soma))

