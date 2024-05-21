# Tupla
Cores = ('Azul', 'Verde', 'Amarelo', 'Vermelho', 'Rosa', 'Roxo')
print('='*30)
print("\033[34m Temos Essas Cores: \033[m")
print(Cores)
print('='*30)
opcao = -1
inicio = fim = 0
while True:
    print('='*30)
    print('0 - Azul')
    print('1 - Verde')
    print('2 - Amarelo')
    print('3 - Vermelho')
    print('4 - Rosa')
    print('5 - Roxo')
    print('6 - Fatiamento da Cor')
    print('7 - Sair')
    
    print('='*30)
    opcao = int(input('Informe o número correspondente a cor válido: '))
    if 0 <= opcao <= 5:
        print(f'Escolheu a cor {Cores[opcao]}')
    elif opcao == 6:
        inicio = int(input('Informe o Inicio: '))
        fim = int(input('Informe o Fim: '))
        print(Cores[inicio:fim])
    elif opcao == 7:
        print('Saindo do programa...')
        break
    else:
        print("Opção invalida.")