
from time import sleep

cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:=^50}'.format(' Contagem Regressiva '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print(' POWW! CABUMM')

from time import sleep

cores = {'limpa':'\033[m',
         'txCiano':'\033[1;36m'}
print(cores['txCiano'], '==' * 25, cores['limpa'])
print('{:=^50}'.format(' Contagem Regressiva '))
print(cores['txCiano'], '==' * 25, cores['limpa'])

for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print(' POWW! CABUMM')

