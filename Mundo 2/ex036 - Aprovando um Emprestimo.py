
# Dicionario com cores
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txAzul':'\033[1;34m'}
print(cores['txAzul'], '==' * 25, cores['limpa'])
print('Aprovando Emprestimos'.center(50,' '))
print(cores['txAzul'], '==' * 25, cores['limpa'])

#Armazenando dados de entrada em variaveis
val_casa = float(input('Informe o Valor Total da Casa: R$'))
salario = float(input('Informe o Salario: R$'))
qtd_anos = int(input('Informe a quantidade de anos para pagar: '))

# Calculando valor da parcela
prestacao = val_casa / (qtd_anos * 12)

if prestacao <= (salario  * 0.30):
    print(''' Emprestimo {}Aprovado{}!!
              Sua prestacao será no valor de R${:.2f}
          '''.format(cores['txVerde'], cores['limpa'], prestacao))
elif prestacao > (salario  * 0.30):
    print('''Emprestimo {}Negado{}
             O Valor da Parcela R${:.2f} excede 30% do seu salário
          '''.format(cores['txVermelho'], cores['limpa'], prestacao))

# Dicionario com cores
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m',
         'txVerde':'\033[1;32m',
         'txAzul':'\033[1;34m'}
print(cores['txAzul'], '==' * 25, cores['limpa'])
print('Aprovando Emprestimos'.center(50,' '))
print(cores['txAzul'], '==' * 25, cores['limpa'])

#Armazenando dados de entrada em variaveis
val_casa = float(input('Informe o Valor Total da Casa: R$'))
salario = float(input('Informe o Salario: R$'))
qtd_anos = int(input('Informe a quantidade de anos para pagar: '))

# Calculando valor da parcela
prestacao = val_casa / (qtd_anos * 12)

if prestacao <= (salario  * 0.30):
    print(''' Emprestimo {}Aprovado{}!!
              Sua prestacao será no valor de R${:.2f}
          '''.format(cores['txVerde'], cores['limpa'], prestacao))
elif prestacao > (salario  * 0.30):
    print('''Emprestimo {}Negado{}
             O Valor da Parcela R${:.2f} excede 30% do seu salário
          '''.format(cores['txVermelho'], cores['limpa'], prestacao))

