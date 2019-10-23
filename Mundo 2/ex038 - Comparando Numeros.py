
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txAmarelo':'\033[1;33m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Comparando Numeros'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

num1 = int(input('Informe o Primeiro Numero: '))
num2 = int(input('Informe o Segundo Numero: '))

if num1 > num2:
    print('O Numero {}{}{} é maior que o {}{}{}'.format(cores['txVerde'], num1, cores['limpa'], cores['txVermelho'], num2, cores['limpa']))
elif num1 < num2:
    print('O Numero {}{}{} é menor que o {}{}{}'.format(cores['txVermelho'], num1, cores['limpa'], cores['txVerde'], num2, cores['limpa']))
else:
    print('Os Numeros {} e {} são Iguais'.format(num1, num2))

cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txAmarelo':'\033[1;33m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Comparando Numeros'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

num1 = int(input('Informe o Primeiro Numero: '))
num2 = int(input('Informe o Segundo Numero: '))

if num1 > num2:
    print('O Numero {}{}{} é maior que o {}{}{}'.format(cores['txVerde'], num1, cores['limpa'], cores['txVermelho'], num2, cores['limpa']))
elif num1 < num2:
    print('O Numero {}{}{} é menor que o {}{}{}'.format(cores['txVermelho'], num1, cores['limpa'], cores['txVerde'], num2, cores['limpa']))
else:
    print('Os Numeros {} e {} são Iguais'.format(num1, num2))

