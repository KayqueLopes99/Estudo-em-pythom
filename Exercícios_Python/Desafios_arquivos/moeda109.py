def formatar_moeda(moeda):
    """_Função para formatar a moeda_

    Args:
        moeda (_float_): _valor digitado_
        replasce() => Trocar uma coisa por outra.

    Returns:
        _type_: _description_
    """
    return f"R${moeda:,.2f}".replace(".", ",")


def metade(moeda, valor=False):
    resulta = moeda/2
    if valor == True:
        resp = formatar_moeda(resulta)
    else:
        resp = resulta
    return resp


def aumentar(moeda, pocentagem, valor=False):
    """_Função para aumentar o dinheiro_

    Args:
        moeda (_float_): _Valor digitado_
        pocentagem (_int_): _Valor digitado_

    Returns:
        _int_: _resultado do aumento_
    """
    valor_porcento_aumento = pocentagem / 100
    calculo = (moeda * valor_porcento_aumento)
    resp1 =  moeda + calculo

    if valor == True:
        resp = formatar_moeda(resp1)
    else:
        resp = resp1
    
    return resp





def diminuir(moeda, pocentagem, valor=False):
    valor_porcento_diminuir = pocentagem / 100
    calculo = (moeda * valor_porcento_diminuir)
    resp1 = moeda - calculo 
    if valor == True:
        resp = formatar_moeda(resp1)
    else:
        resp = resp1
    return resp



def dobra(moeda, valor=False):
    resulta = moeda * 2
    if valor == True:
        resp = formatar_moeda(resulta)
    else:
        resp = resulta
    return resp
    

def resumo(preço, porcento, VALOR):
    print("-"*55)
    print(f"============= Resumo do Preço R$ {preço} ================")
    print("-"*55)
    print(f'\033[91mA Metade de {formatar_moeda(preço)}:\033[m {metade(preço, True):>26}')
        
    print(f'\033[93mO Dobro de {formatar_moeda(preço)}:\033[m {dobra(preço, True):>28}')
        
    print(f'\033[94mAumentando {porcento}% de {formatar_moeda(preço)}:\033[m {aumentar(preço, porcento, True):>20}')
        
    print(f'\033[96mDiminuindo {porcento}% de {formatar_moeda(preço)}:\033[m {diminuir(preço, porcento, True):>20}')
    print("-"*55)
        