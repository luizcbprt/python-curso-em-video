def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um numero passado como parametro
    :param numero: Numero para calculo do Fatorial
    :param show: Parametro Opcional para mostrar ou não o calculo do fatorial
    :return: Retorna o Fatorial do numero
    """
    contador = numero
    resultado = 1
    while contador > 0:
        resultado *= contador
        if show == True:
            print(f'{contador} ', end='')
            if contador != 1:
                print('X', end=' ')
        contador -= 1
    print(f'= {resultado}')



fatorial(4)
fatorial(5, show=True)