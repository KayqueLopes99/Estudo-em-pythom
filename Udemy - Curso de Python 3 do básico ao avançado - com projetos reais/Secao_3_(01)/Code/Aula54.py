"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_de_compras = []

while True:
    print("-"*28)
    print("\033[92m===== Lista de Compras =====\033[m")
    print("-"*28)
    print("[1] - Inserir produto na Lista de Compras.")
    print("[2] - Remover produto na Lista de Compras.")
    print("[3] - Imprimir Lista de Compras.")
    print("[0] - Sair do software.")
    print("-"*28)

    op = input("\033[92mInforme uma opção: \033[m")

    if not op.isdigit():
        print("Informe Algarismos somente ")
        continue

    opcao_convertida = int(op)
     
    if opcao_convertida == 1:
        
        produto = input("Informe o nome do produto para inserir: ").capitalize()
        if not produto.isalpha():
            print("Apenas Letras no nome do produto.")
            continue

        if produto in lista_de_compras:
            print("Produto já se encontra na lista.")
        else:
            lista_de_compras.append(produto)
    
    elif opcao_convertida == 2:
        # Aqui coloquei para remover pelo nome do produto, mas pode ser pelo indice. 
        produto = input("Informe o nome do produto para remover: ").capitalize()
        

        if produto not in lista_de_compras:
            print("Produto não se encontra na lista.")
        else:
            for indice, item_atual in enumerate(lista_de_compras):
                if item_atual == produto:
                    print(f"Item {lista_de_compras[indice]} Removido.")
                    del lista_de_compras[indice]
                    break
                    

    elif opcao_convertida == 3:
        if not lista_de_compras:
            print("\033[93mA lista de compras está vazia.\033[m")
        else:
            print("\033[94m--- Produtos na Lista ---\033[m")
            for indices, produtos in enumerate(lista_de_compras):
                print(f"[{indices}] Produto: {produtos}")


    elif opcao_convertida == 0:
        print("\033[91mSaindo do software.\033[m")
        os.system("cls")
        break
    else:
        print("\033[91mOpção inválida. Escolha entre 0 e 3.\033[m")
        continue
