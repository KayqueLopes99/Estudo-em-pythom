# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano_de_nascimento):
    from datetime import date
    # Obtém o ano atual
    ano_atual = date.today().year
    """_Função para verificar o status de votação com base no ano de nascimento_

    Args:
        ano_de_nascimento (_int_): _É O ANO INFORMADO PARA CALCULAR A IDADE._

    Returns:
        _str_: _Valor Literal_
    """
    idade = ano_atual - ano_de_nascimento
    if idade < 16:
        return f"Com {idade} anos: Voto Negado (Incapazes de Votar)"
    elif 16 <= idade <= 17 or idade >= 65:
        return f"Com {idade} anos: Voto Facultativo (Opcional)"
    else:
        return f"Com {idade} anos: Voto Obrigatório."

# Principal
print("=+=" * 10)
print("\033[34m- Menu de Votação - \033[m")
ano = int(input("\033[91mInforme o seu Ano de Nascimento: \033[m"))
print(f"O Senhor(a) {voto(ano)}")
print("=+=" * 10)
