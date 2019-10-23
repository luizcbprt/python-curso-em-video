
print('==' * 25)
print(' Maior e Menor Valores'.center(50, ' '))
print('==' * 25)

continuar = 'S'
num = maior = menor = soma = cont = 0
while continuar != 'N':
    num = int(input('Informe um Numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja Continuar? S/N')).strip().upper()
print('A media entre todos os valores foi: {}'.format(soma / cont))
print('O Maior foi {}, e o menor foi {}'.format(maior, menor))

print('==' * 25)
print(' Maior e Menor Valores'.center(50, ' '))
print('==' * 25)

continuar = 'S'
num = maior = menor = soma = cont = 0
while continuar != 'N':
    num = int(input('Informe um Numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja Continuar? S/N')).strip().upper()
print('A media entre todos os valores foi: {}'.format(soma / cont))
print('O Maior foi {}, e o menor foi {}'.format(maior, menor))

