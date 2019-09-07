def leiaInt(num=''):
    """
    -> Retorna mensagem de valor inválido enquanto nao for digitado um numero inteiro
    :param num: Numero recebido no parametro
    :return: retorna mensagem de erro caso nao seja digitado um numero inteiro
    """
    while not num.isnumeric():
        print('\033[0;31m', 'Nao foi digitado um numero inteiro!', '\033[m')
        num = input('Informe um Numero Inteiro: ')
    return num


numero = leiaInt(input('Informe um Numero Inteiro: '))

print('Voce Informou um numero inteiro. Obrigado')