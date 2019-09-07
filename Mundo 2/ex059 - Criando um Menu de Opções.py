<<<<<<< Updated upstream
print('==' * 25)
print('Menu de Opções'.center(50, ' '))
print('==' * 25)

num1 = float(input('Informe o Primeiro Numero: '))
num2 = float(input('Informe o Segundo Numero: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('''\nInforme a Opção Desejada:
    
    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do programa''')

    opcao = int(input('Informe a Opção: '))

    if opcao == 1:
        resultado = num1 + num2
        print('{} + {} = {}.'.format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            print('O Maior é {}'.format(num1))
        elif num2 > num1:
            print('O Maior é {}'.format(num2))
        else:
            print('Ambos são iguais.')
    elif opcao == 4:
        num1 = float(input('Informe um Novo Numero: '))
        num2 = float(input('Informe um Novo Numero: '))
=======
print('==' * 25)
print('Menu de Opções'.center(50, ' '))
print('==' * 25)

num1 = float(input('Informe o Primeiro Numero: '))
num2 = float(input('Informe o Segundo Numero: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('''\nInforme a Opção Desejada:
    
    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do programa''')

    opcao = int(input('Informe a Opção: '))

    if opcao == 1:
        resultado = num1 + num2
        print('{} + {} = {}.'.format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            print('O Maior é {}'.format(num1))
        elif num2 > num1:
            print('O Maior é {}'.format(num2))
        else:
            print('Ambos são iguais.')
    elif opcao == 4:
        num1 = float(input('Informe um Novo Numero: '))
        num2 = float(input('Informe um Novo Numero: '))
>>>>>>> Stashed changes
