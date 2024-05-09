#  Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual  será a base de conversão:

# 1 para binário
# 2 para octal
# para hexadecimal

# Em Python:
## bin(numero_decimal)[2:]
## oct(numero_decimal)[2:]
## hex(numero_decimal)[2:]

numero = int(input("Informe um número: "))

print("Escolha a Conversão: ")
print("1 -  binário")
print("2 -  Octal")
print("3 -  Hexadecimal")
opcao = int(input("Escolha: "))

if opcao == 1:
    print('\033[34mConversão em Binario \033[m')
    if numero >= 0:
        resul = bin(numero)[2:]
        print("Resultado: {}".format(resul))
    else: 
        print("Erro!")
elif opcao == 2:
    print("\033[34mConversão em Octal \033[m")
    if numero >= 0:
        resul = oct(numero)[2:]
        print("Resultado: {}".format(resul))
    else: 
        print("Erro!")
elif opcao == 3:
    print("\033[34mConversão em Hexadecimal \033[m")
    if numero >= 0:
        resul = hex(numero)[2:]
        print("Resultado: {}".format(resul))
    else: 
        print("Erro!")
