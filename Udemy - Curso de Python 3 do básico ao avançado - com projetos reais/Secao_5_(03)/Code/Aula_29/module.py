"""Este é um módulo de exemplo
 
 Este módulo contém funções e exemplos de documentação de funções.
 A função soma você já conhece bastante.
 """
def print(msg):
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"{msg}"


def summ(x, y):
    """ Função de somatória

    Args:
        x (_int_): váriavel numerica.
        y (_int_): váriavel numerica.

    Returns:
        _int_: O resultado da Soma
    """
    s = sum(x, y)
    return s


class Information:
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        self.name = name