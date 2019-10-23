
cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m',
         'txAzul':'\033[1;34m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:^50}'.format(' Tratando Varios Valores V1.0'))
print(cores['txCiano'], '==' * 25, cores['limpa'])

qtdDigitado = soma = 0
num = 0

while num != 999:
    num = int(input('Informe um Número [999 - Sair]: '))
    if num != 999:
        qtdDigitado += 1
        soma += num
print('Numeros Informados: {}. Soma Total {}'.format(qtdDigitado, soma))

cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m',
         'txAzul':'\033[1;34m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:^50}'.format(' Tratando Varios Valores V1.0'))
print(cores['txCiano'], '==' * 25, cores['limpa'])

qtdDigitado = soma = 0
num = 0

while num != 999:
    num = int(input('Informe um Número [999 - Sair]: '))
    if num != 999:
        qtdDigitado += 1
        soma += num
print('Numeros Informados: {}. Soma Total {}'.format(qtdDigitado, soma))

