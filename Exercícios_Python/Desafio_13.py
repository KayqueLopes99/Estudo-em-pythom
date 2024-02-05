#Faça um algoritmo que leia um salario de um funcionario e mostre seu novo salario. com 15% de aumento.

salario = float(input('Informe o salario: '))

novo_salario = salario * 1.15

print('Salario: {:.2f}'.format(salario))
print('Salario com aumento: {:.2f}'.format(novo_salario))

