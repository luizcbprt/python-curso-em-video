<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Calculando Indice de Massa Corpórea'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

#IMC = Peso em KG / (Altura * Altura)
altura = float(input('Informe sua altura em Mt: '))
peso = float(input('Informe seu peso em KG: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Voce está abaixo do peso'.format(imc))
elif 18.5 <= imc <= 25:
    print('seu IMC é de {:.2f}. Voce está no Peso Ideal'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é de {:.2f}. VOce está com Sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é de {:.2f}. Voce está com Obesidade'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Voce está com Obsesidade Mórbida'.format(imc))
=======
cores = {'limpa':'\033[m',
         'txAzul':'\033[1;34m',
         'txCiano':'\033[1;36m',
         'txVerde':'\033[1;32m',
         'txVermelho':'\033[1;31m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('Calculando Indice de Massa Corpórea'.center(50, ' '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

#IMC = Peso em KG / (Altura * Altura)
altura = float(input('Informe sua altura em Mt: '))
peso = float(input('Informe seu peso em KG: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Voce está abaixo do peso'.format(imc))
elif 18.5 <= imc <= 25:
    print('seu IMC é de {:.2f}. Voce está no Peso Ideal'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é de {:.2f}. VOce está com Sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é de {:.2f}. Voce está com Obesidade'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Voce está com Obsesidade Mórbida'.format(imc))
>>>>>>> Stashed changes
