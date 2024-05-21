# Tupla
Cores = ('Azul', 'Verde', 'Amarelo', 'Vermelho', 'Rosa', 'Roxo')
Cores2 = ('Marrom', 'Preto', 'Branco', 'Laranja', 'Anil')
print('='*30)
print("\033[34m Temos Essas Cores: \033[m")
print(Cores)
print('='*30)
opcao = -1
inicio = fim = tom = 0
while True:
    print('='*30)
    print('0 - Azul')
    print('1 - Verde')
    print('2 - Amarelo')
    print('3 - Vermelho')
    print('4 - Rosa')
    print('5 - Roxo')
    print('6 - Fatiamento da Cor')
    print('7 - Usando o FOR')
    print('8 - Contagem de Cores')
    print('9 - Enumeração')
    print('10 - Impressão em Ordem')
    print('11 - Colocar no Cores com Junção')
    print('12 - Sair')
    
    print('='*30)
    opcao = int(input('Informe o número correspondente a cor válido: '))
    if 0 <= opcao <= 5:
        print(f'Escolheu a cor {Cores[opcao]}')
    elif opcao == 6:
        inicio = int(input('Informe o Inicio: '))
        fim = int(input('Informe o Fim: '))
        print(Cores[inicio:fim])
    elif opcao == 7:
    # Pode ser assim tbm.
    # for contador range(0, len(lanche)):
    #     print(lanche[contador])

        for tom in Cores:
            print(f'A Cor {tom}.')
    elif opcao == 8:
        print(f'Temos {len(Cores)} Cores.')
    elif opcao == 9:
        # ENUMERATE é um comando para colocar numeros dos indices.
        for pos, tom in enumerate(Cores):
            print(f'Cor {tom} -> Posição {pos}')
    elif opcao == 10:
        print(sorted(Cores))
    elif opcao == 11:
        cores3 = Cores + Cores2
        print(cores3)
        print(f'Temos {len(cores3)} Elementos')
    elif opcao == 12:
        print('Saindo do programa...')
        break
    else:
        print("Opção invalida.")