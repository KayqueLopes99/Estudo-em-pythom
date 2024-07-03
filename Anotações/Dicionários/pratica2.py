import os 
Nordeste = {
    'Alagoas': {'Uf': 'Alagoas', 'sigla': 'AL'},
    'Bahia': {'Uf': 'Bahia', 'sigla': 'BA'},
    'Ceará': {'Uf': 'Ceará', 'sigla': 'CE'},
    'Paraíba': {'Uf': 'Paraíba', 'sigla': 'PB'},
    'Pernambuco': {'Uf': 'Pernambuco', 'sigla': 'PE'},
    'Piauí': {'Uf': 'Piauí', 'sigla': 'PI'},
    'Rio grande do norte': {'Uf': 'Rio Grande do Norte', 'sigla': 'RN'},
    'Maranhão': {'Uf': 'Maranhão', 'sigla': 'MA'},
    'Sergipe': {'Uf': 'Sergipe', 'sigla': 'SE'}
}

Norte = {
    'Acre': {'Uf': 'Acre', 'sigla': 'AC'},
    'Amapá': {'Uf': 'Amapá', 'sigla': 'AP'},
    'Amazonas': {'Uf': 'Amazonas', 'sigla': 'AM'},
    'Pará': {'Uf': 'Pará', 'sigla': 'PA'},
    'Rondônia': {'Uf': 'Rondônia', 'sigla': 'RO'},
    'Roraima': {'Uf': 'Roraima', 'sigla': 'RR'},
    'Tocantins': {'Uf': 'Tocantins', 'sigla': 'TO'}

}

Sudeste = {
    'Espírito santo': {'Uf': 'Espírito Santo', 'sigla': 'ES'},
    'Minas gerais': {'Uf': 'Minas Gerais', 'sigla': 'MG'},
    'Rio de janeiro': {'Uf': 'Rio de Janeiro', 'sigla': 'RJ'},
    'São paulo': {'Uf': 'São Paulo', 'sigla': 'SP'}

}

Sul = {
    'Paraná': {'Uf': 'Paraná', 'sigla': 'PR'},
    'Rio grande do sul': {'Uf': 'Rio Grande do Sul', 'sigla': 'RS'},
    'Santa catarina': {'Uf': 'Santa Catarina', 'sigla': 'SC'}

}
Centro_oeste = {
    'Distrito federal': {'Uf': 'Distrito Federal', 'sigla': 'DF'},
    'Goiás': {'Uf': 'Goiás', 'sigla': 'GO'},
    'Mato grosso': {'Uf': 'Mato Grosso', 'sigla': 'MT'},
    'Mato grosso do sul': {'Uf': 'Mato Grosso do Sul', 'sigla': 'MS'}
   
}

Novos_Estados = dict()


while True:
    print("1 - Imprimir.")
    print("2 - Adicionar Estados Novos.")
    print("3 - Remover Estados.")
    print("0 - Sair.")
    opcao = int(input("Informe Uma Opção do Menu: "))


    if opcao == 1:

        print("1 - Imprimir Todos os Elementos.")
        print("2 - Imprimir Estado.")

        op1 = int(input("Informe uma Opção do Sub-Menu: "))
        if op1 == 1:
            print('\033[91m============ Região Nordeste ============\033[m')
            for estado in Nordeste:
                print(f"Estado: {Nordeste[estado]['Uf']} - Sigla: ({Nordeste[estado]['sigla']})")
            print('\033[91m============ Região Norte ============\033[m')
            for estado in Norte:
                print(f"Estado: {Norte[estado]['Uf']} - Sigla: ({Norte[estado]['sigla']})")
            print('\033[91m============ Região Centro Oeste ============\033[m')
            for estado in Centro_oeste:
                print(f"Estado: {Centro_oeste[estado]['Uf']} - Sigla: ({Centro_oeste[estado]['sigla']})")
            print('\033[91m============ Região Sudeste ============\033[m')
            for estado in Sudeste:
                print(f"Estado: {Sudeste[estado]['Uf']} - Sigla: ({Sudeste[estado]['sigla']})")
            print('\033[91m============ Região Sul ============\033[m')
            for estado in Sul:
                print(f"Estado: {Sul[estado]['Uf']} - Sigla: ({Sul[estado]['sigla']})")
        elif op1 == 2:
            print("==== Região ====")
            print("Nordeste.")
            print("Norte.")
            print("Centro Oeste.")
            print("Sudeste.")
            print("Sul.")

            regiao = str(input("Informe A região: ")).capitalize()
            estado = str(input("Informe O Estado: ")).capitalize()

            if regiao == 'Nordeste' and estado in Nordeste:
               print(f"Região {regiao}:\nInformação do Estado {estado}:\n{Nordeste[estado]}")
            elif regiao == 'Norte' and estado in Norte:
                print(f"Região {regiao}:\nInformação do Estado {estado}:\n{Norte[estado]}")
            elif regiao == 'Centro_oeste' and estado in Centro_oeste:
                print(f"Região {regiao}:\nInformação do Estado {estado}:\n{Centro_oeste[estado]}")
            elif regiao == 'Sudeste' and estado in Sudeste:
                print(f"Região {regiao}:\nInformação do Estado {estado}:\n{Sudeste[estado]}")
            elif regiao == 'Sul' and estado in Sul:
                print(f"Região {regiao}:\nInformação do Estado {estado}:\n{Sul[estado]}")
            else:
                print(f"Estado {estado} não encontrado na região {regiao}.")
        else:
            print("\033[91mOpção Inválida !\nTente Novamente\033[m")

    elif opcao == 2:
        qtd = int(input("Informe quantos Estados Você Irá Adicionar: "))
        for c in range(0, qtd):
            Estado = str(input('Informe o Nome do Estado: ')).capitalize()
            Sigla = str(input('Informe a Sigla do Estado: ')).upper()
            # O Nome do estado  será a chave e a cada iteração ele coloca a uf e a sigla de cada estado.
            Novos_Estados[Estado] = {'Uf': Estado, 'Sigla': Sigla}
        print(f'Os Novos Estado Cadastrados:\n{Novos_Estados}')
    elif opcao == 3:
                print("===== Sub Menu =====")
                print("1 - Remover Estados de uma Região.")
                print("2 - Remover Estado Cadastrado.")
                op3 = int(input("Informe uma Opção do Sub-Menu: "))
                if op3 == 1:
                     print("==== Região ====")
                     print("Nordeste.")
                     print("Norte.")
                     print("Centro Oeste.")
                     print("Sudeste.")
                     print("Sul.")

                     regiao = str(input("Informe A região: ")).capitalize()
                     estado = str(input("Informe O Estado: ")).capitalize()

                     if regiao == 'Nordeste' and estado in Nordeste:
                        del Nordeste[estado]
                        print("Removido!")
                     elif regiao == 'Norte' and estado in Norte:
                         del Norte[estado]
                         print("Removido!")
                     elif regiao == 'Centro_oeste' and estado in Centro_oeste:
                         del Centro_oeste[estado]
                         print("Removido!")
                     elif regiao == 'Sudeste' and estado in Sudeste:
                         del Sudeste[estado]
                         print("Removido!")
                     elif regiao == 'Sul' and estado in Sul:
                         del Sul[estado]
                         print("Removido!")
                     else:
                         print(f"Estado {estado} não encontrado na região {regiao} para ser removido.")
                elif op3 == 2:
                    Estado = str(input('Informe o Nome do Estado: ')).capitalize()
                    del Novos_Estados[Estado]
                    print("Removido!")
                else:
                    print("\033[91mOpção Inválida !\nTente Novamente\033[m")
  
    elif opcao == 0:
        print("Finalizando o Site...")
        os.system('cls')
        break
        
    else:
        print("\033[91mOpção Inválida !\nTente Novamente\033[m")
