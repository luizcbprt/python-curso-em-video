
from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print('{:=^50}'.format(''))
print('{:=^50}'.format('Game Pedra Papel e Tesoura'))
print('{:=^50}'.format(''))

usuario = int(input('''
Selecione sua opção para jogar:

[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
Qual voce escolhe? '''))

comp = randint(1, 3)

print(' Computador está Jogando')
sleep(1)

if usuario == 1 and comp == 2:
    print('Voce Jogou Pedra, mas o computador jogou Papel. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 1 and comp == 3:
    print('Voce Jogou Pedra, e o computador jogou Tesoura. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))
elif usuario == 2 and comp == 1:
    print('Você Jogou Papel, e o Computador jogou Pedra. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))
elif usuario == 2 and comp == 3:
    print('Você Jogou Papel, mas o Computador jogou Tesoura. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 3 and comp == 1:
    print('Você Jogou Tesoura, mas o Computador jogou Pedra. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 3 and comp == 2:
    print('Você Jogou Tesoura, e o Computador jogou Papel. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))

elif usuario == comp:
    print('Você e o Computador jogaram o Mesmo. ', end='')
    print('EMPATE!')

from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print('{:=^50}'.format(''))
print('{:=^50}'.format('Game Pedra Papel e Tesoura'))
print('{:=^50}'.format(''))

usuario = int(input('''
Selecione sua opção para jogar:

[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
Qual voce escolhe? '''))

comp = randint(1, 3)

print(' Computador está Jogando')
sleep(1)

if usuario == 1 and comp == 2:
    print('Voce Jogou Pedra, mas o computador jogou Papel. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 1 and comp == 3:
    print('Voce Jogou Pedra, e o computador jogou Tesoura. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))
elif usuario == 2 and comp == 1:
    print('Você Jogou Papel, e o Computador jogou Pedra. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))
elif usuario == 2 and comp == 3:
    print('Você Jogou Papel, mas o Computador jogou Tesoura. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 3 and comp == 1:
    print('Você Jogou Tesoura, mas o Computador jogou Pedra. ', end='')
    print('Você {}PERDEU{}!'.format(cores['txVermelho'], cores['limpa']))
elif usuario == 3 and comp == 2:
    print('Você Jogou Tesoura, e o Computador jogou Papel. ', end='')
    print('Você {}GANHOU{}!'.format(cores['txVerde'], cores['limpa']))

elif usuario == comp:
    print('Você e o Computador jogaram o Mesmo. ', end='')
    print('EMPATE!')

