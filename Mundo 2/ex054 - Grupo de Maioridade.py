
from datetime import date

print('==' * 25)
print('{:^50}'.format(' Grupo de Maioridade'))
print('==' * 25)

qtdMaiorIdade = 0
qtdMenorIdade = 0
ano_atual = date.today().year

for cont in range(1, 8):
    ano_pessoa = int(input('Informe o ano de nascimento da {} Pessoa: '.format(cont)))
    if (ano_atual - ano_pessoa) >= 21:
        qtdMaiorIdade += 1
    else:
        qtdMenorIdade += 1
print('Maiores de Idade: {}'.format(qtdMaiorIdade))
print('Menores de Idade: {}'.format(qtdMenorIdade))

from datetime import date

print('==' * 25)
print('{:^50}'.format(' Grupo de Maioridade'))
print('==' * 25)

qtdMaiorIdade = 0
qtdMenorIdade = 0
ano_atual = date.today().year

for cont in range(1, 8):
    ano_pessoa = int(input('Informe o ano de nascimento da {} Pessoa: '.format(cont)))
    if (ano_atual - ano_pessoa) >= 21:
        qtdMaiorIdade += 1
    else:
        qtdMenorIdade += 1
print('Maiores de Idade: {}'.format(qtdMaiorIdade))
print('Menores de Idade: {}'.format(qtdMenorIdade))

