
print('==' * 25)
print('{:^50}'.format(' Detector de Palíndromo'))
print('==' * 25)

frase = str(input('Informe uma frase: ')).strip()

normal = frase.replace(' ','')
tras = ''
for i in range(-1, -len(normal) -1, -1):
    tras += normal[i]

if normal == tras:
    print('A frase {} é um Palíndromo!'.format(frase))
else:
    print('A frase {} não é um Palíndromo'.format(frase))

print('==' * 25)
print('{:^50}'.format(' Detector de Palíndromo'))
print('==' * 25)

frase = str(input('Informe uma frase: ')).strip()

normal = frase.replace(' ','')
tras = ''
for i in range(-1, -len(normal) -1, -1):
    tras += normal[i]

if normal == tras:
    print('A frase {} é um Palíndromo!'.format(frase))
else:
    print('A frase {} não é um Palíndromo'.format(frase))

