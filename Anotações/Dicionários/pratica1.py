# Pessoas = dict
Pessoas = {'nome': 'Kayque', 'sexo': 'M', 'idade': 19}

while True:
    print("1- Adicionar elemento no Dicionário.")
    print("2 - Imprimir O Dicionário.")
    print("3 - Imprimir Keys.")
    print("4 - Imprimir Values.")
    print("5 - Imprimir Itens.")
    print("6 - Deletar Elemeto.")
    print("7 - Editar O Valor Cadastrado.")
    print("0 - Sair.")
    opcao = int(input("Informe Uma Opção do Menu: "))


    if opcao == 1:
        chave = str(input("Informe o Tópico do Elemento: "))
        valor = str(input("Informe as palavras que deseja adiconar neste Tópico: "))
        Pessoas[chave] = valor

    elif opcao == 2:
        print(f"O Dicionário Completo: \n{Pessoas}")
        print()
        print("Organizando Dados:")
        for k, v in Pessoas.items():
            print(f"Dados Relacionados ao {k}: {v}")
        print()

    elif opcao == 3:
        print(f'As Chaves do Dicionário:\n{Pessoas.keys()}')
    elif opcao == 4:
        print(f'Os Valores do Dicionário:\n{Pessoas.values()}')
    elif opcao == 5:
        print(f'Os Itens do Dicionário:\n{Pessoas.items()}')
    elif opcao == 6:
        deletar = str(input("Informe o Nome correspondente ao Elemento do Dicionário: "))
        
        if deletar in Pessoas:
            del Pessoas[deletar]
            print("Elemento Deletado!")
        else:
            print("Não Encontado.")
    elif opcao == 7:
        elemento = str(input("Informe o tipo do elemento associado: "))
        novo_valor = str(input("Informe Um Novo Contéudo: "))
        Pessoas[elemento] = novo_valor


    elif opcao == 0:
        print("Finalizando o Site...")
        break
    else:
        print("\033[91mOpção Inválida !\nTente Novamente\033[m")
