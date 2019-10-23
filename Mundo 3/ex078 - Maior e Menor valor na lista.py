
cores = {'limpa':'\033[m',
         'txRoxo':'\033[1;35m'}
print('-=' * 25)
print(f'{cores["txRoxo"]} Maior e Menor Valores em Lista {cores["limpa"]}')
print('-=' * 25)

lista = []
for pos in range(0,5):
    lista.append(int(input(f'Informe o valor para a posição {pos}: ')))

print(f'O maior valor foi {max(lista)} nas posições: ', end='')
for posicao, val in enumerate(lista):
    if val == max(lista):
        print(f'...{posicao}', end='')

print(f'\nO menor valor foi {min(lista)} nas posições: ', end='')
for posicao, val in enumerate(lista):
    if val == min(lista):
        print(f'...{posicao}', end='')

cores = {'limpa':'\033[m',
         'txRoxo':'\033[1;35m'}
print('-=' * 25)
print(f'{cores["txRoxo"]} Maior e Menor Valores em Lista {cores["limpa"]}')
print('-=' * 25)

lista = []
for pos in range(0,5):
    lista.append(int(input(f'Informe o valor para a posição {pos}: ')))

print(f'O maior valor foi {max(lista)} nas posições: ', end='')
for posicao, val in enumerate(lista):
    if val == max(lista):
        print(f'...{posicao}', end='')

print(f'\nO menor valor foi {min(lista)} nas posições: ', end='')
for posicao, val in enumerate(lista):
    if val == min(lista):
        print(f'...{posicao}', end='')

