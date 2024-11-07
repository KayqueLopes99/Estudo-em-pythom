"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores
"""

# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep

C = [
    '\033[m',       # 0 - sem cores
    '\033[0;30;91m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco
]

def titulos(msg, cor=0):
    """Exibe um título com bordas coloridas."""
    tam = len(msg) + 4
    print("~" * tam)
    print(C[cor] + f"  {msg}  " + C[0])
    print("~" * tam)


def interactiveHELP(comando, cor=0):
    print(f"\033[47;30mAbaixo estão as informações sobre o comando '{comando}':\033[m")
    sleep(2)
    print(C[4], end='')
    help(comando)  
    print(C[0], end='')
    sleep(2)
    


while True:
    titulos('Sistema de Comandos',1)
    sleep(2)
    print("1 - Colocar comando.")
    print("2 - Finalizar.")
    op = int(input("Informe uma opção: "))
    
    
    if op == 1:
        comando = input("\033[92mInforme o comando do Python: \033[m").lower() 
        interactiveHELP(comando)
        
    elif op == 2:
        print("\033[92mSaindo ...\033[m")  
        break
    else:
        print("\033[91mERRO! Tente novamente.\033[m")