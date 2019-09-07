def linha(texto):
    print('-=' * 25)
    print(str(texto).center(50, ' '))
    print()


def maior(*valores):
    from time import sleep
    print(f'Analisando os Valores informados...')
    sleep(0.3)
    print(f'{valores}. Foram informados {len(valores)} valores.')
    sleep(0.3)
    for pos, val in enumerate(valores):
        if pos == 0:
            maior = val
        else:
            if val > maior:
                maior = val
    sleep(0.3)
    print(f'O maior valor foi {maior}')
    sleep(0.3)
    print()


linha('Funcao Maior com empacotamento de parametros')

maior(1,5,8,7)

maior(9,1)

maior(7)