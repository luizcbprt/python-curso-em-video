<<<<<<< Updated upstream
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
'''
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[0][2])
print(lanche[1:])
print(lanche[:2])
print(lanche[-3:])
'''
#Maneira 1
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('--' * 25)
#Maneira 2
for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]}')

print('--' * 25)
#Maneira 3
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posicao {pos}')

print('--' * 25)
print(sorted(lanche))
=======
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
'''
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[0][2])
print(lanche[1:])
print(lanche[:2])
print(lanche[-3:])
'''
#Maneira 1
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('--' * 25)
#Maneira 2
for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]}')

print('--' * 25)
#Maneira 3
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posicao {pos}')

print('--' * 25)
print(sorted(lanche))


>>>>>>> Stashed changes
