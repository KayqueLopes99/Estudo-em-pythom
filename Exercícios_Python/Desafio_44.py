# Elabora um programa que calcule o valor a sar pago por um produto. considerando o seu
# praço normal a condição de pagamento:
# - à vista dinheiro/chaque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão:
# praso normal -3x ou mais no cartão: 20% de juros
produto = float(input("Informe o Preço do Produto: "))

print("1- Á vista dinheiro/cheque. ")
print("2- Á vista no cartão. ")
print("3- Até 2x no cartão. ")
print("4- Até 3x ou mais vezes no cartão. ")

pagamento = int(input('Pagamento vai ser: '))

if pagamento == 1:
    pagar = produto - (produto * 0.1)
    print("Á vista dinheiro/cheque.\nTotal: {}".format(pagar))

elif pagamento == 2:
    pagar = produto - (produto * 0.05)
    print("Á vista no cartão.\nTotal: {}".format(pagar))

elif pagamento == 3:
    print("Até 2x no cartão.\nTotal: {}".format(produto))

elif pagamento == 4:
    pagar = produto + (produto * 0.2)
    print("3x ou mais no cartão.\nTotal: {}".format(pagar))

else:
    print("Invalido.")
