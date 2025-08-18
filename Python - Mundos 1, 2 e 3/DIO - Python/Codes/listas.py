"""
Exercício 1 - Lista
Crie um programa que peça ao usuário para inserir nomes de frutas em uma lista. O usuário pode continuar adicionando frutas até digitar "sair". Em seguida, exiba:

A lista completa das frutas.

O total de frutas adicionadas.

A fruta mais longa (com mais caracteres).
"""
lista_de_frutas = []

def valida_opcao(variavel):
    if isinstance(variavel, int) or (isinstance(variavel, str) and variavel.isdigit()):
        variavel_inteiro = int(variavel)
        if 1 <= variavel_inteiro <= 4:
            return variavel_inteiro
        else:
            print("\033[91mOpção selecionada não está no intervalo [1-4].\033[m")
    else:
        print("\033[91mA opção escolhida deve ser um número inteiro.\033[m")



while True:
    print("-"*15)
    print("[1] - Adicionar Fruta.")
    print("[2] - Remover Fruta.")
    print("[3] - Listar frutas adicionmadas.")
    print("[4] - Sair.")

    opcao = valida_opcao(input("Informe um opção do menu: "))

    match opcao:
        case 1:

            alimento = input("Informe a Fruta ou Legume a ser adicionado na lista: ").strip().capitalize()
            if alimento in lista_de_frutas:
                print("\033[91mAlimento já está na lista.\033[m")
            else:
                lista_de_frutas.append(alimento)
                print("\033[92mAlimento Adicionado na lista.\033[m")
        case 2:
            alimento = input("Informe a Fruta ou Legume a ser adicionado na lista: ").strip().capitalize()
            if alimento not in lista_de_frutas:
                print("\033[91mAlimento a ser removido não está na lista.\033[m")
            else:
                 lista_de_frutas.remove(alimento)
                 print("\033[92mAlimento Removido na lista.\033[m")


        case 3:
            print("\nLista de frutas:")
            print("Total de frutas adicionadas:", len(lista_de_frutas))
            if lista_de_frutas:
                print("-"*15)
                for fruta in lista_de_frutas:
                  print(f"{fruta}")
                print("-"*15)
            
            if lista_de_frutas:
               fruta_mais_longa = max(lista_de_frutas, key=len)
               print("\033[92mA fruta com o maior nome é:\033[m", fruta_mais_longa)

            else:
              print("\033[91mNenhuma fruta foi adicionada.\033[m")

            
        case 4:
            print("\033[92mSaindo.\033[m")
            break
            

    