<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}

print('=-' * 25)
print(f'{cores["azul"]}Estatísticas em Produtos{cores["limpa"]}'.center(50, ' '))
print('=-' * 25)


totCompra = qtd1000 = valMaior = valMenor = cont = 0
nomeMaior = nomeMenor = ' '
while True:
    nome = str(input('Informe o nome do Produto: '))
    preco = float(input('Informe o Preço: R$'))

    cont += 1
    if cont == 1 or preco < valMenor:
        valMenor = preco
        nomeMenor = nome

    totCompra += preco

    if preco >= 1000:
        qtd1000 += 1

    if preco > valMaior:
        valMaior = preco
        nomeMaior = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('FINALIZANDO COMPRA'.center(50, ' '))
print(f'O Total da compra foi de R${totCompra:.2f}')
print(f'Foram comprados {qtd1000} produtos acima de R$1000')
print(f'O Produto de maior valor foi {cores["vermelho"]}{nomeMaior}{cores["limpa"]}, custando {cores["vermelho"]}R${valMaior:.2f}{cores["limpa"]}!')
print(f'O produto de menor Valor foi {nomeMenor}, custando R${valMenor:.2f}')
=======
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}

print('=-' * 25)
print(f'{cores["azul"]}Estatísticas em Produtos{cores["limpa"]}'.center(50, ' '))
print('=-' * 25)


totCompra = qtd1000 = valMaior = valMenor = cont = 0
nomeMaior = nomeMenor = ' '
while True:
    nome = str(input('Informe o nome do Produto: '))
    preco = float(input('Informe o Preço: R$'))

    cont += 1
    if cont == 1 or preco < valMenor:
        valMenor = preco
        nomeMenor = nome

    totCompra += preco

    if preco >= 1000:
        qtd1000 += 1

    if preco > valMaior:
        valMaior = preco
        nomeMaior = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('FINALIZANDO COMPRA'.center(50, ' '))
print(f'O Total da compra foi de R${totCompra:.2f}')
print(f'Foram comprados {qtd1000} produtos acima de R$1000')
print(f'O Produto de maior valor foi {cores["vermelho"]}{nomeMaior}{cores["limpa"]}, custando {cores["vermelho"]}R${valMaior:.2f}{cores["limpa"]}!')
print(f'O produto de menor Valor foi {nomeMenor}, custando R${valMenor:.2f}')
>>>>>>> Stashed changes
