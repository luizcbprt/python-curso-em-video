
from random import randint

print('=-' * 25)
print('Jogo do PAR ou ÍMPAR')
print('=-' * 25)
print('\n Vamos Jogar Par ou Ímpar')

cont = jogadas = num_pc = 0
while True:
    num_user = int(input('Digite um Numero: '))
    escolha = input('Par ou Ímpar? [P/I]').upper().strip()[0]
    cont += 1
    print('\n')
    num_pc = randint(1,11)
    if escolha == 'P':
        if (num_user + num_pc) % 2 == 0:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu PAR')
            print('Você VENCEU')
            print('Vamos jogar Novamente \n')
            jogadas += 1
        else:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu ÍMPAR')
            break
    if escolha == 'I':
        if (num_user + num_pc) % 2 != 0:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu ÍMPAR')
            print('Você VENCEU')
            print('Vamos jogar Novamente \n')
            jogadas += 1
        else:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu PAR')
            break
print('--' * 25)
print('Você PERDEU')
print(f'Você ganhou {jogadas} vezes!')
print(f'Total de Jogadas = {cont}')

from random import randint

print('=-' * 25)
print('Jogo do PAR ou ÍMPAR')
print('=-' * 25)
print('\n Vamos Jogar Par ou Ímpar')

cont = jogadas = num_pc = 0
while True:
    num_user = int(input('Digite um Numero: '))
    escolha = input('Par ou Ímpar? [P/I]').upper().strip()[0]
    cont += 1
    print('\n')
    num_pc = randint(1,11)
    if escolha == 'P':
        if (num_user + num_pc) % 2 == 0:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu PAR')
            print('Você VENCEU')
            print('Vamos jogar Novamente \n')
            jogadas += 1
        else:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu ÍMPAR')
            break
    if escolha == 'I':
        if (num_user + num_pc) % 2 != 0:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu ÍMPAR')
            print('Você VENCEU')
            print('Vamos jogar Novamente \n')
            jogadas += 1
        else:
            print(f'Você jogou {num_user} e o computador {num_pc}. Total de {num_user + num_pc} deu PAR')
            break
print('--' * 25)
print('Você PERDEU')
print(f'Você ganhou {jogadas} vezes!')
print(f'Total de Jogadas = {cont}')

