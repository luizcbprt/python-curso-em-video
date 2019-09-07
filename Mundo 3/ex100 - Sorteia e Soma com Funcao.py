lista = []

def linha(texto):
    print('~' * len(texto))
    print(texto)
    if texto == ' ':
        print()
    else:
        print('~' * len(texto))


def sorteia():
    from random import randint
    print(f'Sorteando 5 valores. ', end='')
    for num in range(0,5):
        sorteado = randint(1,100)
        lista.append(sorteado)
        print(f'{sorteado}', end=' ')
    print('PRONTO')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {lista}. Resultado ', end='')
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'{soma}')



linha('Sorteio e Soma de Numeros com Funcao')

sorteia()

somaPar()