# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from Desafios_arquivos import moeda109
from time import sleep
import os
 

while True:
    print("===== Menu =====")
    print("-" * 15)
    print("\033[31m 1 - Metade.\033[m")
    print("\033[31m 2 - Dobrar.\033[m")
    print("\033[31m 3 - Aumentar.\033[m")
    print("\033[31m 4 - Diminuir.\033[m")
    print("\033[31m 0 - Finalizar.\033[m")
    print("-" * 15)

    op = int(input('Informe uma opção do Menu: '))
    

    if 0 <= op <= 4:
        if op != 0:  
            preço = float(input("\033[92mDigite o Preço: R$ \033[m"))
            porcento = float(input("\033[95mDigite a porcentagem: \033[m"))

        if op == 1:
            print(f'\033[91mA Metade de {moeda109.formatar_moeda(preço)}:\033[m {moeda109.metade(preço, True)}')
        elif op == 2:
            print(f'\033[93mO Dobro de {moeda109.formatar_moeda(preço)}:\033[m {moeda109.dobra(preço, True)}')
        elif op == 3:
            print(f'\033[94mAumentando {porcento}% de {moeda109.formatar_moeda(preço)}:\033[m {moeda109.aumentar(preço, porcento, True)}')
        elif op == 4:
            print(f'\033[96mDiminuindo {porcento}% de {moeda109.formatar_moeda(preço)}:\033[m {moeda109.diminuir(preço, porcento, True)}')
        elif op == 0:
            print("\033[92mSaindo ... \033[m")
            break
        sleep(1)  
    else:
        print(f"\033[91mOpção Inválida!\033[m")
        os.system('cls')