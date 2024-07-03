# Lista e dicionário.
import os
Brasil = list()
estado = dict()
Alagoas =  {'Uf': 'Alagoas', 'sigla': 'AL'}
Bahia = {'Uf': 'Bahia', 'sigla': 'BA'}
Ceará = {'Uf': 'Ceará', 'sigla': 'CE'}
Paraíba = {'Uf': 'Paraíba', 'sigla': 'PB'}
Pernambuco = {'Uf': 'Pernambuco', 'sigla': 'PE'}
Piauí =  {'Uf': 'Piauí', 'sigla': 'PI'}
Rio_grande_do_norte = {'Uf': 'Rio Grande do Norte', 'sigla': 'RN'}
Maranhão = {'Uf': 'Maranhão', 'sigla': 'MA'}
Sergipe = {'Uf': 'Sergipe', 'sigla': 'SE'}


Brasil.append(Alagoas)
Brasil.append(Bahia)
Brasil.append(Ceará)
Brasil.append(Paraíba)
Brasil.append(Pernambuco)
Brasil.append(Piauí)
Brasil.append(Rio_grande_do_norte)
Brasil.append(Maranhão)
Brasil.append(Sergipe)

while True:
    print("======= Menu =======")
    print("1 - Imprimir Estado.")
    print("2 - Adicionar Estados.")
    print("3 - Remover Estado.")
    print("0 - Sair.")
    opcao = int(input("Informe Uma Opção do Menu: "))


    if opcao == 1:
        print('=== Sub Menu de Estados ===')
        print("0 - Alagoas.")
        print("1 - Bahia.")
        print("2 - Ceará.")
        print("3 - Paraíba.")
        print("4 - Pernambuco.")
        print("5 - Piauí.")
        print("6 - Rio grande do norte.")
        print("7 - Maranhão.")
        print("8 - Sergipe.")
        index = int(input("Informe o número correspondete ao Estado: "))
        print(f"Informações do estado {Brasil[index]['Uf']}:\n{Brasil[index]}")
    elif opcao == 2:
        qtd = int(input("Informe quantos Estados Você Irá Adicionar: "))
        for c in range(0, qtd):
            estado['Uf'] = str(input('Unidade Federativa: ')).capitalize()
            estado['Sigla'] = str(input('Sigla: ')).upper()
            # copy() SERVE COMO FATIAMENTO E PARA NÃO DUPLICAR VALORES E INFORMAÇÕES.
            Brasil.append(estado.copy())
        print(Brasil)
    elif opcao == 3:
        print('=== Sub Menu de Estados ===')
        print("0 - Alagoas.")
        print("1 - Bahia.")
        print("2 - Ceará.")
        print("3 - Paraíba.")
        print("4 - Pernambuco.")
        print("5 - Piauí.")
        print("6 - Rio grande do norte.")
        print("7 - Maranhão.")
        print("8 - Sergipe.")
        index = int(input("Informe o número correspondete ao Estado: "))
        del Brasil[index]
        print("Removido.")

            



        
    elif opcao == 0:
        print("Finalizando o Site...")
        os.system('cls')
        break
        
    else:
        print("\033[91mOpção Inválida !\nTente Novamente\033[m")
