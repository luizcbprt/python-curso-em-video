
from datetime import date

cores = {'limpa':'\033[m',
         'txVerde':'\033[1;32m',
         'txCiano':'\033[1;36m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Alistamento Militar'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

ano_nasc = int(input('Informe o Ano de seu Nascimento: '))

# Captura o ano atual do sistema
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade < 18:
    print('{}Voce tem {} anos e deverá se alistar em {} anos!{}'.format(cores['txAzul'], idade, 18 - idade, cores['limpa']))
elif idade == 18:
    print('{}Está na hora de se alistar, voce tem {} anos{}'.format(cores['txVerde'], idade, cores['limpa']))
elif idade > 18:
    print('{}Voce tem {} anos e passou {} anos do tempo de se alistar{}'.format(cores['txVermelho'], idade, idade - 18, cores['limpa']))

from datetime import date

cores = {'limpa':'\033[m',
         'txVerde':'\033[1;32m',
         'txCiano':'\033[1;36m',
         'txAzul':'\033[1;34m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Alistamento Militar'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

ano_nasc = int(input('Informe o Ano de seu Nascimento: '))

# Captura o ano atual do sistema
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade < 18:
    print('{}Voce tem {} anos e deverá se alistar em {} anos!{}'.format(cores['txAzul'], idade, 18 - idade, cores['limpa']))
elif idade == 18:
    print('{}Está na hora de se alistar, voce tem {} anos{}'.format(cores['txVerde'], idade, cores['limpa']))
elif idade > 18:
    print('{}Voce tem {} anos e passou {} anos do tempo de se alistar{}'.format(cores['txVermelho'], idade, idade - 18, cores['limpa']))

