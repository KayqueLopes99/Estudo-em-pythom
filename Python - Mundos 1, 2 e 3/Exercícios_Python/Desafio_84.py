# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas 
# C) Uma listagem com as pessoas mais leves.
mais_peso = menos_peso = 0 
Lista_Oficial = []
Lista_armazenador_leves = [] 
Lista_armazenador_pesado = [] 
while True:
    print("++++++ Menu +++++++")
    print("1 - Cadastrar Pessoas.")
    print("0 - Sair.")
    opção = int(input("Informe Uma opção do Menu: "))

    if opção == 1:
        quantidade = int(input("Informe A Quantidade de pessoas que você deseja inserir: "))
        for c in range(0,quantidade):
            
            pessoa = str(input("Informe o Nome de Pessoa: "))
            peso = float(input("Informe a Peso da pessoa: "))

            # Crie uma lista temporária.
            Primeira_lista = [pessoa, peso]
            Lista_Oficial.append(Primeira_lista)  
            # Adicione a lista.

            if c == 0:
                menos_peso = mais_peso = peso
            else:
                if peso > mais_peso:
                    mais_peso = peso
                elif peso < menos_peso:
                    menos_peso = peso

    elif opção == 0:
        print("Saindo...")
        break
    else:
        print("\033[35mInforme Algo Valido\033[m")

print("Informações Adicionada com Sucesso!")
print(f'Lista de Pessoas Cadastradas e seus Dados:\n{Lista_Oficial}\nQuantidade de Usuário Cadastrados: {len(Lista_Oficial)}')
print(f"Maior Peso foi: {mais_peso}Kg do(s) Usuários ", end='')
for p in Lista_Oficial:
    if p[1] == mais_peso:
        print(f'{p[0]} ', end='')# O end é para fazer uma Ligação nos print.
print()# Quebrar a linha com uso do end
print(f"Peso mais leve: {menos_peso}Kg do(s) Usuários ", end='')
for p in Lista_Oficial:
    if p[1] == menos_peso:
        print(f'{p[0]} ', end='')# O end é para fazer uma Ligação nos print.
print()# Quebrar a linha com uso do end