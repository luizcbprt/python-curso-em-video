def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [4, 6, 0, 1, 2]
dobrar(valores)
print(valores)

print('-=' * 30)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(4, 5)
soma(0, 1, 8)