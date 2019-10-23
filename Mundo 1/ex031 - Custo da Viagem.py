
viagem = int(input('Informe a distancia da Viagem: '))
preco_curto = 0.50
preco_longo = 0.45

if viagem <= 200:
    print('O Preço será R${:.2f}. R${:.2f} por KM'.format(viagem * preco_curto, preco_curto))
else:
    print('O preco será R${:.2f}. R${} por KM'.format(viagem * preco_longo, preco_longo))

viagem = int(input('Informe a distancia da Viagem: '))
preco_curto = 0.50
preco_longo = 0.45

if viagem <= 200:
    print('O Preço será R${:.2f}. R${:.2f} por KM'.format(viagem * preco_curto, preco_curto))
else:
    print('O preco será R${:.2f}. R${} por KM'.format(viagem * preco_longo, preco_longo))

