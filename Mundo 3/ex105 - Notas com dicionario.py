def notas(*notas, situac=False):
    """
    -> Calcula Tota, Media e Notas de alunos. Parametro Situac exibe ou nao a situação da turma
    :param notas: Notas dos alunos
    :param situac: True ou False, mostra ou nao a situação da turma
    :return: Dicionario com o resultado dos calculos
    """
    dictResult = {}
    totNotas = 0
    for indice, nt in enumerate(
        notas
    ):  # Enumerate para pegar o indice da iteração
        # Armazena a Maior e Menor Nota
        if indice == 0:
            maiorNota = nt
            menorNota = nt
        else:
            if nt > maiorNota:
                maiorNota = nt
            if nt < menorNota:
                menorNota = nt

        # Soma as notas em uma variável para pegar a média
        totNotas += nt
    medNotas = totNotas / len(notas)  # Calcula a Media

    # Atualiza as informacoes no dicionario
    dictResult.update(
        {
            'Quantidade de Notas': len(notas),
            'Maior Nota': maiorNota,
            'Menor Nota': menorNota,
            'Media Turma': medNotas,
        }
    )

    # Se foi informado parametro situa == True então atualiza o dicionario com a situacao da turma
    if situac == True:
        if medNotas >= 7:
            dictResult.update({'Situacao': 'BOA'})
        elif medNotas >= 5:
            dictResult.update({'Situacao': 'Mais ou Menos'})
        else:
            dictResult.update({'Situacao': 'Ruim'})

    print(dictResult)


notas(5, 8, 9)
notas(10, 4, 2, situac=True)