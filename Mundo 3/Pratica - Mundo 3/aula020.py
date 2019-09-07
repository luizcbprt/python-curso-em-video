def linha():
    print()
    print('-=' * 25)

def titulo(mensagem):
    print('-=' * 25)
    print(mensagem)
    print('-=' * 25)


titulo('Titulo do Programa')

linha()

def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A Soma é {s}')

soma(b=4, a=6)
soma(2, 3)

linha()

#Empacotamento de Parametros
def contador(*num):
    for valores in num:
        print(f'{valores} ', end='')
    print('FIM')

contador(4, 5, 6)
contador(1,5,7,9,3)

linha()

def numeros(*num):
    tamanho = len(num)
    print(f'Recebi os numeros {num}, e o tamanho é {tamanho}')

numeros(4,5,6)