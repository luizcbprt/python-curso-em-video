<<<<<<< Updated upstream
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m'}
print('-=' * 25)
print(f'{cores["txVermelho"]} Contando Vogais em Tupla {cores["limpa"]}'.center(50, ' '))
print('-=' * 25)

familia = ('Rafael', 'Andressa', 'Meg', 'Maffu',
           'Papai', 'Mamae', 'Mocinha', 'Nenem')

for palavra in familia:
    print(f' A palavra {palavra} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
    print(' ')
=======
cores = {'limpa':'\033[m',
         'txVermelho':'\033[1;31m'}
print('-=' * 25)
print(f'{cores["txVermelho"]} Contando Vogais em Tupla {cores["limpa"]}'.center(50, ' '))
print('-=' * 25)

familia = ('Rafael', 'Andressa', 'Meg', 'Maffu',
           'Papai', 'Mamae', 'Mocinha', 'Nenem')

for palavra in familia:
    print(f' A palavra {palavra} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
    print(' ')
>>>>>>> Stashed changes
