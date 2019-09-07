<<<<<<< Updated upstream
print('-=' * 25)
print(' Cadastro Jogador de Futebol '.center(50, '-'))
print('-=' * 25, '\n')

#Inicialização de variáveis
dctDadosJogador = {} #Dicionario
lstGols = [] #Lista
lstJogadores = [] #Lista

while True:
    nome = str(input('Informe o Nome do Jogador: ')).strip().capitalize()
    qtdJogos = int(input('Quantas partidas ele Jogou? '))

    print('\n', '{:-^50}'.format(' QTD Gols em cada Partida '))
    # For para ler a quantidade de Gols
    for gols in range(0,qtdJogos):
        golsEfetuados = int(input(f'Gols efetuados na partida {gols}: '))
        lstGols.append(golsEfetuados)

    totGols = sum(lstGols) #Soma da lista

    # Armazena os dados capturados
    dctDadosJogador.update({'nome':nome,
                            'gols':lstGols.copy(),
                            'total':totGols})
    lstJogadores.append(dctDadosJogador.copy())

    #Limpa Variaveis
    dctDadosJogador.clear()
    totGols = 0
    lstGols.clear()

    #Verificacao de continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N) ')).strip().upper()[0]
    if continuar == 'N':
        break

print(lstJogadores)

#Parte 2 - Exibição de Detalhes dos Jogadores
print('\n', '-*' * 25)
print(f'{"cod":>3} {"Nome":<15} {"gols":<20} {"total":<5}')
for pos, jogador in enumerate(lstJogadores):
    print(f'{pos:>3}', end=' ')
    print(f'{jogador["nome"]:<15}', end='')
    print(f'{jogador["gols"]}', end='')
    print(f'{jogador["total"]:<5}')
=======
print('-=' * 25)
print(' Cadastro Jogador de Futebol '.center(50, '-'))
print('-=' * 25, '\n')

#Inicialização de variáveis
dctDadosJogador = {} #Dicionario
lstGols = [] #Lista
lstJogadores = [] #Lista

while True:
    nome = str(input('Informe o Nome do Jogador: ')).strip().capitalize()
    qtdJogos = int(input('Quantas partidas ele Jogou? '))

    print('\n', '{:-^50}'.format(' QTD Gols em cada Partida '))
    # For para ler a quantidade de Gols
    for gols in range(0,qtdJogos):
        golsEfetuados = int(input(f'Gols efetuados na partida {gols}: '))
        lstGols.append(golsEfetuados)

    totGols = sum(lstGols) #Soma da lista

    # Armazena os dados capturados
    dctDadosJogador.update({'nome':nome,
                            'gols':lstGols.copy(),
                            'total':totGols})
    lstJogadores.append(dctDadosJogador.copy())

    #Limpa Variaveis
    dctDadosJogador.clear()
    totGols = 0
    lstGols.clear()

    #Verificacao de continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N) ')).strip().upper()[0]
    if continuar == 'N':
        break

print(lstJogadores)

#Parte 2 - Exibição de Detalhes dos Jogadores
print('\n', '-*' * 25)
print(f'{"cod":>3} {"Nome":<15} {"gols":<20} {"total":<5}')
for pos, jogador in enumerate(lstJogadores):
    print(f'{pos:>3}', end=' ')
    print(f'{jogador["nome"]:<15}', end='')
    print(f'{jogador["gols"]}', end='')
    print(f'{jogador["total"]:<5}')
>>>>>>> Stashed changes
