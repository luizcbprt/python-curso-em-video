def contador(ini, fim, passo):
    from time import sleep
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    print(f'Contagem de {ini} a {fim} de {passo} em {passo}')
    if ini < fim:  # Se Inicio MENOR que FIM
        for cont in range(ini, fim+passo, passo):
            sleep(0.3)
            print(f'{cont}', end=' ')
    elif (ini > fim) and (passo > 0):  # Se Inicio MAIOR que FIM e passo positivo
        for cont in range(ini, fim-passo, passo*-1):
            sleep(0.3)
            print(f'{cont}', end=' ')
    print('FIM')


def linhaSepara(texto):
    print('-=' * 25)
    print(texto)


# Main Program
linhaSepara('Programa Contador com Funcao')


linhaSepara('Conta de 1 a 10 com passo 1')
contador(1,10,1)

linhaSepara('Conta de 10 a 0 com passo 2')
contador(10, 1, 2)

linhaSepara('Agora é sua vez de Personalizar')
inicio = int(input('Informe o Inicio: '))
fim = int(input('Informe o Final: '))
passo = int(input('Informe o Passo: '))

contador(inicio, fim, passo)
