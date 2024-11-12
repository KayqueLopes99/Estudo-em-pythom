# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista_numerica_crescente = []
while True:
    print("1 -> Cadastrar Algarismos.")
    print("2 -> Sair.")
    opcao = int(input('Informe uma opção: '))
    if opcao == 1:
        valor = int(input('Informe o Valor a ser Cadastrado: '))
        if valor not in lista_numerica_crescente:
            lista_numerica_crescente.append(valor)
        else:
            print("Valor Já na Lista.")

    elif opcao == 2:
        print("\033[35mSaindo...\033[m")
        break
    else:
        print("Informe Algo válido.")
print('-=-'*30)
lista_numerica_crescente.sort()
print(f'A lista Crescente {lista_numerica_crescente}')