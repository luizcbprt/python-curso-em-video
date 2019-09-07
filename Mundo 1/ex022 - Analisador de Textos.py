<<<<<<< Updated upstream
nome = input('Informe seu nome Completo: ')
maiusc = nome.upper()
minusc = nome.lower()

qtd_s_espaco = len(nome.replace(' ',''))
qtd_prim_nome = len(nome[0:nome.lstrip().find(' ')])

primeiro_nome = nome[0:nome.lstrip().find(' ')]

print("""

Nome em maiusculo: {}
Nome em Minusculo: {}
Comprimento sem espaço: {}
QTD Letras primeiro nome: {}
Primeiro Nome: {}
    
    
""".format(maiusc, minusc, qtd_s_espaco, qtd_prim_nome, primeiro_nome))
=======
nome = input('Informe seu nome Completo: ')
maiusc = nome.upper()
minusc = nome.lower()

qtd_s_espaco = len(nome.replace(' ',''))
qtd_prim_nome = len(nome[0:nome.lstrip().find(' ')])

primeiro_nome = nome[0:nome.lstrip().find(' ')]

print("""

Nome em maiusculo: {}
Nome em Minusculo: {}
Comprimento sem espaço: {}
QTD Letras primeiro nome: {}
Primeiro Nome: {}
    
    
""".format(maiusc, minusc, qtd_s_espaco, qtd_prim_nome, primeiro_nome))
>>>>>>> Stashed changes
