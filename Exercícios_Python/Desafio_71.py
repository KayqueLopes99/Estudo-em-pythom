# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
qtd_1 = qtd_10 = qtd_20 = qtd_50 = qtd = 0

print("-" * 30)
print(" ===== Caixa Eletrônico ===== ")
print("-" * 30)
while True:


    valor_sacado = int(input('Valor Sacado: '))
    escolha = int(input('Deseja Sair:\n1 - Sim\n2 - Não\nResposta: '))
    qtd += valor_sacado
    
    if valor_sacado >= 50:
        qtd_50 += valor_sacado // 50
        valor_sacado %= 50
    if valor_sacado >= 20:
        qtd_20 += valor_sacado // 20
        valor_sacado %= 20
    if valor_sacado >= 10:
        qtd_10 += valor_sacado // 10
        valor_sacado %= 10
    if valor_sacado > 0:
        qtd_1 += valor_sacado
    
    if escolha == 1:
        print("Saiu.")
        break

print("-" * 50)
print(f'{qtd} É o valor Gasto.')
print("-" * 50)
print(f'{qtd_1} Quantidades de Moedas de 1 Real.')
print(f'{qtd_10} Quantidades de Notas de 10 Reais.')
print(f'{qtd_20} Quantidades de Notas de 20 Reais.')
print(f'{qtd_50} Quantidades de Notas de 50 Reais.')
print("-" * 50)
