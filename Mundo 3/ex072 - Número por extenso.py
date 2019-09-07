<<<<<<< Updated upstream
print('-=' * 25)
print('{:-^50}'.format(' Numeros por extenso '))
print('-=' * 25)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Informe um Numero entre 0 e 20: '))
    #if escolha >= 0 and escolha <= 20:
    if 0 <= escolha <= 20:
        break
    print('Valor Inválido. Tente novamente')
print(f'Você digitou o Número: {numeros[escolha]}')
=======
print('-=' * 25)
print('{:-^50}'.format(' Numeros por extenso '))
print('-=' * 25)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Informe um Numero entre 0 e 20: '))
    #if escolha >= 0 and escolha <= 20:
    if 0 <= escolha <= 20:
        break
    print('Valor Inválido. Tente novamente')
print(f'Você digitou o Número: {numeros[escolha]}')
>>>>>>> Stashed changes
