<<<<<<< Updated upstream
numero = input('Informe um numero entre 0 e 9999: ')

print('Tamanho: ', len(numero))
print('Numero: ', numero)
for i in numero:
    if len(numero) == 4:
        if i == numero[0]:
            print('Milhar: ', i)
        elif i == numero[1]:
            print('Centena: ', i)
        elif i == numero[2]:
            print('Dezena: ', i)
        elif i == numero[3]:
            print('Unidade: ', i)
    if len(numero) == 3:
        if i == numero[0]:
            print('Centena: ', i)
        elif i == numero[1]:
            print('Dezena: ', i)
        elif i == numero[2]:
            print('Unidade: ', i)
    if len(numero) == 2:
        if i == numero[0]:
            print('Dezena: ', i)
        elif i == numero[1]:
            print('Unidade: ', i)
    if len(numero) == 1:
        print('Unidade: ', i)
=======
numero = input('Informe um numero entre 0 e 9999: ')

print('Tamanho: ', len(numero))
print('Numero: ', numero)
for i in numero:
    if len(numero) == 4:
        if i == numero[0]:
            print('Milhar: ', i)
        elif i == numero[1]:
            print('Centena: ', i)
        elif i == numero[2]:
            print('Dezena: ', i)
        elif i == numero[3]:
            print('Unidade: ', i)
    if len(numero) == 3:
        if i == numero[0]:
            print('Centena: ', i)
        elif i == numero[1]:
            print('Dezena: ', i)
        elif i == numero[2]:
            print('Unidade: ', i)
    if len(numero) == 2:
        if i == numero[0]:
            print('Dezena: ', i)
        elif i == numero[1]:
            print('Unidade: ', i)
    if len(numero) == 1:
        print('Unidade: ', i)
>>>>>>> Stashed changes
