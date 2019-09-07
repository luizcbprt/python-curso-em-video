<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m'}
print('-=' * 25)
print(f'{cores["txVermelho"]}Jogo de Dados em Python{cores["limpa"]}'.center(50, ' '))
print('-=' * 25)

from random import randint
from time import sleep
from operator import itemgetter

print('-- Jogando --'.center(50, ' '))
sleep(0.5)

jogadores = {}
for j in range(1,5):
    numero = randint(1,6)
    print(f'O jogador{j} tirou {numero}')
    jogadores.update({f'jogador{j}':numero})
    sleep(0.5)
print()
print('{:^50}'.format(' RANKING '))

#Ordena o Dicionario usando a funcao build-in SORTED e o pacote operator
ordenado = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

for pos, jogador in enumerate(ordenado):
    sleep(0.5)
    print(f'{pos + 1}º Lugar: {jogador[0]} com {jogador[1]}')
print()
print('FIM')
=======
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m'}
print('-=' * 25)
print(f'{cores["txVermelho"]}Jogo de Dados em Python{cores["limpa"]}'.center(50, ' '))
print('-=' * 25)

from random import randint
from time import sleep
from operator import itemgetter

print('-- Jogando --'.center(50, ' '))
sleep(0.5)

jogadores = {}
for j in range(1,5):
    numero = randint(1,6)
    print(f'O jogador{j} tirou {numero}')
    jogadores.update({f'jogador{j}':numero})
    sleep(0.5)
print()
print('{:^50}'.format(' RANKING '))

#Ordena o Dicionario usando a funcao build-in SORTED e o pacote operator
ordenado = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

for pos, jogador in enumerate(ordenado):
    sleep(0.5)
    print(f'{pos + 1}º Lugar: {jogador[0]} com {jogador[1]}')
print()
print('FIM')
>>>>>>> Stashed changes
