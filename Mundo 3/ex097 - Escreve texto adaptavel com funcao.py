def titulo(msg):
    print('-=' * 25)
    print(str(msg).center(50, ' '))
    print('-=' * 25)


titulo('Escreve texto Adaptavel')
print()

def escreve(texto):
    tamanho = len(texto)
    print('~' * tamanho)
    print(texto)
    print('~' * tamanho)


escreve('Testando texto adaptavel utilizando funcao')
escreve('Rafael')
escreve('maffu')
escreve('oi')