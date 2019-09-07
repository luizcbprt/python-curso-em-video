<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Analisando Triangulos V2.0'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

lado1 = float(input('Informe a primeira reta: '))
lado2 = float(input('Informe a segunda reta: '))
lado3 = float(input('Informe a terceira reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Poderá ser Formado um Triangulo EQUILÁTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Poderá ser Formado um Triangulo ISÓCELES')
    elif lado1 != lado2 != lado3 != lado1:
        print('Poderá ser Formado um Triangulo ESCALENO')
else:
    print('Não poderá ser formado um Triangulo')
=======
cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Analisando Triangulos V2.0'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

lado1 = float(input('Informe a primeira reta: '))
lado2 = float(input('Informe a segunda reta: '))
lado3 = float(input('Informe a terceira reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Poderá ser Formado um Triangulo EQUILÁTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Poderá ser Formado um Triangulo ISÓCELES')
    elif lado1 != lado2 != lado3 != lado1:
        print('Poderá ser Formado um Triangulo ESCALENO')
else:
    print('Não poderá ser formado um Triangulo')
>>>>>>> Stashed changes
