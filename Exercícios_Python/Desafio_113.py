# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaFloat(mensagem):
    """Função para ler um número real com:
    - Solicita a entrada do usuário e substitui vírgula por ponto;
    - Tenta converter o número para float;

    Args:
        mensagem (_type_): _description_

    Returns:
        _Float_: Número real
    """
    while True:
        try:
            numero = input(mensagem).replace(',', '.')
            
             
            return float(numero)
        
        except ValueError:
            
            print("\033[91mErro! Por favor, digite um número Real válido.\033[m")
        
        except KeyboardInterrupt:
            print('\033[91mDados não informados pelo Usuário.\033[m')
def leiaint(mensagem):
    """ Função para ler o inteiro.

    Args:
        mensagem (_str_): A mensagem da pergunta.

    Returns:
        _int_: Numero inteiro.
    """
    while True:
        try:
            
            numero = input(mensagem)
            
            return int(numero)
        
        except ValueError:
            
            print("\033[91mErro! Por favor, digite um número Inteiro válido.\033[m")
        
        except KeyboardInterrupt:
            print('\033[91mDados não informados pelo Usuário.\033[m')
print("=+=" * 10)
valor = leiaint('Digite um número Inteiro: ')
valor01 = leiaFloat('Digite um número Real: ')
print(f"\033[92mVocê acabou de digitar o Número Inteiro: {valor} e um Número Real: {valor01}.\033[m")
print("=+=" * 10)