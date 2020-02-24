
print('-=' * 25)
print(' Cadastro Jogador de Futebol '.center(50, '-'))
print('-=' * 25, '\n')

#Inicialização de variáveis
dctDadosJogador = {} #Dicionario
lstGols = [] #Lista

nome = str(input('Informe o Nome do Jogador: ')).strip().capitalize()
qtdJogos = int(input('Quantas partidas ele Jogou? '))

print('\n', '{:-^50}'.format(' QTD Gols em cada Partida '))
# For para ler a quantidade de Gols
for gols in range(qtdJogos):
    golsEfetuados = int(input(f'Gols efetuados na partida {gols}: '))
    lstGols.append(golsEfetuados)

totGols = sum(lstGols) #Soma da lista

# Armazena os dados captados no dicionário
dctDadosJogador.update({'nome':nome,
                        'gols':lstGols,
                        'total':totGols})

print(dctDadosJogador)
print('\n', '-*' * 25)
#Exibe os dados armazenados no Dicionario
for key, value in dctDadosJogador.items():
    print(f'O campo {key} tem valor: {value}')

print('\n', '-*' * 25)
#Exibe Detalhes de cada partida
print(f'O Jogador {dctDadosJogador["nome"]} jogou {len(dctDadosJogador["gols"])} partidas')

for pos, gols in enumerate(dctDadosJogador["gols"]):
    print(f'    => Na partida {pos}, fez {gols} gols.')
print(f'Foi um total de {dctDadosJogador["total"]} gols.')

print('-=' * 25)
print(' Cadastro Jogador de Futebol '.center(50, '-'))
print('-=' * 25, '\n')

#Inicialização de variáveis
dctDadosJogador = {} #Dicionario
lstGols = [] #Lista

nome = str(input('Informe o Nome do Jogador: ')).strip().capitalize()
qtdJogos = int(input('Quantas partidas ele Jogou? '))

print('\n', '{:-^50}'.format(' QTD Gols em cada Partida '))
# For para ler a quantidade de Gols
for gols in range(qtdJogos):
    golsEfetuados = int(input(f'Gols efetuados na partida {gols}: '))
    lstGols.append(golsEfetuados)

totGols = sum(lstGols) #Soma da lista

# Armazena os dados captados no dicionário
dctDadosJogador.update({'nome':nome,
                        'gols':lstGols,
                        'total':totGols})

print(dctDadosJogador)
print('\n', '-*' * 25)
#Exibe os dados armazenados no Dicionario
for key, value in dctDadosJogador.items():
    print(f'O campo {key} tem valor: {value}')

print('\n', '-*' * 25)
#Exibe Detalhes de cada partida
print(f'O Jogador {dctDadosJogador["nome"]} jogou {len(dctDadosJogador["gols"])} partidas')

for pos, gols in enumerate(dctDadosJogador["gols"]):
    print(f'    => Na partida {pos}, fez {gols} gols.')
print(f'Foi um total de {dctDadosJogador["total"]} gols.')



