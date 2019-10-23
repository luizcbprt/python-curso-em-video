
print('=-' * 25)
print('Analise de dados do grupo'.center(50, ' '))
print('=-' * 25)


idade = qtd_18 = qtd_homem = qtd_mulher_20 = 0
while True:
    sexo = ' '
    continuar = ' '

    idade = int(input('Informe a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Informe o Sexo (M/F): ')).upper().strip()[0]

    if idade > 18:
        qtd_18 += 1
    if sexo == 'M':
        qtd_homem += 1
    if sexo == 'F' and idade < 20:
        qtd_mulher_20 += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N) ')).upper().strip()[0]
    if continuar == 'N':
        break
print('--' * 25)
print(f'Quantidade de maiores de 18 anos: {qtd_18}')
print(f'Quantidade de Homens: {qtd_homem}')
print(f'Quantidade de Mulheres menores de 20 anos: {qtd_mulher_20}')

print('=-' * 25)
print('Analise de dados do grupo'.center(50, ' '))
print('=-' * 25)


idade = qtd_18 = qtd_homem = qtd_mulher_20 = 0
while True:
    sexo = ' '
    continuar = ' '

    idade = int(input('Informe a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Informe o Sexo (M/F): ')).upper().strip()[0]

    if idade > 18:
        qtd_18 += 1
    if sexo == 'M':
        qtd_homem += 1
    if sexo == 'F' and idade < 20:
        qtd_mulher_20 += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? (S/N) ')).upper().strip()[0]
    if continuar == 'N':
        break
print('--' * 25)
print(f'Quantidade de maiores de 18 anos: {qtd_18}')
print(f'Quantidade de Homens: {qtd_homem}')
print(f'Quantidade de Mulheres menores de 20 anos: {qtd_mulher_20}')

