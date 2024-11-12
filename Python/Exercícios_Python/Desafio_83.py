# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
expresao = str(input("Informe a Expressão Matemática: "))

for equilibrio in expresao:
    # Se o caractere é um parêntese aberto, adiciona à lista
    if equilibrio == '(':
        lista.append('(')
    # Se o caractere é um parêntese fechado
    elif equilibrio == ')':
        # Se mina lista não está vazia
        if len(lista) > 0:
            # Pop para remover o ultimo elemento
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print("Expressão Valida.")
    lista.append(expresao)
    print(lista)
else:
    print("Expressão Inválida.")
    