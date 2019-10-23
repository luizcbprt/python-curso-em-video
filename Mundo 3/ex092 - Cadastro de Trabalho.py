
print('-=' * 25)
print('Cadastro de Trabalho'.center(50, ' '))
print('-=' * 25)

from datetime import date
pessoa = {}

nome = str(input('Informe o Nome: ')).strip().capitalize()
anoNasc = int(input(f'Que ano {nome} nasceu? '))
# Calcula Idade usando a funcao date
idade = date.today().year - anoNasc
ctps = int(input('Informe o Nº da Carteira de Trabalho. 0 = NAO POSSUI: '))

# Armazena as informações no dicionario
if ctps == 0:
    pessoa.update({'nome':nome, 'idade':idade, 'ctps':ctps})
else:
    anoContrat = int(input('Informe o Ano de Contratação: '))
    aposentar = (date.today().year - anoContrat) + 35
    salario = float(input('Informe o Salário R$:'))
    pessoa.update({'nome':nome, 'idade':idade, 'ctps':ctps,
                   'contratacao':anoContrat, 'aposentar':aposentar,
                   'salario':salario})


# Imprime os resultados
print('*=' * 30)
for key, value in pessoa.items():
    print(f'{key} tem o valor {value}')

print('-=' * 25)
print('Cadastro de Trabalho'.center(50, ' '))
print('-=' * 25)

from datetime import date
pessoa = {}

nome = str(input('Informe o Nome: ')).strip().capitalize()
anoNasc = int(input(f'Que ano {nome} nasceu? '))
# Calcula Idade usando a funcao date
idade = date.today().year - anoNasc
ctps = int(input('Informe o Nº da Carteira de Trabalho. 0 = NAO POSSUI: '))

# Armazena as informações no dicionario
if ctps == 0:
    pessoa.update({'nome':nome, 'idade':idade, 'ctps':ctps})
else:
    anoContrat = int(input('Informe o Ano de Contratação: '))
    aposentar = (date.today().year - anoContrat) + 35
    salario = float(input('Informe o Salário R$:'))
    pessoa.update({'nome':nome, 'idade':idade, 'ctps':ctps,
                   'contratacao':anoContrat, 'aposentar':aposentar,
                   'salario':salario})


# Imprime os resultados
print('*=' * 30)
for key, value in pessoa.items():
    print(f'{key} tem o valor {value}')

