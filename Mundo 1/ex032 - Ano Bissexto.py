<<<<<<< Updated upstream
from calendar import isleap
from datetime import date

ano = int(input('Informe um ano para analisar ou 0 para ano Atual: '))

if ano == 0:
    ano = date.today().year

if isleap(ano):
    print('O Ano {} é Bisexto'.format(ano))
else:
    print('O Ano {} NÃO é Bisexto'.format(ano))
=======
from calendar import isleap
from datetime import date

ano = int(input('Informe um ano para analisar ou 0 para ano Atual: '))

if ano == 0:
    ano = date.today().year

if isleap(ano):
    print('O Ano {} é Bisexto'.format(ano))
else:
    print('O Ano {} NÃO é Bisexto'.format(ano))

>>>>>>> Stashed changes
