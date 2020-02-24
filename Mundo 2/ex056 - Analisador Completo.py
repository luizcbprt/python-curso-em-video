
print('==' * 25)
print('{:^50}'.format(' Analisador Completo'))
print('==' * 25)

medIdade = 0
maisVelho = 0
nomeMaisVelho = ''
qtdMulher = 0

for pess in range(1, 5):
    nome = str(input('Informe o Nome: '))
    idade = int(input('Informe a Idade: '))
    sexo = str(input('Informe o Sexo (M/F): ').upper())

    if (idade == 1) or (idade > maisVelho):
        maisVelho = idade
        nomeMaisVelho = nome
    medIdade += idade
    if sexo == 'F':
        qtdMulher += 1

print('A pessoa Mais Velha tem {} anos, seu nome é {}'.format(maisVelho, nomeMaisVelho))
print('A Media de Idades é {}'.format(medIdade // 4))
print('A quantidade de Mulheres é {}'.format(qtdMulher))

print('==' * 25)
print('{:^50}'.format(' Analisador Completo'))
print('==' * 25)

medIdade = 0
maisVelho = 0
nomeMaisVelho = ''
qtdMulher = 0

for _ in range(1, 5):
    nome = str(input('Informe o Nome: '))
    idade = int(input('Informe a Idade: '))
    sexo = str(input('Informe o Sexo (M/F): ').upper())

    if (idade == 1) or (idade > maisVelho):
        maisVelho = idade
        nomeMaisVelho = nome
    medIdade += idade
    if sexo == 'F':
        qtdMulher += 1

print('A pessoa Mais Velha tem {} anos, seu nome é {}'.format(maisVelho, nomeMaisVelho))
print('A Media de Idades é {}'.format(medIdade // 4))
print('A quantidade de Mulheres é {}'.format(qtdMulher))

