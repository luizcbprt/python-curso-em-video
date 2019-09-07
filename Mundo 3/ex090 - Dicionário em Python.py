<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m'}

print('-=' * 25)
print('{:-^50}'.format(f' {cores["txAzul"]}Dicionário em Python{cores["limpa"]} '))
print('-=' * 25)

dcAluno = dict()

dcAluno['nome'] = str(input('Informe o Nome do Aluno: ')).capitalize().strip()
dcAluno['media'] = float(input(f'Informe a Media de {dcAluno["nome"]}: '))

if dcAluno["media"] >= 7:
    dcAluno["situacao"] = 'Aprovado'
elif 5 <= dcAluno["media"] < 7:
    dcAluno["situacao"] = 'Recuperação'
else:
    dcAluno["situacao"] = 'Reprovado'

print('-=' * 30)
for key, value in dcAluno.items():
    print(f'O {key} é {value}')

#print(f'Nome é {dcAluno["nome"]}')
#print(f'Media é igual a {dcAluno["media"]}')
#print(f'A situação é {dcAluno["situacao"]}')
=======
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m'}

print('-=' * 25)
print('{:-^50}'.format(f' {cores["txAzul"]}Dicionário em Python{cores["limpa"]} '))
print('-=' * 25)

dcAluno = dict()

dcAluno['nome'] = str(input('Informe o Nome do Aluno: ')).capitalize().strip()
dcAluno['media'] = float(input(f'Informe a Media de {dcAluno["nome"]}: '))

if dcAluno["media"] >= 7:
    dcAluno["situacao"] = 'Aprovado'
elif 5 <= dcAluno["media"] < 7:
    dcAluno["situacao"] = 'Recuperação'
else:
    dcAluno["situacao"] = 'Reprovado'

print('-=' * 30)
for key, value in dcAluno.items():
    print(f'O {key} é {value}')

#print(f'Nome é {dcAluno["nome"]}')
#print(f'Media é igual a {dcAluno["media"]}')
#print(f'A situação é {dcAluno["situacao"]}')
>>>>>>> Stashed changes
