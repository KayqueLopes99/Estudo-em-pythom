import datetime
# Obtém o ano atual
hoje = datetime.datetime.now()
ano_atual = hoje.year


def voto(ano_de_nascimento):
    """_Função para verificar o status de votação com base no ano de nascimento_

    Args:
        ano_de_nascimento (_int_): _É O ANO INFORMADO PARA CALCULAR A IDADE._

    Returns:
        _str_: _Valor Literal_
    """
    idade = ano_atual - ano_de_nascimento
    if idade < 16:
        return f"Com {idade} anos: Voto Negado (Incapazes de Votar)"
    elif 16 <= idade <= 17 or idade >= 70:
        return f"Com {idade} anos: Voto Facultativo (Opcional)"
    else:
        return f"Com {idade} anos: Voto Obrigatório."

# Principal
print("=+=" * 10)
print("\033[34m- Menu de Votação - \033[m")
ano = int(input("Informe o seu Ano de Nascimento: "))
print(f"O Senhor(a) {voto(ano)}")
print("=+=" * 10)
