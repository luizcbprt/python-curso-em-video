
from datetime import date

cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m',
         'txCinza':'\033[1;37m',
         'txAmarelo':'\033[1;33m',
         'txRoxo':'\033[1;35m'}
print(cores['txRoxo'], '==' * 25, cores['limpa'])
print('Classificando Atletas'.center(50, ' '))
print(cores['txRoxo'], '==' * 25, cores['limpa'])

ano_atual = date.today().year
ano_nasc = int(input('Informe o Ano de Nascimento: '))
idade = ano_atual - ano_nasc

if idade <= 9:
    print(
        'Nascidos em {}, com {} anos são da categoria {}MIRIM{}'.format(
            ano_nasc, idade, cores['txAmarelo'], cores['limpa']
        )
    )
elif idade <= 14:
    print(
        'Nascidos em {}, com {} anos são da categoria {}INFANTIL{}'.format(
            ano_nasc, idade, cores['txCiano'], cores['limpa']
        )
    )
elif idade <= 19:
    print(
        'Nascidos em {}, com {} anos são da categoria {}JUNIOR{}'.format(
            ano_nasc, idade, cores['txVerde'], cores['limpa']
        )
    )
elif idade == 20:
    print(
        'Nascidos em {}, com {} anos são da categoria {}SENIOR{}'.format(
            ano_nasc, idade, cores['txAzul'], cores['limpa']
        )
    )
else:
    print(
        'Nascidos em {}, com {} anos são da categoria {}MASTER{}'.format(
            ano_nasc, idade, cores['txRoxo'], cores['limpa']
        )
    )

from datetime import date

cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m',
         'txCinza':'\033[1;37m',
         'txAmarelo':'\033[1;33m',
         'txRoxo':'\033[1;35m'}
print(cores['txRoxo'], '==' * 25, cores['limpa'])
print('Classificando Atletas'.center(50, ' '))
print(cores['txRoxo'], '==' * 25, cores['limpa'])

ano_atual = date.today().year
ano_nasc = int(input('Informe o Ano de Nascimento: '))
idade = ano_atual - ano_nasc

if idade <= 9:
    print(
        'Nascidos em {}, com {} anos são da categoria {}MIRIM{}'.format(
            ano_nasc, idade, cores['txAmarelo'], cores['limpa']
        )
    )
elif idade <= 14:
    print(
        'Nascidos em {}, com {} anos são da categoria {}INFANTIL{}'.format(
            ano_nasc, idade, cores['txCiano'], cores['limpa']
        )
    )
elif idade <= 19:
    print(
        'Nascidos em {}, com {} anos são da categoria {}JUNIOR{}'.format(
            ano_nasc, idade, cores['txVerde'], cores['limpa']
        )
    )
elif idade == 20:
    print(
        'Nascidos em {}, com {} anos são da categoria {}SENIOR{}'.format(
            ano_nasc, idade, cores['txAzul'], cores['limpa']
        )
    )
else:
    print(
        'Nascidos em {}, com {} anos são da categoria {}MASTER{}'.format(
            ano_nasc, idade, cores['txRoxo'], cores['limpa']
        )
    )

