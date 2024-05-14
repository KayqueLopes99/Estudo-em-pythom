# Menu com opções.
'''
 Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
valor1 = int(input('Informe o Primeiro valor: '))
valor2 = int(input('Informe o Segundo valor: '))

opcao = 0
while opcao != 5:
    print('===== Menu =====')
    print("[1] = Somar ")
    print("[2] = Multiplicar ")
    print("[3] = Maior ")
    print("[4] = Novos Numeros ")
    print("[5] = Sair ")
    opcao = int(input("Informe a Opção: "))
    while opcao < 1 or opcao > 5:
        opcao = int(input("Informe uma Opção válida: "))
    if opcao == 1:
        soma = valor1 + valor2
        print("Soma: {}".format(soma))
    elif opcao == 2:
        multi = valor1 * valor2
        print("Multiplicar: {}".format(multi))
    elif opcao == 3:
        if valor2 > valor1:
            print("O Segundo Valor {} é maior".format(valor2))
        else:
            print("O Primeiro Valor {} é maior".format(valor1))
    elif opcao == 4:
        print('Novos números')
        valor1 = int(input('Informe outro Primeiro valor: '))
        valor2 = int(input('Informe outro Segundo valor: '))
    else:
        print("Saiu!!!")
