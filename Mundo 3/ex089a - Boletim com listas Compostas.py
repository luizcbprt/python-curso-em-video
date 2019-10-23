
print('-=' * 25)
print('Boletim com Listas Compostas - Metodo 2')
print('-=' * 25)

lstFicha = []

while True:
    nome = str(input('Informe o Nome: ')).capitalize()
    nota1 = float(input('Informe a 1º Nota: '))
    nota2 = float(input('Informe a 2º Nota: '))
    media = (nota1 + nota2) / 2
    lstFicha.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 25)
print(f'{"No":<5}{"Nome":<13}{"Media":<7}')
for pos, aluno in enumerate(lstFicha):
    print(f'{pos:<5}{aluno[0]:<13}{aluno[2]:<7.1f}')

while True:
    opc = ' '
    opc = int(input('Deseja visuar Notas de Qual aluno? 999 = Sair: '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <=  len(lstFicha) - 1:
        print(f'Notas de {lstFicha[opc][0]}: {lstFicha[opc][1]}')
print('Fim')

print('-=' * 25)
print('Boletim com Listas Compostas - Metodo 2')
print('-=' * 25)

lstFicha = []

while True:
    nome = str(input('Informe o Nome: ')).capitalize()
    nota1 = float(input('Informe a 1º Nota: '))
    nota2 = float(input('Informe a 2º Nota: '))
    media = (nota1 + nota2) / 2
    lstFicha.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 25)
print(f'{"No":<5}{"Nome":<13}{"Media":<7}')
for pos, aluno in enumerate(lstFicha):
    print(f'{pos:<5}{aluno[0]:<13}{aluno[2]:<7.1f}')

while True:
    opc = ' '
    opc = int(input('Deseja visuar Notas de Qual aluno? 999 = Sair: '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <=  len(lstFicha) - 1:
        print(f'Notas de {lstFicha[opc][0]}: {lstFicha[opc][1]}')
print('Fim')

