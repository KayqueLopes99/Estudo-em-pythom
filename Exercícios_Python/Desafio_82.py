#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
Lista = []
pares = []
impares = []
while True:
    print("1 - Adicionar números.")
    print("0 - Sair.")
    opcao = int(input("Informe a  Opção: "))

    if opcao == 1:
                  numero = int(input("Informe o Algarismo  Para adicionar na Lista: "))
                  Lista.append(numero)
                  if numero % 2 == 0:
                          pares.append(numero)
                  else:
                        impares.append(numero)
                          
                  
    elif opcao == 0:
            print("Finalizando ...")
            break
    else:
        print("Informe Algo válido.")

print(f"Lista: {Lista}") 
print(f"Valores Pares: {pares}")
print(f"Valores Impares: {impares}")