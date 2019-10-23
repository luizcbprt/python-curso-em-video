
import random

num_pc = random.randint(0,5)
num_user = int(input('Informe um numero entre 0 e 5: '))

if num_pc == num_user:
    print('''
        Você venceu!
        O Computador pensou no numero {}, e você adivinhou!
        '''.format(num_pc))
else:
    print('''
        Você perdeu!
        O Computador pensou em {}, mas você falou {}
        '''.format(num_pc, num_user))

import random

num_pc = random.randint(0,5)
num_user = int(input('Informe um numero entre 0 e 5: '))

if num_pc == num_user:
    print('''
        Você venceu!
        O Computador pensou no numero {}, e você adivinhou!
        '''.format(num_pc))
else:
    print('''
        Você perdeu!
        O Computador pensou em {}, mas você falou {}
        '''.format(num_pc, num_user))

