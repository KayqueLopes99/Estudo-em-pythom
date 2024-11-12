# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
Produtos = ('Arroz', 6.00, 'Feijão', 5.00, 'Leite', 7.50, 'Chocolate', 12.45, 'Carne', 9.50, 'Macarrão', 4.67, 'Iogute', 8.00, 'Sorvete', 14.00, 'Açai', 10.50, 'Cereal', 23.44)
# Inicio, fim , salto.
for i in range(0, len(Produtos), 2):
    produto = Produtos[i]
    preco = Produtos[i+1]
    print(f'Produto: {produto} ............... Preço: R${preco:.2f}')