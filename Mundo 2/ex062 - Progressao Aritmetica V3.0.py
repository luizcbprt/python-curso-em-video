
print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética V3.0'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
termo = 1
qtd = 0
for _ in range(10):
    print('{} ->'.format(soma), end=' ')
    soma += razao
    qtd += 1
print('\nSoma total da PA: {}'.format(soma))
while termo != 0:
    termo = int(
        input('Deseja mostrar mais resultados? Informe quantos, 0 para Sair')
    )
    if termo != 0:
        for _ in range(termo, 0, -1):
            soma += razao
            print('{} ->'.format(soma), end=' ')
    qtd += 1

print('\nSoma total da PA: {}'.format(soma))
print('Progressão Finalizada com {} termos mostrados'.format(qtd))

print('==' * 25)
print('{:^50}'.format(' Progressão Aritmética V3.0'))
print('==' * 25)

prim_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

soma = prim_termo
termo = 1
qtd = 0
for _ in range(10):
    print('{} ->'.format(soma), end=' ')
    soma += razao
    qtd += 1
print('\nSoma total da PA: {}'.format(soma))
while termo != 0:
    termo = int(
        input('Deseja mostrar mais resultados? Informe quantos, 0 para Sair')
    )
    if termo != 0:
        for _ in range(termo, 0, -1):
            soma += razao
            print('{} ->'.format(soma), end=' ')
    qtd += 1

print('\nSoma total da PA: {}'.format(soma))
print('Progressão Finalizada com {} termos mostrados'.format(qtd))

