
from random import randint

print('-=' * 25)
print('{:-^50}'.format(' Maior e Menor Valores em Tupla'))
print('-=' * 25)

numeros = ''
num = 0
for i in range(0, 5):
    num = randint(1, 10)
    numeros +=  str(num)
numTupla = tuple(numeros)

print(f'A Listagem aleatória é: {numTupla}')
print(f'O maior valor é {max(numTupla)}')
print(f'O menor valor é {min(numTupla)}')

from random import randint

print('-=' * 25)
print('{:-^50}'.format(' Maior e Menor Valores em Tupla'))
print('-=' * 25)

numeros = ''
num = 0
for i in range(0, 5):
    num = randint(1, 10)
    numeros +=  str(num)
numTupla = tuple(numeros)

print(f'A Listagem aleatória é: {numTupla}')
print(f'O maior valor é {max(numTupla)}')
print(f'O menor valor é {min(numTupla)}')

