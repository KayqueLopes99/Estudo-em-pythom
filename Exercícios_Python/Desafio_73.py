# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
colocados = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Red Bull Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco', 'Criciúma', 'Juventude', 'Corinthians', 'Fluminense', 'Vitória', 'Atlético-GO', 'Cuiabá')

opcao = -1

while True:
    print('\033[35m========= MENU =========\033[m')
    print('1 - Primeiros Colocados.')
    print('2 - Últimos Colocados.')
    print('3 - Lista com os Times em Ordem Alfabética.')
    print('4 - Posição do Time.')
    print('5 - Sair.')
    print('\033[35m+\033[m'*25)
    opcao = int(input('Informe uma opção do Menu: '))
    if opcao == 1:
        fim = int(input('Informe o Número de Primeiros colocados: '))
        for i in range(fim):
            print(f'{i+1} Colocado: {colocados[i]}')
    elif opcao == 2:
        inicio = int(input('Informe o Número de Últimos colocados: '))
        for i in range(-inicio, 0, 1): 
            # inicio, fim, salto.
            # i começa com o valor negativo de inicio e vai incrementando até chegar em -1.
            # colocando 3, primeiro (-3 + 1 = -2 -> -2 + 1 = -1 -> -1+1 = 0 que é o fim), logo mostra os colocados 18,19,20.
            print(f'{len(colocados)+i+1} Colocado: {colocados[i]}')
    elif opcao == 3:
        print(sorted(colocados))
    elif opcao == 4:
        print(colocados)
        nome_do_time = str(input('Informe o nome do seu time: '))
        # Se o nome estiver em Times
        if nome_do_time in colocados:
            posição = colocados.index(nome_do_time) + 1 # +1 para não começar em zero.
            print(f'O {nome_do_time} está na {posição} posição.')
        else:
            print('Time não encontrado na lista.')
    elif opcao == 5:
        print("Saindo do Programa...")
        break
    else:
        print('Opção Errada.')