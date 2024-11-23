"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
import os
while True:

    print("-"*28)
    print("\033[92m===== Validação do CPF =====\033[m")
    print("-"*28)
    print("\033[94m[1] - Inserir CPF para validação.\033[m")
    print("\033[94m[0] - Sair do software.\033[m")
    print("-"*28)

    op = input("\033[92mInforme uma opção: \033[m")

    if not op.isdigit():
        print("Informe Algarismos somente.")
        continue
    opcao_convertida = int(op)
     
    if opcao_convertida == 1:

        lista_com_9_digitos_cpf = []
        lista_com_10_digitos_cpf = []
        contador_regressivo_1 = 10
        contador_regressivo_2 = 11
        
        cpf = input("Informe o Cpf para validação: ").replace(".", "").replace("-", "")

        if not cpf.isdigit() or len(cpf) != 11:
            print("\033[91mO CPF deve ter exatamente 11 dígitos e conter apenas números. Tente novamente.\033[m")
            continue

        cpf_fatiado_nove_digitos = str(cpf)[:9]
        cpf_fatiado_dez_digitos = str(cpf)[:10]
        cpf_padronizado = f"{str(cpf)[:3]}.{str(cpf[3:6])}.{str(cpf[6:9])}-{str(cpf[9:11])}"

        for digito_contagem in cpf_fatiado_nove_digitos:
            int_digito_contagem = int(digito_contagem)         
            numero_cpf = int_digito_contagem * contador_regressivo_1
            lista_com_9_digitos_cpf.append(numero_cpf)
            contador_regressivo_1 -= 1

        soma_valores_dos_nove_digitos_1 = sum(lista_com_9_digitos_cpf)
        operacao_1 = (soma_valores_dos_nove_digitos_1 * 10) % 11
        resultado_primeiro_digito = operacao_1 if operacao_1 <= 9 else 0
        # print(f"Primeiro dígito verificador calculado: {resultado_primeiro_digito}")
        # print(f"Lista de cálculos: {lista_com_9_digitos_cpf}")
          
        for digito_contagem in cpf_fatiado_dez_digitos:
            if contador_regressivo_2 != 1:
               int_digito_contagem = int(digito_contagem)         
               numero_cpf = int_digito_contagem * contador_regressivo_2
               lista_com_10_digitos_cpf.append(numero_cpf)
               contador_regressivo_2 -= 1
        
        soma_valores_dos_nove_digitos_2 = sum(lista_com_10_digitos_cpf)
        operacao_2 = (soma_valores_dos_nove_digitos_2 * 10) % 11
        resultado_segundo_digito = operacao_2 if operacao_2 <= 9 else 0

        # print(f"Segundo dígito verificador calculado: {resultado_segundo_digito}")
        # print(f"Lista de cálculos: {lista_com_10_digitos_cpf}")
        
        if resultado_primeiro_digito == int(cpf[9]) and resultado_segundo_digito == int(cpf[10]):
            print(f"\033[92mSucesso! Cpf: {cpf_padronizado} é válido para todo país! \033[m")   
        else:
            print("\033[91mErro! Cpf não é válido para todo país! \033[m")

    elif opcao_convertida == 0:
        print("\033[91mSaindo do software.\033[m")
        os.system("cls")
        break
    else:
        print("\033[91mOpção inválida. Escolha entre 0 e 1.\033[m")
        continue