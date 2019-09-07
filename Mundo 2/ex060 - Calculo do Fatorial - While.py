<<<<<<< Updated upstream
print('==' * 25)
print('Calculo do Fatorial com While'.center(50, ' '))
print('==' * 25)

num = int(input('Informe um Numero: '))
cont = num - 1
numeros = '{} x {}'.format(num, cont)
result = num * cont
while cont > 0:
    cont = cont - 1
    if cont > 0:
        result =+ result * cont
        numeros += ' x {}'.format(cont)

print('O Fatorial de {} é {}'.format(num, result), end=' ')
print('que é igual a {}'.format(numeros))
=======
print('==' * 25)
print('Calculo do Fatorial com While'.center(50, ' '))
print('==' * 25)

num = int(input('Informe um Numero: '))
cont = num - 1
numeros = '{} x {}'.format(num, cont)
result = num * cont
while cont > 0:
    cont = cont - 1
    if cont > 0:
        result =+ result * cont
        numeros += ' x {}'.format(cont)

print('O Fatorial de {} é {}'.format(num, result), end=' ')
print('que é igual a {}'.format(numeros))
>>>>>>> Stashed changes
