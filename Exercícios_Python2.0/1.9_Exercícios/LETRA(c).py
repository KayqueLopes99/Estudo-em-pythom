# Considere a fórmula para cálculo de juros simples, J = (C × I × T) / 100, onde J, C, I e T correspondem a juros, capital, taxa e tempo, respectivamente. Construa um código que solicite ao usuário os valores de C, I e T e calcule J.

T = int(input('Informe o Tempo: '))
C = int(input('Informe o Capital: '))
I = int(input('Informe os Taxa: '))

J = (C * I * T)/100

print("Total dos Juros: {}".format(J))
