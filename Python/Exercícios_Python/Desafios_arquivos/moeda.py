def aumentar(moeda, pocentagem):
    """_Função para aumentar o dinheiro_

    Args:
        moeda (_float_): _Valor digitado_
        pocentagem (_int_): _Valor digitado_

    Returns:
        _int_: _resultado do aumento_
    """
    valor_porcento_aumento = pocentagem / 100
    resp = (moeda * valor_porcento_aumento)
    return moeda + resp



def diminuir(moeda, pocentagem):
    valor_porcento_diminuir = pocentagem / 100
    resp = (moeda * valor_porcento_diminuir)
    return moeda - resp


def dobra(moeda):
    resp = moeda * 2
    return resp


def metade(moeda):
    resp = moeda / 2
    return resp 

def formatar_moeda(moeda, p = 'R$'):
    """_Função para formatar a moeda_

    Args:
        moeda (_float_): _valor digitado_
        replasce() => Trocar uma coisa por outra.

    Returns:
        _type_: _description_
    """
    return f"{p} {moeda:,.2f}".replace(".", ",")

