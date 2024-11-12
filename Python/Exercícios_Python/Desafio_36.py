# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa. o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.


print("\033[34m Empréstimo Bancário \033[m")

valor_da_casa = float(input('Informe o Valor da Casa: '))
salario = float(input('Informe o seu Salário: '))
tempo = int(input('Informe quantos anos você vai pagar todo o valor: '))

Prestacao = tempo * 12
Valor = valor_da_casa / Prestacao

if Valor <= (salario * 0.3):
    print("\033[32mValor a pagar: {:.2f} em {} Meses\033[m".format(Valor, Prestacao))
else:
    print("\033[31mEmprestimo não autorizado.\033[m")
