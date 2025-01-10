from Aula_39_package import product
# copy, sorted, produtos.sort
# deep copy -> copia tudo.
# shalow copy -> não copia tipos muaveis dentro da estrutra.
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print("Produtos com aumento de 10 % no preço:")
print(product.increase_prices_by_10_percent(products))
print("Produtos ordenados por nome (decrescente):")
print(product.sort_products_by_name(products))
print("Produtos ordenados por preço (crescente):")
print(product.sort_products_by_price(products))

