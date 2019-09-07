<<<<<<< Updated upstream
print('==' * 25)
print('Sequencia de Fibonacci V1.0'.center(50, ' '))
print('==' * 25)

seq = int(input('Informe quantos elementos Fibonacci deseja Visualizar: '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')

cont = 3
while cont <= seq:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
=======
print('==' * 25)
print('Sequencia de Fibonacci V1.0'.center(50, ' '))
print('==' * 25)

seq = int(input('Informe quantos elementos Fibonacci deseja Visualizar: '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')

cont = 3
while cont <= seq:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
>>>>>>> Stashed changes
