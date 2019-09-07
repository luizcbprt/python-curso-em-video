<<<<<<< Updated upstream
print('-=' * 25)
print('Lista de Preços com Tupla'.center(50, ' '))
print('-=' * 25)

lista = ('Rtx 2080 TI', 3990.35, 'Biscoito Meg/Maffu', 4.99, 'Pão', 2.00,
         'Bicicleta', 250.00, 'Capacete', 100.90, 'Chocolate', 5.00)

for item in lista:
    if type(item) == str:
        print(item.ljust(30,'.'), end='R$')
    elif type(item) == float:
        print(f'{item:.2f}'.rjust(7, ' '))
print('--' * 25)
=======
print('-=' * 25)
print('Lista de Preços com Tupla'.center(50, ' '))
print('-=' * 25)

lista = ('Rtx 2080 TI', 3990.35, 'Biscoito Meg/Maffu', 4.99, 'Pão', 2.00,
         'Bicicleta', 250.00, 'Capacete', 100.90, 'Chocolate', 5.00)

for item in lista:
    if type(item) == str:
        print(item.ljust(30,'.'), end='R$')
    elif type(item) == float:
        print(f'{item:.2f}'.rjust(7, ' '))
print('--' * 25)
>>>>>>> Stashed changes
