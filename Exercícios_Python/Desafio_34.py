# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$ 1250.00, calcule um aumento de 10¨%.

# Para inferiores ou iguais. O aumento é de 15%.

salario = float(input('Informe seu salário: '))

if salario > 1250:
    aumento = salario + (salario* 0.1)
else:
    aumento = salario + (salario* 0.15)

print("Salário com aumento: {}".format(aumento))