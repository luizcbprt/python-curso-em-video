
print('-=' * 25)
print(' Cadastro de Pessoas com Estatística '.center(50, ' '))
print('-=' * 25)

#Inicializacao de Variaveis
lstPessoas = []
dctPessoa = {}

while True:
    #Leitura dos Dados
    nome = str(input('Informe o Nome: ')).strip().capitalize()
    idade = int(input('Informe a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o Sexo (M/F)')).strip().upper()[0]

    dctPessoa.update({'nome':nome,
                      'idade':idade,
                      'sexo':sexo})
    lstPessoas.append(dctPessoa.copy())


    #Verificacao de Continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\n', '-*' * 25)
print(f'Ao total foram cadastradas {len(lstPessoas)} pessoas.')

#Calcula Media de Idade
totIdade = 0
for pessoa in lstPessoas:
    totIdade += pessoa["idade"]
mediaIdade = totIdade / len(lstPessoas)
print(f'A Media de Idade foi {mediaIdade:.2f} anos')

#Exibe Mulheres
print('As mulheres cadastradas foram: ', end='')
for pessoa in lstPessoas:
    if pessoa["sexo"] == 'F':
        print(pessoa["nome"], end=' ')

#Exibe pessoas acima da média de Idade
print('\n', 'Lista das Pessoas que estão acima da Média: ')
for pessoa in lstPessoas:
    if pessoa["idade"] > mediaIdade:
        print(pessoa)

print('-=' * 25)
print(' Cadastro de Pessoas com Estatística '.center(50, ' '))
print('-=' * 25)

#Inicializacao de Variaveis
lstPessoas = []
dctPessoa = {}

while True:
    #Leitura dos Dados
    nome = str(input('Informe o Nome: ')).strip().capitalize()
    idade = int(input('Informe a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o Sexo (M/F)')).strip().upper()[0]

    dctPessoa.update({'nome':nome,
                      'idade':idade,
                      'sexo':sexo})
    lstPessoas.append(dctPessoa.copy())


    #Verificacao de Continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\n', '-*' * 25)
print(f'Ao total foram cadastradas {len(lstPessoas)} pessoas.')

#Calcula Media de Idade
totIdade = 0
for pessoa in lstPessoas:
    totIdade += pessoa["idade"]
mediaIdade = totIdade / len(lstPessoas)
print(f'A Media de Idade foi {mediaIdade:.2f} anos')

#Exibe Mulheres
print('As mulheres cadastradas foram: ', end='')
for pessoa in lstPessoas:
    if pessoa["sexo"] == 'F':
        print(pessoa["nome"], end=' ')

#Exibe pessoas acima da média de Idade
print('\n', 'Lista das Pessoas que estão acima da Média: ')
for pessoa in lstPessoas:
    if pessoa["idade"] > mediaIdade:
        print(pessoa)


