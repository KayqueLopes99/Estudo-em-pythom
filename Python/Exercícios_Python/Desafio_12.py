#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

nome = str(input('Informe o nome do produto: '))
preco = float(input('Informe o preço do produto: '))

print('Nome: {}'.format(nome))
print('Preço: {:.2f}'.format(preco))

desconto = preco * 0.05
preco_com_desconto = preco - desconto

print('Desconto de 5%: {:.2f}'.format(desconto))
print('Preço com desconto: {:.2f}'.format(preco_com_desconto))

