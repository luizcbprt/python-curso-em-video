print('==' * 25)
print('{:^50}'.format(' Numeros Primos'))
print('==' * 50)

num = int(input('Informe um Numero inteiro: '))
tot = sum(1 for cont in range(1, num + 1) if num % cont == 0)

if tot == 2:
    print(f'O Numero {num} é Primo...e foi divisivel por {tot} numeros')
else:
    print(f'O numero {num} não é primo, pois foi divisivel por {tot} numeros')

print('==' * 25)
print('{:^50}'.format(' Numeros Primos'))
print('==' * 50)

num = int(input('Informe um Numero inteiro: '))
tot = sum(1 for cont in range(1, num + 1) if num % cont == 0)

if tot == 2:
    print(f'O Numero {num} é Primo...e foi divisivel por {tot} numeros')
else:
    print(f'O numero {num} não é primo, pois foi divisivel por {tot} numeros')
