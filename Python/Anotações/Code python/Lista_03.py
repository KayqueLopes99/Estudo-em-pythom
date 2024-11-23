Segunda_lista = list()
tatalMaior = Totalmenor = 0
while True:
    print("++++++ Menu +++++++")
    print("1 - Colocar Elementos na Primeira Lista e Combinar Listas.")
    print("2 - Alterar Elementos.")
    print("3 - Ver elemento selecionado.")
    print("4 - Imprime Lista.")
    print("5 - Pessoas maiores de Idade.")
    print("0 - Sair.")
    opção = int(input("Informe Uma opçõa do Menu: "))

    if opção == 1:
        quantidade = int(input("Informe A Quantidade de pessoas que você deseja inserir: "))
        for c in range(0,quantidade):
            
            pessoa = str(input("Informe o Nome de Pessoa: "))
            idade = int(input("Informe a Idade da pessoa: "))
            # Crie uma lista temporária para cada pessoa e idade
            Primeira_lista = [pessoa, idade]
            Segunda_lista.append(Primeira_lista)  # Adicione a lista temporária à Primeira_lista

        print("Informações Adicionada com Sucesso!")
        print("Juntando as listas...")
        print(f'Combinação da listas:\n{Segunda_lista}')
    
    elif opção == 2:
        while True:
            print("1 - Alterar Todo os Dados de Uma pessoa.")
            print("2 - Alterar Idade ou Nome de uma pessoa.")
            print("0 - Sair.")
            
            op2 = int(input("Informe um opção: "))
            if op2 == 1:
                indice_da_lista = int(input("Informe o Indice da Lista"))
                pessoa = str(input("Informe o Nome de Pessoa: "))
                idade = int(input("Informe a Idade da pessoa: "))
                temp_lista = [pessoa, idade]
                del Segunda_lista[indice_da_lista]
                Segunda_lista.insert(indice_da_lista, temp_lista)
                print(Segunda_lista)
            if op2 == 2:
                indice_da_lista = int(input("Informe o Indice da Lista: "))
                print("Sub índices:\n1- Nome.\n2- Idade.")
                op3 = int(input("Informe o Sub-índice da Lista: "))
                if op3 == 1:
                    pessoa = str(input("Informe o Novo Nome da Pessoa: "))
                    Segunda_lista[indice_da_lista][0] = pessoa
                    print(Segunda_lista)
                elif op3 == 2:
                    idade = int(input("Informe a Nova Idade da Pessoa: "))
                    Segunda_lista[indice_da_lista][1] = idade
                    print(Segunda_lista)
            if op2 == 0:
                print("\033[35mSaindo da Opção ...\033[m")
                break
    elif opção == 3:
        while True:
            print("1 - Ver toda informação de uma pessoa.")
            print("2 - Ver Idade ou Nome de uma pessoa.")
            print("0 - Sair.")
            
            op4 = int(input("Informe um opção: "))
            if op4 == 1:
                indice_da_lista = int(input("Informe o Indice da Lista"))
                print(f"Informações Selecionadas da {indice_da_lista} Pessoa:\n{Segunda_lista[indice_da_lista]}")
            if op4 == 2:
                indice_da_lista = int(input("Informe o Indice da Lista: "))
                print("Sub índices:\n0- Nome.\n1- Idade.")
                op5 = int(input("Informe o Sub-índice da Lista: "))
                if op5 == 1:
                    print(f"Nome da {indice_da_lista} pessoa: {Segunda_lista[indice_da_lista][op5]}")
                elif op5 == 2:
                    print(f"Idade da {indice_da_lista} pessoa: {Segunda_lista[indice_da_lista][op5]}")
            if op4 == 0:
                print("\033[35mSaindo da Opção ...\033[m")
                break
    elif opção == 4:
        
        for p in Segunda_lista:
            print(f"\033[34m{p[0]} tem {p[1]} anos de Idade.\033")
    elif opção == 5:
        for p in Segunda_lista:
            if p[1] >= 18:
                print(f"{p[0]} é maior de idade.")
                tatalMaior += 1
            else:
                print(f"{p[0]} é menor de idade.")
                Totalmenor += 1
        print(f'Temos {tatalMaior} Pessoas Maiores de Idade\nTemos {Totalmenor} Menores de Idade.')
    elif opção == 0:
                print("\033[35mSaindo...\033[m")
                break
    else:
        print("Informe Algo válido.")