<<<<<<< Updated upstream
from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m'}

print(cores['txAzul'], '==' * 25, cores['limpa'])
print('{:^50}'.format(' Jogo da Adivinhação V2.0'))
print(cores['txAzul'], '==' * 25, cores['limpa'])

sleep(0.5)
print(' ... Estou Pensando em um Número .. ')
sleep(0.2)
print('.')
sleep(0.2)
print('..')
sleep(0.2)
print('...')
sleep(0.2)
print('Qual Numero eu Pensei? Está entre 0 e 10')

num_pc = randint(0,10)
num_user = int(input('Informe um numero entre 0 e 10: '))
tentativas = 0

while num_pc != num_user:
    if num_pc != num_user:
        print(cores['txVermelho'], 'ERROU!', cores['limpa'], end=' ')
        print('Eu pensei {}, e voce disse {}'.format(num_pc, num_user))
        tentativas += 1
        num_pc = randint(0,10)
        num_user = int(input('Informe um novo numero para tentar (0..10): '))

print(cores['txVerde'], 'VENCEU!', cores['limpa'], end=' ')
print('Eu pensei {}, e voce acertou'.format(num_pc))
print('Foram Necessárias {} tentativas até você ganhar'.format(tentativas))
=======
from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m'}

print(cores['txAzul'], '==' * 25, cores['limpa'])
print('{:^50}'.format(' Jogo da Adivinhação V2.0'))
print(cores['txAzul'], '==' * 25, cores['limpa'])

sleep(0.5)
print(' ... Estou Pensando em um Número .. ')
sleep(0.2)
print('.')
sleep(0.2)
print('..')
sleep(0.2)
print('...')
sleep(0.2)
print('Qual Numero eu Pensei? Está entre 0 e 10')

num_pc = randint(0,10)
num_user = int(input('Informe um numero entre 0 e 10: '))
tentativas = 0

while num_pc != num_user:
    if num_pc != num_user:
        print(cores['txVermelho'], 'ERROU!', cores['limpa'], end=' ')
        print('Eu pensei {}, e voce disse {}'.format(num_pc, num_user))
        tentativas += 1
        num_pc = randint(0,10)
        num_user = int(input('Informe um novo numero para tentar (0..10): '))

print(cores['txVerde'], 'VENCEU!', cores['limpa'], end=' ')
print('Eu pensei {}, e voce acertou'.format(num_pc))
print('Foram Necessárias {} tentativas até você ganhar'.format(tentativas))
>>>>>>> Stashed changes
