
print('-=' * 25)
print(' Boletim com Listas Compostas ')
print('-=' * 25)

lstBoletim = []
lstTemp = []

while True:

    nome = str(input('Informe o nome do Aluno: ')).capitalize().strip()
    nota1 = float(input('Informe a 1º Nota do aluno: '))
    nota2 = float(input('Informe a 2º Nota do aluno: '))
    # Armazena dados em uma lista temporária para facilitar a organizaçao
    lstTemp.append(nome)
    lstTemp.append([nota1, nota2])

    # Faz o Append da lista temporaria para a principal, e limpa o conteudo
    lstBoletim.append(lstTemp[:])
    lstTemp.clear()

    # Clausura para Parar o Loop que faz leitura dos Alunos
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
# Termino da Insercao de Dados

print('-=' * 25)
# Inicio dos Calculos e exibição
print('No.   Nome         Media')
for pos, aluno in enumerate(lstBoletim):
    media = ntTotal = 0
    for notas in aluno[1]: # Mostra as notas
        ntTotal += notas
    media = ntTotal / 2
    #print(f'Aluno: {aluno[0]} teve media: {media:.2f}')
    print(f'{pos:<6}', end='')
    print(f'{aluno[0]:<13}', end='')
    print(f'{media:<6.2f}')

print()

while True:
    resp = ' '
    print('Informe um aluno para ver as notas ou 999 para Sair: ')
    for pos, aluno in enumerate(lstBoletim):
        print(f'{pos} - {aluno[0]}')


    resp = int(input('Opção: '))
    if resp == 999:
        break

    for pos, aluno in enumerate(lstBoletim): # Itera a lista pegando os alunos e notas
        if pos == resp: # Se a posição na lista é igual a resposta mostra o resultado
            print(f'Aluno: {aluno[0]}') # Posicao 0 = nome do aluno
            for pos, notas in enumerate(aluno[1]): # Posicao 1 = lista com notas
                print(f'{pos+1}º Nota: {notas}')
            print()
            print()
print()
print(' FIM DO PROGRAMA')

print('-=' * 25)
print(' Boletim com Listas Compostas ')
print('-=' * 25)

lstBoletim = []
lstTemp = []

while True:

    nome = str(input('Informe o nome do Aluno: ')).capitalize().strip()
    nota1 = float(input('Informe a 1º Nota do aluno: '))
    nota2 = float(input('Informe a 2º Nota do aluno: '))
    # Armazena dados em uma lista temporária para facilitar a organizaçao
    lstTemp.append(nome)
    lstTemp.append([nota1, nota2])

    # Faz o Append da lista temporaria para a principal, e limpa o conteudo
    lstBoletim.append(lstTemp[:])
    lstTemp.clear()

    # Clausura para Parar o Loop que faz leitura dos Alunos
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
# Termino da Insercao de Dados

print('-=' * 25)
# Inicio dos Calculos e exibição
print('No.   Nome         Media')
for pos, aluno in enumerate(lstBoletim):
    media = ntTotal = 0
    for notas in aluno[1]: # Mostra as notas
        ntTotal += notas
    media = ntTotal / 2
    #print(f'Aluno: {aluno[0]} teve media: {media:.2f}')
    print(f'{pos:<6}', end='')
    print(f'{aluno[0]:<13}', end='')
    print(f'{media:<6.2f}')

print()

while True:
    resp = ' '
    print('Informe um aluno para ver as notas ou 999 para Sair: ')
    for pos, aluno in enumerate(lstBoletim):
        print(f'{pos} - {aluno[0]}')


    resp = int(input('Opção: '))
    if resp == 999:
        break

    for pos, aluno in enumerate(lstBoletim): # Itera a lista pegando os alunos e notas
        if pos == resp: # Se a posição na lista é igual a resposta mostra o resultado
            print(f'Aluno: {aluno[0]}') # Posicao 0 = nome do aluno
            for pos, notas in enumerate(aluno[1]): # Posicao 1 = lista com notas
                print(f'{pos+1}º Nota: {notas}')
            print()
            print()
print()
print(' FIM DO PROGRAMA')

