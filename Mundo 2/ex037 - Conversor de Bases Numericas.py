<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Conversor de Bases Numericas'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

numero = int(input('Informe um numero inteiro: '))
base = int(input('''Informe uma base numerica para conversão:
                  1 - Binário
                  2 - Octal
                  3 - Hexadecimal
                 '''))

if base == 1:
    resultado = bin(numero)
    print('{}O Numero {} convertido em Binário é {}{}'.format(cores['txAzul'], numero, resultado, cores['limpa']))
elif base == 2:
    resultado = oct(numero)
    print('{}O Numero {} convertido em Octal é {}{}'.format(cores['txVermelho'], numero, resultado, cores['limpa']))
elif base == 3:
    resultado = hex(numero)
    print('{}O Numero {} convertido em Hexadecimal é {}{}'.format(cores['txVerde'], numero, resultado, cores['limpa']))
else:
    print('Voce sabe ler? Então por que escolheu uma opção inválida?')
=======
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Conversor de Bases Numericas'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

numero = int(input('Informe um numero inteiro: '))
base = int(input('''Informe uma base numerica para conversão:
                  1 - Binário
                  2 - Octal
                  3 - Hexadecimal
                 '''))

if base == 1:
    resultado = bin(numero)
    print('{}O Numero {} convertido em Binário é {}{}'.format(cores['txAzul'], numero, resultado, cores['limpa']))
elif base == 2:
    resultado = oct(numero)
    print('{}O Numero {} convertido em Octal é {}{}'.format(cores['txVermelho'], numero, resultado, cores['limpa']))
elif base == 3:
    resultado = hex(numero)
    print('{}O Numero {} convertido em Hexadecimal é {}{}'.format(cores['txVerde'], numero, resultado, cores['limpa']))
else:
    print('Voce sabe ler? Então por que escolheu uma opção inválida?')
>>>>>>> Stashed changes
