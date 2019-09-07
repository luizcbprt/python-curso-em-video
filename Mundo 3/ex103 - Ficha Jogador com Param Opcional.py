def ficha(nome='', gols=''):
    """
    -> Funcao para mostrar quantos Gols o jogador fez
    :param nome: Nome do Jogador
    :param gols: Quantidade de Gols
    :return: Retorna a quantidade de gols do jogador
    """
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0

    print(f'O Jogador {nome} fez {gols} gols')


jogador = str(input('Informe o Nome do Jogador: '))
qtdGols = input('Informe a quantidade de Gols: ')
ficha(jogador, qtdGols)