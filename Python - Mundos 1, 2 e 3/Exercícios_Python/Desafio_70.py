#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.
qtd_1000 = total = qtd = 0
barato = caro = 0
print("="*30)
print("Super Mercado")
print("="*30)
while True:
    produto = str(input('Informe o Nome do Produto:')).upper().strip()
    preco = float(input('Informe o Preço do Produto: '))
    escolha = int(input('Deseja Sair:\n1 - Sim\n2 - Não\nResposta: '))
    total += preco
    qtd += 1
    if preco > 1000:
        qtd_1000 += 1

    if qtd == 1:
        caro = barato = produto
   

    else:
        
        if produto > caro:
            caro = produto
           
        if produto < barato:
            barato = produto

    if escolha == 1:
        print("Saiu.")
        break
print("============ FIM ============")
print("-"*30)
print(f'{total} Gasto na Compra.')
print("-"*30)
print(f'{qtd_1000} Custam mais de 1000.')
print("-"*30)
print(f'{barato} É o produto mais Barato.')
print("-"*30)