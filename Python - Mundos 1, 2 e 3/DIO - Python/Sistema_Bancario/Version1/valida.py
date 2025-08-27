from random import randint
from datetime import datetime

def valida_numero(variavel):
    if isinstance(variavel, (int, float)): 
        return variavel

    if isinstance(variavel, str):  
        variavel = variavel.strip()
    
        if not variavel:  
            print("\033[91mErro: Entrada vazia. Insira um número válido.\033[m")
            return None
        
        if variavel.isdigit():  
            return int(variavel)
        
        try:
            return float(variavel)  
        except ValueError:
            print("\033[91mErro: Entrada inválida. Insira um número válido.\033[m")
            return None
    
    print("\033[91mErro: Tipo de dado inválido.\033[m")
    return None


def valida_opcao(variavel):
    if isinstance(variavel, int) or (isinstance(variavel, str) and variavel.isdigit()):
        variavel_inteiro = int(variavel)
        if 1 <= variavel_inteiro <= 4:
            return variavel_inteiro
        else:
            print("\033[91mOpção selecionada não está no intervalo [1-4].\033[m")
    else:
        print("\033[91mA opção escolhida deve ser um número inteiro.\033[m")


