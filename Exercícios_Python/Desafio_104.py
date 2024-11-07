# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(mensagem):
    """ Função para ler o inteiro.

    Args:
        mensagem (_str_): A mensagem da pergunta.

    Returns:
        _type_: Sem retorno.
    """
    while True:
        numero = input(mensagem)
        if numero.isdigit():  # Verifica se a entrada é um número positivo
            return int(numero)  # Retorna o número convertido para inteiro
        else:
            print("\033[91mErro! Por favor, digite um número inteiro válido.\033[m") 

print("=+=" * 10)
valor = leiaint('Digite um número: ')
print(f"\033[92mVocê acabou de digitar o número {valor}.\033[m")
print("=+=" * 10)