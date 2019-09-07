def buscaHelp(pComando):
    """
    -> Programa interativo para buscar o Help do Python e mostrar o resultado
    :param pComando: Comando para busca no Help
    :return: retorna o doc do Help interativo do Python
    """
    return help(pComando)


while True:
    textoBusca = str(input('Informe um comando para buscar Ajuda. SAIR para cancelar: ')).strip()
    if str(textoBusca).upper().strip() == 'SAIR':
        break
    print(buscaHelp(textoBusca))