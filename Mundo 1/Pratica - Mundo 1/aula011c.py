nome = str(input('Informe seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m'}

print('Prazer em de conhecer, {}{}{} !!!'.format(cores['azul'], nome, cores['limpa']))
