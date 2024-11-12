# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome, gols):
    """ Função para escrever a Ficha do Jogador.
    Args:
        nome (_str_):_Nome do Jogador._
        gols (_int_): _Número de Gols._

    Returns:
        _str_: _Ficha do jogador_
    """

    if not nome: # se o nome for vazio.
        nome = "<Desconhecido>"

    return f"\033[91mO jogador {nome} com {gols} Gols no campeonato\033[m"
        
nom = str(input("Informe o seu Nome Jogador: ")).capitalize()
gol = str(input("Informe o número de Gol(s) pontuados: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

resposta = ficha(nom, gol)

print("=+=" * 10)
print(resposta)
print("=+=" * 10)  