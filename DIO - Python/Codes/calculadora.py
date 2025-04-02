"""
Exercício Calculadora
"""

try:
    num_one = input("Informe o Primeiro Número: ")
    num_two = input("Informe o Segundo Número: ")
    int_num_one = float(num_one)
    int_num_two = float(num_two)

    print(f"Soma: {int_num_one + int_num_two}")
    print(f"Subtração: {int_num_one - int_num_two}")
    print(f"Multiplicação: {int_num_one * int_num_two}")
     
    if int_num_two != 0:
       print(f"Divisão: {int_num_one / int_num_two:.2f}")
       print(f"Divisão inteira: {int_num_one // int_num_two:.2f}")
       print(f"Resto da Divisão: {int_num_one % int_num_two:.2f}")
       
    else:
       print("Erro alguma váriavel não é um valor numerico!")
    
    print(f"Potenciação: {int_num_one ** int_num_two:.2f}")



    
except ValueError:
        print("Erro: Entrada inválida! Certifique-se de digitar números.")
