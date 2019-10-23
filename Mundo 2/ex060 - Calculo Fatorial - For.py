
print('==' * 25)
print('Calculo Fatorial - For'.center(50, ' '))
print('==' * 25)

num = int(input('Informe um Numero: '))
fatorial = 1
for i in range(num, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i != 1 else ' = ', end='')
    fatorial *= i
print(fatorial)

print('==' * 25)
print('Calculo Fatorial - For'.center(50, ' '))
print('==' * 25)

num = int(input('Informe um Numero: '))
fatorial = 1
for i in range(num, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i != 1 else ' = ', end='')
    fatorial *= i
print(fatorial)

