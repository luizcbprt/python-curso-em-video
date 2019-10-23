
print('-=' * 25)
print(' Matriz em Python')
print('-=' * 25)

matriz = [[], [], [],
          [], [], [],
          [], [], []]

for indice in range(0,9):
    num = int(input(f'Informe o {indice + 1}º Numero: '))
    matriz[indice].append(num)

print(f'''
[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]
[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]
[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]
''')

print('-=' * 25)
print(' Matriz em Python')
print('-=' * 25)

matriz = [[], [], [],
          [], [], [],
          [], [], []]

for indice in range(0,9):
    num = int(input(f'Informe o {indice + 1}º Numero: '))
    matriz[indice].append(num)

print('''
[ {} ] [ {} ] [ {} ]
[ {} ] [ {} ] [ {} ]
[ {} ] [ {} ] [ {} ]
'''.format(matriz[0], matriz[1], matriz[2],
           matriz[3], matriz[4], matriz[5],
           matriz[6], matriz[7], matriz[8]))
