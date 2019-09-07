def voto(anoNasc=2018):
    """
    -> Retorna se uma pessoa deve ou nao votar baseado na idade
    :param anoNasc: Ano de Nascimento da pessoa
    :return: String indicando se a pessoa deve votar ou não
    opcional >= 65
    obrigatorio = 18
    Nao vota < 16
    """
    from datetime import date
    idade = date.today().year - anoNasc # Calcula o Ano de Nascimento
    if idade >= 65:
        return f'A Pessoa tem {idade} anos. Voto é OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'A Pessoa tem {idade} anos. Voto é OBRIGATORIO'
    else:
        return f'A Pessoa tem {idade} anos. Nao Vota'


# Main Program
anoInformado = int(input('Informe em que ano a Pessoa Nasceu: '))
print(voto(anoInformado))
