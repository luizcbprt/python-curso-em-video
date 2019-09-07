<<<<<<< Updated upstream
print('-=' * 25)
print('{:-^50}'.format(' Lista Ordenada sem Sort'))
print('-=' * 25)

#lista = []
lista = list()
posic = 0

for i in range(0,5):
    num = int(input('Informe um Numero: '))
    if i == 0:
        lista.append(num)
    if i != 0:
        for pos, val in enumerate(lista):
            if num > val:
                posic = pos + 1
            elif num <= val:
                posic = pos
                break
        lista.insert(posic, num)
print(lista)
=======
print('-=' * 25)
print('{:-^50}'.format(' Lista Ordenada sem Sort'))
print('-=' * 25)

#lista = []
lista = list()
posic = 0

for i in range(0,5):
    num = int(input('Informe um Numero: '))
    if i == 0:
        lista.append(num)
    if i != 0:
        for pos, val in enumerate(lista):
            if num > val:
                posic = pos + 1
            elif num <= val:
                posic = pos
                break
        lista.insert(posic, num)
print(lista)
>>>>>>> Stashed changes
