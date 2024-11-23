# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:                                A) Quantos números foram digitados.                             B) A lista de valores, ordenada de forma decrescente.                           C) Se o valor 5 foi digitado e está ou não na lista.
Lista = []
qtd = 0
while True:
    print("1 - Adicionar números.")
    print("0 - Sair.")
    opcao = int(input("Informe a  Opção: "))

    if opcao == 1:
                  numero = int(input("Informe o Algarismo  Para adicionar na Lista: "))
                  Lista.append(numero)
                  qtd += 1
    elif opcao == 0:
            print("Finalizando ...")
            break
    else:
        print("Informe Algo válido.")
           

print("+=+"*20)
print(f"\033[36mA lista Ilustrada: {Lista} \033[m")
print("+=+"*20)
print(f"\033[36mQuantidade de Algarismos: {qtd}\033[m")
print("+=+"*20)
print(f"\033[36mLista Ordenda em Ordem Decrescente: {Lista}\033[m")
print("+=+"*20)
if 5 not in Lista:
    print("\033[36mO valor 5 não está na lista.\033[m")
    print("+=+"*20)
else:
    print("+=+"*20)
    print("\033[36mValor 5 está na Lista.\033[m")
    print("+=+"*20)
Lista.sort(reverse=True)