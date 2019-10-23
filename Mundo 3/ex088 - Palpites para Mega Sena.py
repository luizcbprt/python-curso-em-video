
from random import randint, choice
from time import sleep

print('-=' * 25)
print(' Palpites para a Mega Sena')
print('-=' * 25)

lstJogos = []
lstNumeros = list(range(1,61)) # Lista com os numeros para cada Jogo
qtdJogos = int(input('Quantos jogos você deseja Gerar: '))

# Cria a lista vazia com a quantidade de jogos escolhida
for criaJogos in range(0, qtdJogos):
    lstJogos.append([0, 0, 0, 0, 0, 0])

for jogada in range(0, len(lstJogos)):
    for numero in range(0, 6):
        num = choice(lstNumeros) # Escolhe um numero da lista
        while True:
            # Troca os numeros caso estejam repetidos
            if num in lstJogos[jogada]:
                num = choice(lstNumeros)
            else:
                lstJogos[jogada][numero] = num
                break

print('Gerando Jogos')
sleep(1)

#Ordena os numeros dentro de cada jogada
for jogo in range(0, len(lstJogos)):
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

lstJogos = []
lstNumeros = list(range(1,61)) # Lista com os numeros para cada Jogo
qtdJogos = int(input('Quantos jogos você deseja Gerar: '))

# Cria a lista vazia com a quantidade de jogos escolhida
for criaJogos in range(0, qtdJogos):
    lstJogos.append([0, 0, 0, 0, 0, 0])

for jogada in range(0, len(lstJogos)):
    for numero in range(0, 6):
        num = choice(lstNumeros) # Escolhe um numero da lista
        while True:
            # Troca os numeros caso estejam repetidos
            if num in lstJogos[jogada]:
                num = choice(lstNumeros)
            else:
                lstJogos[jogada][numero] = num
                break

print('Gerando Jogos')
sleep(1)

#Ordena os numeros dentro de cada jogada
for jogo in range(0, len(lstJogos)):
    lstJogos[jogo].sort()
    print(f'Jogo {jogo+1}: ', end = '')
    sleep(0.5) # Aguarda entre
    print(lstJogos[jogo])

print('FIM')

