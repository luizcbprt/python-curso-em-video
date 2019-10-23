
print('-=' * 25)
print('{:-^50}'.format(' Validando Expressoes Matematicas '))
print('-=' * 25)

expres = []
qtdAbreParnt = qtdFechaParnt = 0

expres.append(str(input('Informe uma Expressao: ')))

for verifica in expres:
    for caractere in verifica:
        if caractere == '(':
            qtdAbreParnt += 1
        elif caractere == ')':
            qtdFechaParnt += 1

if qtdAbreParnt == qtdFechaParnt:
    print('A Expressao é Valida!')
else:
    print('A Expressao está incorreta')

print('-=' * 25)
print('{:-^50}'.format(' Validando Expressoes Matematicas '))
print('-=' * 25)

expres = []
qtdAbreParnt = qtdFechaParnt = 0

expres.append(str(input('Informe uma Expressao: ')))

for verifica in expres:
    for caractere in verifica:
        if caractere == '(':
            qtdAbreParnt += 1
        elif caractere == ')':
            qtdFechaParnt += 1

if qtdAbreParnt == qtdFechaParnt:
    print('A Expressao é Valida!')
else:
    print('A Expressao está incorreta')

