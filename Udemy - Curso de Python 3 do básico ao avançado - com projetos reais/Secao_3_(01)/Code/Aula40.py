# Exercício guiado - Calculadora -
"""
 Calculadora com while 
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None <- não saõ validos

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True <- são validos
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break 

"""

## Solução(Pessoal):
while True:
    print("-" * 27)
    print("------- Calculadora -------")
    print("-" * 27)

    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input("Informe o operador (+, -, *, /): ")

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        print("Apenas números válidos (inteiros ou decimais) são permitidos.")
        continue  # Voltar ao início do loop

    num_1_float = float(numero_1)
    num_2_float = float(numero_2)

    
    if operador not in '+-*/':
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
        
    print("------ RESULTADO ABAIXO -------")

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f"A Soma entre {num_1_float} e {num_2_float}: {soma}")
    elif operador == "-":
        subtracao = num_1_float - num_2_float
        print(f"A Subtração entre {num_1_float} e {num_2_float}: {subtracao}")
    elif operador == "*":
        multiplicacao = num_1_float * num_2_float
        print(f"A Multiplicação entre {num_1_float} e {num_2_float}: {multiplicacao}")
    elif operador == "/":
        divisao = num_1_float / num_2_float
        print(f"A Divisão entre {num_1_float} e {num_2_float}: {divisao}")
    else:
        print("ERRO!")

    op = input("[s] = Sair || [n] = Continuar: ").lower()
    if op == 's':
        print("Saindo...")
        break
print("-" * 27)