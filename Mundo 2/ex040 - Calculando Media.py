<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Calculando Media'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

nome = str(input('Informe o Nome do aluno: '))
nota1 = float(input('Informe a Primeira Nota: '))
nota2 = float(input('Informe a Segunda Nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua Media foi de {}{}{}.'.format(cores['txVermelho'], media, cores['limpa']))
    print('Aluno {} está {}REPROVADO{}'.format(nome, cores['txVermelho'], cores['limpa']))
elif media >= 5 and media <= 6.9:
    print('Sua Media foi de {}'.format(media))
    print('Aluno {} está de {}RECUPERAÇÃO{}'.format(nome, cores['txCiano'], cores['limpa']))
elif media >= 7:
    print('Sua Média foi de {}'.format(media))
    print('Aluno {} foi {}APROVADO{}'.format(nome, cores['txVerde'], cores['limpa']))
=======
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Calculando Media'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

nome = str(input('Informe o Nome do aluno: '))
nota1 = float(input('Informe a Primeira Nota: '))
nota2 = float(input('Informe a Segunda Nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua Media foi de {}{}{}.'.format(cores['txVermelho'], media, cores['limpa']))
    print('Aluno {} está {}REPROVADO{}'.format(nome, cores['txVermelho'], cores['limpa']))
elif media >= 5 and media <= 6.9:
    print('Sua Media foi de {}'.format(media))
    print('Aluno {} está de {}RECUPERAÇÃO{}'.format(nome, cores['txCiano'], cores['limpa']))
elif media >= 7:
    print('Sua Média foi de {}'.format(media))
    print('Aluno {} foi {}APROVADO{}'.format(nome, cores['txVerde'], cores['limpa']))
>>>>>>> Stashed changes
