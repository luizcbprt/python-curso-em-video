<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:=^50}'.format(' Gerenciador de Pagamentos '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

preco_normal = float(input('Informe o Valor do Produto: '))
condic = int(input('''Informe a Condição de Pagamento
1 - Dinheiro/Cheque (10% Desc)
2 - A Vista Cartão (5% Desc)
3 - 2x Cartão (Sem Juros)
4 - 3x Cartão (20% Juros)
'''))

preco_final = preco_normal

if condic == 1:
    print('Na condição Dinheiro o produto recebe 10% de Desconto.')
    desconto = preco_normal * 0.10
    preco_final = preco_normal - desconto
    print('Preço a pagar será R${:.2f} - R${:.2f}. Total R${:.2f} '.format(preco_normal, desconto, preco_final))
elif condic == 2:
    print('Na condição CARTAO A VISTA o produto recebe 5% de Desconto.')
    desconto = preco_normal * 0.05
    preco_final = preco_normal - desconto
    print('Preço a pagar será R${:.2f} - R${:.2f}. Total R${:.2f}'.format(preco_normal, desconto, preco_final))
elif condic == 3:
    print('Na condição Cartao 2x o produto custará o preço normal.')
    print('Preço a pagar será R${:.2f}.'.format(preco_normal))
else:
    print('Em mais de 3x no Cartao o produto receberá um Acréscimo de 20%')
    acrescimo = preco_normal * 0.20
    preco_final = preco_normal + acrescimo
    print('Preço a pagar será R${:.2f} + R${:.2f}. Total R${:.2f}'.format(preco_normal, acrescimo, preco_final))
=======
cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:=^50}'.format(' Gerenciador de Pagamentos '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

preco_normal = float(input('Informe o Valor do Produto: '))
condic = int(input('''Informe a Condição de Pagamento
1 - Dinheiro/Cheque (10% Desc)
2 - A Vista Cartão (5% Desc)
3 - 2x Cartão (Sem Juros)
4 - 3x Cartão (20% Juros)
'''))

preco_final = preco_normal

if condic == 1:
    print('Na condição Dinheiro o produto recebe 10% de Desconto.')
    desconto = preco_normal * 0.10
    preco_final = preco_normal - desconto
    print('Preço a pagar será R${:.2f} - R${:.2f}. Total R${:.2f} '.format(preco_normal, desconto, preco_final))
elif condic == 2:
    print('Na condição CARTAO A VISTA o produto recebe 5% de Desconto.')
    desconto = preco_normal * 0.05
    preco_final = preco_normal - desconto
    print('Preço a pagar será R${:.2f} - R${:.2f}. Total R${:.2f}'.format(preco_normal, desconto, preco_final))
elif condic == 3:
    print('Na condição Cartao 2x o produto custará o preço normal.')
    print('Preço a pagar será R${:.2f}.'.format(preco_normal))
else:
    print('Em mais de 3x no Cartao o produto receberá um Acréscimo de 20%')
    acrescimo = preco_normal * 0.20
    preco_final = preco_normal + acrescimo
    print('Preço a pagar será R${:.2f} + R${:.2f}. Total R${:.2f}'.format(preco_normal, acrescimo, preco_final))
>>>>>>> Stashed changes
