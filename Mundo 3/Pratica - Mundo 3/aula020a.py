def dobrar(lista):
    for item in lista:
        item *= 2


valores = [4, 6, 0, 1, 2]
dobrar(valores)
print(valores)

print('-=' * 30)

def soma(*valores):
    s = sum(valores)
    print(f'Somando os valores {valores} temos {s}')


soma(4, 5)
soma(0, 1, 8)