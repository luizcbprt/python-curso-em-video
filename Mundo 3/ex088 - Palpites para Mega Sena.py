
from random import randint, choice
from time import sleep

print('-=' * 25)
print(' Palpites para a Mega Sena')
print('-=' * 25)

lstNumeros = list(range(1,61)) # Lista com os numeros para cada Jogo
qtdJogos = int(input('Quantos jogos você deseja Gerar: '))

lstJogos = [[0, 0, 0, 0, 0, 0] for _ in range(qtdJogos)]
for lstJogo in lstJogos:
    for numero in range(6):
        num = choice(lstNumeros) # Escolhe um numero da lista
        while True:
            # Troca os numeros caso estejam repetidos
            if num in lstJogo:
                num = choice(lstNumeros)
            else:
                lstJogo[numero] = num
                break

print('Gerando Jogos')
sleep(1)

#Ordena os numeros dentro de cada jogada
for jogo in range(len(lstJogos)):
    lstJogos[jogo].sort()
    print(f'Jogo {jogo+1}: ', end = '')
    sleep(0.5) # Aguarda entre
    print(lstJogos[jogo])

print('FIM')

from random import randint, choice
from time import sleep

print('-=' * 25)
print(' Palpites para a Mega Sena')
print('-=' * 25)

lstNumeros = list(range(1,61)) # Lista com os numeros para cada Jogo
qtdJogos = int(input('Quantos jogos você deseja Gerar: '))

lstJogos = [[0, 0, 0, 0, 0, 0] for _ in range(qtdJogos)]
for lstJogo in lstJogos:
    for numero in range(6):
        num = choice(lstNumeros) # Escolhe um numero da lista
        while True:
            # Troca os numeros caso estejam repetidos
            if num in lstJogo:
                num = choice(lstNumeros)
            else:
                lstJogo[numero] = num
                break

print('Gerando Jogos')
sleep(1)

#Ordena os numeros dentro de cada jogada
for jogo in range(len(lstJogos)):
    lstJogos[jogo].sort()
    print(f'Jogo {jogo+1}: ', end = '')
    sleep(0.5) # Aguarda entre
    print(lstJogos[jogo])

print('FIM')

