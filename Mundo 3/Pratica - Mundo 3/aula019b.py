<<<<<<< Updated upstream
brasil = list()
estado = dict()

for c in range(0,3):
    estado['uf'] = str(input('Informe a UF: '))
    estado['sigla'] = str(input('Informe a Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for estd in brasil:
    for key, value in estd.items():
        print(f'O campo {key} tem valor {value}')
=======
brasil = list()
estado = dict()

for c in range(0,3):
    estado['uf'] = str(input('Informe a UF: '))
    estado['sigla'] = str(input('Informe a Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for estd in brasil:
    for key, value in estd.items():
        print(f'O campo {key} tem valor {value}')
>>>>>>> Stashed changes
