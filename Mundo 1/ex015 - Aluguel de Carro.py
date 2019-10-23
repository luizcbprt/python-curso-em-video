
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'fndAzul':'\033[44m',
         'roxo':'\033[1;35m',
         'fndRoxo':'\033[45m'}

print(cores['azul'],'=' * 45,cores['limpa'])
print('{}PROGRAMA PARA CALCULAR ALUGUEL DE CARRO{}'.format(cores['roxo'],cores['limpa']))
print(cores['azul'],'=' * 45, cores['limpa'])

qtdKm = float(input('Informe quantos Km voce percorreu: '))
qtdDias = int(input('Informe a quantidade de dias que permaneceu com o carro: '))

pagar = (qtdKm * 0.15) + (qtdDias * 60)

print('O Valor total a Pagar será de R${}'.format(pagar))

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'fndAzul':'\033[44m',
         'roxo':'\033[1;35m',
         'fndRoxo':'\033[45m'}

print(cores['azul'],'=' * 45,cores['limpa'])
print('{}PROGRAMA PARA CALCULAR ALUGUEL DE CARRO{}'.format(cores['roxo'],cores['limpa']))
print(cores['azul'],'=' * 45, cores['limpa'])

qtdKm = float(input('Informe quantos Km voce percorreu: '))
qtdDias = int(input('Informe a quantidade de dias que permaneceu com o carro: '))

pagar = (qtdKm * 0.15) + (qtdDias * 60)

print('O Valor total a Pagar será de R${}'.format(pagar))

