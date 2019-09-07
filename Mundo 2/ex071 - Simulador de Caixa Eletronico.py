<<<<<<< Updated upstream
print('-=' * 25)
print('{:-^50}'.format(' Simulador de Caixa Eletronico '))
print('-=' * 25)

qtd50 = qtd20 = qtd10 = qtd1 = 0

valSaque = float(input('Informe o Valor para Sacar: R$'))
while True:
    if valSaque >= 50:
        qtd50 += 1
        valSaque -= 50
    elif valSaque < 50 and valSaque >= 20:
        qtd20 += 1
        valSaque -= 20
    elif valSaque < 20 and valSaque >= 10:
        qtd10 += 1
        valSaque -= 10
    elif valSaque < 10:
        qtd1 += 1
        valSaque -= 1

    if valSaque == 0:
        break

print('==' * 25)
print(f'Total de {qtd50} células de R$50')
print(f'Total de {qtd20} cédulas de R$20')
print(f'Total de {qtd10} céduas de R$10')
print(f'Total de {qtd1} cédulas de R$1')
=======
print('-=' * 25)
print('{:-^50}'.format(' Simulador de Caixa Eletronico '))
print('-=' * 25)

qtd50 = qtd20 = qtd10 = qtd1 = 0

valSaque = float(input('Informe o Valor para Sacar: R$'))
while True:
    if valSaque >= 50:
        qtd50 += 1
        valSaque -= 50
    elif valSaque < 50 and valSaque >= 20:
        qtd20 += 1
        valSaque -= 20
    elif valSaque < 20 and valSaque >= 10:
        qtd10 += 1
        valSaque -= 10
    elif valSaque < 10:
        qtd1 += 1
        valSaque -= 1

    if valSaque == 0:
        break

print('==' * 25)
print(f'Total de {qtd50} células de R$50')
print(f'Total de {qtd20} cédulas de R$20')
print(f'Total de {qtd10} céduas de R$10')
print(f'Total de {qtd1} cédulas de R$1')
>>>>>>> Stashed changes
