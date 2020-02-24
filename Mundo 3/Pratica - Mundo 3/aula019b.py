
brasil = []
estado = {}

for c in range(3):
    estado['uf'] = str(input('Informe a UF: '))
    estado['sigla'] = str(input('Informe a Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for estd in brasil:
    for key, value in estd.items():
        print(f'O campo {key} tem valor {value}')

brasil = []
estado = {}

for _ in range(3):
    estado['uf'] = str(input('Informe a UF: '))
    estado['sigla'] = str(input('Informe a Sigla: '))
    brasil.append(estado.copy())
print(brasil)

for estd in brasil:
    for key, value in estd.items():
        print(f'O campo {key} tem valor {value}')

