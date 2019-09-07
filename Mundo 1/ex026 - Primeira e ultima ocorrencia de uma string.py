frase = input('Informe uma frase: ')

qtd_a = frase.lower().count('a')
pos_prim = frase.lower().find('a')
pos_ultima = frase.lower().rfind('a')

print('''
   A frase informada foi '{}'
   Ela possui {} letras 'a'
   A primeira letra 'a' está na posição {}
   A ultima letra 'a' está na posição {}   
    
'''.format(frase, qtd_a, pos_prim, pos_ultima))

frase = input('Informe uma frase: ')

qtd_a = frase.lower().count('a')
pos_prim = frase.lower().find('a')
pos_ultima = frase.lower().rfind('a')

print('''
   A frase informada foi '{}'
   Ela possui {} letras 'a'
   A primeira letra 'a' está na posição {}
   A ultima letra 'a' está na posição {}   
    
'''.format(frase, qtd_a, pos_prim, pos_ultima))
