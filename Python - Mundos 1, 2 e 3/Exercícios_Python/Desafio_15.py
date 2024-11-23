# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantidade KM percorrido do carro: '))
dias = int(input('Quantidade de dias de alugado: '))

custo_por_dia = 60
custo_por_km = 0.15

custo_total = (km * custo_por_km) + (dias * custo_por_dia)

print("Custo total: R${:.2f}".format(custo_total))