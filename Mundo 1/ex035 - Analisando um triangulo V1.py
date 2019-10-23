
print('='*20)
print('Analisador de Triangulos')
print('='*20)

reta1 = int(input('Informe a primeira reta: '))
reta2 = int(input('Informe a segunda reta: '))
reta3 = int(input('Informe a terceira reta: '))

r1_true = 'N'
r2_true = 'N'
r3_true = 'N'

if reta1 < (reta2 + reta3) and reta1 > abs(reta2 - reta3):
    r1_true = 'S'
if reta2 < (reta1 + reta3) and reta2 > abs(reta1 - reta3):
    r2_true = 'S'
if reta3 < (reta1 + reta2) and reta3 > abs(reta1 - reta2):
    r3_true = 'S'

if r1_true == 'S' and r2_true == 'S' and r3_true == 'S':
    print('As Retas podem formar um triangulo! ')
else:
    print('As Retas NÃO podem formar um triangulo')

print('='*20)
print('Analisador de Triangulos')
print('='*20)

reta1 = int(input('Informe a primeira reta: '))
reta2 = int(input('Informe a segunda reta: '))
reta3 = int(input('Informe a terceira reta: '))

r1_true = 'N'
r2_true = 'N'
r3_true = 'N'

if reta1 < (reta2 + reta3) and reta1 > abs(reta2 - reta3):
    r1_true = 'S'
if reta2 < (reta1 + reta3) and reta2 > abs(reta1 - reta3):
    r2_true = 'S'
if reta3 < (reta1 + reta2) and reta3 > abs(reta1 - reta2):
    r3_true = 'S'

if r1_true == 'S' and r2_true == 'S' and r3_true == 'S':
    print('As Retas podem formar um triangulo! ')
else:
    print('As Retas NÃO podem formar um triangulo')

