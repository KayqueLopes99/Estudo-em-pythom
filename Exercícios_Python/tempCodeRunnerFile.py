from Desafios_arquivos import moeda
from time import sleep

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
            print(f'\033[91mA Metade de {moeda.formatar_moeda(preço)}:\033[m {moeda.formatar_moeda(moeda.metade(preço))}')
        elif op == 2:
            print(f'\033[93mO Dobro de {moeda.formatar_moeda(preço)}:\033[m {moeda.formatar_moeda(moeda.dobra(preço))}')
        elif op == 3:
            print(f'\033[94mAumentando {porcento}% de {moeda.formatar_moeda(preço)}:\033[m {moeda.formatar_moeda(moeda.aumentar(preço, porcento))}')
        elif op == 4:
            print(f'\033[96mDiminuindo {porcento}% de {moeda.formatar_moeda(preço)}:\033[m {moeda.formatar_moeda(moeda.diminuir(preço, porcento))}')
        elif op == 0:
            print("\033[92mSaindo ... \033[m")
            break
        sleep(1)  
    else:
        print(f"\033[91mOpção Inválida!\033[m")